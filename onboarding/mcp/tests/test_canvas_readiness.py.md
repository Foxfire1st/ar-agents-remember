# mcp/tests/test_canvas_readiness.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The static readiness check: an admitted self-contained page is ready, a page that requests the network is not, a page that escapes its revision or names a missing asset is not, and an evidence reference must be one the packet carries.

## Code Commentary

- A network request disqualifies a page before it is offered as ready.
- An evidence reference the admitted packet does not carry disqualifies the page.


Readiness also derives a part map: claims require resolving bases and unique part ownership; `data-evidence-claim` carries actual claim IDs while `data-evidence` retains its separate basis-reference check. A page without explicit parts is one implicit `page` part containing its real claims, with whole-page staleness rather than invented part IDs.

## Evidence

- The case `test_a_page_that_requests_the_network_is_not_ready` protects this behaviour. [1]
- The case `test_an_evidence_reference_must_be_one_the_admitted_packet_carries` protects this behaviour. [2]

- Readiness also derives a part map: claims require resolving bases and unique part ownership; `data-evidence-claim` carries actual claim IDs while `data-evidence` retains its separate basis-reference check. A page without explicit parts is one implicit `page` part containing its real claims, with whole-page staleness rather than invented part IDs. [3]
