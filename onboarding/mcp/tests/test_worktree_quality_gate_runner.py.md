# mcp/tests/test_worktree_quality_gate_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_quality_gate_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T08:41+02:00 |
| lastVerifiedCommitHash |  `100b40d6be4a7d03eedbb1164ce54e2e8a314038`|
| lastVerifiedCommitDate |  2026-08-14T08:23:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

Owns the strict quality-runner command, preview, environment, memory-cap, report-replacement, and
failure-transport regressions split from the closeout mutation suite.

## Code Commentary

### Logic

`CodeQualityGateTests` proves wrapper applicability and altitude, exact diff-base forwarding,
host-managed and explicitly capped full gates, atomic replacement of the one enclosure test report, interpreter selection,
repository-selector scrubbing, and bounded failure output.

### Conventions

Checkout and target helpers remain single-owned in `test_worktree_closeout_quality_gate.py` and are
imported here; runner policy and closeout mutation are separate test responsibilities.

### Invariants And Boundaries

- A leaf runs the targeted wrapper; a master runs the full wrapper host-managed
  by default while preserving literal pytest `-n=auto`.
- Explicit caps report `mode=explicit-cap` and retain host swap; absent caps
  report `mode=host-managed` and run the plain wrapper.
- The report path is stable and each completed run replaces its predecessor.
- Missing wrappers and invalid modes fail loudly rather than weakening the gate.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this repository-local runner suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The runner suite covers preview, execution, cap, report, interpreter, and failure contracts. | `CodeQualityGateTests` | mcp/tests/test_worktree_quality_gate_runner.py:19-486 |
| Stable helpers remain in the closeout mutation suite. | `_checkout_with_wrapper`; `_quality_target` | mcp/tests/test_worktree_closeout_quality_gate.py:49-53; mcp/tests/test_worktree_closeout_quality_gate.py:56-62 |

## Cross-Repo References

The runner can certify a consuming repository's checkout when that checkout carries the wrapper.

| Finding | Anchor | Source |
| --- | --- | --- |
| Applicability is determined from the supplied checkout rather than a repository name. | `quality_wrapper_path`; `requires_strict_code_quality` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:80-82; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:149-156 |

## L23 Quality Scratch Regression

Quality-gate coverage now expects only durable `test-results.md` in the reports
directory and asserts every subprocess temp environment points at the short
native `QUALITY_TEMP_ROOT`. This pins the durable-report/scratch separation.

## Update History
- 2026-08-14T06:40+02:00 — L23 final candidate review: quality-runner tests require Dagger-only
  execution, explicit mode/diff base, exact candidate materialization, fail-closed status, and no
  host or direct-Docker compatibility path.
- 2026-08-12T20:10+02:00 — L23 curator: documented short native temp-root propagation through the quality runner; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 replaced a platform branch in the test expectation with an equivalent lookup; host-managed and explicit-cap runtime behavior is unchanged.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: added the
  host-managed full command/report proofs and resource-policy payload coverage;
  retained explicit-cap failure proofs. Verification metadata remains pinned
  until closeout stamps L24.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: created from `CodeQualityGateTests` in the
  closeout quality-gate suite; retained shared helpers and separated runner policy from closeout
  mutation while bringing both files below the hard size gate.
