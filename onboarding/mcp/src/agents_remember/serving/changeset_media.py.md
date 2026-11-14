# mcp/src/agents_remember/serving/changeset_media.py

## Governing Overview

[overview](overview.md)

## Purpose

Resolves a change set's before or after media source from its existing range selectors.

## Code Commentary

Comparison, leaf, master and enclosure requests resolve their selected side on the server. Side, kind, mode and supplied generation pins are checked before selector resolution. Historical paths are checked lexically before reading the selected object, rather than following today's filesystem symlinks.

## Relationships

The shared media reader supplies types, byte bounds, ranges and response headers. This resolver adds no client-selected commit shortcut or bytes cache.

## Evidence

- Resolves a change set's before or after media source from its existing range selectors. [1]
