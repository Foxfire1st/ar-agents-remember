# dashboard/src/panels/detail-panel/changeSetBar.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/changeSetBar.test.tsx`   |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-09-23T04:31:57+02:00 |
| lastVerifiedCommitHash | `86639933d61528387ce106dbd4d7a334bd468671`                  |
| lastVerifiedCommitDate | 2026-09-24T18:51:31+02:00|
| governingOverview      | `../overview.md`                                            |

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


**Three cases were added, and they are the three answers the entry read can give.** The first asserts the **task-context** path: the server answers the entries route with an empty list, the bar still offers the reviewer, and activating it hands the cockpit `review: {}` — no selector, because there is none. The second asserts the **refinement**: when the server offers a recorded subject, the target carries that `selectorKind`/`selectorId`. The third asserts **survival**: an entry read that itself fails leaves the button in place rather than removing it. The subject case flushes the pending entry read before asserting, because the entry is offered from task context immediately — a click that lands before the server answers opens the whole-task review, and that ordering is asserted rather than hidden by timing.

**One case was added for the bound generation.** `opens the series view bound to the generation the net published` stubs the master net with its four endpoints and asserts the entry carries those pins into the viewer target, so the view and its expansions read the listed generation rather than re-resolving the live tip. cit:(["opens the series view bound to the generation the net published"], dashboard/src/panels/detail-panel/changeSetBar.test.tsx:75-142)

**One case was added for the complete catalogue (`260921-ICR-L9`, `ICR-R09@v1`).** `offers every catalogue row for review, not just the first` stubs the entries route with a three-row catalogue — a `both` row, a retired `before_only` row and an `after_only` row, with `total_subjects: 3` — and asserts the picker renders all three with the server's totals, that the retired row is marked `retired · before-only` rather than dropped or merged into the live population, and that selecting the **second and third** rows puts **their** identities on the Intent review target. That is the packet's non-conforming example ("the API returns multiple entries but only the first is reachable") falsified at the picker: the old hook's `entries?.[0]` selection made rows 2..n unreachable, and this case fails against it. The subject stub in `carries the server's recorded subject when the pair offers one` gained the additive `presence`/totals fields only; its assertions are unchanged.

### Conventions

One behavior boundary per suite, per the test-split rule.

### Invariants And Boundaries

Assertions were preserved verbatim from the monolithic suite; the two stubs that mirror the wire shape were updated additively (catalogue `presence`/totals) and their assertions are unchanged.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The change-set bar suite, now with the generation-bound series entry case and the complete-catalogue traversal case. | `describe`; "opens the series view bound to the generation the net published" | dashboard/src/panels/detail-panel/changeSetBar.test.tsx:14-417; dashboard/src/panels/detail-panel/changeSetBar.test.tsx:75-142 |
| **The packet's conforming example at the picker: every catalogue row is offered with its totals, the retired row is marked, and the second and third rows are selectable onto the review target.** | "offers every catalogue row for review, not just the first" | dashboard/src/panels/detail-panel/changeSetBar.test.tsx:308-394 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the D01 refusal cases.** A new subsection records the three cases this leaf adds in a dedicated describe block, the base-defect witness against the unmodified production bytes, and the two mutations that make the guards load-bearing. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T15:12:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **one new catalogue traversal case (343 → 417 lines; `ICR-R09@v1`).** `offers every catalogue row for review, not just the first` (`:308-377`) stubs a three-row catalogue with totals, asserts every row is rendered with the retired row marked `retired · before-only`, and asserts the second and third rows put their own identities on the Intent review target — falsifying the first-row-only mechanism the packet names. The subject stub in the carried-subject case gained the additive `presence`/totals fields only; its assertions are unchanged. The Logic section records the case and the additive stub rule; the suite row is re-derived (`:14-343` → `:14-417`) and one row was added for the new case. **Stamp accounting:** the verification pair names the leaf's base — the last real commit the reading was taken against — because the new case exists only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **one new generation case (273 → 343 lines).** The Logic and table record `opens the series view bound to the generation the net published` (`:75-142`); the entry-read cases below it moved with the insertion and the suite row is re-derived (`:13-136` → `:14-343`). Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the module gained the three answers the entry read can give** — no subject (task context, `review: {}`), a recorded subject (carried on the target), and a failing read (the entry survives). The pre-existing subject case was updated to flush the entry read before asserting, which is what makes the "the entry is offered immediately and the subject refines it" ordering a measured fact rather than a race. One citation row was re-derived against this candidate. **Stamp accounting:** the previous verification stamp is left as it was, because nothing in this leaf is committed; the claims this card's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.


- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  change-set bar suite split from `DetailPanel.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
## 260921-ICR-L12 The Closed Leaf's Entry Set, And Two Cases For It

`260921-ICR-L12` (`ICR-R12@v1`) rewrites this module's closed-leaf expectation and adds the two
cases that measure it:

- the existing "no live enclosure" case asserted **exactly one** button (committed). It now asserts
  what is true instead: committed is always present, working is absent because there is no uncommitted
  delta once the enclosure is closed, and the Intent review is offered — so the case selects the
  committed button by its label rather than by position, and the closed-leaf document is built by a
  shared helper.
- **"offers the Intent review for a closed leaf, bound to its recorded comparison"** is the packet's
  defect as a case: the catalogue answers one recorded subject, the picker is mounted, and clicking the
  entry opens `review: { selectorKind: "invariant", selectorId: "inv-1", historical: true }` — the
  record the entry is addressed to travels with the subject.
- **"keeps the closed leaf's Intent review when its record offers no subject"** pins the other half of
  the same fact: with an empty catalogue the entry is still offered and still opens the recorded
  comparison (the task-context target), because the read is a refinement and never the gate.

No live-leaf case changed: the working change-set and the live review entry are exactly what they
were.

## Update History
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **the closed leaf's entry set, and two cases for it (ICR-R12@v1).** The "no live enclosure" case now
expects committed **and** the Intent review with no working button, and two new cases measure the
recorded target (`historical: true` beside the recorded subject) and that an empty catalogue does not
remove the entry. No live-leaf case changed. **Citation accounting:** the rows this leaf's insertions
moved were re-derived against the candidate. **Stamp accounting:** no verification stamp was advanced —
the candidate is uncommitted and the governed closeout owns the real stamp.
