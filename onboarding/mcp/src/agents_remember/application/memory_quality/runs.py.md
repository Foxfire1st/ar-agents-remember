# mcp/src/agents_remember/application/memory_quality/runs.py

## Governing Overview

[application/overview.md](../overview.md)

## Purpose

Bounded single-flight registry for asynchronous memory-quality checks and citation previews. It is a process-local working
surface, not recovery evidence: live work is retained for polling, terminal history is evictable,
and a new unique request is refused when live work occupies the configured capacity.

## Code Commentary

### Logic

`QualityRunIdentity` contains every result-affecting fact: configured repository, frozen resolved
scope, normalized checks, detail limit, curator-report publication semantics, operation kind and immutable document selectors. Under the module
lock, `start_quality_run` first reuses equivalent live work. It then prunes expired terminal rows and
only enough oldest terminal rows to admit one request. If the registry is still at
`MAX_QUALITY_RUNS`, every retained row is live and the function returns the typed
`capacity-reached` admission without creating a record or thread.

An admitted daemon worker settles its retained row to `completed` or `failed`; launch failure rolls
the row back. `poll_quality_run` requires both configured repository and run id, returns a detached
snapshot whose retained result is deep-copied, and maps wrong-repository lookup to the same absence as an unknown id.

### Conventions

- Module-level `_registry` plus one `threading.Lock`; admission, pruning, lookup, and settlement
  mutate or inspect shared state under that lock.
- Runtime store only: nothing here survives a process restart. The typed controller translates an
  absent snapshot into nondisclosing `run-not-found` guidance.
- The registry returns `QualityRunAdmission` and `QualityRunSnapshot`; public dictionaries belong to
  `application/memory_quality/controller.py` and `run_answers.py`.

### Invariants And Boundaries

- The cap applies to all retained rows and therefore to live work; terminal pruning never deletes a
  running row.
- Same-identity lookup precedes capacity refusal, so an equivalent start can recover its live run id
  even while capacity is full.
- This module holds no checker reference; the quality controller or citation-preview owner supplies one closed callable after scope
  and identity have been resolved.
- Polling is repository-owned and nondisclosing; a run id alone is insufficient.
- Never the survival layer: terminal eviction or restart requires a new request.

## Evidence

### Repo-Internal References







### Cross-Repo References

No cross-repo boundary applies to this runtime registry.

No meaningful cross-repo references found.

## MCAR-L03 Poll Identity

`QualityRunSnapshot` now carries the admitted `QualityRunIdentity`, allowing poll to revalidate the
same exact code/memory pair instead of reconstructing scope from repository id.

## Shared preview identity and retained results

Citation previews use this same capacity-eight registry. The operation and frozen document selectors prevent a preview from aliasing a quality check or another selection. The worker deep-copies a completed result into retention, and polling deep-copies it again, so mutation by the producer or a caller cannot rewrite later polls. Worker exceptions settle a failed run; a completed computation can still carry an unsuccessful quality or repair result. Terminal eviction and process restart remain loss of runtime state, not durable recovery evidence.


- Run identity distinguishes operation and immutable selectors. [6]


- Results are detached at retention and polling. [7]



- The canonical identity and typed registry values. [1]



- Admission reuses equivalent live work before terminal pruning and hard live-cap refusal. [2]



- Polling requires repository ownership and returns a detached snapshot. [3]



- Pruning removes terminal rows only. [4]



- The typed controller owns public capacity and nondisclosure translations. [5]
