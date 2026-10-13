# core/lifecycle-frame.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Current source contract evidence

- Current source declarations support the qualified naming or fixture account; no executed test or acceptance is inferred. [2]

## Purpose

The shipped minimal lifecycle frame describes effects/signals, dispatch-time seat binding,
trust intake and response ownership. It does not advertise removed lifecycle MCP tools.

## Code Commentary

The signal table describes fleeting start, phase movement, developer handoff, persistent
promotion by worktree start, re-adoption, unsaved-work disposition and terminal recording
as effects rather than model tool calls. Lifecycle correlation is server-side and belongs
to the seat's own contract. A non-mutating spawned seat need not instantiate one; no seat
adopts or advances another seat's lifecycle. Dispatch binding is a separate identity fact.

Architect/orchestrator trust intake reports repository/memory/drift/freshness before relying
on managed context; spawned roles consume the compiled facts instead of rerunning it.
The trust checkpoint calls context_packet with include_drift and include_freshness, without include_providers or provider-state reporting. Provider-start/degradation prose remains as legacy source residue, not provider execution authority. Those are not current permission to invoke removed provider/lifecycle tools or
supply removed arguments to the candidate's advertised context-packet schema. Retired
providers perform no normal install/start/index/watch; preserve report/order/no-kill safety
boundaries without teaching the obsolete setup route as implemented.

## Current evidence

- Current instruction contract and retained-read replacement, not historical provider/tool examples. [1]

## Historical superseded body (non-operative)

The following text is the prior onboarding account, retained for provenance.
It is not current setup, query, publication, or tool-call guidance; the current
contract above replaces its provider/tool/database and hook generalizations.



The shared **minimal lifecycle frame**: the six signals every session shares, which seats run them,
the opening trust checkpoint, and how every seat meets a provider degradation.

## Code Commentary

### Logic

The signal table maps `lifecycle_start` (fleeting, one per session, no id), `lifecycle_phase` (the
phase axis), `lifecycle_turn_end_notification` (set `awaiting-developer`, return immediately, and the
**next turn's first AR call auto-resumes**), the automatic `worktree_start` promotion to persistent,
`worktree_attach`, the `switch_lifecycle` save gate, and the terminal `lifecycle_end`.

Two rules carry the most weight for every other file: a tool call outside any lifecycle is **dropped,
never misattributed**, and **a spawned role that never touches a mutating AR tool simply never
instantiates a lifecycle** — that is the designed shape, not a gap. `## Which signals a seat runs` maps
each seat class onto that rule, and `## The trust checkpoint` binds the four-step
`context_packet` / report / drift / provider opening detail to the architect and orchestrator only.

`## Provider degradation, as every seat meets it` is the shared response protocol: a
`degradation-alert` pauses provider **starting**, leaf-altitude seats stop starting providers and hold
**no kill authority**, and the orchestrator owns investigation dispatch, the remediation order, and the
stop.

### Conventions

A role file binds whether its seat runs the trust checkpoint; a spawned role never repeats it,
because its spawner compiles the facts into the brief.

### Invariants And Boundaries

- A tool call outside any lifecycle is dropped, never misattributed; `paused` is system-owned.
- A spawned role runs its own lifecycle when it runs one and never adopts its spawner's.
- Seat binding is the dispatch-time catalog binding, not lifecycle adoption.
- A holder of one lifecycle never advances another seat's.
- Leaf-altitude seats never start providers while a degradation-alert is live and hold no kill authority.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

| The six-signal frame and the dropped-call rule. | `## The Minimal Lifecycle Frame` | skills/l-01-agent-lifecycles/core/lifecycle-frame.md:1-38 |
| The four-step trust checkpoint bound to the architect and orchestrator. | `## The trust checkpoint` | skills/l-01-agent-lifecycles/core/lifecycle-frame.md:40-56; skills/l-01-agent-lifecycles/core/lifecycle-frame.md:39-39 |
| The provider-degradation response protocol every seat meets. | `## Provider degradation, as every seat meets it` | skills/l-01-agent-lifecycles/core/lifecycle-frame.md:57-70 |

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
