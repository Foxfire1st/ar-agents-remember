# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:43+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Worktree integration](../overview.md)

## Purpose

Owns the pure identity, canonical serialization, digest, and bounded-conflict vocabulary used by
the lifecycle enclosure publication state machine.

## Code Commentary

`EnclosureBindingIdentity` is the closed set of locator/manifest facts protected by the enclosure
binding digest. `enclosure_binding_payload` includes the predecessor terminal proof only when one
exists; `locator_binding` deliberately excludes mutable publication state and proof fields when
comparing immutable address bindings. The SHA-256 helpers and `model_text` define the deterministic
bytes used by both publication and readback verification. Conflict constructors report only bounded
model dumps or byte digests and sizes.

This module performs no reads, writes, locking, path confinement, or state transitions. Those remain
in `lifecycle_operation_location.py`, which supplies already-confined paths and calls these pure
functions while reserving, proving, validating, terminalizing, or resuming an enclosure.

## Invariants And Boundaries

- The binding payload has one canonical field set and deterministic JSON encoding.
- Mutable locator state and proof fields cannot change immutable binding identity.
- Byte conflicts disclose digest and size, not raw lifecycle contract contents.
- This module never becomes a fallback locator, journal reader, or write authority.
- `lifecycle_operation_location.py` remains the sole public locator-to-manifest state-machine owner.

## Docs References

No external Domain Documentation source is configured. The repository models and state-machine
tests govern this internal durability boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Binding identity and payload fields are closed and predecessor-aware. | `EnclosureBindingIdentity`; `enclosure_binding_payload` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py:24-115 |
| Canonical digests, serialization, and bounded conflicts are pure helpers. | `locator_id`; `sha256_payload`; `model_text`; `location_conflict`; `byte_conflict` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py:118-165 |
| Enclosure publication consumes the binding and digest API before any publication. | "def prepare_enclosure_publication("; "binding = enclosure_binding_payload("; "binding_fingerprint = sha256_payload(binding)" | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py:180-265 |
| Readback verification re-derives the same binding and request identity. | "def _validate_manifest("; "class EnclosureBindingIdentity:"; "def enclosure_binding_payload(" | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py:1031-1107; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py:25-25; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py:95-115 |

## Cross-Repo References

No cross-repository authority is owned here.

## Update History

- 2026-08-24T21:43+02:00 — Created for the hard-limit repair that separated pure enclosure binding
  and serialization from locator/manifest I/O without changing the publication contract.