# l-02-agent-orchestration/jobs/orchestrator.claude-code.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/orchestrator.claude-code.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T11:00+02:00                      |
| lastVerifiedCommitHash | `763ec25a77b4cdf44c87509c2d1baca3d275ba20` |
| lastVerifiedCommitDate | 2026-07-04T11:09:24+02:00|

## Purpose

This file is the per-harness **overlay** for the orchestrator seat when it runs on the **claude-code**
harness. It carries only what is harness-specific — the concrete knobs, the sub-agent fan-out mechanic,
and the durable-report rule — and does **not** restate the orchestrator's duties, spirit test, or
topology (those live in `jobs/orchestrator.md`). Resolution: base job < harness variant < settings.json
orchestration block.

## Code Commentary

### Logic

This packaged file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-02-agent-orchestration/jobs/orchestrator.claude-code.md`; the authored skill source owns the
wording, and this is the synced runtime mirror.

The overlay sits between the portable `jobs/orchestrator.md` base and the settings.json orchestration
block (resolution: `jobs/orchestrator.md` → **this overlay** → settings.json). Harness knobs override
the base knob block: harness `claude-code`; model = the strongest available reasoning model (the
concrete id named by settings.json `orchestration.roles.orchestrator.model`); effort `high`; tools =
full tool surface + the `Agent`/`Task` sub-agent tool for fan-out.

The **sub-agent fan-out with durable reports** idiom maps the design record's addendum item 5 to this
harness: the orchestrator's portfolio analysis fans out through the **`Agent`/`Task` sub-agent tool**,
where each fan-out analysis (route-coherence scan, conflict/regression scan, per-designer adversarial
review) is dispatched as a sub-agent that **WRITES** a templated durable report
(`templates/impact-analysis.md`, `templates/onboarding-coherency.md`) and returns only a compact
summary — the report is the artifact of record, the returned summary is not. This keeps the
orchestrator's context from exploding and makes the analysis survive compaction, a session clear, or
termination. A sub-agent that only returns prose is a bug; if the analysis matters it lands as a durable
report file, and a sub-agent may not be the sole holder of a finding. **AR state mutations stay in the
main loop**: sub-agents never call the mutating Agents Remember MCP tools (no `task_doc` writes, no gate
decisions, no `spawn_agent_session`, no closeout) — those are the orchestrator's own main-loop calls
made after reading the sub-agents' durable reports; sub-agents are read-and-write-reports actors and the
orchestrator is the only mutator. Fan-out is capped by settings.json
`orchestration.concurrency.maxSubAgents`. Prefer **continuing an existing sub-agent** (its report
already in flight) over spawning a fresh one for a follow-up on the same analysis, so the durable report
accretes rather than fragmenting across files.

### Conventions

Per-harness job variant (borrowed D12): a `jobs/<role>.<harness>.md` overlay carries only
harness-specific content (concrete knobs, the fan-out mechanic, tool-surface specifics) and never
restates the role's duties. It is one of the two exemplars that ship (with
`jobs/worker.claude-code.md`).

### Invariants And Boundaries

The overlay is additive over the base and does not redefine the seat's duties. Sub-agents write durable
report artifacts and may not be the sole holder of a finding (prose-only return is a bug). **AR state
mutations stay in the main loop** — the orchestrator is the only mutator; sub-agents never call the
mutating AR MCP tools. Fan-out is capped by settings.json `orchestration.concurrency.maxSubAgents`.
`spawn_agent_session` is the L2 spawn tool and is **not yet implemented** — a main-loop call, never a
sub-agent's.

### Todos

No current todo is recorded in this job variant file.

### Docs References

No external domain documentation applies to this repository-local job variant.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This overlay resolves on top of the portable orchestrator job and is selected by the frame's
per-harness variant resolution.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file overlays the portable orchestrator job; read that file for the seat's duties, spirit test, and topology. | L11-L23 | [jobs/orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/orchestrator.md) |
| The frame's variant resolution (job base < harness variant < settings.json) is what layers this overlay over the base and under the settings block. | L231-L243 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/SKILL.md) |
| Fan-out sub-agents write into the report-template library this overlay names (impact analysis, onboarding coherency). | n/a | [templates/impact-analysis.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/templates/impact-analysis.md) |

## Cross-Repo References

No sibling repository evidence is needed for this repository-local job variant.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-04T11:00+02:00 — Created file-level onboarding for the new `l-02-agent-orchestration` skill's
  Claude Code orchestrator overlay (leaf 260703-L1), the per-harness variant resolved between the
  portable base job and the settings.json orchestration block. Captured the harness knobs (the
  `Agent`/`Task` sub-agent tool for fan-out) and the sub-agent fan-out rule: sub-agents WRITE durable
  report artifacts while AR state mutations (`task_doc`, gates, spawn, closeout) stay in the main loop,
  fan-out capped by `orchestration.concurrency.maxSubAgents`; noted the overlay does not restate the
  seat's duties. Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-02-agent-orchestration/jobs/orchestrator.claude-code.md`. Verification metadata pinned until
  closeout stamps the L1 commit.
