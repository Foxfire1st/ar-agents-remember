# mcp/tests/test_agents_remember_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_agents_remember_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T15:19+02:00 |
| lastVerifiedCommitHash |  `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`|
| lastVerifiedCommitDate |  2026-08-12T17:53:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite proves the Dagger module itself is pinned, parseable, fail-closed, and builds the intended clean quality graph before live Docker execution is considered trustworthy.

## Code Commentary

### Logic

In-process fake Dagger objects record container graph construction. The tests cover pinned manifest/image inputs, targeted and full argument selection, real/fake Codex probe wiring, export-before-verdict behavior, invalid public inputs, and green/red verification.

### Conventions

The suite tests graph semantics without a daemon; live field proof remains a separate Dagger run.

### Invariants And Boundaries

- Unit doubles may replace Dagger transport but not command/graph selection.
- Reports must export at the exact completed boundary even for a red run.
- Invalid mode, diff base, or memory inputs refuse.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this test contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The test contract is defined by the pinned repository module. | `DAGGER_MANIFEST`; `DAGGER_MODULE` | mcp/tests/test_agents_remember_quality.py:14-17 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Tests cover pinning, refusal, graph construction, export ordering, and verdicts. | `test_agents_remember_quality_module_is_pinned_and_parseable`; `test_dagger_verify_returns_green_and_refuses_red_quality_results` | mcp/tests/test_agents_remember_quality.py:82-216 |

## Cross-Repo References

No sibling-repository boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fake Dagger objects isolate graph verification from external transport. | `FakeContainer`; `FakeDag` | mcp/tests/test_agents_remember_quality.py:29-80 |

## Update History

- 2026-08-12T15:19+02:00 — Created with L23's Dagger graph contract tests; verification provenance remains closeout-owned.
