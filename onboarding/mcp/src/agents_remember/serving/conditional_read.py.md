# mcp/src/agents_remember/serving/conditional_read.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Share weak If-None-Match comparison across serving routes.

## Code Commentary

Callers supply the opaque current revision. The helper accepts wildcard or any comma-separated entity tag with the same opaque value, strips a weak prefix, and treats an absent header as a miss. It does not read a resource, mint a revision or decide whether a retained representation is current. Different callers may derive revisions differently; a projector content sequence is not the only possible producer.

## Evidence

- Comparison is shared and independent of representation discovery or generation validation. [1]
