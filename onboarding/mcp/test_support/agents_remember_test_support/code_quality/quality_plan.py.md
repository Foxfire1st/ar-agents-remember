# mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00 |
| governingOverview | overview.md |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

quality_plan.py owns the immutable configuration, progress-state model, scope facade, and
deterministic subprocess plan for the Python quality wrapper. It was extracted from check.py so
command construction can be reviewed and tested independently from process execution and result
interpretation.

check.py remains the public execution facade and re-exports the established planning names. This
module is not a second quality entrypoint and cannot publish acceptance evidence.

## Code Commentary

### Typed inputs and progress

CheckConfig is the complete immutable input to a wrapper run: candidate root, derived GateScope,
opaque Dagger admission capability, scoring thresholds, target base/scope, evidence paths, and
progress state. L19 added the optional `selection_digest` field (the immutable repository
selector-result digest) so the retry/execution layers can bind and revalidate the exact selection
identity. Step encodes the enforcement distinction structurally: report_note is absent for an
enforcing step and present for a report-only step.

QualityProgress atomically replaces one JSON current-state artifact. It records start time, current
step, detail, and completed steps. It is intentionally not an append log, acceptance artifact, or
delivery-attempt journal.

### Scope facade

git_ls_files, top_level_packages, toml_section, pytest_testpaths, and derive_scope delegate to the
single scope policy module. They remain here only as the stable plan-facing surface re-exported by
check.py; they do not duplicate scope logic.

### Ordered plan

quality_steps constructs one ordered rail list from CheckConfig. The fixed source rails are Ruff,
Ruff format, Pyright, file size, layering, and durable evidence lifecycle validation, with causal
preflight when requested. Radon CC and MI are explicitly report-only. Pytest is last so earlier
source failures cannot be hidden behind suite output.

Full runs use the repository test roots and product coverage paths. Targeted runs use the
diff-derived lint, type, size, test, and coverage populations. A targeted plan with no tests omits
pytest rather than synthesizing success; check.py reports that state in the execution transaction.

### Pytest command

_pytest_step requires the opaque Dagger capability before constructing a command. Evidence-lane
triggering supplies the exact marker expression. Phase reporting, causal reporting, and dependency
retry selection are explicit plugins and paths. Coverage instruments product modules and writes one
declared JSON artifact. A retry delta enables per-test coverage contexts so check.py can invalidate
and merge proof safely.

Root pytest configuration owns default xdist behavior. The plan does not inject a second worker
policy.

## Invariants And Boundaries

- This module constructs plans; it does not spawn subprocesses or decide final success.
- Scope policy is delegated, not copied.
- CheckConfig is immutable after construction.
- Every pytest plan requires Dagger admission.
- Enforcing versus report-only behavior is carried by Step, not inferred from names.
- Targeted populations are diff-derived; there is no arbitrary caller file list.
- Evidence lane, retry selection, causal report, and coverage arguments remain explicit.
- The immutable selection digest is part of the configuration but never shapes the rail plan
  itself; it is consumed by retry/execution identity.
- check.py is the stable facade; callers should not create a parallel wrapper.

## Docs References

None. This behavior is repository-owned.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Progress is one atomic current-state record. | `QualityProgress` | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:57-96 |
| The complete wrapper input is immutable and now carries the selection digest. | `CheckConfig`; `selection_digest` | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:100-121 |
| The ordered rail plan is pure construction. | `quality_steps` | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:136-168 |
| Pytest command construction enforces Dagger admission. | `_pytest_step` | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:247-287 |

## Cross-Repo References

None.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): recorded the L19 addition of the
  `selection_digest` field on `CheckConfig` that carries the immutable selector-result
  identity into retry/execution consumers. Verification is pinned to the owning commit.

- 2026-08-28T04:48+02:00 — Created by extracting the typed plan/progress responsibility from the
  oversized check.py facade without changing its caller contract.
