# mcp/src/agents_remember/application/review_frame_read.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Finite stored-byte reads for frame metadata and assets: reads one sentinel byte beyond the admitted size rather than the whole file followed by a size check, and refuses a descriptor population larger than the admitted revision.

## Code Commentary

`read_frame_bytes` refuses an oversized or growing stored file by measuring what it actually read, so a corrupt manifest of megabytes costs the admitted bound and no more. `validate_asset_read_bounds` checks the manifest's declared population and aggregate against the admitted revision before the store opens any asset payload, so modified metadata cannot authorize an over-cap read.

## Evidence

- Stored metadata and assets are read through a finite sentinel bound, not whole-then-check. [1]
- A modified manifest cannot authorize more assets than the admitted revision holds. [2]
