---
name: readable-explainers
description: "Evidence-based method for writing and laying out explanatory content people can actually read, understand and remember (explainers, guides, long-form pages, study notes, teaching docs, onboarding docs, summaries of complex topics). Use this whenever the user asks to explain, teach, summarize, digest, make something easier to read or understand, make it stick, build intuition, or produce any text longer than a few paragraphs meant to be learned from, even if they never say readability. Also use it when asked to improve or restructure an existing article, page or doc for comprehension."
---

# Readable Explainers

You are writing for a person who wants to understand something and still have it three weeks later. Two facts drive everything below. First, typography and layout only remove friction; they barely change what is remembered. Second, what changes memory is what the reader is made to *do*: guess, retrieve, explain, compare. So the skill has two layers, and the learning layer matters more than the reading layer.

Use this skill for the substance and structure of the writing. For diagrams, figures and animation inside the piece, pair it with the `explanatory-visuals` skill.

## The core stance

Before writing, answer three questions and keep the answers in front of you:

1. **What is the one idea?** If the reader forgets everything else, what should survive? Write it as one sentence. Every section should be traceable to it.
2. **What are the three to seven facts I most want remembered?** Those are the ones that get a pre-question, a retrieval check, or both. Everything else is supporting cast.
3. **Who is reading and what do they already know?** Pre-knowledge decides how much "cast of characters" you need and whether analogies help or condescend.

## Layer 1: structure that survives scanning

Most readers scan; eye-tracking studies find people read roughly a quarter of the words on a long page, and attention decays steeply down the page. Design so a scanner still gets the idea and a reader gets the depth.

**Front-load at every level.** Page: an advance organizer at the very top, before any table of contents (the whole idea in ~120 words, then "on this page" with time estimates per section). Section: a one-sentence bottom line right under the heading. Paragraph: the point in the first sentence.

**Headings state the claim, not the topic.** "Radiotherapy breaks DNA in every cell it touches, and bets the tumour repairs it worst" beats "Radiotherapy". Meaningful headings measurably improve recall and search; labels do not. Put the key word in the first two words of the heading.

**One idea per paragraph, two to four sentences, sentences under 25 words.** Comprehension falls off a cliff past ~40-word sentences. If a paragraph passes 150 words on screen, split it or put a figure between the halves.

**Bullets for parallel lists; prose for causal reasoning.** Bullets strip out "because" and "so", and those connectives are what carry a mechanism. Keep bullets under seven items and front-load each.

**Same skeleton for every repeated unit.** If you explain seven things, use the identical sub-structure for each (heading claim → one-liner → guess-first → how it works → steps → analogy → where it shines / where it fails → check yourself). Consistency lets the reader stop re-orienting and spend attention on content.

**Never hide the main explanation.** Accordions and "click to expand" hurt when they hold required content; readers miss it and can't search it. Use collapsed elements only for optional depth and for answers the reader is meant to guess first.

**Navigation for long pieces.** A labelled "on this page" list, a sticky bar that shows the current section, and a thin progress indicator. Section-level time estimates are more useful than a whole-page reading time.

## Layer 2: techniques that change what is remembered

Ranked by the strength of evidence. The first three are the ones to fight for when space is tight.

**1. Retrieval practice.** End each major unit with two or three questions the reader answers from memory before revealing the answer, and end the piece with a mixed quiz (8–10 items) that makes the reader discriminate between the things just learned. Practice testing outranks every other study technique in the literature (Dunlosky 2013; Adesope 2017), and it also corrects the overconfidence people have when reading on screens. Feedback must be immediate. Questions target the mechanism ("why does X spare healthy cells?"), never trivia.

**2. Pre-questions ("guess first").** Open each unit with one question whose answer is the fact you most want remembered, and make the reader commit before reading. Guessing, even wrongly, roughly doubles memory for that specific answer (prequestion meta-analysis 2023, g = 0.54). It does not help facts you didn't ask about, so aim it.

**3. Spacing.** Tell the reader to return to the quiz in a few days, and revisit core concepts in later sections rather than fully in one place. Distributed practice is the second-best-evidenced technique and the cheapest to add.

**4. Pre-training: the cast of characters.** Before the mechanism, name the parts. A short "meet the pieces" block (five to eight named components, one line each, with the same icon that appears in every later figure) frees working memory for the interactions. Mayer's pre-training effect is one of the most replicated in multimedia learning.

**5. Segmenting with numbered steps.** Break each mechanism into three to seven steps, numbered in the text and matching numbered markers in the figure. Discrete, learner-paced steps beat continuous prose or continuous animation for processes.

**6. Concrete before abstract, then fade.** Start with one specific case (a named drug, one patient, one transaction), then the general principle, then the class. Walk through one full worked example before asking the reader to reason about another.

**7. Analogies that map, and say where they break.** An analogy works when its parts correspond structurally to the real thing, not when it is vivid. Every analogy gets a one-line "where it breaks" so the reader doesn't carry the wrong part over.

**8. Self-explanation and elaborative "why".** Phrase transitions as why-questions and answer them. Occasionally ask the reader to explain a step in their own words before moving on.

**9. Conversational second person.** "Your cells", "you might wonder why". Personalized style improves transfer (d ≈ 0.5) without being chatty.

**10. Signal sparingly.** Bold only the first use of a key term, one to three per section. Over-signalling erases the effect. Do not add features that let readers highlight; learner highlighting is a low-utility technique.

**11. Summaries at start and end.** An advance organizer at the top, a short recap (three to seven "things to keep") at the end. Position matters less than presence.

**12. Narrative thread.** Where the content allows, frame sections as problem → attempt → why it failed → what worked. Stories are remembered better than essays (g ≈ 0.5), as long as the mechanism content stays intact inside them.

