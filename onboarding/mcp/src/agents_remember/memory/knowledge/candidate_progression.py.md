# candidate_progression.py

## Governing Overview

[overview.md](../overview.md)

## Purpose

Advance a draft candidate code-tree binding only from an explicitly observed predecessor while preserving its knowledge and all other admission scope.

## Code Commentary

### Logic

read_candidate_predecessor reads the exact receipt and logical dataset identity. plan_candidate_code runs the same binding checks without a lockfile or receipt write. progress_candidate_code takes the existing candidate exclusive lock, rechecks the predecessor receipt and dataset, validates the unchanged repository/lane/task/memory scope and code base, and runs the source-currentness check before the ordinary receipt writer publishes the successor.

### Conventions

Use existing capture, candidate locking, receipt and dataset identity owners. Refusals retain their explicit cause.

### Invariants And Boundaries

Normal candidate open remains strict. Only the code tree may progress; knowledge rows, allocation state and the original before half are not changed. A stale predecessor, moved dataset, foreign scope or moved source refuses without a replacement receipt.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No Domain Documentation source is configured. This account concerns the repository's own admission contract.

No configured domain source could be checked.

### Repo-Internal References

These constructs bind the code capture and candidate progression to the existing authority.

- `read_candidate_predecessor` implements the described admission boundary. [1]
- `plan_candidate_code` implements the described admission boundary. [2]
- `progress_candidate_code` implements the described admission boundary. [3]
- `_validate_progression` implements the described admission boundary. [4]
- `_same_scope` implements the described admission boundary. [5]

### Cross-Repo References

The leaf contract supplies code and memory roots; this module introduces no independent repository-selection authority.

No separate cross-repository authority is introduced.
