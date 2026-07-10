# l-01-agent-lifecycles/templates/turn-report.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/turn-report.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-08T23:59+02:00 |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce` |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|

## Purpose

This template is the **mandatory worker hand-off artifact** of the `l-01-agent-lifecycles` report-template library. A worker fills it at **every** hand-off so a leaf's work survives session death and a respawned successor onboards from **state, not the transcript**. It is the leaf's single artifact of record; a missing turn report is nudged by the HFX2-L2 supervisor sweep, never by a manager watching for it (uniform-mechanism ruling 2026-07-07).

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-01-agent-lifecycles/templates/turn-report.md`. It has three parts: a prose header naming the artifact and its writer (`roles/worker.md`), a numbered **Rules** block, and a fenced **Shape** the worker copies verbatim — a metadata table (leaf / master / worker / worktree / status / checks / written) followed by the sections *What Was Done*, *Issues Hit*, *Solved On The Spot*, *What Is Left*, *Onboarding Refreshed*, *Escalations*, and the closing **Respawn State** block that onboards a successor from state alone.

### Conventions

The report is written in the **main loop** from the worker's own work plus any sub-agent summaries — never delegated to a sub-agent. It states facts (what changed, what broke, what is proven green, what remains) rather than a narrative, and lives durably in the series notes (`notes/reports/<leaf>-worker-report.md`), referenced from the leaf `task_doc` and posted through the inbox with `messageKind: turn-report`.

### Invariants And Boundaries

The report is mandatory at every hand-off, and a missing one is nudged — by the HFX2-L2 supervisor
sweep mechanically, never a manager hand-rolling its own watch over the artifact (uniform-mechanism
ruling 2026-07-07, 260707-HFX2-L5). The **Respawn State** section must let a fresh successor continue **without reading any transcript**. A plan delta beyond blank-filling does not belong in *Solved On The Spot* — it is escalated to the manager and recorded under *Escalations*.

### Todos

No TODO markers are present in this report template.

### Docs References

No external domain documentation applies to this repository-local report template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This bundle copy is the shape the worker job writes at every hand-off; the frame catalogs it as a per-role artifact obligation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | n/a | [turn-report.md](agents-remember/skills/l-01-agent-lifecycles/templates/turn-report.md) |
| The worker writes the turn report in the main loop at every hand-off; it is the leaf's single artifact of record. | n/a | [worker.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md) |
| The frame lists the mandatory worker turn report among the per-role artifact obligations. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-08T23:59+02:00 — 260707-HFX2-L5 (doctrine rewrite, active vigilance → passive
  process-and-ack): "A missing turn report is nudged by the manager" reworded to name the HFX2-L2
  supervisor sweep as the actual mechanism, never a manager watching for it (uniform-mechanism
  ruling 2026-07-07); Invariants And Boundaries updated to match. Doctrine-only change set (5
  canonical `skills/` files synced to 9 downstream copies, 0 Python); sync-propagated bundle copy of
  the canonical `skills/l-01-agent-lifecycles/templates/turn-report.md`. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L5 commit.

- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed under l-01-agent-lifecycles/templates/; role-file reference now roles/worker.md. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T12:31+02:00 - L3: pinned the default
  `notes/reports/<leaf>-worker-report.md` artifact path and `turn-report` inbox
  message-kind convention. Verification metadata pinned until closeout stamps
  the L3 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` turn-report report template (leaf 260703-L1) — the mandatory worker hand-off artifact whose Respawn State onboards a successor from state, not the transcript. Verification metadata pinned until closeout stamps the L1 commit.
