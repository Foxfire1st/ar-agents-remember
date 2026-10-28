# mcp/tests/test_explainer_control.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The caller check, the record and the report move on the master-to-architect path: only the architect claims, only the seat the record names updates or retires, and a Manager start records the architect parent it actually has.

## Code Commentary

- An architect claim writes the record; another hosted caller is refused having written nothing.
- A claim moves one held report to the claiming seat, respects a provider limit or timeout, falls back to the tray on an unavailable destination, and restores custody when no report file exists.
- Update and Retire name the seat the record holds; another seat, or no record at all, is refused as a claim.
- Both seat actions reach the real seat service through the registered tool, and a path receipt id is refused at that boundary.
- A Manager start records the architect parent it has and writes nothing when it has none.

## Evidence

- The case `test_an_architect_claim_writes_the_record` protects the architect's claim writing the record. [1]
- The case `test_a_non_architect_claim_is_refused_and_writes_nothing` protects a non-architect claim being refused without a write. [2]
- The case `test_a_claim_moves_one_held_report_to_the_claiming_seat` protects a claim moving exactly one held report to the claiming seat. 
- The case `test_update_by_another_seat_is_refused_and_names_claim` protects an Update from a seat the record does not name being refused as a claim. [4]
- The case `test_update_and_retire_reach_the_real_seat_service` protects both seat actions reaching the composed seat service. [5]
- The case `test_a_path_receipt_id_is_refused_at_the_tool_boundary_and_leaves_outside_bytes` protects a path receipt id being refused at the tool boundary with no outside write. [6]

- Retired at the fifth freeze d59c3493: mcp/tests/test_explainer_control.py::test_a_claim_moves_one_held_report_to_the_claiming_seat - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
