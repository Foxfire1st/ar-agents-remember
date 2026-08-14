# initialization.jsonl

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/claude_stream_json/2.1.210/initialization.jsonl` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:08+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/tests overview](../../../overview.md)

## Purpose

Provides the current Claude 2.1.210 fake-transport startup and model-catalog fixture used by the
ACPUI-L1 capability tests. The version labels reproducible test evidence; it is not a production
compatibility pin.

## Code Commentary

### Logic

The four JSONL frames model the native token-free discovery sequence: correlated control
initialization, `system/init`, a zero-turn and zero-cost bootstrap result, and a correlated
`list_models` response. The catalog includes a reasoning model with its own effort menu, a model
without effort, and an account-disabled model.

### Conventions

Each line is one vendor-shaped frame. Request ids intentionally match the adapter's startup
constants, and the initialize payload intentionally omits the obsolete `models` and `account`
fields because model discovery now has its own control request.

### Invariants And Boundaries

- Discovery evidence remains prompt-free and token-free: the bootstrap result records zero turns
  and zero cost.
- Effort values belong to their advertised model and are not a global enum.
- Disabled models remain catalog evidence but are not selectable.
- The fixture contains no credentials or model-generated response content and does not authorize a
  version gate or fallback behavior.

### Todos

None known.

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The Claude adapter suite selects this versioned fixture root explicitly and proves both the
token-free discovery sequence and the normalized catalog projection.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture loader selects the 2.1.210 directory and parses each JSONL frame. | `_load_fixture` | mcp/tests/test_harness_control_claude.py:43-44 |
| Discovery and running advertise consume the initialization and catalog frames without a model turn. | `test_discover_uses_only_token_free_bootstrap_and_list_models` | mcp/tests/test_harness_control_claude_stream_1.py:33-53 |
| The dedicated parser validates model identity, model-local effort, disabled state, and current-model selection. | `parse_list_models_response` | mcp/src/agents_remember/serving/claude_stream_capabilities.py:15-32 |

## Cross-Repo References

No meaningful cross-repo references were needed for this fixture.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 6 citation findings (3 rows); scoped recheck clean.

- 2026-07-15T20:08+02:00 — 260714-ACPUI-L1 curator: created the strict sidecar for the current
  prompt-free initialization and dynamic `list_models` fixture. Verification metadata remains empty
  until closeout stamps the L1 code commit.
