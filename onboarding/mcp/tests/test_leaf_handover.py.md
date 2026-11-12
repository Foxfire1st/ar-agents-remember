# mcp/tests/test_leaf_handover.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

A leaf handover addresses its sibling seats without pinning their occupants: each leaf role receives the exact
sibling addresses of its two peers and no agent id, and a role or a context without a leaf receives no sibling
value at all.

## Code Commentary

### Logic

`handovers()` compiles a handover through `role_launch_preparation` from a `role_launch_context`, and the two
cases read the compiled answer.

- `test_leaf_roles_receive_exact_sibling_addresses_without_agent_ids` checks the addresses and the absence of
  any agent id.
- `test_other_roles_and_leafless_contexts_receive_no_sibling_value` keeps the value out of a non-leaf role and
  out of a context with no leaf.

### Conventions

The compiled handover is the assertion surface, so a value added to the context but dropped by compilation is
caught.

### Invariants And Boundaries

- A sibling is an address, never a seat: no agent id travels in a handover.

## Evidence

- The compiled handover carries the exact sibling addresses for each leaf role. [1]
