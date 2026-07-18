# mcp/native_helpers/conversation_library/src/protocol.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/native_helpers/conversation_library/src/protocol.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Locked native conversation-library helper overview](../overview.md)

## Purpose

Pins the helper's exact version handshake, framing, operation-schema, and raw-error privacy
boundaries with deterministic Node tests.

## Code Commentary

### Logic

The six tests verify exact Claude/Pi protocol constants, exact requested/observed handshake tuples,
malformed/wrong-version rejection, unknown fields across every operation, known-but-inapplicable
field rejection, and one fixed safe output across bearer, JSON credential, environment secret,
POSIX/Windows path, and long-input examples.

### Conventions

Negative cases are table-driven across sibling operations and credential shapes so a narrow happy
path cannot make a broader privacy/schema claim.

### Invariants And Boundaries

- Test each operation's exact accepted shape before adding fields.
- Privacy tests assert the unsafe value itself never survives, not merely that one regex ran.
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

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the helper regression sidecar after
  hostile privacy/schema fix rounds passed. Verification is blank until closeout commits and stamps
  the new source.
