# mcp/tests/test_paseo_launch.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Runs the role-launch dispatch route against a fake bridge, with capsule compilation stubbed and the
rest real: request shaping, refusals, the receipt, the execution's answer and the leaf enclosure the
launch records. Two module-level cases also prove what a role tool definition carries — the product
XDG homes and the place of the user settings — without starting anything.

## Code Commentary

### Logic

`PaseoLaunchTestCase` wires the shared fake runtime (`FakeRuntime`, `CATALOG`, `SERVER_ID` from
`paseo_launch_test_support`) into the catalog, launch and status bridge calls, stubs `_role_defaults`
with `ROLE_DEFAULTS`, compiles its own handover, and exposes `request()`, `dispatch()`, `refused()`,
`receipt_path()`, `receipt()`, `agent_of()`, `refresh()` and `close_execution()`. `FakeEnclosures`
stands in for AR's worktree status and start of one leaf, and `record_enclosure_in_leaf()` writes what a
real start leaves in the task document.

- **Refusal is free of effects.** `LaunchRefusalTests.test_a_launch_that_cannot_start_refuses_before_any_runtime_call_or_receipt`
  checks the refusal arrives with no launch call (no workspace opened, no agent created or archived) and no receipt
  file. Selection validation and an attempted leaf-enclosure start are checked separately from those
  launch calls; an unanswered catalog alone is not treated as a launch refusal.
- **Unanswered catalog.** `test_an_unanswered_catalog_passes_configured_choices_to_the_host`
  requests `metadata` and then `selected` data for `gpt-a`, opens the workspace and creates one agent
  with the configured `codex`/`gpt-a`/`low` choices. It records one enclosure start and a running receipt.
- **Feature values are merged, never clobbered.** `LaunchFeatureValuesTests` shows a service tier merged
  into accepted feature values, feature values passing through untouched when no tier is asked for, and a
  tier alone setting only its own key.
- **Tool definition.** `test_role_tool_definition_carries_product_xdg_homes_without_starting` and
  `test_role_tool_definition_carries_the_place_of_the_user_settings` pin the environment and the settings
  path an agent's tool server must inherit from its launching process.
- **No-answer codes.** `NO_ANSWER_CODES` names the reply codes that do not count as an answer, so a reply
  is never read as a started seat by accident.

### Conventions

Cases use `SPRINT_REF`, `MASTER_REF` and `LEAF_REF` task-document references under a temporary
coordination root and read the receipt from the path the route reports.

### Invariants And Boundaries

- A refused launch leaves no launch call (no workspace opened, no agent created or archived) and no receipt behind.
- The bridge is fake here; nothing starts a daemon, and the capsule body comes from the case's stub.

## Bounded locator at any report depth

`DeepLaunchFolderTests` compiles one launch at a shallow report folder and another under a deeply nested one. At both depths the stored artifact is beside its report under its own name and mode `0444`, the reference's `path` is the request's locator, the note stays within `RECOVERY_NOTE_LIMIT` and names the locator with the artifact's SHA-256, and the first message's first line names the same pair; the two notes are one length once the role is set aside, and the two locator paths are equally long while the deep artifact's own path is at least 318 characters. A further case plants a locator that leads to another folder and finds the launch refused with a 409 before it starts: no runtime call, no receipt, nothing written in the foreign folder, and the alias unchanged.

The fixture now gives the process a short temporary home of its own, as a real account has, because each launch keeps its locator under it. `RoleFolderAndIdentityTests` reads that home after the launch census and finds one locator symlink per request and no file at all, with no harness configuration there.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]

- The launch fixture now imports `FakeRuntime`, `CATALOG` and `SERVER_ID` from `paseo_launch_test_support`; `CATALOG` remains exported for suites built on this fixture. `PaseoLaunchTestCase.setUp` wires the shared fake into catalog/launch/status bridge calls. This is fixture-owner relocation, not a change to launch identity, retry or holder-replacement semantics. [2]
