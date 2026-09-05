# `mcp/src/agents_remember/application/lifecycle/lifecycle_status_wait.py`

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/lifecycle_status_wait.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[application lifecycle overview](overview.md)

## Purpose

Application controller for the read-only lifecycle status-change wait (CCR-R15): the MCP
`worktree_status_wait` tool is addressed by canonical contract, operation kind, expected
public generation, and an opaque typed afterRevision obtained from a prior
`worktree_status` snapshot. The controller resolves the exact task-owned journal
location, runs the bounded read-only wait loop, projects the R18 coherent envelope from the exact
durable record the wait compared, and translates every typed outcome into the public response. It
never writes the journal and never acquires lifecycle, queue, gate, or worker authority.

## Code Commentary

### Logic

`LifecycleStatusWaitRequest` (extra=forbid) carries `contract_path`,
`operation_kind`, `expected_generation` (ge=1),
`after_revision` (ge=0; zero is admitted so a caller without a prior snapshot receives
the typed wrong-cursor refusal instead of a schema error), and `timeout_seconds`
(default 30.0, ge=0.0). `worktree_status_wait_tool` resolves the journal location
through `configured_lifecycle_operation_location`/`location_decision_payload`,
runs `wait_for_lifecycle_change`, and for a changed outcome projects the snapshot via
`observed_operation_projection`. Payload builders translate every typed outcome; a wait
refusal always names the exact next read-only snapshot action
(`_NEXT_SNAPSHOT_TOOL` = `worktree_status` — CCR-R15 never recommends a mutating
action from a wait refusal) and refusal details carry the expected versus observed
`meaningfulRevision` cursor facts.

### Conventions

- Read-only: the controller never mutates, retries, cancels, or acquires lifecycle/queue/gate/
  worker authority.
- Coherent changed payloads return the compact status plus the next meaningful cursor;
  unchanged/timeout returns the unchanged snapshot and cursor without claiming failure.

### Invariants And Boundaries

- Wrong contract/generation/cursor and unreadable journals refuse typed.
- The wait snapshot envelope equals the task-status envelope for the exact compared record
  (R18/R15), so the returned cursor and envelope never splice different journal revisions.

### Todos

None.

## Docs References

No configured external Domain Documentation source governs this controller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs this wait controller. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The typed read-only wait request and tool entry. | `LifecycleStatusWaitRequest`; `worktree_status_wait_tool` | mcp/src/agents_remember/application/lifecycle/lifecycle_status_wait.py:66-111 |
| Outcome-to-payload translation for coherent and refusal outcomes. | `_coherent_wait_payload`; `_refusal_wait_payload`; `_projection_incoherent_payload` | mcp/src/agents_remember/application/lifecycle/lifecycle_status_wait.py:134-260 |
| Refusal detail carries expected/observed cursor facts. | `_refusal_expected`; `_refusal_observed` | mcp/src/agents_remember/application/lifecycle/lifecycle_status_wait.py:300-318 |
| The read-only bounded wait loop it drives. | `wait_for_lifecycle_change` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:105-148 |
| The shared outcome vocabulary. | `LifecycleWaitOutcome` | mcp/src/agents_remember/models/lifecycles/operation_wait.py:14-25 |
| Same-envelope snapshot projection for changed outcomes. | `observed_operation_projection` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:260-278 |

## Cross-Repo References

No cross-repository boundary is crossed by this controller.

| Finding | Anchor | Source |
| --- | --- | --- |
| The controller drives one repository's lifecycle wait tool. | `worktree_status_wait_tool` | mcp/src/agents_remember/application/lifecycle/lifecycle_status_wait.py:81-111 |

## 260831-CCR-L15 Status-Change Wait Controller

Created with the lifecycle status-change waiting tool: it resolves the task-owned journal, runs the
bounded read-only wait, projects the R18 coherent envelope for changed outcomes, and returns typed
refusals whose details carry the expected versus observed meaningful cursor.

## Update History
- 2026-09-05T06:24:16+00:00: Generated citation repair: `LifecycleWaitOutcome` repointed to mcp/src/agents_remember/models/lifecycles/operation_wait.py:14-25. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `observed_operation_projection` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:260-278. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): created
  this card for the new read-only wait application controller.
