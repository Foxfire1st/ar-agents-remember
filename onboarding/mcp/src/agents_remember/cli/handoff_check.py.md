# mcp/src/agents_remember/cli/handoff_check.py

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

New read-only whole-document checker resolves handoff targets against an explicitly named candidate.

## Code Commentary

The handoff-check CLI takes the list, required --code and --tree, and optional --memory. It resolves the named Git tree and uses read_handoff_shapes plus CodeSnapshot to check entry target/proof anchors, weakness anchors, dependent documents and stands_on links, history covers and repoints. With --memory it resolves stored record and entry links; missing or retired record links are reported. Without memory, record links and incomplete stored-entry covers report unchecked rather than passing. It prints every collected problem, returns 1 on problems, 2 for unreadable inputs, and 0 when these checks are clean. Fired links remain explicitly checked by the writer. It writes no knowledge and decides no Curator admission, invariant meaning or execution result.

## Evidence

- New read-only whole-document checker resolves handoff targets against an explicitly named candidate. [1]
