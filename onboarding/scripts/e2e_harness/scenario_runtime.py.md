# scenario_runtime.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/scenario_runtime.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T09:45+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

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

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| Resource ownership and teardown are bounded to the fixture's explicit tmux identity. | `teardown` | scripts/e2e_harness/scenario_runtime.py:19-72 |
| Destructive tmux commands require the exact fixture root and no inherited server address. | `_isolated_tmux_environment` | scripts/e2e_harness/scenario_runtime.py:178-187 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Teardown visits recorded seats and run-prefixed sessions before stopping the server. | `teardown` | scripts/e2e_harness/scenario_runtime.py:19-54 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Cleanup acts only on disposable fixture resources. | `teardown` | scripts/e2e_harness/scenario_runtime.py:19-72 |

## Update History

- 2026-08-31T09:45+02:00 — 260821-ARSPAWN-L5 closeout repair: made the isolated server's
  `exit-empty` scope explicit while preserving role-pane exit behavior. Verification remains
  closeout-owned.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: tightened the tmux
  boundary from an assumed Dagger context to an explicitly proven fixture `TMUX_TMPDIR`, with
  structured refusal when ownership cannot be established. Verification remains closeout-owned.

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T21:59:40+02:00 — 260821-ARSPAWN-L5: replaced silent cleanup suppression
  with total structured evidence and corrected the tmux boundary: the broad stop owns the dedicated
  Dagger server, not an arbitrary shared host server. Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created onboarding for scoped resource preparation and teardown. Verification metadata remains closeout-owned.
