# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_records.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Read one immutable curator generation with typed integrity checks, independently of live readiness.

## Code Commentary

### Logic

An exact SHA-256 names the content-addressed record and projection. The reader validates record bytes, typed leaf/contract identity, deterministic projection and declared durable attestation copy. Attestation dependencies are checked against the record's own code/memory identities.

Judgment evidence is read through its retained custody owner, and assessment evidence through the publisher-recorded destinations. The returned generation result includes the verified evidence facts. Missing, corrupt, foreign or mismatched content refuses; old source/memory evidence with no custody cannot be replaced by current bytes.

### Conventions

Use the existing typed owners and exact recorded identities. Keep operation evidence and candidate provenance in task notes.

### Invariants And Boundaries

The reader proves retained integrity, not current live quality or acceptance. Strict currentness remains in require_current_curator_coherence, and no reclaimed live quality report is recreated or searched for.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured. The repository declarations below support this contract.

No configured domain source could be checked.

### Repo-Internal References

The cited owners carry the behavior and failure boundaries described above.

- One content-addressed generation is validated through its own retained inputs. [1]
- The exact durable attestation copy and recorded dependency binding are required. [2]

### Cross-Repo References

No separate repository supplies this contract.

No cross-repository reference is required.
