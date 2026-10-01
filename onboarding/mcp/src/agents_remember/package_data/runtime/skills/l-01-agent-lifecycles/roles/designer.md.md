# l-01-agent-lifecycles/roles/designer.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the optional sprint-bound designer lifecycle. The canonical
`skills/l-01-agent-lifecycles/roles/designer.md` owns the role; the sync process publishes this
exact artifact without a separate packaged interpretation.

The packaged role is now a **self-contained lifecycle in the corpus's readable order** — purpose and
authority → required inputs → normal workflow → permitted writes and actions → stop and escalation
cases → completion and handoff, then its machine-readable knob block. It declares its shared sources
with `**Inherits:**` rather than restating them (`core/authority.md`, `core/invariants.md`,
`core/loop.md`, `core/acceptance.md`, `operations/orientation.md`, `operations/planning.md`). The
reframing and evidence-first design method it applies now lives once in `operations/planning.md`, and
its altitude is stated structurally: the designer is **a HAT the architect pulls inline**, with a
separate sprint chair optional, and it produces task/design artifacts without a worktree.

**This role file names no sibling role file.** The corpus forbids learning one's own obligations from
another seat's prose; only wearing a hat or dispatching that seat may cite `roles/<other>.md`, and the
shipped check fails on any other reference.

## Code Commentary

### Logic

The architect may create or switch to `(sprint document, designer)` through one `dispatch_agent`
call when design deserves a dedicated conversation; an identity-free launcher may target it only
for explicit developer-declared takeover. Otherwise the architect may apply the same drawing-board
method inline. A dispatched
designer remains designer, creates task/design artifacts without a worktree, and returns durable
artifacts to the architect. `message_parent` carries clarification or escalation without revealing
an occupant id. The dispatch/tools rows are structural documentation rather than settings keys.

### Conventions

The designer works evidence-first, keeps scope at the sprint/design boundary, and hands durable
artifacts back to the architect. Edit the canonical role and synchronize this runtime copy.

### Invariants And Boundaries

- The designer role is task-document-and-role bound, not leaf-key or session-id addressed.
- Inline architect design is hat collapse; a dispatched designer never absorbs another role.
- This packaged artifact must remain byte-identical to the canonical role.

### Todos

None recorded.

## Evidence

### Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

No meaningful cross-repo references found.

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.
