# mcp/src/agents_remember/models/context_packet.py

## Governing Overview

[overview.md](overview.md)

## Current source contract evidence

- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance. [17]

## Purpose

`context_packet.py` defines the mounted `SlimContextPacket` v3 naming/orientation answer and retains `ContextPacketV2` as the whole-result contract. The slim answer holds roots, optional task/master, needed action lines, serving build and pair commits; it does not carry V2 provider/settings/freshness blocks.

## Code Commentary

The V2 nested-object account below describes the retained whole result, not what leaves the mounted tool. `SlimRoots` names code/memory/enclosure/rendered task document; `SlimTask` names ID/master; `SlimPair` names code/memory commits. `SlimContextPacket.contextPacketVersion` is 3. Optional absent facts stay omitted; its declaration does not itself measure the ordinary under-600-token requirement.

The model separates repository Git facts, resolved paths, memory/storage facts, worktree summary, provider summary, and drift summary into explicit nested objects. `ContextPacketV2` fixes `contextPacketVersion` to `2` and carries a diagnostics hint pointing agents at `provider_diagnostics` for raw provider details.

**Vocabularies this packet does not produce are imported, never retyped** — the same rule the gate/lifecycle/inbox/orchestration models follow. `RepoSummary.state` is `RepoState` from `kernel.git_facts`, `BranchFreshness.state` is `FreshnessState` from `kernel.git_freshness`, and `MemorySummary.mode` is `ReadableMemoryMode` from `kernel.memory_mode`: `external` for every started task, still reading the legacy `disabled` a contract on disk may carry, exactly as `WorktreeSummary.memoryMode` in the same response does. A local copy is only ever measured against the producer when a real payload carries the new member — as a `ValidationError`, inside a tool handler with no `except` for one.

The same value must mean the same thing on every field of one response: `memory.mode` and `worktree.memoryMode` share the readable declaration, so they cannot disagree about a legacy mode again.

`FreshnessSummary` is the opt-in branch-freshness section: `status` is `checked`/`not-checked`, with optional `BranchFreshness` blocks for the code and memory repos. `ContextPacketV2.worktree` is a `WorktreeSummary`, constructed directly by `application.worktree_status.worktree_status_packet`, not validated from a dict. `ContextPacketV2.drift` is `DriftSummary`, which carries an `error` field so `include_drift=true` against a repo with no onboarding root reports why instead of raising.

## Evidence

The V2 references below witness the retained rich model/producer, not the current mounted packet. Current answer evidence must also cite SlimContextPacket and the registry’s slim mapping; no executor or token measurement was run here.


- ContextPacketV2 carries the nested packet objects; RepoSummary, BranchFreshness and MemorySummary use vocabularies imported from the owning producers. [7]


- Memory mode is the shared readable alias [8]


- Mode field reads legacy `disabled` as-is [9]


- Startup/bootstrap response contract [10]


The following source-backed definitions and producer seams retain the broader response and vocabulary account alongside the readable-mode correction; they are declarations, not evidence of an executor run.

- The application constructs ContextPacketV2 from Git, resolved paths, memory, worktree, provider, drift and freshness facts. [11]
- Provider readiness in the packet uses compact provider summary models. [12]
- RepoState and VALID_REPO_STATES define the producer vocabulary; git_facts_to_packet supplies the dict RepoSummary validates. [13]
- FreshnessState and VALID_FRESHNESS_STATES define the producer vocabulary; freshness_to_packet supplies the freshness dict. [14]
- ReadableMemoryMode is external/disabled for persisted reads; the startable MemoryMode is external only. Packet memory.mode and worktree.memoryMode use the readable alias. [15]
- worktree_status_packet returns WorktreeSummary directly; the packet constructs its worktree block rather than validating a dict. [16]
