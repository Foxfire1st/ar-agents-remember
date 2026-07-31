# mcp/src/agents_remember/serving/conversation/library/codex_normalize.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/codex_normalize.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this internal parser.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The ports suite proves the normalized grammar (strict `ConversationItem` validators included)
on fake native payloads; the shared primitives module owns the capping/extraction helpers.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Codex reads normalize items with ordinals, windows, roles, blocks, and provenance through the strict contract validators. | L255-L289 | [test_conversation_library_ports.py](agents-remember/mcp/tests/test_conversation_library_ports.py) |
| Shared capping, provenance, and text-extraction primitives this parser builds on. | L18-L69 | [normalize_common.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/normalize_common.py) |
| The normalized item/block/provenance grammar this parser targets. | L311-L399 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local parser.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T16:50+02:00 — No content impact: the leaf's whole edit to this parser is the deletion
  of the trailing `# noqa: UP040 - Python 3.11 support` from the `ToolPhase` line. The declaration
  `ToolPhase: TypeAlias = Literal["completed", "failed", "interrupted"]` and its docstring are
  otherwise byte-identical, so the terminal-phase vocabulary this card pins is exactly what the
  source still declares. The suppression went dead because the root `pyproject.toml` now sets
  `[tool.ruff] target-version = "py311"`, and UP040 only fires when the target supports PEP 695
  `type` statements. Re-read the builder dispatch, the provenance/evidence-reference conventions,
  and the unknown-vendor and fail-closed invariants against the current file: none of them names a
  lint directive or an interpreter floor, so every claim still holds.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: the only non-format change here is a lint-suppression cleanup — the `# noqa: UP040` suppression on the `ToolPhase` type alias was deleted, because `[tool.ruff] target-version` is now pinned to the supported floor `py311` and those PEP 695 upgrade rules no longer fire. The declarations themselves are byte-identical. Nothing else in the file changed, so no other claim in this sidecar can have been invalidated by this leaf. Attested, deliberately not rewritten.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the Codex thread-item parser
  sidecar. Verification is blank until closeout commits and stamps the new source.
