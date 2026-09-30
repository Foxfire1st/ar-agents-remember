# dashboard/src/panels/review/MarkerTargetState.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/MarkerTargetState.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**Where an unknown membership's `Attribution unknown` state is shown (2 cases; ruling Q3).** The payload is the real
review of INV-Z66EMHMH on comparison 3 (`markerUnknown.memberUnknown.captured.json`) and the target is the real
before-side occurrence of its FAM-4V4GSQCS membership (`markerUnknown.file.captured.json`); the one derived body drops
the review's family entries, as a review that composed no family has none.

## Code Commentary

### Logic

- **Case 1.** `MemberTargetNote` marks only the member row of the named family and revision; another row and another
  subject show nothing.
- **Case 2.** When the named family is not in the review's context, `MemberFamilyLabel` shows the state on the
  invariant view (mutation Q3-6).

### Conventions

- `inScope` mounts inside a scope value holding the real target.

### Invariants And Boundaries

- Part of the proof of the candidate invariant recorded on `MarkerTargetState.tsx.md`.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The real payload and target. | "markerUnknown.memberUnknown.captured.json"; `inScope` | dashboard/src/panels/review/MarkerTargetState.test.tsx:1-53 |
| The two cases. | "marks the member's row when the named family is in the tree, and only that row"; "shows the state on the invariant view when the named family is not in the review" | dashboard/src/panels/review/MarkerTargetState.test.tsx:55-93 |
| The components under test. | `MemberTargetNote`; `MemberFamilyLabel` | dashboard/src/panels/review/MarkerTargetState.tsx:56-81; dashboard/src/panels/review/MarkerTargetState.tsx:158-182 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new target-state test module MIK-R34 adds (2 cases), recording ruling Q3. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
