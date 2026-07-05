# l-01-agent-lifecycles/templates/deep-research-report.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/deep-research-report.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T16:20+02:00 |
| lastVerifiedCommitHash |                                            `19d76dbd73673ffc72d0ee1b6a868ac2fdf15ad0`|
| lastVerifiedCommitDate |                                            2026-07-05T16:23:40+02:00|

## Purpose

This companion file provides the reusable report shape for deeper research in the `l-01-session-job-lifecycle` skill. It keeps the main lifecycle compact by owning the full and compact report templates, evidence-ledger format, proof inventory, evidence kind taxonomy, evidence limits, and final lifecycle decision summary.

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The template is a companion to the lifecycle entry contract and the detailed spine.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The entry contract lists this file as the reusable report and evidence-ledger shape for deeper research. | L29-L33 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |
| The lifecycle delegates report shape to this template while preserving its required proof categories. | L87-L97 | [lifecycle.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/lifecycle.md) |
| The template defines report rules, full and compact shapes, evidence kinds, and evidence-ledger guidance. | L12-L123 | [deep-research-report.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/deep-research-report.md) |

As of cycle 4 the decision block asks for the suggested artifact shape (minimal w-02 task vs master + series) instead of the retired 'build mode' axis.

## Cross-Repo References

No sibling repository evidence is needed for this lifecycle report template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): retired build-mode vocabulary replaced with artifact shape. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: moved from the retired l-01-session-job-lifecycle skill into the shared template library and renamed deep-research-report.md; used by the orchestrator lifecycle's research phase. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-04T14:50+02:00: Created file-level onboarding for the new deep research report template companion file. Verification metadata is intentionally blank until closeout refreshes it to the first code commit containing the new source file.
