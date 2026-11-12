# Explainer treatment

AR's own treatment for this repository's explanation pages. It steers how a page looks, reads,
moves and responds, and nothing else. It cannot change what the explainer may read, write or
start, the rules of evidence, or the page's isolation; where it seems to disagree with them, they
hold. Techniques and their numbers are in `TECHNIQUES.md`; the dashboard around the page is in
`DESIGN.md`.

## Intent

The page explains what this task set out to do and how it got there. A reader who did not follow
the work comes away knowing the objective, what actually happened on the way, and how the system
behaves now, faster than from the diff, the records or the reports. The reader plays it: figures
move through what happened and how it works, and the reader stops, steps and replays them.

The substrate informs; it is not the content. The requirement gives the objective. The task's
reports in `notes/reference/<leaf>/`, where they exist, give what happened: the problems as they
showed, what was found, what was tried and dropped, and the measurements before and after. The
code and the memory records ground each claim. The invariants and their facets, such as a known
weakness, a condition or an earlier change, help piece the story together with the task and its
reports: which guarantee was at stake, which weakness the work met, closed or left open. Use them
that way, inside the story. A page that restates the records, one invariant after another,
explains nothing, because the reader could read the records.

Each figure is built from this task's own material: its real call path, its recorded
measurements, its actual hunks. An illustration that would fit any change explains none.

The still page is the same explanation with motion or script off. It is the reduced form, never
the plan.

## Who reads, and in what order

The reader is the developer who asked, a reviewer coming to it cold, or a later reader of the
documentation, with the code a click away and none of its context. Tell it in this order, so a
reader who stops early still holds a true picture:

1. **The answer.** A title saying what the task achieved. A lede of at most three sentences: the
   objective, the outcome, and for whom. Beside it, one moving figure of the outcome, such as the
   measured before and after.
2. **What happened.** The story of the work, in order: the problem as it showed, what was found,
   what changed and what was measured. It is a sequence the reader plays (a step-through or a
   scrubbed timeline), each step a short sentence beside its figure. Numbers come from the
   reports, with the report named.
3. **How it works now.** The mechanism in motion, before and after on the same input, driven by
   the reader.
4. **What it means for the guarantees.** Which guarantees changed and how they still hold, and any
   known weakness the work closed or left open, shown in the figures above: a node lights, a path
   stays closed. One sentence each, with its record as a mark. Never a section that walks the
   invariants one by one.
5. **Where to look first.** Ordered entry points into the code, one reason each, each opening its
   excerpt in place. Say that the order is yours.
6. **Risks and open questions,** marked as your reading.
7. **Not covered.** What was not read, not comparable or unavailable.

A focused explanation keeps this order inside its part. Skip a step with nothing to say; never pad
one.

## How the page explains through interaction

- **Play.** Figures move. A request travels the changed path, a measured time shrinks from before
  to after, a block moves to its new owner. A figure plays once when it comes into view, then
  replays, pauses, steps and scrubs on the reader's hand.
- **Drive.** "How it works" has at least one figure the reader drives: step, scrub, toggle a
  condition, switch before and after on one input, or select a node to trace its path.
- **Link.** A claim, its code lines and its figure nodes are one thing in three places: hover or
  focus on one lights the others, a click pins, Escape clears.
- **Descend.** A ladder of abstraction: the whole change, a part, its hunk. Detail opens in place
  below what the reader chose; the way back stays visible.
- **Ask.** Every control answers a reader's question: what happens when…, where is this in the
  code, what changed here, which of these matter. A control that answers none is decoration.
- **Say the state.** Each driven figure states its state in a sentence beside it ("Step 3 of 7:
  the record is written before the root exists").

## Character and voice

Lively and legible: a short motion piece about one task's work, closer to an explorable
explanation or an explainer video than to a report or a slide deck. It answers the reader's hand
at once and invites the next question. The dashboard is a dark instrument panel; the page is its
live instrument.

Prose is the caption, not the content. At most two short paragraphs a part; the figures carry the
explanation, and a reader who skips the prose still follows from the motion. Plain sentences,
present tense, active voice. Name the owner of each judgment. Say "the record shows" only when
the basis shows it, "the report measured" for a number from a report, and "I read this as" for
your own inference. No superlatives, urgency, rhetorical questions, exclamation marks or emoji.

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

The page moves, and motion carries the explanation: an order, a propagation, a sequence in time, a
measured change, a block moving to its new place. The developer's motion vocabulary in
`kit/ar-video/23fd71bf/` (its easing, signals and camera) is the house style; Motion Canvas,
in the same kit, is the tool for timed scenes. A figure plays once when it comes into view and
then waits for the reader, who can replay, pause, step and scrub it. A control shows its effect
at once.

Motion never:

- decorates, or loops without end;
- moves the layout, text or scroll position under the reader: a figure's box is reserved before
  it draws, and detail opens below the control that opened it;
- plays in two figures at once;
- carries anything the still form lacks: the still form holds each figure's final state and its
  steps as a list.

Every moving figure pauses, steps and scrubs from the keyboard and ends on its final state.

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
- No text walls and no cards of prose. One item per row; the diff is marked, not retold in prose.
- No glow, neon, gradient fills, glass, stock "AI" imagery or meaningless icons.
- No name or logo of the tool that wrote the page; the page speaks for the repository.
- No WebGL or shaders by default; HTML, CSS, SVG and Canvas2D suffice.

## Still, reduced, narrow

**Still form.** The markup, before any script runs, holds the whole explanation: each figure's
steps as an ordered list, both sides of every switch, every rung open; a canvas figure has a
markup twin. Script turns it into the driven figure and never adds content the still form lacks.

**Reduced motion.** No transitions, no autoplay; every control still works and every highlight
still links. Figures open on their final state with their steps listed.

**Narrow.** 600–700px is a normal width. Below 560px: one column, before above after, a sticky
figure becomes a figure above each step, labels shortened, tables as key/value rows, code wrapped.
Down to 390px nothing scrolls sideways; controls stay at least 32px high.

**Keyboard.** Tab reaches every control, with a visible 2px `current` focus ring; each driven
figure names its keys beneath it.
