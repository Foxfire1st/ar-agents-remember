# mcp/tests/test_canvas_readiness.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The static readiness check: an admitted self-contained page is ready, a page that requests the network is not, a page that escapes its revision or names a missing asset is not, and an evidence reference must be one the packet carries.

## Code Commentary

- A network request disqualifies a page before it is offered as ready.
- An evidence reference the admitted packet does not carry disqualifies the page.

## Evidence

- The case `test_a_page_that_requests_the_network_is_not_ready` protects this behaviour. [1]
- The case `test_an_evidence_reference_must_be_one_the_admitted_packet_carries` protects this behaviour. [2]
