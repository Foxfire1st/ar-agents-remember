# mcp/src/agents_remember/canvas/explainer_staging.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

This module stages the exact draft bytes for registered explainer publication.

## Code Commentary

A render can reuse an admitted draft or a request-owned staging directory. Active draft records protect their directories during cleanup. Browser-observed DOM and loaded assets supply advisory inventory, and the typed publication result identifies the revision to read back.

## Relationships

The explainer server runs readiness and load checks. The frame store owns durable promotion and revision identity.

## Evidence

- Request staging preserves active draft ownership during allocation and cleanup. [1]
