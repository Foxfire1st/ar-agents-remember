# mcp/tests/test_provider_limit_suppression.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Focused unit-regression suite verifying window-scoped provider-limit suppression across the sibling sidecar writer (`serving/paseo/provider_limits.py` and `provider_limit_suppressions.py`), the non-blocking MCP server hook (`mcp/server.py`), and the `agents-remember provider-limits` runtime CLI (`cli/provider_limit_hold.py` and `cli/__main__.py`).

## Code Commentary

The module contains fourteen test functions (twenty-one collected cases with parametrization) grouped across four areas:

- **Sidecar compatibility, `recordedAt` preservation, and expiry pruning**: verifies that a legacy `ar-provider-limits/v1` file with no sidecar still reads as a live limit (`recordedAt: null` in status), that `record_usage_reads` keeps `provider-limits.json` strictly v1 (`extra="forbid"`) while preserving `recordedAt` across re-reads, and that expired sidecar entries prune during both `claim_due_reports` (`_periodic_update`) and `record_usage_reads` at population sizes 2 and 20.
- **Window filtering, `until` recomputation, `clearedSeats`, and atomic pair rollback**: verifies multi-window `until` recomputation when one window is suppressed while another stays live, single-window suppression dropping the report, emitting `clearedSeats`, stopping periodic rechecks, and still holding on a later different exhausting window, `claim_due_reports` emitting `clearedSeats` when dropping a sidecar-suppressed live report, and `_commit_pair_locked` rolling back the sidecar (both pre-existing and absent) when `_write_limits` raises.
- **Causal turn-start guard and async MCP hook**: parametrized fail-closed matrix (missing agent, `idle`, earlier turn start, equal timestamp, missing `eventAt`, incomplete publication) plus missing/malformed `host-activity.json` and legacy `recordedAt is None` (while operator CLI still suppresses legacy records), `in-turn` and `permission` success with persisted evidence fields, real `AgentsRememberMCP.call_tool("server_info")` proving `_bound_agent_id` snapshotting, off-event-loop execution (`threading.get_ident()`), and `OSError` containment, plus unbound and malformed bindings snapshotting `None` and skipping the hook.
- **Operator CLI (`provider-limits status|suppress|unsuppress`)**: invokes `cli.__main__.main` end-to-end for `status`, multi-window `--window`-required exit-2 refusal, non-live report/window exit-2 refusals naming the target, `--report --window` and `--agent` suppressions, `unsuppress` restoring normal re-read judgment, and exit-2 refusal on missing suppressions.

## Relationships

- Registered once in `mcp/tests/test-evidence-lanes.toml` under `unit-regression`.
- Declared as an exact consumer of `mcp/tests/_user_settings_guard.py`, `mcp/tests/fixtures/repository_profiles/node/package-lock.json`, and `mcp/tests/paseo_runtime_test_support.py` in `mcp/tests/evidence-lifecycle.toml`.

## Evidence

- Verifies legacy v1 compatibility without a sidecar, `recordedAt` preservation across re-reads, and expired sidecar pruning at sizes 2 and 20. [1]
- Verifies multi-window `until` recomputation, single-window report drop with `clearedSeats` and stopped polling, periodic drop clear markers, and two-file rollback on limits-write failure. [2]


- Verifies `agents-remember provider-limits status`, `suppress`, and `unsuppress` JSON outputs and exit-2 refusals end-to-end. [4]

- Verifies the fail-closed causal guard matrix, `in-turn`/`permission` auto-suppression, off-loop MCP hook execution with I/O error containment, and unbound/malformed binding skips. [3]
