# mcp/tests/test_launch_identity_confirmation.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Unittest suite verifying launch-time binding confirmation, single retry under the same `requestId`, zero-live-seats refusal, multiple, unreadable, and unbound server discrimination, `/proc`-absent and lazy-harness (`claude`) behavior, held-seat create and open re-confirmation, real `paseo_bridge.mjs` `skipToolServerWait=true`, and unspoofable `role_message` sender-line derivation from `AgentBinding`.

## Code Commentary

- Builds on `PaseoLaunchTestCase` (fast-polling `_LaunchFixture` with `write_server_bindings = False` and synthetic `/proc` helpers `_write_fake_proc`, `_write_binding_file`, `_seed_harness`), `RoleToolsTestCase`, and `AgentCommandScriptTests` (driving the real `paseo_bridge.mjs` script).
- Six test classes (14 test methods) cover: foreign-binding single retry succeeding and double-failure HTTP 502 refusal with zero live seats; missing-registration timeout retry and refusal; immediate refusal under the 5 s window for two bound servers under one harness root or shared `parentPid`; unbound server allowed versus unreadable server refused under the same harness; `/proc`-absent identity-only confirmation (`ancestrySkippedReason="proc-unavailable"`); lazy `claude` provider skipping Step 2 confirmation in one `agent-create` call; held-seat confirmation at create and re-confirmation at open with `skipToolServerWait=True`, single retry when the prior binding disappears, and double-failure archiving both; real bridge skipping `TOOL_SERVER_START_MS` (6 s) when `skipToolServerWait=True`; and `sender_line`/`role_message` deriving sender strictly from `AgentBinding` despite spoofed message text or ambient env vars.
- Registered in `mcp/tests/test-evidence-lanes.toml` (`unit-regression`) and `mcp/tests/evidence-lifecycle.toml`; source assertions only, not a live run record.

## Relationships

- **Code under test:** `mcp/src/agents_remember/cli/role_launch_confirmation.py`, `paseo_launch.py`, `role_launch_outcome.py`, `role_held_messages.py`, `paseo_role_caller.py`, `paseo_role_tools.py`, `paseo_bridge.mjs`, and `serving/server_bindings.py`.
- **Support:** `paseo_launch_test_support.py`, `paseo_role_tools_test_support.py`, `test_paseo_launch.py`, and `test_paseo_bridge_agents.py`.
- **Catalogs:** `mcp/tests/test-evidence-lanes.toml` and `mcp/tests/evidence-lifecycle.toml`.

## Evidence

- Foreign binding on attempt 1 archives attempt 1 and retries once under the same `requestId` (`:retry-1`); double failure refuses HTTP 502 with zero live seats. [1]

- Missing registration retries once then refuses; duplicate bound servers (under harness root or shared parent PID) and unreadable servers refuse immediately while unbound servers pass. [2]

- Absent `/proc` confirms by identity only (`proc-unavailable`) and lazy `claude` skips Step 2 confirmation in one `agent-create` call. [3]
- Held seats confirm at create and re-confirm at open with `skipToolServerWait=True`, retry once when the prior binding disappears, and archive both on double failure. [4]
- Real `paseo_bridge.mjs` skips `TOOL_SERVER_START_MS` when `skipToolServerWait=True`, and `role_message` and `sender_line` derive sender strictly from `AgentBinding`. [5]
