# l-01-agent-lifecycles/roles/strategist.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T23:45+02:00 |
| lastVerifiedCommitHash | `9d58058e3ce4815b0356794fc21973ebe9c71345` |
| lastVerifiedCommitDate | 2026-07-06T11:47:10+02:00|

## Purpose

This is the portable **strategist** role file the `l-01-agent-lifecycles` frame houses at the
portfolio tier — the SPRINT PLANNER (developer-named 2026-07-05; ruled mandatory 2026-07-06). Like
every role file it carries both axes in one file — the **role** (verify the in-flight master set is
coherent, resolve dependency chains, establish blast radius, shuffle leaves, deliver the
orchestration task) and the **lens** (mechanical phases with real tools; judgment phases with
mandatory citations) — plus duties, artifact obligations, a comms protocol, and a knob block. The
central doctrine the card must protect: **a strategist run is a MANDATORY precondition for any
orchestrated run** (even a single master gets the pass), and the strategist is a **reader, not a
mutator** — it drafts the orchestration task as a notes artifact; the orchestrator adopts it.

## Code Commentary

### Logic

L13 review follow-up (L13R-1): the knob table's `harness` example is the registry id `claude` (was the non-id `claude-code`); spawn refuses non-registry values, so examples must model valid input.

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/roles/strategist.md`; it is model-interpreted markdown, never an
executor. The body defines: the seat (**spawn-first by design** — portfolio analysis is
token-heavy and must not burn the orchestrator's context; the designer's inline-hat precedent
explicitly does NOT apply; spawned with `AR_SPAWN_ROLE=strategist`); the loop position (the
portfolio three-party loop's BUILDER: owner = orchestrator, reviewer = the plan-review criteria
catalog); the **eight-phase method** as the operating procedure — 1 inventory (JSON-primary task
docs + series contracts + notes), 2 **two-sided touch-surface extraction** (existing surfaces map
against the route map `onboarding/**/overview.md` + `overview.index.json`; NEW/greenfield surfaces
map by DECLARATION — parent route + intended shape, the L9 `serving/notes.py` precedent;
"unplannable as scoped" fires only when a leaf can name neither), 3 structural dependency analysis
with `cgc_dependencies`/`cgc_callers`/`cgc_callees` + `grepai_search`/`grepai_trace` +
`cgc_complexity` producing an evidence-cited EDGE LIST (ORDER / CONFLICT / INDEPENDENT; new-surface
edges from declaration cross-reference), 4 cited semantic/doctrine edges (an uncited edge is
refutable by default), 5 the blast-radius register (low/medium/high — the input to the owning
seat's loop-tier scoring), 6 the cross-master coherence/contradiction sweep (directional
contradictions are quo-vadis → developer), 7 topological ordering with leaf moves (from→to +
rationale) and parallel waves, 8 the orchestration task with shown work. Six duties run brief
intake → portfolio read → analysis → the orchestration task → drawing-board rounds (multi-round
convergence expected; the drawing board IS this loop's escalation; 3-full-round cap) →
adopted-plan handover (round 2, L12R-8: the artifact write is unconditional; the inbox is the
delivery channel when the brief wires it, otherwise the final playback message carries the ref). Re-evaluation rules: an in-sprint master added before implementation starts
re-plans; an out-of-sprint master waits for the next sprint.

### Conventions

Role + lens in one file (D10); a portable knob block (D7, highest-reasoning / high-effort — the
sprint plan parameterizes every downstream loop) resolving role-file defaults <
`settings.json orchestration.roles.strategist`. The brief carries **refs to durable portfolio
state, never pasted state**. Comms ride the inbox (brief context in, artifact refs out) + stdin
push for round feedback.

### Invariants And Boundaries

**READER, NOT MUTATOR.** The tool surface is stated positively: read-only AR retrieval
(`read_ar_files`, `grepai_*`, `cgc_*`, `context_packet`, `drift_check`), native reads, native
writes ONLY to the own draft artifact, inbox. No `task_doc`, no `worktree_*`, no `lifecycle_*`, no
gates, no spawn, no git — a seat that never touches mutating AR tools never instantiates a
lifecycle (the designed shape). **No orchestration task, no orchestrated run** — the mandatory
pre-run is doctrine, not a knob. Citation discipline binds the judgment phases: every claimed
edge carries a citation, and thin leaf scopes become explicit "unplannable as scoped" findings,
never silent guesses.

### Todos

No TODO is recorded for this role file. Wiring the orchestration task as a first-class
dashboard/task-doc kind is deferred to the L14 hierarchy work (proven at the L15 pilot).

### Docs References

No external domain documentation applies to this repository-local orchestration role file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The strategist is spawned by the orchestrator before any orchestrated run and hands its plan back
for adoption.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [strategist.md](agents-remember/skills/l-01-agent-lifecycles/roles/strategist.md) |
| The frame that houses this seat, the role registry row, and the three-party-loop doctrine home. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md) |
| The orchestrator that dispatches the strategist (Job P mandatory pre-run) and adopts the plan. | n/a | [orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md) |
| The deliverable's template — the orchestration task with the shown-work requirements. | n/a | [orchestration-task.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md) |
| The plan-review criteria catalog the loop's reviewer runs against the orchestration task. | n/a | [plan-review.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/plan-review.md) |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-06T23:45+02:00 — L13 adversarial-review follow-up (L13R-1): knob-table harness example fixed to the registry id `claude`. Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-8): duty 6 aligned with the Tool Surface — the orchestration-task artifact write is unconditional; inbox posting is the when-wired delivery channel, the final playback message the fallback. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `roles/strategist.md` (leaf 260703-L12): the spawn-first sprint planner, mandatory precondition for any orchestrated run; the eight-phase method with two-sided touch surfaces and evidence-cited edges; reader-not-mutator boundary; drawing-board rounds with the 3-full-round cap. Verification metadata pinned until closeout stamps the L12 commit.
