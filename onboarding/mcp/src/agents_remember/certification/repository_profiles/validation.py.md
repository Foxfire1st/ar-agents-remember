# mcp/src/agents_remember/certification/repository_profiles/validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No configured Domain Documentation source applies; validation is repository-neutral R22 behavior.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The aggregate validator returns every independent finding. | `validate_repository_profile` | mcp/src/agents_remember/certification/repository_profiles/validation.py:57-126 |
| Selector duplicates and identity placeholders refuse before execution. | `_validate_selector`; `_validate_selector_command` | mcp/src/agents_remember/certification/repository_profiles/validation.py:663-672; mcp/src/agents_remember/certification/repository_profiles/validation.py:675-706 |
| Command placeholders must be complete, declared, and list-atomic. | `_validate_command_placeholders` | mcp/src/agents_remember/certification/repository_profiles/validation.py:709-750 |
| Gate-lineage and dependency findings enforce exact rails, artifacts, and clean-room rules. | `_validate_rail`; `_validate_artifact_dependencies`; `_validate_gate_semantics` | mcp/src/agents_remember/certification/repository_profiles/validation.py:471-490; mcp/src/agents_remember/certification/repository_profiles/validation.py:598-639; mcp/src/agents_remember/certification/repository_profiles/validation.py:642-660 |

## Cross-Repo References

None; this is the repository-neutral validation authority.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 selector-validation changes — duplicate checks across input/external-input/output fields and
  the mandatory selector identity placeholder set. Verification is pinned to the owning commit.
