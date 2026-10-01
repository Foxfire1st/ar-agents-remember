# mcp/src/agents_remember/worktrees/integration/lifecycle/certification_observation.py

## Governing Overview

[Governing integration overview](overview.md)

## Purpose

Takes the exact current lifecycle journal observation after immutable evidence readback, allowing only concurrent heartbeat fields to differ.

## Code Commentary

### Logic

`observe_certification_publication` reads the current record and compares it with the evidence-verified record after normalizing only `recordRevision`, `heartbeatAt` and `currentCommand` for comparison. A missing record or any other changed field raises a typed certification contract refusal with expected/observed operation key, generation and revision and zero declared gate starts. The actual current record, including its current revision, is returned for the caller’s strict CAS.

### Conventions

The caller verifies evidence first, invokes this read immediately before publication, and uses the returned complete record for one CAS. A lost CAS is a refusal, not an instruction to retry.

### Invariants And Boundaries

- Cancellation, selection, intent, generation and authority changes are not heartbeat differences.
- The helper performs no mutation and does not itself publish a certificate or acquire worker authority.
- Revision/heartbeat write legality remains the journal owner’s responsibility; this comparison does not infer semantic currentness from a revision number alone.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

No configured domain documentation applies.

### Repo-Internal References

- `observe_certification_publication` owns the described selection or observation boundary. [1]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

No cross-repository reference is required.
