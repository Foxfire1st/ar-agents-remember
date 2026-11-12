# mcp/src/agents_remember/serving/review_summary.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Transport the small task-context changed-intent summary and optional numbered comparison through the app-owned conditional reader.

## Code Commentary

`register_review_summary_route` registers GET /api/review/intent/summary before the greedy static mount. It accepts repository/master/leaf and optional comparison. An unwired process returns named HTTP 503 instead of inventing zero counts.

With the port wired, a negative comparison receives a typed unavailable result with candidate_unresolved refusal, offending number and a next action naming a recorded comparison or omitting the number. This remains HTTP 200. Other requests pass their exact optional number to IntentSummaryCache; typed counted/partial/unavailable bodies use 200 and a matching conditional representation can be bodyless 304.

An unavailable body is an answered comparison limitation, unlike an absent summary collaborator. Other review routes retain their own refusal status behavior; treating an ordinary uninitialized leaf as a transport 404 would misstate that distinction.

## Invariants And Boundaries

Task context names no filesystem path. Counts, record resolution, cache admission and generation capture remain outside this transport. A negative or unrecorded comparison is unavailable, never a measured zero or a request for the latest live comparison.

## Evidence

- Wired/default/numbered transport and negative-number response preserve typed status behavior. [7]
- Negative numbers become a named unavailable comparison answer with no count. [8]
- Unwired is a named process-level failure rather than zero counts. [9]
