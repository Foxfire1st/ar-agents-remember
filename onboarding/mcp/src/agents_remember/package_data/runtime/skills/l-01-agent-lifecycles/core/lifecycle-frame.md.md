# core/lifecycle-frame.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Current source contract evidence

- The packaged frame is byte-equal to the canonical current worktree-only contract account; no executed acceptance is inferred. [2]

## Purpose

The shipped minimal lifecycle frame describes contract-owned lifecycle adoption through worktree tools, role-start seat binding, trust intake and response ownership. It does not advertise removed lifecycle MCP tools or independent fleeting/phase/developer-handoff signals.

## Code Commentary

The current table has three contract effects: worktree_start adopts the new contract’s lifecycle, worktree_attach re-adopts an existing contract, and close records completed or abandoned. Nothing else begins, blocks or hands over a lifecycle. A role that calls neither worktree tool has no lifecycle; no role adopts or advances its starter’s or another seat’s lifecycle. role_start seat binding is separate: Architect starts without a document, and other roles use their canonical selection.

Architect/orchestrator trust intake reports repository/memory/drift/freshness before relying
on managed context; started roles consume the AR handover’s task facts and workspace bindings instead of rerunning it. Drift maintenance on committed non-dirty source is approval-gated through role_message up the parent chain.
The trust checkpoint calls context_packet with include_drift and include_freshness, without include_providers or provider-state reporting. Provider-start/degradation prose remains as legacy source residue, not provider execution authority. Those are not current permission to invoke removed provider/lifecycle tools or
supply removed arguments to the candidate's advertised context-packet schema. Retired
providers perform no normal install/start/index/watch; preserve report/order/no-kill safety
boundaries without teaching the obsolete setup route as implemented.

## Current evidence

- Worktree tools alone adopt the current contract lifecycle, while role-start binding is separate. [1]

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
