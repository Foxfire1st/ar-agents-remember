# mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T18:54:49+02:00 |
| lastVerifiedCommitHash |  `e0820b04a499cbfb2079c78485346c50917a238a`|
| lastVerifiedCommitDate |  2026-09-13T18:02:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[activation overview](overview.md)

## Purpose

This file is the per-series-contract activation authority for durable atomic-master work. A series
contract proves that work exists; this replace-in-place snapshot separately records whether that one
contract is currently `reconciling` or `active`. The record is keyed by the canonical series
contract, so two atomic masters that share one protected code/external-memory source pair never share
this state: each tracks only its own `reconciling -> active` transition. The queue only observes it,
and task-document mutation never reads it.

## Code Commentary

### Logic

`contract_fingerprint` hashes the canonical resolved contract path with `sha256`, and
`activation_path(coordination_root, contract)` names exactly one activation file under the
coordination control plane (`controlplane/atomic-series-activation/<digest>.json`). Contract identity,
not source-pair identity, addresses the record.

`observe_atomic_series(contract)` is strict and side-effect free: absence is vacant, malformed or
inconsistent authority is unreadable, a durable vacant record stays vacant, and a selected terminal
contract is observed as effective vacancy. `observe_atomic_series_path(contract, path)` takes the
same contract, so every read carries this contract's fingerprint. `AtomicSeriesActivationObservation`
carries `contract_path` and `contract_fingerprint` alongside the observed state, record, error type,
and detail, and `source_fact` publishes the `contractFingerprint` with the address and state.
`_require_record_identity` refuses any record whose `contractFingerprint` or resolved `contractPath`
is not this exact contract with status `atomic-series-activation-contract-mismatch`, so another
contract's record can never be adopted as this one's authority.

`publish_atomic_series_selection` runs beneath repository integration authority and the store lock.
It archives unreadable authority before replacement, is idempotent for the same contract/state, and
otherwise advances the record revision. A malformed regular file is copied byte-for-byte with digest
evidence. A symlink, directory, or other nonregular entry is never followed: the entry is classified
via `lstat`, moved atomically to an opaque archive destination, and described by evidence before the
canonical regular snapshot is written. Per-contract selection records current exposure for that one
contract: it neither removes another contract's record nor terminalizes another master's task. Exact continuation/cancellation
checks bind the addressed record to the same master and canonical contract path.

`activation_waiting_reason(observation)` takes only the observation and returns only
`atomic-series-reconciling` while that contract is reconciling. Vacant, active, and any foreign
record are never waiting reasons; genuine wave dependencies remain the sprint execution graph's own
`predecessor-incomplete:` reasons.

`require_selected_atomic_series` is the this-contract's-own-in-flight guard for
`resolution_action="continue"`: it proves the observation is the required `reconciling` state and the
record selects this contract's canonical master and path. `require_atomic_series_cancellation_owner`
performs the same proof for cancel/replay against this contract's selected or last-released record.
`publish_atomic_series_selection` refuses a terminal contract with `atomic-series-terminal`.

CCR-R25 adds a pure public admission projection beside that authority. `AtomicSeriesActivationError`
retains its observation plus expected/observed edge facts. `AtomicSeriesAdmissionRequest` and
`atomic_series_admission_projection` combine the request, the addressed contract's own activation
observation, a contract-scoped retry precondition, and a contract-bound read-only `worktree_status`
action; there is no foreign-blocker or source-pair classification. `atomic_series_status_projection`
exposes the same contract-grounded observation to series status. These functions only project
evidence; selector publication, release, repair, and source synchronization remain owned by the
existing transaction.

CQ01 bounds malformed-authority diagnostics at the public boundary. `bounded_activation_detail`
keeps the original prefix and a visible truncation suffix within 8192 characters; both
`AtomicSeriesActivationObservation.source_fact` and `atomic_series_status_projection` apply it to
unreadable selector detail. The bound preserves the parser error and leaves selector bytes
unchanged, so status and downstream admission can retain actionable evidence without crossing the
response-size contract.

### Conventions

The `StoreOwnership` declaration names MCP as the sole writer and states that one
`reconciling -> active` transition is recorded per canonical series contract. Contract addressing uses
the canonical series contract path; master identity uses the canonical `TaskDocumentRef`, never a
source branch, checkout path, or remote-tracking ref. Errors carry a stable status and detail for
boundary translation. Regular-file reads use `O_NOFOLLOW` when the platform supplies it, so a
post-`lstat` symlink swap cannot silently redirect the trusted read.

### Invariants And Boundaries

- Task authoring is wholly upstream and unlocked.
- Activation state is per contract: two atomic masters sharing one protected source pair hold
  independent records, and one selection never pauses, replaces, or clears the other.
- Queue projection may observe but cannot publish, release, repair, or own this snapshot.
- A selector record never carries commit/lifecycle evidence.
- Normal observation has no fallback to queue rows, contract census order, task prose, or ambient Git.
- A record whose fingerprint or contract path is not this exact contract is unreadable for this
  contract and is never adopted as its authority.
- Corrupt authority is preserved before an explicit selecting repair replaces it.
- Nonregular authority is quarantined as an opaque entry; its target/content is never adopted.
- Only this contract's own `reconciling` state is a waiting reason; a foreign master is never a
  reason to wait.
- Admission and status projections never infer a live process from `active` or `reconciling`, and
  they never repair a vacant, unreadable, or mismatched selection.
