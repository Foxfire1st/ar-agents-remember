# dashboard/src/panels/review/KnowledgeStatements.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Render the supplied declared statement operands, reusing DiffPane/FilePane without a read or local
content classifier. The current statement vocabulary is present/absent/unresolved. There is no
binary statement branch or future binary-producer obligation; binary code-source content is separate.

## Code Commentary

Branch on declared state, not on text. Two present sides use the shipped diff and before language.
With exactly one present side, both state lines are visible: a known absent opposite is an explicitly
empty diff operand, while unresolved uses available content and an explicit no-diff explanation.
No present side yields both state lines only. Split is the default; the caller can supply inline.

The server model owns present-text/state consistency. This display component does not deeply validate
arbitrarily cast JavaScript props. Its nullish text fallbacks are not a claim that unreadable means empty.
The selected revision normally uses SubjectReview/IntentStatementBody; labelled addition/removal prose
is implemented there and reaches this declared-operand renderer on its fallback branch. This module
is not the exclusive owner of every statement display or the old technical-pane location.

The current test module uses direct synthetic component operands with real shipped pane components,
not a mounted native captured comparison. Addition/removal, unresolved-opposite and neither-present
cases do not introduce the removed unsupported binary fixture. Historical browser/mutation observations
below remain historical rather than fresh execution or performance/MEMORY acceptance.

## Invariants And Boundaries

Known absence and unreadable content remain different. Current wire-state narrowing supersedes the
old four-state/required-binary Todo. Shared renderer reuse does not mean the current direct tests are
native producer or host acceptance witnesses.

## Historical source-epoch explanation — preserved, superseded where different

Earlier useful explanation and observations remain below with inert prose reference markers. Current
wire vocabulary, owners, fixture kind and delegation above supersede contradictory old claims.

