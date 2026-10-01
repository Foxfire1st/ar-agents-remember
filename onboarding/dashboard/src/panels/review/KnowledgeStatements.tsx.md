# dashboard/src/panels/review/KnowledgeStatements.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The statement area of pane 1: the two recorded operands, and the state of each side. It is the one
owner of the rule ICR-R06@v1 states — **a knowledge addition or removal renders the complete
available statement alongside the explicit known-absent side** — and it exists because the surface
that used to own that area got it wrong in a way no gate caught: `ReviewSurface`'s `KnowledgePane`
drew the shipped diff only when *both* sides were `present`, and its `sideState` helper returned
`null` for the side that *was* present, so an added or a removed statement rendered as two muted
state lines and **no statement text at all**. The header comment states that history and the rule
that replaces it, and `ReviewSurface` now delegates the whole area to this component.

The component is display-only in the same sense the rest of the surface is: it renders the two
`ReviewSideContent` values the payload carried, holds no state, makes no request, and adds no
control. It reuses the shipped `DiffPane` and `FilePane` rather than growing a second diff engine or
a second viewer.

## Code Commentary

### Logic

The caller may supply the split or inline DiffMode; the default remains split for the technical statement pane. Both two-sided and one-sided diffs honor that layout. Operand presence/unavailability rules and full statement content are unchanged.

**Every branch is decided by a side's declared `state`, never by inspecting its text.** That is the
module header's own rule and it is what makes the four cases below exhaustive without a fifth: the
component counts the `present` sides and branches on the count, so the text of a non-present side can
never be read as an operand.

**Both sides `present` → the shipped two-sided diff, exactly as before.** `bothPresent` renders
`DiffPane` with `before.text ?? ""`, `after.text ?? ""`, `language={before.language}`, the caller `mode` (split by default)
and `collapse={false}` — the same call, and the same before-side language, the pane made before the
one-sided paths existed. The `?? ""` can only apply to a `present` side, which the model guarantees
carries text.

**One `present`, the other `absent` → a one-sided diff with the absent side named above it.**
`oneSidedDiff` feeds `DiffPane` the present operand on its own side and a genuinely empty string on
the absent side — which is the diff engine's own shape for an addition (an empty `a` = every line
added) or a removal (an empty `b` = every line removed). The empty half is a *stated* fact rather
than one the reader has to interpret, because the caller renders `sideLine` for **both** sides beside
it: `<name> (<state>): <detail>`, carrying `data-testid="review-<name>-state"` and
`data-side-state={side.state}`. The language passed to the diff is the drawn operand's own, because
that operand is the only text in the pane.

