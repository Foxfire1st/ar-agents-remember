# mcp/src/agents_remember/models/structural/atomic_series_activation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/structural/atomic_series_activation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T11:43+02:00 |
| lastVerifiedCommitHash |  `e0820b04a499cbfb2079c78485346c50917a238a`|
| lastVerifiedCommitDate |  2026-09-13T18:02:04+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The activation store derives this contract's own fingerprint and refuses any record that is not this exact contract. | "def contract_fingerprint("; `_require_record_identity` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-134; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:360-372 |
| Focused tests prove that two contracts sharing one protected source pair hold independent selection, that vacant and active are never waiting states, that release addresses only the released contract, and that another contract's record can never be adopted. | `class AtomicSeriesActivationTests(unittest.TestCase):`; `test_contracts_sharing_one_source_pair_hold_independent_selection`; `test_vacant_and_active_are_never_waiting_states`; `test_release_addresses_only_the_released_contract`; `test_another_contracts_record_can_never_be_adopted` | mcp/tests/test_atomic_series_activation.py:109-206 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-13T14:21:37+02:00 — LOCR-L36 contract-scoped activation re-key: rewrote Purpose, Logic, Conventions, and Invariants around the per-contract record — `AtomicSeriesActivationRecord` is now `schemaVersion "2.0"` carrying `contractFingerprint` (SHA-256 of the canonical resolved contract path), `AtomicSeriesActivationArchiveEvidence` is `"2.0"` too, and the deleted `AtomicSeriesSourceRef` / `AtomicSeriesSourcePair` models plus the `sourcePairFingerprint` field no longer appear anywhere in this card. Added the invariant that one canonical series contract (not one protected source pair) has at most one replace-in-place record, and that a foreign contract's snapshot is refused with `atomic-series-activation-contract-mismatch`. Rebound both reference rows: the store row now cites `contract_fingerprint` and `_require_record_identity`, and the test row cites the contract-scoped forcing tests by name instead of the removed source-pair isolation wording. No verification stamp advanced.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01 preparation rebound the structural activation citations to the current source-pair and identity-validator definitions; the model vocabulary is unchanged and no acceptance claim is made.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `AtomicSeriesActivationTests` repointed to mcp/tests/test_atomic_series_activation.py:96-137. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of source-pair, selection, and archive
  vocabulary; verification awaits the real code commit.

- 2026-08-26T06:05+02:00 — Moved this card with the model into `models/structural/`; canonical
  vocabulary and history are preserved, and the structural route now governs it. Final ranges
  remain post-Dagger-owned.

- 2026-08-26T05:40+02:00 — Reconciled archive evidence with the final regular/opaque/absence
  vocabulary and nonregular-entry quarantine. Final ranges remain post-Dagger-owned.

- 2026-08-26T02:55+02:00 — Drafted strict one-to-one onboarding for the moving IAS candidate;
  final citation ranges and verification provenance remain post-Dagger work.
