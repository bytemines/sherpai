---
name: explanatory-visuals
description: "How to design diagrams, figures and UI-quality illustrations that make a mechanism, process, system or comparison understandable, look visually harmonious, and use motion only where it helps. Use this whenever the user asks for a diagram, figure, illustration, infographic, schematic, visual explanation, show how it works, make it visual, animated or interactive explainer, step-by-step picture, before/after, comparison map, timeline, or any inline SVG/HTML/CSS graphic in a page, doc or slide, even when they only say make it look nice or add some movement. Also use it to review or polish an existing figure."
---

# Explanatory Visuals

A figure earns its place when a cold reader can see a mechanism they would otherwise have to assemble from prose. Everything here serves that: pick the right kind of picture, draw the parts that the claim hinges on, make it look like one designer made it, and move only what needs to move. The research is unusually clear on this domain, and the effects are large: text-plus-diagram designs show the strongest gains of any medium, and the same studies show that decoration actively hurts.

Pair this skill with `readable-explainers` for the words around the figure.

## Step 1: decide what the picture is for

Write the figure's claim as one sentence before drawing. If it needs two sentences, you need two figures. Then pick the archetype whose natural reading matches the claim. People read diagrams with built-in mappings (Tversky): dots are things, lines are relations, boxes are containment, arrows are asymmetric relations (cause, sequence, motion), left→right is time, up is more, near is related, central and large is important. Use those mappings; violating them is the main way diagrams mislead.

| The claim is… | Draw a… | Layout rule |
|---|---|---|
| A leads to B leads to C | flow / process | one direction only, left→right or top→down, arrows with heads |
| …and returns to the start | cycle | clockwise from 12 o'clock; label what drives the loop |
| X sits on / depends on Y | layered stack | foundation at the bottom; equal heights unless height means something |
| is-a / part-of / reports-to | tree | root at top or left; siblings aligned; ≤ 3–4 levels visible |
| the change is… | before / after | identical framing both sides; only the changed thing differs |
| A vs B on the same dimensions | side-by-side | same rows in the same order; shared axis |
| two independent dimensions define regimes | 2×2 map | label the axis *poles*; place named examples in quadrants |
| when, in order | timeline | time on x, to scale or labelled "not to scale" |
| what are the parts | anatomy / exploded view | numbered callouts; parts in real spatial relation |
| how it works | mechanism with numbered steps | numbers on the figure match numbers in the text; ≤ 7 steps |

**Show the mechanism, not the label.** A box that says "cache" says less than the prose. The path a request takes through it, the two stores it sits between, and the arrow that disappears when the cache is removed say what words can't. Comparing options? Draw the difference: the one edge each option adds or removes, side by side in identical frames.

**Parts before process.** If the reader won't recognise the components, show an anatomy panel (or label the parts in step 1) before the mechanism. Then reuse exactly those shapes.

**Arrows make it a mechanism.** Adding arrows to a structural diagram nearly doubles the number of functional ("this does that") descriptions readers produce. So arrows mean only direction, sequence, cause, motion or force, and each carries what it does or what moves along it ("compresses", "sends token", "hot gas ≈ 60 °C"). Never use an arrow as a pointer; use a leader line with no head for labelling. Direction must be readable from arrowheads alone, with motion off.

## Step 2: make it explanatory (the evidence-backed rules)

- **Coherence: cut everything that doesn't carry the claim.** Removing interesting-but-irrelevant imagery improves retention with effect sizes near 1.0. No decorative icons, stock imagery, gradients, 3D, background art. Ask of each mark: if I delete it, does the meaning change?
- **Labels on the figure, never a legend.** A legend forces the eye to shuttle; putting words beside the thing they name is the single largest effect in the multimedia literature (d ≈ 1.1). Keep labels within one line-height of their referent; leader lines only when unavoidable, thin, never crossing.
- **Signal one thing.** One accent colour, one highlighted element, dim the rest to 30–50% opacity. Three or four signals per view at most; more cancels the effect.
- **Number the steps and match the text.** Same numbers, same order, same wording for the step names. Circles with numbers in a consistent style.
- **Colour-link words and picture.** If the prose names an element, give the term and the element the same hue (a swatch or coloured underline, not coloured body text). Readers find referents faster and retain more.
- **Caption states the takeaway**, not a description ("Selectivity lives in the repair, not the beam"). Pair every figure with a sentence and every abstract paragraph with a figure.
- **Encode with the right channel.** Comparisons of quantity: position or length. Categories: hue, at most six to eight. Order or amount: lightness. Never rainbow for quantity; never hue for order.
- **Icons need words the first time.** Truly universal icons are rare; label on first use, then the icon can stand alone.
- **Same mark, same meaning, across the whole document.** Define a small vocabulary once (this shape is a cell, this colour is the immune system, dashed means optional) and never restyle it.

## Step 3: make it harmonious

Harmony is mostly consistency plus restraint. A figure reads as professionally designed when a handful of parameters are held fixed everywhere.

