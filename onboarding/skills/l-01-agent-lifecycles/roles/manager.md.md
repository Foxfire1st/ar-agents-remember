# skills/l-01-agent-lifecycles/roles/manager.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/roles/manager.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T14:20+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/roles/overview.md` |

## Governing Overview

[roles overview](overview.md)

## Purpose

The manager is one persistent seat on one canonical master document. It owns that master's leaf
execution and closeout chain: dispatch workers, verify builder evidence, obtain independent review,
obtain curator coherence, decide delegated leaf gates, close out and integrate leaves, and hand the
completed master to the orchestrator.

## Logic

For each dependency-ready real leaf, the manager calls structural `dispatch_agent` with the leaf
document, role, and complete brief. The control plane owns readiness and the exact-pinned initial
brief; the manager never requests or stores an occupant id. The manager gathers builder code/report,
reviewer verdict, and curator coherence report before closeout. It runs leaf-scoped quality at leaf
altitude and the full wrapper once at master integration altitude.

When all leaves land, an adversarial master-exit verdict becomes evidence on the handover seam; the
manager writes the master-handover packet and remains reachable at `(master document, manager)`.
Ordinary follow-ups and escalations use structural child/parent messaging so replacements are
transparent.

## Conventions

- One manager sees one master, not the portfolio.
- Independent leaves dispatch in parallel unless a named dependency or one-writer constraint applies.
- Builder, reviewer, and curator are distinct real leaf seats with distinct artifacts.
- Delegated decisions are attributed; human-only gates remain human-owned.
- Completed subordinate seats may be reclaimed only after their durable report exists.

## Invariants And Boundaries

- Manager identity is the canonical master document plus `manager` role.
- Manager never becomes a native sub-agent, worker, reviewer, curator, orchestrator, or architect.
- Manager may retire only its own master's worker/reviewer/curator child seats.
- Manager does not self-approve, bypass blocked checks, or invent portfolio-wide authority.
- Handover and completion rely on durable artifacts and terminal/finalizer truth, not model completion posts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One manager owns one canonical master and the complete leaf closeout chain. | "## What This Seat Is" | skills/l-01-agent-lifecycles/roles/manager.md:10-30 |
| Hosted child dispatch uses leaf document, role, and complete brief without retained occupant ids. | "## Hosted Role Dispatch" | skills/l-01-agent-lifecycles/roles/manager.md:41-47 |
| The leaf loop sequences builder, reviewer, curator, closeout, integration, and cleanup duties. | "### 2 — Leaf dispatch loop (per leaf)" | skills/l-01-agent-lifecycles/roles/manager.md:94-182 |
| Master exit and handover use durable verdict/packet evidence and structural ownership. | "### 3 — Master-exit seam"; "### 4 — Handover to the orchestrator" | skills/l-01-agent-lifecycles/roles/manager.md:184-211 |
| Structural parent/child messages are the role's communication path. | "## Comms Protocol" | skills/l-01-agent-lifecycles/roles/manager.md:219-232 |

## Update History

- 2026-08-11T14:20+02:00 — Rewrote the default body around real-master ownership, structural child
  dispatch, and the builder/reviewer/curator closeout chain; removed duplicate history and task deltas.
- 2026-08-10T07:30+02:00 — Durable reports became the precondition for subordinate cleanup.
- 2026-08-08T02:00+02:00 — Leaf and master quality checks were assigned to their proper altitudes.
- 2026-07-12T14:20+02:00 — Established the self-contained one-master manager lifecycle.