> ## Purpose
>
> The declared-operand statement renderer and fallback for the selected-subject reading area. Within this component, a readable addition/removal retains the complete available statement beside its explicitly named absent side; an unreadable opposite is not manufactured into an empty operand.
>
> It is not the exclusive owner of that display obligation. In the converted-tree selected-revision path, `SubjectReview.SelectedStatement` calls `IntentStatementBody`; added and removed revisions use `IntentWordDiff.OneSidedStatement`, which directly draws labelled prose and the opposite side's named state. That path delegates here when its expected present operand is not present. The other/raw declared-operand calls and the four local branches below remain this component's responsibility.
>
> The module header records the historical defect in the former technical `KnowledgePane`: it drew the diff only for two present operands and omitted the present side's words in one-sided reads. That history explains these local branches, not exclusive ownership or current placement behind Technical details.
>
> The component is display-only in the same sense the rest of the surface is: it renders the two
> `ReviewSideContent` values the payload carried, holds no state, makes no request, and adds no
> control. It reuses the shipped `DiffPane` and `FilePane` rather than growing a second diff engine or
> a second viewer.
>
> ## Code Commentary
>
> ### Logic
>
> The caller may supply the split or inline DiffMode; the component default remains split. Its placement is the selected-subject main reading area, not Technical details. Both two-sided and one-sided diffs honor that layout. Operand presence/unavailability rules and full statement content are unchanged.
>
> **Every branch is decided by a side's declared `state`, never by inspecting its text.** That is the
> module header's own rule and it is what makes the four cases below exhaustive without a fifth: the
> component counts the `present` sides and branches on the count, so the text of a non-present side can
> never be read as an operand.
>
> **Both sides `present` → the shipped two-sided diff, exactly as before.** `bothPresent` renders
> `DiffPane` with `before.text ?? ""`, `after.text ?? ""`, `language={before.language}`, the caller `mode` (split by default)
> and `collapse={false}` — the same call, and the same before-side language, the pane made before the
> one-sided paths existed. The `?? ""` can only apply to a `present` side, which the model guarantees
> carries text.
>
> **One `present`, the other `absent` → a one-sided diff with the absent side named above it.**
> `oneSidedDiff` feeds `DiffPane` the present operand on its own side and a genuinely empty string on
> the absent side — which is the diff engine's own shape for an addition (an empty `a` = every line
> added) or a removal (an empty `b` = every line removed). The empty half is a *stated* fact rather
> than one the reader has to interpret, because the caller renders `sideLine` for **both** sides beside
> it: `<name> (<state>): <detail>`, carrying `data-testid="review-<name>-state"` and
> `data-side-state={side.state}`. The language passed to the diff is the drawn operand's own, because
> that operand is the only text in the pane.
>
> **One `present`, the other `binary` or `unresolved` → the available text as content, the
> unavailable side's own reason beside it, and no diff.** `unavailable(state)` is the one predicate for
> that pair, and `availableContent` renders the `review-no-diff-claimed` line ("no diff is drawn: the
> other side is not a known-empty operand, so an addition or a removal cannot be claimed from it.") and
> the present operand in a shipped `FilePane`. A diff here would claim the opposite operand is a
> known-empty document — precisely the claim the server's `absent`/`unresolved` split exists to make
> unavailable, and precisely the empty-string operand the packet forbids.
>
> **Neither side `present` → both sides' own state lines and nothing else.** When a selected subject supplies no readable operand, neither side may read as an empty document; no diff or content pane is rendered. This component does not decide whether the surface mounts a knowledge pane for an unselected task-context view.
>
> **The text is never re-typed here.** A present side's `text` is what the server recorded, and a side
> that is not `present` carries no text at all (the model refuses one that does), so nothing in this
> module can turn a missing operand into an empty document — the property the renderer's cases assert
> against the real `DiffPane`/`FilePane` DOM rather than against a prop.
>
> ### Conventions
>
> The component takes `before` and `after`, both `ReviewSideContent` from `../../data/review`, plus optional `mode`; it declares no client and holds no state. Its helpers are plain module-level
> functions with lower-case names (`unavailable`, `sideLine`, `bothPresent`, `oneSidedDiff`,
> `availableContent`) and the exported component is the one declaration in `PascalCase`, matching the
> route's idiom. `sideLine` is the single source of the `review-before-state` / `review-after-state`
> test ids and of the `data-side-state` attribute, so a case can read a side's declared state back out
> of the DOM instead of inferring it from a sentence. Inline `style` objects match the cockpit panels'
> idiom.
>
> ### Invariants And Boundaries
>
> - **A state is drawn, never inferred.** The four branches are a function of `state` alone; no branch
>   reads a side's text to decide what it is.
> - **Known absence is named, and it is not the same fact as unavailable content.** An `absent` side is
>   the empty operand of a one-sided diff *and* a named state line; a `binary`/`unresolved` opposite
>   never reaches the diff at all and gets the explicit no-diff line instead.
> - **A present statement is always drawn.** Every path that has one `present` side renders its text
>   (in the diff, or in `FilePane`); no path can drop it, which is the defect this component closes.
> - **The diff engine and the viewer are reused, not re-implemented.** `DiffPane` comes from the
>   change-set route and `FilePane` from the file-viewer route; this module declares neither.
> - **Display-only.** No request, no control, no state, no conclusion; the component renders records
>   another owner stored.
> - **Boundary.** It owns its declared-operand/fallback rendering, not every selected-revision statement path. `IntentWordDiff` owns labelled addition/removal prose reached through `SubjectReview`. A side's state and text remain `mcp/src/agents_remember/application/review_statement_sides.py`'s contract and the payload remains the server's wire shape; this file re-derives neither.
>
> ### Todos
>
> None recorded. One declared limit, restated here because it is a rendering obligation rather than a
> defect: `binary` is a declared `ReviewSideState` with **no producer** on the statement-side path
> today (it appears in the vocabulary and in the source-inventory content classification, and in no
> statement-side builder), so the renderer's `binary` case is a declared-state fixture whose detail is
> the test's own words rather than a server value. The branch is still required: the renderer must
> treat unsupported content distinctly from a known absence whether or not a producer exists yet.

## Evidence

### Docs References

No configured Domain Documentation source was available. Repository implementation and stored case
declarations below are static witnesses, not fresh execution grades.

### Repo-Internal References

- The current header explains declared-state rendering and the historical omitted-one-sided-text defect; no binary statement-side branch remains. [1]
- ReviewKnowledgePane supplies the separate before/after statement operands. [10]
- The selected revision delegates to IntentStatementBody; its addition/removal prose falls back to KnowledgeStatements only when the expected available side is not present. [11]
- The one-sided diff engine, unchanged and reused: a split-mode CodeMirror diff over `before`/`after` with its own `diff-pane` host. [12]
- The content viewer the unreadable-opposite path reuses, and its own test id. [13]
- Stored synthetic component cases assert full addition/removal text and an unreadable opposite without a diff; they are not mounted native-route execution. [14]
- Stored synthetic addition/removal and unreadable-opposite declarations drive the real pane components, not a live server or captured comparison. [15]
- Stored direct component cases cover both-present suppression of side lines and declared absent/unresolved tokens when neither side is present; no binary state is injected. [16]
- Stored Python producer cases describe the corresponding added/removed statement operands; this is assertion-source inspection, not a current suite grade. [18]
- The owner of the data half of this contract. [19]
- The renderer imports declared side content and the shipped diff/content panes, not a client. [2]
- Only unresolved is unavailable statement content; known absence may be an empty diff operand, not an unreadable side. [3]
- **The state line rendered for every non-two-sided area, carrying the state's own token in `data-side-state`.** [4]
- The unchanged two-sided path, with the before side's declared language preserved exactly as the pre-R06 pane passed it. [5]
- **The one-sided diff: the present operand on its own side, the known-absent side genuinely empty, and the drawn operand's own language.** [6]
- **The available-content path: the explicit no-diff line and the readable operand as content, so no addition or removal is claimed from an unreadable side.** [7]
- **The branch itself: count the present sides, render both state lines for anything that is not two-sided, and split on `unavailable`. The two-present early return is why a both-present area names no side.** [8]
- The current statement wire has present/absent/unresolved and declared content fields; binary code-source states are separate. [9]

### Cross-Repo References

No new cross-repository behavior or authority is introduced.
