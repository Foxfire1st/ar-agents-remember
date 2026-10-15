# skills/c-03-repo-bootstrap/templates/file-card-template.md

## Governing Overview

[Repository onboarding overview](../../../overview.md)

## Purpose

This template defines the file-card work order that constrains a future file-level onboarding worker to one concrete source file.

## Code Commentary

### Logic

The file card records source and onboarding targets, classification, priority, role, risk, suggested action and wave, governing context, why the file matters, required explanations, worker inputs, bounded reads, reference expectations, known traps, questions and done criteria. Governing context identifies the nearest overview, ancestor overviews and local area; inputs include the source file, nearest overview, existing onboarding when present, area report and relevant documentation or boundary packs.

The required output is a converted card with a source-path title, relative `## Governing Overview` link, Purpose, Code Commentary, and temporary citation-table evidence in the `Finding`, `Anchor`, `Source` grammar. The fixer replaces those tables with numbered finding lines and writes the companion. Reference numbers and companion JSON must not be authored manually. The required-section list does not request metadata stamps or an Update History section; these are not additional file-card output requirements.

### Conventions

Phase 4G of the bootstrap skill creates file cards for priority source files before file-level onboarding is assigned, except for tiny repositories. Phase 4H gives each file worker one card and has it follow `c-05-create-or-update-onboarding-files`. The card keeps workers scoped and prevents broad rediscovery: permitted reads are listed, while unrelated areas, unlisted adjacent-repository files, broad directory scans and other areas' reports require escalation.

Source paths, targets, generation-time, classifications, suggested actions and waves, traps and questions are format placeholders, not evidence of an assignment, completion, authorization or current risk classification. The `Done When` checklist describes the expected output; it does not record a completed wave.

### Invariants And Boundaries

A file card does not replace `c-05-create-or-update-onboarding-files`; it prepares bounded instructions for that skill's file-level onboarding. Durable onboarding explains only its concrete source file, stays self-sufficient, and links to the nearest governing overview. References are evidence-backed. Task-local planning stays out of durable onboarding, and open questions belong in the wave review or `STATE.md`.

### Todos

No file-local follow-up is identified by the checked inputs; reference anchors carry currentness rather than metadata stamps. The template's completion checklist is a work-order constraint, not an assertion that onboarding was written or verified.

### Docs References

The checked template and relevant repository-local bootstrap-skill sections define this format without requiring external documentation. No relevant external documentation was found in those inputs.

## Evidence

### Repo-Internal References

- The file card records targets, classification, governing context, inputs, bounded reads, explanations, traps, questions and done criteria. [1]
- Required output uses a source-path title, relative governing-overview link, prose and temporary citation tables; the fixer owns numbering and sidecar generation. [2]
- Phase 4G writes file cards for priority files and requires them before assignment except for tiny repositories. [3]
- Phase 4H gives each file worker one card and delegates file-level onboarding to c-05 while preserving bounded reads, self-sufficiency and one-to-one mapping. [4]
- Done criteria require concrete-file onboarding, a governing backlink, evidence-backed references, no task-local planning and questions in review or state. [5]

### Cross-Repo References

No sibling repository was consulted for this template. No meaningful cross-repo reference was found in the checked template or relevant bootstrap-skill sections; a work order's boundary-pack field is not itself evidence of a live external boundary.
