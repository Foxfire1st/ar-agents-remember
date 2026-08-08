# mcp/tests/test_worktree_integrate_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_integrate_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-08T02:00+02:00 |
| lastVerifiedCommitHash | `1b7f6f07c5ccc64627299b5d22463ef9c267e187` |
| lastVerifiedCommitDate | 2026-08-08T02:42:36+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The L17 proof suite for altitude routing at the integration seam: leaf
integration certifies its change set with the targeted contract, series/master
integration runs the full wrapper once, memory-capped, inside
`worktree_integrate` itself, and a refused gate blocks integration without
merging.

## Code Commentary

### Logic

`IntegrationQualityGateAltitudeTests` (lines 48-192) builds typed integration
contracts of both kinds (`integration_contract`, lines 25-47) and pins:

- `test_leaf_integration_runs_the_targeted_contract` — a leaf contract drives
  the gate with mode `targeted`;
- `test_series_integration_runs_the_full_capped_gate` — a series contract runs
  the full mode with the settings-owned cap;
- `test_altitude_routing_is_kind_based` — `quality_gate_mode` returns
  `GATE_TARGETED` for leaf and `GATE_FULL` otherwise;
- `test_quality_gate_memory_cap_reads_the_settings_owned_value` — the cap
  comes from `load_agentic_settings(...).quality_gate.memory_cap_bytes`;
- `test_a_refused_gate_blocks_integration_without_merging` — the refusal shape
  (`blocked-quality-gate`) precedes any merge;
- `test_dry_run_reports_the_planned_gate_without_running_it` — the preview
  carries the planned gate (mode + cap) and does not execute it.

### Conventions

The suite patches the gate runner rather than the routing helpers, so altitude
routing and refusal ordering are tested through the real `integrate.py` code
path.

### Invariants And Boundaries

- The integration step itself invokes the gate — no manager or orchestrator has
  to remember a separate full-gate invocation.
- `memory_quality_check` is not part of this move; it stays a per-leaf closeout
  gate.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for the integration-gate suite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The altitude routing and gate invocation under test. | `quality_gate_mode`, `_quality_gate_memory_cap`, `_run_integration_quality_gate` | mcp/src/agents_remember/worktrees/modules/integrate.py:54-63; mcp/src/agents_remember/worktrees/modules/integrate.py:64-68; mcp/src/agents_remember/worktrees/modules/integrate.py:664-693 |
| The planned gate the dry run reports. | `_quality_gate_preview`, `IntegratePreview`, `_dry_run_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:69-80; mcp/src/agents_remember/worktrees/modules/integrate.py:81-88; mcp/src/agents_remember/worktrees/modules/integrate.py:368-414 |
| The cap plan the full mode uses. | `plan_capped_command` | mcp/src/agents_remember/code_quality/memory_cap.py:94-135 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new integration-altitude suite; content derived from
  the current worktree source. Verification metadata pinned until closeout
  stamps the 260731-EFA-L17 commit.
