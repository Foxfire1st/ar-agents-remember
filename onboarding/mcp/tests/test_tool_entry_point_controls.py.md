# mcp/tests/test_tool_entry_point_controls.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Tests for tool entry-point controls.

## Code Commentary

The tests drive the invalid-input responses of the registered tool entry points. Every control keeps its red case through the world's single classifier, including the two MIK-R130 controls: a delivered answer that still carries an envelope field is unvalidatable, and an answer whose whole-result file is missing or unreadable is unvalidatable with the situation named — never a fallback to the delivered answer.

The argument-versus-response validation control calls `citation_fix` with no `repo_id`: that required argument, not the now-optional contract, supplies the input-model refusal. The classifier must identify argument-validation rather than mistake it for a tool-response-model failure.

- The validation control omits required repo_id and asserts argument-validation, while contract_path is optional. [5]

## Evidence

- A delivered answer that keeps an envelope field is unvalidatable, each field on its own subTest. [2]
- An answer without a readable whole-result file is unvalidatable, and the detail says which. [3]
- A handler that goes round the choke point arrives as unvalidatable with its key named. [4]
