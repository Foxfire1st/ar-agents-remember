# mcp/src/agents_remember/certification/repository_profiles/selection_results.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/selection_results.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

The canonical repository-neutral result contract for one test-selection provider (CCR-R19@v2). It
defines the content-addressed `repository-selector-result/v2` shape — an exact candidate-bound
population with dependency reasons, global invalidators, and typed unresolved inputs — so any
repository selector emits one verifiable contract and no selector may silently broaden its own
scope.

## Code Commentary

### Logic

`RepositorySelectionDraft` is the typed provider input; `build_repository_selection_result`
normalizes it into an immutable `RepositorySelectionResult`. Population is exactly
`empty`/`targeted`/`full`; a declared full result must publish full, and a targeted result can
never broaden itself to full. `complete:false` carries the sole failure code
`test-selection-ownership-incomplete` together with every `unresolvedInputs` reason; no
incomplete result is admissible as green.

`RepositorySelectionReason` pairs each input decision with a typed `effect`
(`select`/`global-invalidate`/`irrelevant`/`unresolved`); select reasons must name their
exact output artifact and value, and non-selection reasons must not. Every output value must have an
exact dependency reason. `repository_selection_result_digest` content-addresses the canonical
JSON (excluding only the declared `selectionDigest`), and the model re-verifies that digest at
validation; collections are unique and canonically ordered.

### Conventions

- Wire values are stable kebab-case literals.
- The result is normalized and digest-bound at construction; consumers never patch values.
- Language-specific selector logic lives in profiles; this module is repository-neutral.

### Invariants And Boundaries

- Empty, targeted, and full are explicit modes; full requires a declared profile mode and is never
  inferred from uncertainty.
- Incomplete ownership is a typed defect with every path/reason; it never triggers safe-full or
  language-specific fallback.
- Retry/cache consumers accept only the exact immutable selection identity (digest).
- The contract is repository/language agnostic; Python/Pyright/pytest is one R22 profile instance.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; CCR-R19@v2 is the governing packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R19 packet requires a complete, versioned, repository-owned selection authority, exact population modes, and typed ownership failure with no safe-full fallback. | "Normative Requirement"; "Required Behavior"; "Failure And Recovery" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R19-v2-exact-test-selection-ownership.md:11-49 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical result and its digest-verified contract. | `RepositorySelectionResult`; `repository_selection_result_digest` | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:89-130; mcp/src/agents_remember/certification/repository_profiles/selection_results.py:189-200 |
| Provider inputs are normalized into the immutable result at construction. | `RepositorySelectionDraft`; `build_repository_selection_result` | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:25-40; mcp/src/agents_remember/certification/repository_profiles/selection_results.py:203-241 |
| Population/completion/output-reason invariants are enforced at validation. | `_verify_population`; `_verify_completion`; `_verify_output_reasons` | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:133-137; mcp/src/agents_remember/certification/repository_profiles/selection_results.py:140-150; mcp/src/agents_remember/certification/repository_profiles/selection_results.py:175-186 |

## Cross-Repo References

None; this is the generic selector-result contract inside agents-remember.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card for the newly added
  `repository-selector-result/v2` contract and its build/digest/invalidation semantics.
  Verification is pinned to the owning commit.