**Colour.** Neutrals do the work: roughly 60% surface, 30% secondary greys and tints, 10% accent. One accent hue for the focal element; ≤ 6 categorical hues, chosen for colour-blind safety (about 8% of men have red-green deficiency: never red vs green alone, and pair every colour with a label, shape or position). Define palettes in OKLCH so lightness steps are perceptually even; keep chroma moderate. Contrast: text ≥ 4.5:1, any line or shape needed for understanding ≥ 3:1 against its neighbours. Dark mode is not an inversion: darker surfaces (not pure black), desaturated accents (drop chroma 20–30%, raise lightness), layering by lighter surface rather than shadow, contrast re-checked.

**Typography inside figures.** One typeface (a sans for labels), two or three sizes only (e.g. 16/13/11 px), nothing under 11–12 px *at the size the figure actually renders in its layout column*, not in the viewBox (a 960-wide viewBox in a 640-px column shrinks every label by a third, so either give the figure the full width, stack it, or simplify it), horizontal text only, tabular numerals for aligned numbers, tracked uppercase (+5–12%) for tiny category labels, no coloured body text (colour a swatch or underline instead).

**Grid and spacing.** Every coordinate and gap on a 4/8-px system. Gaps inside a group visibly smaller than gaps between groups (≥ 2:1), because proximity is how readers group things. Group with whitespace first, thin lines second, boxes last; enclosure is the strongest grouping cue, so one level of boxes at most and a tinted region before a bordered one.

**Strokes, corners, shapes.** At most three stroke weights (hairline for grids and leaders, standard for shapes, heavy for emphasis). Icons on a 24-px grid with a 2-px stroke, all outline or all filled, never mixed. One corner radius per class of element. Few primitives with fixed meanings: rounded rectangle = thing/actor, circle = state/step, pill = tag, line = relation, arrow = directed relation. Flat fills; if depth is needed, one soft shadow or a two-tone fill, never bevels.

**Line and arrow conventions.** Filled closed arrowheads scaled so they don't dominate; one prevailing direction per diagram; dashed = optional, inferred, hypothetical or future; dotted = boundary or hidden; solid = actual. Label the arrow with its action, along the shaft, not across it. Uniform stroke weight unless thickness encodes quantity.

**Composition.** One dominant element by size, contrast or position; everything else quiet. Reading order should be 1 → 2 → 3 without arrows telling the eye where to go. Consolidate whitespace into regular blocks; give the focal element extra room. Align by visual mass, not bounding box (arrowheads and circles need a pixel or two of optical offset).

**Depth cues.** Three layers at most: background context (lightest), structure (mid), the claim (darkest plus accent). De-emphasis by opacity or lightness, not by shrinking.

## Step 4: motion only where the change is the content

The meta-analyses are sobering: on average, animation barely beats a static picture (g ≈ 0.2), and it loses outright when written text competes with it (g ≈ 0.1). It wins, sometimes by a lot (g up to 0.9), when the thing to be learned is itself a change (a trajectory, a timing, a flow) and there is no competing text. So:

- **Default to discrete, user-advanced steps.** People mentally chop processes into steps; a step-through build (one new element per step, previous steps dimmed, ← → controls) matches that and beats smooth animation for most mechanisms. Three to seven steps, one change per step, one caption line per step.
- **Continuous motion only for continuous change**, and one thing moves at a time, slowly enough to be apprehended. If the reader can't say what just moved, it was too fast or too much.
- **Keep text static and outside the moving region.** Never animate the words the reader must read. Captions live in a fixed panel.
- **Motion should show causality, continuity and attention**: what triggered what, where something went, look here. Nothing moves "for delight".
- **Techniques.** Draw-on for a path forming (`stroke-dasharray`/`stroke-dashoffset` from the path length to 0, 600–1200 ms). Marching dashes for ongoing flow (short dashes, muted colour, 2–4 s per cycle, pausable). One pulse (two cycles, 300–400 ms each) to signal an element at the moment the text mentions it. Morph or cross-fade for before/after of the same element (400–700 ms). Scrollytelling with a sticky figure and discrete state changes per text block, never continuous scroll-scrubbing of the mechanism.
- **Parameters.** State changes 150–250 ms; reveals 250–400 ms; large moves ≤ 600 ms; stagger related elements 30–60 ms. Ease-out on entry, ease-in on exit, standard easing for moves; `linear` only for draw-on progress and flow loops. Longer travel, longer duration, capped around 500 ms.
- **Every animated figure has a static end state** that is a complete, labelled figure on its own. Nothing the reader needs may exist only mid-animation (a "stored in cache" state that appears for a second and vanishes is lost to reduced-motion readers and to anyone who blinked). Autoplay only for one-shot intros under five seconds; anything longer or looping gets pause/step/replay controls.
- **Accessibility.** Author motion inside `@media (prefers-reduced-motion: no-preference)` so the default is safe; under reduced motion, replace transforms and parallax with 150–250 ms cross-fades and show the end state. Avoid large parallax, scroll-jacking, full-screen wipes and zooms through space (vestibular triggers scale with how much of the screen moves). Nothing flashes more than three times a second.

