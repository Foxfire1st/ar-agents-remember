# mcp/src/agents_remember/application/memory_quality/runs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/memory_quality/runs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[application/overview.md](../overview.md)

## Purpose

Bounded single-flight registry for asynchronous memory-quality checks. It is a process-local working
surface, not recovery evidence: live work is retained for polling, terminal history is evictable,
and a new unique request is refused when live work occupies the configured capacity.

## Code Commentary

### Logic

`QualityRunIdentity` contains every result-affecting fact: configured repository, frozen resolved
scope, normalized checks, detail limit, and curator-report publication semantics. Under the module
lock, `start_quality_run` first reuses equivalent live work. It then prunes expired terminal rows and
only enough oldest terminal rows to admit one request. If the registry is still at
`MAX_QUALITY_RUNS`, every retained row is live and the function returns the typed
`capacity-reached` admission without creating a record or thread.

An admitted daemon worker settles its retained row to `completed` or `failed`; launch failure rolls
the row back. `poll_quality_run` requires both configured repository and run id, returns an immutable
snapshot copy, and maps wrong-repository lookup to the same absence as an unknown id.

### Conventions

- Module-level `_registry` plus one `threading.Lock`; admission, pruning, lookup, and settlement
  mutate or inspect shared state under that lock.
- Runtime store only: nothing here survives a process restart. The typed controller translates an
  absent snapshot into nondisclosing `run-not-found` guidance.
- The registry returns `QualityRunAdmission` and `QualityRunSnapshot`; public dictionaries belong to
  `application/memory_quality_controller.py`.

### Invariants And Boundaries

- The cap applies to all retained rows and therefore to live work; terminal pruning never deletes a
  running row.
- Same-identity lookup precedes capacity refusal, so an equivalent start can recover its live run id
  even while capacity is full.
- This module holds no checker reference; the controller supplies one closed callable after scope
  and identity have been resolved.
- Polling is repository-owned and nondisclosing; a run id alone is insufficient.
- Never the survival layer: terminal eviction or restart requires a new request.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical identity and typed registry values. | `QualityRunIdentity`; `QualityRunAdmission`; `QualityRunSnapshot` | mcp/src/agents_remember/application/memory_quality/runs.py:27-53 |
| Admission reuses equivalent live work before terminal pruning and hard live-cap refusal. | `start_quality_run` | mcp/src/agents_remember/application/memory_quality/runs.py:70-104 |
| Polling requires repository ownership and returns a detached snapshot. | `poll_quality_run` | mcp/src/agents_remember/application/memory_quality/runs.py:107-119 |
| Pruning removes terminal rows only. | `_prune_terminal_locked` | mcp/src/agents_remember/application/memory_quality/runs.py:140-161 |
| The typed controller owns public capacity and nondisclosure translations. | `start_memory_quality_request`; `poll_memory_quality_request` | mcp/src/agents_remember/application/memory_quality/controller.py:111-143; mcp/src/agents_remember/application/memory_quality/controller.py:146-208 |

## Cross-Repo References

No cross-repo boundary applies to this runtime registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## MCAR-L03 Poll Identity

`QualityRunSnapshot` now carries the admitted `QualityRunIdentity`, allowing poll to revalidate the
same exact code/memory pair instead of reconstructing scope from repository id.

## Update History

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored the controller start/poll row (76-144 to 111-143/146-208) shifted by the CCR-R08 +57-line controller insertion. Citation-only re-anchor; no content impact.

- 2026-08-29T21:46+02:00 — MCAR-L03: retained exact admitted scope identity in poll snapshots.
  Verification remains closeout-owned.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: replaced the advisory-cap/string-key contract with complete typed identity, same-identity-first admission, terminal-only pruning, a hard live-work cap, launch rollback, and repository-owned poll snapshots. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-20T21:30+02:00 — Created for 260815-DAG-L15-R7: the bounded single-flight background run
  registry (MAX 8, TTL 30 min, completed-only eviction, runtime store per D4) behind the async
  memory-quality surface. Verified at code commit de3a0fd9.
