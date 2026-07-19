# mcp/src/agents_remember/serving/conversation/library/claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The dormant Claude library port: helper-backed list/read/resolve through the repository-owned
locked helper (`@anthropic-ai/claude-agent-sdk@0.3.207` `listSessions` / `getSessionMessages` /
`getSessionInfo`), with the version handshake re-proving locked runtime/helper versions on
every spawn.

## Code Commentary

### Logic

`ClaudeConversationLibrary.list` verifies the signed list cursor, calls the helper's `list`,
derives the catalog generation from the helper's store signature (resetting stale cursors as
`CatalogGenerationError`), and mints rows keyed by session id with title preference
`customTitle`/`summary`/`firstPrompt` and an optional millisecond-epoch `lastModified`.
`read` verifies the read cursor, calls the helper's `read`, and maps records: user items
(unknown-input lane; all-tool-result content becomes a correlated tool-result item), assistant
items (text/thinking/tool_use/tool_result/image blocks), and anything else as system notices —
unknown content blocks become explicit `unknown-vendor` evidence. `resolve_resume_target`
re-proves identity through the helper and mints the server-private argv target
`--resume <sessionId>`.

### Conventions

Constructed per request with the caller's server-resolved authorization binding; the port never
authorizes. Claude history is honestly `partial`: the SDK rebuilds chronological
user/assistant chains, and thinking/tool/permission records appear only where the installed
history persists them.

### Invariants And Boundaries

- Helper-reported invalid pages, missing fields, non-text cursors, and identity mismatches fail
  closed as `LibraryStoreError`/`InvalidLibraryCursorError`; helper `stale-identity` surfaces
  through the host as `StaleNativeIdentityError`.
- Range-absurd but type-valid `lastModified` values fail as typed `LibraryStoreError` with an
  exact out-of-range reason (review F4), never raw 500s.
- Unknown content blocks (including images) are explicit evidence with safe summaries, never
  guessed renderings.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this internal port.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The ports suite proves rows/paging, block/role/provenance mapping, range-absurd timestamp
failures, and exact argv resume targets on fake helpers; the installed suite proves the
version-mismatch fail-closed posture on the real machine; the locked helper implements the
native seam.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Claude list rows and paging, read block/role/provenance mapping, and argv resume minting on fake helper boundaries. | L472-L567 | [test_conversation_library_ports.py](agents-remember/mcp/tests/test_conversation_library_ports.py) |
| A range-absurd but type-valid `lastModified` fails as a typed store error. | L497-L511 | [test_conversation_library_ports.py](agents-remember/mcp/tests/test_conversation_library_ports.py) |
| Installed Claude 2.1.214 vs locked 2.1.211 fails closed and visible on the real helper seam. | L540-L568 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |
| The locked helper's scope-exact listSessions/getSessionMessages/getSessionInfo implementations. | L65-L169 | [claude.ts](agents-remember/mcp/native_helpers/conversation_library/src/claude.ts) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local port.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the helper-backed Claude port
  sidecar. Verification is blank until closeout commits and stamps the new source.
