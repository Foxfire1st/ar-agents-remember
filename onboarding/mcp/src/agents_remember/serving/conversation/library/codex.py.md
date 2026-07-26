# mcp/src/agents_remember/serving/conversation/library/codex.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/codex.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:34 |
| lastVerifiedCommitHash |  `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f`|
| lastVerifiedCommitDate |  2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The dormant Codex library port: DIRECT read-only list/read/resolve over one short-lived
`codex app-server` stdio connection per operation — no Node helper, no local catalog or index —
plus the live gate probe that reports the installed CLI version. The list
also surfaces harness sub-agent conversations: a second probed `thread/list` over the sub-agent
source kinds groups agent threads under their parent's top-level row as
`ConversationLibraryAgentRow` children.

## Code Commentary

### Logic

`_AppServer` resolves the installed harness executable, starts the existing
`CodexStdioTransport`, performs the initialize handshake (validated client name/version), and
exposes `thread/list` (parameterized source kinds: `_SOURCE_KINDS` for top-level conversations,
`_AGENT_SOURCE_KINDS` for the sub-agent fetch) and `thread/read`.
`CodexConversationLibrary.list` verifies the signed list cursor (scope, generation), fetches one
sub-agent page first (`_agent_page`, capped at `_AGENT_LIST_LIMIT` = 100), recomputes the catalog
generation from a newest-100 top-level id probe PLUS the sub-agent ids and the `agents_note`
text (so agent churn resets stale cursors too), resets stale cursors as
`CatalogGenerationError`, and mints rows whose conversation keys bind scope, vendor id, identity
digest, and generation. `_agent_row` keys each agent row by its `parentThreadId` and `_row`
groups matching agents under the parent row on the same page; an agent whose parent pages
outside the window appears on its parent's own page. Sub-agent identity is evidence-bound:
row-level `agentNickname`/`agentRole` win, then the `source.subAgent.thread_spawn` spawn record,
then the honest `agent <short-id>` fallback. `read` verifies the read cursor (ordinal above the
first item), normalizes the thread through `codex_normalize` (agent threads read through the
same path — their conversation key carries the agent thread id), derives the generation from
item count plus `updatedAt`, and returns the newest window with an honest `totalItems` and
older-page cursor. `resolve_resume_target` proves readability, then mints a server-private
target carrying `{"kind": "codex-thread-resume", "threadId": ...}` for the landed opener
channel. `probe_app_server_version` is the gate probe: connect, prove list, return the observed
CLI version.

### Conventions

Constructed per request with the caller's server-resolved authorization binding so every minted
cursor/key re-binds that exact principal/tenant; the port itself never authorizes. Historical
tool/command completeness is honestly `partial` (Codex does not persist every tool
interaction), and unmapped vendor kinds become explicit `unknown-vendor` evidence items rather
than guessed semantics. The `_AGENT_SOURCE_KINDS` vocabulary (`subAgent`, `subAgentReview`,
`subAgentCompact`, `subAgentThreadSpawn`, `subAgentOther`) is PROVEN, not guessed: the vendored codex main `ThreadSourceKind` enum and a live probe of the
installed codex 0.145.0 app-server (2026-07-26) agree, and the server's own -32600 error names
exactly these variants. The vendor `parentThreadId`/`ancestorThreadId` list filters are
experimental-gated on 0.145.0, so parent grouping is client-side over the `parentThreadId`
every thread/list row carries.

### Invariants And Boundaries

- Nothing here resumes, forks, or mutates a thread; the native app-server remains the one
  list/read authority on every call.
- Shape-skewed payloads and range-absurd but type-valid timestamps fail as typed
  `LibraryStoreError` (review F3/F4), never raw 500s; `thread/read` RPC method-absence maps to
  `LibraryStoreError`, other RPC errors to `UnknownNativeConversationError`.
- Sub-agent fetch degrades, never kills the listing: a native RPC refusal of
  the sub-agent `thread/list` (e.g. an app-server predating the sub-agent source kinds)
  propagates as `CodexAppServerRpcError` from `thread_list_agents` and becomes an exact
  `agents_note` ("sub-agent conversations are unavailable on this Codex install: ...") on the
  page; transport-level failures still fail closed as `LibraryStoreError`.
- Sub-agent visibility is honest, never silently absent: a continuation cursor on the agent
  page names the truncation (`_AGENT_LIST_LIMIT` fetch cap), and a nested agent whose parent is
  ITSELF an agent thread (depth ≥ 2) is counted and named in `agents_note` rather than dropped
  (fix-round review finding 7).
- A sub-agent row without a textual `parentThreadId` is not groupable and fails closed through
  shape validation; agent identity text comes only from native evidence
  (`agentNickname`/`agentRole`/`source.subAgent.thread_spawn`), never fabricated.
- The read generation is a content fingerprint of the observed thread; the documented
  newest-100 list probe bounds deep-mutation detection honestly. The list generation signature
  now also binds the sub-agent ids and the `agents_note` text, so agent churn resets stale list
  cursors exactly like top-level churn.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this internal port.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The ports suite proves rows/keys/cursors, generation resets, windows, shape-skew and
range-absurd failures, and exact resume targets on fake transports; the dedicated agents suite
proves sub-agent grouping, degrade/truncation/nested notes, and
fail-closed ungroupable rows on fake native boundaries; the installed suite re-proves the
list/read/resolve round-trip against the real app-server; the substrate supplies the validated
initialize/state helpers.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Codex list maps rows/keys/next-cursor, generation mismatch resets, reads window by ordinal, and resolve mints the exact codex-thread-resume target. | L227-L460 | [test_conversation_library_ports.py](agents-remember/mcp/tests/test_conversation_library_ports.py) |
| Shape-skewed list/read payloads and range-absurd timestamps fail as typed store errors. | L297-L387; L504-L518 | [test_conversation_library_ports.py](agents-remember/mcp/tests/test_conversation_library_ports.py) |
| Sub-agent grouping with probed source kinds, agent-thread read, RPC-refusal degrade note, truncation note, nested depth-2 naming, and ungroupable-row fail-closed. | L257-L474 | [test_conversation_library_agents.py](agents-remember/mcp/tests/test_conversation_library_agents.py) |
| The installed suite proves the live gate and list/read/resolve round-trip on the real installed app-server (0.145.0 at the probe; earlier passes observed 0.144.5). | L134-L186 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |
| The substrate state validators this port reuses for initialize, epoch timestamps, and required object/text/list shape checks. | L127-L155; L527-L542; L551-L572 | [codex_app_server_state.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_state.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local port.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-26T15:34 — 260718-CHATS-L7: sub-agent grouping — the port now fetches one probed
  sub-agent thread page (`_AGENT_SOURCE_KINDS`, capped at 100), groups agent rows under their
  parent's top-level row via `parentThreadId`, folds agent ids plus `agents_note` into the
  catalog generation, and carries `agents_note` on the page; RPC refusals degrade to an exact
  note, truncation and nested depth-2 agents are named, ungroupable rows fail closed. Sidecar:
  corrected the now-false "top-level source kinds only; sub-agent threads belong to their
  parent's history" claim, rewrote Purpose/Logic/Conventions/Invariants, refreshed ports-suite
  citation ranges (+7 shift from the L7 fake-transport addition), fixed the stale
  codex_app_server_state.py validator range, added the new test_conversation_library_agents.py
  suite, and reworded the installed-suite version claim. Change uncommitted; verification
  hash/date intentionally unchanged.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the direct Codex app-server port
  sidecar. Verification is blank until closeout commits and stamps the new source.
