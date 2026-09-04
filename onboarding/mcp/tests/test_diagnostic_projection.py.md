# mcp/tests/test_diagnostic_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_diagnostic_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:50+02:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R13 optional-lane readiness projection tests (leaf 260831-CCR-L13, code commit 4ba18bb2). The optional lane projects not-requested-optional before any request, the newest terminal result after a request, and blocking facts that a requested failure or abort can never erase. Historical passes cannot override a newer failure, no diagnostic pass can satisfy or promote into R14, and a plan change stales the newest result until a newer result binds the current plan.

## Code Commentary

### Logic

The suite is registered in the `unit-regression` lane. Its builders reconstruct the canonical registry/plan tower (`_identity`/`_rail`/`scenario_registry`/`certifying_plan`/`diagnostic_plan`/`manifest_for`, lines 88-253), bind one candidate lane (`LaneScenario`, lines 255-289; `make_lane`, lines 267-271), and reserve/run/publish terminal results in the store (`publish_terminal`, lines 418-445). `DiagnosticLaneProjectionTests` (lines 448-563) covers: not-requested-optional with no fabricated evidence (lines 449-460); running projection for a live attempt (lines 462-485); aborted and hard-failure results blocking certification (lines 487-498); a historical pass never overriding a newer failure (lines 500-512); a pass never satisfying or promoting into R14 (lines 514-520); plan change staling the newest result (lines 522-545); not-requested-optional never erasing a requested failure (lines 547-556); and candidates keeping separate lanes (lines 558-563).

### Conventions

Projection semantics are exercised through the real durable store with temporary directories, no Dagger or external service.

### Invariants And Boundaries

- An empty lane projects not-requested-optional and fabricates no artifact/owner/telemetry evidence.
- A requested failure or abort blocks certification until a newer terminal pass or a changed candidate's disposition.
- Diagnostic passes never satisfy or promote into R14.
- Plan changes stale the newest result until a newer binding.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R13@v2 (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) and the R14v3 alignment keep diagnostic evidence non-satisfying; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| No diagnostic pass can satisfy or be promoted into the R14 final proof. | `DiagnosticLaneProjectionTests.test_pass_never_satisfies_or_promotes_into_r14` | mcp/tests/test_diagnostic_projection.py:514-520 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exercises the lane projection functions against a real isolated store. | `project_diagnostic_lane`; `diagnostic_blocks_certification`; `diagnostic_never_satisfies_certification` | mcp/src/agents_remember/certification/diagnostics/projection.py:101-166 |
| The lane helpers publish through the durable diagnostic manifest store. | `publish_terminal` | mcp/tests/test_diagnostic_projection.py:418-445 |
| Store/manifest builders are shared with the diff-coverage closure module. | `make_lane`; `scenario` | mcp/tests/test_diagnostic_diff_coverage.py:95 |

## Update History

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new standalone CCR-R13 optional-lane projection suite delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).
