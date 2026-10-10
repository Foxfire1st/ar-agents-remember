# mcp/src/agents_remember/models/context_packet.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`context_packet.py` defines `ContextPacketV2`, the compact startup/bootstrap response contract for `context_packet`.

## Code Commentary

The model separates repository Git facts, resolved paths, memory/storage facts, worktree summary, provider summary, and drift summary into explicit nested objects. `ContextPacketV2` fixes `contextPacketVersion` to `2` and carries a diagnostics hint pointing agents at `provider_diagnostics` for raw provider details.

**Vocabularies this packet does not produce are imported, never retyped** — the same rule the gate/lifecycle/inbox/orchestration models follow. `RepoSummary.state` is `RepoState` from `kernel.git_facts`, `BranchFreshness.state` is `FreshnessState` from `kernel.git_freshness`, and `MemorySummary.mode` is `ReadableMemoryMode` from `kernel.memory_mode`: `external` for every started task, still reading the legacy `disabled` a contract on disk may carry, exactly as `WorktreeSummary.memoryMode` in the same response does. A local copy is only ever measured against the producer when a real payload carries the new member — as a `ValidationError`, inside a tool handler with no `except` for one.

The same value must mean the same thing on every field of one response: `memory.mode` and `worktree.memoryMode` share the readable declaration, so they cannot disagree about a legacy mode again.

`FreshnessSummary` is the opt-in branch-freshness section: `status` is `checked`/`not-checked`, with optional `BranchFreshness` blocks for the code and memory repos. `ContextPacketV2.worktree` is a `WorktreeSummary`, constructed directly by `application.worktree_status.worktree_status_packet`, not validated from a dict. `ContextPacketV2.drift` is `DriftSummary`, which carries an `error` field so `include_drift=true` against a repo with no onboarding root reports why instead of raising.

## Evidence

- Packet vocabularies imported from producers [7]
- Memory mode is the shared readable alias [8]
- Mode field reads legacy `disabled` as-is [9]
- Startup/bootstrap response contract [10]
