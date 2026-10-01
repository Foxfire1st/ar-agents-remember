# dashboard/src/panels/review/ReviewRefresh.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The review surface's explicit refresh control and the one sentence that says what its answer means
(`ICR-R17@v1`). It is `ReviewSurface.tsx`'s second extraction in this leaf — the surface keeps the read
cycle in [`ReviewReadCycle.ts`](ReviewReadCycle.ts.md) and passes this component the two values it
needs — so no read logic lives here and no rendering decision lives in the surface's read path.

**What a refresh is.** It is a read of the *same* question — same task context, same subject, same page
position — that additionally carries the identity of the comparison the reader is looking at. The
server compares that identity against the comparison it renders, so the answer is one of exactly two
facts and never a blend of them:

- the candidate's comparison is still the one on screen (`current`), and the panes below are the answer
  to the question that was asked — the whole payload was replaced, not patched;
- the candidate published another comparison while the panel stayed open (`superseded`): the panes
  below are the candidate's **current** comparison, replaced whole, and the identity the reader was
  reading is named beside the refresh control as the previous input that moved — never presented as
  the generation on screen.

**A failed refresh keeps the old generation.** The control is a re-read, so a read that fails leaves the
last coherent comparison exactly where it was, still labelled, with its error stated beside it by the
outcome region — and the notice therefore describes the *displayed* comparison and never claims a
generation the surface is not showing.

**What it is not.** No polling loop lives here: nothing re-reads on a timer and the control is the
reader's own action. It chooses no dataset — the previous identity it carries is only ever compared,
never substituted for the comparison the server resolves. And the identity belongs to the question it
was displayed under: it is sent only by a read that replaces exactly that question, so the notice can
never announce a candidate publication for a question the reader had merely switched to.

## Code Commentary

### Logic

The notice leads with Comparison current or Comparison updated; exact previous/current bindings and the explanation of whole-comparison replacement remain inside Generation details. The displayed comparison is still the subject of the claim.

**The module header is the contract, and it is the thing the first fix round had to make true.** It
states the two possible answers, the failed-refresh rule, and the boundary (no polling, no dataset
choice, the identity belongs to one question). Because the notice is a claim about a store, the header
also states the rule a later reader must not weaken: the sentence describes the **displayed**
comparison.

**`ReviewGenerationState` is the two states a *rendered* claim may have, and `undefined` is not one of
them.** The type is `"current" | "superseded"`; "no claim" is expressed by the whole `ReviewGeneration`
being `null`. The comment above it says why: a surface that has not been re-read since it was opened
has compared nothing against the displayed identity, and claiming either state would assert a
measurement nobody made. `superseded` carries the comparison that is there now, so the sentence can
name both sides.

**`ReviewRefresh` is a button plus a conditional notice, and it holds no state.** The props are the
reader's `onRefresh`, the `busy` flag (the surface passes `read.phase === "loading"`) and the
`generation` value or `null`. The button carries `data-testid="review-refresh"`,
`data-review-busy={busy ? "true" : "false"}`, `aria-busy` and a `title` that says what the action is;
the notice carries `data-testid="review-generation-notice"`, `data-generation-state`,
`data-previous-binding` and `data-current-binding` — which is what lets a case assert the sentence and
the pane attribute agree instead of asserting wording alone.

**The sentence is chosen by the state, and each clause is a fact the answer published.** For
`superseded` the text is `` `the candidate's comparison moved (was ${previousBindingDigest}, is now
${currentBindingDigest}) — the panes below have been replaced whole with the current one` ``; for
`current` it is `` `the comparison below is still the candidate's current one
(${previousBindingDigest})` ``. The `superseded` wording is the second fix round's correction: the
earlier text claimed the panes below were "the comparison you were reading", which the DOM contradicts
— a `stale` answer publishes the **current** comparison and merely *names* the carried identity as the
previous input — so the sentence now names both digests and says which one the panes hold.

**`generationOf` is the one place a claim is derived, and it refuses to claim more than it measured.**
It returns `null` unless every one of these holds: the read that carried the identity has
`phase === "reviewed"`; a `carried` identity exists; a `shown` payload exists; and that payload's
`comparison?.binding_digest` is present. Otherwise it returns `{state, previousBindingDigest,
currentBindingDigest}` where the state is `current` exactly when the shown digest equals the carried
one. The two digests are read from the payload the surface actually renders — never from the props and
never from the request — because a notice that described a generation the panes are not showing would
be a false statement about the store, which is worse than showing no notice at all.

**The phase gate is the first fix round's rule, and the comment states the reasoning rather than the
rule.** The refresh exists to answer "has the candidate moved?", and a read that never reached the
server has answered nothing: a `refused` or `failed` refresh renders **no** generation claim, the last
coherent comparison stays on screen with the outcome region's failure beside it, and the surface does
not tell the reader "still current" about a question nobody measured. The comment also records why the
comparison could not have produced anything new there — the payload it would have compared is the
retained one, whose identity the reader was already looking at.

