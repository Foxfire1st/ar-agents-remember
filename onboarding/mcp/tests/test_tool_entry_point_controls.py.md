# mcp/tests/test_tool_entry_point_controls.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Check the tool entry-point world's classifiers and its ability to complete a real tool call when a cross-thread socket wake-up is refused.

## Code Commentary

The negative controls drive invalid-input responses through the ordinary world's classifier. It marks a delivered answer with an envelope field as unvalidatable. It also marks a missing or unreadable whole-result file as unvalidatable and names the problem.

The corruption and deadline controls use the registered `server_info` route, patching public `self.world.server.call_tool` via `mock.patch.object` for the silent-handler timeout check. The retained-list control injects an undeclared key into a real `read_ar_files` result and checks the classifier names its indexed path.

The socket-denial control patches `socket.socket.send` to raise `EPERM` during an actual `server_info` call and requires a classified payload. It sets ten-second initialization and response budgets for that call.

The argument-versus-response validation control calls `citation_fix` with no `repo_id`: that required argument, not the now-optional contract, supplies the input-model refusal. The classifier must identify argument-validation rather than mistake it for a tool-response-model failure.

- The validation control omits required repo_id and asserts argument-validation, while contract_path is optional. [5]

## Evidence

- A delivered answer that keeps an envelope field is unvalidatable, each field on its own subTest. [2]

- An answer without a readable whole-result file is unvalidatable, and the detail says which. [3]

- A handler that goes round the choke point arrives as unvalidatable with its key named. [4]

- The retained handler deadline control patches public `self.world.server.call_tool`, names `server_info`, and checks cleanup plus the next call. [6]


- The retained-list control injects an undeclared key into a real `read_ar_files` list item and names its indexed path in the unvalidatable result. [7]

- A real tool call reaches a classified payload with socket send refused. [8]
