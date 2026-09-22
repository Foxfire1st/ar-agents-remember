# dashboard/src/panels/detail-panel/changeSetBar.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/changeSetBar.test.tsx`   |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-09-22T11:00:00+02:00 |
| lastVerifiedCommitHash | `f141d164265e926be9249acf6ae680ccf9ffae61`                  |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l2`, uncommitted; base `702714fc05363cb28eacaf101ba8384475a6aa56` |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5` |
| lastVerifiedCommitDate | 2026-09-22T12:24:11+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The change-set bar behavior suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split (32-name set reconciled item-for-item). Pins the
doc-reader change-set bar rendering and interactions.

## Code Commentary

### Logic

Uses the shared `test-utils.tsx` seeds to mount a reader with a change-set bar and
assert the button/bar behavior against the rendered document.


**Three cases were added, and they are the three answers the entry read can give.** The first asserts the **task-context** path: the server answers the entries route with an empty list, the bar still offers the reviewer, and activating it hands the cockpit `review: {}` — no selector, because there is none. The second asserts the **refinement**: when the server offers a recorded subject, the target carries that `selectorKind`/`selectorId`. The third asserts **survival**: an entry read that itself fails leaves the button in place rather than removing it. The subject case flushes the pending entry read before asserting, because the entry is offered from task context immediately — a click that lands before the server answers opens the whole-task review, and that ordering is asserted rather than hidden by timing.

**One case was added for the bound generation.** `opens the series view bound to the generation the net published` stubs the master net with its four endpoints and asserts the entry carries those pins into the viewer target, so the view and its expansions read the listed generation rather than re-resolving the live tip. cit:(["opens the series view bound to the generation the net published"], dashboard/src/panels/detail-panel/changeSetBar.test.tsx:75-142)

### Conventions

One behavior boundary per suite, per the test-split rule.

### Invariants And Boundaries

Assertions were preserved verbatim from the monolithic suite.

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
| The change-set bar suite, now with the generation-bound series entry case. | `describe`; "opens the series view bound to the generation the net published" | dashboard/src/panels/detail-panel/changeSetBar.test.tsx:14-343; dashboard/src/panels/detail-panel/changeSetBar.test.tsx:75-142 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **one new generation case (273 → 343 lines).** The Logic and table record `opens the series view bound to the generation the net published` (`:75-142`); the entry-read cases below it moved with the insertion and the suite row is re-derived (`:13-136` → `:14-343`). Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the module gained the three answers the entry read can give** — no subject (task context, `review: {}`), a recorded subject (carried on the target), and a failing read (the entry survives). The pre-existing subject case was updated to flush the entry read before asserting, which is what makes the "the entry is offered immediately and the subject refines it" ordering a measured fact rather than a race. One citation row was re-derived against this candidate. **Stamp accounting:** the previous verification stamp is left as it was, because nothing in this leaf is committed; the claims this card's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.


- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  change-set bar suite split from `DetailPanel.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
