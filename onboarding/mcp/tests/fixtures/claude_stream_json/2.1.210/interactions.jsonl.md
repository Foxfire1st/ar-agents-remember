# interactions.jsonl

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/claude_stream_json/2.1.210/interactions.jsonl` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:08+02:00 |
| lastVerifiedCommitHash |  `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |  2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The Claude adapter suite loads both frames and proves permission and question responses through the
same durable interaction boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture loader selects the 2.1.210 directory. | `FIXTURE_ROOT` | mcp/tests/test_harness_control_claude.py:40-40 |
| The fixture loader parses each JSONL frame through `_load_fixture`. | `_load_fixture` | mcp/tests/test_harness_control_claude.py:49-50 |
| The interaction test consumes both frames and verifies the explicit permission and question responses. | `test_permissions_and_ask_user_question_use_durable_interaction_response` | mcp/tests/test_harness_control_claude.py:694-745 |

## Cross-Repo References

No meaningful cross-repo references were needed for this fixture.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: anchored fixture loading and durable
  permission/question response coverage to exact test symbols.

- 2026-07-15T20:08+02:00 — 260714-ACPUI-L1 curator: created the strict sidecar for the current
  versioned permission and `AskUserQuestion` fixture. Verification metadata remains empty until
  closeout stamps the L1 code commit.
