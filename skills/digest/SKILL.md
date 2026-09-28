---
name: digest
description: "Use when the user runs /digest, or asks for a digest, explainer or learning page on one or more topics, URLs or files (\"digest X\", \"explain these 3 things\", \"make me a study page on Y\", \"compare A vs B so I remember it\"). Do NOT use for a quick chat answer, or for polishing a single existing figure (use explanatory-visuals alone)."
argument-hint: "<topic | url | file> [; <topic> ...] [--compare]"
---

# Digest

Topics: $ARGUMENTS (outside Claude Code: whatever topics the user gave)

Turn each topic into an explainer people understand and still remember weeks later, by running two skills together:
- **readable-explainers** — the words: structure, pre-questions, retrieval checks, end quiz, reading surface.
- **explanatory-visuals** — the figures: one claim per figure, mechanism with numbered steps, labels on the figure.

Load both skills before writing anything. They are the spec; this skill only orchestrates.

## 1. Parse the topics

- Split on `;` or newlines. Each item is a topic, a URL, or a local file path.
- Nothing given → ask for the topic(s) and stop.
- `--compare` (or the user asks to compare) → one combined explainer that contrasts the topics: side-by-side / 2×2 figures, a mixed quiz that makes the reader tell them apart. Otherwise each topic gets its own explainer.

## 2. Gather sources

- URL → fetch it. File → read it. Bare topic → research it (web search, official docs, the repo if it's about code).
- Keep a short source list per topic and cite it at the bottom of the explainer.

## 3. Build each explainer

Follow the readable-explainers **Process** end to end (one idea, 3–7 memorable facts, reader profile → advance organizer → cast of characters → shared unit skeleton → end quiz + spacing prompt). Every mechanism unit gets a figure built with explanatory-visuals and passes its checklist.

Output one self-contained HTML page per explainer (inline SVG, no external assets beyond fonts):
- Artifact/publish tool available → publish it and return the link.
- Otherwise → write `./digests/<topic-slug>.html` and return the path.

## 4. Several topics → parallel

With 2+ topics and no `--compare`, dispatch one subagent per topic, all in a single message. Give each its topic, its sources, and the instruction to load both skills and follow step 3. Then reply with a short index: topic → one-sentence idea → link/path.

## Done when

Every explainer passes both skills' "Checklist before shipping", and the user has a link or path for each topic.
