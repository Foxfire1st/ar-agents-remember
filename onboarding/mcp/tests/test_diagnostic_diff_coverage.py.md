# mcp/tests/test_diagnostic_diff_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_diagnostic_diff_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:50+02:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R13 diff-coverage closure tests (leaf 260831-CCR-L13, code commit 4ba18bb2, closing the run-2 python-diff-coverage gap). The module takes the model-validator refusal cells, store CAS/in-flight/state guards, projection disposition cells, planning admission refusals, and executor helper cells that the primary suites leave untaken; each case exercises one uncovered changed unit with no behavior change to the implementation. It is fully standalone and only reuses builders from the leaf's own new diagnostic test modules.

## Code Commentary

### Logic

The suite is registered in the `integration` lane (a python-diff-coverage consumer group). It reuses builders from `test_diagnostic_models`, `test_diagnostic_planning`, `test_diagnostic_projection`, `test_diagnostic_store`, and `test_diagnostic_executor` (imports, lines 63-97) plus local helpers `terminal_attempt`/`_draft_payload`/`aborted_result`/`manifest_payload`/`build_manifest`/`outcome_payload` (lines 108-214).

Closure groups cover: `DiagnosticModelClosureTests` (lines 217-276) - nonblank unpadded semantic text, bounded owner-release evidence, runtime/authority/environment binding digest mismatches, outcome/manifest disposition matching, and manifest-to-candidate binding; `DiagnosticRunManifestClosureTests` (lines 278-341) - attempts binding the manifest candidate, unique nonces, gapless result prefix, results binding the candidate, terminal result requiring its attempt reservation and terminal slot; `DiagnosticPlanningClosureTests` (lines 344-380) - invalid-registry plan admission refusal and scenario-gate/digest helpers; `DiagnosticProjectionClosureTests` (lines 383-461) - projection validator fail-closed cells and the never-returns-optional-once-attempts-exist refusal; `DiagnosticStoreClosureTests` (lines 464-556) - publish-requires-running, non-newest abandon refusal, CAS collision fail-closed, non-object manifest root, empty forbidden root skipped, candidate mismatch, mark-running readback guard, draft/attempt binding mismatch, and illegal state transitions; `DiagnosticExecutorClosureTests` (lines 559-611) - runner-protocol no-default, aborted telemetry terminal, public gate wrapper, diagnostic-altitude green refusal, and default clock/nonce sources.

### Conventions

Each case exercises exactly one uncovered changed unit without changing implementation behavior; assertion style mirrors the primary suites (typed error codes or `ValidationError` matches).

### Invariants And Boundaries

- Closure cases never alter production behavior; they only take untaken refusal/validator branches.
- The module is standalone and depends only on the leaf's own builders plus the package under test.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. The run-2 python-diff-coverage gap closure is a repository-internal quality obligation under CCR-R13@v2; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| Closure cases take the validator/store/projection/planning/executor cells the primary suites leave untaken. | `DiagnosticStoreClosureTests.test_cas_collision_fails_closed` | mcp/tests/test_diagnostic_diff_coverage.py:486-492 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Reuses the leaf's own scenario builders across all five primary diagnostic suites. | `test_diagnostic_models`; `test_diagnostic_planning`; `test_diagnostic_projection`; `test_diagnostic_store`; `test_diagnostic_executor` | mcp/tests/test_diagnostic_diff_coverage.py:63-97 |
| Exercises the shared diagnostics package and executor internals. | `store_module`; `require_gates_one_to_three_green` | mcp/tests/test_diagnostic_diff_coverage.py:51-59; mcp/tests/test_diagnostic_diff_coverage.py:581-582 |

## Update History

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new standalone CCR-R13 diff-coverage closure suite delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).
