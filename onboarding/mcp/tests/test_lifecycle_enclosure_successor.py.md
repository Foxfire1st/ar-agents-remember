# mcp/tests/test_lifecycle_enclosure_successor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_enclosure_successor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
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

| Finding | Source Range | Source Path |
| --- | --- | --- |
| Fixture helpers construct terminal predecessor and successor contracts. | L37-L86 | [source](mcp/tests/test_lifecycle_enclosure_successor.py) |
| Success and real-abandon boundary tests prove reservation and publication. | L87-L170 | [source](mcp/tests/test_lifecycle_enclosure_successor.py) |
| Negative cases reject conflicting or untrusted predecessor evidence. | L171-L296 | [source](mcp/tests/test_lifecycle_enclosure_successor.py) |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
