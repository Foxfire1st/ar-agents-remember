# mcp/src/agents_remember/models/lifecycles/enclosure.py

## Governing Overview

[Lifecycle models overview](overview.md)

## Purpose

Defines immutable enclosure locator, manifest, terminal archive, receipt, outside-scratch-root record, and cleanup argument contracts.

## Code Commentary

### Logic

Strict models bind repository/task identity, generation, contract digest, predecessor, the generation's outside scratch root (`OutsideScratchRootRecord`), archive entries, removed working-state identities (`TerminalEnclosureArchive.removedWorkingState`), and cleanup request evidence; validators require exact manifest, path, and removed-working-state uniqueness proofs.

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

## 260928-MIK-L198 — The manifest carries the outside scratch root record

`OutsideScratchRootRecord` is a frozen strict model that forbids extra fields and holds `path`, `generation` and `markerSha256`, the identity a root is proved by. `LifecycleEnclosureManifest` carries it as the optional `outsideScratch` field, defaulting to `None`. `_expected_manifest_text` excludes `outsideScratch` from the serialised text exactly when it is `None`, the same rule the file already applies to `predecessorTerminal`, so a manifest published before this change keeps its exact bytes. A generation that records a root carries the three cells in that key, and the existing successor/predecessor validator is unchanged.
