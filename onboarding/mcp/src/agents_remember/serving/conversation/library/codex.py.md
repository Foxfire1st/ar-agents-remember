# mcp/src/agents_remember/serving/conversation/library/codex.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this internal port.

No configured domain documentation was available.

### Repo-Internal References

The ports suite proves rows/keys/cursors, generation resets, windows, shape-skew and
range-absurd failures, and exact resume targets on fake transports; the dedicated agents suite
proves sub-agent grouping, degrade/truncation/nested notes, and
fail-closed ungroupable rows on fake native boundaries; the installed suite re-proves the
list/read/resolve round-trip against the real app-server; the substrate supplies the validated
initialize/state helpers.

- The library owner maps native lists and reads, verifies cursors, and mints resume targets after exact identity checks. [1]
- Native Codex payload shape failures become typed library-store errors rather than fabricated history. [2]
- Native agent rows require their actual parent and grouping evidence; no unproven agent identity is fabricated. [3]
Historical evidence (retired with the d3610903 suite reduction): The installed suite historically exercised the live gate and list/read/resolve round-trip on the real installed app-server (0.145.0 at the probe; earlier passes observed 0.144.5). These removed artifacts provide no current execution or capability-enablement proof.
- The substrate state validators this port reuses for initialize, epoch timestamps, and required object/text/list shape checks. [4]

### Cross-Repo References

No meaningful cross-repo boundary exists for this local port.

No meaningful cross-repo references found.

## 260731-EFA-L2 Current Delta

**`AppServerSeams`** (`env`, `transport_factory`, defaulting to `os.environ` and
`CodexStdioTransport`; module default `DEFAULT_APP_SERVER_SEAMS`) is now how a codex app-server
subprocess is reached, as one substitutable value. The environment selects the binary and its
credentials; the transport factory decides how the process is spoken to. A fake transport against
the real environment (or the reverse) talks to a process nobody meant to start, so **both are
replaced as one seam**.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
