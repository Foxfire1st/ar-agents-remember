# Onboarding Drift Report

**Scope checked:** `/home/mohamedreadone/Projects/ar-coordination/worktrees/agents-remember/260714-acpui-l2-launch-with-flags-ar/memory-260714-acpui-l2-launch-with-flags/onboarding`
**Generated:** 2026-07-15T23:27:41+02:00
**Repository HEAD:** `fc2e8b2`

## Summary

| Classification | Count |
| --- | ---: |
| up to date | 707 |
| drifted | 36 |
| missing verification | 2 |
| missing | 0 |
| orphaned | 0 |
| disabled | 32 |
| unsupported | 0 |

## Actionable Findings

| Onboarding unit | Source file | Storage | Classification | Trust | Likely affected sections | Note |
| --- | --- | --- | --- | --- | --- | --- |
| `overview.md` | `.` | memory-repo | drifted | medium | overview; route summary; invariants | Source has local unstaged changes not represented in HEAD. |
| `dev-skills/README.md.md` | `dev-skills/README.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `dev-skills/dashboard-experience-review/SKILL.md.md` | `dev-skills/dashboard-experience-review/SKILL.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `dev-skills/dashboard-experience-review/delegation-map.md.md` | `dev-skills/dashboard-experience-review/delegation-map.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `dev-skills/dashboard-experience-review/owned-methods.md.md` | `dev-skills/dashboard-experience-review/owned-methods.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `dev-skills/dashboard-experience-review/templates/missing-view-matrix-template.md.md` | `dev-skills/dashboard-experience-review/templates/missing-view-matrix-template.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `dev-skills/dashboard-experience-review/templates/review-report-template.md.md` | `dev-skills/dashboard-experience-review/templates/review-report-template.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `dev-skills/dashboard-experience-review/templates/scenario-catalog-template.md.md` | `dev-skills/dashboard-experience-review/templates/scenario-catalog-template.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `docs/design/engine-room/engine-room-visual-language.html.md` | `docs/design/engine-room/engine-room-visual-language.html` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `docs/design/engine-room/podstage.html.md` | `docs/design/engine-room/podstage.html` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `docs/design/observable-lifecycle.md.md` | `docs/design/observable-lifecycle.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `docs/reference/overview.md` | `docs/reference` | memory-repo | drifted | medium | overview; route summary; invariants | Source has local unstaged changes not represented in HEAD. |
| `docs/reference/harnesses.md.md` | `docs/reference/harnesses.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `docs/reference/mcp-tools.md.md` | `docs/reference/mcp-tools.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `docs/reference/settings-json.md.md` | `docs/reference/settings-json.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `docs/reference/skills.md.md` | `docs/reference/skills.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `entities.md` | `entity:Delivery Injector` | memory-repo | drifted | medium | entity catalog; Delivery Injector; source evidence | mcp/src/agents_remember/mcp/tools/terminal.py: Source has local unstaged changes not represented in HEAD. |
| `entities.md` | `entity:Harness Capability Snapshot` | memory-repo | drifted | low | entity catalog; Harness Capability Snapshot; source evidence | Unable to compute entity fingerprint: fatal: path 'mcp/src/agents_remember/serving/harness_launch.py' exists on disk, but not in 'HEAD' |
| `entities.md` | `entity:Seat Retirement` | memory-repo | drifted | medium | entity catalog; Seat Retirement; source evidence | mcp/src/agents_remember/mcp/tools/terminal.py: Source has local unstaged changes not represented in HEAD. |
| `entities.md` | `entity:Supervisor Sweep` | memory-repo | drifted | medium | entity catalog; Supervisor Sweep; source evidence | mcp/src/agents_remember/kernel/agentic_settings.py: Source has local unstaged changes not represented in HEAD. |
| `mcp/overview.md` | `mcp` | memory-repo | drifted | medium | overview; route summary; invariants | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/kernel/agentic_settings.py.md` | `mcp/src/agents_remember/kernel/agentic_settings.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/mcp/server.py.md` | `mcp/src/agents_remember/mcp/server.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/mcp/tools/overview.md` | `mcp/src/agents_remember/mcp/tools` | memory-repo | drifted | medium | overview; route summary; invariants | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/mcp/tools/terminal.py.md` | `mcp/src/agents_remember/mcp/tools/terminal.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/models/overview.md` | `mcp/src/agents_remember/models` | memory-repo | drifted | medium | overview; route summary; invariants | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/models/terminal.py.md` | `mcp/src/agents_remember/models/terminal.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md.md` | `mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md.md` | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/serving/overview.md` | `mcp/src/agents_remember/serving` | memory-repo | drifted | medium | overview; route summary; invariants | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/serving/codex_app_server_adapter.py.md` | `mcp/src/agents_remember/serving/codex_app_server_adapter.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/serving/codex_app_server_session.py.md` | `mcp/src/agents_remember/serving/codex_app_server_session.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/serving/harness_capabilities.py.md` | `mcp/src/agents_remember/serving/harness_capabilities.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/serving/harness_control_adapter.py.md` | `mcp/src/agents_remember/serving/harness_control_adapter.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/serving/harness_control_claude.py.md` | `mcp/src/agents_remember/serving/harness_control_claude.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/serving/harness_control_factories.py.md` | `mcp/src/agents_remember/serving/harness_control_factories.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/serving/harness_control_runner.py.md` | `mcp/src/agents_remember/serving/harness_control_runner.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/serving/harness_launch.py.md` | `mcp/src/agents_remember/serving/harness_launch.py` | memory-repo | missing verification | medium | metadata; verification | Missing source path or lastVerifiedCommitHash. |
| `mcp/src/agents_remember/serving/harnesses.py.md` | `mcp/src/agents_remember/serving/harnesses.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/serving/pi_rpc_adapter.py.md` | `mcp/src/agents_remember/serving/pi_rpc_adapter.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/src/agents_remember/serving/terminal_opener.py.md` | `mcp/src/agents_remember/serving/terminal_opener.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/tests/overview.md` | `mcp/tests` | memory-repo | drifted | medium | overview; route summary; invariants | Source has local unstaged changes not represented in HEAD. |
| `mcp/tests/fixtures/claude_stream_json/2.1.207/initialization.jsonl.md` | `mcp/tests/fixtures/claude_stream_json/2.1.207/initialization.jsonl` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `mcp/tests/fixtures/claude_stream_json/2.1.207/interactions.jsonl.md` | `mcp/tests/fixtures/claude_stream_json/2.1.207/interactions.jsonl` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `mcp/tests/fixtures/claude_stream_json/2.1.207/turn.jsonl.md` | `mcp/tests/fixtures/claude_stream_json/2.1.207/turn.jsonl` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `mcp/tests/fixtures/claude_stream_json/2.1.210/initialization.jsonl.md` | `mcp/tests/fixtures/claude_stream_json/2.1.210/initialization.jsonl` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `mcp/tests/fixtures/claude_stream_json/2.1.210/interactions.jsonl.md` | `mcp/tests/fixtures/claude_stream_json/2.1.210/interactions.jsonl` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `mcp/tests/fixtures/claude_stream_json/2.1.210/turn.jsonl.md` | `mcp/tests/fixtures/claude_stream_json/2.1.210/turn.jsonl` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `mcp/tests/fixtures/pi_rpc/activity.jsonl.md` | `mcp/tests/fixtures/pi_rpc/activity.jsonl` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `mcp/tests/test_agentic_settings.py.md` | `mcp/tests/test_agentic_settings.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/tests/test_codex_app_server_adapter.py.md` | `mcp/tests/test_codex_app_server_adapter.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/tests/test_dispatch_expectation_rows.py.md` | `mcp/tests/test_dispatch_expectation_rows.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/tests/test_harness_control_claude.py.md` | `mcp/tests/test_harness_control_claude.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/tests/test_harness_control_runner.py.md` | `mcp/tests/test_harness_control_runner.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/tests/test_harness_launch.py.md` | `mcp/tests/test_harness_launch.py` | memory-repo | missing verification | medium | metadata; verification | Missing source path or lastVerifiedCommitHash. |
| `mcp/tests/test_harnesses.py.md` | `mcp/tests/test_harnesses.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/tests/test_spawn_agent_session.py.md` | `mcp/tests/test_spawn_agent_session.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `mcp/tests/test_terminal_opener.py.md` | `mcp/tests/test_terminal_opener.py` | memory-repo | drifted | medium | logic; invariants; conventions; docs references | Source has local unstaged changes not represented in HEAD. |
| `pyproject.toml.md` | `pyproject.toml` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `skills/l-01-agent-lifecycles/overview.md` | `skills/l-01-agent-lifecycles` | memory-repo | drifted | medium | overview; route summary; invariants | Source has local unstaged changes not represented in HEAD. |
| `skills/l-01-agent-lifecycles/SKILL.md.md` | `skills/l-01-agent-lifecycles/SKILL.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `skills/l-01-agent-lifecycles/roles/architect.md.md` | `skills/l-01-agent-lifecycles/roles/architect.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `skills/l-01-agent-lifecycles/roles/curator.md.md` | `skills/l-01-agent-lifecycles/roles/curator.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `skills/l-01-agent-lifecycles/roles/designer.md.md` | `skills/l-01-agent-lifecycles/roles/designer.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `skills/l-01-agent-lifecycles/roles/manager.md.md` | `skills/l-01-agent-lifecycles/roles/manager.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `skills/l-01-agent-lifecycles/roles/orchestrator.md.md` | `skills/l-01-agent-lifecycles/roles/orchestrator.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `skills/l-01-agent-lifecycles/roles/reviewer.md.md` | `skills/l-01-agent-lifecycles/roles/reviewer.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `skills/l-01-agent-lifecycles/roles/strategist.md.md` | `skills/l-01-agent-lifecycles/roles/strategist.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `skills/l-01-agent-lifecycles/roles/system-specialist.md.md` | `skills/l-01-agent-lifecycles/roles/system-specialist.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
| `skills/l-01-agent-lifecycles/roles/worker.md.md` | `skills/l-01-agent-lifecycles/roles/worker.md` | disabled | disabled | high | none | Source path is excluded by pathRules. |
