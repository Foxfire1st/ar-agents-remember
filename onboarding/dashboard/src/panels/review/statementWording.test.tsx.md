# dashboard/src/panels/review/statementWording.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/statementWording.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T13:23:08+02:00 |
| lastVerifiedCommitHash | `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`|
| lastVerifiedCommitDate | 2026-09-30T13:46:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R31 rule 3's cases (5): "wording unchanged" only when every authored text field is identical.** The knowledge
pane and member rows start from the real served invariant review of the converted scratch leaf
(`gitTrees.invariant.captured.json`); `successor()` derives the second revision by changing exactly the field each
case is about, and mounts the real `SelectedStatement`.

## Code Commentary

### Logic

- Identical authored text on two revisions renders once, with `revision r2 → r3` as compact metadata.
- A condition-only revision is never labelled unchanged: the changed condition is named.
- The decision reads every field, and a field that was not carried is never promoted to unchanged
  (`wordingComparison` directly).
- Review F5: when one statement side is not present, each side keeps its own state line and no single prose block is
  shown.
- An added statement renders as labelled prose ("Added statement"), not a split code editor.

### Conventions

- The fixed successor revision ID and the display versions `r2`/`r3` are the derivation's own values, stated in the
  file.
- Since MIK-L35, `successor()` passes the member rows keyed by side (`MemberSides`: `{ before: [...], after:
  [after] }`), because `SelectedStatement` now reads each side's text only from that side's own rows (review R1 F1).
  That one line is the only change the API forced; no assertion changed (review R2 §4). These cases mount without the
  tree-comparison scope, so they pin the dataset path's rule 3 rendering; MIK-R35's tree-path cases are in
  `IntentWordDiff.test.tsx`.

### Invariants And Boundaries

- These cases pin the 13:40 rule, including its negative (a condition-only change is not "wording unchanged"); the
  reviewer's mutation (treating an uncarried field as identical) fails a case here.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1` lives outside the repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The real body the revisions start from, and the one-field successor. | "'gitTrees.invariant.captured.json',"; `successor` | dashboard/src/panels/review/statementWording.test.tsx:20-20; dashboard/src/panels/review/statementWording.test.tsx:35-51 |
| The side-keyed member rows the one-field successor mounts with (MIK-L35). | "members={{ before: [{ ...row, display_version: 'r2' }], after: [after] }}" | dashboard/src/panels/review/statementWording.test.tsx:48-48 |
| The five cases. | "renders two revisions with identical authored text once, with the revisions as metadata"; "never labels a condition-only revision unchanged: the changed condition is named"; "decides from every field and never promotes an uncarried field to unchanged"; "keeps each side's own state line when one statement side is not present (F5)"; "renders an added statement as labelled prose, not a split code editor" | dashboard/src/panels/review/statementWording.test.tsx:53-135 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T13:23:08+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): body update. Conventions record the one-line change review R1 F1 forced (the rows passed keyed by side; 2026-09-30T12:16:39), with no assertion changed, and that these cases pin the dataset path; one row added. The installed fixer normalised the successor row.
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new test module, recording review F5 (06:10:21). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
