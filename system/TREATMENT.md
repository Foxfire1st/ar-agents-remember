# Explainer treatment

The explainer uses this repository's treatment to present its essay and figures. Its capability
governs the authoring stages, evidence and isolation.
Techniques and their numbers are in `TECHNIQUES.md`. The dashboard around the page is in
`DESIGN.md`.

## Intent

The essay explains the objective, what the evidence establishes, and how the system behaves on
the binding. Read the copied task and requirement packets, the task's reference notes, and the
selected reports listed in `inputs/reports.md`. Record the path and SHA-256 of each report used
in the reading stage. Choose the changes and the parts that matter, explain each part on its own,
and join those explanations into a complete essay with evidence. For a planned binding, explain
the current code and memory and identify the requirement's effects as intended.

Use the code and memory records to ground each claim. An invariant, known weakness or condition
belongs beside the account it helps explain. Keep the explanation in the markup so a reader can
follow it with motion or script off.

Show the central mechanism with at least one figure the reader drives from `TECHNIQUES.md`. For
a planned binding, mark the illustrated mechanism as intended. Use the bound material, such as a
real call path, recorded measurements, or the relevant code. Plan each figure's states, inputs
and kit parts before assembling the page from the essay and those assets.

## Who reads, and in what order

The reader is the developer who asked, a reviewer coming to it cold, or a later reader of the
documentation, with the code a click away and none of its context. Tell it in this order, so a
reader who stops early still holds a true picture:

1. **The answer.** A title stating the recorded outcome or intended change and a short lede
   explaining the objective and who it affects. Add an outcome figure if it helps.
2. **What happened.** Explain the problem, what was found, what changed and what was measured.
   Attribute measurements to their reports. A timeline can support the sequence where it helps.
3. **How it works now.** Explain the mechanism and the before and after. The reader can trace a
   path, compare the same input in both states, or drive another figure that shows the mechanism.
4. **What it means for the guarantees.** Explain which guarantees changed, how they hold, and
   which weaknesses the work closed or left open. Place the record mark beside the claim it grounds.
5. **Where to look first.** Ordered entry points into the code, one reason each. Each opens its
   kit-highlighted excerpt in place. Say that the order is yours.
6. **Risks and open questions,** marked as your reading.
7. **Not covered.** What was not read, not comparable or unavailable.

A focused explanation keeps this order inside its part. Skip a step with nothing to say; never pad
one.

## Figures and controls

- **Choose one job.** Give each figure a sequence, comparison, rule or path to explain from this
  binding. Use a step, scrubber, condition toggle, before-and-after switch or Sandbox for the
  central mechanism as the technique table describes.
- **Link.** Link a claim to its cited lines and to its figure nodes where a figure exists. Hover
  or focus highlights the linked elements, a click pins them, and Escape clears the pin.
- **Descend.** A ladder of abstraction: the whole change, a part, its hunk. Detail opens in place
  below what the reader chose; the way back stays visible.
- **Ask.** Every control answers a reader's question: what happens when…, where is this in the
  code, what changed here, which of these matter. A control that answers none is decoration.
