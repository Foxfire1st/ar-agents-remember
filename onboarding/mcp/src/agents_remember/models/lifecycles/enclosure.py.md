# mcp/src/agents_remember/models/lifecycles/enclosure.py

## Governing Overview

[Lifecycle models overview](overview.md)

## Purpose

Defines immutable enclosure locator, manifest, terminal archive, receipt, and cleanup argument contracts.

## Code Commentary

### Logic

Strict models bind repository/task identity, generation, contract digest, predecessor, archive
entries, removed working-state identities (`TerminalEnclosureArchive.removedWorkingState`), and
cleanup request evidence; validators require exact manifest, path, and removed-working-state
uniqueness proofs.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- The locator-manifest-journal address chain is exact; terminal cleanup requires replayable archive proof; duplicate or mismatched paths/digests refuse.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- No external domain source is required to establish this repository-owned implementation. [1]

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- The module's concrete API, control flow, and validation boundary are implemented here. [2]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [3]
