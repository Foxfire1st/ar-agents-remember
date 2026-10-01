# mcp/src/agents_remember/models/structural/atomic_series_activation.py

## Governing Overview

[structural models overview](overview.md)

## Purpose

This file defines the closed durable vocabulary for selecting one live atomic master per canonical
series contract. It keeps contract identity, current selection, observation state, and malformed
snapshot archive evidence strict and separate from task documents, queue members, and operation
journals.

## Code Commentary

### Logic

`AtomicSeriesActivationRecord` is the one replace-in-place snapshot for a canonical series contract.
It is `schemaVersion "2.0"` and carries `contractFingerprint` (SHA-256 of the canonical resolved
contract path), `selectedMaster`, `contractPath`, one of `vacant|reconciling|active`, a monotonic
revision, and selection time. The former `AtomicSeriesSourceRef` / `AtomicSeriesSourcePair` models and
the `sourcePairFingerprint` field they fed are gone: two atomic masters commanded by one sprint derive
the *same* protected source pair, so the source pair could not be the key. The observed vocabulary
adds `unreadable` without making it a writable selection state. `AtomicSeriesActivationArchiveEvidence`
is also `"2.0"` and carries `contractFingerprint` beside an archive classification
(`raw-bytes|opaque-entry|absence`), optional snapshot path, digest, size, original activation
path/error, replacement master, and repair time. That vocabulary lets a repair prove whether it copied
malformed regular bytes, moved an opaque nonregular entry without following it, or observed absence.

### Conventions

Every model is frozen and rejects extra fields. Contract-path text is nonblank and bounded;
fingerprints use lowercase SHA-256. `TaskDocumentRef` is the master identity, while runtime ids and
queue positions never enter the record.

### Invariants And Boundaries

- One canonical series contract has at most one replace-in-place activation record; two atomic masters
  that share one protected source pair hold independent records, because the contract — not the source
  pair — is the key.
- A snapshot whose `contractFingerprint` or `contractPath` is not this exact contract is refused rather
  than adopted (`atomic-series-activation-contract-mismatch`); recovery requires an explicit selecting
  repair.
- `unreadable` is read evidence, never a state callers may publish.
- A durable vacant record retains the last selected master for audit and exact cancellation replay.
- These models contain no commit, claim, certification, integration, or lifecycle state.
- Opaque-entry evidence describes quarantine; it never claims the entry was read as trusted bytes.

### Todos

Exact model claims and citations are reconciled to the contract-scoped source. Verification metadata
remains intentionally empty while this source is uncommitted.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The activation store derives this contract's own fingerprint and refuses any record that is not this exact contract. [1]
- Focused tests prove that two contracts sharing one protected source pair hold independent selection, that vacant and active are never waiting states, that release addresses only the released contract, and that another contract's record can never be adopted. [2]

### Cross-Repo References

No cross-repository source is configured for this memory root.
