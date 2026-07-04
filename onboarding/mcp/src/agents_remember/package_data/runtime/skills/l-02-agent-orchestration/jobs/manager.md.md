# l-02-agent-orchestration/jobs/manager.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/manager.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T11:00+02:00                     |
| lastVerifiedCommitHash | `763ec25a77b4cdf44c87509c2d1baca3d275ba20` |
| lastVerifiedCommitDate | 2026-07-04T11:09:24+02:00|

## Purpose

This is the portable **manager** job file the `l-02-agent-orchestration` frame houses at the master
tier. Like every job file it carries **both axes in one file** — the **role** (drive exactly one master
series) and the **lens** (leaf loop: dispatch · review · delegated gates · master-exit handover) — plus
an opening move, duties, artifact obligations, a comms protocol, and a harness-agnostic knob block. The
central doctrine the card must protect: **the spirit test does NOT apply to the manager** — the default
agent behavior stands, with no creative-liberty prompting in either direction.

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-02-agent-orchestration/jobs/manager.md`; it is model-interpreted markdown, never an executor.
The body defines: the seat (**one per master task**, its own coordination leaf + chat, **no worktree**);
the lens (opening move = read the master `task_doc` + leaf docs and order the leaves; retrieval lean =
intent-confirmation on the master's own routes, no bird's-eye view; decide default = dispatch the next
ready leaf, exit through the master-exit seam); the **default-behavior rule**; four duty blocks; the
artifact obligations; the comms protocol; and the knob block. The leaf dispatch loop spawns a **fresh
worker per leaf**, monitors for the mandatory turn-report artifact (missing → a rate-limited stdin
nudge), reviews the artifact vs the `task_doc` (the manager's own **leaf-level review — explicitly not an
adversarial seam**), decides the leaf's **DELEGATED** gates **attributed** (`decidedBy: <manager
lifecycle>`, `decidedVia: orchestration`; the owning agent never self-approves, a distinct configured
role — the manager — may), and integrates leaf → master integration branch via the
`c-11-memory-carryover-from-branch` skill. At master exit it spawns the **adversarial reviewer**
(master-exit seam); a blocking verdict **decomposes into fix leaves** the manager dispatches, and
verdicts are **evidence, not decisions** (the manager decides the handover gate with the verdict as judge
evidence). It then posts the **master-handover packet** (`templates/master-handover-packet.md`) up to the
orchestrator.

### Conventions

Role + lens in one file (D10); a portable knob block (D7) resolving job base <
`jobs/manager.<harness>.md` variant < `settings.json orchestration.roles.manager`. Coordination seat =
an ordinary `subTask` leaf with no enclosure and a role marker; comms ride the inbox (durable, dashboard-
visible) plus stdin push (nudges/messages into hosted worker sessions, poll as fallback). Gate delegation
is documented here but **enforced in leaf L4**; until then hand-offs follow the
`l-01-session-job-lifecycle` skill.

### Invariants And Boundaries

**The spirit test does NOT apply to this seat — it is orchestrator-only.** The manager gets **no
creative-liberty prompting in either direction**: the **default agent behavior stands** (fulfill the
task, fill small unambiguous blanks a competent implementer would fill, and no more). A **plan delta
beyond blank-filling ESCALATES to the orchestrator** — never a reshape, and **never straight to the
developer**. The manager has **no bird's-eye view** (one master, not the portfolio); the breadth /
blast-radius reasoning belongs to the orchestrator. The **owning agent never self-approves**; the manager
decides its leaves' delegated gates as the distinct configured role. Escalation resolves within the
master's own view first, then rises up the ladder to the orchestrator.

### Todos

No `jobs/manager.<harness>.md` overlay ships yet; author one when a harness needs manager-specific knobs.
No other TODO is recorded for this job file.

### Docs References

No external domain documentation applies to this repository-local orchestration job file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The manager spawns workers, spawns the master-exit reviewer, and hands its master up to the orchestrator.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [manager.md](agents-remember/skills/l-02-agent-orchestration/jobs/manager.md) |
| The frame that houses this seat and owns the escalation ladder, gate-delegation doctrine, and the two adversarial seams. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/SKILL.md) |
| The worker seat the manager spawns fresh per leaf and whose turn report it reviews. | n/a | [worker.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/worker.md) |
| The adversarial reviewer spawned at the master-exit seam, whose blocking verdict decomposes into fix leaves the manager dispatches. | n/a | [adversarial-reviewer.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/adversarial-reviewer.md) |
| The orchestrator seat the manager escalates to and hands the completed master over to. | n/a | [orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/orchestrator.md) |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration job file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-02-agent-orchestration` manager job file (leaf 260703-L1) — one manager per master, the leaf dispatch loop with delegated attributed gates and C-11 integration, the master-exit adversarial seam and handover packet, and the critical rule that the spirit test does NOT apply here (default behavior stands; a plan delta escalates to the orchestrator, never the developer). Verification metadata pinned until closeout stamps the L1 commit.
