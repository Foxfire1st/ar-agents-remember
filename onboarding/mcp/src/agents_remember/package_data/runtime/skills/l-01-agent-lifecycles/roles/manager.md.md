# l-01-agent-lifecycles/roles/manager.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T19:55+02:00 |
| lastVerifiedCommitHash | `91b29d026a5733cc3ccea3d3275efd5057334f64` |
| lastVerifiedCommitDate | 2026-07-05T18:49:20+02:00|

## Purpose

This is the portable **manager** job file the `l-01-agent-lifecycles` frame houses at the master
tier. Like every job file it carries **both axes in one file** — the **role** (drive exactly one master
series) and the **lens** (leaf loop: dispatch · review · delegated gates · master-exit handover) — plus
an opening move, duties, artifact obligations, a comms protocol, and a harness-agnostic knob block. The
central doctrine the card must protect: **the spirit test does NOT apply to the manager** — the default
agent behavior stands, with no creative-liberty prompting in either direction.

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/roles/manager.md`; it is model-interpreted markdown, never an executor.
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
`roles/manager.<harness>.md` variant < `settings.json orchestration.roles.manager`. Coordination seat =
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

No `roles/manager.<harness>.md` overlay ships yet; author one when a harness needs manager-specific knobs.
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
| Canonical source this bundle copy is sync-propagated from. | n/a | [manager.md](agents-remember/skills/l-01-agent-lifecycles/roles/manager.md) |
| The frame that houses this seat and owns the escalation ladder, gate-delegation doctrine, and the two adversarial seams. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md) |
| The worker seat the manager spawns fresh per leaf and whose turn report it reviews. | n/a | [worker.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md) |
| The adversarial reviewer spawned at the master-exit seam, whose blocking verdict decomposes into fix leaves the manager dispatches. | n/a | [adversarial-reviewer.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/adversarial-reviewer.md) |
| The orchestrator seat the manager escalates to and hands the completed master over to. | n/a | [orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md) |

As of the 260703-L8 reopened pass the file carries two additions: a flat-run note (in a flat series the ORCHESTRATOR wears this hat — same duties, same artifacts, one chair) and the reopen-and-reshape rule in the leaf-review bullet (a leaf whose deliverable came out wrong is reopened under its own id via task_reopen and its doc reshaped — never duplicated into a redo sibling; new leaves are for genuinely new changes).

As of the L8 de-harnessing pass the overlay-authoring sentence is gone and the knob harness row is a preference settings overrides: no per-harness manager files.

As of cycle 4 the master-exit procedure is operable as-built: the manager RAISES the `master-handover-approval` gate (delegable, never human-pinned) with the verdict attached as evidenceRefs, and the ORCHESTRATOR decides it — identity mechanics stated (raiser = the manager's ambient lifecycle; the deciding orchestrator's ambient identity becomes decidedBy; owner-never-self-approves holds; no ids handled). The leaf loop now names the human-pinned kinds (integration-approval, push-approval, cleanup-approval) and marks the integrate step's durable-gate behavior; reviewer spawns state AR_SPAWN_ROLE=reviewer; finalize wording is honest (statuses via the tool, steps by hand); the knob footer resolution is role-file defaults < settings.

As of cycle 5: the seam channel is exact: raise with lifecycle_gate(..., wait=false) → carry the returned gateId in the handover packet; identity truth restated (gate ids are model-visible, lifecycle ids stay server-side); the integrate-step sentence now defines the series' standing approval (the developer's portfolio-gate approval recorded in the planner master) and the seat's own hand-off idiom (gates + inbox, never the developer-facing notification). Cycle 6 completes the raise's address: §3's call now carries `enclosure="<master task name>"` — the master identity integration enforcement matches the gate by — and adds the all-human conditional (under an all-human policy the raise blocks and the developer decides; do not pass wait=false). Cycle 7 pins the address as a contract, not a convention: §3 now states the match is exact-string — the EXACT master task name as the contracts carry it (`worktree_start`'s `task_name`) — and that a wait=false raise without an enclosure is refused.

## Cross-Repo References

No sibling repository evidence is needed for this orchestration job file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-05T19:55+02:00 - L8 builder cycle 7: §3 pins the enclosure as the EXACT contract task name (exact-string match) and states the enclosure-less raise refusal (AR4-1c). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: §3 raise now carries enclosure=<master task name> (the integration guard's address) + the do-not-pass-wait=false-under-all-human conditional (AR3-1/AR3-2). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the seam channel is exact: raise with lifecycle_gate(..., wait=false) → carry the returned gateId in the handover packet. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): master-exit seam made operable (raise-with-verdict -> orchestrator decides); human-pinned kinds enumerated at the integrate step; reviewer spawn value stated. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 - L8 de-harnessing pass: overlay-authoring sentence removed (no per-harness files). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:15+02:00 - L8 orchestrator routes rework: flat-run note added (in a flat series the orchestrator wears this hat) and the leaf-review bullet gained the reopen-and-reshape rule (task_reopen a wrong deliverable, never a redo sibling). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: the manager now owns the leaf lifecycle END-TO-END (worker closeout stripped; worktree_start -> closeout/gates -> integrate -> finalize incl. task-doc steps); master-exit reviewer spawn procedure inlined; gate policy described as-built; briefs compiled from templates/worker-brief.md with AR_SPAWN_ROLE + the qualified leaf key. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` manager job file (leaf 260703-L1) — one manager per master, the leaf dispatch loop with delegated attributed gates and C-11 integration, the master-exit adversarial seam and handover packet, and the critical rule that the spirit test does NOT apply here (default behavior stands; a plan delta escalates to the orchestrator, never the developer). Verification metadata pinned until closeout stamps the L1 commit.
