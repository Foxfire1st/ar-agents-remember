# mcp/src/agents_remember/worktrees/integration/closeout/door_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/door_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns public status, declaration, provenance update, defer, resume, and withdrawal commands for the
canonical closeout door.

## Code Commentary

Each mutation takes the short task-publication lock, re-reads configured authority, authorizes the
caller, and publishes exact contract bytes. It then requests a best-effort refresh of every affected
disposable projection. A publication conflict exposes bounded expected/observed evidence; only a
proven accepted-before result is retryable.

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
- The task-publication lock is bounded to compare-and-swap publication, never leaf execution.
- No queue state authorizes a task or door mutation.
- A missing-intent door is observable but not current; provenance update is the only advertised
  recovery route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public door commands publish under the canonical task CAS. | `closeout_door_tool`; `task_publication_lock`; `publish_door_intent` | mcp/src/agents_remember/worktrees/integration/closeout/door_control.py:38-84 |
| Status response reports legacy missing-intent doors with the update-provenance route. | `_response`; unavailable computation | mcp/src/agents_remember/worktrees/integration/closeout/door_control.py:92-120 |

## CCR-R02@v2 Door Currentness

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, a door without canonical task
intent stays readable but is never current; the public status surface names the exact stale state
and the canonical `update-provenance` republish route. Part of the landed L25 candidate
`99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the closeout-door status response now surfaces `closeout-door-task-intent-unavailable` for
  legacy doors and advertises `closeout_door.update-provenance` as the recovery action. Verified
  at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final public door-control boundary. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
