# mcp/native_helpers/conversation_library/src/protocol.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/native_helpers/conversation_library/src/protocol.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Locked native conversation-library helper overview](../overview.md)

## Purpose

Pins the helper's ready-by-contract handshake, framing, operation-schema, and raw-error privacy
boundaries with deterministic Node tests.

## Code Commentary

### Logic

The tests verify exact Claude/Pi protocol constants, the handshake tuple carrying the observed
versions, malformed-shape rejection, unknown fields across every operation, known-but-inapplicable
field rejection, and one fixed safe output across bearer, JSON credential, environment secret,
POSIX/Windows path, and long-input examples. Since 260718-CHATS-L5F (R4)
`handshake reports observed versions and is ready by contract, never version-gated` pins the removal
of the version gate: `buildHandshake` always returns `status: "ready"` and reports the runtime/helper
versions as informational only — a version difference no longer yields `incompatible`; the
list/read OPERATION result is the gate. The former wrong-version rejection is gone (malformed-shape
rejection remains).

### Conventions

Negative cases are table-driven across sibling operations and credential shapes so a narrow happy
path cannot make a broader privacy/schema claim.

### Invariants And Boundaries

- Test each operation's exact accepted shape before adding fields.
- Privacy tests assert the unsafe value itself never survives, not merely that one regex ran.
- The handshake is ready-by-contract: a version difference is reported as informational metadata and
  never rejected (260718-CHATS-L5F R4); only a malformed handshake shape fails.
- Tests cover protocol behavior only; they do not claim list/read/resume execution.

### Todos

Add native operation tests only when actual helper behavior lands behind the same locked boundary.

## Docs References

No Domain Documentation source is configured; the repository protocol is the direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Production protocol code implements the exact versions, handshake, fixed error output, and per-operation key validator under test. | L3-L139; L141-L259 | [protocol.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.ts) |
| The Python foundation suite separately checks exact package/lock pins and forbidden ambient resolution. | L63-L99 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this repository-local test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: corrected the handshake coverage for the R4
  version-gate removal — the new `handshake reports observed versions and is ready by contract, never
  version-gated` test pins that `buildHandshake` always returns `ready` (versions informational) and
  the operation result is the gate; removed the "wrong-version rejection" description (malformed-shape
  rejection remains). Verification metadata stays pinned (uncommitted); closeout re-stamps.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the helper regression sidecar after
  hostile privacy/schema fix rounds passed. Verification is blank until closeout commits and stamps
  the new source.
