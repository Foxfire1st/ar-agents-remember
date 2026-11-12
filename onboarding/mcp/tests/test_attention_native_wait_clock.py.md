# mcp/tests/test_attention_native_wait_clock.py

## Governing Overview

[overview](overview.md)

## Purpose

The test proves that the native attention reader's stall clock leaves a task alone while one of its seats holds a declared wait whose check is still to come, and starts the clock once that check has passed.

## Code Commentary

One case builds a host snapshot with a single idle Worker seat whose `declaredWait` waits for `background` with its check due three minutes after the seat's last event. It builds the task entries with `build_task_entries` and reads the native attention input through the reader that `ProjectionInputState` holds, at a chosen instant each time.

One minute after the event the task's activity is `waiting` and the reader keeps no stall clock. Two minutes after the check is due, past the 60-second `WAIT_CHECK_GRACE`, the task's activity is `paused` and the stall clock for the task starts at that read instant.

## Relationships

The task state and the stall watch both read `agent_waits` in `mcp/src/agents_remember/observer/task_entries.py`; `NativeAttentionInput._read_stall_clocks` in `mcp/src/agents_remember/serving/projections/native_attention.py` counts a seat that waits as busy. The case reuses the publication and task fixtures of `test_attention_native_inputs.py` and the runtime configuration of `test_paseo_role_agents.py`.

## Evidence

- The seat's declared wait has its check due three minutes after its last event. [1]
- While the check is to come the task reads `waiting` and no stall clock is kept. [2]
- After the check has passed the task reads `paused` and the clock starts at the read instant. [3]
- A declared wait counts only until its check time plus a 60-second grace. [4]
- The stall watch treats a seat that works or waits as busy. [5]
