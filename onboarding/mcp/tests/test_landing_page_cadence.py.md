# mcp/tests/test_landing_page_cadence.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Protect server-owned landing interest and transient per-contract probe pacing through the composed runtime and controlled clocks.

## Code Commentary

The composed-runtime case activates two actual Projector subscriptions, permits probes while either remains and observes no additional probe after the final departure. The discovery-disconnect case revokes interest across the awaited discovery and asserts observation is not called. The clock case covers the 30/120/600/3600-second bands and semantic-answer reset. A two-population case covers rewritten/new/reopened/finished/removed contract state and schedule/observation reclamation.

## Invariants And Boundaries

These are in-process assertions with a real app/refresher/subscription composition and mocked remote observation/discovery seams. They do not prove native outbound calls, CPU budget, every disconnect race, rendered-page freshness or installation acceptance. Provider safety is deliberately a separate suite and is not stopped by landing disinterest.

## Evidence

- The suite owns composition, disconnect, age/reset and bounded-population assertions. [1]

- Composition binds the same landing instance to the Projector's real subscriber predicate. [2]
