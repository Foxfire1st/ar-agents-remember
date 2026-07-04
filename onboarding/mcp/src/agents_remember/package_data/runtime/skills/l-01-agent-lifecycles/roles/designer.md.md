# l-01-agent-lifecycles/roles/designer.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/designer.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T01:30+02:00 |
| lastVerifiedCommitHash | `277f27a33b35aed8235cbb3c1ae2b5633cc88b22` |
| lastVerifiedCommitDate | 2026-07-05T01:30:08+02:00|

## Purpose

This is the portable **designer** job file the `l-01-agent-lifecycles` frame houses at the front of
the pipeline. Task design is registered as its **own job** (developer decision 2026-07-04): before
orchestration one implicit do-it-all role did design, features, and fixes; the roles now diversify and
the designer owns helping the developer think a master through. Like every job file it carries **both
axes in one file** — the **role** (co-think a master task with the developer) and the **lens**
(meta-question · reframe-before-execution · evidence-first, the `tasks/AGENTS.md` collaboration
doctrine given a job shape) — plus an opening move, duties, artifact obligations, a comms protocol, and
a harness-agnostic knob block.

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/roles/designer.md`; it is model-interpreted markdown, never an executor.
The body defines: the seat (front of the pipeline, scoped to **one master**); the lens (opening move =
meta-question the ask; retrieval lean = evidence-first within the master's scope; decide default = a
`w-02-light-task-workflow`-shaped master + leaf `task_doc` handed into the portfolio, **not** a build);
six duties (reframe with `tasks/AGENTS.md`, evidence-first master-scoped, blast-radius WITHIN the master,
author the `task_doc`, declare the designer limit, ask never fill silently); the artifact obligations
(the `task_doc`, a designer-limits note, durable fan-out evidence reports); the comms protocol (the
developer is the standing interlocutor in the attached chat; handover joins the portfolio); and the knob
block. The designer shares the orchestrator's **bird's-eye toolkit** (route indexes · onboarding ·
`grepai_search` · `cgc_*` · blast-radius) but is **scoped to one master**, so cross-master and —
especially — **future-master** collisions can slip a single-master view; that residual risk is **owned
downstream, not here**: at portfolio streamlining the **orchestrator doubles as the designer's
adversarial reviewer** (planned-vs-planned and planned-vs-past). The designer's duty is to *declare* the
limit, not to close it.

### Conventions

Role + lens in one file (borrowed D10); a portable knob block (D7) whose defaults resolve job base <
`roles/designer.<harness>.md` variant < `settings.json orchestration.roles.designer`. Unlike the deeper
seats that relay through the ladder, the designer's primary channel is the **developer directly** — the
seat is a co-thinking loop, so the developer is the standing interlocutor. Evidence is gathered through
the `c-04-retrieval-strategy-router` skill, not ad-hoc reads; sub-agents fan out and write durable
reports.

### Invariants And Boundaries

The designer is **scoped to one master**; cross-master and future-master reasoning is explicitly out of
its reach. It **declares** the master-scoped blind spot on the doc (never hides it) so the orchestrator's
later adversarial pass can close it. It **asks, never fills silently** — assumptions and truth gaps only
the developer can resolve are surfaced as a short, high-leverage list. It **designs, it does not
implement**: the decide default is a `task_doc` into the portfolio, never a build.

### Todos

No `roles/designer.<harness>.md` overlay ships yet; author one when a harness needs designer-specific
knobs. No other TODO is recorded for this job file.

### Docs References

No external domain documentation applies to this repository-local orchestration job file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The designer job is housed by the frame and its residual risk is closed by the orchestrator seat.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [designer.md](agents-remember/skills/l-01-agent-lifecycles/roles/designer.md) |
| The frame that houses this seat and defines the job registry, contact points, and knob resolution. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md) |
| The orchestrator seat doubles as the designer's adversarial reviewer at portfolio streamlining and shares the bird's-eye toolkit. | n/a | [orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md) |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration job file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed to roles/ under the unified skill; new duty: decision-needing questions land in the task doc's openQuestions (the rendered decision surface), notes/ carries the analysis. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` designer job file (leaf 260703-L1) — task design as its own job, the role + lens axes, the master-scoped bird's-eye toolkit whose residual cross/future-master collision risk is owned downstream by the orchestrator-as-reviewer at streamlining. Verification metadata pinned until closeout stamps the L1 commit.
