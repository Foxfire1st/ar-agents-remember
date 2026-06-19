# mcp/src/agents_remember/providers/grepai/seed.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/seed.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00     |
| lastVerifiedCommitHash | `add1235644c8a5a4b5d6a1b114f29510cdc03d36`                         |
| lastVerifiedCommitDate | 2026-06-19T15:03:04+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`seed.py` owns GrepAI workflow-local database clone support for worktree warm-starts.

## Code Commentary

### Logic

`_resolve_clone_context` first refuses a **benchmark-scoped** target: when the target `grepai-memory` provider's `instance.scope == "benchmark"`, it returns `_clone_skip` immediately, before reading any source, so a benchmark stack can never clone from another provider stack (hermetic). Otherwise the module resolves a source and target `grepai-memory` provider from explicit settings, starts both Postgres backends through lifecycle calls, and clones the source database into the target with `pg_dump` piped through a temporary SQL file into `psql`. The dump/restore commands have no total-time cap (clone time scales with index size by design, though copies run <60s in practice) but execute under `_run_with_stall_watchdog`: a `Popen` poll loop that kills the child only after `GREPAI_CLONE_STALL_SECONDS` (300, overridable via `seed_stall_seconds`) of **zero progress** — dump progress is the temp file's size, restore progress is `_target_database_size` (a bounded `pg_database_size` query against the target container). A stall returns a structured phase-named result (`phase: dump/restore`, `stalled: True`, the stall window, and an operator-facing message); the watchdog routes child stderr to a temp file so an unread pipe buffer can never deadlock the child. `GrepaiCloneContext` carries the resolved project id, source/target coordination roots, backend containers, database names, users, passwords, and settings files. Dry-runs return the planned dump/restore commands without touching Docker.

### Invariants And Boundaries

- A benchmark-scoped target is never cloned (hermetic): `_resolve_clone_context` returns `_clone_skip` before resolving any source, so a benchmark cannot start or read the live workspace GrepAI backend. Defense-in-depth alongside the benchmark runner no longer wiring a seed source (task 260619).
- A wedge's signature is silence, not duration: only zero progress for the stall window may kill a clone; a progressing clone of any size must never be killed (2026-06-10 design review — this mechanic enables rapid worktree provider deployment).
- Source and target GrepAI backend containers must be different; same-container clone requests are skipped instead of mutating the live provider in place.
- An intentional skip (no source memory configured, same source/target backend, missing source settings, benchmark-scoped target, etc.) is a benign outcome, not a failed phase: `_clone_skip` returns `ok: True` with `skipped: True`, mirroring CGC's benign skips.
- The clone is database-level warm-start, not a text rewrite of indexed chunks. The watcher reconciles active-project file changes after target settings point at the workflow-local memory root.
- Source provider settings may come from the current settings file when source and target coordination roots match, or from an explicit source settings path for worktree workflow-local copies.
- The module starts backends only; watcher refresh and provider-level sequencing stay in `grepai/setup.py` and `provider_setup.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Isolated GrepAI settings define the target roots and workflow-local backend names used by clone operations. | [isolated.py](isolated.py.md) |
| GrepAI setup calls clone before refresh when seed options are present. | [setup.py](setup.py.md) |
| Provider setup threads source/target settings into GrepAI seed options for worktrees (benchmarks pass none). | [../provider_setup.py](../provider_setup.py.md) |
| Tests cover dry-run clone planning, benchmark-style target settings, and the benchmark-scope clone guard. | [../../../../../tests/test_provider_setup.py](../../../../../tests/test_provider_setup.py.md) |
| Watchdog complete/stall/progress-reset/exit-code behavior and the no-total-cap contract are unit-tested. | [../../../../../tests/test_seed_timeouts.py](../../../../../tests/test_seed_timeouts.py.md) |

## Update History

- 2026-06-19T13:42: `_resolve_clone_context` now refuses a benchmark-scoped target (`instance.scope == "benchmark"`) with a `_clone_skip` before resolving any source, so a benchmark stack can never clone from another provider stack (hermetic). Defense-in-depth alongside the benchmark runner no longer wiring a seed source; corrected Purpose/Invariants since benchmarks no longer warm-start (task 260619).
- 2026-06-10T05:30+02:00 — `_clone_database` runs under a stall watchdog (`_run_with_stall_watchdog`): no total-time cap (clones scale with index size by design), killed only after 300s of zero progress (dump-file growth / `_target_database_size` probe), returning a structured phase-named `stalled` result. stderr goes to a temp file so unread pipe buffers cannot deadlock the child.
- 2026-05-31T12:30+02:00 — Documented that `_clone_skip` now returns `ok: True` (benign skip, mirroring CGC) instead of `ok: False` (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented that clone dump/restore now run uncapped (`timeout=None`) since clone time scales with index size (never-cap-indexing run). Verified against `825a172`.
- 2026-05-29T18:35+02:00: Narrowed the `GrepaiCloneContext | dict` union via `isinstance` and removed the dead `_is_clone_skip`; behavior-preserving (commit `0549b28`).
- 2026-05-27T18:10:12+02:00: Created for GrepAI provider warm-start support.
