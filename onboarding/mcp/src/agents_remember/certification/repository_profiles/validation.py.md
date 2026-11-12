# mcp/src/agents_remember/certification/repository_profiles/validation.py

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Aggregate fail-closed validation for one repository-owned Gate 1-4 profile. It returns every
independent schema/graph/config finding before any command starts, so profile errors surface as a
typed report rather than a partial execution.

## Code Commentary

### Logic

`validate_repository_profile` builds unique catalogs for rails, selections, selectors, executors,
and decoders, then runs the publication, executor, decoder, selector, selection-authority,
selection, rail, semantic-input, coverage, selection-dependency, and cycle validators, returning a
sorted `RepositoryProfileValidationReport`.

L19 tightened selector validation: `_validate_selector` now rejects duplicate entries across
`inputUniverse`, `externalInputs`, and `outputArtifacts` (`duplicate-selector-field`),
and `_validate_selector_command` requires the selector command to consume its exact sandbox
result path plus the identity placeholders `{candidate-kind}`, `{candidate-value}`,
`{selector-configuration-digest}`, `{selector-id}`, and `{selector-version}`
(`selector-identity-input-unused`). Command placeholders are validated for complete bounded
names, declared membership, and list-placeholder token atomicity.

### Invariants And Boundaries

- Validation is exhaustive over a bounded catalog; there is no truncation or partial admission.
- Each required purpose/mode selection pair must be declared once (local-precommit targeted,
  closeout targeted, closeout full).
- Gate-2 rails require an exact scope provider and input selectors; Gate-3 rails must consume a
  declared Gate-2 artifact; Gate-4 rails require clean-room execution and always teardown.
- Selector commands must bind their exact result and selector identity inputs (L19).
- A rail's skipped exit codes must be a subset of its success exit codes.

### Todos

None recorded.

### Current source-selection contract

Profile validation rejects duplicate generated-input identities and requires each generated input checkRail to identify a declared Gate-1 rail. It delegates environment reconstruction and source applicability to their canonical validators. Executor argument uniqueness includes retainedReportsArgument when declared, with no diff-base argument. Rail command validation permits only the source placeholders admitted for that rail’s exact applicability; the extracted validation_primitives owner supplies shared gate-set, duplicate and finding helpers.

- `validate_repository_profile` carries the current contract described above. [1]
- `_validate_executor` carries the current contract described above. [2]
- `_validate_rail_runtime` carries the current contract described above. [3]

## Evidence

### Docs References

No configured Domain Documentation source applies; validation is repository-neutral R22 behavior.

### Repo-Internal References

- The aggregate validator returns every independent finding. [4]
- Selector duplicates and identity placeholders refuse before execution. [5]
- Command placeholders must be complete, declared, and list-atomic. [6]
- Rail validation checks the declared rail contract and ownership constraints. [7]
- Artifact dependencies must name valid producing rails and artifacts. [8]
- Gate semantic validation checks the applicable gate contract. [9]

### Cross-Repo References

None; this is the repository-neutral validation authority.
