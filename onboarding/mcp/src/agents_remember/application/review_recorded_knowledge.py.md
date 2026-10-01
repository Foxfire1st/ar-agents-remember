# review_recorded_knowledge.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Read a closed leaf knowledge state from its exact recorded memory commit endpoints when no frozen review generation exists.

## Code Commentary

### Logic

read_recorded_knowledge delegates endpoint selection to recorded_committed_range. read_memory_knowledge reads only the knowledge.sqlite Git blob at each endpoint, checks that it is a regular file, and asks the dataset identity owner to read it. Each side retains available, not-recorded, missing or corrupt state. Mismatched repository namespaces make the after side corrupt. The RecordedKnowledge instance holds temporary read files until the composed resolution is released, then its finalizer cleans them.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

No current worktree, branch tip or sibling generation supplies a missing operand. Temporary paths never enter comparison or cursor identity. The result is explicitly reconstructed history, not a new retained comparison generation or knowledge publication.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

No configured domain source could be checked.

### Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

- `RecordedKnowledge` owns the behavior described above. [1]
- `read_recorded_knowledge` owns the behavior described above. [2]
- `read_memory_knowledge` owns the behavior described above. [3]

### Cross-Repo References

No independent cross-repository interface is introduced by this source.

No additional cross-repository evidence is required.
