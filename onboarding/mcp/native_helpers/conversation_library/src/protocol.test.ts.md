# mcp/native_helpers/conversation_library/src/protocol.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/native_helpers/conversation_library/src/protocol.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Production protocol code implements the exact versions, handshake, fixed error output, and per-operation key validator under test. | `PROTOCOL_VERSION`; `CLAUDE_SDK_VERSION`; `PI_CODING_AGENT_VERSION`; `redactHelperError`; `buildHandshake`; `parseHelperRequest`; `validateOperationShape`; `requireExactKeys` | mcp/native_helpers/conversation_library/src/protocol.ts:13-15; mcp/native_helpers/conversation_library/src/protocol.ts:98-102; mcp/native_helpers/conversation_library/src/protocol.ts:13-13; mcp/native_helpers/conversation_library/src/protocol.ts:306-325; mcp/native_helpers/conversation_library/src/protocol.ts:327-345; mcp/native_helpers/conversation_library/src/protocol.ts:347-445; mcp/native_helpers/conversation_library/src/protocol.ts:447-452 |
| The Python foundation suite separately checks exact package/lock pins and forbidden ambient resolution. | `test_helper_package_and_lock_select_only_the_exact_repository_dependencies`; `test_helper_runtime_source_has_no_incidental_module_resolution` | mcp/tests/test_conversation_foundation.py:125-136; mcp/tests/test_conversation_foundation.py:139-160 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this repository-local test.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 2 table citations and normalized 2 source paths; no unresolved Tier-3 claims.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: corrected the handshake coverage for the R4
  version-gate removal — the new `handshake reports observed versions and is ready by contract, never
  version-gated` test pins that `buildHandshake` always returns `ready` (versions informational) and
  the operation result is the gate; removed the "wrong-version rejection" description (malformed-shape
  rejection remains). Verification metadata stays pinned (uncommitted); closeout re-stamps.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the helper regression sidecar after
  hostile privacy/schema fix rounds passed. Verification is blank until closeout commits and stamps
  the new source.
