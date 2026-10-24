# mcp/tests/test_paseo_launch_repeat.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers what a second call to the role launch does: a repeat answered from its receipt, a replaced or
losing execution, a reused request id, workspace placement shared by a role's seats, and the runtime
reply that must name the minted agent and its server. Every case runs the real dispatch route against
the fake bridge, with a capsule the case can change.

## Code Commentary

### Logic

`RepeatTestCase` extends the launch fixture with a capsule that can change and a count of compilations:
`change_what_a_launch_is_compiled_from()` edits every selected task document, the capsule and the first
message, `launch_that_stays_starting()` leaves a receipt whose process has ended, and `free_seat_for()`,
`successor_note()` and `seat_predecessor()` exercise the used-seat rule, while `binding_files()` and
`binding_bytes()` observe the per-seat binding directory.

- **Repeats.** `test_a_repeat_is_answered_from_its_receipt_whatever_changed_since_the_launch` and the
  `ServiceTierReplayTests` cases prove a repeat keeps the first profile choices after the host role or
  the catalog changed, and that a still-loading catalog refuses before an agent or workspace exists.
- **Replaced executions.** `ReplacedExecutionTests` archives the agent of the newest archived receipt
  when a start arrives without one, closes a launch whose agent cannot be opened before its first
  message, and proves a losing launch takes back the binding file it created but leaves a file that is
  not its own alone.
- **Reused request ids.** `ReusedRequestIdTests` refuses an id of an archived execution, an id bound to
  another selection, and a binding file that does not record the selection — each before an enclosure is
  created.
- **Runtime replies.** `RuntimeReplyTests` refuses a reply that does not name the minted agent and the
  server, names the workspace the agent is in, resolves the folder and cuts the title at the runtime's
  limit, and derives `canStart` from whether the task-bound execution is open.
- **Workspace placement.** `WorkspacePlacementTests` proves a role's seats share one task workspace and
  its saved placement, and that a persisted-`cwd`-only launch is replayed without new placement.

### Conventions

Each case drives the route through the fixture's request/dispatch helpers and asserts on the receipt
file and the fake runtime's record of the agent, never on internal call order alone.

### Invariants And Boundaries

- A repeat never recompiles a capsule or creates a second agent.
- A request id belongs to one selection; a binding file a launch did not create is never touched.

## Evidence

- Repeats, replaced executions, reused request ids, runtime replies, workspace placement and service-tier replay are asserted against the fake bridge. [1]
