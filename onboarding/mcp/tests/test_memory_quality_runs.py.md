# mcp/tests/test_memory_quality_runs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_quality_runs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused forcing suite for the bounded typed run registry and the single memory-quality controller.

## Code Commentary

### Logic

`MemoryQualityRunRegistryTests` proves completed/failed/unknown snapshots, same-identity reuse before
capacity refusal, unique-work refusal without thread launch, expired/oldest terminal pruning,
launch-failure rollback, wrong-repository nondisclosure, and concurrent hard-cap admission at
multiple patched capacities. `MemoryQualityControllerTests` proves check and path normalization,
every result-affecting identity field, leaf curator-publication identity, typed capacity guidance,
identical wrong-repository/unknown poll shape, and unknown-check refusal before scope or registry
work.

Under CCR-R03@v1 the curator-publication controller case mocks the exact candidate-tree capture
(`_curator_candidate_inputs`) so the checklist write path is exercised with stable code/memory
candidate trees while the other seams stay real
cit:([`_curator_candidate_inputs`], mcp/tests/test_memory_quality_runs.py:462-472).

### Invariants And Boundaries

- Each test clears the process-local registry; retained state never crosses a case.
- Capacity assertions inspect admitted live records and launched callables, not timing-based peak
  guesses.
- Controller tests mock the slow execution/scope seams narrowly while exercising real identity and
  admission logic.
- Wrong-repository polling is compared structurally with unknown polling to prevent disclosure.
- Curator-publication identity now includes the exact candidate trees captured around the scan.

## Docs References

No configured Domain Documentation source applies; the forcing set is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external authority governs the run registry contract. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Direct registry forcing set. | `MemoryQualityRunRegistryTests` | mcp/tests/test_memory_quality_runs.py:41-190 |
| Canonical controller/identity forcing set. | `MemoryQualityControllerTests` | mcp/tests/test_memory_quality_runs.py:195-405 |
| Registry contract under test. | `QualityRunIdentity`; `start_quality_run`; `poll_quality_run`; `_prune_terminal_locked` | mcp/src/agents_remember/application/memory_quality/runs.py:27-161 |
| Controller contract under test. | `MemoryQualityExecution`; `start_memory_quality_request`; `poll_memory_quality_request` | mcp/src/agents_remember/application/memory_quality/controller.py:48-144 |
| R03 candidate-tree capture mock in the curator-publication case. | `_curator_candidate_inputs` | mcp/tests/test_memory_quality_runs.py:462-472 |

## Cross-Repo References

No cross-repo boundary applies to this forcing suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260821-DAGQC-L2 Registry And Controller Forcing Set

The suite now forces complete typed identity, same-identity reuse before capacity checks, hard live
capacity, terminal-only pruning, thread-launch rollback, detached snapshots, wrong-repository
nondisclosure, explicit capacity guidance, and canonical resolved-scope/check/detail/publication
identity. These tests replace the former string-key/advisory-bounded assertions.

## MCAR-L03 Async Pair Forcing

Controller cases now prove the full pair participates in run identity, start responses expose it,
candidate poll requires the original contract path and revalidates the pair, pair races during
derived checklist evidence block the final publication write, and asynchronous scope refusal is
not rewritten as completion.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the candidate-tree capture mock in the curator-publication controller case; prior registry, capacity, and pair-forcing prose preserved.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: expanded total controller proof for async
  pair refusal, stale candidate polling, official running/failed polling, final publication
  identity, and pair revalidation. The derived-evidence race now mocks its unrelated Git-owned
  classifier so it reaches the intended third revalidation seam.

- 2026-08-29T21:46+02:00 — MCAR-L03: added exact-pair async start/poll/race/refusal coverage.
  Dagger verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the memory-quality controller/run package extraction; concurrency, saturation, polling, and result-identity behavior are unchanged.
- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: rebuilt the focused registry/controller tests around typed identity, hard live capacity, terminal-only pruning, and nondisclosing poll ownership. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: added the never-settles registry
  regression and made the wrapper start/poll case deterministically observe the running envelope
  before completion. Verified at code commit e5cb139f.

- 2026-08-20T21:30+02:00 — Created for 260815-DAG-L15-R7: the run-registry forcing suite
  (start/poll/completed/failed/single-flight/boundedness/TTL eviction) plus the application-wrapper
  tests covering the started/run-not-found/running/failed envelope branches and the key-scoping
  branches (extended in the gate-repair rounds). Verified at code commit de3a0fd9.