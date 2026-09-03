# mcp/tests/test_clean_room.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_clean_room.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite verifies the clean-room CLI remains a transparent, fail-closed adapter over the canonical Dagger executor.


CCR-R22@v1 (L22, commit `685f83c44055`) adds the two new required CLI arguments
(`--repository-id`, `--certification-profile`) to the clean-room CLI tests and asserts they
reach `CleanQualityRequest.repository_id`/`profile_reference`.

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
| All public CLI result and forwarding branches are exercised. | `test_clean_room_cli_passes_explicit_candidate_and_memory_limit`; `test_clean_room_script_entry_exits_with_the_canonical_result` | mcp/tests/test_clean_room.py:13-68; mcp/tests/test_clean_room.py:88-108 |

## Cross-Repo References

No cross-repository boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Temporary paths stay within each test. | `test_clean_room_cli_passes_explicit_candidate_and_memory_limit` | mcp/tests/test_clean_room.py:13-68 |

## Update History
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the repository-id/certification-profile CLI assertions in clean-room tests.


- 2026-08-28T06:28+02:00 — No content impact: reviewed the clean-room helper's move into
  `agents_remember_test_support`; all test scenarios and expectations are unchanged.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the clean-executor package relocation used by the script-entry patch; CLI exit propagation behavior is unchanged.
- 2026-08-12T15:19+02:00 — Created with L23 clean-room CLI tests; verification provenance remains closeout-owned.
