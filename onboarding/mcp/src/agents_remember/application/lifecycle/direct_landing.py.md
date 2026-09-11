# mcp/src/agents_remember/application/lifecycle/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Application lifecycle overview](overview.md)

## Purpose

Publishes the direct-landing application tool and its recovery guidance over the durable operation journal.

## Code Commentary

### Logic

It validates feature/config authority, invokes the direct landing owner, reads canonical operation projections, and returns exact resume, retry, cancel, or cleanup guidance for unreadable and terminal generations. Since 260831-CCR (commit `99dc249b`), `_direct_error_payload` (line 119) also forwards the typed `nextAction` from a `DirectLandingError` into the refusal payload when present (`task_intent_recovery`, line 129), so a direct-landing refusal caused by missing or stale canonical task intent advertises exactly `direct_landing.update-provenance`/retire-and-republish rather than a generic recovery hint.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Direct landing is explicit and journal-backed; it is never an automatic fallback from queued closeout, and unreadable durable evidence refuses without scanning for substitutes.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- A legacy missing-intent direct-landing generation cannot be recovered or retried through the
  public tool; the typed refusal names the republish/retire route.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `direct_landing_tool` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:1-285 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `direct_landing_tool` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:1-285 |
| Refusal payloads forward the typed task-intent next action. | `_direct_error_payload`; `task_intent_recovery` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:119-141 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `direct_landing_tool` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:1-285 |

## CCR-R02@v2 Task-Intent Refusal Guidance

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, every consumer must return the
exact unavailable/stale reason and route the record through its canonical republish/retire
operation. `DirectLandingError.next_action` (owned by
`worktrees/integration/direct_landing/direct_landing_errors.py`) is the typed carrier, and the
error payload here surfaces it to the caller. Part of the landed L25 candidate `99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the direct-landing error payload now forwards the typed `nextAction` on task-intent refusals;
  documented the recovery-guidance seam and the missing-intent no-reuse boundary. Verified at code
  commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
