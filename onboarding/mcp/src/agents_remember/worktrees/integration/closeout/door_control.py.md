# mcp/src/agents_remember/worktrees/integration/closeout/door_control.py

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns public status, declaration, provenance update, defer, resume, and withdrawal commands for the
canonical closeout door.

## Code Commentary

Each mutation re-reads configured authority, authorizes the caller, and publishes the exact door
generation through `publish_door_intent`; the former short task-publication lock, and with it any
serialization against a concurrent task mutation, is deleted. It then requests a best-effort
refresh of every affected disposable projection. A publication conflict exposes bounded
expected/observed evidence; only a proven accepted-before result is retryable.

Since 260831-CCR (commit `99dc249b`) the status response surface reports a legacy door that
predates canonical task intent: `_response` (line 92-120) computes `unavailable` when the
published generation's `taskIntent` is not a `TaskIntentIdentity` (line 94-96) and then reports
`state: closeout-door-task-intent-unavailable` with the summary "The legacy closeout door predates
canonical task intent." and the exact `nextAction: closeout_door.update-provenance`
(line 106-120). The generation payload is still returned so the caller can see the exact legacy
bytes.

## Invariants And Boundaries

- Door publication is canonical; projection refresh is a downstream effect.
- Projection failure never rolls back an accepted task or door mutation.
- The former task-publication lock is deleted; door publication is no longer serialized against a concurrent task mutation.
- No queue state authorizes a task or door mutation.
- A missing-intent door is observable but not current; provenance update is the only advertised
  recovery route.

## Evidence

### Repo-Internal References

- Public door commands publish under the canonical closeout-door journal after re-reading configured authority; the former `task_publication_lock` task CAS is deleted. [1]
- Status response reports legacy missing-intent doors with the update-provenance route. [2]

## CCR-R02@v2 Door Currentness

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, a door without canonical task
intent stays readable but is never current; the public status surface names the exact stale state
and the canonical `update-provenance` republish route. Part of the landed L25 candidate
`99dc249b`.
