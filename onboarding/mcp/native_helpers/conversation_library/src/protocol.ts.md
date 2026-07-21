# mcp/native_helpers/conversation_library/src/protocol.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/native_helpers/conversation_library/src/protocol.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Locked native conversation-library helper overview](../overview.md)

## Purpose

Defines the versioned JSON-lines contract shared by the Python host and the repository-locked
Claude/Pi native helpers, and — since 260718-CHATS-L2 — the serve loop, version probing,
signing, and paging primitives the two helper entries implement list/read/resolve with.

## Code Commentary

### Logic

- Declares protocol, exact Claude/Pi helper versions, request-byte limit, operations, discriminated
  request/response types, and handshake result.
- `buildHandshake` is now ALWAYS `ready` once the helper loaded and matched the wire
  `PROTOCOL_VERSION` (260718-CHATS-L5F R4, developer ruling 2026-07-21: the contract is the only
  gate). It reports the observed runtime/helper versions as informational evidence and NEVER
  compares them to a locked/expected constant to refuse; the request's `expectedRuntimeVersion`/
  `expectedHelperVersion` survive as informational provenance only. The real gate is whether the
  subsequent list/read/resolve operation succeeds against the installed runtime.
- `parseHelperRequest` byte-bounds and parses one JSON object, validates protocol/request id/
  operation, then reconstructs the request from an exact operation-specific key set.
- Page operations require string-or-null cursors and positive safe-integer limits.
- `redactHelperError` intentionally ignores raw detail and returns one fixed allow-listed string.
- L2 adds the execution seam: `serveJsonLines` runs one correlated request/response loop over
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

- Never accept unknown or operation-inapplicable fields.
- The handshake is ready-by-contract: it never gates on a runtime/helper version comparison (R4).
  A version drift is reported as informational evidence, not refused; the operation is the gate.
- Never expose raw helper error detail, regardless of its secret/path syntax: operation failures
  may carry allow-listed helper-supplied copy, everything else is the fixed redaction.
- Never add ambient module resolution: `observedDependencyVersion` resolves only through the
  declared lockfile dependency, never an npm cache, checkout, or global install.
- The request-byte bound protects the helper process before JSON parsing; read cursors must name
  an ordinal above the first item.

### Todos

None — list/read/resolve execution landed in L2; resume replay is proven by the live contract
probe (the R4 version gate is removed — no locked-version gate remains anywhere in this contract).

## Docs References

No Domain Documentation source is configured. Local manifest, lock, and tests are the direct
contract evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The helper entries implement the operations this module frames; the Python host correlates
against this exact contract; the helper suite covers the admission and privacy matrix.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The private manifest and lock select the exact dependency versions represented by the protocol constants. | L1-L22 | [package.json](agents-remember/mcp/native_helpers/conversation_library/package.json) |
| Helper tests cover exact versions, malformed framing, wrong protocol, exact key sets, inapplicable fields, and hostile error details. | L14-L210 | [protocol.test.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.test.ts) |
| Python foundation tests forbid incidental resolution in production helper source. | L102-L120 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The Python host spawns this contract's entries and correlates handshake plus one operation per process. | L100-L148 | [helper_host.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/helper_host.py) |
| The locked Claude and Pi entries consume the serve loop, probing, signing, and paging primitives. | L3-L22; L4-L17 | [claude.ts](agents-remember/mcp/native_helpers/conversation_library/src/claude.ts), [pi.ts](agents-remember/mcp/native_helpers/conversation_library/src/pi.ts) |

## Cross-Repo References

No neighboring workspace repository participates in the helper process boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
