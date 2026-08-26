# mcp/tests/test_task_doc_structural_publication_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_doc_structural_publication_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces exact JSON/Markdown source-set and compare-and-swap behavior for L2 structural task-document
publication.

## Code Commentary

### Logic

Seven L2-owned tests force the exact accepted source set and paired JSON/Markdown CAS. Attach
refuses independent JSON or Markdown drift in the selected master without publishing any protected
document. Detach binds the selected missing master's exact absence without promoting the unrelated
sprint into a create transaction, refuses one-sided JSON or Markdown appearance, and permits a
later create only after the exact absence-bound detach publishes. Master synchronization likewise
refuses independent JSON or Markdown drift while preserving the selected leaf and paired master
documents.

The removed create-first winner-order case required task publication to proceed through the
pre-L3 queue freeze. It is intentionally not part of this L2 source. L3 owns task unlocking,
post-publication queue invalidation/rebuild, and the associated winner-order acceptance tests.

### Conventions

Each helper induces drift or publication ordering at the real `TaskDocPublication` /
`TaskDocPublicationTransaction` seam. Assertions compare selected and affected JSON/Markdown
pairs byte-for-byte on refusal instead of treating queue topology as an accepted task source.

### Invariants And Boundaries

- Only selected task-document JSON/Markdown pairs belong to the structural publication CAS source
  set; topology discovery cannot silently widen it.
- Exact missing-file absence is a source fact, so one-sided JSON or Markdown appearance must refuse
  publication without overwriting the concurrent writer.
- L2 does not use these tests to approve the current queue freeze or to claim the L3 task-first
  invalidation/rebuild contract has landed.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to these repository-internal forcing tests.

## Repo-Internal References

The test source is the direct evidence for the regression contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| Attach refuses independent selected-master JSON or Markdown drift and leaves every protected selected/affected document unchanged. | `TaskDocStructuralPublicationL2Tests` | mcp/tests/test_task_doc_structural_publication_l2.py:29-92 |
| Detach binds exact selected-master absence, excludes the unrelated sprint from the later create source set, and refuses independent missing-master JSON or Markdown appearance. | `TaskDocDetachAbsencePublicationL2Tests` | mcp/tests/test_task_doc_structural_publication_l2.py:95-198 |
| Master synchronization refuses independent JSON or Markdown drift and preserves the selected leaf plus paired master documents. | `TaskDocMasterSyncPublicationL2Tests` | mcp/tests/test_task_doc_structural_publication_l2.py:201-256 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces exact JSON/Markdown source CAS for structural task writers, detach absence, and master synchronization.

### Current Invariants

- Structural mutation publishes task truth from the selected source set without a second queue-owned read.
- Appearance, disappearance, or drift of any bound source refuses without partial publication.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-24T00:10+02:00 — 260821-CLIVE-L2: reconciled the retained seven exact source-set/CAS
  tests and removed the create-first L3 task-unlocking acceptance claim from current L2 onboarding;
  verification fields remain closeout-owned.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
