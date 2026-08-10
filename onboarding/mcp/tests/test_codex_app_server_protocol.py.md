# mcp/tests/test_codex_app_server_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_app_server_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Deterministic stdio transport and parser tests for Codex app-server protocol boundaries, including
cancellation-safe correlation without retained request tombstones.

## Code Commentary

### Logic

The tests use temporary child processes to prove response/server-message correlation, malformed
JSON failure, oversized-line failure, thread-open effort/status parsing, and rejection of unknown
status or missing effective-effort echoes.

The L3 cancellation cases write a request, cancel its caller, and prove that a late response is
dropped rather than satisfying the next request. A two-size scaling case cancels 8 and 64 requests
whose responses never arrive, then successfully issues one more request. This pins removal of the
cancelled future itself as sufficient reclamation: the transport retains no ever-growing abandoned
request-id set.

### Conventions

Each child process is local and deterministic; transport limits are set explicitly when testing
boundedness. The cancellation scaling test uses two input sizes so retained-state behavior is
demonstrated rather than inferred from a single request.

### Invariants And Boundaries

- Protocol parse failures are typed and loud.
- Thread-open parsing requires the effective reasoning effort and recognized status.
- Cancelling a correlated request removes its pending future; a later syntactically valid response
  is stale and cannot resolve another request.
- Missing late responses require no tombstone retention, and subsequent requests must still work
  after both tested cancellation volumes.
- These tests do not authorize compatibility parsing or silent fallback.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Late-response coverage proves that cancelling one request cannot steal or poison the next request's correlated response. | `test_cancelled_request_neutralizes_late_response_and_next_request_survives` | mcp/tests/test_codex_app_server_protocol.py:239-262 |
| Two-size coverage proves that 8 and 64 cancelled requests without responses require no retained tombstone store and leave the next request usable. | `test_cancelled_requests_without_responses_need_no_retained_tombstones` | mcp/tests/test_codex_app_server_protocol.py:265-291 |
| The transport removes cancelled pending futures and discards only syntactically valid responses whose ids no longer have a live future. | `CodexStdioTransport` | mcp/src/agents_remember/serving/codex_app_server_protocol.py:60-305 |
| Fixture captures the pinned protocol identity. | "codex-app-server/0.144.3" | mcp/tests/fixtures/codex_app_server_0_144_3.json:4-4 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |

## 260727-CHATS-IM-L2 Framing-Fuse Regression Delta

The protocol suite now covers increasing below-fuse sizes including the exact 4,846,576-byte
production failure, the constant's 128 MiB compatibility value, and the payload-versus-delimiter
boundary. Its large boundary subprocess proves exactly 128 MiB of JSON plus newline succeeds while
one more payload byte fails. The shared-fatal regression proves an above-fuse record delivers one
explicit failure to every pending RPC and the event stream; the fuse is not presented as history
paging.

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the supported protocol-test citations and removed the unsupported reviewer-verdict row; final exact frozen-snapshot check is clean.
- 2026-08-02T18:15+02:00 — 260731-EFA-L6 curator W1-B06: repaired 4 Repo-Internal reference rows and 1 exact staged fixture range; retained 1 unresolved reviewer-verdict Cross-Repo row; scoped result preserves 2 Tier-3 findings (`citation_anchor_missing`, `citation_source_malformed`).

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: documented measured-size compatibility,
  increasing payloads, exact 128 MiB delimiter-excluded boundary, and shared-fatal above-fuse
  regressions. Verification metadata remains pinned while uncommitted.

- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented cancellation-safe correlation,
  stale late-response disposal, and two-size proof that missing responses need no retained
  tombstones; corrected the governing overview backlink. Verification metadata remains pinned
  until closeout stamps the L3 code commit.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for stdio correlation,
  bounded message handling, thread parsing, and loud incompatibility tests. Verification remains
  unset until closeout stamps the code commit.