## Layer 3: the reading surface

These remove friction. Apply them all; none of them substitutes for Layer 2.

- Body text 17–19 px on screen (never under 16), line height 1.5–1.6, measure 55–70 characters (`max-width: 62ch`), left-aligned, ragged right. Paragraph spacing about one line.
- Contrast at least 7:1 for body text; dark grey on off-white rather than pure black on pure white. Light mode as default; offer a dark toggle. Dark-on-light reads more accurately for most people.
- One display face, one body face, one utility face at most. Serif versus sans makes no reliable difference; rendering quality and x-height do. Letter-space small uppercase labels (+5–12%); never letter-space lowercase.
- Give the reader controls: text size steps, theme toggle, remembered between visits. Provide a print stylesheet; paper still beats screens for informational text in the meta-analyses.
- On phones, comprehension of dense text roughly halves: shorter paragraphs, every figure fits one viewport, definitions inline rather than in a distant glossary.
- Do not use "Bionic Reading" (bolded word-starts): it fails every controlled test. Do not use hard-to-read fonts as a "desirable difficulty": that finding failed to replicate across 17 studies. Do not interleave the prose itself; interleaving helps discrimination quizzes, not expository text.

## Working with figures

Words and a relevant picture together beat words alone by a wide margin (d ≈ 0.7–1.3), but only when the picture shows the mechanism and sits next to the words that explain it. Put the figure in the same viewport as its paragraph, label inside the figure rather than in a legend, give the caption the takeaway rather than a description, and match step numbers between text and picture. On narrow screens, place the figure immediately after the steps it illustrates, before the analogy and details, and make the mechanism figure fit a phone viewport by simplifying or stacking it rather than by sideways scrolling; a figure the reader has to pan is a figure they skip. Draw the figures with the `explanatory-visuals` skill.

## Process

1. Write the one idea, the memorable facts, and the reader profile (the three questions above).
2. Draft the advance organizer and the "on this page" list first; they are the outline.
3. Draft the cast of characters if the reader will meet more than four unfamiliar parts.
4. Write each unit on the shared skeleton. For each, write the pre-question and the two check questions *before* the prose, so the prose is written to answer them.
5. Pass for scanning: heading claims, first-sentence points, paragraph length, sentence length.
6. Pass for signalling: strip bold down to first-use key terms; strip anything that is interesting but irrelevant to the claim (seductive details reliably hurt retention).
7. Add the end quiz with feedback and the "come back in three days" line. If the reader gave a length target, the questions and quiz count toward it; trim supporting prose before trimming retrieval.
8. Apply the reading surface, test at phone width and in dark mode, add controls and print styles.

## Checklist before shipping

- One-sentence idea at the top; every section traceable to it.
- Every unit opens with a committed guess and closes with two retrieval questions with answers.
- A mixed end quiz with immediate feedback and a spacing prompt.
- Cast of characters precedes the first mechanism, with icons reused in every figure.
- Headings are claims; first sentences carry the point; paragraphs ≤ 4 sentences; sentences ≤ 25 words.
- Steps numbered in text and figure alike; figure in the same viewport as its text; caption states the takeaway.
- Every analogy has a "where it breaks".
- Bold limited to first-use key terms; no decorative asides inside mechanism sections.
- No required content hidden in accordions.
- 17–19 px body, ≤ 70-character measure, 1.5–1.6 line height, ≥ 7:1 contrast, light default with dark option, text-size control, print stylesheet, phone-width check.

## Evidence base (for when you need to justify a choice)

- Practice testing and distributed practice rated highest utility; rereading, highlighting, summarising rated low: Dunlosky et al. 2013, *Psychological Science in the Public Interest*; Adesope et al. 2017 meta-analysis of practice testing.
- Pre-questions: 2023 meta-analysis (97 studies), g = 0.54 on questioned content, ~0 on unquestioned; Kang et al. 2009 on curiosity and wrong guesses.
- Spacing: Cepeda et al. 2006 (317 experiments).
- Mayer's multimedia principles (spatial contiguity d ≈ 1.1, coherence d ≈ 0.86, segmenting d ≈ 0.8, pre-training d ≈ 0.75, signalling d ≈ 0.4, personalization d ≈ 0.3–0.5): Cambridge Handbook of Multimedia Learning; Ginns 2013 on conversational style; Schroeder & Cenkci 2018 on contiguity.
- Seductive details hurt retention: Sundararajan & Adesope 2020 meta-analysis.
- Self-explanation g = 0.55: Bisra et al. 2018. Generation effect d = 0.4: Bertsch et al. 2007. Worked examples g = 0.48 for novices: Barbieri et al. 2023. Concreteness fading: Fyfe et al. 2014.
- Narrative vs expository memory g = 0.55: Mar et al. 2021.
- Informative headings improve recall: Hartley & Trueman 1983; Lorch 1989 review of text signals.
- Scanning, F-pattern, 20–28% of words read, attention decay down the page, accordions, sticky headers, mobile comprehension halving: Nielsen Norman Group eye-tracking and usability studies.
- Line length 45–75 characters, readers prefer ~55; font size fluent range; positive polarity (dark on light) advantage; Larson & Picard 2006 on good typography improving mood and problem-solving; SURL 2004 on whitespace improving comprehension: Dyson 2004 review, Legge & Bigelow 2011, Piepenbrock et al. 2013.
- Bionic Reading no effect: Readwise n = 1,916; Snell 2024. Disfluent fonts failed replication: Wetzler 2021 and others.
- Screens worse than paper for informational reading (g ≈ −0.2 to −0.27) and screen overconfidence: Delgado et al. 2018; Clinton 2019.
- Sentence length limits: GOV.UK content design research (25 words); interleaving does not help expository text: Brunmair & Richter 2019.
