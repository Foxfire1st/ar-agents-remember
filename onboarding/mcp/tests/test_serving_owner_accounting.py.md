# mcp/tests/test_serving_owner_accounting.py

## Governing Overview

[governing overview](overview.md)

## Purpose

F01/F02: exact thread CPU through the actual recurring owner callers.

## Code Commentary

The suite checks every recurring caller attributes each stage and drains repeated cancel. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

The controlled runtime fixture supplies `usage_read=None`, matching the real `_ServingRuntime` default. The held-delivery loop can then reach its accounted tick instead of raising on a missing fixture attribute before any stage runs. Success, per-stage failure and repeated-cancellation assertions remain the same.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence



- The controlled recurring-owner proof supplies the optional usage port [2]

- F01/F02: exact thread CPU through the actual recurring owner callers. [1]
