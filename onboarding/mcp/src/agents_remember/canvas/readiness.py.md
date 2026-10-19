# mcp/src/agents_remember/canvas/readiness.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The static readiness check a revision passes before it is offered as ready: it reads the exact bytes about to be published and refuses a page that names something it does not carry. It executes nothing and says so.

## Code Commentary

- `check_page` follows the document's own references, refusing a reference that leaves the revision and one that names no admitted asset.
- Motion and evidence-reference checks are separate named checks, so a failure names what it observed rather than asserting a verdict.
- `ReadinessReport.ready` is true only when no check failed, and `diagnostics` gives the presenter the failed checks with their observations.

## Evidence

- The static check refuses a page that names something its revision does not carry. [1]
- A report is ready only when no check failed. [2]
