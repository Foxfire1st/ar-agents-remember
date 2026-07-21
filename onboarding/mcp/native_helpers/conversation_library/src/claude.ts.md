# mcp/native_helpers/conversation_library/src/claude.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/native_helpers/conversation_library/src/claude.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Locked native conversation-library helper overview](../overview.md)

## Purpose

The locked Claude helper entry: implements handshake, list, read, and resolve-resume-target
over the pinned `@anthropic-ai/claude-agent-sdk@0.3.207` on one JSON-lines loop, so the Python
host can serve the dormant Claude library without ever discovering modules outside this
repository package.

## Code Commentary

### Logic

`handleClaude` dispatches validated requests: handshake probes the installed `claude
--version` and the helper's own locked dependency version, then builds the ready/incompatible
verdict. List calls `listSessions({dir: canonicalProjectScope, includeWorktrees: false})` —
scope-exact, never widening a caller's authorized scope to another checkout's history — sorts
by `lastModified` descending, offset-pages, and returns a SHA-256 store signature over
sessionId:lastModified pairs. Read calls `getSessionMessages` in the exact scope (unreadable or
empty → typed `stale-identity`), windows by ordinal with stable 1-based positions, and maps
each message to a typed record (uuid, parentToolUseId, parentAgentId, role, content, optional
timestamp) plus an honest `totalItems`. Resolve calls `getSessionInfo` and returns the native
identity (absent → `stale-identity`) for the Python port's argv resume target.

### Conventions

All paging, signing, error, and serve-loop behavior comes from `./protocol.js`; this entry only
maps SDK results to protocol payloads. Optional session fields are copied explicitly when
defined, so unknown or inapplicable fields never cross the helper seam.

### Invariants And Boundaries

- Worktree sessions belong to their own canonical scope (`includeWorktrees: false`).
- Native absence/unreadability is typed `stale-identity`, never a synthetic empty page.
- Raw SDK errors never cross the boundary: they become the protocol's typed vocabulary with
  allow-listed detail only.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the pinned SDK manifest/lock and the local tests
are the direct contract evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The protocol module owns the serve loop, handshake, paging, and error vocabulary this entry
consumes; the Python port and host drive it on the production seam; the installed suite proves the
library gates on the live CONTRACT probe, not a version comparison (260718-CHATS-L5F R4 made
`buildHandshake` ready-by-contract, so this entry's handshake no longer fails closed on a version
drift — the observed versions are informational and the `list`/`read` operation is the gate).

| Finding | Citations | Source Path |
| --- | --- | --- |
| The JSONL serve loop, handshake builder, offset/ordinal paging, signature, and typed error helpers consumed here. | L102-L259 | [protocol.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.ts) |
| The Python Claude port calls list/read/resolve-resume-target through the locked helper host. | L87-L182 | [claude.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/claude.py) |
| The installed suite gates Claude on the live helper contract probe, not a version comparison (L5F R4); the observed runtime/helper version rides evidence informationally. | L540-L568 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

## Cross-Repo References

The installed `@anthropic-ai/claude-agent-sdk` npm dependency is a third-party library resolved
only from this repository's package/lock; no neighboring workspace repository participates.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: reference-health correction only (claude.ts
  source unchanged this leaf). The R4 change to `protocol.ts::buildHandshake` (ready-by-contract, no
  version comparison — developer ruling 2026-07-21) made this entry's cited "installed 2.1.214 vs
  locked 2.1.211 fails closed through the handshake" claim FALSE; corrected the Repo-Internal summary
  and row to the contract-only gate. Verification stamp unchanged (source not modified).
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the locked Claude helper entry
  sidecar. Verification is blank until closeout commits and stamps the new source.
