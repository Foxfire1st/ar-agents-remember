# mcp/tests/test_master_retirement_state_machine.py

## Governing Overview

[tests overview](overview.md)

## Purpose

The retire operation as one state machine: every state is read from disk, never from the route. One case kills the operation at every transition, with a sprint and without one, and then asks the same four things of the state it left: does the sprint still resolve every master it names, is there at most one retirement record, is every other request refused without a change, and does the same request complete.

## Code Commentary

`_kill` drives a death at each seam and `_refused_without_change` checks that a refusal changed nothing; `_damages` renders the four ways a sprint document can be made unreadable. The cases also cover a half-written sprint pair, a master attached again between attempts, a lone master a sprint commands now, a folder that never moves from under a sprint, a repeated request that writes no second record, a sprint that lost its last master, the restart notice, a dry run after a partial cleanup, and a missing master.

## Evidence

- A death at any transition leaves a state the same request completes, with the sprint still resolving every master it names and at most one record. [1]
- Every other request against the state a death left is refused without a change. [2]
- A dry run after a partial cleanup lists exactly what remains. [3]
