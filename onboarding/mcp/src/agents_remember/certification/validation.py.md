# mcp/src/agents_remember/certification/validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:11+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Performs bounded, exhaustive semantic validation of the canonical rail registry across profiles,
gate classification, ownership, dependencies, applicability, artifacts, and cycles.

## Code Commentary

### Logic

`validate_registry` first checks the measured work census. Within budget it indexes every retained
profile and rail variant and accumulates all independent findings rather than stopping at the first
defect. Profile checks enforce gate populations; rail checks enforce fixed gate/class/authority
meaning, runtime and uniqueness contracts, dependency direction/applicability, artifact producer
and consumer rules, and cycle freedom.

### Conventions

Findings have stable code, path, and detail fields. Conflicting declaration variants remain
individually addressable so one conflict cannot hide inner semantic defects.

### Invariants And Boundaries

- Validation is exhaustive only within the one proven budget; over-budget registries fail before
  reachability allocation.
- Gate 3 rails consume declared Gate 2 suite artifacts; later-gate dependencies or artifacts cannot
  flow backwards.
- Certifying profiles populate all five gates with the closed rail classifications and authorities.
- Profile-inapplicable prerequisites cannot authorize an applicable dependant.
- Missing, ambiguous, self, cyclic, or wrong-gate artifact/dependency relations are explicit
  findings, never guessed or repaired.
- No repository-specific rail name, owner, test command, or fallback is accepted here.

### Todos

None within registry semantic validation.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Validation checks the work census before building indexes and returns all bounded findings. | `validate_registry` | mcp/src/agents_remember/certification/validation.py:58-101 |
| Profile validation enforces declared gate order and population. | `_validate_profiles`; `_validate_profile_gates`; `_validate_profile_population` | mcp/src/agents_remember/certification/validation.py:145-220 |
| Each rail is checked against gate classification, authority, runtime, uniqueness, applicability, dependencies, and artifacts. | `_validate_rail` | mcp/src/agents_remember/certification/validation.py:231-286 |
| Dependency checks reject missing, backward, cross-gate, and profile-inapplicable prerequisites. | `_validate_dependencies`; `_validate_dependency_applicability` | mcp/src/agents_remember/certification/validation.py:342-429 |
| Artifact validation binds consumers to exact legal producers and gate direction. | `_validate_artifacts`; `_validate_rail_artifacts` | mcp/src/agents_remember/certification/validation.py:415-537 |
| Dependency cycles are reported without unbounded traversal. | `_validate_cycles`; `_resolve_acyclic_nodes` | mcp/src/agents_remember/certification/validation.py:539-585 |

## Cross-Repo References

Repository portability is achieved through contributed generic profiles and rails.

| Finding | Anchor | Source |
| --- | --- | --- |
| The validator receives only a canonical registry contract. | `validate_registry` | mcp/src/agents_remember/certification/validation.py:58-64 |

## Update History

- 2026-09-01T03:11+02:00 — Created for bounded exhaustive certification-registry validation.
  Verification remains closeout-owned until the source candidate is committed.
