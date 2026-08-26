# mcp/tests/test_terminal_enclosure_cleanup_l5.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_enclosure_cleanup_l5.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Force terminal archive, receipt, deletion, retry, and accepted-argument behavior.

## Code Commentary

### Logic

The suite cuts cleanup before and after archive publication/readback/locator receipt, proves the archive survives enclosure deletion and retry, rejects live-operation cleanup, and binds one exact cleanup or abandon argument set to the terminal request.

### Invariants And Boundaries

- The enclosure root is deletable only after canonical evidence survives outside it.
- Retry reuses the accepted archive and exact cleanup arguments.
- Changed terminal arguments conflict instead of falling back to defaults.
- Active or ambiguous operation evidence is never deleted.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Archive/readback/deletion and crash-retry behavior are forced. | `test_terminal_archive_reads_back_before_root_deletion_and_survives_retry`; `test_terminal_archive_reuses_bytes_after_crash_before_locator_publication` | mcp/tests/test_terminal_enclosure_cleanup_l5.py:30-65; mcp/tests/test_terminal_enclosure_cleanup_l5.py:68-118 |
| Live-operation refusal and exact terminal argument identity are forced. | `test_terminal_archive_refuses_live_operation_and_preserves_enclosure`; `test_terminal_archive_binds_one_cleanup_disposition` | mcp/tests/test_terminal_enclosure_cleanup_l5.py:121-152; mcp/tests/test_terminal_enclosure_cleanup_l5.py:155-180 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.