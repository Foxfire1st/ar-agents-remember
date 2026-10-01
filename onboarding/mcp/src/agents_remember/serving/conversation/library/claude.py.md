# mcp/src/agents_remember/serving/conversation/library/claude.py

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The dormant Claude library port: helper-backed list/read/resolve through the repository-owned
locked helper (`@anthropic-ai/claude-agent-sdk` `listSessions` / `getSessionMessages` /
`getSessionInfo`). The helper handshake on every spawn reports the
observed runtime/helper versions as informational evidence ONLY — the contract is the only gate:
the native `list`/`read` operation succeeding is the proof, and a version drift never demotes the
surface (the old locked-version re-prove is gone). List rows also carry
sub-agent children (`ConversationLibraryAgentRow`): the locked helper sweeps each session's
on-disk `subagents/agent-<agentId>.jsonl` transcripts plus `.meta.json` identity, and agent
conversations open through the library's own composite vendor id `<sessionId>/<agentId>`.

## Code Commentary

### Logic

`ClaudeConversationLibrary.list` verifies the signed list cursor, calls the helper's `list`,
derives the catalog generation from the helper's store signature (resetting stale cursors as
`CatalogGenerationError` — the helper's signature sweep covers agents too), and mints rows
keyed by session id with title preference `customTitle`/`summary`/`firstPrompt` and an optional
millisecond-epoch `lastModified`. Each row's helper-supplied `agents` list becomes
`ConversationLibraryAgentRow` children (`_agent_row`): identity comes only from the native
`.meta.json` (`description`/`agentType`/`model`, `toolUseId` as `join_key` to the spawning tool
call), with the honest `agent <short-id>` fallback when the meta carries no title evidence.
`_rows` also computes the page-level `agents_note`: a helper that predates sub-agent
enumeration (no response-level `agentsEnumerated: true` marker, or any row missing the
`agents` key) degrades to the visible unavailability note, and nested agents with
`spawnDepth > 1` are counted and named (they stay listed flat under the top-level session).
`read` verifies the read cursor, splits the composite vendor id (`_split_agent_vendor_id`), and
routes an `agentId` through the helper so the locked helper reads
`subagents/agent-<agentId>.jsonl`; record mapping is unchanged: user items (unknown-input lane;
all-tool-result content becomes a correlated tool-result item), assistant items
(text/thinking/tool_use/tool_result/image blocks), and anything else as system notices —
unknown content blocks become explicit `unknown-vendor` evidence. `resolve_resume_target`
fails closed with an exact reason for agent conversations (sub-agent transcripts have no
native resume target); for top-level sessions it re-proves identity through
the helper and mints the server-private argv target `--resume <sessionId>`.

### Conventions

Constructed per request with the caller's server-resolved authorization binding; the port never
authorizes. Claude history is honestly `partial`: the SDK rebuilds chronological
user/assistant chains, and thinking/tool/permission records appear only where the installed
history persists them. The composite agent vendor id grammar `<sessionId>/<agentId>`
(`_AGENT_ID_SEPARATOR = "/"`) is minted ONLY by this port — session ids and agent ids never
contain "/" — so the split in `read`/`resolve_resume_target` is unambiguous. Agent identity is meta-bound: `description` wins over `agentType` for the
title, and a missing title is never fabricated.

### Invariants And Boundaries

- Helper-reported invalid pages, missing fields, non-text cursors, and identity mismatches fail
  closed as `LibraryStoreError`/`InvalidLibraryCursorError`; helper `stale-identity` surfaces
  through the host as `StaleNativeIdentityError`.
- Sub-agent capability honesty: a helper without sub-agent enumeration proof
  is VISIBLY unavailable through `agents_note`, never silently absent. The response-level
  `agentsEnumerated` marker covers the empty catalog too (fix-round review finding 11) — over
  zero rows only the marker proves the helper enumerates agents. Nested `spawnDepth > 1` agents
  are shown flat under the top-level session AND named in the note (fix-round review finding
  7); the flat per-session grouping never pretends to model agent-of-agent parenting.
- A row whose `agents` key is present but not a list, and an agent row without `agentId`,
  fail closed as `LibraryStoreError`.
- Claude sub-agent transcripts have no native resume target: `resolve_resume_target` on a
  composite agent id fails closed with the exact reason instead of minting an argv that would
  resume the parent session under a false identity.
- Range-absurd but type-valid `lastModified` values fail as typed `LibraryStoreError` with an
  exact out-of-range reason (review F4), never raw 500s.
- Unknown content blocks (including images) are explicit evidence with safe summaries, never
  guessed renderings.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this internal port.

No configured domain documentation was available.

### Repo-Internal References

The ports suite proves rows/paging, block/role/provenance mapping, range-absurd timestamp
failures, and exact argv resume targets on fake helpers; the dedicated agents suite proves
sub-agent grouping, capability-honesty notes, agent reads, and the resume fail-closed on fake
helper boundaries; the installed suite proves the library gates on CONTRACT, not version; the
locked helper implements the native seam, including the on-disk `subagents/` enumeration.

- The Claude library owns helper-backed list/read and exact native resume-target construction. [1]
- Out-of-range native timestamps raise LibraryStoreError even when their value has an integer type. [2]
- Claude sub-agent rows derive identity and title from native helper metadata. [3]
Historical evidence (retired with the d3610903 suite reduction): The installed suite historically exercised the Claude library gates on contract, not version — a runtime drift still enables when the native operation probe passes. These removed artifacts provide no current execution or capability-enablement proof.
- The locked helper defines the session-listing call. [4]
- The locked helper defines the session-messages call. [5]
- The locked helper defines the session-info call. [6]
- The locked helper enumerates sub-agent transcripts and their metadata. [7]
- The locked helper reads sub-agent transcripts through the on-disk authority. [8]

### Cross-Repo References

No meaningful cross-repo boundary exists for this local port.

No meaningful cross-repo references found.
