# mcp/src/agents_remember/certification/repository_profiles/selection_results.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies; CCR-R19@v2 is the governing packet.

- Repository selection produces one immutable result and validates the declared population and completion state before publication. [1]

### Repo-Internal References

- The canonical result and its digest-verified contract. [2]
- Typed provider inputs normalized into one immutable selector result. [3]
- Normalize and content-address one provider result. [4]
- Selector population validation checks the declared universe against its selected and excluded members. [5]
- Selector completion validation enforces the declared completion state. [6]
- Selector output validation requires consistent output reasons. [7]

### Cross-Repo References

None; this is the generic selector-result contract inside agents-remember.
