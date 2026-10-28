# mcp/src/agents_remember/application/review_frame_read.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Finite stored-byte reads for frame metadata and assets: reads one sentinel byte beyond the admitted size rather than the whole file followed by a size check, and refuses a descriptor population larger than the admitted revision.

## Code Commentary

`read_frame_bytes` refuses an oversized or growing stored file by measuring what it actually read, so a corrupt manifest of megabytes costs the admitted bound and no more. `validate_asset_read_bounds` checks the manifest's declared population and aggregate against the admitted revision before the store opens any asset payload, so modified metadata cannot authorize an over-cap read.

## Evidence

- Stored metadata and assets are read through a finite sentinel bound, not whole-then-check. [1]
- A modified manifest cannot authorize more assets than the admitted revision holds. 

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/review_frame_read.py::validate_asset_read_bounds - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 6df6b68c1b9714d360296e4cdeb978f5c22f7eea. Retired means the anchor no longer stands, not that the cited subject was deleted.
