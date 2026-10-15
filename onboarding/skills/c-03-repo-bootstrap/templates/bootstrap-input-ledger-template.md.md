# skills/c-03-repo-bootstrap/templates/bootstrap-input-ledger-template.md

## Governing Overview

[Repository overview](../../../overview.md)

## Purpose

This template defines the source-intake ledger used before bootstrap agents ask for additional sources or proceed into research, including source deltas for existing-memory slice maintenance.

This authored `skills/` template defines an artifact format; the packaged runtime source is a byte-identical distribution twin in this bounded inspection, not an independent contract owner. The document below describes placeholders and expected information, not the state of a bootstrap run.

## Code Commentary

### Logic

The template captures target repo, control mode, bootstrap mode, memory root, onboarding root, topology, branch, source inventory gate status, presented source inventory, excluded sources, weak categories, user-added sources, corrections, source deltas, settings path-rule exclude review, cross-repo context, assumptions, hard stops, and operator decision.

The header distinguishes `sourceInventoryGate` (pending / accepted / corrected / blocked) from the per-source status (readable / unreadable / unavailable) and user decision (approved / excluded / corrected / pending). Source inventory delta has added / refreshed / moved / deleted treatments for existing-memory slice maintenance. Settings excludes are explicitly a review checklist against resolved `system/settings.json`, not a hidden replacement for `pathRules`; its literal entries include dependency/build/cache directories, `.env` and `.env.*`, generated paths and both Zone.Identifier patterns. Cross-repo rows distinguish expected from actual branch and record matched / mismatch / missing with read-only / ignored use. The hard-stop list covers unresolved roots, unreadable required sources, ambiguous meanings, required-boundary branch mismatch, LOW-confidence durable claims, unresolved docs/code conflict and updates outside the target repository. Operator decision records control mode, added-source presence and proceed yes/no.

### Conventions

Preserved workflow guidance, checked by the parent against the canonical bootstrap skill; it describes the procedure, not completed execution:

> The ledger is the durable record of what sources were presented and accepted or rejected. It should be written after the source inventory review, before scout and deeper bootstrap work or automated execution.

### Invariants And Boundaries

Preserved advisory boundary from the incoming card:

> The source inventory must be shown before asking for additions, and the ledger should not cite source registries as proof. It is an intake decision artifact, not evidence for durable behavior claims.

The presented choices and empty `<...>` fields describe an intake artifact format. They do not say that sources were accepted, an operator approved this candidate, a required boundary matched, or execution may proceed. The settings review and branch mismatch fields expose decisions; this template alone does not enforce those decisions.

The source header still literally offers `topology | external / mixed` at line 10. This is inherited template vocabulary, not evidence that mixed topology is currently supported; the governing overview states that only external topology is supported. The inherited choice is disclosed rather than silently rewritten.

### Historical And Verification Limits

The incoming card carried this unfinished verification instruction:

> Fill verification metadata after the source file is committed.

It is retained as a historical Todo, not an assertion that verification metadata is missing now, an authority grant, or a request to hand-write mechanical sidecar fields. This comparison supplies no executed bootstrap, source approval, test result, completed wave, closeout, publication or acceptance.

The old card also attributed a workflow requirement to the packaged `c-03-repo-bootstrap` skill: 

> `c-03-repo-bootstrap` skill requires source inventory review to be written to `bootstrap/input-ledger.md` using this template before automated execution starts.

The attribution is preserved and checked against the current canonical bootstrap skill. The separate skill citation below supports the procedural requirement; the template alone proves only its artifact format.

### Docs References

The incoming card recorded the following repository-local documentation assessment:

> No external documentation is needed for this repository-local template.

> No relevant external documentation found.

These are inherited assessments, not a fresh external documentation search. The present evidence is the inspected local template.

### Cross-Repo References

The incoming card recorded:

> No sibling repository evidence is needed for this template.

> No meaningful cross-repo references found.

These are preserved scope assessments, not a fresh sibling-repository inspection. Any cross-repo fields in the template describe recorded context, not permission to write another repository.

## Evidence

### Repo-Internal References

The citation rows below preserve the incoming template-evidence meanings while retargeting them to the canonical authored source and narrowing ranges to the information described. They prove the shape of a template, not execution or acceptance of its values. Inherited cross-file skill claims remain qualified above.

- The input ledger records run metadata, onboarding root, source inventory gate status, and the presented source inventory with status, planned use, and user decision. [1]
- The template captures excluded sources, weak source categories, additional user sources, corrections, source deltas, settings path-rule exclude review, cross-repo context, assumptions, hard stops, and proceed/no-proceed decision. [2]
- Settings excludes are a review checklist and not a hidden substitute for pathRules. [3]
- Expected/actual branch context, assumptions, hard stops and operator decision are explicit intake fields. [4]
- The bootstrap skill requires accepted or corrected source inventory to be recorded in bootstrap/input-ledger.md before automated execution. [5]
- The reviewed source inventory is written to the input ledger using this template. [6]