**The refresh also re-validates the task entry (`260921-ICR-L47`, ruling 2026-09-28T16:27:28+02:00 on
L47-R1-F2).** The click calls `onRefresh()` and then `revalidateEntry()` from `useRevalidateIntentEntry()`
(`data/intentEntryRevalidation.tsx`), because the entry's `+N −N` describe the same comparison. It re-reads
the entry's summary once (the entry is hidden while the reviewer is open) and does not re-read the catalogue.
Without the cockpit's provider `revalidateEntry` is a no-op.

- The click refreshes, then re-validates the entry. [1]

### Conventions

One exported component, one exported deriving function and two exported types; no state, no effect and
no client call. Everything it renders comes from props and everything it reads comes from the payload
the caller hands it, so a case can drive it with a literal `generation` value. Props are destructured
inline with their types declared in the parameter position; the inline `style` objects and the
`data-*` attributes follow the cockpit panels' idiom, and the button is a real `<button
type="button">`. The comment above `generationOf` names the two leaf ids whose defects it closes
(`L17-F2`, `L17-R2-F2`) so a later reader can find the case that pins each.

### Invariants And Boundaries

- **No claim without an answered read.** `generationOf` consults `read.phase` first: only a read whose
  phase is `reviewed` may produce a `current` or `superseded` claim, so a refusal or a transport
  failure renders no notice at all.
- **The claim is derived from what is rendered.** Both digests come from the `shown` payload, so the
  notice and the pane's own `data-comparison` cannot disagree.
- **`current` and `superseded` are the only claimable states, and "no claim" is `null`.** A surface that
  has not been re-read asserts nothing.
- **The sentence is a claim about the panes it sits beside.** A `superseded` notice names the moved
  previous identity and the current one, and says the panes hold the current one; it never presents the
  carried identity as the generation on screen.
- **A failed refresh changes no claim.** The retained comparison stays on screen and the notice
  describes it — or, when no read answered, no notice is rendered.
- **The control is the reader's own action.** No timer, no polling loop and no automatic re-read is
  started here; the component calls `onRefresh` and, since `260921-ICR-L47`, the entry's re-validation, and nothing else.
- **The control chooses no dataset.** It carries whatever identity the caller hands it; the previous
  identity is only ever compared by the server and never substituted for the comparison resolved.
- **Boundary.** This module owns the control and the sentence. The request sequence and the carried
  identity belong to `ReviewReadCycle.ts`, the outcome rendering to `ReviewOutcome.tsx`, and the
  `stale`/`current` decision itself to the server's own staleness rule — this component only restates
  that decision against the payload it was handed.

### Todos

None recorded. One honest note about the surface above this component is recorded rather than closed
here: the same-flush defect the second fix round closed (`L17-R2-F1`) was reachable only because the
subject change and the refresh click could land inside one React flush — a passive-effect timing gap no
single user action produces in today's shell. The fix is at the component boundary this leaf's test
treats as in scope, and no shell change was made or claimed.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header and its four
statements, the two exported types, the control with its `data-*` surface, the `generationOf` derivation
with its phase gate, the one call site in `ReviewSurface.tsx`, and the three cases that measure the
control, the failed refresh and the sentence-versus-DOM agreement. Every anchor in a row occurs inside
the range that row cites.

- **The module's own statement of what a refresh is — the two possible answers and never a blend — that a failed refresh keeps the old generation, and what it deliberately is not (no polling loop, no dataset choice, the identity belongs to one question).** [2]
- The module's two imports: the payload type it reads its digests from and the read state whose phase gates the claim. [3]
- **The two states a rendered claim may have, with "no claim" expressed as `null` rather than as a third state — a surface that has not been re-read has measured nothing.** [4]
- **The control: the reader's own refresh button with its observable busy state, and the conditional notice carrying the state and both digests as data attributes.** [5]
- **The sentence, chosen by the state, with each clause a fact the answer published — and the first fix round's correction, which made it say which generation the panes below hold.** [6]
- **The one derivation of a claim: the phase gate first, then the carried identity, then the payload the surface renders, and the state decided by comparing the two digests.** [7]
- **The reason the phase gate exists — a read that never reached the server has answered nothing, so a failure renders no "still current" claim beside its own error — and the reason both digests come from the rendered payload.** [8]
- The surface supplies refresh, loading state and the displayed generation to the shared control. [9]
- **The case that measures the whole refresh path through the real surface and client: the read carries the displayed identity, the notice names both digests, the panes hold the current comparison, and the sentence is asserted to agree with the pane's own `data-comparison`.** [10]
- **The case that pins the phase gate: a failed refresh keeps the labelled old comparison and its error and renders no generation claim at all.** [11]
- The submission disclosure carries the server staleness and submission boundary. [12]

| `ReviewRefresh` owns the behavior described above. | `ReviewRefresh` | dashboard/src/panels/review/ReviewRefresh.tsx:48-50 |
| `generationOf` owns the behavior described above. | `generationOf` | dashboard/src/panels/review/ReviewRefresh.tsx:113-115 |

### Cross-Repo References

No cross-repository behavior is implemented in this file. The claim it renders is about one
repository namespace's candidate comparison, answered by the same-origin dashboard route.

No meaningful cross-repo references found.
