# docs/features.md

## Governing Overview

[Repository overview](../overview.md)

## Purpose

Tours Agents Remember's product capabilities—mirrored cards, sidecars, knowledge records, anchor currentness and commit attribution, isolated worktrees, derived knowledge index, role agents and Paseo host, dashboard, review page/explainer, direct execution, MCP tool server, repository `system/` instructions, and operational guardrails—linking to each dedicated reference page.

## Code Commentary

- Distinguishes reference-anchor currentness (blob and content identity, `stale:blob`) from realization/proof currentness (`current`/`stale`/`unverifiable`) and invariant states (`current`/`stale`/`unverifiable`/`unrealized`).
- Documents `read_ar_files` brief-to-compact row degradation and names-only `knowledge_read`, alongside per-build/tree SQLite knowledge-index caching and eviction (14 days / 1 GiB).
- Defines read-only versus mutating MCP tool trust boundaries (`intent_note`, `dry_run`, answer token bounds, and tool-log routing between `<enclosure>/logs/` and `<coordination-root>/logs/mcp/`).

## Relationships

- Links outward to `docs/concepts.md`, `docs/workflows.md`, `docs/roles.md`, `docs/dashboard.md`, and `docs/reference/mcp-tools.md`.

## Evidence

- Reference-anchor blob and content currentness versus realization/proof and four-state invariant currentness. [1]
- Knowledge retrieval routes with `read_ar_files` brief-to-compact row degradation and names-only `knowledge_read`. [2]
- MCP tool server read-only versus mutating trust boundaries, answer token bounds, and tool-log locations. [3]
