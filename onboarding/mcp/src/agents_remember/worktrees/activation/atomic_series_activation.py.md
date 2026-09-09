# mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T18:54:49+02:00 |
| lastVerifiedCommitHash |  `602143bd1d48226f4d53b83ff7c5002a695dcdff`|
| lastVerifiedCommitDate |  2026-09-09T00:26:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[activation overview](overview.md)

## Purpose

This file is the single source-pair-scoped activation authority for durable atomic-master work. A
series contract proves that work exists; this replace-in-place snapshot independently decides which
live series may expose implementation work. The queue only observes it, and task-document mutation
never reads it.

## Code Commentary

### Logic

`atomic_series_source_pair` normalizes repository identity and canonical source branches from the
exact canonical series contract. The deterministic JSON fingerprint names one activation file under
the coordination control plane. `observe_atomic_series` is strict and side-effect free: absence is
vacant, malformed or inconsistent authority is unreadable, a durable vacant record stays vacant,
and a selected terminal contract is observed as effective vacancy.

`publish_atomic_series_selection` runs beneath repository integration authority and the store lock.
It archives unreadable authority before replacement, is idempotent for the same contract/state, and
otherwise advances the record revision. A malformed regular file is copied byte-for-byte with
digest evidence. A symlink, directory, or other nonregular entry is never followed: the entry is
classified via `lstat`, moved atomically to an opaque archive destination, and described by evidence
before the canonical regular snapshot is written. Selection changes logically pause the former
master but do not remove its contract or terminalize its task. Exact continuation/cancellation
checks bind the selected or last-released record to the same master and contract path.
`activation_waiting_reason` projects only unselected, paused-by, or reconciling reasons.

CCR-R25 adds a pure public admission projection beside that authority. `AtomicSeriesActivationError`
retains its observation plus expected/observed edge facts. `AtomicSeriesAdmissionRequest` and
`atomic_series_admission_projection` combine the request, exact source pair, observed activation
record, foreign blocker, wait/corrective-action classification, retry precondition, and a
contract-bound read-only `worktree_status` action. `atomic_series_status_projection` exposes the
same source-grounded observation to series status. These functions only project evidence; selector
publication, release, repair, and source synchronization remain owned by the existing transaction.

CQ01 bounds malformed-authority diagnostics at the public boundary. `bounded_activation_detail`
keeps the original prefix and a visible truncation suffix within 8192 characters; both
`AtomicSeriesActivationObservation.source_fact` and `atomic_series_status_projection` apply it to
unreadable selector detail. The bound preserves the parser error and leaves selector bytes
unchanged, so status and downstream admission can retain actionable evidence without crossing the
response-size contract.

### Conventions

The `StoreOwnership` declaration names MCP as the sole writer. Source identity uses Git common-dir
identity plus canonical local branch, not checkout path or remote-tracking ref. Errors carry a
stable status and detail for boundary translation. Regular-file reads use `O_NOFOLLOW` when the
platform supplies it, so a post-`lstat` symlink swap cannot silently redirect the trusted read.

### Invariants And Boundaries

- Task authoring is wholly upstream and unlocked.
- Multiple live series for one source pair are valid; selection is exposure, not existence.
- Queue projection may observe but cannot publish, release, repair, or own this snapshot.
- A selector record never carries commit/lifecycle evidence.
- Normal observation has no fallback to queue rows, contract census order, task prose, or ambient Git.
- Corrupt authority is preserved before an explicit selecting repair replaces it.
- Nonregular authority is quarantined as an opaque entry; its target/content is never adopted.
- Admission and status projections never infer a live process from `active` or `reconciling`, and
  they never repair a vacant, unreadable, or foreign selection.
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
| Strict Pydantic records define the selector state and archive evidence consumed here. | `AtomicSeriesSourceRef`; `AtomicSeriesSourcePair`; `AtomicSeriesActivationRecord`; `AtomicSeriesActivationArchiveEvidence` | mcp/src/agents_remember/models/structural/atomic_series_activation.py:16-30; mcp/src/agents_remember/models/structural/atomic_series_activation.py:33-39; mcp/src/agents_remember/models/structural/atomic_series_activation.py:42-54; mcp/src/agents_remember/models/structural/atomic_series_activation.py:57-72 |
| The selecting transaction moves reconciling to active only after exact sync. | `activate_atomic_series_contract`; `reconcile_selected_series_under_authority` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:41-79; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:82-100 |
| Queue projection translates this authority only into source facts and waiting reasons. | `project_series_activation` | mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py:30-53 |
| The pure public admission projection retains source-pair observations and contract-bound recovery facts without mutation. | `atomic_series_admission_projection` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:37-89 |
| Public activation diagnostics are bounded before they cross status or admission response boundaries. | `bounded_activation_detail`; `AtomicSeriesActivationObservation.source_fact` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:62-69; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:116-128 |
| The status facade retains the same activation observation without mutation and bounds unreadable detail. | `atomic_series_status_projection` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:502-512 |
| Focused forcing covers absence, replacement, source-pair isolation, exact release, and corrupt bytes. | `AtomicSeriesActivationTests` | mcp/tests/test_atomic_series_activation.py:96-137 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

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
