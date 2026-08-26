# mcp/tests/test_lifecycle_enclosure_successor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_enclosure_successor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Force same-address terminal-to-successor enclosure publication.

## Code Commentary

### Logic

The tests build a verified terminal predecessor archive/receipt, reserve and resume one successor generation, cut the real abandon boundary, and reject unproved, conflicting, tampered, noncanonical, or nonrestartable predecessor evidence.

### Invariants And Boundaries

- No successor exists before verified terminal archive proof.
- Only the exact predecessor tombstone may become the accepted successor contract bytes.
- Retry is idempotent and conflicting successors lose.
- The successor locator retains the predecessor archive link.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture helpers construct terminal predecessor and successor contracts. | `_terminal_abandoned_predecessor`; `_successor`; `_real_successor` | mcp/tests/test_lifecycle_enclosure_successor.py:37-48; mcp/tests/test_lifecycle_enclosure_successor.py:51-58; mcp/tests/test_lifecycle_enclosure_successor.py:61-84 |
| Success and real-abandon boundary tests prove reservation and publication. | `test_terminal_predecessor_reserves_and_resumes_one_linked_successor`; `test_real_abandon_completion_is_the_successor_admission_boundary` | mcp/tests/test_lifecycle_enclosure_successor.py:97-119; mcp/tests/test_lifecycle_enclosure_successor.py:122-168 |
| Negative cases reject conflicting or untrusted predecessor evidence. | `test_terminal_predecessor_refuses_unproved_and_conflicting_successors`; `test_successor_refuses_a_nonrestartable_predecessor_contract`; `test_successor_refuses_tampered_terminal_archive_bytes`; `test_successor_refuses_missing_or_mismatched_terminal_receipt`; `test_successor_refuses_terminal_archive_outside_the_canonical_external_address`; `test_successor_locator_cannot_change_the_manifest_predecessor_link` | mcp/tests/test_lifecycle_enclosure_successor.py:171-193; mcp/tests/test_lifecycle_enclosure_successor.py:196-208; mcp/tests/test_lifecycle_enclosure_successor.py:211-223; mcp/tests/test_lifecycle_enclosure_successor.py:226-239; mcp/tests/test_lifecycle_enclosure_successor.py:242-264; mcp/tests/test_lifecycle_enclosure_successor.py:267-296 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.