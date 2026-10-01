# dashboard/src/panels/detail-panel/changeSetBar.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The change-set bar behavior suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split (32-name set reconciled item-for-item). Pins the
doc-reader change-set bar rendering and interactions.

## Code Commentary

### 260921-ICR-L32 The Refusal Cases For The Live-Leaf Change-Set Read

Three cases in a new `describe("the counter read's refusal (L32/D01)")` block pin the defect D01 was: `renders a refused counter read's own code and reason, never as a read that has not answered` (the refusal's code and reason reach the control, and a refusal no longer renders as a read that has not answered), `keeps a measured empty answer apart from a refusal and from a read that has not answered` (three states, three renderings), and `does not let a superseded read's refusal land on the control that replaced it` (the liveness guard is load-bearing). Against the leaf's base production bytes the first two **fail** — the base-defect witness — while on the candidate the module is **14 passed** (11 pre-existing plus these three). Restoring the old empty rejection handler fails two of them, and deleting the liveness guard fails the third.

### Logic

Uses the shared `test-utils.tsx` seeds to mount a reader with a change-set bar and
assert the button/bar behavior against the rendered document.


**The Intent review cases (rewritten by `260921-ICR-L47`, `ICR-R24@v3`).** The entry is now the compact
`IntentReviewEntry` fed by the changed-intent summary, so the former catalogue cases (task-context on an
empty list, the recorded subject carried into the target, the complete-catalogue picker) were replaced:
`opens the task-context review; the reviewer chooses the subject` answers the summary with `+1 −1`, asserts
the counts and the live label, and asserts the click opens `review: {}` — no subject, because the reviewer
chooses it. `keeps the entry when the summary read itself fails` rejects the summary fetch and asserts the
button stays, shows no numbers, carries `data-review-state="network"` and the word `offline`, and — after
opening the `?` disclosure — that the disclosure names `network` and the reason `socket closed` (the
L47-R1-F4 fix restored this assertion).

**One case was added for the bound generation.** `opens the series view bound to the generation the net published` stubs the master net with its four endpoints and asserts the entry carries those pins into the viewer target, so the view and its expansions read the listed generation rather than re-resolving the live tip. cit:(["opens the series view bound to the generation the net published"], dashboard/src/panels/detail-panel/changeSetBar.test.tsx:236-303)

*(The L9 complete-catalogue case, `offers every catalogue row for review, not just the first`, was removed by
`260921-ICR-L47`: the entry no longer offers a picker; the reviewer's own catalogue owns traversal of every
subject.)*

### 260921-ICR-L33 The Net's Leaf Attribution

One case was added, in the master block: **`carries the master net's leaf attribution beside its total
(R33.2)`** (`:162-235`). It drives the real `DocChangeSetBar` in `kind="master"` against a stubbed
route and asserts the rendered `changeset-leaf-attribution` phrase (`2 leaf/leaves · 1 committed ·
1 working`) beside the net total, that the request carries `includeLeaves=true`, and that a non-master
read renders no attribution at all — an absent answer is not rendered as a zero. Against the leaf's
base production bytes the case fails (the base asked with `includeLeaves=false` and rendered no
attribution), which is what makes it evidence for the change rather than a restatement of it.

### Conventions

One behavior boundary per suite, per the test-split rule.

### Invariants And Boundaries

Assertions were preserved verbatim from the monolithic suite until `260921-ICR-L47`, which replaced the Intent review cases because the entry's design changed (compact control over the changed-intent summary, no catalogue at the entry); the change-set, series, generation, attribution and counter-refusal cases are unchanged.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The change-set bar suite, now with the generation-bound series entry case and the complete-catalogue traversal case. [1]
- **The Intent review opens the task-context review and the reviewer chooses the subject; a failed summary read keeps the entry with `offline` and the reason in the disclosure.** [2]
- **The closed leaf's recorded entry with intent counts, and its survival when knowledge is unavailable.** [3]
- The net's leaf attribution rendered beside the total, the request that asks for it, and the absent-answer rule. [4]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

## 260921-ICR-L12 The Closed Leaf's Entry Set, And Two Cases For It

`260921-ICR-L12` (`ICR-R12@v1`) rewrites this module's closed-leaf expectation and adds the two
cases that measure it:

- the existing "no live enclosure" case asserted **exactly one** button (committed). It now asserts
  what is true instead: committed is always present, working is absent because there is no uncommitted
  delta once the enclosure is closed, and the Intent review is offered — so the case selects the
  committed button by its label rather than by position, and the closed-leaf document is built by a
  shared helper.
- **"offers the Intent review for a closed leaf, bound to its recorded comparison"** is the packet's
  defect as a case. *(Since `260921-ICR-L47`: the summary answers `+2 −1`, the entry reads
  `Intent review (recorded)` with those counts, no picker is mounted, and the click opens
  `review: { historical: true }` with no subject.)*
- **"keeps the closed leaf's Intent review when its record offers no subject"** pinned the other half.
  *(Since `260921-ICR-L47` it is "keeps the closed leaf's Intent review when its knowledge is
  unavailable": the summary answers `unavailable`, and the entry is still offered and still opens the
  recorded comparison, because the summary is a label and never the gate.)*

No live-leaf case changed: the working change-set and the live review entry are exactly what they
were.
