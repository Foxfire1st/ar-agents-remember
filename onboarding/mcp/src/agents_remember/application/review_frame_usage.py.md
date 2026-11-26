# mcp/src/agents_remember/application/review_frame_usage.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

This module counts the physical bytes of an admitted frame lineage and task area.

## Code Commentary

Revision usage sums files in the revision directory, including metadata and any saved advisory inventory. Draft accounting adds recorded reserved bytes. Directory reads check confinement and refuse symlinked entries.

## Relationships

The frame store uses this accounting before promotion. The inventory writer uses the resulting budget when choosing a sidecar or omission marker.

## Evidence

- Revision usage counts the files stored under the admitted revision directory. [1]
