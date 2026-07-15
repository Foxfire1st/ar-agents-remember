# mcp/tests/test_codex_app_server_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_app_server_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:21+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892` |
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Late-response coverage proves that cancelling one request cannot steal or poison the next request's correlated response. | L94-L117 | [test_codex_app_server_protocol.py](agents-remember/mcp/tests/test_codex_app_server_protocol.py) |
| Two-size coverage proves that 8 and 64 cancelled requests without responses require no retained tombstone store and leave the next request usable. | L120-L146 | [test_codex_app_server_protocol.py](agents-remember/mcp/tests/test_codex_app_server_protocol.py) |
| The transport removes cancelled pending futures and discards only syntactically valid responses whose ids no longer have a live future. | L93-L106; L220-L232 | [codex_app_server_protocol.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_protocol.py) |
| Fixture captures the pinned protocol identity. | L1-L31 | [codex_app_server_0_144_3.json](agents-remember/mcp/tests/fixtures/codex_app_server_0_144_3.json) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Reviewer confirmed malformed/oversized protocol and pinned-schema checks. | L25-L29 | [260713-PHA-L3-reviewer-verdict.md](ar-coordination/tasks/agents-remember/260713_protocol-backed-harness-adapters/notes/reports/260713-PHA-L3-reviewer-verdict.md) |

## Update History

- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented cancellation-safe correlation,
  stale late-response disposal, and two-size proof that missing responses need no retained
  tombstones; corrected the governing overview backlink. Verification metadata remains pinned
  until closeout stamps the L3 code commit.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for stdio correlation,
  bounded message handling, thread parsing, and loud incompatibility tests. Verification remains
  unset until closeout stamps the code commit.
