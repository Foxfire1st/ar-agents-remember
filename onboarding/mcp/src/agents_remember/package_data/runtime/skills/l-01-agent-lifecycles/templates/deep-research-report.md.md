# l-01-agent-lifecycles/templates/deep-research-report.md

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

## Evidence

### Docs References

No external domain documentation applies to this repository-local lifecycle report template.

No relevant external documentation found.

### Repo-Internal References

The template is a companion to the lifecycle entry contract and the detailed spine.

- The entry contract lists this file in the `templates/…` companion-file line as one of the shapes spawning seats compile briefs from. [1]
- The entry contract lists this file in the `templates/…` companion-file line as one of the shapes spawning seats compile briefs from; the router shrank from 620 to 179 lines in 260915-CAPS-L1, so the anchor is rebased. [2]
- The template defines report rules, full and compact shapes, evidence kinds, and evidence-ledger guidance. [3]

As of cycle 4 the decision block asks for the suggested artifact shape (minimal w-02 task vs master + series) instead of the retired 'build mode' axis.

### Cross-Repo References

No sibling repository evidence is needed for this lifecycle report template.

No meaningful cross-repo references found.
