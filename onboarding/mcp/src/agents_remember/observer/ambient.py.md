# mcp/src/agents_remember/observer/ambient.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Process-scoped worktree lifecycle attribution, retained event emission, activity heartbeat and the ambient registry. No session start/block/ask/promote/save-gate transition API remains.

## Code Commentary

attach adopts a contract lifecycle, is a same-id no-op, or pauses the previous owner before adoption, preserving per-process attribution. end checks the terminal vocabulary, emits the ending event, stops the ticker, forgets served state and clears current. Tool/read observation remains exception-contained and never attributes a lifecycle-less call to another owner; completed-answer token counts are passed explicitly. Mutation/emission uses the same lock. The ticker rechecks its stop deadline and falls quiet after inactivity. These retained lower-level functions do not restore model-facing lifecycle signal tools or notifier banner ownership.

`emit_read_packet` projects every per-file caller entry into the fixed facts-only allowlist `{path, lines, status, bytes}` before emission. It drops source/onboarding/overview content regardless of what the caller supplied; Event.data is flexible, so envelope extra-forbid is not the privacy enforcement. Packet repoId names the read repository separately from the lifecycle owner. Lifecycle-less reads are dropped and validation/I/O failures are contained so logging cannot break the recorded read. This retained observation is not a restored file-text MCP response or model signal.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.

## Source-bound reference inputs

- [1]
- [2]
- [3]
- [4]
- [7]

- emit_read_packet strips caller entry content by selecting only path/lines/status/bytes, drops lifecycle-less calls and contains emission failure. [12]
- [11]
