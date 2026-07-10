# mcp/tests/_scaling.py

| Field                  | Value                            |
| ---------------------- | -------------------------------- |
| repository             | agents-remember                  |
| path                   | `mcp/tests/_scaling.py`          |
| doc_type               | `file-level-onboarding`          |
| lastUpdated            | 2026-07-09T19:31+02:00           |
| lastVerifiedCommitHash |                                  `e400ed0ce98752d1b65d00de97c9b84c7ea20814`|
| lastVerifiedCommitDate |                                  2026-07-10T20:04:45+02:00|
| governingOverview      | `../overview.md`                 |

## Governing Overview

[mcp overview](../overview.md) — there is no route-local `mcp/tests/overview.md`; existing test sidecars are governed by the package overview.

## Purpose

`_scaling.py` is the shared CS-6 regression helper module for durable-store, projection, and process/session scaling tests. It gives future store/process surfaces one reusable assertion floor instead of re-deriving growth and reclamation checks per test file.

## Code Commentary

### Logic

`measure_scaling()` records deterministic cost values or best-of wall-clock timings across input sizes. `assert_subquadratic()` requires at least two distinct sizes and compares smallest to largest cost against an `n**1.7` ceiling, making accidental quadratic behavior fail loudly. `assert_bounded_file_size()` checks post-compaction file size, and `assert_bounded_count()` checks fan-out/read/process/session counts against a cap.

### Conventions

Prefer deterministic operation counts over wall-clock timings when a mechanism exposes them; wall-clock is the fallback. Tests should call these helpers at two or more sizes for CS-6 D2/D3 surfaces.

### Invariants And Boundaries

A single-size smoke test is not a CS-6 scaling proof. This helper intentionally raises when `assert_subquadratic()` receives fewer than two sizes.

### Todos

No known follow-up in this file.

## Docs References

No external documentation governs these repo-local regression helpers.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The helper module documents the CS-6 regression floor and the three assertion families future tests reuse. | L1-L18; L58-L125 | [mcp/tests/_scaling.py](agents-remember/mcp/tests/_scaling.py) |
| Store/projection CS-6 tests import the helpers for bounded count, bounded file size, and subquadratic proofs. | L20; L438-L571 | [mcp/tests/test_store_scaling_cs6.py](agents-remember/mcp/tests/test_store_scaling_cs6.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Same-repository tests only. | N/A | N/A |

## Update History

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: created for the shared CS-6 scaling/reclamation assertion helpers added with the store and projection scaling regressions. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
