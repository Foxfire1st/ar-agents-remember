# mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T19:16:43+02:00 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff` |
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[activation overview](overview.md)

## Purpose

Pure public admission and diagnostic projection for one atomic-series operation. It combines the
requested master/contract identity, the exact source-pair observation, any foreign selected master,
the wait or corrective-action classification, a retry precondition, and a contract-bound
`worktree_status` action without publishing or repairing activation authority.

## Code Commentary

### Logic

`AtomicSeriesAdmissionRequest` carries the operation/status/detail inputs plus optional contract,
requested identity, activation observation, classification, and expected/observed edge facts.
`atomic_series_admission_projection` derives missing identity and source-pair values, reports a
foreign blocker only for a different selected `active` or `reconciling` master, and emits the
source-pair fingerprint, activation facts, retry precondition, and read-only status address. The
projection preserves supplied expected/observed edge dictionaries rather than recomputing or
silently dropping them.

CQ01 makes `_admission_activation` apply the same 8192-character bounded diagnostic projection as
the selector observation and status facade. An unreadable activation still reports its concrete
error type and parser-detail prefix, with an explicit truncation suffix when needed; the admission
projection does not mutate or repair the authority.

CQ04 applies that same bound to the admission request's public `detail` field. A malformed parent
contract may yield a parser reason far beyond the response limit; the projection retains its
actionable prefix and truncation marker instead of allowing the structured admission response to
re-expand the raw error.

`_admission_requested_identity` derives the canonical series master reference from a contract when
the caller did not supply one. `_admission_source_pair` uses the observation when present and only
falls back to the contract's source pair; an invalid pair is represented as absent. The blocker,
activation, status-action, and retry helpers keep the output explicit for foreign, vacant,
unreadable, and unobserved states.

### Conventions

The returned mapping uses the public camelCase keys (`sourcePair`, `sourcePairFingerprint`,
`retryPrecondition`, and `statusAction`) while retaining the caller's operation/status/detail.
The status action includes the repository and exact contract path needed for a subsequent
read-only `worktree_status` call.

### Invariants And Boundaries

- This module projects observations; it never writes selector bytes, repairs a contract, releases a
  selection, or synchronizes a source pair.
- `active` and `reconciling` selections are logical ownership facts and never prove that a live
  process exists.
- A missing, vacant, or unreadable observation does not become permission to continue an old
  operation; the retry precondition names the required correction and recheck.
- Foreign blocking identity is emitted only when the selected master differs from the requested
  master and the observed record is in a blocking state.
- Expected and observed contract-edge evidence remains caller-owned and is carried through the
  projection for startup refusal diagnostics.

### Todos

The source is an uncommitted L38 candidate. Closeout owns the eventual commit-derived verification
stamp; this sidecar does not claim acceptance or Gate 5 evidence.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Request fields define the optional source, identity, observation, classification, and edge-evidence inputs. | `AtomicSeriesAdmissionRequest` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:21-34 |
| The public projection assembles classification, requested identity, source pair, activation, blocker, retry, and status evidence while bounding its public detail. | `atomic_series_admission_projection` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:38-92 |
| Requested identity and source-pair resolution preserve canonical contract addressing and explicit invalid-pair absence. | `_admission_requested_identity`; `_admission_source_pair` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:95-121 |
| Foreign selection is a blocker only for a different selected master in `active` or `reconciling` state. | `_admission_blocking` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:124-145 |
| Activation and status-action projections retain observed state, source fingerprint, bounded detail, and exact read-only status arguments. | `_admission_activation`; `_admission_status_action` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:148-193 |
| Retry guidance distinguishes foreign, vacant, unreadable, and general correction states. | `_admission_retry_precondition` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:196-222 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-08T19:16:43+02:00 — CCR-L38 CQ04 preparation rebound the public admission `detail` field to the shared 8192-character diagnostic bound, preserving oversized parser-error evidence through structured refusal output without mutation or acceptance claim.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01 preparation reconciled admission unreadable-detail projection with the shared bounded diagnostic helper. Concrete validation evidence remains available under the public response limit, with no authority mutation or acceptance claim; verification remains closeout-owned.
- 2026-09-08T17:36:08+02:00 — CCR-L38 source-grounded preparation added the one-to-one sidecar for the current `atomic_series_admission.py` diagnostic projection. The source remains uncommitted; the base metadata is retained and closeout owns the eventual verification stamp. No acceptance or Gate 5 claim.
