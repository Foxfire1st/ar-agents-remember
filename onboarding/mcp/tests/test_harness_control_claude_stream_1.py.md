# mcp/tests/test_harness_control_claude_stream_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_harness_control_claude_stream_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                                        |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Claude structured launch, discovery, prompt and interaction contracts.

## Code Commentary

### Logic

Token-free bootstrap and list_models discover capabilities without query cost. Launch preserves arguments/environment and requires structured init; absent capabilities or model mismatch close loudly. Prompt acceptance, activity, settling and terminal completion are distinct. Permission and user-question responses use the exact durable interaction identity.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A fixture version is evidence, not authority to invent unsupported flags. Authentication data must not leak into handshake evidence and ordinary launch keeps its supplied MCP configuration.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Discover uses only token free bootstrap and list models. | `test_discover_uses_only_token_free_bootstrap_and_list_models` | mcp/tests/test_harness_control_claude_stream_1.py:30-50 |
| Launch preserves arguments environment and requires structured init. | `test_launch_preserves_arguments_environment_and_requires_structured_init` | mcp/tests/test_harness_control_claude_stream_1.py:52-107 |
| Missing protocol capability fails loudly. | `test_missing_protocol_capability_fails_loudly` | mcp/tests/test_harness_control_claude_stream_1.py:109-121 |
| Expected launch model mismatch closes and propagates as failure. | `test_expected_launch_model_mismatch_closes_and_propagates_as_failure` | mcp/tests/test_harness_control_claude_stream_1.py:123-139 |
| Correlated acceptance retry activity and terminal result are distinct. | `test_correlated_acceptance_retry_activity_and_terminal_result_are_distinct` | mcp/tests/test_harness_control_claude_stream_1.py:142-183 |
| Permissions and ask user question use durable interaction response. | `test_permissions_and_ask_user_question_use_durable_interaction_response` | mcp/tests/test_harness_control_claude_stream_1.py:185-236 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
