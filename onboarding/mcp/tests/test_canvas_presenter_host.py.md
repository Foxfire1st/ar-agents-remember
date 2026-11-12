# mcp/tests/test_canvas_presenter_host.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The confined host operations: a start authors a confined draft and persists the host receipt, the draft publishes through the confined writer, a turn reaches the host, and a resume keeps its identity across a restart.

## Code Commentary

- The draft is authored inside the prepared folder and nowhere else.
- A turn's receipt is recorded rather than invented, and resume keeps the recorded identity.


The host-operation cases use an explicit deterministic `LocalPresenterHarness`; named cases inject start-only or unconfigured runners. Production wires no presenter harness, and construction without a runner refuses. These facade/fixture assertions establish neither model authoring nor native-host execution.

## Evidence

- The case `test_start_authors_a_confined_draft_and_persists_the_host_receipt` protects this behaviour. 
- The case `test_a_turn_travels_to_the_host_and_its_receipt_is_recorded` protects this behaviour. [2]
- The case `test_resume_keeps_the_same_identity_across_a_restart` protects this behaviour. [3]

- The host-operation cases use an explicit deterministic `LocalPresenterHarness`; named cases inject start-only or unconfigured runners. Production wires no presenter harness, and construction without a runner refuses. These facade/fixture assertions establish neither model authoring nor native-host execution. [4]

- Retired at the fifth freeze d59c3493: mcp/tests/test_canvas_presenter_host.py::test_start_authors_a_confined_draft_and_persists_the_host_receipt - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976. Retired means the anchor no longer stands, not that the cited subject was deleted.
