# mcp/tests/test_codex_app_server_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_app_server_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:30+02:00 |
| lastVerifiedCommitHash | `acb308c50072d8cde0015c4828e39d12480872ed`|
| lastVerifiedCommitDate | 2026-07-14T12:32:48+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[mcp/tests overview](../overview.md)

## Purpose

Deterministic stdio transport and parser tests for Codex app-server protocol boundaries.

## Code Commentary

The tests use temporary child processes to prove response/server-message correlation, malformed JSON
failure, oversized-line failure, thread-open effort/status parsing, and rejection of unknown status
or missing effective-effort echoes.

## Conventions

Each child process is local and deterministic; transport limits are set explicitly when testing
boundedness.

## Invariants And Boundaries

- Protocol parse failures are typed and loud.
- Thread-open parsing requires the effective reasoning effort and recognized status.
- These tests do not authorize compatibility parsing or silent fallback.

## Todos

None known for this leaf.

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Tests target bounded transport methods and parser helpers. | L35-L116 | [codex_app_server_protocol.py](../src/agents_remember/serving/codex_app_server_protocol.py) |
| Fixture captures the pinned protocol identity. | L1-L31 | [codex_app_server_0_144_3.json](fixtures/codex_app_server_0_144_3.json) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Reviewer confirmed malformed/oversized protocol and pinned-schema checks. | L25-L29 | [260713-PHA-L3-reviewer-verdict.md](../../../../../../../../../../../../ar-coordination/tasks/agents-remember/260713_protocol-backed-harness-adapters/notes/reports/260713-PHA-L3-reviewer-verdict.md) |

## Update History

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for stdio correlation,
  bounded message handling, thread parsing, and loud incompatibility tests. Verification remains
  unset until closeout stamps the code commit.
