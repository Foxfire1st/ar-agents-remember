# mcp/tests/test_tool_answer_table_rows.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The answer table's row gates and authored ownership cases (MIK-R108 rules 6 to 8): each failure mode fails its gate, and every row has the owner it claims.

## Code Commentary

`ToolAnswerRowGateTests` builds a shaped row and then breaks one thing at a time: a missing row, a field outside the row, a field with no stated use, an empty use, a use for an unknown field, a shaped row carrying an interim leaf, an interim row without one, a case over the row bound, a bound over twice the largest case, and a shaped row without case payloads. The positive controls are a valid shaped row and a production-proven row without payloads, which is allowed. Case-level gates reject an invalid code, a guard hit, and a field outside the row, and the replacement and short form paths are asserted where a case carries an invalid code or hits the guard. `ToolAnswerOwnershipTests` requires the implementation to match the authored roster, removed tools to have no row and no owner, and the exception rows to keep their stated ownership: `role_message` names its interim leaf while `server_info` stays the ownerless exception.

## Invariants And Boundaries

A row is authored, never synthesized: the ownership cases compare the implementation with the roster rather than with the registry. A production-proven row is the one shape allowed to omit case payloads, so the gate cannot be satisfied by deleting evidence.

## Evidence

### Repo-Internal References

- Each rule-6 failure mode fails its gate, and a production-proven row is the one shape allowed without case payloads. [1]

- Every authored row's owner matches the roster, and a removed tool has no row and no owner. [2]
