# mcp/src/agents_remember/providers/grepai/seed.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`seed.py` owns GrepAI workflow-local database clone support for worktree warm-starts.

## Code Commentary

### 260731-EFA-L2 Clone Resolution Split

`_resolve_clone_context` was split so each step owns one question:

- `_clone_inputs(args, target_settings)` → **`_CloneInputs(source_coordination_root,
  target_settings_path, project_id)`** (a `NamedTuple`) or the skip payload naming the first
  missing coordinate. The hermetic-benchmark refusal lives here, so a benchmark-scoped target is
  still refused before any source is read.
- **`_GrepaiCloneEnd(coordination_root, settings_path, provider)`** — one end of the clone. Source
  and target are symmetric, so `_clone_context_from_providers(source, target, ...)` reads as
  source → target instead of six interleaved parameters.
- `_run_with_stall_watchdog(command, watchdog, *, cwd, stdout, stdin)` takes
  **`_StallWatchdog(progress, stall_seconds, poll_seconds=GREPAI_CLONE_POLL_SECONDS)`** — a
  wedge's signature is silence, not duration, so how to sample progress, how often, and how long
  zero movement is tolerated are one rule. The watchdog now also enters `Popen` as a context
  manager: a `stdout=PIPE` caller gets a read end this function owns, and both exits (the stall
  kill and the normal return) leave the `Popen` unreferenced, so without `__exit__` the pipe would
  be finalised by GC rather than by the code that opened it.

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

## Evidence

### Repo-Internal References

- Isolated GrepAI settings define the target roots and workflow-local backend names used by clone operations. [1]
- GrepAI setup calls clone before refresh when seed options are present. [2]
- Provider setup threads source/target settings into GrepAI seed options for worktrees (benchmarks pass none). [3]
