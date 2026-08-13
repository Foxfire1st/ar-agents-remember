# skills/l-01-agent-lifecycles/roles

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `skills/l-01-agent-lifecycles/roles` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-11T14:40+02:00 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|

## Purpose

This route owns the self-contained lifecycle for each role. Every file states what one seat is,
which task-document altitude it occupies, the loop and artifacts it owns, its communication path,
and the work it must refuse or escalate.

## Hot Path Summary

Architect owns sprint-level direction. Orchestrator owns the portfolio and manager topology.
Manager occupies one canonical master and drives the leaf closeout chain. Worker occupies one leaf
and produces code plus a turn report. Reviewer produces independent verdict evidence. Curator
occupies one leaf coherence pass and reconciles existing intent, ruled intent, and implemented
reality into onboarding. Other specialist roles retain their own documented altitude and artifact.

Manager, orchestrator, and worker doctrine shares one quality altitude rule:
leaf checks remain targeted, while the once-per-master full wrapper keeps
pytest `-n=auto` and host-managed RAM/swap unless constrained CI explicitly
configures a hard cap.

The curator's terminal artifact is valid only after current-additions coverage and the full
leaf-scoped memory-quality worklist have been repaired and rerun. Expected dirty-source drift and
real-commit verification fields remain separately closeout-owned; they do not excuse a repairable
onboarding or citation finding.

Roles are immutable within dashboard-owned seats. Horizontal role expansion uses structural
dispatch to another document+role seat; native sub-agents, when allowed by a hands-on role, remain
read/search helpers and never become AR role seats.

## Conventions

- A role file is complete enough to start from its brief without transcript history.
- The source role files are canonical; packaged copies are exact synchronization outputs.
- Each role writes its artifact of record and communicates structurally one rung at a time.
- Shared dispatch/authority doctrine remains in the parent `SKILL.md`.

## Invariants And Boundaries

- Manager owns a real master; worker/reviewer/curator own real leaves.
- Role replacement preserves the task-document/role address.
- Builder, reviewer, curator, and owner duties remain separate.
- Curator completion requires the required missing-onboarding and full-quality reruns to name no
  curator-actionable work.
- No role absorbs lifecycle machinery, memory duty, or gate authority assigned to another role.
- Terminal/finalizer truth and durable artifacts, not model completion posts, signal completion.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Curator is a fresh conservative coherence seat with onboarding-only writes and a mandatory pre-closeout repair-and-rerun loop. | "# Lifecycle — Curator"; "### 4 — Iterate The Checklist, Then Report" | skills/l-01-agent-lifecycles/roles/curator.md:1-47; skills/l-01-agent-lifecycles/roles/curator.md:136-191 |
| Manager is one master-scoped owner of the builder/reviewer/curator closeout chain. | "# Lifecycle — Manager" | skills/l-01-agent-lifecycles/roles/manager.md:1-47 |
| Worker is one leaf-scoped builder whose terminal artifact is the turn report. | "# Lifecycle — Worker" | skills/l-01-agent-lifecycles/roles/worker.md:1-33 |
| The shared registry enumerates every remaining role file. | "## The Role Registry" | skills/l-01-agent-lifecycles/SKILL.md:95-111 |

## L23 Role Recovery Semantics

Architect guidance treats a resumed thematic master behind super as a sync of
the same master, while manager guidance requires current master and leaf edges
before reading or delegating work. Both rely on plane-owned task identity and
never pass branch/commit/session ids between roles.

## Update History
- 2026-08-12T20:20+02:00 — L23 curator: documented architect/manager lineage recovery and dispatch boundaries; verification remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 route impact: manager,
  orchestrator, and worker quality-altitude doctrine now uses host-managed
  master memory by default and keeps leaf checks targeted. Verification
  metadata remains pinned until closeout stamps L24.

- 2026-08-11T14:40+02:00 — Made the curator's missing-onboarding and full-quality repair-and-rerun
  obligation part of the role route's current contract, with commit-derived stamps left to closeout.
- 2026-08-11T14:10+02:00 — Replaced task-delta sections with direct current role ownership,
  altitude, artifact, and separation contracts.
- 2026-08-10T07:30+02:00 — Durable reports became the cleanup precondition for short-lived seats.
- 2026-08-09T12:08+02:00 — Role-local watcher/ladder prose was superseded by fact relay.
- 2026-07-12T14:20+02:00 — Established the governing role-route overview.
