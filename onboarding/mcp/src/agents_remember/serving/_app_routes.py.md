# mcp/src/agents_remember/serving/_app_routes.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Register the retained projection reads, review-aware projection stream, raw event stream, action acknowledgement/dismissal and developer direct-execution grant routes. No gate-decision or operator-inbox route is registered here.

## Code Commentary

The review stream multiplexes projection/memory invalidation with moved notices. _merged_stream lets notice exhaustion leave the page stream alive and ordinary stream exhaustion close it; finally cancels/gathers pending next-event tasks and aclosing releases subscriptions.

A ready state response serves a copy of the memoized projection with its build tail, or bodyless 304 on a matching weak ETag; an unprimed projector refuses. Task-body reads use the runtime’s generation-validated body cache and revision ETag, not enclosure/lifecycle resolution: unprimed is 503, missing document 404, and 304 requires current observed dependencies as well as an ETag match. Raw-event SSE remains separate from the ordinary state snapshot/delta stream. The state stream now optionally carries review-memory invalidations on the same connection: only all-omitted `reviewRepo`/`reviewMaster`/`reviewLeaf` selects no identity; any supplied component forms a three-string tuple with missing/empty components normalized to empty strings. This normalization is not authentication or full selector admission. `multiplex_review_memory` owns selector/root checks, emits revision invalidations or explicit error events, and keeps the ordinary events distinct. The route iterates that multiplexer under `contextlib.aclosing`; the helper owns its streams/tasks and the native watcher owns its handles. These source cleanup paths are not an observed runtime cleanup certificate. Pure action evaluation returns an optional dismissal intent; the router persists its published kind/fingerprint and returns `dismissal-not-held` 503 on OSError instead of success. Other accepted actions are acknowledgements, not product mutations; the separate developer-grant route keeps its admitted owner.

GET /api/diagnostics/background is a read-only view of the shared serving ledger, not projection mutation or acceptance. Event-tail accounting and watcher-health serialization retain their existing runtime owners; removed gate and inbox routes stay absent.

## Evidence boundary

This is current-source interpretation of the admitted frozen candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs


- The state response uses projector revision weak ETags, refuses an absent snapshot, returns bodyless 304 on a match, otherwise copies the memoized projection and adds the served-state tail. [1]


- The state SSE route passes ordinary snapshot/delta events through the optional review-memory multiplexer under aclosing; the distinct raw-event route still forwards observer records and its own ready marker. [2]


- All omitted review selectors opt out; any supplied selector forms a normalized three-string identity for the resolver. The multiplexer—not normalization—checks segments/root admission, emits review.memory.error on admitted failure paths and keeps ordinary events flowing. [3]

- The review stream multiplexes projection/memory invalidation with moved notices. _merged_stream lets notice exhaustion leave the page stream alive and ordinary stream exhaustion close it; finally cancels/gathers pending next-event tasks and aclosing releases subscriptions. [4]
