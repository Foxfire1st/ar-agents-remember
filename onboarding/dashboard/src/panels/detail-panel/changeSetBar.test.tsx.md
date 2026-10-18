# dashboard/src/panels/detail-panel/changeSetBar.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The change-set bar behavior suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split (32-name set reconciled item-for-item). Pins the
doc-reader change-set bar rendering and interactions.

## Code Commentary

### 260921-ICR-L32 The Refusal Cases For The Live-Leaf Change-Set Read

Refusal cases distinguish own code/reason, unanswered reads and measured empty, and drop superseded refusals. Historical L32 fail-before/mutation receipts are not a current passing total or a run in this preparation.

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

- The change-set bar suite retains the exact generation-bound master series entry and compact Intent review controls: a closed leaf opens its recorded comparison (even when knowledge is unavailable) and explicitly has no review-subject picker; a live leaf opens review: {} for task-context review and leaves subject selection to the reviewer. The series click carries the published code/memory endpoints and digest. These cases do not exercise complete-catalogue traversal or provide a complete-catalogue picker. Complete-catalogue traversal remains reviewer-owned, not a picker exercised by these cases. [1]


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
