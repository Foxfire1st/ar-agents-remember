# scenario.py

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Executes the real ambient-to-hosted role chain and live manager vacancy/replacement acceptance flow,
recording checkpoints L5-C00 through L5-C09 against the exact fixture candidate.

## Code Commentary

### Logic

The scenario constructs one immutable context, starts the real dashboard and Codex boundary, verifies
the architect launch and canonical brief, waits for the architect-to-worker structural chain, then
exercises pre-vacancy delivery, manager retirement, vacancy persistence, replacement rebinding, and
post-replacement delivery. Each semantic phase is a small named function so failure ownership stays
obvious and complexity cannot accumulate in one controller.
Every phase also runs through one exception-to-checkpoint boundary. A wait, subprocess, parsing, or
fixture exception that occurs before a phase's normal assertion therefore still records the exact
requirement, expectation, observed exception, and corrective owner instead of degrading to a generic
outer timeout.
Only after the first one-call brief transaction is accepted, the ambient launch is repeated once
against the same task/role/brief and must retain both the original architect occupant and its
durable brief row. Both ambient calls record missing plane identity, while the hosted architect
must project connected `dispatch_agent` readiness and the exact 0.151.0 app-server identity.

### Conventions

Stable checkpoint definitions are module constants; actual candidate evidence is attached at runtime.
Private session ids appear only in administrative stimulus/evidence. Public message assertions use the
canonical task document plus role.

### Invariants And Boundaries

- L5-C01 requires real connected MCP readiness and normal `dispatch_agent` discovery.
- L5-C00 proves the disposable dashboard and tmux substrate before role launch.
- L5-C01 also requires two successful identity-free ambient calls to converge on one occupant.
- The architect's stored initial message byte-matches the canonical compiled brief.
- A vacancy row has no private occupant correlation and rebinds to the replacement only at delivery.
- Failure captures catalog, inbox, control, tmux, response, and Codex evidence before teardown.
- Teardown executes in `finally` for every outcome and its result is retained as independent
  diagnostic/acceptance evidence.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

- The scenario's authority is its live public-boundary observations and stable requirement checkpoints. [1]

### Repo-Internal References

- Ambient launch, structural chain, and canonical brief are separate acceptance phases. [2]
- Vacancy, queued rebinding, and post-replacement routing are independently asserted. [3]

### Cross-Repo References

No meaningful cross-repository reference applies.

- All task and repository addresses come from the disposable fixture. [4]
