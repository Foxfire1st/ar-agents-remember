# mcp/src/agents_remember/application/lifecycle/direct_landing.py

## Governing Overview

[Application lifecycle overview](overview.md)

## Purpose

Publishes the direct-landing application tool and its recovery guidance over the durable operation journal.

## Code Commentary

### Logic

It validates configured series authority and the current canonical-leaf grant, invokes verify-existing or exact-pair create mode, and reads canonical journal projections for recovery guidance. Typed nextAction/detail is preserved on refusals; the adapter does not authorize from settings, hide an accepted cut or retry with a different generation. Historical task-intent recovery is retained where applicable, not a substitute for direct grant/generation authority.

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

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- No external domain source is required to establish this repository-owned implementation. [1]

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- The module's concrete API, control flow, and validation boundary are implemented here. [2]
- Refusal payloads forward the typed task-intent next action. [3]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [4]

## CCR-R02@v2 Task-Intent Refusal Guidance

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, every consumer must return the
exact unavailable/stale reason and route the record through its canonical republish/retire
operation. `DirectLandingError.next_action` (owned by
`worktrees/integration/direct_landing/direct_landing_errors.py`) is the typed carrier, and the
error payload here surfaces it to the caller. Part of the landed L25 candidate `99dc249b`.

- The application boundary preserves current grant admission and journal-owned direct recovery. [5]
