# l-01-agent-lifecycles/templates/deep-research-report.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/deep-research-report.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-28T07:20+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l30-ar`, uncommitted; base `7dcec036094768c5f50e571fb45e59a27ae78efc` |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80` |
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|

## Purpose

This companion file provides the reusable report shape for deeper research in the `l-01-agent-lifecycles` skill. It keeps the main lifecycle compact by owning the full and compact report templates, evidence-ledger format, proof inventory, evidence kind taxonomy, evidence limits, and final lifecycle decision summary.

## Code Commentary

### Logic

The file starts by defining when to use the compact versus full shape. The full shape captures the frame, short answer, findings, evidence ledger, proof inventory, remaining truth gaps, and lifecycle decision. The compact shape preserves the same essential answer/evidence/truth-gap/decision structure for smaller research-only exits. The evidence ledger records source/query, claim proven, and limits so reports are claim-first rather than tool-call logs.

### Conventions

Findings use `F-xx` identifiers, evidence rows use `E-xx` identifiers, and findings cite evidence IDs. Evidence kinds are intentionally aligned with the lifecycle's retrieval strategy language: Semantics, Relationship, and Intent, with additional kinds for external references, executable validation, developer clarification, and inference.

### Invariants And Boundaries

This file owns formatting, not lifecycle gating. The lifecycle still owns when deeper research happens, the required proof categories, the plan gate, and the build-mode decision. Evidence rows must name what they prove and what they do not prove so the report does not overclaim.

### Todos

No current todo is recorded for this deep research report template.

## Docs References

No external domain documentation applies to this repository-local lifecycle report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The template is a companion to the lifecycle entry contract and the detailed spine.

| Finding | Anchor | Source |
| --- | --- | --- |
| The entry contract lists this file in the `templates/…` companion-file line as one of the shapes spawning seats compile briefs from. | `## Companion Files` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:126-144 |
| The entry contract lists this file in the `templates/…` companion-file line as one of the shapes spawning seats compile briefs from; the router shrank from 620 to 179 lines in 260915-CAPS-L1, so the anchor is rebased. | "## Which Lifecycle Am I? (the router — exactly three conditions, in order)" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:24-66 |
| The template defines report rules, full and compact shapes, evidence kinds, and evidence-ledger guidance. | `# Deep Research Report Template` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/deep-research-report.md:1-123 |

As of cycle 4 the decision block asks for the suggested artifact shape (minimal w-02 task vs master + series) instead of the retired 'build mode' axis.

## Cross-Repo References

No sibling repository evidence is needed for this lifecycle report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-09-20T01:33+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared the enforced `citation_claim_reopened` row this card carried by reading the claim and disposing of the three mechanical projections that held it open.** The claim — *"The entry contract lists this file in the `templates/…` companion-file line as one of the shapes spawning seats compile briefs from"* — was re-read against the bytes its range covers: the anchor `## Companion Files` resolves at `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:126`, inside the cited `:126-144`, and that section's `templates/…` bullet (`:133-136`) names `deep-research-report` among the field schemas the spawning seats compile briefs from. The wording is RETAINED, and the sibling row above it (`## Which Lifecycle Am I? …` at `:24-66`) is unaffected. **Three mechanical anchor-range projection bullets — 2026-09-18T10:45:13 (`:126-144`), 2026-09-17T06:49:47 (`:599-614`) and 2026-09-09T12:22:46 (`:573-588`) — were retired**: each recorded a tool projection rather than a reading, and the newest of the three wrote exactly the range verified here; the extents they wrote stay recorded in the 2026-09-16T08:01+02:00 CAPS-L1 entry below. **The two commit rows were replaced by one `reviewedWorkingCandidate` row** because the body has been rewritten since `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` — the projections moved this range — so that stamp no longer evidences the bytes it sits beside; no hash was invented and no stamp advanced. The cited `…/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md` is byte-identical to this leaf's base `7dcec036`, so the construct read here is the construct at the substituted base. No Finding text, anchor, range or other row was changed.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: Repaired citations this leaf falsified: the canonical lifecycle corpus was consolidated (the router shrank 620 → 179 lines; all nine role files and several templates were rewritten), so the cited anchors and ranges no longer resolved. No behavioral claim changed — the cited rule was re-pointed at its current home. Verification metadata remains closeout-owned. `## Companion Files` now cites `SKILL.md:125-142`; the previous `:573-588` exceeded the router's 179 lines.

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 2 citation entries (4 findings); no Tier-3 findings.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 citations and DELETED 1 whose material
  is gone, after the `l-01-session-job-lifecycle` skill was renamed to `l-01-agent-lifecycles` and
  its files moved into `templates/` and `roles/`. Repointed the entry-contract row to
  `l-01-agent-lifecycles/SKILL.md` L376-L383 (the `templates/…` companion-file bullet, where
  `deep-research-report` is now named on L381) and reworded it to match what SKILL.md actually
  says. Fixed the self-citation link, which pointed at the retired skill path; its L12-L123 range
  is still exact (Report Rules at L12 through the end of Evidence Ledger Guidance at L123 in a
  123-line file). **Deleted** the row "The lifecycle delegates report shape to this template while
  preserving its required proof categories" (was `lifecycle.md` L87-L97): `lifecycle.md` no longer
  exists and nothing replaced that delegation — a full-tree grep for `deep-research`, `proof`,
  `report shape` and `evidence ledger` across `SKILL.md`, `lenses.md`, all nine `roles/` files and
  all five `criteria/` files finds this template's own L3-L6 self-description and one bare listing
  on SKILL.md L381, and no lifecycle-side statement of required proof categories at all. Also
  corrected the Purpose paragraph's stale `l-01-session-job-lifecycle` skill name.

- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): retired build-mode vocabulary replaced with artifact shape. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: moved from the retired l-01-session-job-lifecycle skill into the shared template library and renamed deep-research-report.md; used by the orchestrator lifecycle's research phase. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-04T14:50+02:00: Created file-level onboarding for the new deep research report template companion file. Verification metadata is intentionally blank until closeout refreshes it to the first code commit containing the new source file.
