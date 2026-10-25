# mcp/tests/test_paseo_role_bridge.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Runs the bridge's `agent-send` and `agent-wait` commands as the real script against a scripted daemon
client, and proves an agent created by a role start is named to the runtime as its parent. Delivery is
judged only against a live agent with an open session: a running turn is steered when its provider
takes a steer and held otherwise, and a send that fails still says what is known of the delivery.

## Code Commentary

### Logic

The fixtures build the scenario pieces the runtime reports — `agent()`, `sent()`, `reply()`, `tool()`,
`ends()` for a turn that ends with the runtime's own event, and `begins()` for a turn starting with the
entries the runtime records — while `RoleBridgeScriptTestCase.call()` runs one command and `recorded()`
reports what the fake client was asked to do.

- **Send eligibility.** `AgentSendScriptTests` proves only a live agent with an open session is sent to,
  an agent waiting for a permission decision is not, and an idle agent starts a turn while a running turn
  is steered only into a provider known to take one — never cut off.
- **Attachments.** `test_images_and_text_attachments_go_with_the_message_only_when_given` sends native
  image and text attachments when they are given and leaves a send without them unchanged, and a
  malformed payload fails before any operation is recorded.
- **Resume ordering.** `test_a_send_after_a_resume_gives_the_tool_servers_their_time_first` waits out
  the tool servers a resumed session starts (`TOOL_SERVER_START_MS`) before sending.
- **Waits.** `AgentWaitScriptTests` reports a turn that ends during the call from the runtime's own
  event, one that ended before the call from the agent's state, gives an unnamed message time to begin
  its turn, refuses to attribute a later turn to the message, and reports a pending permission or a
  still-running turn as such. `SteeredWaitScriptTests` covers a message handed to a running turn: that
  turn or the next one consumes it.
- **Parent.** `test_the_starting_agent_is_named_to_the_runtime_as_the_parent` checks the created agent
  carries the starting agent's id as its parent.
- **Creation wire.** `R71CreationWireTests` proves creation sends mode and each feature before any
  prompt, that the profile bridge reads only the running host's configuration, and that the read grant
  uses exact server info while keeping mutators out.

### Conventions

Every case starts the real script against the scenario's runtime and asserts on the fake client's record
of calls as well as on the command's answer.

### Invariants And Boundaries

- A send never cuts off a running turn; it steers or holds.
- A failed send reports what is known of the delivery rather than claiming a clean refusal.

## Evidence


- Send eligibility, steering versus holding, attachment payloads, waits and parent naming run against the real script. [1]

- Native image and text attachments travel only when given, and a malformed payload fails before any recorded operation. [2]
