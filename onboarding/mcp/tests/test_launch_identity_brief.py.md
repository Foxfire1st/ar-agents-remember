# mcp/tests/test_launch_identity_brief.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Unittest suite verifying that `brief_prompt` and `_compile_handover` place the `server_info` identity self-check paragraph in every role's opening brief preamble (between the AR-tools line and the first-read/handover sections) and that all three parent role authoring sources (`architect.md`, `orchestrator.md`, `manager.md`) carry the `IDENTITY MISMATCH:` recovery rule.

## Code Commentary

- Compiles canonical capsules from `skills/l-01-agent-lifecycles/composition-manifest.json` via `compile_admitted_capsule` and `routed_admission_for` against temporary task documents (`sprint/task.json`, `master/task.json`, `master/01_leaf.json`) with patched `build_context_packet`, `_read_task_doc`, and `task_scoped_mcp_config_for_reader`.
- `_assert_self_check_clauses` verifies all required clauses in `IDENTITY_SELF_CHECK_PARAGRAPH`: first-action `server_info` on `agents-remember-task`, comparison of `agentBinding` (`requestId`, `role`, task doc refs) against handover `requestId`, `role`, and `selection`, explicit warning that `host.parent.agentId` is the parent's id, no work/write/`role_message` on mismatch or missing server, and a single 300-character-capped `IDENTITY MISMATCH:` final line.
- Exercises all six roles (`architect`, `orchestrator`, `manager`, `worker`, `reviewer`, `curator`) via `_compile_handover`, checks preamble ordering and JSON handover projection fields, and verifies that the three parent roles' compiled prompts and canonical role source files each contain `EXPECTED_PARENT_RULE` with exactly one `IDENTITY MISMATCH:` occurrence.
- Registered in `mcp/tests/test-evidence-lanes.toml` (`unit-regression`) and `mcp/tests/evidence-lifecycle.toml`; source assertions only, not a live run record.

## Relationships

- **Code and docs under test:** `mcp/src/agents_remember/cli/role_brief_message.py` (`IDENTITY_SELF_CHECK_PARAGRAPH`, `brief_prompt`), `mcp/src/agents_remember/cli/role_launch_preparation.py` (`_compile_handover`), and `skills/l-01-agent-lifecycles/roles/{architect,orchestrator,manager}.md`.
- **Catalogs:** `mcp/tests/test-evidence-lanes.toml` and `mcp/tests/evidence-lifecycle.toml`.

## Evidence

- Verifies all `server_info` identity self-check clauses and exact preamble ordering in `brief_prompt` between the AR-tools paragraph and first-read/instructions/handover sections. [1]
- Compiles canonical capsules via `_compile_handover` for all six roles (`architect`, `orchestrator`, `manager`, `worker`, `reviewer`, `curator`), checking preamble placement, projection fields, and parent recovery rule. [2]
- Verifies `architect.md`, `orchestrator.md`, and `manager.md` each carry `EXPECTED_PARENT_RULE` with exactly one `IDENTITY MISMATCH:` occurrence. [3]
