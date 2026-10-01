# mcp/src/agents_remember/certification/validation.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

No configured domain documentation could be checked.

### Repo-Internal References

- Validation checks the work census before building indexes and returns all bounded findings. [1]
- Profile validation enforces declared gate order and population. [2]
- Each rail is checked against gate classification, authority, runtime, uniqueness, applicability, dependencies, and artifacts. [3]
- Dependency checks reject missing, backward, cross-gate, and profile-inapplicable prerequisites. [4]
- Artifact validation binds consumers to exact legal producers and gate direction. [5]
- Dependency cycles are reported without unbounded traversal. [6]

### Cross-Repo References

Repository portability is achieved through contributed generic profiles and rails.

- The validator receives only a canonical registry contract. [7]
