# skills/l-01-agent-lifecycles/templates/impact-analysis.md

## Governing Overview

[overview](../overview.md)

## Purpose

The canonical impact-analysis template is the report the Reviewer uses for planned-work conflicts and risks to landed work, including analyses delegated to its helpers; the Orchestrator and developer can inspect it for planning and review decisions. It makes both planned-versus-planned collisions and planned-versus-past regressions visible. The packaged runtime file is its distribution twin, not another report-contract authoring home.

## Code Commentary

### Logic

The report records recipient, analytical author label, subject and written time, followed by the surface swept, routes/areas, code anchors, both risk axes, evidence inventory and an actions section for the spawning agent's main loop. Planned-versus-planned includes present or future master/leaf collisions and suggested resolutions such as foundation extraction, leaf movement or sequencing. Planned-versus-past names already-landed work at risk and its evidence limits.

Evidence-first findings cite route indexes and the files opened from `read_ar_files` results. The inventory records the identifiers and card paths returned by `read_ar_files` and the files opened with native file tools. Naming locates the material to inspect; it is not source/onboarding text or independent proof of a collision or regression. Each finding states what its evidence does not prove.

### Conventions

The author field is an analysis role or a helper label identifying the assigned routes, not a field specified for a runtime occupant ID. Keep analytical responsibility distinct from transport identity. Maintain the canonical template as the contract; keep the packaged copy in sync without treating source byte equality as proof that synchronization or installation ran.

### Invariants And Boundaries

This is a report, not a decision. Its actions section feeds the Orchestrator's spirit test and proposals to reshape the plan (`roles/orchestrator.md#changes-to-the-plan`) or the Reviewer's verdict; the template says it never decides and performs no mutation. A helper author does not obtain an AR seat or boundary authority by writing the report. The current router keeps task boundary acts with the owning seat, and the current Orchestrator distinguishes delivery reports, findings, review, curation and Git publication rather than inferring acceptance from host status.

### Documentation Scope

The template holds no TODO and needs no sibling-repository evidence for this report contract.

## Evidence

- The Reviewer uses the template for planned-work conflicts and risks to landed work and owns its helper's contribution; the spawning agent alone changes AR state. [1]

- Both collision and regression axes need evidence and per-finding limits; the report never decides. [2]

- Recipient, author, subject and timestamp are report fields, with analytical rather than occupant authorship. [3]

- Scope, current/future collisions, resolution suggestions and landed regression risks are retained. [4]

- The evidence inventory records `read_ar_files` identifiers and card paths and the natively opened files, and the actions section performs no mutation. [5]

- Harness helpers hold no AR seat; boundary acts and one Curator writer remain with the seat. [6]

- Orchestrator verifies Manager delivery while leaving the Manager's leaf diff, repair and evidence loop intact, and keeps reports, findings, review, curation and Git publication separately addressed. [7]
