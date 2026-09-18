# mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T19:16:43+02:00 |
| lastVerifiedCommitHash | `f05ba167cd6dfb56b48a775f3da5d45528c09c82` |
| lastVerifiedCommitDate | 2026-09-18T17:19:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[activation overview](overview.md)

## Purpose

Pure public admission and diagnostic projection for one atomic-series operation. It combines the
requested master/contract identity, the addressed contract's own activation observation, a
contract-scoped retry precondition, and a contract-bound `worktree_status` action without publishing
or repairing activation authority. Selection is per series contract, so a foreign master is never a
blocker or a precondition here: every refusal this module explains is corrective action on the
addressed contract.

## Code Commentary

### Logic

`AtomicSeriesAdmissionRequest` carries the operation/status/detail inputs plus optional contract,
requested identity, activation observation, and expected/observed edge facts.
`atomic_series_admission_projection` derives missing requested identity, emits the
`contractFingerprint` from the observation when present, plus activation facts, retry precondition,
and read-only status address. The projection preserves supplied expected/observed edge dictionaries
rather than recomputing or silently dropping them; it emits none of the removed classification,
blocking, or source-pair keys.

CQ01 makes `_admission_activation` apply the same 8192-character bounded diagnostic projection as
the selector observation and status facade. An unreadable activation still reports its concrete
error type and parser-detail prefix, with an explicit truncation suffix when needed; the admission
projection does not mutate or repair the authority.

CQ04 applies that same bound to the admission request's public `detail` field. A malformed parent
contract may yield a parser reason far beyond the response limit; the projection retains its
actionable prefix and truncation marker instead of allowing the structured admission response to
re-expand the raw error.

`_admission_requested_identity` derives the canonical series master reference from a contract when
the caller did not supply one, and falls back to the contract's own resolved contract path. There is
no source-pair fallback: identity is the requested master plus the exact contract path.
`_admission_retry_precondition` keeps the output explicit for vacant, unreadable, and general
correction states, and never names a different master.

### Conventions

The returned mapping uses the public camelCase keys (`contractFingerprint`, `retryPrecondition`, and
`statusAction`) while retaining the caller's operation/status/detail. The status action includes the
repository and exact contract path needed for a subsequent read-only `worktree_status` call.

### Invariants And Boundaries

- This module projects observations; it never writes selector bytes, repairs a contract, releases a
  selection, or synchronizes a source pair.
- `active` and `reconciling` selections are logical ownership facts and never prove that a live
  process exists.
- A missing, vacant, or unreadable observation does not become permission to continue an old
  operation; the retry precondition names the required correction and recheck.
- No foreign-blocker concept survives: a different master's state is never emitted as this
  contract's blocker, and every retry precondition is scoped to the addressed contract.
- Expected and observed contract-edge evidence remains caller-owned and is carried through the
  projection for startup refusal diagnostics.

### Todos

The source is an uncommitted candidate. Closeout owns the eventual commit-derived verification
stamp; this sidecar does not claim acceptance or Gate 5 evidence.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Request fields define the optional contract, requested identity, activation observation, and edge-evidence inputs. | `AtomicSeriesAdmissionRequest` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:18-30 |
| The public projection assembles requested identity, contract fingerprint, activation, retry, and status evidence while bounding its public detail. | `atomic_series_admission_projection` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:33-74 |
| Requested identity resolves the canonical master reference and the exact contract path with no source-pair fallback. | `_admission_requested_identity` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:77-89 |
| The activation projection retains observed state, contract fingerprint, bounded detail, and exact selected identity. | `_admission_activation` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:92-116 |
| The status action keeps the repository and exact contract path for a read-only `worktree_status` call. | `_admission_status_action` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:119-137 |
| Retry guidance distinguishes vacant, unreadable, and general contract-scoped correction states. | `_admission_retry_precondition` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:140-158 |
| The response model carries the contract fingerprint, activation, retry precondition, and status action with no classification, blocking, or source-pair field. | "class AtomicSeriesAdmission(StrictResponseModel):"; "class AtomicSeriesAdmissionActivation(StrictResponseModel):" | mcp/src/agents_remember/models/worktree.py:228-241; mcp/src/agents_remember/models/worktree.py:203-215 |
| Registered forcing proves a sync refusal addresses only this contract's own state and bounds oversized unreadable detail. | "def test_registered_sync_refusal_addresses_only_this_contracts_own_state(self) -> None:"; "def test_registered_status_and_sync_bound_oversized_unreadable_detail(self) -> None:" | mcp/tests/test_activation_admission_registered.py:178-222; mcp/tests/test_activation_admission_registered.py:268-321 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-13T14:19:25+02:00 — Contract-scoped admission: rewrote Purpose/Logic/Conventions/Invariants so the projection emits `contractFingerprint` plus activation, retry precondition, and status action, removed the classification, blocking, and source-pair keys and the whole cross-contract blocker story, and recorded the contract-scoped vacant/unreadable/general retry wording. Citations rebound to the frozen source; verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-08T19:16:43+02:00 — CCR-L38 CQ04 preparation rebound the public admission `detail` field to the shared 8192-character diagnostic bound, preserving oversized parser-error evidence through structured refusal output without mutation or acceptance claim.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01 preparation reconciled admission unreadable-detail projection with the shared bounded diagnostic helper. Concrete validation evidence remains available under the public response limit, with no authority mutation or acceptance claim; verification remains closeout-owned.
- 2026-09-08T17:36:08+02:00 — CCR-L38 source-grounded preparation added the one-to-one sidecar for the current `atomic_series_admission.py` diagnostic projection. The source remains uncommitted; the base metadata is retained and closeout owns the eventual verification stamp. No acceptance or Gate 5 claim.
