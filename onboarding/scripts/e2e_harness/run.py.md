# run.py

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Owns exact candidate identity, targeted applicability, two fresh scenario replications, per-run
artifacts, residual-resource acceptance, and the final no-retry summary.

## Code Commentary

### Logic

`main` first requires Dagger admission and declares the test-process boundary, records the Git
commit and candidate tree, then validates the supplied profile-owned source-selection decision
against the exact candidate, mode and diff base before executing exactly two fresh roots.
Non-applicable decisions are refused by this runner; the repository profile prevents their start. `_run_once` always removes its root, captures exceptions as evidence, and writes a run
report; a root-removal error is recorded separately and fails an otherwise successful run instead
of being ignored. The summary names zero retries and links both immutable run reports.
The fixture invocation id is preserved in per-run and aggregate evidence. L5-C10 requires
both an empty residual-session set and a clean structured teardown result.

Admission is deliberately the first statement in `main`, before argument parsing, report-directory
creation, candidate inspection, or fixture setup. A direct host invocation therefore fails without
creating evidence or reaching any tmux command; this safety property does not depend on valid CLI
arguments.

Under CCR-R03@v1 `_candidate_identity` stages the candidate index in an OS temp directory that is
proven outside the repository, instead of a scratch directory inside it — so the temporary index
can never self-include in the hashed candidate tree (the L26-documented diagnostic limitation is
fixed for this harness) cit:([`_candidate_identity`], scripts/e2e_harness/run.py:206-218).

### Conventions

Immutable invocation context travels as one frozen record. Unix-socket roots are intentionally short,
and candidate identity is computed before any scenario starts. The candidate-index scratch root must
never be inside the repository being staged.

### Invariants And Boundaries

- `RUN_COUNT` is exactly two and failed runs are not retried.
- The repository profile owns dependency scope and zero-start applicability; `selection.py` validates that admitted decision without deriving a competing dependency list.
- Only Dagger admission can enter the controller; host execution is rejected before all parsing and
  side effects.
- Candidate commit/tree, command, diff base, and selected paths appear in durable evidence.
- Any tmux session or recorded cleanup failure surviving scenario teardown fails L5-C10.
- Disposable-root cleanup errors are diagnostics; they never replace an earlier primary failure.
- The candidate tree is hashed from a scratch index outside the repository; `.arspawn-e2e-*`
  artifacts cannot enter it.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

- Candidate and replication evidence is repository-owned and recorded directly. [1]

### Repo-Internal References

- Two fresh runs are performed without a retry branch. [2]
- Residual tmux ownership is a named acceptance checkpoint. [3]
- R03 outside-repo candidate-index staging. [4]

### Cross-Repo References

No meaningful cross-repository reference applies.

- Run roots and candidate identity stay within the current candidate and disposable fixture. [5]
