# mcp/src/agents_remember/application/knowledge_names.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Project selected knowledge rows into names and openable record locations without changing the full application results used by the dashboard and CLI.

## Code Commentary

Projection belongs at the agent transport boundary, not in the shared knowledge selection. Rows retain identity, record kind, computed state and location; family membership names the member invariant and carries the family separately. Proof facets and record prose are not transported. Missing state evidence is not silently promoted to current.

A resolver lives for one answer. It binds the selection-time memory commit and dirtiness, rejects a moved commit, and shares record/index/sidecar and file-line caches between sizing and projection. Sidecar entry declarations outrank history mentions. Declaration lines are indexed once per file; a mark absent from that map retains the ordered fallback search, so this is not a constant-time guarantee for every possible mark.

Locations are memory-root-relative when the caller has the named worktree, otherwise absolute, with memory commit provenance. Card-section fallbacks are labelled rather than represented as exact heading resolution.

## Evidence

- The transport projection drops record text while retaining names and paging. [1]
- Selection provenance and cached lookup remain one-answer concerns. [2]
- Declared ID lines are indexed once; undeclared marks retain their fallback. [3]
- Membership and ordinary rows locate authoritative record or sidecar declarations. [4]
