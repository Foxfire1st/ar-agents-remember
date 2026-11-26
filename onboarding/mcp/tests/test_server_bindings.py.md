# mcp/tests/test_server_bindings.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Pytest suite verifying live MCP server binding records under `runtime/server-bindings/<pid>.json`, `run_server` dual-record lifecycle and `runtime/servers/` backward compatibility, dead and recycled PID reclamation, once-only write-error logging, procfs ancestry walking, and `harness_root_pids` filtering.

## Code Commentary

- Uses synthetic `/proc` trees (`_FakeProc`, `_write_proc_entry`, `_stat_line`), a `world` fixture (`McpRuntimeConfig` plus patched `process_serving_build` and `atexit`), and monkeypatched `PROC_ROOT`, `os.kill`, `atomic_write_text`, and `mcp_server.create_server`.
- Eight pytest functions (one parametrized over `bound`, `unbound`, and `unreadable`) verify: bound/unbound/unreadable registration and idempotent cleanup; `run_server` creating and cleaning up both `runtime/servers/<pid>.json` and `runtime/server-bindings/<pid>.json` on normal exit and exception; legacy `server_inventory` seeing only the unchanged `<pid>.json` file; dead and recycled PID reclamation at populations `4` and `16` while leaving `corrupt.json` and `other-schema.json` untouched; once-only write-failure warning; 10-deep ancestry capped at `BINDING_ANCESTOR_LIMIT`, parenthesized `comm`, cycle termination, and absent-`/proc` fallback; and `harness_root_pids` exclusion of descendants, `agents_remember.mcp` processes, wrong env names, and prefix-colliding values plus multi-root discovery.
- Registered in `mcp/tests/test-evidence-lanes.toml` (`unit-regression`) and `mcp/tests/evidence-lifecycle.toml`; source assertions only, not a live run record.

## Relationships

- **Code under test:** `mcp/src/agents_remember/serving/server_bindings.py`, `mcp/src/agents_remember/mcp/server.py` (`run_server`), and `mcp/src/agents_remember/serving/server_registry.py` (`server_inventory`).
- **Catalogs:** `mcp/tests/test-evidence-lanes.toml` and `mcp/tests/evidence-lifecycle.toml`.

## Evidence

- Tests register, read, and idempotently clean up `bound`, `unbound`, and `unreadable` binding records and verify `atexit` registration. [1]
- Tests `run_server` dual registration and cleanup across all three modes, exception cleanup, and legacy `runtime/servers/` compatibility. [2]
- Tests dead and recycled PID reclamation at populations 4 and 16 while preserving corrupt/other-schema files, and verifies once-only write-error logging. [3]
- Tests ancestry depth capping, parenthesized `comm`, cycle termination, absent `/proc`, and `harness_root_pids` environment, cmdline, and hierarchy filtering. [4]
