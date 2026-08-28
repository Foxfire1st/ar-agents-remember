# mcp/test_support/agents_remember_test_support/code_quality/check.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/test_support/agents_remember_test_support/code_quality/check.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | overview.md |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

check.py is the Dagger-only execution facade for the repository Python quality rail. It consumes
the typed plan from quality_plan.py, executes each rail, controls retry and causal continuation,
merges coverage proof, runs CRAP and changed-line scoring, and returns the one wrapper result. It
does not own test selection metadata or lifecycle publication.

The module deliberately re-exports the established CheckConfig, Step, GateScope, scope helpers,
quality_steps, and RADON_REPORT_NOTE names from quality_plan.py. Existing callers keep one stable
facade while planning and execution have separate implementation owners.

## Code Commentary

### Execution transaction

run_quality_check establishes the candidate root and progress artifact, reports full or targeted
scope, prepares content-addressed retry proof, and delegates the actual transaction to
execute_quality_rails. Deterministic source rails run before pytest. A failed source rail does not
let pytest consume stale or unrelated evidence; causal continuation may skip only the proven
dependent population and records the skipped set explicitly.

run_fixed_checks executes the plan in order. The plan itself comes from quality_plan. This module
owns result interpretation: report-only Radon commands still fail when the tool process breaks,
enforcing commands fail on any non-zero result, and every step updates the one self-overwriting
progress record.

### Pytest, retry, and coverage

prepare_retry_plan accepts proof reuse only under the opaque Dagger admission capability and the
current lane trigger. Ambiguous manifests, stale provenance, changed configuration, incompatible
runtime, or incomplete dependency ownership produce a fresh run or a loud refusal; there is no
host or diagnostic fallback.

run_pytest_only and run_coverage_rails execute the planned pytest command and then finalize evidence.
A delta retry retains old coverage separately, removes invalidated test contexts, writes fresh
coverage independently, and merges the two only after the delta passes. Missing or inconclusive
coverage cannot be reported as success. complete_coverage_rails feeds the same finalized JSON to
CRAP and changed-line coverage so the scorers do not perform competing measurements.

### Causal continuation

The causal report can suppress only tests proven to depend on an observed failed owner. Invalid,
missing, or incomplete causal evidence selects the full population. Independent tests continue,
and a failed owner remains a failing quality result even when downstream execution is reduced.

### Scope and configuration

config_from_args validates the repository-owned configuration, resolves all report paths beneath
the project root, obtains Dagger admission before any quality behavior, and derives either the
full scope or the diff-owned targeted scope. The wrapper accepts no caller-authored file list.
Tracked source, pytest roots, product coverage paths, file-size arming, and the diff base all come
from repository truth.

The staged index is intentional quality input. Closeout must stage the exact candidate before
running the wrapper; widening git enumeration to arbitrary untracked files would certify content
that may not enter the commit and would still not make those files diff-measurable.

### Result text

step_header, step_failure, and step_success keep the enforcement distinction visible in durable
logs. Radon is explicitly report-only because findings do not change Radon's exit status. A
non-zero Radon process remains a tool failure. No baseline, exemption, compatibility path, or
silent fallback turns a finding into success.

## Invariants And Boundaries

- The wrapper runs only with a valid Dagger admission capability.
- check.py owns execution and result interpretation; quality_plan.py owns types and command
  construction.
- The facade re-exports the pre-split public planning names so callers do not fork.
- Full and targeted scope are derived; callers cannot provide arbitrary paths.
- Pytest evidence is finalized before CRAP or changed-line coverage reads it.
- Retry reuse is candidate-, configuration-, selection-, runtime-, environment-, and
  artifact-bound.
- Invalid causal evidence cannot suppress any test.
- Host execution and diagnostic output cannot become acceptance evidence.
- The progress file is one bounded, atomic current-state view rather than an append-only log.

## Docs References

None. This behavior is repository-owned.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Stable facade re-exports the extracted plan contract. | `__all__` | mcp/test_support/agents_remember_test_support/code_quality/check.py:81-95 |
| One top-level execution transaction owns retry and progress. | `run_quality_check` | mcp/test_support/agents_remember_test_support/code_quality/check.py:148-198 |
| Fixed rails consume the typed plan and apply causal continuation. | `run_fixed_checks` | mcp/test_support/agents_remember_test_support/code_quality/check.py:395-492 |
| Coverage retry is merged explicitly before scoring. | `_merge_retry_coverage` | mcp/test_support/agents_remember_test_support/code_quality/check.py:550-565 |
| CLI input becomes one validated derived configuration. | `config_from_args` | mcp/test_support/agents_remember_test_support/code_quality/check.py:737-798 |

## Cross-Repo References

None.

## Update History

- 2026-08-28T04:48+02:00 — Split typed plan construction and progress state into quality_plan.py,
  retained check.py as the stable execution facade, and corrected retry/causal ownership.
- 2026-08-27T18:33+02:00 — Documented product-only scoring, dependency-owned retry, causal
  continuation, evidence lanes, and Dagger-only acceptance.
- 2026-08-25T08:27+02:00 — Moved the quality implementation from shipped product source into the
  repository test-support package.
