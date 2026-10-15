# skills/c-03-repo-bootstrap/templates/route-local-overview-card-template.md

## Governing Overview

[Repository onboarding overview](../../../overview.md)

## Purpose

This template defines the overview card used as a scoped work order before a route-local overview worker writes durable memory.

## Code Commentary

### Logic

The overview card records repository and route metadata, the target and parent overviews, generation-time, priority and confidence fields, why the overview exists, governed paths and coverage status, required explanation topics, inputs, backlinks, downlinks, and open questions.

Its explanation checklist covers the subtree's purpose, structures, inclusions and exclusions, nearby-code connections, load-bearing files, workflows, documentation and cross-repo behavior, and future file-level onboarding. Required inputs are the root overview, area report and area brief; interface and concerns reports are conditional on relevance, while documentation and boundary packs are conditional on availability.

### Conventions

Phase 4C of the bootstrap skill writes an overview card for each selected governing route before Phase 4D overview waves. Cards identify the parent overview, child overview candidates, and governed files so workers do not repeat broad repository discovery. The required links include a parent backlink plus downlinks to child candidates and planned or existing file onboarding.

Route, target, timestamp, priority, confidence, coverage-status and question placeholders describe the work-order format. They do not assert that an overview or file card exists, that coverage is complete, or that work has been authorized.

### Invariants And Boundaries

An overview card is a promotion artifact, not durable source onboarding. The durable output is the mirrored route-local `overview.md` produced from it. The card supplies bounded construction context without replacing the route-local overview or the file-specific onboarding that follows.

### Todos

The earlier card's instruction to fill verification metadata after a source commit is historical, not a current instruction to add commit stamps. The template's `generated` field describes the work order's format; it is not a verified-commit field. Phase 4D describes route-local overview verification through reference anchors rather than recorded commits.

### Docs References

The checked template and relevant repository-local bootstrap-skill sections define this format without requiring external documentation. No relevant external documentation was found in those inputs.

## Evidence

### Repo-Internal References

- The overview card records route metadata, governed paths, explanation topics, inputs, links and questions. [1]
- Phase 4C creates cards for selected governing routes and bounds discovery with parent, child and governed-file context. [2]
- Overview waves use cards to construct mirrored durable route-local overviews, with reference-anchor verification rather than recorded commits. [3]
- The promotion pipeline distinguishes overview cards from the durable route-local overview output. [4]

### Cross-Repo References

No sibling repository was consulted for this template. No meaningful cross-repo reference was found in the checked template or relevant bootstrap-skill sections; a work order's boundary-pack field is not itself evidence of a live external boundary.