- Public unreadable-detail projections remain bounded while preserving a concrete parser-error
  prefix and explicit truncation marker.

### Todos

Exact selector claims and citations are reconciled to the frozen source; verification remains
closeout-owned until the real code commit exists.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Strict Pydantic records define the contract-keyed selector state and archive evidence consumed here. | `AtomicSeriesActivationRecord`; `AtomicSeriesActivationArchiveEvidence` | mcp/src/agents_remember/models/structural/atomic_series_activation.py:16-27; mcp/src/agents_remember/models/structural/atomic_series_activation.py:30-45 |
| The fingerprinted record is keyed by the canonical series contract path and stores no source-pair field. | "class AtomicSeriesActivationRecord(BaseModel):"; "class AtomicSeriesActivationArchiveEvidence(BaseModel):" | mcp/src/agents_remember/models/structural/atomic_series_activation.py:16-27; mcp/src/agents_remember/models/structural/atomic_series_activation.py:30-45 |
| A sha256 of the canonical contract path is the per-contract identity that names one activation record. | "def contract_fingerprint("; "def activation_path(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-134; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:137-142 |
| The strict observation carries the contract path and fingerprint for every read. | "class AtomicSeriesActivationObservation:"; "def source_fact(self) -> dict[str, object]:" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:91-102; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:115-127 |
| Any record that is not this exact contract is refused as a mismatch instead of adopted. | `_require_record_identity`; `atomic-series-activation-contract-mismatch` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:360-372; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:369-372 |
| Strict, side-effect-free observation resolves absent, nonregular, malformed, and terminal cases into vacant/unreadable facts. | `observe_atomic_series`; `observe_atomic_series_path` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:145-152; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:290-335 |
| Publication is idempotent per contract/state, archives corrupt authority first, and quarantines nonregular entries without following them. | `publish_atomic_series_selection`; `_archive_unreadable_selection` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:155-212; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:453-524 |
| Only this contract's own reconciling state is projected as a waiting reason. | `activation_waiting_reason`; `atomic-series-reconciling` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:275-287; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:285-287 |
| Continuation and cancellation bind to this contract's own selected or last-released record. | `require_selected_atomic_series`; `require_atomic_series_cancellation_owner` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:215-243; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:246-272 |
| A terminal contract cannot be selected. | "atomic-series-terminal" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:168-172 |
| Public activation diagnostics are bounded before they cross status or admission response boundaries. | `bounded_activation_detail`; "def source_fact(self) -> dict[str, object]:" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:61-68; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:115-127 |
| The status facade retains the same contract-grounded activation observation without mutation and bounds unreadable detail. | `atomic_series_status_projection` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:434-444 |
| The selecting transaction moves this contract's reconciling state to active only after exact sync. | `activate_atomic_series_contract`; `reconcile_selected_series_under_authority` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:55-100; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:103-121 |
| Queue projection translates this authority only into contract source facts and waiting reasons. | `project_series_activation` | mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py:29-51 |
| The pure public admission projection retains this contract's activation observation and contract-scoped recovery facts without mutation. | `atomic_series_admission_projection` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:33-74 |
| Focused forcing covers two masters sharing one source pair, vacant/active non-waiting states, exact release, non-adoption of another contract's record, and the terminal refusal. | "class AtomicSeriesActivationTests(unittest.TestCase):"; `test_contracts_sharing_one_source_pair_hold_independent_selection`; `test_another_contracts_record_can_never_be_adopted` | mcp/tests/test_atomic_series_activation.py:109-140; mcp/tests/test_atomic_series_activation.py:117-140; mcp/tests/test_atomic_series_activation.py:174-209 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-13T14:19:04+02:00 — Per-contract re-keying: rewrote Purpose/Logic/Conventions/Invariants around `contract_fingerprint`/`activation_path` contract addressing, the `contract_path`+`contract_fingerprint` observation, `_require_record_identity`'s `atomic-series-activation-contract-mismatch` refusal, and `activation_waiting_reason` returning only `atomic-series-reconciling`. Removed the source-pair model, fingerprint, waiting reasons, and logical-pause claims, and rebound every citation to the frozen source. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01 preparation reconciled the bounded unreadable-detail projection through the observation source fact and status facade. The parser-error prefix and truncation marker remain source-grounded, selector bytes remain read-only, and verification metadata stays closeout-owned; no acceptance claim.
- 2026-09-08T17:47:39+02:00 — CCR-L38 source-grounded preparation split the admission and status citations after the public admission projection moved into its dedicated module. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: recorded the pure admission and status projections, retained activation observations, and no-live-process inference boundary. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `AtomicSeriesActivationTests` repointed to mcp/tests/test_atomic_series_activation.py:96-137. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of selector observation, publication,
  archive, and exact identity claims.

- 2026-08-26T06:05+02:00 — Moved with the selector into the focused `worktrees/activation/` route;
  behavior and prior history are preserved, with no old-path compatibility owner.

- 2026-08-26T05:40+02:00 — Reconciled the completed nonregular-entry quarantine: strict `lstat`,
  no-follow regular reads, opaque atomic move plus evidence, and refusal when preservation cannot
  complete. Final ranges remain post-Dagger-owned.

- 2026-08-26T02:55+02:00 — Drafted the selector authority against the pre-Dagger frozen partition;
  nonregular-entry repair, exact ranges, and verification remain open.
