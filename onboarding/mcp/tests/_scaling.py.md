# mcp/tests/_scaling.py

| Field                  | Value                            |
| ---------------------- | -------------------------------- |
| repository             | agents-remember                  |
| path                   | `mcp/tests/_scaling.py`          |
| doc_type               | `file-level-onboarding`          |
| lastUpdated            | 2026-07-09T19:31+02:00           |
| lastVerifiedCommitHash |                                  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |                                  2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                 |

## Governing Overview

[mcp overview](../overview.md) — there is no route-local `mcp/tests/overview.md`; existing test sidecars are governed by the package overview.

## Purpose

`_scaling.py` is the shared CS-6 regression helper module for durable-store, projection, and process/session scaling tests. It gives future store/process surfaces one reusable assertion floor instead of re-deriving growth and reclamation checks per test file.

## Code Commentary

### Logic

`measure_scaling()` records deterministic cost values or best-of wall-clock timings across input sizes. `assert_subquadratic()` requires at least two distinct sizes and compares smallest to largest cost against a growth ceiling, making accidental quadratic behavior fail loudly. `assert_bounded_file_size()` checks post-compaction file size, and `assert_bounded_count()` checks fan-out/read/process/session counts against a cap.

The ceiling is one frozen `GrowthCeiling(exponent, tolerance)` value, not two independent keywords: `limit_for(size_ratio)` returns `size_ratio**exponent * (1 + tolerance)` and `absolute_floor` returns `max(1e-6, tolerance)` for the degenerate small-N-cost-is-zero branch. The module-level `SUBQUADRATIC = GrowthCeiling()` is the default (`n**1.7` with `DEFAULT_SUBQUADRATIC_EXPONENT` and 50% CI headroom), and `assert_subquadratic()` takes it as `ceiling: GrowthCeiling = SUBQUADRATIC`. A caller loosening the bound therefore says so once, in a named place, instead of nudging half of it at a call site.

### Conventions

Prefer deterministic operation counts over wall-clock timings when a mechanism exposes them; wall-clock is the fallback. Tests should call these helpers at two or more sizes for CS-6 D2/D3 surfaces.

### Invariants And Boundaries

A single-size smoke test is not a CS-6 scaling proof. This helper intentionally raises when `assert_subquadratic()` receives fewer than two sizes.

### Todos

No known follow-up in this file.

## Docs References

No external documentation governs these repo-local regression helpers.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The helper module documents the CS-6 regression floor and the three assertion families future tests reuse. | `measure_scaling`; `assert_subquadratic`; `assert_bounded_file_size`; `assert_bounded_count` | mcp/tests/_scaling.py:62-85; mcp/tests/_scaling.py:88-131; mcp/tests/_scaling.py:134-141; mcp/tests/_scaling.py:144-155 |
| The `GrowthCeiling` value object and the `SUBQUADRATIC` default that `assert_subquadratic()` accepts as one `ceiling` parameter. | `GrowthCeiling`; `SUBQUADRATIC`; `assert_subquadratic` | mcp/tests/_scaling.py:33-55; mcp/tests/_scaling.py:58-58; mcp/tests/_scaling.py:88-131 |
| The CS-6 store/projection suite imports the three scaling helpers and invokes them in its compaction and cooldown scenarios. | "from _scaling import"; `test_compact_reclaims_stale_records_and_bounds_file_at_two_sizes`; `test_in_cooldown_with_snapshot_does_not_read_the_file` | mcp/tests/test_store_scaling_cs6.py:27-27; mcp/tests/test_store_scaling_cs6.py:98-117; mcp/tests/test_store_scaling_cs6.py:119-149 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository tests only. | N/A | N/A |

## Update History
- 2026-08-04T13:25:51+02:00 — 260731-EFA-L6 S18-B01 same-reviewer semantic-binding repair: bound helper reuse to the importing suite's concrete scenarios under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the `test_store_scaling_cs6.py`
  citation. The single import of all three helpers is L27 (was cited L20, which is now
  `import unittest`), and the stamped `L438-L571` block no longer contains any helper call. Grepped
  the file for the three names: 16 call sites spread L113-L701, so the row now cites the import plus
  one verified example of each family — L113-L117 (`assert_bounded_file_size` then
  `assert_subquadratic` on post-compact signal-log bytes), L147-L149 (`assert_bounded_count` on
  reads across 50 cooldown checks) and L604-L617 (bounded sweep disk reads/writes plus the
  subquadratic sweep). Claim reworded to say the helpers are reused throughout rather than confined
  to one block, since that is what the file shows.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: `assert_subquadratic()` no longer takes the
  loose `exponent`/`tolerance` keywords the card described — the two are now one frozen
  `GrowthCeiling` with `limit_for()` and `absolute_floor`, defaulted by the new module-level
  `SUBQUADRATIC`, and the parameter is `ceiling: GrowthCeiling = SUBQUADRATIC`. The Logic
  section was rewritten to name that object and its arithmetic, the reference row was
  re-anchored to the current file (L1-L18 and L58-L125 became L1-L19 and L62-L155 after the
  29-line dataclass block landed above the helpers), and a row was added for the value object
  itself. The two-distinct-sizes requirement and the other three assertion families are
  unchanged.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: created for the shared CS-6 scaling/reclamation assertion helpers added with the store and projection scaling regressions. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
