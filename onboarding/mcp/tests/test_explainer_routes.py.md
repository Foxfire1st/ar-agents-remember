# mcp/tests/test_explainer_routes.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The page's routes answer what a page cannot recompute: the trusted list of the revision it shows, the moved notice as the watcher gave it, a plan for a planning leaf only, the developer's own removal, and an Update's counts.

## Code Commentary

- The state route's trusted list is the host's own read of the shown revision, and a failure to read staleness is named instead of reported as nothing stale.
- The notice the page carries is the watcher's own record passed through unchanged; a watcher that cannot tell contributes nothing.
- The planned route serves a planning leaf its plan and refuses another leaf, and the removal route never removes the pinned agreed revision.
- Reads start nothing, and a stale comparison number or an unknown history is refused before any seat is reached.
- The revision list and the state read past the old display ceiling, because no display constant decides what the store holds.


The cancel route forwards the exact seat/request pair from the leaf ledger, reports stopped-turn and prevented-publication facts from its host reply, marks a request the ledger never saw uncertain, and rejects a missing request ID. This fixture-level route assertion does not certify a live host cancellation.

## Evidence

- The case `test_the_state_route_answers_the_trusted_list_of_the_page_it_shows` protects the trusted list being the host's read of the shown revision. [1]
- The case `test_the_state_route_names_why_it_could_not_read_staleness` protects an unreadable staleness being named, never reported as nothing stale. [2]
- The case `test_the_planned_route_answers_a_planning_leaf_and_refuses_another` protects the planned route serving a planning leaf and refusing any other. [3]
- The case `test_the_removal_route_removes_and_never_the_pinned_revision` protects the developer's removal refusing the pinned revision by name. [4]
- The case `test_the_reads_start_nothing` protects a page read opening, building and waking nothing. [5]
- The case `test_a_stale_comparison_number_and_an_unknown_history_are_refused_before_the_seat` protects a stale comparison number and unknown history being refused before the seat. [6]

- The cancel route forwards the exact seat/request pair from the leaf ledger, reports stopped-turn and prevented-publication facts from its host reply, marks a request the ledger never saw uncertain, and rejects a missing request ID. This fixture-level route assertion does not certify a live host cancellation. [7]


