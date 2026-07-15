# interactions.jsonl

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/claude_stream_json/2.1.210/interactions.jsonl` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:08+02:00 |
| lastVerifiedCommitHash |  |
| lastVerifiedCommitDate |  |
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/tests overview](../../../overview.md)

## Purpose

Provides the Claude 2.1.210 permission and user-question frames used to keep durable interaction
routing covered alongside the ACPUI-L1 startup fixture cohort.

## Code Commentary

### Logic

The first frame requests permission for a Bash tool invocation. The second requests one structured
single-select answer through `AskUserQuestion`; the adapter test replies through the durable
interaction response path and verifies the vendor response shapes.

### Conventions

The request and tool-use ids are stable fixture correlations. Questions preserve Claude's nested
header, option label, description, and `multiSelect` fields without turning fixture text into
application policy.

### Invariants And Boundaries

- Fixture requests never authorize an automatic permission or user-input decision.
- The frames contain no credentials or model-generated answer content.
- Interaction evidence remains separate from model-catalog discovery and from terminal completion.

### Todos

None known.

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The Claude adapter suite loads both frames and proves permission and question responses through the
same durable interaction boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The fixture loader selects the 2.1.210 directory and parses each JSONL frame. | L29-L36 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| The interaction test consumes both frames and verifies the explicit permission and question responses. | L391-L432 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |

## Cross-Repo References

No meaningful cross-repo references were needed for this fixture.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:08+02:00 — 260714-ACPUI-L1 curator: created the strict sidecar for the current
  versioned permission and `AskUserQuestion` fixture. Verification metadata remains empty until
  closeout stamps the L1 code commit.
