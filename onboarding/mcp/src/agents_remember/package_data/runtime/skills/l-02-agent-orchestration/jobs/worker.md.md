# l-02-agent-orchestration/jobs/worker.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/worker.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T11:00+02:00                     |
| lastVerifiedCommitHash | `763ec25a77b4cdf44c87509c2d1baca3d275ba20` |
| lastVerifiedCommitDate | 2026-07-04T11:09:24+02:00|

## Purpose

This is the portable **worker** job file the `l-02-agent-orchestration` frame houses at the leaf tier.
Like every job file it carries **both axes in one file** — the **role** (implement exactly one leaf,
short-lived) and the **lens** (the `l-01-session-job-lifecycle` build spine, worker lens) — plus an
opening move, duties, artifact obligations, a comms protocol, and a harness-agnostic knob block. A
harness overlay ships: `jobs/worker.claude-code.md`.

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-02-agent-orchestration/jobs/worker.md`; it is model-interpreted markdown, never an executor.
The body defines: the seat (**one per task leaf, short-lived, fresh session**, spawned by the manager and
onboarded from the **context packet + the `task_doc` — never from a transcript**; own harness + MCP
process, AmbientLifecycle singleton preserved, D11); the lens (opening move = `worktree_attach` and read
the leaf plan — **no reframe here**, the design was done upstream; retrieval lean = intent-confirmation
on the leaf's own files; decide default = build, the leaf is a build unit by construction); the
**default-behavior rule**; the six-step l-01 build spine (attach → implement per the leaf plan +
**refresh matching onboarding in the same pass** via the `c-05-create-or-update-onboarding-files` skill →
checks green before every incremental commit → closeout → integrate → turn report); the artifact
obligation; the comms protocol; and the knob block. The **closeout gate is decided by the MANAGER**
(delegated, attributed), not the developer; human review waits at the master/super seams. Continuity
lives in the `task_doc` + the turn report, not the session — which is why the worker can be short-lived
and respawned safely.

### Conventions

Role + lens in one file (D10); a portable knob block (D7) resolving job base < `jobs/worker.claude-code.md`
variant < `settings.json orchestration.roles.worker`. "Spine unchanged, lens specializes" (borrowed 260619
S8): the worker runs the ordinary l-01 build spine; the worker lens tunes it, it does not fork it. Comms
ride the inbox (receive the dispatch/context packet, post the turn report, raise escalations) plus stdin
push (the manager's nudges); replies are inbox rows or the turn-report artifact — **never an untracked
side channel**.

### Invariants And Boundaries

The worker is onboarded from **state, not a transcript**. A **MANDATORY turn-report artifact**
(`templates/turn-report.md`) is written at **every** hand-off — the worker's single most important
obligation; **a missing report is nudged by the manager**. Testing is never deferred — the
`system/tools.md` suite is green before every incremental commit. The **same default-behavior rule as the
manager applies: the default agent behavior stands, no creative-liberty prompting in either direction,
the SPIRIT TEST DOES NOT APPLY**, and a **plan delta beyond blank-filling escalates to the MANAGER**
(up the ladder — never a self-reshape, never straight to the developer).

### Todos

The build gate enforcement (delegated closeout attribution) is documented here but is **leaf L4**; until
it lands, the hand-off follows the `l-01-session-job-lifecycle` skill. No other TODO is recorded for this
job file.

### Docs References

No external domain documentation applies to this repository-local orchestration job file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The worker is spawned by the manager, has a Claude Code overlay, and runs the l-01 build spine.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [worker.md](agents-remember/skills/l-02-agent-orchestration/jobs/worker.md) |
| The frame that houses this seat and owns the escalation ladder, artifact obligations, and knob resolution. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/SKILL.md) |
| The Claude Code harness overlay resolved on top of this portable base. | n/a | [worker.claude-code.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/worker.claude-code.md) |
| The manager that spawns the worker, decides its delegated closeout gate, and nudges a missing turn report. | n/a | [manager.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/manager.md) |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration job file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-02-agent-orchestration` worker job file (leaf 260703-L1) — one short-lived fresh worker per leaf onboarded from context packet + task_doc (never a transcript), the l-01 build spine in the leaf worktree, the manager-decided closeout gate, the mandatory turn-report artifact, and the same default-behavior rule as the manager (spirit test does not apply; a plan delta escalates to the manager). Verification metadata pinned until closeout stamps the L1 commit.
