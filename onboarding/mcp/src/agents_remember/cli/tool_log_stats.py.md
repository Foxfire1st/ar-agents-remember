# mcp/src/agents_remember/cli/tool_log_stats.py

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

The read-only `tool-log-stats` command (MIK-R108 rule 8): per-tool/operation answer sizes — calls, median, p90, largest, sums and guard-cut rates — read from a log folder over a span of days.

## Code Commentary

### Logic

- `add_arguments` takes the log folder and the day span; `run` stays read-only and returns the process exit status.
- `collect_rows` walks the day's JSONL lines, skipping blank and malformed ones, and sizes each tool and operation from the log only.

### Invariants And Boundaries

- The command reads the log; it never writes, repairs or prunes it.
- Malformed lines are skipped, never fatal.

## Evidence

- Per-tool sizes are read from the log folder, skipping bad lines. [1]
- The command entry stays read-only and reports the exit status. [2]
