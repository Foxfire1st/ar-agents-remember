# mcp/native_helpers/conversation_library/src/pi.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/native_helpers/conversation_library/src/pi.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Locked native conversation-library helper overview](../overview.md)

## Purpose

The locked Pi helper entry: implements handshake, list, read, and resolve-resume-target over
the pinned `@earendil-works/pi-coding-agent@0.80.7` `SessionManager` on one JSON-lines loop,
reading session files read-only without ever calling `switch_session` on any running process.

## Code Commentary

### Logic

`handlePi` dispatches validated requests: handshake probes the installed `pi --version` and the
helper's own locked dependency version. List calls `SessionManager.list(canonicalProjectScope)`,
sorts by `modified` descending, offset-pages, and returns a SHA-256 store signature over
id:modified pairs with the session file path carried per row. Read resolves the session file by
native id (`findSessionFile`; absent → typed `stale-identity`), opens it read-only through
`SessionManager.open`, walks the current branch via `getBranch` (empty → `stale-identity`),
windows by ordinal, and maps each entry to a typed record preserving the durable entry id,
parentId, type, timestamp, and per-type detail (message/custom/compaction/branch_summary/
thinking_level_change/model_change/session_info/label). Resolve returns the native identity
plus the session file path and header cwd for the Python port's `--session` argv target.

### Conventions

All paging, signing, error, and serve-loop behavior comes from `./protocol.js`; this entry only
maps `SessionManager` results to protocol payloads. `toISOString` conversions happen here, so a
date failure becomes `helper-failed` → typed `LibraryStoreError` on the Python side and the
Python port never parses timestamps numerically.

### Invariants And Boundaries

- Session files are opened read-only for reads/resolution; no entry is appended, branched, or
  mutated by this helper.
- The durable Pi entry id is the identity anchor forwarded to the Python normalizer; records
  without it fail closed there.
- Native absence is typed `stale-identity`, never a synthetic empty page.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the pinned manifest/lock and the local tests are
the direct contract evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The protocol module owns the serve loop, handshake, paging, and error vocabulary this entry
consumes; the Python Pi port drives it on the production seam; the installed suite proves the
live gate and the real open.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The JSONL serve loop, handshake builder, offset/ordinal paging, signature, and typed error helpers consumed here. | L102-L259 | [protocol.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.ts) |
| The Python Pi port calls list/read/resolve-resume-target through the locked helper host. | L88-L182 | [pi.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/pi.py) |
| The installed suite proves the live Pi gate, the list/read/resolve round-trip, and the real end-to-end open through this helper. | L215-L262; L360-L479 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

## Cross-Repo References

The installed `@earendil-works/pi-coding-agent` npm dependency is a third-party library
resolved only from this repository's package/lock; no neighboring workspace repository
participates.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the locked Pi helper entry
  sidecar. Verification is blank until closeout commits and stamps the new source.
