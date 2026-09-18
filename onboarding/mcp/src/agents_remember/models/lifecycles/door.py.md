# mcp/src/agents_remember/models/lifecycles/door.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/door.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Journal-owned closeout-door generation and publication evidence. The door moved out of the
worktree contract, so this vocabulary carries no contract-byte pair to hash, compare, or re-read;
the intent names the generation and proving it is the journal's own state transition.

## Code Commentary

### Logic

Door generations retain code/memory candidates and bases, task identity, review/coherence,
admission, and scheduling evidence. They contain no `ledgerMemoryCommit` or `ledgerProvenance`,
and dependency construction has no ledger edge. Refreshing or deleting the cache cannot stale a
generation through a cache-provenance fingerprint.

The public surface is `CloseoutDoorGeneration`, `DoorPublicationEvidence`. This module is strict evidence vocabulary, not an I/O or scheduling owner. Its models keep generation, publication, enclosure, termination, legacy, and direct-landing facts explicit so partial or contradictory state fails validation instead of being inferred from queue rows or task prose.

Under CCR-R03@v1 the immutable door generation also carries a typed direct-dependency declaration.
`DoorDependencyInputs` freezes the exact code/memory candidate trees, task-topology fingerprint,
digest-bearing task intent, and the review/memory/admission/scheduling provenance records a
source generation reads; `closeout_door_dependencies` builds the `closeout-door/v1` declaration
(the candidate code tree, optional memory tree, semantic-topology and task-intent identities, the
review and coherence provenance-record edges, admission, scheduling, validator, and predecessor edge), and
`require_closeout_door_dependencies` refuses `closeout-door-dependencies-stale` when a generation's
declared inputs no longer match its canonical source facts
cit:([`DoorDependencyInputs`, `closeout_door_dependencies`, `require_closeout_door_dependencies`], mcp/src/agents_remember/models/lifecycles/door.py:146-155; mcp/src/agents_remember/models/lifecycles/door.py:158-196; mcp/src/agents_remember/models/lifecycles/door.py:199-226).

The door cut narrowed a persisted model, so `DoorPublicationEvidence` also tolerates its own
retired bytes on read. `_RETIRED_DOOR_CONTRACT_DIGEST_FIELDS` names the three contract-byte
digests the model carried while the door lived in the worktree contract
(`expectedBeforeContractSha256`, `expectedPublishedContractSha256`,
`observedPublishedContractSha256`); a `model_validator(mode="before")` strips exactly those names
before validation. They are not fields and cannot be written again, but operation records already
on disk still carry them, and `LifecycleOperationRecord.model_validate` reads them back —
including when cleanup archives and reads back a leaf's canonical terminal enclosure evidence.
Only these three names are tolerated, so every other unknown key stays a hard `extra_forbidden`
refusal. This is the treatment a retired `closeout_door:` contract key already gets: tolerant on
read, gone on the next rewrite
cit:([`_RETIRED_DOOR_CONTRACT_DIGEST_FIELDS`, `_drop_retired_contract_digests`], mcp/src/agents_remember/models/lifecycles/door.py:232-236; mcp/src/agents_remember/models/lifecycles/door.py:252-269).

### Conventions

The file exposes typed values or one narrow operation boundary. Callers consume those values directly rather than reconstructing lower-level state from strings, mutable task documents, or queue projection. Door dependency edges reuse the shared `ar-evidence-dependencies/v1` encoding instead of a door-private digest scheme.

### Invariants And Boundaries

- Preserve the module's single ownership seam; do not add a fallback reader or duplicate authority.
- Expected refusal states remain typed and bounded, while unexpected programming faults remain loud.
- Durable lifecycle facts live in the canonical root journal; scheduling projections may only consume them.
- Door dependencies are declared, never inferred: missing, extra, wrong-version, or stale dependency
  inputs refuse publication/currentness instead of broadening to a universal candidate tuple.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation source applies. | — | — |

## Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| Door generation and dependency construction bind consumed evidence without a ledger identity or provenance edge. | `_decode_legacy_missing_intent`; `CloseoutDoorGeneration`; `closeout_door_dependencies` | mcp/src/agents_remember/models/lifecycles/door.py:89-142; mcp/src/agents_remember/models/lifecycles/door.py:158-196 |
| The module defines `CloseoutDoorGeneration`; `DoorPublicationEvidence` as its public seam. | `CloseoutDoorGeneration` | mcp/src/agents_remember/models/lifecycles/door.py:89-142 |
| The three retired contract-byte digest names and the read-time strip that keeps older persisted operation records loadable while every other unknown key still fails. | `_RETIRED_DOOR_CONTRACT_DIGEST_FIELDS` | mcp/src/agents_remember/models/lifecycles/door.py:232-236 |
| The R03 door dependency vocabulary owned by this record type. | `_edges_are_unique_and_canonical`; `EVIDENCE_DEPENDENCY_POLICIES` | mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:98-118; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:141-211 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No separate external implementation source applies to this file. | — | — |

## 260821-CLIVE Canonical Door Contract

The canonical source has exactly four dispositions: `waiting`, `deferred`, `withdrawn`, and
`claimed`. Its immutable generation identity includes candidate, master, sprint, contract and tree
facts, task-topology fingerprint, code/memory/review/admission/scheduling provenance, and
predecessor edges. `claimed` additionally requires the exact operation identity. Cancel, retire,
supersede, commit, certification, and integration outcomes belong to the lifecycle journal, not the
door vocabulary. Public actions are limited to status, declare, defer, resume, withdraw, and
provenance update with an exact action-specific payload matrix.

## 260831-CCR-R03 Declared Door Dependencies

Generation identity now includes the `dependencies` declaration, and the door source/successor
owners recompute it from the exact candidate tree, topology, intent, and provenance records at
currentness time (worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Removed ledger identities and provenance dependencies from the documented door generation. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/models/lifecycles/door.py` changed since the recorded verification
  commit. Re-read the card against the frozen on-disk source and re-checked its claims and cited
  ranges: nothing this card asserts is falsified by the change, so no wording changed. Verification
  metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (the retired contract-byte digests are stripped on load). Re-read
  the card: it already records the journal-owned door and the retired-digest strip, and every cited
  range matches. No wording changed; verification metadata remains closeout-owned.
- 2026-09-11T14:54:00+02:00 — Retired contract-byte digests stay readable at code commit `76ce662a`: recorded the `model_validator(mode="before")` that strips `expectedBeforeContractSha256` / `expectedPublishedContractSha256` / `observedPublishedContractSha256` from persisted `DoorPublicationEvidence` records, so older operation journals load while every other unknown key remains an `extra_forbidden` failure. Corrected the Purpose to the journal-owned door and repointed the `DoorPublicationEvidence` range (234-253 → 244-274). Verification metadata remains pinned because this is a targeted single-claim repair; source documentation only, no acceptance claim.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the typed `closeout-door/v1` direct-dependency declaration on the immutable door generation and the new door dependency builders/currentness guards; prior disposition, identity, and provenance prose preserved.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-source model package relocation; immutable door generation and request vocabulary are unchanged.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: reconciled the full door-generation and request vocabulary. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.