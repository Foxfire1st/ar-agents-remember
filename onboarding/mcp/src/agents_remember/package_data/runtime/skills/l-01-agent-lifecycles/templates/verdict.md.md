# l-01-agent-lifecycles/templates/verdict.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/verdict.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-11T15:20+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|

## Purpose

This template is the **adversarial reviewer's** artifact of the `l-01-agent-lifecycles` report-template library. It lands under the series `notes/reports/` directory and attaches to the handover gate as **judge evidence** at either of the two review seams — **master-exit** (before a manager hands to the orchestrator) and **super-exit** (before the orchestrator hands to the developer). The two variants now share rules but carry different review shapes because master-exit reviews one completed master branch while super-exit reviews the accumulated super branch. Since 260703-L12 round 2 the template also serves three-party-loop reviews via the Loop-Review Adaptation note (master-exit shape minus the gate machinery; decider = the loop owner) and forces the criteria-catalog results the reviewer doctrine demands.

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-01-agent-lifecycles/templates/verdict.md`. It carries a prose header naming the writer (`roles/reviewer.md`), a numbered **Rules** block, and two fenced variants. The **Master-Exit Variant** records the master integration branch, master/leaf task docs, recommendation, decider, artifact path, and exact gate evidence ref (`kind=reviewer-verdict`, `ref=...`, `verdict=...`), then reviews completion against master task docs, code quality for the master branch, onboarding-vs-code for master-side sidecars/route overviews, ranked refute-tested findings, and manager fix leaves for a BLOCK. The **Super-Exit Variant** records the super branch, portfolio/master task docs, recommendation, decider, artifact path, and the same gate evidence ref shape, then reviews portfolio completion, whole-super branch quality, accumulated onboarding/carry-over/ledger coherence, ranked findings, and orchestrator-routed fix leaves for a BLOCK. As of 260703-L12 round 2 (L12R-3) BOTH variants carry a **Criteria Catalog Results** section (one row per bound criterion — Criterion id · catalog · Ran · Finding · Evidence — plus a proposed-amendments line for the promotion ratchet), Rule 6 makes reporting every bound catalog criterion mandatory (the binding table lives in `roles/reviewer.md`), and a closing **Loop-Review Adaptation** section defines the loop-review shape: the master-exit variant minus the gate-evidence row and Judge-Evidence Note, decider = the loop owner (owning seat / orchestrator for the plan review), delta-verifies appending a dated delta section to the same artifact.

### Conventions

Every finding is **refute-or-confirm**: it must survive an attempt to refute it, findings are ranked, and each cites a backing evidence file. All three lenses (completion · code quality · onboarding-vs-code) are covered explicitly, even to state a lens is clean. Regressions are checked against the past via route indexes, `cgc`, and `grepai`. The gate evidence reference is part of the artifact contract, not optional prose.

### Invariants And Boundaries

A verdict is **evidence, not a decision**: it states an explicit pass / pass-with-notes / block **recommendation**, and the gate's **decider** (manager, orchestrator, or developer per L4 policy) decides — the verdict is never written as if it were the gate outcome. A **BLOCK must decompose into fix leaves** (concrete, leaf-shaped findings the owning manager/orchestrator can dispatch); a block that cannot be named as fix leaves is invalid and resolves to pass-with-notes or names the leaves. Prose-only complaints are not a valid block.

### Todos

No TODO markers are present in this report template.

### Docs References

No external domain documentation applies to this repository-local report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This bundle copy is the shape the adversarial-reviewer job writes at each seam; its lenses cite the impact-analysis and onboarding-coherency backing reports.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | `# Verdict Template (adversarial reviewer)` | skills/l-01-agent-lifecycles/templates/verdict.md:1-142 |
| The adversarial reviewer writes this verdict at the master-exit and super-exit seams as judge evidence. | "as judge evidence"; `### MASTER-EXIT — Manager Before Orchestrator Handover` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:105-125; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:165-165 |
| The master-exit completion and code-quality lenses name impact-analysis and quality/impact backing evidence. | "# Adversarial Verdict — master-exit"; `# Impact-Analysis Template` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/impact-analysis.md:1-52; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/verdict.md:68-68 |
| The master-exit onboarding lens names a backing onboarding-coherency report. | "# Adversarial Verdict — master-exit"; `# Onboarding-Coherency Template` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/onboarding-coherency.md:1-48; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/verdict.md:68-68 |
| The frame defines the two seams and the evidence-not-decision doctrine (SKILL.md) and the block-decomposes-into-fix-leaves doctrine (the reviewer role). | "verdicts are evidence"; "A master-exit block without fix leaves is invalid" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:195-195; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:123-124 |

As of cycle 4 the decider rows are ruled: master-exit = orchestrator (delegated master-handover-approval; serious issues escalate to the developer); super-exit = developer (human review concentrates at the super gate); the reviewer role file reference is roles/reviewer.md.

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-14T06:34+02:00 — L23 synchronized runtime template: verdicts identify the reviewed route,
  exact candidate, surrounding ownership, forcing evidence, and delta-review disposition.

- 2026-08-11T15:20+02:00 — Rebound both backing-report rows to the unique master-exit variant and
  the referenced template headings; the paired super-exit copy no longer makes provenance ambiguous.
- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 5 citation rows; the judge-evidence row was re-bound from the removed roles/adversarial-reviewer.md to roles/reviewer.md (L31-L36 + the seam rubrics L90-L135), the fix-leaf doctrine split to SKILL.md L190-L201 plus reviewer.md L109-L111, and the stale role-file mention in Logic corrected. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-3): Rule 6 (report every bound catalog criterion) + the Criteria Catalog Results section in both variants + the Loop-Review Adaptation note (master-exit shape minus gate machinery; decider = loop owner; delta sections append). The ruled-deciders shape is unchanged. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): decider rows ruled per the seam decision; L4 shorthand replaced. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed under l-01-agent-lifecycles/templates/; role-file reference now roles/adversarial-reviewer.md. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T13:16+02:00: 260703-L6 split the verdict shape into explicit master-exit and super-exit
  variants, added evidence-file and gate-evidence-ref fields, and made BLOCK fix-leaf decomposition
  seam-specific for the manager or orchestrator owner. Verification metadata pinned until closeout
  stamps the L6 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` verdict report template (leaf 260703-L1) — the adversarial reviewer's master-exit/super-exit artifact that is evidence not a decision, whose BLOCK must decompose into fix leaves, covering the completion/code-quality/onboarding-vs-code lenses under a refute-or-confirm posture. Verification metadata pinned until closeout stamps the L1 commit.
