# mcp/src/agents_remember/serving/server_registry.py

## Governing Overview

[overview](overview.md)

## Purpose

Keeps one small record per running MCP server and dashboard process under the coordination root, so `runtime_install` and `server_info` can list the running servers and say which ones still run an old build.

## Code Commentary

- `register_server(config, role)` writes `<coordinationRoot>/runtime/servers/<pid>.json` atomically at boot: pid, role (`mcp` from `mcp/server.py::run_server`, `dashboard` from the serving lifespan), loaded Python digest, boot time, settings file, package root and the kernel's process start time. It returns an idempotent cleanup that removes the record and is also registered with `atexit`. A record that cannot be written is logged once per process and the server keeps running.
- `server_inventory(config)` reads every record. A record whose process is gone, or whose pid now belongs to a process with another start time, is removed and skipped; a record that cannot be parsed is skipped and left in place. A pid that exists under another user counts as alive.
- Each live record is reported as a `RunningServerPayload` with its `currentness`: the record's loaded digest compared with the Python files now at its package root (`build_currentness.inspect_build`), with the remedy for its role. The scan then lets `retain_live_builds` drop comparison state of boots that are gone.
- The inventory writes no inventory file and refuses nothing; refusal of a stale build's writes belongs to the MCP tool dispatcher. An unreadable records directory yields an empty list with a warning.

## Evidence

- The record fields and the records directory. [1]
- Liveness by signal probe plus the process start time. [2]
- The boot record, its one-time write warning and its exit cleanup. [3]
- Dead records are removed by the reader. [4]
- The inventory compares each live record's build and reclaims comparison state. [5]
- The MCP server registers itself for the life of `run_server`. [6]
- `server_info` and `runtime_install` list the running servers. [7]
