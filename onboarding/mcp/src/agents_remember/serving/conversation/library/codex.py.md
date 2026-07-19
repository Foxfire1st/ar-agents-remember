# mcp/src/agents_remember/serving/conversation/library/codex.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/codex.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The dormant Codex library port: DIRECT read-only list/read/resolve over one short-lived
`codex app-server` stdio connection per operation — no Node helper, no local catalog or index —
plus the live gate probe that reports the installed CLI version.

## Code Commentary

### Logic

`_AppServer` resolves the installed harness executable, starts the existing
`CodexStdioTransport`, performs the initialize handshake (validated client name/version), and
exposes `thread/list` (top-level source kinds only; sub-agent threads belong to their parent's
history) and `thread/read`. `CodexConversationLibrary.list` verifies the signed list cursor
(scope, generation), recomputes the catalog generation from a newest-100 id probe, resets stale
cursors as `CatalogGenerationError`, and mints rows whose conversation keys bind scope, vendor
id, identity digest, and generation. `read` verifies the read cursor (ordinal above the first
item), normalizes the thread through `codex_normalize`, derives the generation from item count
plus `updatedAt`, and returns the newest window with an honest `totalItems` and older-page
cursor. `resolve_resume_target` proves readability, then mints a server-private target carrying
`{"kind": "codex-thread-resume", "threadId": ...}` for the landed L0E opener channel.
`probe_app_server_version` is the gate probe: connect, prove list, return the observed CLI
version.

### Conventions

Constructed per request with the caller's server-resolved authorization binding so every minted
cursor/key re-binds that exact principal/tenant; the port itself never authorizes. Historical
tool/command completeness is honestly `partial` (Codex does not persist every tool
interaction), and unmapped vendor kinds become explicit `unknown-vendor` evidence items rather
than guessed semantics.

### Invariants And Boundaries

- Nothing here resumes, forks, or mutates a thread; the native app-server remains the one
  list/read authority on every call.
- Shape-skewed payloads and range-absurd but type-valid timestamps fail as typed
  `LibraryStoreError` (review F3/F4), never raw 500s; `thread/read` RPC method-absence maps to
  `LibraryStoreError`, other RPC errors to `UnknownNativeConversationError`.
- The read generation is a content fingerprint of the observed thread; the documented
  newest-100 list probe bounds deep-mutation detection honestly.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this internal port.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The ports suite proves rows/keys/cursors, generation resets, windows, shape-skew and
range-absurd failures, and exact resume targets on fake transports; the installed suite
re-proves the same against the real app-server; the substrate supplies the validated
initialize/state helpers.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Codex list maps rows/keys/next-cursor, generation mismatch resets, reads window by ordinal, and resolve mints the exact codex-thread-resume target. | L220-L407 | [test_conversation_library_ports.py](agents-remember/mcp/tests/test_conversation_library_ports.py) |
| Shape-skewed list/read payloads and range-absurd timestamps fail as typed store errors. | L290-L380; L497-L511 | [test_conversation_library_ports.py](agents-remember/mcp/tests/test_conversation_library_ports.py) |
| The installed suite proves the live gate and list/read/resolve round-trip on the real 0.144.5 app-server. | L134-L214 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |
| The substrate state validators this port reuses for initialize, rows, and timestamps. | L30-L36 | [codex_app_server_state.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_state.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local port.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the direct Codex app-server port
  sidecar. Verification is blank until closeout commits and stamps the new source.
