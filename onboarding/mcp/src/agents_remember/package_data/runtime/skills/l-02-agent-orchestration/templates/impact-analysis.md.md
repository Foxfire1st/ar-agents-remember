# l-02-agent-orchestration/templates/impact-analysis.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/templates/impact-analysis.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T11:00+02:00                     |
| lastVerifiedCommitHash | `763ec25a77b4cdf44c87509c2d1baca3d275ba20` |
| lastVerifiedCommitDate | 2026-07-04T11:09:24+02:00|

## Purpose

This template is the **integrity-bulwark** report of the `l-02-agent-orchestration` report-template library. A fan-out sub-agent writes it for the **orchestrator** (portfolio phase) or the **adversarial reviewer** (completion + code-quality lenses), covering the change's blast radius on **two axes**: planned-vs-planned and planned-vs-past.

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-02-agent-orchestration/templates/impact-analysis.md`. It carries a prose header naming its consumers and the write-vs-mutate rule, a numbered **Rules** block, and a fenced **Shape**: a metadata table (for / author / subject / written) followed by *Surface Swept*, a *Planned-vs-Planned* collisions table (with other masters/leaves, incl. FUTURE), a *Planned-vs-Past* regression-surface table, an *Evidence Inventory* (route indexes, `cgc` queries, `grepai` queries, paired `read_ar_files` reads), and a *Bottom Line* for the spawning agent's main loop.

### Conventions

The report is **evidence-first**: every finding cites the route indexes, `cgc_*` queries, `grepai_search` queries, and `read_ar_files` reads that back it, and each finding states its **limits** — what the evidence does not prove.

### Invariants And Boundaries

This is a **report, not a decision** — it feeds the orchestrator's spirit test / reshape proposals or the reviewer's verdict; it never decides. **Sub-agents WRITE it; AR state mutations** (`task_doc`, gates, spawn, closeout) stay in the **spawning agent's main loop**. It must cover both axes: planned-vs-planned (collision with another master/leaf, present or future) and planned-vs-past (the "fixed one, broke two" regression surface).

### Todos

No TODO markers are present in this report template.

### Docs References

No external domain documentation applies to this repository-local report template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This bundle copy is written by fan-out sub-agents and consumed by the orchestrator's integrity bulwark and the reviewer's completion lens.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | n/a | [impact-analysis.md](agents-remember/skills/l-02-agent-orchestration/templates/impact-analysis.md) |
| The orchestrator's portfolio integrity bulwark consumes this report; its fan-out sub-agents write it while AR mutations stay in the orchestrator main loop. | n/a | [orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/orchestrator.md) |
| The adversarial reviewer's completion + code-quality lenses cite this report as backing evidence. | n/a | [adversarial-reviewer.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/adversarial-reviewer.md) |
| The frame's artifact-obligation doctrine keeps AR mutations in the main loop while sub-agents write templated reports. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-02-agent-orchestration` impact-analysis report template (leaf 260703-L1) — the integrity-bulwark report over two axes (planned-vs-planned incl. FUTURE masters, and planned-vs-past regression surface), evidence-first and a report not a decision, written by sub-agents while AR mutations stay in the spawning agent's main loop. Verification metadata pinned until closeout stamps the L1 commit.
