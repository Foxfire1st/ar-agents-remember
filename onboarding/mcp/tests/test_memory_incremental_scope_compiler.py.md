# mcp/tests/test_memory_incremental_scope_compiler.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Exact incremental memory dependency closure and non-accepting reuse, including historical Git-tree attention nodes and rename handling.

## Code Commentary

### Logic

R06 includes direct, transitive and reverse-only dependencies and leaves full-only checks pending. Stale indexes, adjacent candidates and missing or ambiguous authority refuse. R07 publishes every member, preserves typed blocked results and never promotes incremental success. Unchanged interrupted work reuses exact passes; changed memory reuses only units with identical dependency inputs. The current regressions keep historical Git-tree members in attention without execution and mark only the old side of a rename historical.

### Conventions

This card describes the current candidate source after the CCR-L42 historical-member and rename regressions; historical entries below record earlier test populations and do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Incremental memoryReady is not closeoutReady or acceptanceEligible. Full-final obligations remain explicit; no silent full fallback repairs unproven scope.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Direct transitive and reverse only dependencies are complete. [1]
- Full only checker remains pending without silent full fallback. [2]
- Stale index and adjacent candidate snapshot are scope unproven. [3]
- Missing or ambiguous r01 r02 authority is scope unproven. [4]
- R07 execution publishes every member and never promotes incremental success. [5]
- R07 blocked unit preserves code and blocks aggregate. [6]
- R07 unchanged interruption reuses exact passes without executing. [7]
- R07 memory change reuses only units with identical dependency inputs. [8]

| Historical Git-tree attention is excluded from execution, and rename observation marks only the old node historical. | `test_r07_historical_document_stays_in_attention_without_execution`; `test_git_rename_marks_only_the_old_node_as_historical` | mcp/tests/test_memory_incremental_scope_compiler.py:595-629; mcp/tests/test_memory_incremental_scope_compiler.py:631-661 |

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
