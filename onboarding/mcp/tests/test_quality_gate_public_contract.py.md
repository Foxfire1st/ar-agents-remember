# mcp/tests/test_quality_gate_public_contract.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks lossless public closeout readiness and immutable quality evidence. The retained cases preserve finalization authority through projection, keep diagnostic results non-certifying even when their rails match, reject stale certificates and invalid profiles, and refuse changed decoder bytes under the same identifier.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

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
- Diagnostic readiness stays non certifying with matching rails [2]
- Stale certificates and invalid profile remain non green [3]
- Recovery refuses same id decoder byte drift [4]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
