# mcp/native_helpers/conversation_library/src/protocol.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/native_helpers/conversation_library/src/protocol.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:45+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Locked native conversation-library helper overview](../overview.md)

## Purpose

Defines the versioned JSON-lines contract shared by the Python host and the repository-locked
Claude/Pi native helpers, and the serve loop, version probing,
signing, and paging primitives the two helper entries implement list/read/resolve with.

## Code Commentary

### Logic

- Declares protocol, exact Claude/Pi helper versions, request-byte limit, operations, discriminated
  request/response types, and handshake result.
- `buildHandshake` is ALWAYS `ready` once the helper loaded and matched the wire
  `PROTOCOL_VERSION` — the contract is the only gate. It reports the observed runtime/helper versions as informational evidence and NEVER
  compares them to a locked/expected constant to refuse; the request's `expectedRuntimeVersion`/
  `expectedHelperVersion` survive as informational provenance only. The real gate is whether the
  subsequent list/read/resolve operation succeeds against the installed runtime.
- `parseHelperRequest` byte-bounds and parses one JSON object, validates protocol/request id/
  operation, then reconstructs the request from an exact operation-specific key set.
- Page operations require string-or-null cursors and positive safe-integer limits.
- One additive optional key extends the `read` operation: `agentId` (L52,
  L402-L426). It is admitted into the exact-key set, type-checked when present, and copied onto
  the reconstructed `ReadRequest` only as a string — present only for a sub-agent transcript
  read, so hosts and reads that never send it stay byte-identical.
- `redactHelperError` intentionally ignores raw detail and returns one fixed allow-listed string.
- The execution seam: `serveJsonLines` runs one correlated request/response loop over
  stdin/stdout (parse failures answer `invalid-request`, handler failures the typed vocabulary);
  `failureFor`/`raiseHelperError` map helper failures onto the four typed errors with
  allow-listed detail; `probeRuntimeVersion` observes an installed runtime's `--version` (first
  semver token); `observedDependencyVersion` reads the helper's own locked dependency version
  through the standard ESM resolver from inside this package; `signatureOf` is the deterministic
  SHA-256 native-store signature; `pageByOffset`/`windowByOrdinal` are the list and newest-window
  paging primitives with decimal cursor validation.

### Conventions

All request operations are explicit discriminated unions. Exact-key lists and reconstructed return
objects are intentional protocol authority, not compatibility scaffolding. Every line gets exactly
one correlated response so the Python host's request/response pairing can never drift.

### Invariants And Boundaries

- Never accept unknown or operation-inapplicable fields. The single sanctioned exception shape
  is an ADDITIVE optional key admitted deliberately (the `agentId` key on `read`): optional,
  exactly typed, and invisible to pre-existing callers — never a required-key change.
- The handshake is ready-by-contract: it never gates on a runtime/helper version comparison.
  A version drift is reported as informational evidence, not refused; the operation is the gate.
- Never expose raw helper error detail, regardless of its secret/path syntax: operation failures
  may carry allow-listed helper-supplied copy, everything else is the fixed redaction.
- Never add ambient module resolution: `observedDependencyVersion` resolves only through the
  declared lockfile dependency, never an npm cache, checkout, or global install.
- The request-byte bound protects the helper process before JSON parsing; read cursors must name
  an ordinal above the first item.

### Todos

None — list/read/resolve execution is landed; resume replay is proven by the live contract
probe (no locked-version gate remains anywhere in this contract).

## Docs References

No Domain Documentation source is configured. Local manifest, lock, and tests are the direct
contract evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The helper entries implement the operations this module frames; the Python host correlates
against this exact contract; the helper suite covers the admission and privacy matrix.

| Finding | Anchor | Source |
| --- | --- | --- |
| The private manifest and lock select the exact dependency versions represented by the protocol constants. | "@anthropic-ai/claude-agent-sdk", "@earendil-works/pi-coding-agent" | mcp/native_helpers/conversation_library/package.json:14-15 |
| Helper tests cover exact versions, malformed framing, wrong protocol, exact key sets, inapplicable fields, and hostile error details. | "the exact locked helper versions are protocol constants", "request parser rejects malformed framing and wrong protocol", "request parser rejects unknown fields for every operation", "request parser rejects known fields when they belong to another operation", "helper crash detail is fixed allow-listed copy for secrets" | mcp/native_helpers/conversation_library/src/protocol.test.ts:14-17; mcp/native_helpers/conversation_library/src/protocol.test.ts:41-66; mcp/native_helpers/conversation_library/src/protocol.test.ts:68-123; mcp/native_helpers/conversation_library/src/protocol.test.ts:125-179; mcp/native_helpers/conversation_library/src/protocol.test.ts:181-218 |
| Python foundation tests forbid incidental resolution in production helper source. | `test_helper_runtime_source_has_no_incidental_module_resolution` | mcp/tests/test_conversation_foundation.py:139-160 |
| The Python host spawns this contract's entries and correlates handshake plus one operation per process. | `ConversationLibraryHelperHost` | mcp/src/agents_remember/serving/conversation/library/helper_host.py:91-221 |
| The locked Claude and Pi entries consume the serve loop, probing, signing, and paging primitives. | `handleClaude`, `handlePi` | mcp/native_helpers/conversation_library/src/claude.ts:65-78; mcp/native_helpers/conversation_library/src/pi.ts:54-67 |

## Cross-Repo References

No neighboring workspace repository participates in the helper process boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-03T02:44:44+02:00 — W3-B05 curator: anchored 5 Tier-2 table citations with exact source paths; fixer generated all ranges.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: recorded the additive optional `agentId` on
  the `read` operation (sub-agent transcript reads only): admitted into the exact-key set,
  type-checked when present, copied only as a string, invisible to pre-L7 callers. Verification
  metadata stays pinned (uncommitted); closeout re-stamps the candidate commit.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: version-gate REMOVAL (developer ruling
  2026-07-21, R4). Corrected the now-false `buildHandshake` doctrine: it is always `ready` once the
  wire protocol version matches and reports observed runtime/helper versions as informational
  evidence; it never refuses on a version comparison. Reworded the "never promote a version
  mismatch to ready" invariant and the resume-replay Todo accordingly. Uncommitted; closeout
  re-stamps verification.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: documented the added execution seam — the
  correlated JSONL serve loop, typed failure mapping, runtime/dependency version probing,
  store signature, and offset/ordinal paging primitives the two new helper entries consume.
  Verification stays pinned at the L9 commit until closeout stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the JSONL protocol/privacy sidecar
  after same-reviewer PASS closed raw-error and exact-shape findings. Verification is blank until
  closeout commits and stamps the new source.
