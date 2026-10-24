# mcp/tests/test_mik_r196_dashboard_address_truth.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Pins that the answer's dashboard address is published only when something serves it, and that an unserved origin is reported as a reason instead (L188-B24).

## Code Commentary

Each case monkeypatches the serving daemon's ensure and the address owner's origin probe, then calls the owner's address function for a config with the embed port. An address is answered only after the dashboard owner was asked and the origin answered HTTP 200. When the origin does not answer, the address is absent and the detail names the URL and the owner's outcome, so the answer carries the reason. A raising owner is reported the same way with the exception's name. A 503 page is the origin speaking and not serving, so it is not a continuation; and a failed owner is not published even when the port accepts a connection.

## Invariants And Boundaries

A dead pointer is never published as the address, and the detail always names both what was tried and what came back. The owner is asked before the address is answered, which the recording stub asserts by call.

## Evidence

### Repo-Internal References

- The address is answered only after the owner was asked and the origin answered. [1]

- An unserved origin, a 503 page and a failed owner are reported as reasons, never published as an address. [2]