## Interactive and explorable figures

Interactivity reliably raises engagement; it raises learning only when the interaction exposes a cause (change a parameter, see the consequence) or makes the reader commit (predict before reveal). Steppers and scrollers perform about the same. Follow Victor's ladder: start concrete (one instance, one setting), give direct control of one parameter, then let the reader step up to views over time or over parameters, and always let them click back down to a concrete case. Add a "predict first" moment before any reveal; it is the part with evidence behind it.

## Building in SVG/HTML

Hand-author inline `<svg>` with native shapes and `<text>`; size by `viewBox` and let CSS scale it; wide flows read left→right, stacks top→down. Use `currentColor` and the page's colour tokens so the figure follows light and dark themes; reserve literal hues for the one element that carries meaning. Arrowheads as `<marker>` or small polygons. Text 11–13 px at drawn scale, `text-anchor` for alignment, short labels; sentences belong in the caption. Align to a grid; eyeballed offsets read as noise. Wrap in `<figure>` with a `<figcaption>` stating the claim and give the `<svg>` `role="img"` plus an `aria-label` with the same claim. No scripts, styles or foreign objects inside the SVG; keep path data short (long decorative paths mean the drawing wants a real tool, so simplify).

## Checklist before shipping a figure

1. One claim, written down; the figure supports only that.
2. The mechanism is visible: something acts on something, arrows with heads and verbs, no arrow used as a pointer.
3. Parts introduced before process, and drawn the same way every time.
4. Every element labelled on the figure; no legend; terms colour-linked to the prose where the prose names them.
5. Numbered steps match the text, ≤ 7.
6. Caption states the takeaway and how to read the figure.
7. Legible at final size in its real column and at phone width: no label under 11–12 px rendered, nothing clipped, no `min-width` wider than the column; horizontal text, one typeface, 2–3 sizes.
8. Colour is never the only encoding; ≤ 6 categorical hues; passes a deutan/greyscale check; quantities by position or length.
9. Text ≥ 4.5:1, essential lines and shapes ≥ 3:1.
10. All coordinates on the 4/8-px grid; ≤ 3 stroke weights; one radius per element class; optical alignment checked.
11. Coherence pass done: nothing decorative survives; no gradients, 3D or clip-art.
12. Consistent with the document's other figures: same tokens, same icon vocabulary, same arrow and dash conventions.
13. Works in light and dark themes with contrast re-checked.
14. If animated: the change itself is the content; text is static; one thing moves at a time; durations and easings within the ranges above; pause/step/replay present for anything over five seconds or looping.
15. Reduced motion respected with cross-fades; the static end state alone is a complete figure.

## Evidence base

- Text + diagram is the medium where multimedia principles pay off most (about twice the effect of video/VR): 2025 meta-analysis of Mayer's research program, *Educational Research Review*.
- Spatial contiguity d ≈ 1.10 (Mayer), g = 0.63 (Schroeder & Cenkci 2018, 58 comparisons); temporal contiguity d ≈ 1.2; coherence d ≈ 0.86, removing seductive details g ≈ 1.0 (Sundararajan & Adesope 2020); signalling g = 0.53 retention (Schneider et al. 2018, 103 studies); segmenting d ≈ 0.3–0.45 (Rey et al. 2019); pre-training supportive but smaller.
- Animation vs static g = 0.23 overall, 0.88 with no competing text, 0.11 with written text; iconic beats abstract; cueing inside animation adds nothing: Berney & Bétrancourt 2016 (140 comparisons); Höffler & Leutner 2007 d = 0.37; Ploetzner et al. 2020 on when the change itself must be learned. Apprehension and congruence principles: Tversky, Morrison & Bétrancourt 2002.
- Arrows nearly double functional descriptions: Heiser & Tversky 2006. Natural diagram mappings: Tversky 2011, "Visualizing Thought".
- Colour-linking text and figure raised retention from 70% to 82%: Ozcelik et al. 2009.
- Perceptual accuracy ranking (position > length > angle > area > lightness > hue): Cleveland & McGill 1984, replicated by Heer & Bostock 2010. Rainbow maps harmful: Borland & Taylor 2007. Bertin's visual variables.
- Gestalt grouping strengths (enclosure and connection override proximity): Palmer 1992; Palmer & Rock 1994.
- Interactivity raises engagement, not comprehension; steppers ≈ scrollers: McKenna et al. 2017. Explorable explanations and the ladder of abstraction: Bret Victor 2011; Hohman et al., Distill 2020.
- Practitioner references: Bang Wong's *Nature Methods* "Points of View" columns; Rougier, Droettboom & Bourne, "Ten Simple Rules for Better Figures" (2014); Tufte's data-ink and smallest effective difference; Nature figure specifications; Okabe-Ito colour-blind palette; Material Design motion durations and easing, icon grid and dark theme; Apple HIG animation rules; Willenskomer's "UX in Motion" principles; Val Head on motion sensitivity; WCAG 1.4.11, 2.2.2, 2.3.1, 2.3.3; web.dev and MDN on `prefers-reduced-motion`.
