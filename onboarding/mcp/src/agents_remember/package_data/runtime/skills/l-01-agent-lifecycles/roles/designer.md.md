# l-01-agent-lifecycles/roles/designer.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/designer.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-30T12:34+02:00 |
| lastVerifiedCommitHash | `f9f92ca793811b6cb738d7e302dfecdf8636e96e` |
| lastVerifiedCommitDate | 2026-08-30T14:26:46+02:00|

## Purpose

Packaged runtime copy of the optional sprint-bound designer lifecycle. The canonical
`skills/l-01-agent-lifecycles/roles/designer.md` owns the role; the sync process publishes this
exact artifact without a separate packaged interpretation.

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

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.

## Update History

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 replaced stale Operations creation with
  architect-owned dispatch, separated explicit ambient takeover, and fixed structural-row
  ownership. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `designer.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: the designer
  hat is now pulled by the architect, not the backend orchestrator; spawned designer seats keep
  role-seat immutability; handoff goes through the architect to the backend orchestrator's
  portfolio review. Sync-propagated bundle copy. Verification metadata pinned until closeout
  stamps the HFX-L6 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): Knobs table gained the three
  free-form escape-hatch rows (launchArgs / sessionCommands / promptKeywords, settings-only, never
  validated) and the knob footer now includes the rolesPerLevel per-level override and the
  harnesses.md manual pointer. Sync-propagated bundle copy. Verification metadata pinned until
  closeout stamps the L16 commit.

- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the knob tools row gains the inbox (the no-brief announce path is executable).. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): knob footer variant rung removed. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 - L8 de-harnessing pass: overlay-authoring sentence removed (no per-harness files). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:15+02:00 - L8 orchestrator routes rework: re-framed from seat to hat (worn by the orchestrator, inline, mid-flight valid; separate chair = logistics); body rewritten accordingly. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed to roles/ under the unified skill; new duty: decision-needing questions land in the task doc's openQuestions (the rendered decision surface), notes/ carries the analysis. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` designer job file (leaf 260703-L1) — task design as its own job, the role + lens axes, the master-scoped bird's-eye toolkit whose residual cross/future-master collision risk is owned downstream by the orchestrator-as-reviewer at streamlining. Verification metadata pinned until closeout stamps the L1 commit.
