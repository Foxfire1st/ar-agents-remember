# mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- Request fields define the optional contract, requested identity, activation observation, and edge-evidence inputs. [1]
- The public projection assembles requested identity, contract fingerprint, activation, retry, and status evidence while bounding its public detail. [2]
- Requested identity resolves the canonical master reference and the exact contract path with no source-pair fallback. [3]
- The activation projection retains observed state, contract fingerprint, bounded detail, and exact selected identity. [4]
- The status action keeps the repository and exact contract path for a read-only `worktree_status` call. [5]
- Retry guidance distinguishes vacant, unreadable, and general contract-scoped correction states. [6]
- The response model carries the contract fingerprint, activation, retry precondition, and status action with no classification, blocking, or source-pair field. [7]
- Registered forcing proves a sync refusal addresses only this contract's own state and bounds oversized unreadable detail. [8]

### Cross-Repo References

No cross-repository source is configured for this memory root.
