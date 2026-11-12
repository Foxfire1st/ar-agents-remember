# mcp/src/agents_remember/worktrees/integration/closeout/door.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Journal publication owner for closeout-door generations. The door is declared, claimed and proven in
the journal alone; the worktree contract no longer stores one.

## Code Commentary

### Logic

Door successors bind the accepted code and memory candidate trees, task intent, topology, and review/memory/admission/scheduling provenance. Their identity and immutable transition checks contain no ledger row, cache digest, or ledger-commit cell, so rebuilding the downstream cache cannot invalidate a claimed door.

The public surface is `DoorContractReadFailure`, `DoorPublicationClassification`, `DoorPublicationError`, `door_generation_for_operation`, `successor_waiting_door`, `prepare_door_publication`, plus the journal storage accessors `door_journal_path`, `read_published_door`, `write_published_door` and the single live reader `live_closeout_door`. The journal owns a write-once closeout-door generation. Publication intent and the journal's own state transition decide recovery; the queue may consume the published door but cannot synthesize, repair, or retain lifecycle evidence.

**Door storage moved out of the contract (closeout-door cut, commit `fad9808e`).**
`door_journal_path(contract)` resolves `<worktree_group>/reports/closeout-door.json`;
`read_published_door` returns the declared generation or `None`; `write_published_door` publishes one
generation atomically; `publish_door_intent` is the write path. `live_closeout_door(contract,
record=None)` replaced every `contract.closeout_door` read in the tree. It resolves in order: the
operation record's own `doorPublication.generation` when a record is supplied, otherwise the
contract's declared-door journal, falling back to the located lifecycle operation store's retained
publication. A contract with none of these has no live door — that is an absence, not a conflict, and
a contract outside the journal is never an error. `WorktreeContract` no longer has a `closeout_door`
field: a contract that still carries a `closeout_door:` block parses, the key is never read, and the
next rewrite drops it. The redundant "contract copy equals journal copy" comparisons and the
contract-byte before/after SHA proof were deleted as requirements rather than satisfied —
`DoorPublicationEvidence` is now `{state, generation}` and no longer carries
`expectedBeforeContractSha256` / `expectedPublishedContractSha256` /
`observedPublishedContractSha256`.

Under CCR-R03@v1 claiming re-requires the waiting generation's declared dependencies
(`require_closeout_door_dependencies`), and a waiting successor computes its own `closeout-door/v1`
declaration from the claimed predecessor's candidate trees, topology, intent, and provenance
records before hashing the successor identity — so the successor is a declared content-addressed
consumer of exactly the prior generation it reads
cit:([`door_generation_for_operation`, `successor_waiting_door`], mcp/src/agents_remember/worktrees/integration/closeout/door.py:79-114; mcp/src/agents_remember/worktrees/integration/closeout/door.py:117-172).

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity. Door dependency declarations are rebuilt from the exact provenance records, never from queue rows or task prose.

#### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.
- A claimed or successor generation must carry a dependency declaration equal to its canonical
  inputs; a stale or missing declaration refuses publication state.
- **The contract is not a door store.** Door state lives in the journal and in the operation record's
  own publication; no reader may reintroduce a contract-owned copy, and no comparison may be
  re-derived against contract bytes. An absent door is an absence, not a conflict.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `successor_waiting_door` binds successor identity to code/memory and task provenance without a ledger dependency. [1]
- `_require_door_transition` preserves the exact door identity and legal publication transitions. [2]

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `DoorContractReadFailure`; `DoorPublicationClassification`; `DoorPublicationError` as its public seam. [3]
- The door journal is written and read here, and `live_closeout_door` is the single live reader every former `contract.closeout_door` call site now uses. [4]
- Claim and successor seams re-require or rebuild the door dependency declaration. (`door_generation_for_operation`; `successor_waiting_door`) [5]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

No additional cross-repository evidence applies.

## 260821-CLIVE Sole Door Publication Authority

This module is the sole journal publication/CAS owner for door generations. Only an exact already
published waiting generation may become claimed, and the claimed operation identity is immutable.
A waiting successor hashes its predecessor edge plus the complete task, repository, and provenance
evidence. Legal door dispositions remain waiting/deferred/withdrawn/claimed; journal outcomes such
as cancel, retire, and supersede never masquerade as door states. "Contract publication" here meant
the contract-byte proof that was deleted with the contract field; the sole-authority claim now covers
the door journal only.

## 260831-CCR-R03 Dependency-Bound Door Steps

The claim and successor steps now participate in the door dependency contract: currentness is
reproven at claim, and the successor declares the exact predecessor generation as an input
(worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).
