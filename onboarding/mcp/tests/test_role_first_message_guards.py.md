# mcp/tests/test_role_first_message_guards.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The negative controls of the first-message checks themselves (MIK-R193 rules 1, 6 and 7): each case fails the check under test when that check is blind.

## Code Commentary

The repeat control admits only the bootstrap role and operation pair holding one value twice, and raises for a pair that adds a task or names another role. The reachability oracle answers for a file-only root, an indexed path through the projected documents list, and a name that starts no field of the hand-over object; it reports a field the object does not have under either root, so a check that only recognised projected roots would fail here. The path control writes a real file at the prefix of a backticked path whose complete text does not exist, and requires the whole path to be reported rather than its prefix accepted; the same check is then shown running on the message handed to the host, and a launch with no snapshot is refused rather than read as clean. A held delivery is checked against the snapshot of the actual send: an opening whose waiting work names a missing path fails, and the same opening delivered cleanly passes, which keeps the control negative. The held-seat case drives the real opener for every leaf role and harness, takes one message into the store, and requires the delivered turn to begin with the saved opening with the waiting work standing once.

## Invariants And Boundaries

A control fails the check when the check is blind, so a passing control is evidence about the check and not about the product. `FIXTURE_HARNESSES` and `LEAF_ROLES` set the matrix, whose built count is asserted at the end so a skipped combination cannot pass as a clean run.

## Evidence

### Repo-Internal References

- Only the admitted bootstrap pair may hold one value twice, and the control fails every other pair. [1]

- The path check reads a whitespace-bearing path whole and runs on the message the host was handed. [2]

- A held seat opens through the real delivery path, and the delivered turn begins with its saved opening. [3]
