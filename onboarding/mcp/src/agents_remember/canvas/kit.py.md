# mcp/src/agents_remember/canvas/kit.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The pinned offline kit the product ships. A page names a kit file by its path relative to its own revision; the revision must carry that file as an admitted asset, and the bytes are compared with the manifest when `kit_assets` carries them into an attempt, and that is the only check: nothing refuses a kit path afterwards, so a presenter may publish its own bytes there, and serving re-serves the revision's admitted assets as published. The kit is the presenter's offline toolbox, not a boundary.

## Code Commentary

- `kit_manifest` exposes each pinned entry with its identity, licence and files; `kit_files` indexes the shipped bytes by kit-relative path with their size and digest, which is what `_read_verified` compares before a byte is handed out.
- `kit_assets` returns the named files as revision assets under the contract path a page names them by, so the kit is served through the same admitted-asset route as the page's own files.
- `KitRefused` is raised for a file that is not shipped or whose bytes are not the manifest's,.

## Evidence

- The manifest is the kit's inventory and the verification source. [1]
- Kit files are served as revision assets under the manifest's contract path. [2]
