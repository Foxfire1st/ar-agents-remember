# mcp/src/agents_remember/testing/eligibility.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/eligibility.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns the one total admission decision for an explicit bounded request against the reviewed
content-sealed cohort.

## Code Commentary

### Logic

`classify_direct_selection` validates one-to-eight unique exact selectors, loads the strict v2
manifest, resolves complete cohort membership, and verifies every audited file/configuration hash,
declared symbol, local import, effect, node, fixture/autouse member, and reachability fact. It
returns a typed eligible/refused decision with a binding over the exact request and verified
closure. `direct_selection_is_current` repeats the verification before a result is retained.

### Conventions

The manifest carries reviewed dependency/effect knowledge. This module performs narrow AST
verification; it does not attempt to infer safety for non-members or analyze the whole repository.

### Invariants And Boundaries

- A non-member is not analyzed into eligibility; it refuses as `not-in-cohort`.
- One refused member makes a mixed request refuse atomically.
- Unknown effects, missing imports/symbols/fixtures, hash drift, unreachable audit files, or
  changed configuration refuse before pytest.
- There is no auto-refresh, caller purity assertion, or fallback route.

### Todos

None. Expansion requires a separate decision.

## Docs References

No external domain documentation governs this repository admission policy.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public total decision and currency check are small entrypoints. | `classify_direct_selection` | mcp/src/agents_remember/testing/eligibility.py:50-83 |
| Cohort, hashes, AST symbols, nodes, fixtures, and binding are verified fail-closed. | `_verify_cohort` | mcp/src/agents_remember/testing/eligibility.py:137-327 |
| The manifest parser separately owns schema/population validation. | `load_direct_cohort_manifest` | mcp/src/agents_remember/testing/cohort_manifest.py:89-248 |

## Cross-Repo References

No cross-repository authority participates in admission.

## Update History

- 2026-08-25T01:56+02:00 — Superseded the generic transitive analyzer design with one explicit
  v2 sealed-cohort verifier.
- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
