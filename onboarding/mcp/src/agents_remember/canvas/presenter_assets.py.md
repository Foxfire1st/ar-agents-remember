# mcp/src/agents_remember/canvas/presenter_assets.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Reads a prospective revision's assets through held directories, within its publication quota, so publication collects exactly the files the revision carries.

## Code Commentary

- `collect_assets` scans within `MAX_ASSET_DEPTH` and `MAX_WORKING_ENTRIES`, refusing work beyond the quota instead of truncating silently.

## Evidence

- Assets are collected through held directories within the publication quota. [1]
