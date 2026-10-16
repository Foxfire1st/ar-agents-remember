# mcp/src/agents_remember/serving/_app_routes.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Register the retained projection reads, raw event stream, action acknowledgement/dismissal and developer direct-execution grant routes. No gate-decision or operator-inbox route is registered here.

## Code Commentary

A ready state response serves a copy of the memoized projection with its build tail, or bodyless 304 on a matching weak ETag; an unprimed projector refuses. Task-body reads use the runtime’s generation-validated body cache and revision ETag, not enclosure/lifecycle resolution: unprimed is 503, missing document 404, and 304 requires current observed dependencies as well as an ETag match. Raw-event SSE and snapshot/delta SSE retain distinct contracts. Pure action evaluation returns an optional dismissal intent; the router persists its published kind/fingerprint and returns `dismissal-not-held` 503 on OSError instead of success. Other accepted actions are acknowledgements, not product mutations; the separate developer-grant route keeps its admitted owner.

GET /api/diagnostics/background is a read-only view of the shared serving ledger, not projection mutation or acceptance. Event-tail accounting and watcher-health serialization retain their existing runtime owners; removed gate and inbox routes stay absent.

## Evidence boundary

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs

- [1]
- [2]
