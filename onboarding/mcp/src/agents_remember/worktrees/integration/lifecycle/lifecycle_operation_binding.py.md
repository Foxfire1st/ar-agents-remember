# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py

## Governing Overview

[Worktree integration](../overview.md)

## Purpose

Owns the pure identity, canonical serialization, digest, and bounded-conflict vocabulary used by
the lifecycle enclosure publication state machine.

## Code Commentary

`EnclosureBindingIdentity` is the closed set of locator/manifest facts protected by the enclosure
binding digest. `enclosure_binding_payload` includes the predecessor terminal proof only when one
exists; `locator_binding` deliberately excludes mutable publication state and proof fields when
comparing immutable address bindings. The SHA-256 helpers and `model_text` define the deterministic bytes used by both publication and readback verification, and `model_text` omits each of `predecessorTerminal` and `outsideScratch` that is null, so a manifest published before the root record existed keeps its exact bytes. Conflict constructors report only bounded
model dumps or byte digests and sizes.

This module performs no reads, writes, locking, path confinement, or state transitions. Those remain
in `lifecycle_operation_location.py`, which supplies already-confined paths and calls these pure
functions while reserving, proving, validating, terminalizing, or resuming an enclosure.

## Invariants And Boundaries

- The binding payload has one canonical field set and deterministic JSON encoding, and that set is address identity plus the predecessor terminal proof: the outside scratch root is recorded in the manifest and covered by the manifest digest, not by the binding fingerprint.
- Mutable locator state and proof fields cannot change immutable binding identity.
- Byte conflicts disclose digest and size, not raw lifecycle contract contents.
- This module never becomes a fallback locator, journal reader, or write authority.
- `lifecycle_operation_location.py` remains the sole public locator-to-manifest state-machine owner.

## Evidence

### Docs References

No external Domain Documentation source is configured. The repository models and state-machine
tests govern this internal durability boundary.

### Repo-Internal References

- Binding identity and payload fields are closed and predecessor-aware. [1]
> Retained earlier citation wording: - Canonical digests, serialization, and bounded conflicts are pure helpers. [2]
> Retained earlier citation wording: - Enclosure publication consumes the binding and digest API before any publication. [3]

> Retained earlier citation wording: - Readback verification re-derives the same binding and request identity. [4]


### Cross-Repo References

No cross-repository authority is owned here.

## 260928-MIK-L198 — Exact bytes leave a null root out, the binding does not carry it

`model_text` now omits each of `predecessorTerminal` and `outsideScratch` that is null, and passes `exclude=None` when neither is null, so a manifest published before the root record existed re-serialises to the same bytes. That is what keeps `expectedManifestSha256`, the terminal archive's manifest entry and every readback proof stable across the change. The binding payload is untouched: `enclosure_binding_payload` still holds the nine address fields plus the `predecessorTerminal` proof, and it names nothing about the root. The root is covered by the manifest digest and not by the binding fingerprint, so recording it does not change a published enclosure's binding identity. `EnclosureBindingIdentity` gains no field either, and `locator_binding` still excludes mutable state and proof fields.

- Canonical digests, serialization, and bounded conflicts are pure helpers.  Anchor: `locator_id` [2]


- Enclosure publication consumes the binding and digest API before any publication.  Anchor: "def prepare_enclosure_publication("; "binding = enclosure_binding_payload("; "binding_fingerprint = sha256_payload(binding)" [3]


- Readback verification re-derives the same binding and request identity. [4]
