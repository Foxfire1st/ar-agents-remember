# mcp/src/agents_remember/benchmarks/runner.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`runner.py` is now a compatibility facade for the benchmark prepare/run/analyze
surface. The benchmark implementation lives in `runner_modules/`, while this
module preserves the historical `agents_remember.benchmarks.runner` import path
used by MCP application entry points, CLI entrypoints, and tests.

## Code Commentary

### Logic

The facade re-exports focused benchmark modules for existing callers and keeps a
small compatibility wrapper around `prepare_repo()` so tests and callers that
monkeypatch `benchmark_runner.run_command`, `benchmark_runner.remove_path`, or
`benchmark_runner.repo_has_commit` still affect repository preparation. It also
keeps `shutil`, `subprocess`, and `provider_setup` available as module
attributes because benchmark portability tests patch those old facade-level
objects.

The extracted implementation responsibilities are governed by
`runner_modules/overview.md`: manifest parsing, workspace preparation,
MCP/provider registration, Codex execution, JSONL analysis, service payloads,
and CLI wiring each live in a focused file.

### Invariants And Boundaries

- Keep this file thin; new benchmark behavior belongs in the owning
  `runner_modules` file.
- Preserve the public `agents_remember.benchmarks.runner` import surface unless
  all MCP application entry point and test callers are migrated in the same change.
- The facade is allowed to contain compatibility glue for monkeypatch-sensitive
  public functions, but not benchmark business logic.
- `__main__` dispatch must continue to call the extracted CLI `main()`.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- MCP benchmark tools import the facade as `benchmark_runner`. [1]

### Cross-Repo References

No configured sibling repository is required for this facade.
