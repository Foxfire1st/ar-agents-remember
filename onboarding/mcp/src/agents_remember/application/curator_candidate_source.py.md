# curator_candidate_source.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Capture the exact pre-closeout code source used by leaf curation and recheck it before writes and publication.

## Code Commentary

### Logic

CuratorSourceTrees carries the exact code/memory tree IDs, admitted base and source provenance, plus the optional live capture whose currentness check it delegates. The value moved from the ingest module without changing persisted data.

capture_curator_code uses the shared future-code candidate owner on the real admitted leaf contract, checks its code base, and retains its exact identity. CuratorCodeCapture.currentness_refusal reloads the contract, rejects moved admission facts, and asks require_current_future_code_candidate to prove the same source is still current.

### Conventions

Use existing capture, candidate locking, receipt and dataset identity owners. Refusals retain their explicit cause.

### Invariants And Boundaries

Taskless bootstrap retains its own admission and never calls this leaf capture helper. Source movement is stale_precondition, not permission to use HEAD, another worktree or a new capture under the old claim.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No Domain Documentation source is configured. This account concerns the repository's own admission contract.

No configured domain source could be checked.

### Repo-Internal References

These constructs bind the code capture and candidate progression to the existing authority.

- `capture_curator_code` implements the described admission boundary. [1]
- `CuratorCodeCapture` implements the described admission boundary. [2]

### Cross-Repo References

The leaf contract supplies code and memory roots; this module introduces no independent repository-selection authority.

No separate cross-repository authority is introduced.
