# l-01-agent-lifecycles/roles/designer.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/designer.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T04:40+02:00 |
| lastVerifiedCommitHash | `314d21a8917decf942b302413e0cd31e8befec33` |
| lastVerifiedCommitDate | 2026-07-05T04:29:52+02:00|

## Purpose

The design lifecycle as a HAT the orchestrator pulls inline whenever design is needed - front of the pipeline or mid-flight. Not a seat: it cannot sit in a coordination leaf because the task is what it exists to create; no leaf, no worktree, no branch, no spawn required. A heavy design may run the same hat in a separate session (AR_SPAWN_ROLE=designer - chair logistics, not a role distinction).

## Code Commentary

### Logic

Sync-propagated copy of the canonical skills/l-01-agent-lifecycles/roles/designer.md. Content unchanged in substance: the tasks/AGENTS.md co-think doctrine as a job (meta-question, reframe, evidence-first via c-04), blast-radius bounded to the one master, task_doc authorship with a code example per distinct change, decision-needing questions into the task doc's openQuestions (notes/ carries the analysis), the declared master-scoped limit (cross-master collisions are owned downstream at the orchestrator's bulwark). Re-framed in this pass from seat to hat: headers and entry conditions name the orchestrator as the wearer, escalation is simply the handover into the portfolio job, and the knob table's harness row is 'the wearer's'.

As of the L8 de-harnessing pass the overlay-authoring sentence is gone: no per-harness designer files; the hat is fully portable.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-05T04:40+02:00 - L8 de-harnessing pass: overlay-authoring sentence removed (no per-harness files). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:15+02:00 - L8 orchestrator routes rework: re-framed from seat to hat (worn by the orchestrator, inline, mid-flight valid; separate chair = logistics); body rewritten accordingly. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed to roles/ under the unified skill; new duty: decision-needing questions land in the task doc's openQuestions (the rendered decision surface), notes/ carries the analysis. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` designer job file (leaf 260703-L1) — task design as its own job, the role + lens axes, the master-scoped bird's-eye toolkit whose residual cross/future-master collision risk is owned downstream by the orchestrator-as-reviewer at streamlining. Verification metadata pinned until closeout stamps the L1 commit.
