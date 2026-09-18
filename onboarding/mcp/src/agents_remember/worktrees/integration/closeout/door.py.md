# mcp/src/agents_remember/worktrees/integration/closeout/door.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/door.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `successor_waiting_door` binds successor identity to code/memory and task provenance without a ledger dependency. | `successor_waiting_door` | mcp/src/agents_remember/worktrees/integration/closeout/door.py:117-172 |
| `_require_door_transition` preserves the exact door identity and legal publication transitions. | `_require_door_transition` | mcp/src/agents_remember/worktrees/integration/closeout/door.py:302-360 |

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `DoorContractReadFailure`; `DoorPublicationClassification`; `DoorPublicationError` as its public seam. | `DoorContractReadFailure`; `DoorPublicationError` | mcp/src/agents_remember/worktrees/integration/closeout/door.py:32-36; mcp/src/agents_remember/worktrees/integration/closeout/door.py:61-76 |
| The door journal is written and read here, and `live_closeout_door` is the single live reader every former `contract.closeout_door` call site now uses. | `live_closeout_door` | mcp/src/agents_remember/worktrees/integration/closeout/door.py:203-232 |
| Claim and successor seams re-require or rebuild the door dependency declaration. (`door_generation_for_operation`; `successor_waiting_door`) | `door_generation_for_operation`; `successor_waiting_door` | mcp/src/agents_remember/worktrees/integration/closeout/door.py:79-85; mcp/src/agents_remember/worktrees/integration/closeout/door.py:117-172 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

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

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=8030607f94cfd3a9b1ab094b9f1caef465e24a0646cde170eae24c11aa25a781. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.

- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `door_generation_for_operation`, `successor_waiting_door` repointed to mcp/src/agents_remember/worktrees/integration/closeout/door.py:117-175, mcp/src/agents_remember/worktrees/integration/closeout/door.py:79-114. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: recorded that door storage moved out of the worktree contract into `<worktree_group>/reports/closeout-door.json`, named the journal accessors (`door_journal_path`, `read_published_door`, `write_published_door`) and the single live reader `live_closeout_door` that replaced every `contract.closeout_door` read, and recorded that `DoorPublicationEvidence` shed its three contract-SHA fields to `{state, generation}`. Replaced the contract-publication wording in Purpose, Logic and the sole-authority section, and added the no-contract-door-store invariant. Verification metadata remains pinned because only the cut-affected claims were reconciled; source documentation only, no acceptance claim.

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): widened the claim row and prose cit range to door.py:83-120 so the cited range holds the `door_generation_for_operation` declaration.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded dependency re-requirement at claim and successor dependency declaration; prior sole-authority and public-seam prose preserved.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded sole door publication, exact claim, and successor identity rules. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
