# mcp/src/agents_remember/serving/conversation/library/codex_normalize.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/codex_normalize.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The ports suite proves the normalized grammar (strict `ConversationItem` validators included)
on fake native payloads; the shared primitives module owns the capping/extraction helpers.

| Finding | Anchor | Source |
| --- | --- | --- |
| Codex reads normalize items with ordinals, windows, roles, blocks, and provenance through the strict contract validators. | `CodexLibraryTests` | mcp/tests/test_conversation_library_ports.py:221-410 |
| Shared capping, provenance, and text-extraction primitives this parser builds on. | `capped_text`, `native_provenance`, `text_content_parts` | mcp/src/agents_remember/serving/conversation/library/normalize_common.py:18-23; mcp/src/agents_remember/serving/conversation/library/normalize_common.py:26-31; mcp/src/agents_remember/serving/conversation/library/normalize_common.py:51-56 |
| The normalized item/block/provenance grammar this parser targets. | "class ConversationItem(WireModel):" | mcp/src/agents_remember/models/conversations/content.py:160-160 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local parser.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 3 repository-internal citations for the Codex port tests, shared normalizers, and normalized item grammar.
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
