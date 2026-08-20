# l-01-agent-lifecycles/roles/strategist.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-20T05:10+02:00 |
| lastVerifiedCommitHash | `2f494982971091a18023a0ecdb2a532a4201a7c5` |
| lastVerifiedCommitDate | 2026-08-20T00:11:16+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the optional sprint-bound strategist lifecycle. The canonical
`skills/l-01-agent-lifecycles/roles/strategist.md` owns doctrine; the sync process publishes this
exact runtime artifact.

## Code Commentary

### Logic

After developer approval, the architect may dispatch `(sprint document, strategist)`. The
strategist is read-only: it analyzes portfolio dependencies and drafts the orchestration task,
`message_parent` carries clarification or quo-vadis escalation to the architect, the architect rules
the plan, and the orchestrator adopts it. The role never edits task docs, raises gates, mutates Git,
or addresses an orchestrator occupant.

### Conventions

Use cited evidence for dependency and coherence claims, preserve the draft/adoption boundary, and
edit only the canonical role before synchronization.

### Invariants And Boundaries

- The strategist remains a sprint-bound reader, not a mutator or orchestrator child.
- Durable artifacts, not runtime identity, carry the result across occupant replacement.
- This packaged artifact must remain byte-identical to the canonical role.

### Todos

None recorded.

## Repo-Internal References

When approved, the strategist is spawned by the orchestrator and hands its plan back for adoption.

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | `# Lifecycle — Strategist` | skills/l-01-agent-lifecycles/roles/strategist.md:1-204 |
| The frame that houses this seat, the role registry row, and the three-party-loop doctrine home. | `## The Role Registry`; `## The Three-Party Loop (one home — this section owns the loop doctrine)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:95-112; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:190-248 |
| The orchestrator that dispatches an approved strategist, adopts its plan, or authors the orchestration task after a sanctioned skip. | `# Lifecycle — Orchestrator` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:1-463 |
| The deliverable's template — the orchestration task with the shown-work requirements. | `# Orchestration-Task Template` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md:1-91 |
| The plan-review criteria catalog the loop's reviewer runs against the orchestration task. | `# Criteria Catalog — Plan Review (the strategist loop)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/plan-review.md:1-84 |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260815-DAG-L14 Doctrine Sync

The strategist adoption payload is updated to the atomic `attach_master` flow and the first-class
sprint seats structure.

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.

## 260815-DAG-L2 Evidence-Cited Topology Planning

Initial facts are architect-compiled; runtime-reshape facts arrive from the orchestrator through
the architect. The strategist classifies organizational versus atomic execution, builds the exact
activity-on-node graph, and records dependency meaning, blast radius, priority, blockers,
reprioritization, and leaf moves in one canonical Judgment Register. Every selected graph relation
cites evidence and its owning judgment id; large size alone never makes a master atomic.

## Update History

- 2026-08-20T05:10+02:00 — 260815-DAG-L14: adoption payload updated to the atomic
  `attach_master` flow and seats structure. Verified at code commit 2f494982.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: synchronized fact/judgment separation, graph-edge
  traceability, and dependency/risk-driven master classification. Verification remains
  closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `strategist.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 6 citation anchors across 5 reference claims; scoped recheck clean (0 findings).

- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-10T02:39+02:00 — HFX3/L14 combined curation: superseded mandatory-precondition wording
  with architect-proposed, developer-approved dispatch; preserved reader-not-mutator and the
  unconditional artifact duty of an already-running strategist; recorded the orchestrator-owned
  sanctioned-skip path and added the governing-overview backlink. Verification metadata remains
  pinned until closeout stamps the eventual two-parent code commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: added
  role-seat immutability; clarified that drawing-board feedback and quo-vadis contradictions go
  through the architect relay while the strategist remains the reader-not-mutator portfolio
  planner for backend orchestration. Sync-propagated bundle copy. Verification metadata pinned
  until closeout stamps the HFX-L6 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): Knobs table gained the three
  free-form escape-hatch rows (launchArgs / sessionCommands / promptKeywords, settings-only, never
  validated) and the knob footer now includes the rolesPerLevel per-level override and the
  harnesses.md manual pointer. Sync-propagated bundle copy. Verification metadata pinned until
  closeout stamps the L16 commit.

- 2026-07-06T23:45+02:00 — L13 adversarial-review follow-up (L13R-1): knob-table harness example fixed to the registry id `claude`. Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-8): duty 6 aligned with the Tool Surface — the orchestration-task artifact write is unconditional; inbox posting is the when-wired delivery channel, the final playback message the fallback. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `roles/strategist.md` (leaf 260703-L12): the spawn-first sprint planner, mandatory precondition for any orchestrated run; the eight-phase method with two-sided touch surfaces and evidence-cited edges; reader-not-mutator boundary; drawing-board rounds with the 3-full-round cap. Verification metadata pinned until closeout stamps the L12 commit.
