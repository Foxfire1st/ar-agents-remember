# mcp/native_helpers/conversation_library/src/protocol.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/native_helpers/conversation_library/src/protocol.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Locked native conversation-library helper overview](../overview.md)

## Purpose

Defines the versioned JSON-lines contract and fail-closed admission/privacy shell shared by the
future Python host and repository-locked Claude/Pi native helpers.

## Code Commentary

### Logic

- Declares protocol, exact Claude/Pi helper versions, request-byte limit, operations, discriminated
  request/response types, and handshake result.
- `buildHandshake` returns ready only when requested and observed runtime/helper values match the
  selected repository pin.
- `parseHelperRequest` byte-bounds and parses one JSON object, validates protocol/request id/
  operation, then reconstructs the request from an exact operation-specific key set.
- Page operations require string-or-null cursors and positive safe-integer limits.
- `redactHelperError` intentionally ignores raw detail and returns one fixed allow-listed string.

### Conventions

All request operations are explicit discriminated unions. Exact-key lists and reconstructed return
objects are intentional protocol authority, not compatibility scaffolding.

### Invariants And Boundaries

- Never accept unknown or operation-inapplicable fields.
- Never promote a version mismatch to ready.
- Never expose raw helper error detail, regardless of its secret/path syntax.
- Never add ambient module resolution or operation behavior to this contract shell.
- The request-byte bound protects the helper process before JSON parsing.

### Todos

List/read/resume execution is intentionally absent until the production native-library leaf.

## Docs References

No Domain Documentation source is configured. Local manifest, lock, and tests are the direct
contract evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The private manifest and lock select the exact dependency versions represented by the protocol constants. | L1-L22 | [package.json](agents-remember/mcp/native_helpers/conversation_library/package.json) |
| Helper tests cover exact versions, malformed framing, wrong protocol, exact key sets, inapplicable fields, and hostile error details. | L14-L210 | [protocol.test.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.test.ts) |
| Python foundation tests forbid incidental resolution in production helper source. | L80-L99 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No neighboring workspace repository participates in the helper process boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the JSONL protocol/privacy sidecar
  after same-reviewer PASS closed raw-error and exact-shape findings. Verification is blank until
  closeout commits and stamps the new source.
