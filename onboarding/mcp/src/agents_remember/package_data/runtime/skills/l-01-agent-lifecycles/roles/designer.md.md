# l-01-agent-lifecycles/roles/designer.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/designer.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T17:40+02:00 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77` |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|

## Purpose

The design lifecycle as a HAT the architect pulls inline whenever design is needed - front of the
pipeline or mid-flight. Not a coordination leaf by default: it cannot sit in a coordination leaf
because the task is what it exists to create; no leaf, no worktree, no branch, no spawn required. A
heavy design may run the same hat in a separate session (AR_SPAWN_ROLE=designer - chair logistics,
not a role distinction).

## Code Commentary

### Logic

Sync-propagated copy of the canonical skills/l-01-agent-lifecycles/roles/designer.md. Content remains the tasks/AGENTS.md co-think doctrine as a job (meta-question, reframe, evidence-first via c-04), blast-radius bounded to the one master, task_doc authorship with a code example per distinct change, decision-needing questions into the task doc's openQuestions (notes/ carries the analysis), and the declared master-scoped limit (cross-master collisions are owned downstream at the backend orchestrator's bulwark). HFX-L6 changes the wearer from orchestrator to architect, adds role-seat immutability for spawned designer sessions, and makes the primary channel the architect chat/relay.

As of the L8 de-harnessing pass the overlay-authoring sentence is gone: no per-harness designer files; the hat is fully portable.

As of cycle 4 the knob footer resolution reads role-file defaults < settings (dead variant rung removed).

As of cycle 5: the knob tools row gains the inbox (the no-brief announce path is executable).

### L16 Knob Additions

260703-L16: the Knobs table gains the three FREE-FORM rows (`launchArgs` — verbatim harness argv;
`sessionCommands` — lines pasted + submitted into the fresh session before the brief;
`promptKeywords` — prepended as the first line of the dispatch brief paste; all settings-only,
never validated, recorded in spawn provenance), and the knob footer now names the per-level
override (`orchestration.rolesPerLevel.<level>.<role>`; role-file defaults < settings < level
override) plus the `docs/reference/harnesses.md` spawn-knobs manual.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.


## Update History

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
