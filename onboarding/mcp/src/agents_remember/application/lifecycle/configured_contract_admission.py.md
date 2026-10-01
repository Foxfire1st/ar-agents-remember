# mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Closed admission for every public current-contract mutation route.

## Code Commentary

### Logic

The public surface is `ConfiguredContractAccepted`, `ConfiguredContractRefused`, `admit_configured_contract`, `configured_authority_refusal`, `configured_contract_reread_refusal`, `execute_configured_contract_operation`. This application boundary exposes a closed public result and delegates durable mutation to its owning domain seam. Expected configured-contract, location, or legacy failures are translated through typed decisions; callers do not enumerate lower-level exception families or invent alternate authority. Admission is strict by default, including current candidate-worktree identity. An exact-pair consumer may explicitly set `require_candidate_identity=False` only because the shared code-memory pair validator owns that same live-candidate check; configured repository roots, separation, task identity, and enclosure confinement remain admitted here.

### Conventions

The file exposes typed values or one narrow operation boundary. Callers consume those values directly rather than reconstructing lower-level state from strings, mutable task documents, or queue projection.

### Invariants And Boundaries

- Preserve the module's single ownership seam; do not add a fallback reader or duplicate authority.
- Disabling the admission layer's candidate-identity check is valid only for an exact-pair consumer
  that immediately delegates the same obligation to the canonical pair validator.
- Expected refusal states remain typed and bounded, while unexpected programming faults remain loud.
- Durable lifecycle facts live in the canonical root journal; scheduling projections may only consume them.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

- The module defines `ConfiguredContractAccepted`; `ConfiguredContractRefused`; `admit_configured_contract` as its public seam. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Final Terminal Admission Route

`admit_configured_terminal_contract` keeps live mutation admission strict, but recognizes one
state-disjoint terminal route when the exact locator is `terminal-archived`. That route requires
readable surviving contract truth, the exact external archive and receipt, and configured
repository identity for the archived contract without requiring worktrees cleanup already removed.
Present-invalid archive or authority evidence becomes a bounded refusal. Terminal admission is
only for status and exact cleanup retry; it is never a generic fallback for live mutations.
