# mcp/src/agents_remember/serving/server_bindings.py

## Governing Overview

[overview](overview.md)

## Purpose

Publishes and reads per-PID live MCP server binding and process-ancestry records under `<coordination-root>/runtime/server-bindings/<pid>.json`, and discovers live harness root PIDs via Linux `/proc`. Keeps seat identity confirmation separate from legacy `runtime/servers/<pid>.json` so older `_ServerRecord` readers stay unaffected.

## Code Commentary

- **Strict models (`extra="forbid"`):** `ProcessAncestor` (`pid`, `processStart`), `BoundIdentityPayload` (`agentId`, `requestId`, `role`, optional `sprintDocumentRef`/`masterDocumentRef`/`taskDocumentRef`), and `ServerBindingRecord` (`pid`, `processStart`, `startedAt`, `configPath`, `parentPid`, `parentProcessStart`, `ancestors`, `bindingState` in `"bound" | "unbound" | "unreadable"`, `binding`, `unreadableReason`).
- **Procfs and ancestry:** `_read_stat_fields(pid)` splits `/proc/<pid>/stat` on the last `')'` (`rsplit(")", 1)`) so `comm` fields containing spaces or parentheses parse cleanly. `process_ancestors(pid, limit=8)` walks upward stopping at `pid <= 1`, cycle detection, or `BINDING_ANCESTOR_LIMIT` (`8`); if `/proc` is absent and `pid == os.getpid()`, falls back to `[ProcessAncestor(pid=os.getppid(), processStart=None)]` when `ppid > 1`.
- **Atomic registration and cleanup:** `bindings_directory(config)` resolves `config.coordination_root / "runtime" / "server-bindings"`. `register_server_binding` writes `<pid>.json` atomically via `atomic_write_text` and returns an idempotent `cleanup()` callback (also registered with `atexit`). Write `OSError`s log once per process through thread-safe `_BindingWarnings` without stopping the server; unlink failures log a warning.
- **Liveness and reclamation:** `live_server_bindings(config)` reads `*.json`, validates each file, and checks PID liveness (`os.kill(pid, 0)`, treating `PermissionError` as alive) plus `processStart` equality when both sides are present. Dead or recycled-PID files are unlinked and omitted; corrupt or wrong-schema JSON files are skipped and left untouched.
- **Harness root discovery:** `harness_root_pids(agent_id)` returns `None` when `/proc` is unavailable or unreadable and `[]` for an empty `agent_id`. Otherwise it scans numeric `/proc/<pid>` entries for exact NUL-delimited `PASEO_AGENT_ID=<agent_id>` in `environ`, excludes processes whose `cmdline` is unreadable or contains `b"agents_remember.mcp"`, and returns sorted root PIDs whose `ppid` is not itself in the matching set.

## Relationships

- **Callers:** `mcp/src/agents_remember/mcp/server.py` (`_register_process_binding` and `run_server` register and clean up peer binding records alongside `server_registry.register_server`); `mcp/src/agents_remember/cli/role_launch_confirmation.py` (`confirm_seat_binding` calls `live_server_bindings` and `harness_root_pids`); `mcp/tests/paseo_launch_test_support.py` (`FakeRuntime._record_fake_binding` writes synthetic records).
- **Dependencies:** `agents_remember.kernel.atomic_write.atomic_write_text`, `agents_remember.kernel.primitives.runtime_config.McpRuntimeConfig`.
- **Documentation and tests:** Documented in `docs/reference/runtime-layout.md` (`Server binding records`); tested by `mcp/tests/test_server_bindings.py` and `mcp/tests/test_launch_identity_confirmation.py`.

## Evidence

- Strict Pydantic models define per-PID binding, ancestry, and `bound`, `unbound`, and `unreadable` states. [1]
- Procfs stat parsing handles spaces and parentheses in `comm`, caps ancestry at 8 with a cycle guard, and falls back to `os.getppid()` when `/proc` is absent. [2]
- Registration atomically writes `runtime/server-bindings/<pid>.json`, logs write errors once via `_BindingWarnings`, and returns an idempotent `atexit` cleanup callback. [3]
- Live-record reading checks PID liveness plus `processStart` equality, reclaiming dead or recycled records while leaving unparseable files intact. [4]

- Harness root discovery matches exact NUL-delimited `PASEO_AGENT_ID=<agent_id>`, excludes `agents_remember.mcp` processes, and filters to non-descendant roots or `None` when `/proc` is unavailable. [5]
