# scenario.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/scenario.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T22:37:01+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

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

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| The scenario's authority is its live public-boundary observations and stable requirement checkpoints. | `C01` | scripts/e2e_harness/scenario.py:56-108; scripts/e2e_harness/scenario.py:141-178 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Ambient launch, structural chain, and canonical brief are separate acceptance phases. | `_launch_architect` | scripts/e2e_harness/scenario.py:181-415 |
| Vacancy, queued rebinding, and post-replacement routing are independently asserted. | `_check_vacancy` | scripts/e2e_harness/scenario.py:417-531 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| All task and repository addresses come from the disposable fixture. | `_fixture_addresses` | scripts/e2e_harness/scenario.py:616-622 |

## Update History

- 2026-08-30T22:37:01+02:00 — 260821-ARSPAWN-L5 added the fixture-start checkpoint and
  exception-to-checkpoint wrapper so every unexpected stage failure retains expected, actual,
  requirement, and corrective-owner evidence.

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T21:59:40+02:00 — 260821-ARSPAWN-L5: added the explicit identity-free
  same-seat repeat, exact ambient/hosted 0.151.0 assertions, and separately retained teardown
  evidence. Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created onboarding for the phased real-consumer spawn and replacement scenario. Verification metadata remains closeout-owned.
