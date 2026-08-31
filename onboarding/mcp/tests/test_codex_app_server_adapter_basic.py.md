# mcp/tests/test_codex_app_server_adapter_basic.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_codex_app_server_adapter_basic.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-30T22:33:39+02:00                                            |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`                                        |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Exercises basic Codex app-server negotiation, startup identity, model discovery, desired/effective
settings, connected-MCP-tool readiness for role launches, and fail-clean adapter teardown under the
current Desktop user-agent contract.

## Code Commentary

L23 broadens initialize coverage from one Desktop product token to product-agnostic server identity: the Agents Remember token and Codex Desktop token both pass only with the exact client suffix, while mismatched client identity still fails cleanly.

The Desktop regression presents a host-first primary token (`Codex Desktop/<version>`) plus the
exact initialize client suffix. Its positive case proves the host version feeds the adapter
protocol identity; its negative peer changes only the requested client version and proves startup
fails cleanly rather than accepting an unrelated host response.

The settings-update regression drives all deliberate-state branches through the public adapter:
an already-effective echo stays inert, a stale effective echo remains inert while a requested
change is pending, a matching desired echo promotes that selection, and an unrelated echo fails
the adapter. This raises meaningful branch coverage on the changed session owner rather than
exempting its CRAP score.

ARSPAWN-L5 adds the role-start readiness boundary: paginated native MCP status must converge on a
connected server advertising exact `dispatch_agent`; settled absence and timeout refuse, and a
cleanup failure remains secondary to the primary readiness refusal. Roleless startup retains its
existing path.
The negative matrix now covers invalid readiness requests, malformed status data and tool
inventories, invalid/repeated/exhausted pagination, and a role-start thread with no established
thread identity.


## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_codex_app_server_adapter_basic.py`.
- Both initialize wire forms retain the existing independent thread `cliVersion` agreement gate.
- Readiness polling is bounded, uses the native app-server inventory, and has no alternate tool-name
  or cleanup-masking fallback.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Desktop startup accepts the host-first product version only with the exact Agents Remember client suffix and rejects a version-mismatched suffix. | `test_client_user_agent_uses_host_version_and_exact_client_identity`; `test_client_user_agent_rejects_wrong_client_identity` | mcp/tests/test_codex_app_server_adapter_basic.py:549-566; mcp/tests/test_codex_app_server_adapter_basic.py:569-581 |
| Public settings notifications cover matching, stale-effective, desired-promotion, and drift-refusal branches. | `test_settings_updates_cover_matching_stale_and_drift_branches` | mcp/tests/test_codex_app_server_adapter_basic.py:663-723 |

## Update History

- 2026-08-31T13:42+02:00 — A005 closeout repair completed fail-closed Codex MCP readiness parsing
  and pagination coverage required by the changed-unit gate.

- 2026-08-30T22:33:39+02:00 — 260821-ARSPAWN-L5 recorded the connected-`dispatch_agent`
  startup gate, pagination, bounded timeout, roleless preservation, and primary-failure retention.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-12T04:41+02:00 — 260731-EFA-L22 closeout repair: added public adapter coverage for all
  `accept_settings_update` paths after the first targeted closeout run proved tests/diff coverage
  green but correctly refused the changed session owner at CRAP 46.84.

- 2026-08-12T04:15+02:00 — 260731-EFA-L22 Codex Desktop repair: added positive host-first
  negotiation coverage and exact-client-suffix refusal coverage, and migrated the shared fixture
  instead of retaining unused CLI compatibility; the focused module passes under `-n=auto`.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
