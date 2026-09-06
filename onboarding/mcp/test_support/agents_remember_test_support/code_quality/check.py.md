# mcp/test_support/agents_remember_test_support/code_quality/check.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/check.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:35:26+00:00 |
| lastVerifiedCommitHash | `c87d61cf3ed2fa467cb3e16bbdd5271c92c80c28` |
| lastVerifiedCommitDate | 2026-09-04T14:53:25+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Executes the repository's Dagger-admitted Python quality plan. It owns command/result interpretation, retry and causal continuation, coverage finalization and the wrapper outcome; quality_plan owns command planning and types.

## Code Commentary

### Logic

run_quality_check validates the opaque admission capability, reports derived full/targeted scope and runs one execution transaction. execute_quality_rails removes stale coverage and report artifacts before any attempt, prepares retry proof, executes fixed checks, then scores only finalized current coverage. Failed pre-test checks cannot reuse an old report as success.

The facade preserves public planning exports. run_fixed_checks consumes the ordered plan; report-only Radon diagnostics still fail when the tool process itself fails. Causal continuation may skip only the proven dependent population and never turns its failed owner into a passing result. Invalid or missing causal proof cannot suppress tests.

Retry binds candidate, configuration, selector, runtime, environment and artifacts. Delta retry removes invalidated test contexts, runs fresh evidence and merges coverage only after success. The immutable selection digest is forwarded into retry identity. Incomplete targeted ownership raises ScopeError rather than broadening to a guessed population.

main requires Dagger admission before quality work, normalizes the native subprocess environment, resets tempfile's cached root and creates /tmp/arq before temporary coverage allocation. This avoids the prior failure where the configured short temp root did not exist. A positive optional memory cap is applied explicitly; memory or scope failures return wrapper failure.

### Conventions

Derived repository scope and the recorded diff base are inputs; callers cannot substitute arbitrary file lists. Keep plan construction, execution, and lifecycle publication in their distinct owners.

### Invariants And Boundaries

- No host or diagnostic fallback can create acceptance evidence.
- The staged candidate is the intended quality input; unrelated untracked files are not silently included.
- Fresh pytest/coverage evidence is finalized before diagnostic CRAP and changed-line reporting. Coverage percentages and CRAP scores do not fail delivery; missing/malformed artifacts and execution failures still do.
- Incomplete ownership and invalid admission refuse instead of inventing a selection.
- Clear stale artifacts before execution; never report old coverage as current.
- Create the short temporary root before allocating beneath it.

### Todos

No source change or quality run was performed during this documentation recovery.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| Admission and execution transaction | `run_quality_check` | mcp/test_support/agents_remember_test_support/code_quality/check.py:168-218 |
| Finalize current evidence before diagnostic reporting | `complete_coverage_rails` | mcp/test_support/agents_remember_test_support/code_quality/check.py:273-315 |
| Ordered enforcing checks and causal continuation | `run_fixed_checks` | mcp/test_support/agents_remember_test_support/code_quality/check.py:415-512 |
| Exact retry inputs without a coverage-floor field | `prepare_retry_plan` | mcp/test_support/agents_remember_test_support/code_quality/check.py:661-706 |
| Dagger admission and short temporary-root initialization | `main` | mcp/test_support/agents_remember_test_support/code_quality/check.py:822-867 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-06T21:35:26+00:00 — Reconciled the d3610903 test-policy reduction against the current source, preserved integrity/ownership boundaries, and replaced stale forcing-suite citations with current owner evidence. Existing verification hash/date retained; source comparison is not final acceptance.

- 2026-09-05T06:14:14+00:00 — Reconciled execution/retry invariants and recorded the actual short-temporary-root creation fix, preserving the selection and stale-evidence lessons.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): recorded the L19 exact-ownership
  changes — targeted config now refuses incomplete test impact with
  `test-selection-ownership-incomplete` instead of safe-full expansion, and the retry plan
  binds `selection_digest`. Verification is pinned to the owning commit.

- 2026-08-28T04:48+02:00 — Split typed plan construction and progress state into quality_plan.py,
  retained check.py as the stable execution facade, and corrected retry/causal ownership.

- 2026-08-27T18:33+02:00 — Documented product-only scoring, dependency-owned retry, causal
  continuation, evidence lanes, and Dagger-only acceptance.

- 2026-08-25T08:27+02:00 — Moved the quality implementation from shipped product source into the
  repository test-support package.
