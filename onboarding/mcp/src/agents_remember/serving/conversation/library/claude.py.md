# mcp/src/agents_remember/serving/conversation/library/claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:34 |
| lastVerifiedCommitHash |  `b252c42cca200933d5c9c36e26de47a526a569ce`|
| lastVerifiedCommitDate |  2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this internal port.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The ports suite proves rows/paging, block/role/provenance mapping, range-absurd timestamp
failures, and exact argv resume targets on fake helpers; the dedicated agents suite proves
sub-agent grouping, capability-honesty notes, agent reads, and the resume fail-closed on fake
helper boundaries; the installed suite proves the library gates on CONTRACT, not version; the
locked helper implements the native seam, including the on-disk `subagents/` enumeration.

| Finding | Anchor | Source |
| --- | --- | --- |
| Claude list rows and paging, read block/role/provenance mapping, and argv resume minting on fake helper boundaries. | `ClaudeLibraryTests` | mcp/tests/test_conversation_library_ports.py:465-573 |
| A range-absurd but type-valid `lastModified` fails as a typed store error. | `ClaudeLibraryTests` | mcp/tests/test_conversation_library_ports.py:465-573 |
| Sub-agent grouping with meta identity, helper-without-evidence and empty-catalog unavailability notes, nested spawnDepth naming, agent read routing, agent resume fail-closed, and agent-row shape failures. | `ClaudeLibraryAgentTests` | mcp/tests/test_conversation_library_agents.py:471-648 |
| The installed suite proves the Claude library gates on contract, not version — a runtime drift still enables when the native operation probe passes. | `test_installed_claude_library_gates_on_contract_not_version` | mcp/tests/test_conversation_library_installed.py:591-617 |
| The locked helper defines the session-listing call. | "listSessions({" | mcp/native_helpers/conversation_library/src/claude.ts:83-83 |
| The locked helper defines the session-messages call. | "getSessionMessages(" | mcp/native_helpers/conversation_library/src/claude.ts:377-377 |
| The locked helper defines the session-info call. | "getSessionInfo(" | mcp/native_helpers/conversation_library/src/claude.ts:426-426 |
| The locked helper enumerates sub-agent transcripts and their metadata. | `listSubagents` | mcp/native_helpers/conversation_library/src/claude.ts:180-204 |
| The locked helper reads sub-agent transcripts through the on-disk authority. | `readClaudeAgentTranscript` | mcp/native_helpers/conversation_library/src/claude.ts:313-369 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local port.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-04T11:35:04+02:00 — 260731-EFA-L6 S18-B10 curator: source-first semantic citation curation; repaired this card's scoped citation findings with frozen-source evidence and corrected stale or pooled claims where needed.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/conversation/library/claude.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 7 line(s), touching only redundant
  grouping parentheses. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds. Noted while checking: the references table also
  cites line ranges inside `test_conversation_library_agents.py`,
  `test_conversation_library_installed.py`, `test_conversation_library_ports.py`; those ranges
  shifted because this task edited those files, so treat the cited numbers as approximate and the
  linked cards as authoritative.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-26T15:34 — 260718-CHATS-L7: sub-agent grouping — list rows now carry
  `ConversationLibraryAgentRow` children from the locked helper's `subagents/*.jsonl` +
  `.meta.json` evidence; agent conversations open through the port's composite
  `<sessionId>/<agentId>` vendor id (read routes `agentId` to the helper;
  `resolve_resume_target` fails closed with an exact reason); a helper without enumeration
  proof degrades to a visible `agents_note` (`agentsEnumerated` marker covers the empty
  catalog), and nested `spawnDepth > 1` agents are named, never silently absent. Sidecar:
  rewrote Purpose/Logic/Conventions/Invariants, refreshed ports-suite citation ranges (+7 shift
  from the L7 fake-transport addition), re-anchored the claude.ts citations to the post-L7
  helper layout (listSessions moved to L80; new sub-agent section L135-L370), and added the new
  test_conversation_library_agents.py suite. Change uncommitted; verification hash/date
  intentionally unchanged.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R4 version-gate removal — corrected the now-false
  "version handshake re-proving locked runtime/helper versions on every spawn" claim. The helper
  handshake reports observed versions as informational evidence only; the contract (the succeeding
  `list`/`read` operation) is the only gate and a version drift never demotes the surface. Reworded
  the installed-suite reference from "2.1.214 vs locked 2.1.211 fails closed" to gates-on-contract.
  Change uncommitted; closeout re-stamps verification.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the helper-backed Claude port
  sidecar. Verification is blank until closeout commits and stamps the new source.
