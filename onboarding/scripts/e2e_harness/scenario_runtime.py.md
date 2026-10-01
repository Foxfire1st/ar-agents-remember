# scenario_runtime.py

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Owns preparation and teardown of the scenario's tmux server, hosted sessions, dashboard daemon, and
deterministic provider resources.

## Code Commentary

### Logic

Preparation creates the Dagger container's isolated tmux server under a fixture-owned
`TMUX_TMPDIR`, removes inherited `TMUX`, and passes that exact environment to every broad server
operation. `_isolated_tmux_environment` refuses cleanup unless both facts still prove ownership.
Preparation sets `exit-empty=off` at the explicit server scope before removing its temporary
anchor, keeping the isolated namespace available until the first dispatched role session arrives.
Teardown attempts every recorded-seat retirement/termination, dashboard stop, and server stop even
when an earlier leg fails, returning each cleanup failure as structured secondary evidence.

### Conventions

Resource ownership is bounded by the clean-room container and recorded fixture catalog, not a host
scan. The final `tmux kill-server` intentionally owns the container's dedicated server; it is never
run on the developer's host tmux server. Cleanup tolerates an already-absent server but does not
claim success for other errors; `run.py` checks both its result and residual sessions.

### Invariants And Boundaries

- The broad tmux-server stop is safe only because Dagger gives the scenario the entire isolated
  server; this module must not be run against a shared host tmux server.
- Loss of the fixture tmux stamp converts teardown into structured refusal evidence; it never
  authorizes a default-server kill.
- `exit-empty` is a server option; the fixture sets it with `-s`, not by relying on inferred option
  scope.
- Teardown is idempotent for already-removed run resources.
- Cleanup failures are returned, never silently suppressed or allowed to replace a primary failure.
- Resource cleanup does not erase acceptance evidence written outside the disposable root.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

- Resource ownership and teardown are bounded to the fixture's explicit tmux identity. [1]
- Destructive tmux commands require the exact fixture root and no inherited server address. [2]

### Repo-Internal References

- Teardown visits recorded seats and run-prefixed sessions before stopping the server. [3]

### Cross-Repo References

No meaningful cross-repository reference applies.

- Cleanup acts only on disposable fixture resources. [4]
