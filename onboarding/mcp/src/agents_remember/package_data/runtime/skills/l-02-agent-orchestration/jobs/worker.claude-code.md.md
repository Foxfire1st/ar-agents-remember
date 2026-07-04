# l-02-agent-orchestration/jobs/worker.claude-code.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/worker.claude-code.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T11:00+02:00                     |
| lastVerifiedCommitHash | `763ec25a77b4cdf44c87509c2d1baca3d275ba20` |
| lastVerifiedCommitDate | 2026-07-04T11:09:24+02:00|

## Purpose

This is the **per-harness overlay** for the worker seat when it runs on the **claude-code** harness. It
carries only what is harness-specific — the concrete knob values and the AR-mutations-stay-in-the-main-
loop idiom as it applies to a worker's own fan-out — and it **does not restate** the build spine, the
default-behavior rule, or the escalation ladder (read `jobs/worker.md` for those).

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-02-agent-orchestration/jobs/worker.claude-code.md`; it is model-interpreted markdown, never an
executor. Resolution base < harness variant < settings: `jobs/worker.md` (portable base) →
**this overlay** → `settings.json orchestration.roles.worker`. The body carries three things: a harness
knob table that overrides the base block (adds the `Agent`/`Task` sub-agent tool for read-only fan-out);
the **AR-mutations-stay-in-the-main-loop** rule scoped to the leaf — sub-agents fan out for **read/search
and write durable notes**, returning compact summaries, while **the worker's own main loop owns every
Agents Remember state mutation** (`worktree_attach`, native edits, `c-05-create-or-update-onboarding-files`
sidecar writes, `worktree_closeout_preview`/`_apply`, `worktree_integrate`, and the **mandatory turn
report**); and the fresh-session, state-not-transcript restatement (respawn onboards from the leaf
`task_doc` + the previous turn report, `templates/turn-report.md`).

### Conventions

Per-harness variant resolution (borrowed D12): the overlay adds harness-specific knobs and idioms on top
of the portable base and never restates the role's duties. The turn report is written **by the worker in
the main loop** from the sub-agents' summaries + its own work — never delegated to a sub-agent, because
it is the leaf's single artifact of record and must reflect the main loop's actual state.

### Invariants And Boundaries

A **sub-agent never mutates AR state**: it never edits the worktree, never writes a sidecar, never closes
out, never integrates, and never posts the turn report. Every AR state mutation is a **main-loop** call.
Continuity is durable state (task_doc + turn report), so a killed or compacted Claude Code worker session
loses nothing a successor cannot reconstruct from the report.

### Todos

No further harness-specific TODO is recorded for this overlay.

### Docs References

No external domain documentation applies to this repository-local orchestration job overlay.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The overlay resolves on top of the portable worker base within the frame.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [worker.claude-code.md](agents-remember/skills/l-02-agent-orchestration/jobs/worker.claude-code.md) |
| The portable worker base this file overlays (build spine · default-behavior rule · escalation ladder). | n/a | [worker.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/worker.md) |
| The frame that defines the per-harness variant resolution order and the knob block. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration job overlay.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-02-agent-orchestration` worker Claude Code overlay (leaf 260703-L1) — the harness knob overrides, the resolution order (base < variant < settings), and the AR-mutations-stay-in-the-main-loop rule (sub-agents fan out read-only and write durable notes; the worker's main loop owns every state mutation and the turn report). Verification metadata pinned until closeout stamps the L1 commit.
