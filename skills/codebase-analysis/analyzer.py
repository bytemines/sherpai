#!/usr/bin/env python3
"""
Codebase Analyzer - Scans codebase and outputs structured JSON or ASCII report.

Usage:
    python analyzer.py [--root PATH] [--scope PATH...] [--threshold LINES] [--ascii]
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Tuple
from collections import defaultdict


# ═══════════════════════════════════════════════════════════════════════════
# CONFIG — All settings defined here. No external files.
# ═══════════════════════════════════════════════════════════════════════════

THRESHOLD_SHOULD_REFACTOR = 500
THRESHOLD_URGENT_REFACTOR = 800
THRESHOLD_CRITICAL = 1000

SCORE_MAX = 100

PENALTY_SIZE = [
    (1000, 30),  # >1000 lines → -30
    (500,  20),  # >500  lines → -20
    (200,  10),  # >200  lines → -10
]

PENALTY_COMPLEXITY = [
    (20, 25),  # >20 keywords → -25
    (10, 15),  # >10 keywords → -15
    (5,   5),  # >5  keywords → -5
]

PENALTY_IMPORTS = [
    (15, 15),  # >15 imports → -15
    (8,  10),  # >8  imports → -10
    (5,   5),  # >5  imports → -5
]

CATEGORIES = {
    "keep":     {"min_score": 80, "icon": "+", "bar": "="},
    "minor":    {"min_score": 60, "icon": "~", "bar": "-"},
    "refactor": {"min_score": 40, "icon": "!", "bar": "#"},
    "urgent":   {"min_score": 0,  "icon": "X", "bar": "X"},
}

EXCLUDE_PATTERNS = [
    "node_modules", ".git", "__pycache__", "dist", "build", ".next",
    "target", "bin", "obj", ".venv", "venv", "env", ".env",
    "cache", ".cache", "coverage", ".pytest_cache", ".mypy_cache",
    "site-packages", "*.egg-info", ".npm", ".yarn", "bower_components",
    "vendor", "third_party", "3rdparty", "*generated*", "*.gen.*",
    "protobuf", "typings", "@types",
]

LANGUAGES = {
    "python":     {"ext": [".py"],        "max": 500, "kw": ["def", "class", "if", "elif", "else", "for", "while", "try", "except", "with"]},
    "typescript": {"ext": [".ts", ".tsx"], "max": 300, "kw": ["function", "class", "if", "else", "for", "while", "try", "catch", "switch"]},
    "javascript": {"ext": [".js", ".jsx"], "max": 300, "kw": ["function", "class", "if", "else", "for", "while", "try", "catch", "switch"]},
    "rust":       {"ext": [".rs"],         "max": 400, "kw": ["fn", "struct", "impl", "if", "else", "for", "while", "match"]},
    "go":         {"ext": [".go"],         "max": 400, "kw": ["func", "type", "struct", "interface", "if", "else", "for", "range"]},
}

MONOREPO_INDICATORS = ["packages", "apps", "workspaces", "services", "modules"]

PROJECT_MARKERS = {
    "Cargo.toml":    ("rust", "rust"),
    "package.json":  ("node", "typescript"),
    "pyproject.toml": ("python", "python"),
    "setup.py":      ("python", "python"),
    "go.mod":        ("go", "go"),
}


# ═══════════════════════════════════════════════════════════════════════════
# ANALYZER
# ═══════════════════════════════════════════════════════════════════════════

class CodebaseAnalyzer:
    def __init__(self, root_dir: str, scopes: List[str] = None, threshold: int = 200):
        self.root_dir = Path(root_dir).resolve()
        self.threshold = threshold
        self.scopes = scopes or []
        self.project_info = self._detect_project()

    def _detect_project(self) -> Dict[str, Any]:
        ptype, lang = "unknown", "unknown"
        structure = "single-repo"

        for marker, (pt, ln) in PROJECT_MARKERS.items():
            if (self.root_dir / marker).exists():
                ptype, lang = pt, ln
                break

        for ind in MONOREPO_INDICATORS:
            if (self.root_dir / ind).is_dir():
                structure = "monorepo"
                break

        return {"type": ptype, "structure": structure, "primary_language": lang,
                "name": self.root_dir.name, "root": str(self.root_dir)}

    def _should_exclude(self, path: Path) -> bool:
        path_str = str(path)
        return any(p.replace("*", "") in path_str for p in EXCLUDE_PATTERNS)

    def _detect_language(self, fp: Path) -> str:
        for lang, cfg in LANGUAGES.items():
            if fp.suffix in cfg["ext"]:
                return lang
        return "unknown"

    def _count_keywords(self, content: str, language: str) -> Dict[str, int]:
        if language not in LANGUAGES:
            return {"total": 0}
        counts = {}
        for kw in LANGUAGES[language]["kw"]:
            counts[kw] = content.count(f" {kw} ") + content.count(f"{kw}(")
        counts["total"] = sum(counts.values())
        return counts

    def _detect_scope(self, fp: Path) -> str:
        rel = fp.relative_to(self.root_dir)
        for scope in self.scopes:
            sp = Path(scope)
            if sp in rel.parents or rel == sp:
                return str(sp)
        if self.project_info["structure"] == "monorepo":
            for ind in MONOREPO_INDICATORS:
                ind_path = self.root_dir / ind
                if ind_path.exists():
                    try:
                        r = fp.relative_to(ind_path)
                        if r.parts:
                            return f"{ind}/{r.parts[0]}"
                    except ValueError:
                        pass
        return rel.parts[0] if len(rel.parts) > 1 else "root"

    @staticmethod
    def _calc_penalty(value: int, table: List[Tuple[int, int]]) -> int:
        for threshold, penalty in table:
            if value > threshold:
                return penalty
        return 0

    def _calculate_score(self, fdata: Dict) -> int:
        score = SCORE_MAX
        score -= self._calc_penalty(fdata["lines"], PENALTY_SIZE)
        score -= self._calc_penalty(fdata["keywords"].get("total", 0), PENALTY_COMPLEXITY)
        score -= self._calc_penalty(fdata["import_count"], PENALTY_IMPORTS)
        return max(0, score)

    @staticmethod
    def _get_category(score: int) -> Tuple[str, str, str]:
        for name, cfg in CATEGORIES.items():
            if score >= cfg["min_score"]:
                return name, cfg["icon"], cfg["bar"]
        return "urgent", "X", "X"

    def _analyze_file(self, fp: Path) -> Dict[str, Any] | None:
        try:
            content = fp.read_text(encoding="utf-8", errors="ignore")
            lines = content.count("\n") + 1
            language = self._detect_language(fp)
            keywords = self._count_keywords(content, language)

            import_count = 0
            for line in content.split("\n")[:100]:
                s = line.strip()
                if any(s.startswith(p) for p in ["import ", "from ", "require(", "import {"]):
                    import_count += 1

            return {"path": str(fp.relative_to(self.root_dir)), "lines": lines,
                    "language": language, "keywords": keywords,
                    "import_count": import_count, "scope": self._detect_scope(fp)}
        except Exception:
            return None

    def scan(self) -> Dict[str, Any]:
        files = []
        total = 0

        for fp in self.root_dir.rglob("*"):
            if not fp.is_file() or self._should_exclude(fp):
                continue
            if self._detect_language(fp) == "unknown":
                continue
            total += 1
            data = self._analyze_file(fp)
            if data and data["lines"] >= self.threshold:
                data["score"] = self._calculate_score(data)
                cat, icon, bar = self._get_category(data["score"])
                data["category"] = cat
                data["icon"] = icon
                data["bar_char"] = bar
                files.append(data)

        files.sort(key=lambda x: x["lines"], reverse=True)

        scopes = defaultdict(list)
        for f in files:
            scopes[f["scope"]].append(f)

        by_cat = defaultdict(int)
        by_lang = defaultdict(int)
        for f in files:
            by_cat[f["category"]] += 1
            by_lang[f["language"]] += 1

        return {
            "project": self.project_info,
            "summary": {
                "total_scanned": total,
                "files_above_threshold": len(files),
                "threshold": self.threshold,
                "by_category": dict(by_cat),
                "by_language": dict(by_lang),
            },
            "files": files,
            "scopes": {
                s: {"file_count": len(fs),
                    "total_lines": sum(f["lines"] for f in fs),
                    "avg_lines": sum(f["lines"] for f in fs) // max(len(fs), 1),
                    "max_lines": max((f["lines"] for f in fs), default=0),
                    "files": [f["path"] for f in fs]}
                for s, fs in scopes.items()
            },
        }


# ═══════════════════════════════════════════════════════════════════════════
# ASCII REPORT
# ═══════════════════════════════════════════════════════════════════════════

W = 72  # report width


def _hline(ch="─"):
    print(ch * W)


def _banner(text):
    _hline("═")
    pad = (W - len(text) - 4) // 2
    print(f"║{' ' * pad} {text} {' ' * (W - pad - len(text) - 4)}║")
    _hline("═")


def print_ascii_report(r: Dict) -> None:
    proj = r["project"]
    summ = r["summary"]
    files = r["files"]
    scopes = r["scopes"]

    print()
    _banner("CODEBASE ANALYSIS")
    print()
    print(f"  Project : {proj['name']}")
    print(f"  Type    : {proj['type']}  |  Structure: {proj['structure']}")
    print(f"  Language: {proj['primary_language']}")
    print(f"  Root    : {proj['root']}")
    print()

    # ── Summary ──
    _hline()
    print(f"  Scanned {summ['total_scanned']} files  |  "
          f"{summ['files_above_threshold']} above {summ['threshold']}-line threshold")
    _hline()
    print()

    # ── Health bar ──
    cats = summ.get("by_category", {})
    total = max(summ["files_above_threshold"], 1)
    cat_order = ["urgent", "refactor", "minor", "keep"]
    cat_labels = {"urgent": "URGENT", "refactor": "REFACTOR", "minor": "MINOR", "keep": "OK"}
    cat_chars = {n: CATEGORIES[n]["bar"] for n in cat_order}

    print("  Health Distribution:")
    print()
    bw = W - 4
    bar = ""
    for c in cat_order:
        cnt = cats.get(c, 0)
        bar += cat_chars[c] * max(0, int((cnt / total) * bw))
    print(f"  [{bar[:bw].ljust(bw)}]")
    print()
    legend = "  ".join(
        f"  {cat_chars[c]} {cat_labels[c]}: {cats.get(c, 0)} ({int(cats.get(c, 0) / total * 100)}%)"
        for c in cat_order if cats.get(c, 0)
    )
    print(legend)
    print()

    # ── Top files bar chart ──
    _hline()
    print("  Largest Files:")
    _hline()
    print()

    top = files[:15]
    if top:
        mx = top[0]["lines"]
        mpl = min(max(len(f["path"]) for f in top), 40)
        bs = W - mpl - 18

        for f in top:
            p = f["path"]
            if len(p) > mpl:
                p = "..." + p[-(mpl - 3):]
            bl = max(1, int((f["lines"] / mx) * bs))
            print(f"  {f['icon']} {p.ljust(mpl)} {f['lines']:>5} |{f['bar_char'] * bl}")
    print()

    # ── Scopes ──
    _hline()
    print("  Scope Breakdown:")
    _hline()
    print()

    slist = sorted(scopes.items(), key=lambda x: x[1]["total_lines"], reverse=True)
    if slist:
        msl = slist[0][1]["total_lines"] or 1
        mnl = min(max(len(s) for s, _ in slist), 25)
        bs = W - mnl - 22
        for sn, sd in slist:
            n = sn[:mnl - 2] + ".." if len(sn) > mnl else sn
            bl = max(1, int((sd["total_lines"] / msl) * bs))
            print(f"  {n.ljust(mnl)} {sd['file_count']:>3} files |{'=' * bl}| {sd['total_lines']} ln")
    print()

    # ── Languages ──
    langs = summ.get("by_language", {})
    if langs:
        _hline()
        print("  Languages:")
        _hline()
        print()
        tl = max(sum(langs.values()), 1)
        for lang, cnt in sorted(langs.items(), key=lambda x: -x[1]):
            pct = int(cnt / tl * 100)
            print(f"  {lang:<12} {cnt:>4} files  {pct:>3}%  {'#' * (pct // 2)}")
        print()

    # ── Score scatter ──
    if files:
        _hline()
        print("  Score Map (score vs size):")
        _hline()
        print()

        ROWS, COLS = 12, 50
        grid = [[" "] * COLS for _ in range(ROWS)]
        ml = max(f["lines"] for f in files)

        for f in files:
            col = min(int(f["score"] / 100 * (COLS - 1)), COLS - 1)
            row = ROWS - 1 - min(int(f["lines"] / ml * (ROWS - 1)), ROWS - 1)
            grid[row][col] = f["icon"]

        for i, row in enumerate(grid):
            lbl = f"{ml:>5}" if i == 0 else (f"{files[-1]['lines']:>5}" if i == ROWS - 1 else "     ")
            print(f"  {lbl} |{''.join(row)}|")
        print(f"        +{'-' * COLS}+")
        print(f"        0{'score':^{COLS - 3}}100")
        print()
        print("  Legend: + ok   ~ minor   ! refactor   X urgent")
        print()


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Codebase Analyzer")
    parser.add_argument("--root", default=".", help="Root directory")
    parser.add_argument("--scope", nargs="+", help="Specific scopes")
    parser.add_argument("--threshold", type=int, default=200, help="Min lines (default: 200)")
    parser.add_argument("--ascii", action="store_true", help="ASCII report instead of JSON")
    args = parser.parse_args()

    analyzer = CodebaseAnalyzer(args.root, scopes=args.scope or [], threshold=args.threshold)
    results = analyzer.scan()

    if args.ascii:
        print_ascii_report(results)
    else:
        for f in results["files"]:
            f.pop("bar_char", None)
            f.pop("icon", None)
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
