# mcp/src/agents_remember/certification/repository_profiles/selection_results.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/selection_results.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff`|
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
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
| Repository selection produces one immutable result and validates the declared population and completion state before publication. | "class RepositorySelectionResult("; "def _verify_population("; "def _verify_completion(" | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:85-126; mcp/src/agents_remember/certification/repository_profiles/selection_results.py:129-146 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical result and its digest-verified contract. | `RepositorySelectionResult`; `repository_selection_result_digest` | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:85-126; mcp/src/agents_remember/certification/repository_profiles/selection_results.py:185-196 |
| Typed provider inputs normalized into one immutable selector result. | "class RepositorySelectionDraft" | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:22-36 |
| Normalize and content-address one provider result. | "def build_repository_selection_result" | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:199-237 |
| Selector population validation checks the declared universe against its selected and excluded members. | "def _verify_population" | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:129-133 |
| Selector completion validation enforces the declared completion state. | "def _verify_completion" | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:136-146 |
| Selector output validation requires consistent output reasons. | "def _verify_output_reasons" | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:171-182 |

## Cross-Repo References

None; this is the generic selector-result contract inside agents-remember.

## Update History

- 2026-09-09T02:49:53+02:00 — CCR-L38 bounded inherited claim reconciliation: replaced the unsupported task-packet citation with exact result, population, and completion validation anchors. Source hashes: mcp/src/agents_remember/certification/repository_profiles/selection_results.py=9d1a5180e610830636b4e96e2ac794fd8013dd51c65d08893dadc0c44b3ccd20; verification metadata remains unchanged.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card claims against the frozen candidate source and repaired exact citation coordinates (RepositorySelectionResult→85-126; repository_selection_result_digest→185-196). Preserved claim prose; source-sha256=9d1a5180e610830636b4e96e2ac794fd8013dd51c65d08893dadc0c44b3ccd20; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card for the newly added
  `repository-selector-result/v2` contract and its build/digest/invalidation semantics.
  Verification is pinned to the owning commit.
