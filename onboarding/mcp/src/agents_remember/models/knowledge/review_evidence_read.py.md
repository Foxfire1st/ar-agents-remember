# mcp/src/agents_remember/models/knowledge/review_evidence_read.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The receipt shapes one bounded evidence read answers with: the side and tree actually read, the object and byte window examined, the returned range and its remainder, a relationship edge with its owner's semantics, a claim resolution, and a supplemental read.

## Code Commentary

`EvidenceReadReceipt` keeps apart the facts a reader must tell apart: the side and effective tree, the object's measured size, the returned range, the requested range, truncation and the limit that cut it, and the honest continuation. A shortened answer therefore never claims to be the whole source.
`RelationshipEdge` and `EvidenceRelationshipRead` record an edge the owner actually holds (`members` on a family, `links`/`supersedes` on a decision or invariant, `realizes`/`proves` on a sidecar, rows in a history file) with its direction, depth and cut; `ClaimResolution` says whether every basis resolves and why not, and `SupplementalRead` carries the bytes or the refusal.

## Evidence

- A read receipt states the side and tree read, the examined window, the returned range and every limit that shaped it. [1]
- A relationship read reports the edge its own owner records, with depth and cut. [2]
- A claim resolution is mechanical: each basis must resolve against the packet that cites it. [3]
