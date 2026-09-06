# mcp/tests/test_memory_incremental_scope_compiler.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_incremental_scope_compiler.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Exact incremental memory dependency closure and non-accepting reuse.

## Code Commentary

### Logic

R06 includes direct, transitive and reverse-only dependencies and leaves full-only checks pending. Stale indexes, adjacent candidates and missing or ambiguous authority refuse. R07 publishes every member, preserves typed blocked results and never promotes incremental success. Unchanged interrupted work reuses exact passes; changed memory reuses only units with identical dependency inputs.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Incremental memoryReady is not closeoutReady or acceptanceEligible. Full-final obligations remain explicit; no silent full fallback repairs unproven scope.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Direct transitive and reverse only dependencies are complete. | `test_direct_transitive_and_reverse_only_dependencies_are_complete` | mcp/tests/test_memory_incremental_scope_compiler.py:226-244 |
| Full only checker remains pending without silent full fallback. | `test_full_only_checker_remains_pending_without_silent_full_fallback` | mcp/tests/test_memory_incremental_scope_compiler.py:247-257 |
| Stale index and adjacent candidate snapshot are scope unproven. | `test_stale_index_and_adjacent_candidate_snapshot_are_scope_unproven` | mcp/tests/test_memory_incremental_scope_compiler.py:260-284 |
| Missing or ambiguous r01 r02 authority is scope unproven. | `test_missing_or_ambiguous_r01_r02_authority_is_scope_unproven` | mcp/tests/test_memory_incremental_scope_compiler.py:313-324 |
| R07 execution publishes every member and never promotes incremental success. | `test_r07_execution_publishes_every_member_and_never_promotes_incremental_success` | mcp/tests/test_memory_incremental_scope_compiler.py:570-591 |
| R07 blocked unit preserves code and blocks aggregate. | `test_r07_blocked_unit_preserves_code_and_blocks_aggregate` | mcp/tests/test_memory_incremental_scope_compiler.py:594-631 |
| R07 unchanged interruption reuses exact passes without executing. | `test_r07_unchanged_interruption_reuses_exact_passes_without_executing` | mcp/tests/test_memory_incremental_scope_compiler.py:634-653 |
| R07 memory change reuses only units with identical dependency inputs. | `test_r07_memory_change_reuses_only_units_with_identical_dependency_inputs` | mcp/tests/test_memory_incremental_scope_compiler.py:656-689 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-06T00:23:26+00:00 — L30 recovery: Refreshed the incoming affected-execution range; unchanged test source retains its verification stamp.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 993953760ef65c4670a40c63a6d6ef0fbcddbe3b (CCR-R07@v3/L07): created the card covering the R06 scope-compile edges and the R07 affected-closure plan/execute/reuse/aggregate edges added by this commit; no prior sidecar existed.
