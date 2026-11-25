# mcp/src/agents_remember/application/knowledge_names.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Project selected knowledge rows into names and openable record locations without changing the full application results used by the dashboard and CLI.

## Code Commentary

For `knowledge_read`, projection belongs at the agent transport boundary. The shared knowledge selection continues to serve full results to the dashboard and command line. `read_ar_files` assembles its own compact answer, including the current source file rules when its brief fits. Rows retain identity, record kind, source currentness and location. The projection adds recordState and a compact writer when available. Family membership names the member invariant and carries the family separately. Proof facets and record prose are not transported. Missing state evidence is not silently promoted to current.

A resolver lives for one answer. It binds the selection-time memory commit and dirtiness, rejects a moved commit, and shares record/index/sidecar and file-line caches between sizing and projection. Sidecar entry declarations outrank history mentions. Declaration lines are indexed once per file; a mark absent from that map retains the ordered fallback search, so this is not a constant-time guarantee for every possible mark.

Locations are memory-root-relative when the caller has the named worktree, otherwise absolute, with memory commit provenance. Card-section fallbacks are labelled rather than represented as exact heading resolution.

## Evidence

- The transport projection drops record text while retaining names and paging. [1]
- Selection provenance and cached lookup remain one-answer concerns. [2]
- Declared ID lines are indexed once; undeclared marks retain their fallback. [3]
- Membership and ordinary rows locate authoritative record or sidecar declarations. [4]

- The mounted source-context projection adds standing from the selected index. [5]
