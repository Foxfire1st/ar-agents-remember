# l-02-agent-orchestration/templates/verdict.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/templates/verdict.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T11:00+02:00                     |
| lastVerifiedCommitHash | `763ec25a77b4cdf44c87509c2d1baca3d275ba20` |
| lastVerifiedCommitDate | 2026-07-04T11:09:24+02:00|

## Purpose

This template is the **adversarial reviewer's** artifact of the `l-02-agent-orchestration` report-template library. It attaches to the handover gate as **judge evidence** at either of the two review seams — **master-exit** (before a manager hands to the orchestrator) and **super-exit** (before the orchestrator hands to the developer) — which share one shape.

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-02-agent-orchestration/templates/verdict.md`. It carries a prose header naming the writer (`jobs/adversarial-reviewer.md`) and the two seam variants, a numbered **Rules** block, and a fenced **Shape**: a metadata table (seam / scope / reviewer / task docs / recommendation / decider / written) followed by the three lens sections — *Lens 1 Completion vs Task Docs*, *Lens 2 Code Quality*, *Lens 3 Onboarding vs Code* — then *Findings (ranked; each refute-tested)*, *If BLOCK — Fix Leaves (decomposed, leaf-shaped)*, and a *Judge-Evidence Note*. The completion and code-quality lenses cite a backing `templates/impact-analysis.md` artifact; the onboarding lens cites a backing `templates/onboarding-coherency.md` artifact.

### Conventions

Every finding is **refute-or-confirm**: it must survive an attempt to refute it, findings are ranked, and each cites its backing sub-agent report. All three lenses (completion · code quality · onboarding-vs-code) are covered explicitly, even to state a lens is clean. Regressions are checked against the past via route indexes, `cgc`, and `grepai`.

### Invariants And Boundaries

A verdict is **evidence, not a decision**: it states an explicit pass / pass-with-notes / block **recommendation**, and the gate's **decider** (manager, orchestrator, or developer per L4 policy) decides — the verdict is never written as if it were the gate outcome. A **BLOCK must decompose into fix leaves** (concrete, leaf-shaped findings the owning manager/orchestrator can dispatch); a block that cannot be named as fix leaves is invalid and resolves to pass-with-notes or names the leaves. Prose-only complaints are not a valid block.

### Todos

No TODO markers are present in this report template.

### Docs References

No external domain documentation applies to this repository-local report template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This bundle copy is the shape the adversarial-reviewer job writes at each seam; its lenses cite the impact-analysis and onboarding-coherency backing reports.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | n/a | [verdict.md](agents-remember/skills/l-02-agent-orchestration/templates/verdict.md) |
| The adversarial reviewer writes this verdict at the master-exit and super-exit seams as judge evidence. | n/a | [adversarial-reviewer.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/adversarial-reviewer.md) |
| Lens 1/2 cite a backing impact-analysis report. | n/a | [impact-analysis.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/templates/impact-analysis.md) |
| Lens 3 cites a backing onboarding-coherency report. | n/a | [onboarding-coherency.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/templates/onboarding-coherency.md) |
| The frame defines the two seams and the evidence-not-decision / block-decomposes-into-fix-leaves doctrine. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-02-agent-orchestration` verdict report template (leaf 260703-L1) — the adversarial reviewer's master-exit/super-exit artifact that is evidence not a decision, whose BLOCK must decompose into fix leaves, covering the completion/code-quality/onboarding-vs-code lenses under a refute-or-confirm posture. Verification metadata pinned until closeout stamps the L1 commit.
