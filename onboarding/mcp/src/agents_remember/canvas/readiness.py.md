# mcp/src/agents_remember/canvas/readiness.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The static readiness check a revision passes before it is offered as ready: it reads the exact bytes about to be published and refuses a page that names something it does not carry. It executes nothing and says so.

## Code Commentary

- `check_page` follows the document's own references, refusing a reference that leaves the revision and one that names no admitted asset.
- Motion and evidence-reference checks are separate named checks, so a failure names what it observed rather than asserting a verdict.
- `ReadinessReport.ready` is true only when no check failed, and `diagnostics` gives the presenter the failed checks with their observations.

`_check_parts` derives the product’s static map from `data-part` and `data-evidence-claim`: nested claims belong to the innermost part, part ids obey the shared grammar, and invalid/reserved/duplicate ids, unknown or unmapped claims and unresolved claim bases fail readiness. A page declaring no parts has one implicit whole-page part. The report carries the admitted map for publication; the explainer never supplies a separate map.

## Evidence

- The static check refuses a page that names something its revision does not carry. [1]
- A report is ready only when no check failed. [2]

- The current implementation adds part-map and claim-basis checks to static readiness and returns that derived map for retained publication. [3]
