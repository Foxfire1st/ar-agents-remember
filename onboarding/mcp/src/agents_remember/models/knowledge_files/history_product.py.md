# mcp/src/agents_remember/models/knowledge_files/history_product.py

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Defines the product-written evidence attached to history, including exact revision writes, crossing selections and the review fact.

The invariant title is display metadata. Its value is excluded from invariant meaning and crossing-selection digests, so a title-only edit leaves those identities stable.

## Evidence

- The semantic projection excludes derived attribution and the invariant title. Crossing selection also excludes the invariant title. [1]
- A written revision couples record identity, revision, writer and meaning evidence. [2]
- A review fact binds the accepted review round, verdict, tree and attribution. [3]
