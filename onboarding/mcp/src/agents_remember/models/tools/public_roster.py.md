# mcp/src/agents_remember/models/tools/public_roster.py

## Governing Overview

[models overview](../overview.md)

## Purpose

`public_roster.py` holds the single definition of `PUBLIC_TOOLS` — the ordered tuple of the **72** tool
names the MCP server advertises as its public surface (66 until 260915-KS-L20 appended the five
`knowledge_*` operations; 63 until 260915-CAPS-L4 added `role_capsule_compile`, `skill_catalog_list`
and `skill_catalog_read`; 62 until 260831-LOCR-L37 added `worktree_pause`). It is a
**zero-runtime-import leaf**: it
imports nothing, defines nothing else, and exists only so a `models` response model can read the
roster without importing `mcp`.

Since 260831-LOCR-L32 the tuple lives here rather than in `mcp/tools/base.py`, which now re-exports
it. The relocation changed the object's home and nothing else — same tuple, same order — so every
consumer is unchanged and `agents_remember.mcp.tools.base.PUBLIC_TOOLS` still resolves the identical
object. The tuple held 62 unique names from L30 until 260831-LOCR-L37 added `worktree_pause`
immediately after `worktree_sync`, which is a membership change made here and in
`mcp/registration/worktrees.py` in the same leaf. 260915-CAPS-L4 made the next membership change: three
names **appended at the tail**, together with the new `capsule_serving.py` registrar and its three
`TOOL_RESPONSE_MODELS` rows in one change, so the roster, the registrar and the registry never
disagreed. 260915-KS-L20 is the **second append-only membership change**: the five `knowledge_*`
operation names go on at the tail, together with the fourteenth `TOOL_REGISTRARS` entry
(`registration/knowledge.py`) and five `TOOL_RESPONSE_MODELS` rows in the same change, so no earlier
name's advertised position moved and there is no interleaving to verify.

## Code Commentary

### Logic

The module body is one module docstring and one literal:

```python
PUBLIC_TOOLS = (
    "ping",
    ...
    # The capsule operation and the skill discovery/read surface.
    "role_capsule_compile",
    "skill_catalog_list",
    "skill_catalog_read",
    # The knowledge operation family: read, change, diff, integrity and projection.
    "knowledge_read",
    "knowledge_change",
    "knowledge_diff",
    "knowledge_integrity_check",
    "knowledge_project",
)
```

`PUBLIC_TOOLS` spans **L22-L97**; the file is 97 lines. The only other statement is
`from __future__ import annotations` at L20 — no imports, no helpers, no package-level side effects.

### Conventions

- The tuple's order is the order `mcp/registration/` publishes tools in; order is part of the
  advertisement contract, so an edit here is a wire change and not a cosmetic reorder.
- Membership is maintained in one place and one place only. `mcp/tools/base.py` re-exports this
  object through `__all__`; it must never re-declare a second tuple.

### Invariants And Boundaries

- **Zero runtime imports, deliberately.** `models/worktree.py` imports this module at module scope,
  and it does so while `models.tools.tool_registry` may still be initializing. Any import added here
  can therefore create the cycle this relocation removed.
- **This module never imports `mcp`.** `layers.toml` ranks `models` = 2 and `mcp` = 22, and the
  `mcp` charter forbids any import from below; a `models → mcp` edge is a layering violation.
- `PUBLIC_TOOLS` is the *advertised* name set, not the *registered* name set. A tool can be
  registered (`models/tools/tool_registry.py`) and deliberately absent here — `session_retire` is the
  live example.
- Do not add a second roster, a frozenset mirror, or a derived copy. `PUBLIC_TOOL_RESPONSE_MODELS`
  derives the response-model subset; nothing derives the tuple.

## Why The Roster Lives In `models`

This is the whole point of the relocation, so it is recorded rather than left to be re-derived.

The roster was defined in `mcp/tools/base.py`. `application/worktree_status.py::_project_terminal_contract_status`
writes a `nextAction` / `nextTool` / `nextArgs` triple into the `worktree_status` payload, and that
payload is validated once against `TOOL_RESPONSE_MODELS["worktree_status"]` — `WorktreeStatusResponse`
→ `WorktreeCommandResponse` → `FlexibleToolResponse` → `FlexibleResponseModel` (`extra="allow"`). The
envelope declared **none** of those three keys, so the values crossed the wire verbatim and
unchecked. Enforcing the vocabulary at the model boundary requires `models/worktree.py` to read
`PUBLIC_TOOLS`, and while the tuple lived in `mcp` that read was not expressible:

- `models → mcp` is a layering violation (`layers.toml` ranks `models` = 2, `mcp` = 22; the `mcp`
  charter forbids any import from below).
- A function-local import is unwritable here: `ruff` rule `PLC0415` refuses it and suppressions are
  forbidden in this repository.
- Module-level imports in either direction are circular (`mcp.tools.base` → `models.worktree` →
  `mcp.tools.base`).

Moving the tuple to a zero-import `models` leaf makes the check *expressible* instead of
special-cased, and it matches `layers.toml`'s own doctrine: wire vocabulary is defined in `models`
and imported by whoever decides it. The layering checker returned to its exact baseline of 16
violations with no `models → mcp` edge and no new cycle.

## Evidence

### Repo-Internal References

- The roster's single definition, 72 ordered names, in a module that imports nothing. [1]
- The stop's advertised name, placed immediately after its sync sibling in the working half of the tuple. [2]
- The three capsule/skill-serving advertised names, appended at the tail with the registrar and registry rows that publish them. [3]
- The five `knowledge_*` names 260915-KS-L20 appended at the tail, with the comment naming the family, published in the same change as their registrar and registry rows. [4]
- The adapter re-exports this object through `__all__` instead of declaring its own tuple. [5]
- The response model that reads the roster to enforce the worktree surface's next-move vocabulary. [6]
- The by-name response-model registry the roster is compared against, and the deliberate non-public names it excludes. [7]
- The live registered-order comparison that treats this tuple as the advertised authority. [8]
- The executor that pins the worktree surface's enforcement of this roster in both directions. [9]
- The registrar that publishes the three capsule/skill names, whose order the tuple must match. [10]
- The registrar that publishes the five `knowledge_*` names appended to `TOOL_REGISTRARS` in the same change. [11]

### Cross-Repo References

No cross-repository implementation dependency governs this repository-local tuple.
