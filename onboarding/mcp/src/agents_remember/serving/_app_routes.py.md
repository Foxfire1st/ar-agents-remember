# mcp/src/agents_remember/serving/_app_routes.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Register the retained projection reads, raw event stream, action acknowledgement/dismissal and developer direct-execution grant routes. No gate-decision or operator-inbox route is registered here.

## Code Commentary

A ready state response serves a copy of the memoized projection with its build tail, while a matching weak ETag returns a bodyless 304; an unprimed projector refuses. The task-document route resolves against the current enclosures and distinguishes unavailable projection from missing document. Snapshot SSE and raw-event SSE have different payload contracts. Action evaluation is pure: only a returned dismissal intent is durably applied to AttentionDismissalStore; other accepted actions are acknowledged, not mutations. The separate developer-grant endpoint delegates to its admitted grant owner.

## Evidence boundary

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs

- [1]
- [2]