- **Say the state.** Each driven figure states its state in a sentence beside it ("Step 3 of 7:
  the record is written before the root exists").

## Character and voice

Use clear, direct prose and let paragraph length follow the reasoning. Keep evidence marks inline
with the text they ground. Use plain sentences, present tense and active voice. Name the owner
of each judgment.
Say "the record shows" only when the basis shows it, "the report measured" for a number from a
report, and "I read this as" for your own inference. No superlatives, urgency, rhetorical
questions, exclamation marks or emoji.

## Colour

A dark page in the dashboard's tokens, named as in `DESIGN.md`. The page cannot read the
dashboard's stylesheet: take the values from `col(tone, alpha, dl)` in `kit/ar-video/23fd71bf/`,
which carries the same tokens; `dl` lights a state without a new colour. Each role keeps one
meaning across the page; `TECHNIQUES.md` names roles.

| Role | Token | Meaning |
|---|---|---|
| `bg` | `bg` | the page |
| `raised` | `bgPanel` | figures, code, tables, controls |
| `rule` | `grid` | 1px borders, idle edges, a scrubber's track |
| `ink` | `ink` | body text, what stayed |
| `muted` | `muted` | secondary text, limits, context lines, steps not yet reached |
| `spine` | `cyan` | section labels, links, a signal travelling a path |
| `current` | `amber` | where the reader is: selected node, current step, pinned claim, focus |
| `new` | `mint` | added, the after state, a new path |
| `gone` | `alarm` | removed, broken, a failing path |
| `stale` | `amber`, dashed | a part older than the code it explains |
| `reading` | `purple`, dashed | the explainer's inference and grades |

`gold` and `dormant` stay off the page. A figure uses `spine`, `current` and at most two meaning
colours. Colour never carries meaning alone: a word, a sign (+, −, →) or a border style goes with
it. Body text keeps at least 7:1 contrast, labels at least 4.5:1.

## Type and measure

The approved mockup's explanation state (`.xdoc`) sets title, lede, prose and section labels. The
system UI sans for prose; the dashboard's `--font-mono` stack for code, paths, identifiers, marks,
figure labels and step counts. No web fonts.

- Title 1.45rem/1.3, weight 650; lede 1.04rem; prose 15px/1.65; secondary 13px; code 13px/1.55;
  marks and figure labels 11px.
- Section labels 0.78rem, weight 700, capitals, 0.12em tracking, `spine`. Nothing else in capitals.
- Prose at most 78ch; figures, tables and code take the frame's width, up to 1080px.
- An 8px rhythm: 40px between parts, 16–24px inside. Corners 6px on blocks, 3px on marks. Shadows
  only on what floats.

## Motion and response

Use motion to show how a state changes, for example a propagation, a sequence, a code morph, or
a measured change. The developer's motion vocabulary in `kit/ar-video/23fd71bf/` is the house
style. Motion Canvas in the same kit supports timed scenes. A scripted moving figure plays
once in view, then waits for the reader to replay, pause, step or scrub from the keyboard. It
ends on its final state.

A WebM or MP4 video plays once on reader action with controls. Supply a still frame and listed
steps in the markup.

Reserve a figure's box before it draws, and open detail below its control. Keep the layout,
text and scroll position stable. Run one figure at a time. The still form supplies the labeled
state and steps.

## Honest figures

- A figure drawn from the code says so in its caption: "drawn from the code at <revision>, not a
  recorded run". A pass or a failure shows only where a record holds it.
- A what-if switch offers the cases the hunk's conditions handle and shows what the code decides.
- A number the reader can change spans only values the code or record defines, or a range marked
  illustrative. What the page computes from it is a model: mark it as your reading and name the
  lines it follows.
- No invented numbers, no passed badge without a recorded run, no partial graph drawn as whole.
- A limit that changes a claim stands beside it, not only under "Not covered".

## Prohibitions

- No section that walks the invariants or records one by one, and no paraphrase of a record's
  statement. A record is a mark beside the claim it grounds.
- No claim list. The claim map is for the product; on the page each claim is a sentence in the
  part it explains, beside its code or figure, with its mark.
- Use paragraphs for the explanation and mark the relevant diff lines beside the claims they ground.
- No glow, neon, gradient fills, glass, stock "AI" imagery or meaningless icons.
- No name or logo of the tool that wrote the page; the page speaks for the repository.
- No WebGL or shaders by default; HTML, CSS, SVG and Canvas2D suffice.

## Still, narrow and keyboard

**Still form.** The markup holds the full essay before any script runs. Include ordered steps
and labeled states for figures where they apply. A canvas figure has a markup equivalent.
Script may add interaction to the same material.

**Narrow.** 600–700px is a normal width. Below 560px: one column, before above after, a sticky
figure becomes a figure above each step, labels shortened, tables as key/value rows, code wrapped.
Down to 390px nothing scrolls sideways; controls stay at least 32px high.

**Keyboard.** Tab reaches every control, with a visible 2px `current` focus ring; each driven
figure names its keys beneath it.