**One `present`, the other `binary` or `unresolved` → the available text as content, the
unavailable side's own reason beside it, and no diff.** `unavailable(state)` is the one predicate for
that pair, and `availableContent` renders the `review-no-diff-claimed` line ("no diff is drawn: the
other side is not a known-empty operand, so an addition or a removal cannot be claimed from it.") and
the present operand in a shipped `FilePane`. A diff here would claim the opposite operand is a
known-empty document — precisely the claim the server's `absent`/`unresolved` split exists to make
unavailable, and precisely the empty-string operand the packet forbids.

**Neither side `present` → both sides' own state lines and nothing else.** This is the task-context
pane, where no subject was compared and neither side may read as an empty operand; no diff and no
content pane are rendered.

**The text is never re-typed here.** A present side's `text` is what the server recorded, and a side
that is not `present` carries no text at all (the model refuses one that does), so nothing in this
module can turn a missing operand into an empty document — the property the renderer's cases assert
against the real `DiffPane`/`FilePane` DOM rather than against a prop.

### Conventions

The component takes exactly two props, `before` and `after`, both `ReviewSideContent` from
`../../data/review`; it declares no client and holds no state. Its helpers are plain module-level
functions with lower-case names (`unavailable`, `sideLine`, `bothPresent`, `oneSidedDiff`,
`availableContent`) and the exported component is the one declaration in `PascalCase`, matching the
route's idiom. `sideLine` is the single source of the `review-before-state` / `review-after-state`
test ids and of the `data-side-state` attribute, so a case can read a side's declared state back out
of the DOM instead of inferring it from a sentence. Inline `style` objects match the cockpit panels'
idiom.

### Invariants And Boundaries

- **A state is drawn, never inferred.** The four branches are a function of `state` alone; no branch
  reads a side's text to decide what it is.
- **Known absence is named, and it is not the same fact as unavailable content.** An `absent` side is
  the empty operand of a one-sided diff *and* a named state line; a `binary`/`unresolved` opposite
  never reaches the diff at all and gets the explicit no-diff line instead.
- **A present statement is always drawn.** Every path that has one `present` side renders its text
  (in the diff, or in `FilePane`); no path can drop it, which is the defect this component closes.
- **The diff engine and the viewer are reused, not re-implemented.** `DiffPane` comes from the
  change-set route and `FilePane` from the file-viewer route; this module declares neither.
- **Display-only.** No request, no control, no state, no conclusion; the component renders records
  another owner stored.
- **Boundary.** It owns the statement area's *rendering* contract only. What a side's state and text
  are is `mcp/src/agents_remember/application/review_statement_sides.py`'s contract, and the payload
  those values arrive in is the server's wire shape; this file re-derives neither.

### Todos

None recorded. One declared limit, restated here because it is a rendering obligation rather than a
defect: `binary` is a declared `ReviewSideState` with **no producer** on the statement-side path
today (it appears in the vocabulary and in the source-inventory content classification, and in no
statement-side builder), so the renderer's `binary` case is a declared-state fixture whose detail is
the test's own words rather than a server value. The branch is still required: the renderer must
treat unsupported content distinctly from a known absence whether or not a producer exists yet.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the component's own header comment
and its four branches, the shipped renderers it reuses, the model types it consumes, the surface
that now delegates to it, and the case module that drives the real `ReviewSurface` over the real
client.

**Test-name anchors are quoted, not backticked.** A row that cites one case names it by the
double-quoted string the case passes to `it`: a test name is several words, so a backticked span is not
identifier-shaped and the citation grammar refuses it as an anchor.

- **The header's own record of the defect and the rule: the pane drew the diff only when both sides were present while the side line returned null for the present side, and the four branches that replace it are decided by declared state.** [1]
- The two shipped renderers and the wire types this module imports, and the absence of any client import. [2]
- **The one predicate for the unavailable-content pair, which is what keeps `binary`/`unresolved` out of the diff branch.** [3]
- **The state line rendered for every non-two-sided area, carrying the state's own token in `data-side-state`.** [4]
- The unchanged two-sided path, with the before side's declared language preserved exactly as the pre-R06 pane passed it. [5]
- **The one-sided diff: the present operand on its own side, the known-absent side genuinely empty, and the drawn operand's own language.** [6]
- **The available-content path: the explicit no-diff line and the readable operand as content, so no addition or removal is claimed from an unreadable side.** [7]
- **The branch itself: count the present sides, render both state lines for anything that is not two-sided, and split on `unavailable`. The two-present early return is why a both-present area names no side.** [8]
- The model a side is: the closed four-member state literal and the value that carries `state`, optional `text`, `language` and `detail`. [9]
- The pane whose two statement fields feed this component. [10]
- The technical knowledge pane delegates its statement operands to KnowledgeStatements. [11]
- The one-sided diff engine, unchanged and reused: a split-mode CodeMirror diff over `before`/`after` with its own `diff-pane` host. [12]
- The content viewer the unreadable-opposite path reuses, and its own test id. [13]
- **The renderer cases: the addition and the removal assert the statement text in the real diff DOM, and the unreadable-opposite case asserts the viewer's content with no diff pane present.** [14]
- **The renderer cases: the addition and the removal assert the statement text in the real diff DOM, and the unreadable-opposite case asserts `FilePane` content with no `diff-pane` present.** [15]
- The case that a both-present area names no side, and the case that each of the three non-present states is carried through as its own token. [16]
- The case that no subject compared renders two named states and neither pane. [17]
- **The server-side half of the same contract: the statement sides and the field rows these branches are a function of.** [18]
- The owner of the data half of this contract. [19]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The component renders one repository
namespace's records and carries no identity that ranges beyond it.

No meaningful cross-repo references found.
