# mcp/tests/role_first_message_support.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Builds one real first message through the product's own start path and holds the checks the first-message cases drive (MIK-R193 rules 1, 3, 5, 6 and 7).

## Code Commentary

`FirstMessageMatrixBase` writes the settings, the task documents and the launch context for a role and harness, starts the seat through the launch route (held or not), and reads back the prompt the host was handed. `check_message` applies the rule checks; `check_nothing_twice` finds repeated passages other than the ones allowed to repeat; `check_projected_values` compares every projected field with the hand-over object's own value rather than with the projector's output; `check_reachable` and `_unreachable` accept a name only when it starts at a field the hand-over object has; `check_paths` and `_missing_paths` read every absolute path the message emits, whole, including a backticked or quoted span that holds a space. The pure helpers are the projection reader, the message key, the forty-word window counter, the code-font name reader, the dotted-path lookup, the value and path collectors, and `_may_repeat`, which exempts absolute paths and task-document references from the repeat rule. `_check_paths_at_send` records the check at the send boundary.

## Invariants And Boundaries

The checks run on the message the host was given, not on a copy read back afterwards, and a launch with no snapshot is refused rather than read as clean. A held seat has no send until its delivery, which is why the snapshot expectation is per seat and not global. `FIXTURE_HARNESSES` extends the known harness ids with `hermes`.

## Evidence

### Repo-Internal References

- The matrix builds the real first message for every allowed role and harness through the launch route. [1]

- Path and reachability checks read delimited spans whole and run at the send boundary. [2]

- Only absolute paths and task-document references are allowed to stand in two places. [3]
