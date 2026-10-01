# mcp/src/agents_remember/serving/conversation/library/codex_normalize.py

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

Converts native Codex app-server thread items into the landed normalized `ConversationItem`
grammar with exact provenance rules: one responsibility, so the Codex port never parses vendor
payloads inline.

## Code Commentary

### Logic

`conversation_items_from_thread` flattens a thread's turns into the canonical chronological
order with stable 1-based global ordinals, keeping the turn id and status as correlation
context. A builder map dispatches on the item `type`: user messages (unknown-input lane,
capped text, optional vendor client-id correlation), agent messages (Markdown block), reasoning
(thinking block from summary/content parts), command executions and MCP tool calls (tool
input/output blocks with terminal phase from item status, error presence, or turn status),
file changes (diff blocks per change, explicit unknown-vendor block when detail is absent),
and context compaction (system notice). Anything unmapped becomes an explicit `unknown-vendor`
evidence item with a safe summary — nothing is flattened into guessed semantics and no raw
frame is retained.

### Conventions

Every item carries `native-history` source, `native-only` provenance strength with a
`codex-native-history` origin, revision 1, and a `codex-item:<id>` evidence reference. Text is
capped through the shared `normalize_common` primitives.

### Invariants And Boundaries

- Unknown vendor kinds are explicit evidence, never guessed Markdown; unknown-input provenance
  never masquerades as terminal-controlled input.
- Tool phases are the normalized terminal vocabulary (`completed`/`failed`/`interrupted`);
  in-flight history states are never projected.
- Required `type`/`id` fields fail closed through the substrate's typed validators.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this internal parser.

No configured domain documentation was available.

### Repo-Internal References

The ports suite proves the normalized grammar (strict `ConversationItem` validators included)
on fake native payloads; the shared primitives module owns the capping/extraction helpers.

- Native Codex thread turns are flattened into chronological ConversationItem ordinals by the normalization owner. [1]
- Shared capping, provenance, and text-extraction primitives this parser builds on. [2]
- The normalized item/block/provenance grammar this parser targets. [3]

### Cross-Repo References

No meaningful cross-repo boundary exists for this local parser.

No meaningful cross-repo references found.
