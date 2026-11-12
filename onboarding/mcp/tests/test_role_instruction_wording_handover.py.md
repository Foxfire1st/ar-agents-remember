# mcp/tests/test_role_instruction_wording_handover.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

What a launched role is told: the handover text the launch builds in code, and the role tool descriptions, neither of which may name a forbidden host string.

## Code Commentary

The fixture compiles a role's capsule and builds the handover for taskless, sprint, master and leaf selections admitted by the production resolver, isolating only the task-reader and enclosure plumbing: no launch, model or lifecycle operation runs. The cases require the developer question channel to match the role and its parent, the owner relation to route developer questions and preserve coordinators, and the first message to name no forbidden host string. The reader context must name the readers of the task tool server, the handover must name that server, its two tools and the host, and a role without a parent must be told it needs none while a started role is told who started it. The description cases hold the three role-tool descriptions to the same forbidden list.

## Invariants And Boundaries

The forbidden search is the shared case-folded literal-substring matcher over the whole text: each entry must appear as one contiguous run of characters, so a spelling broken across a line is not matched. The text checked is the compiled capsule and the built handover, not a template source.

The compact role_message description stays within 600 characters and states the host mid-turn promise, queued held delivery and no resend of held messages. Host acceptance or consuming-turn completion is distinct from AR acceptance; the source check remains separate from live message delivery. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
### Repo-Internal References

- The handover names the tool server, its two tools and the host, and tells a parentless role it needs none. [Past-epoch source caption, detached from live reference 1. Recorded citation custody: mcp/tests/test_role_instruction_wording_handover.py blob d26f7a71fe3a996c2c34acccc3af29f5d88d16a3 (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The handover test asserts Paseo and agents-remember-task host fields, the role_start/role_message tool names, scoped reader-discovery instructions and held/permission wording. The parentless control requires no invented parent; a started role records its actual starter and role/task return address.

- No first message and none of the three tool descriptions names a forbidden host string. [Past-epoch source caption, detached from live reference 2. Recorded citation custody: mcp/tests/test_role_instruction_wording_handover.py blob d26f7a71fe3a996c2c34acccc3af29f5d88d16a3 (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The first-message control rejects forbidden host strings across generated role prompts. The description control checks three role-agent tool descriptions—role_start, role_message and role_start_set—and separately checks user_settings_init; no stored description or first-message assertion proves host delivery.

- The handover test asserts Paseo and agents-remember-task host fields, the role_start/role_message tool names, scoped reader-discovery instructions and held/permission wording. The parentless control requires no invented parent; a started role records its actual starter and role/task return address. [1]
- The first-message control rejects forbidden host strings across generated role prompts. The description control checks three role-agent tool descriptions—role_start, role_message and role_start_set—and separately checks user_settings_init; no stored description or first-message assertion proves host delivery. [2]

- The compact role_message description stays within 600 characters and states the host mid-turn promise, queued held delivery and no resend of held messages. Host acceptance or consuming-turn completion is distinct from AR acceptance; the source check remains separate from live message delivery. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [3]
