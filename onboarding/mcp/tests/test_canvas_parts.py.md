# mcp/tests/test_canvas_parts.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The page's part map and the operations that read it: the innermost containing element owns a claim, a part id no reader may be told to mark is refused, and neither operation carries anything the protocol does not admit.

## Code Commentary

- Element nesting, not the most recent close tag, decides a claim's part — including voids, repeated tags, and an element that is both a part and a claim.
- Readiness may name only a part the map admits; a claim outside every part is a problem, while a page with no parts is one part.
- An offer is bounded and carries plain text verbatim, and one outside its bounds is refused by name.
- `stale-parts` drops ids the revision does not hold and keeps the true count, and a host message is bound to its own frame.

## Evidence

- The case `test_a_claim_belongs_to_the_innermost_part` protects a claim belonging to the innermost part that contains it. [1]
- The case `test_static_dom_containment_decides_every_part_boundary` protects nesting deciding every part boundary, matched closes only. [2]
- The case `test_readiness_reads_a_claim_id_and_refuses_a_basis_reference` protects readiness reading a claim id and refusing a basis reference. [3]
- The case `test_an_offer_outside_its_bounds_is_refused_by_name` protects an out-of-bounds offer being refused by name. [4]
- The case `test_stale_parts_drops_unknown_ids_and_keeps_the_true_count` protects unknown ids being dropped while the count stays true. [5]
- The case `test_a_host_message_round_trips_and_is_bound_to_its_own_frame` protects a host message round-tripping only within its own frame. [6]
