# mcp/tests/test_clean_room.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_clean_room.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T15:19+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite verifies the clean-room CLI remains a transparent, fail-closed adapter over the canonical Dagger executor.

## Code Commentary

### Logic

The tests assert explicit candidate and memory-limit forwarding, refusal text and exit status, quiet success, and script-entry behavior.

### Conventions

The executor is doubled because these tests own CLI translation only.

### Invariants And Boundaries

- Adapter exceptions become a non-zero refusal.
- Successful and failing executor status is preserved exactly.

### Todos

None.

## Docs References

No external Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source governs this CLI translation test. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| All public CLI result and forwarding branches are exercised. | `test_clean_room_cli_passes_explicit_candidate_and_memory_limit`; `test_clean_room_script_entry_exits_with_the_canonical_result` | mcp/tests/test_clean_room.py:13-73 |

## Cross-Repo References

No cross-repository boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Temporary paths stay within each test. | `test_clean_room_cli_passes_explicit_candidate_and_memory_limit` | mcp/tests/test_clean_room.py:13-73 |

## Update History

- 2026-08-12T15:19+02:00 — Created with L23 clean-room CLI tests; verification provenance remains closeout-owned.
