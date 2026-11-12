# mcp/src/agents_remember/package_data/canvas/kit/manifest.json

## Governing Overview

[governing route overview](../../../../../overview.md)

## Purpose

The pinned kit's own inventory: for each library its version, licence and shipped files with size and digest, which is what `_read_verified` compares when a kit file is carried into an attempt; nothing refuses a kit path afterwards.

## Code Commentary

- Each entry names its pinned version and the licence text read for it, so a page's library is traceable to a licence.
- Every shipped file carries size and digest, and the host compares them through `kit_files`/`_read_verified` when a file is carried into an attempt; no later check refuses a kit path, so the manifest keeps the toolbox honest rather than bounding it.
- The manifest declares only what ships; it is not a package manager and loads nothing from the network.

## Evidence

- The manifest names each pinned library with version, licence and files. [1]
- Every shipped file carries its size and digest. [2]
