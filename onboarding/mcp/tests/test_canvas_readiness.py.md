# mcp/tests/test_canvas_readiness.py

## Governing Overview

[governing route overview](overview.md)

Static cases admit CSS motion and check actual HTML media elements for autoplay, loop and controls. Markup-like JavaScript text gains no static evidence authority.

## Purpose

The static readiness check: an admitted self-contained page is ready, a page that requests the network is not, a page that escapes its revision or names a missing asset is not, and an evidence reference must be one the packet carries.

## Code Commentary

- A network request disqualifies a page before it is offered as ready.
- An evidence reference the admitted packet does not carry disqualifies the page.


The part-map cases refuse missing or unresolvable bases, distinguish claim IDs from basis references, and observe one implicit part containing the real claims when the page declares no parts.

The media cases admit a controlled video, refuse actual autoplay or loop attributes or absent controls, and verify that filenames and other attribute values do not decide the result.

## Evidence

- The case `test_a_page_that_requests_the_network_is_not_ready` protects this behaviour. [1]
- The case `test_an_evidence_reference_must_be_one_the_admitted_packet_carries` protects this behaviour. [2]

- The tests check resolvable claim bases and the independent claim and basis attributes. [3]
- The video cases check actual controls, autoplay and loop attributes, including ordinary filenames. [4]
