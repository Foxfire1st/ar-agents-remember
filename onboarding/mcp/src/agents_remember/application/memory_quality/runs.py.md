# mcp/src/agents_remember/application/memory_quality/runs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/memory_quality/runs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea` |
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
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
| The canonical identity and typed registry values. | `QualityRunIdentity`; `QualityRunAdmission`; `QualityRunSnapshot` | mcp/src/agents_remember/application/memory_quality/runs.py:26-34; mcp/src/agents_remember/application/memory_quality/runs.py:37-44; mcp/src/agents_remember/application/memory_quality/runs.py:47-53 |
| Admission reuses equivalent live work before terminal pruning and hard live-cap refusal. | `start_quality_run` | mcp/src/agents_remember/application/memory_quality/runs.py:71-105 |
| Polling requires repository ownership and returns a detached snapshot. | `poll_quality_run` | mcp/src/agents_remember/application/memory_quality/runs.py:108-121 |
| Pruning removes terminal rows only. | `_prune_terminal_locked` | mcp/src/agents_remember/application/memory_quality/runs.py:142-163 |
| The typed controller owns public capacity and nondisclosure translations. | `start_memory_quality_request`; `poll_memory_quality_request` | mcp/src/agents_remember/application/memory_quality/controller.py:264-270; mcp/src/agents_remember/application/memory_quality/controller.py:273-279 |

## Cross-Repo References

No cross-repo boundary applies to this runtime registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## MCAR-L03 Poll Identity

`QualityRunSnapshot` now carries the admitted `QualityRunIdentity`, allowing poll to revalidate the
same exact code/memory pair instead of reconstructing scope from repository id.

## Update History

- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): No content impact: this document's own source is unchanged. MIK-R09 (260928-MIK-L09) moved lines in `application/memory_quality/controller.py`, so the citation rows into them were re-pointed by the installed fixer (run once; its generated bullets are kept, since no claim was reworded) or, for the row it declined, by the exact +2 shift. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): No content impact: citation-only repair. Ranges into `mcp/src/agents_remember/application/memory_quality/controller.py`, `mcp/src/agents_remember/application/memory_quality/runs.py`, moved by MIK-R30's line insertions (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-working line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-18T19:55:32+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document** (one table row, two anchors). The row cited `controller.py:111-143` and `146-208`, neither of which holds `start_memory_quality_request` or `poll_memory_quality_request`; the two definitions this leaf's changes left in the controller are at `258-264` and `267-273`, which is what the cell cites now. The claim and both anchors are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored the controller start/poll row (76-144 to 111-143/146-208) shifted by the CCR-R08 +57-line controller insertion. Citation-only re-anchor; no content impact.

- 2026-08-29T21:46+02:00 — MCAR-L03: retained exact admitted scope identity in poll snapshots.
  Verification remains closeout-owned.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: replaced the advisory-cap/string-key contract with complete typed identity, same-identity-first admission, terminal-only pruning, a hard live-work cap, launch rollback, and repository-owned poll snapshots. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-20T21:30+02:00 — Created for 260815-DAG-L15-R7: the bounded single-flight background run
  registry (MAX 8, TTL 30 min, completed-only eviction, runtime store per D4) behind the async
  memory-quality surface. Verified at code commit de3a0fd9.
