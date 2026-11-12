# mcp/src/agents_remember/worktrees/modules/state_refusals.py

## Governing Overview

[Worktree modules overview](overview.md)

## Purpose

Build task-state refusal results and preserve caller-owned checks, rather than deciding transaction eligibility.

## Code Commentary

`state_refusal_result` returns a nonzero command result with the supplied state, code and unchanged sentence. An optional `RefusalNext` carries either the existing tool name and argument mapping, or a non-server command as separate `argv` values. The latter becomes `nextStep.nextArgs` plus a `command` made from those same values with `shlex.join`; no server tool is invented and paths are never concatenated into an unquoted command. With no next step, no successor is fabricated. Provider and handover helpers retain their existing facts; series queue errors offer a call only for the recognized completed/abandoned-master cases.

`terminal_state_refusal` recognizes a finite message set and returns `None` for an unrecognized failure so the caller can raise. This module is not proof that every reachable prewrite exception has been converted. task_stage_refusal separately returns blocked/task-stage-invalid with the original binding error and repair-the-named-document/parent-row prose, not a fabricated mutation tool. Integration conversion preserves the check's sentence and distinguishes incomplete closeout from other integration preconditions.

The shared terminal-blocker formatter retains producer fields and adds coded sentences. Its dirty/unmerged sentences mention force; that wording does not add a force input to cleanup or waive its preflight, which calls with force false. Recovery authority belongs to the actual route, not to this presentation helper.

handover_gate_blocked preserves the existing master-handover refusal code, gate ID, reason and coded blocker, while stripping inherited nextTool, nextArgs and nextRequiredArgs. Its blocker names STORED_GATE_WAY_OUT: no product tool decides a stored gate; agents-remember removed-stores names the log and removes it only on the user’s word. Dry/real refusals retain their distinction from success and no approval is fabricated.

## Evidence

- The constructor preserves the producer sentence and carries tool arguments or separate CLI values with a correctly quoted display. [1]

- Terminal conversion is a recognized-message mapping with an unrecognized fallback. [2]


- Shared blocker sentences preserve producer fields and add the dirty/unmerged force wording without changing a caller. [3]

- Cleanup calls terminal preflight with force false; formatter prose supplies no override to that route. [4]


- handover_gate_blocked preserves the existing master-handover refusal code, gate ID, reason and coded blocker, while stripping inherited nextTool, nextArgs and nextRequiredArgs. Its blocker names STORED_GATE_WAY_OUT: no product tool decides a stored gate; agents-remember removed-stores names the log and removes it only on the user’s word. Dry/real refusals retain their distinction from success and no approval is fabricated. [5]

## Current source evidence


- Invalid task/parent stage binding returns a blocked named refusal without a fabricated mutating recovery tool. [6]
