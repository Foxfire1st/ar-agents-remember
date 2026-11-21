# mcp/tests/test_quality_gate_public_contract.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks lossless public closeout readiness and immutable quality evidence. The retained cases preserve finalization authority through projection, keep a diagnostic with matching rails under its distinct plan digest while the separately certified readiness stays green, project stale certificates and an invalid profile as non-green, and refuse changed decoder bytes under the same identifier.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

The current source assertions concern readiness and decoder identity. The repository test-evidence policy treats coverage and CRAP as reporting signals. A production CRAP score of 20 prompts review.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Closeout readiness is lossless on every surface [1]
- A diagnostic observation has rails equal to the certified gate’s rails and a distinct plan digest. The complete input’s certified readiness remains true. [2]
- Stale certificates and invalid profile remain non green [3]

- The same-ID decoder case changes the accepted decoder bytes, keeps the publication generation, and requires rendering to raise a dependency mismatch. [4]


- The repository test-evidence policy reports coverage and CRAP outside its enforcing rails. Its production-function review threshold is 20. [5]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
