# mcp/test_support/agents_remember_test_support/code_quality/check.py

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

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured.

### Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

- Admission and execution transaction [1]
- Finalize current evidence before diagnostic reporting [2]
- Ordered enforcing checks and causal continuation [3]
- Exact retry inputs without a coverage-floor field [4]
- Dagger admission and short temporary-root initialization [5]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.
