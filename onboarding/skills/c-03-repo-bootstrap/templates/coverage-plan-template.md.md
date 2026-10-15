# skills/c-03-repo-bootstrap/templates/coverage-plan-template.md

## Governing Overview

[Repository overview](../../../overview.md)

## Purpose

This template defines the coverage-planning artifact that turns scout and area research into prioritized route, file, evidence, and slice cleanup work.

This authored `skills/` template defines an artifact format; the packaged runtime source is a byte-identical distribution twin in this bounded inspection, not an independent contract owner. The document below describes placeholders and expected information, not the state of a bootstrap run.

## Code Commentary

### Logic

The coverage plan records strategy, area coverage goals, route classifications, file classifications, evidence pack needs, deferred routes/files, slice cleanup decisions, developer review questions, and decisions.

The metadata lists generated time, control mode, bootstrap mode and the `basedOn` inputs: scout report, area reports, area briefs, root overview, input ledger and developer notes. Strategy is free-text; area rows select priority, coverage goal, evidence needed and suggested first wave. Route classification offers core-logic / cross-repo-boundary / workflow / routine-support / deleted-route / moved-route / stale-onboarding-route with priority, reason and suggested treatment. File classification offers landmine / boundary / core-logic / routine-support. The evidence-pack queue asks independently for docs and boundary packs. Deferred paths have reasons and revisit triggers. Slice cleanup addresses moved or disappeared routes with affected overview, child onboarding or bootstrap artifacts, remove / move / retire / preserve disposition and review needed. Six developer questions challenge order, hidden risk, deprecation, classification, first wave and stale-memory treatment; the decision log retains date, decision and source.

### Conventions

Preserved workflow guidance, checked by the parent against the canonical bootstrap skill; it describes the procedure, not completed execution:

> Coverage planning happens before governing route maps and waves. It should classify work by risk and value, and in existing-memory slice maintenance it should decide whether stale route memory is refreshed, moved, removed, retired, or preserved.

### Invariants And Boundaries

Preserved advisory boundary from the incoming card:

> The plan is scheduling and prioritization input. It should not become durable file behavior documentation or promote low-confidence findings into fact.

The plan is a format for scheduling and prioritization, not documentation of file behavior or a completion record. Its suggested actions, example wave name, remove/move/retire/preserve options and review-needed vocabulary do not grant permission to delete memory or establish that any review, migration or cleanup occurred.

### Historical And Verification Limits

The incoming card carried this unfinished verification instruction:

> Fill verification metadata after the source file is committed.

It is retained as a historical Todo, not an assertion that verification metadata is missing now, an authority grant, or a request to hand-write mechanical sidecar fields. This comparison supplies no executed bootstrap, source approval, test result, completed wave, closeout, publication or acceptance.

### Docs References

The incoming card had no external-documentation assessment. This bounded proposal examined local artifact-format evidence only and makes no new claim that an external search found nothing.

### Cross-Repo References

The incoming card had no cross-repository reference section. Boundary-pack fields describe planning inputs; this proposal inspected no sibling repository and establishes no external boundary behavior.

## Evidence

### Repo-Internal References

The citation rows below preserve the incoming template-evidence meanings while retargeting them to the canonical authored source and narrowing ranges to the information described. They prove the shape of a template, not execution or acceptance of its values. Inherited cross-file skill claims remain qualified above.

- The coverage plan template captures strategy, area goals, route classification, file classification, and evidence pack queues. [1]
- The template records deferred routes/files, slice cleanup decisions, developer review questions, and decisions for later waves. [2]
- Existing-memory slice cleanup identifies affected memory, disposition and review needed for moved or disappeared routes. [3]
- Developer review challenges ordering, risk, deprecation, classification, first wave and historical preservation before recording decisions. [4]
- The skill places coverage planning before governing-route mapping and the later overview/file waves. [5]
