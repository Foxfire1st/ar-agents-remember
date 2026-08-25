# mcp/src/agents_remember/testing/selection_contract.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/selection_contract.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns the closed typed vocabulary between explicit cohort verification, diagnostic bootstrap, and
the direct runner.

## Code Commentary

### Logic

`UnsafeEffectFamily` and `DirectRefusalCode` enumerate all policy outcomes.
`ResolvedDependencyClosure` records the audited paths and observations supplied by the manifest
verifier. An `EligibleDirectSelection` carries exact nodes, candidate root, closure, and binding;
`RefusedDirectSelection` carries the whole request, one stable reason, and optional source-backed
observation.

### Conventions

Decisions are values rather than exceptions at the public classifier boundary. Exceptions remain
private parsing/verification mechanics translated by the classifier.

### Invariants And Boundaries

- A decision is eligible or refused; there is no unknown or fallback decision.
- Closed enums make new effects/refusals explicit policy changes.
- Closure observations record reviewed facts; they are not claims from a generic analyzer.

### Todos

None.

## Docs References

No external documentation owns these internal types.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Unsafe families and refusal codes are closed. | `UnsafeEffectFamily` | mcp/src/agents_remember/testing/selection_contract.py:13-47 |
| Atomic eligible/refused decisions carry exact closure and binding. | `EligibleDirectSelection` | mcp/src/agents_remember/testing/selection_contract.py:49-86 |

## Cross-Repo References

No cross-repository boundary is owned here.

## Update History

- 2026-08-25T01:56+02:00 — Clarified that closure observations are sealed audit facts after the
  generic analyzer was removed.
- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
