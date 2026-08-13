# mcp/src/agents_remember/serving/conversation/library/codex.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/codex.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T04:15+02:00 |
| lastVerifiedCommitHash |  `1580f92715ff93c988f9a15439ad9bec60ef4c5d`|
| lastVerifiedCommitDate |  2026-08-13T00:18:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The dormant Codex library port: DIRECT read-only list/read/resolve over one short-lived
`codex app-server` stdio connection per operation — no Node helper, no local catalog or index —
plus the live gate probe that reports the installed Codex runtime version. The list
also surfaces harness sub-agent conversations: a second probed `thread/list` over the sub-agent
source kinds groups agent threads under their parent's top-level row as
`ConversationLibraryAgentRow` children.

## Code Commentary

### Logic

`_AppServer` resolves the installed harness executable, starts the existing
`CodexStdioTransport`, performs the initialize handshake (current Desktop product plus the exact
client name/version sent on the request), and
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
- The library connection passes its owned `_CLIENT_NAME` and `_CLIENT_VERSION` into the shared
  validator; it cannot accept a Desktop response addressed to another initialize client.
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The ports suite proves rows/keys/cursors, generation resets, windows, shape-skew and
range-absurd failures, and exact resume targets on fake transports; the dedicated agents suite
proves sub-agent grouping, degrade/truncation/nested notes, and
fail-closed ungroupable rows on fake native boundaries; the installed suite re-proves the
list/read/resolve round-trip against the real app-server; the substrate supplies the validated
initialize/state helpers.

| Finding | Anchor | Source |
| --- | --- | --- |
| Codex list maps rows/keys/next-cursor, generation mismatch resets, reads window by ordinal, and resolve mints the exact codex-thread-resume target. | `test_list_maps_rows_keys_and_next_cursor`, `test_list_generation_mismatch_resets_cursor`, `test_read_normalizes_items_with_ordinals_and_window`, `test_resolve_mints_exact_resume_target` | mcp/tests/test_conversation_library_ports.py:266-283; mcp/tests/test_conversation_library_ports.py:285-299; mcp/tests/test_conversation_library_ports.py:301-334; mcp/tests/test_conversation_library_ports.py:427-447 |
| Shape-skewed list/read payloads and range-absurd timestamps fail as typed store errors. | `test_shape_skewed_list_payloads_fail_as_store_errors`, `test_shape_skewed_read_payloads_fail_as_store_errors`, `test_range_absurd_timestamp_fails_as_store_error` | mcp/tests/test_conversation_library_ports.py:336-388; mcp/tests/test_conversation_library_ports.py:390-425; mcp/tests/test_conversation_library_ports.py:543-556 |
| Sub-agent grouping with probed source kinds, agent-thread read, RPC-refusal degrade note, truncation note, nested depth-2 naming, and ungroupable-row fail-closed. | `test_agents_group_under_parent_with_probed_source_kinds`, `test_agent_conversation_reads_native_agent_thread`, `test_unproven_agent_kinds_degrade_to_exact_note`, `test_truncated_agent_listing_is_visible`, `test_nested_depth2_agents_are_named_not_silently_absent`, `test_ungroupable_agent_row_fails_closed` | mcp/tests/test_conversation_library_agents.py:302-340; mcp/tests/test_conversation_library_agents.py:350-369; mcp/tests/test_conversation_library_agents.py:371-384; mcp/tests/test_conversation_library_agents.py:386-392; mcp/tests/test_conversation_library_agents.py:394-424; mcp/tests/test_conversation_library_agents.py:426-434 |
| The installed suite proves the live gate and list/read/resolve round-trip on the real installed app-server (0.145.0 at the probe; earlier passes observed 0.144.5). | `test_live_gate_supports_list_read_and_partial_completeness`, `test_live_list_read_and_resolve_round_trip` | mcp/tests/test_conversation_library_installed.py:136-153; mcp/tests/test_conversation_library_installed.py:155-176 |
| The substrate state validators this port reuses for initialize, epoch timestamps, and required object/text/list shape checks. | `validate_initialize_response`, `iso_from_epoch`, `required_object`, `required_text`, `required_list` | mcp/src/agents_remember/serving/codex_app_server_state.py:132-162; mcp/src/agents_remember/serving/codex_app_server_state.py:561-566; mcp/src/agents_remember/serving/codex_app_server_state.py:585-588; mcp/src/agents_remember/serving/codex_app_server_state.py:595-599; mcp/src/agents_remember/serving/codex_app_server_state.py:602-606 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local port.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

**`AppServerSeams`** (`env`, `transport_factory`, defaulting to `os.environ` and
`CodexStdioTransport`; module default `DEFAULT_APP_SERVER_SEAMS`) is now how a codex app-server
subprocess is reached, as one substitutable value. The environment selects the binary and its
credentials; the transport factory decides how the process is spoken to. A fake transport against
the real environment (or the reverse) talks to a process nobody meant to start, so **both are
replaced as one seam**.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T04:15+02:00 — 260731-EFA-L22 Codex Desktop repair: passed the library connector's
  already-owned client version into strict initialize validation and documented the clean-cut
  Desktop host-first identity contract.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 10 initial citation findings (5 anchor, 0 prose, 5 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file citation. The sub-agent
  row had slid off the codex class and across the module-level `CLAUDE_AGENT_LIST` fixture into
  the claude suite; it was retargeted to `CodexLibraryAgentTests`, which still holds the six named
  cases: `test_agents_group_under_parent_with_probed_source_kinds`,
  `test_agent_conversation_reads_native_agent_thread`,
  `test_unproven_agent_kinds_degrade_to_exact_note`, `test_truncated_agent_listing_is_visible`,
  `test_nested_depth2_agents_are_named_not_silently_absent`, and
  `test_ungroupable_agent_row_fails_closed`.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `AppServerSeams` / `DEFAULT_APP_SERVER_SEAMS` as the single env+transport substitution.
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
