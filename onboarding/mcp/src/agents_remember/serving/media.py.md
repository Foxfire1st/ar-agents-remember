# mcp/src/agents_remember/serving/media.py

## Governing Overview

[overview](overview.md)

## Purpose

Defines the served picture/video types, byte bound and HTTP media response.

## Code Commentary

The fixed list covers PNG, JPEG, GIF, WebP, SVG, MP4 and WebM. The named limit is 16 MiB. Single byte ranges permit partial responses. Typed unsupported-media, oversized-source and invalid-range errors map to 415, 413 and 416. Successful media responses use no-store, nosniff and an inert content-security policy, including when an SVG URL is opened directly.

## Relationships

Source adapters supply measured bytes. The response adds no persistent media cache. File, notes, change-set and knowledge routes retain their own source-selection authority.

## Evidence

- Defines the served picture/video types, byte bound and HTTP media response. [1]
