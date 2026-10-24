# mcp/tests/tool_entry_point_world.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

The hermetic world the tool entry-point sweep runs in, and the classifier of its answers: one disposable
coordination root, one registered server and one MCP client session per call, with every public tool invoked once
and each outcome assigned to an arm. A call that does not return is a sweep deadline, never a product exception.

## Code Commentary

### Logic

`EntryPointWorld.call()` invokes one registered tool exactly as a consumer does and reads back what arrived;
`build()` authors the master and leaf and opens their real enclosure through the tools; `benign()` and `prepare()`
give the sweep its inputs (no per-tool ambient arrangement, so no tool is a function of ambient state alone);
`sweep()` invokes every public tool once in registration order and classifies each outcome; `census()`,
`coordination_census()`, `coordination_boundary()` and `repository_state()` observe what a read must not change.

- **Whole results.** `_read_whole_result()` reads the log-named whole result from the file the answer names, and a
  missing or unreadable file is an unvalidatable finding rather than a fallback.
- **Arms.** `_returned_arm()` validates the whole result under its model and judges the delivered answer,
  `_refusal_arm()` classifies `ok: false` from a delivered code and an actionable next, and `_raised_arm()` decides
  by which model refused. `classify()` is the one classifier the sweep and the controls share.
- **Shape.** `_judge_delivered()` checks shape, envelope, keys and `ok` in that order,
  `_unknown_delivered_path()` names a delivered key neither the whole result nor the shaping owns, and
  `_unknown_in_mapping()`, `_unknown_in_truncated()` and `_unknown_in_list()` do the same for a mapping, a
  truncated list and a retained list item.
- **Deadlines.** `_ToolCallTimeout` names the tool and the phase of a passed limit, outside the product-raiser
  classifier, and `SESSION_WAIT_SECONDS`/`TOOL_RESPONSE_WAIT_SECONDS` are the bounds.
- **Inventory.** `ARMS`, `REFUSED_MODEL`, `REFUSAL_IDENTITY_KEYS`, `NAVIGATION_KEYS`, `COORDINATION_WRITE_ZONES`,
  `KNOWN_MEMORY_SCAFFOLD_ADDITIONS` and `_TRUNCATED_LIST_KEYS` are the constants the classification and the
  boundary comparison read; the benign table carries the current roster keys.

### Conventions

A call is made through a real client session, and the answer is judged against the whole result it names — never
against the answer alone.

### Invariants And Boundaries

- A missing whole result is a finding, not a licence to judge the answer by itself.
- A reply arriving after the deadline is a named timeout, not a product refusal.

## Evidence

- The whole result is read back from the file the answer names, and a missing or unreadable file is an unvalidatable finding. [2]
- A returned call validates the whole result under its model and judges the delivered answer as delivered. [3]
- One shared classifier serves the sweep and the controls. [4]
- A passed phase limit names the tool and the phase, outside the product-raiser classifier. [5]
- The world obtains the guarded settings path before settings-parent creation and stub writing. [6]
- The returned-call arm reads the log-named whole result and delegates validation and delivered-answer judging. [8]
- The delivered-answer refusal arm classifies `ok: false` from the delivered code and actionable-next marks. [9]

- The shared benign table carries the 42 current roster keys; the earlier 41-key account is the base source before `user_settings_init` was added. Table membership is preparation, not registration or execution. [10]

- The shared world uses an object-form read refusal stimulus, delegates validation through its classifier helpers and records timeout continuation in its own sweep. [11]
- `build()` authors and starts the addressed enclosure without a session lifecycle option. [13]
- The shared sweep uses fixed fixture labels and preserves the named timeout continuation. [14]

- A fake-account child imports this worktree's world, receives the guard's refusal and leaves the fake configuration home empty — `test_building_the_world_with_the_users_own_environment_is_refused` in mcp/tests/test_user_settings_guard.py. [7]
