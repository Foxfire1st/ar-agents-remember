# dashboard/src/panels/detail-panel/changeSetBar.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/changeSetBar.test.tsx`   |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-09-28T17:10:24+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`                  |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
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
| **The Intent review opens the task-context review and the reviewer chooses the subject; a failed summary read keeps the entry with `offline` and the reason in the disclosure.** | "opens the task-context review; the reviewer chooses the subject"; "keeps the entry when the summary read itself fails" | dashboard/src/panels/detail-panel/changeSetBar.test.tsx:393-444 |
| **The closed leaf's recorded entry with intent counts, and its survival when knowledge is unavailable.** | "offers the Intent review for a closed leaf, bound to its recorded comparison"; "keeps the closed leaf's Intent review when its knowledge is unavailable" | dashboard/src/panels/detail-panel/changeSetBar.test.tsx:75-130 |
| The net's leaf attribution rendered beside the total, the request that asks for it, and the absent-answer rule. | "carries the master net's leaf attribution beside its total (R33.2)" | dashboard/src/panels/detail-panel/changeSetBar.test.tsx:160-233 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-28T17:10:24+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): **body update — the Intent review cases were rewritten for the compact entry (`ICR-R24@v3`).** The Logic paragraph on the three catalogue-answer cases and the L9 complete-catalogue paragraph are replaced by the current cases (task-context open with intent counts; failed summary read with `offline` and the disclosure reason, L47-R1-F4); the L12 section's two closed-leaf bullets are annotated with their current form; the Invariants sentence now says why assertions changed. The reopened row that named the removed L9 case was replaced by rows citing the current cases. No stamp advanced; closeout owns the real stamp.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "opens the series view bound to the generation the net published" repointed to dashboard/src/panels/detail-panel/changeSetBar.test.tsx:236-303. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T23:30:00+02:00 — 260921-ICR-L33 curator (candidate `ar/260921-icr-l33-ar`, uncommitted; code base `86639933d61528387ce106dbd4d7a334bd468671` plus the working-tree delta; adversarial round 2 `verify-l33.md` = `pass`): **one case added for the net's leaf attribution.** The subsection above records `carries the master net's leaf attribution beside its total (R33.2)`, its base-defect standing, and the absent-answer rule; the catalogue row was re-derived into the case this leaf's insertion moved (`308-394` → `469-539`) with the gate's own resolver. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.
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
  defect as a case. *(Since `260921-ICR-L47`: the summary answers `+2 −1`, the entry reads
  `Intent review (recorded)` with those counts, no picker is mounted, and the click opens
  `review: { historical: true }` with no subject.)*
- **"keeps the closed leaf's Intent review when its record offers no subject"** pinned the other half.
  *(Since `260921-ICR-L47` it is "keeps the closed leaf's Intent review when its knowledge is
  unavailable": the summary answers `unavailable`, and the entry is still offered and still opens the
  recorded comparison, because the summary is a label and never the gate.)*

No live-leaf case changed: the working change-set and the live review entry are exactly what they
were.

## Update History
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **the closed leaf's entry set, and two cases for it (ICR-R12@v1).** The "no live enclosure" case now
expects committed **and** the Intent review with no working button, and two new cases measure the
recorded target (`historical: true` beside the recorded subject) and that an empty catalogue does not
remove the entry. No live-leaf case changed. **Citation accounting:** the rows this leaf's insertions
moved were re-derived against the candidate. **Stamp accounting:** no verification stamp was advanced —
the candidate is uncommitted and the governed closeout owns the real stamp.
