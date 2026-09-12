# mcp/src/agents_remember/models/tools/public_roster.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/tools/public_roster.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-12T22:55+02:00 |
| lastVerifiedCommitHash | `5a7bd5779935d1a7e24e978b52638edfd300ac4d` |
| lastVerifiedCommitDate | 2026-09-12T23:26:17+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models overview](../overview.md)

## Purpose

`public_roster.py` holds the single definition of `PUBLIC_TOOLS` — the ordered tuple of the 62 tool
names the MCP server advertises as its public surface. It is a **zero-runtime-import leaf**: it
imports nothing, defines nothing else, and exists only so a `models` response model can read the
roster without importing `mcp`.

Since 260831-LOCR-L32 the tuple lives here rather than in `mcp/tools/base.py`, which now re-exports
it. The object is unchanged — same tuple, same order, same 62 unique names — so every consumer is
unchanged and `agents_remember.mcp.tools.base.PUBLIC_TOOLS` still resolves the identical object.

## Code Commentary

### Logic

The module body is one module docstring and one literal:

```python
PUBLIC_TOOLS = (
    "ping",
    ...
    "message_child",
)
```

`PUBLIC_TOOLS` spans **L22-L85**; the file is 85 lines. The only other statement is
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The roster's single definition, 62 ordered names, in a module that imports nothing. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-85 |
| The adapter re-exports this object through `__all__` instead of declaring its own tuple. | "__all__ = [\"PUBLIC_TOOLS\", \"RESERVED_TOOLS\", \"TRANSPORT\"]" | mcp/src/agents_remember/mcp/tools/base.py:19-19 |
| The response model that reads the roster to enforce the worktree surface's next-move vocabulary. | `_require_registered_public_next_tool` | mcp/src/agents_remember/models/worktree.py:331-369 |
| The by-name response-model registry the roster is compared against, and the deliberate non-public names it excludes. | `TOOL_RESPONSE_MODELS`; `INTERNAL_COMPAT_TOOL_NAMES` | mcp/src/agents_remember/models/tools/tool_registry.py:120-139; mcp/src/agents_remember/models/tools/tool_registry.py:147-225 |
| The live registered-order comparison that treats this tuple as the advertised authority. | `PublicSurfaceInventoryTests` | mcp/tests/test_tools.py:220-281 |
| The executor that pins the worktree surface's enforcement of this roster in both directions. | `test_next_tool_must_name_a_registered_public_tool`; `test_the_worktree_surface_refuses_a_registered_but_non_public_tool` | mcp/tests/test_worktree_status_terminal_next_tool.py:231-278 |

## Cross-Repo References

No cross-repository implementation dependency governs this repository-local tuple.

## Update History
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: created the card for the new zero-import `models`
  leaf. Recorded that the relocation is what makes the worktree next-move vocabulary enforceable at
  the model boundary (the `models → mcp` layering violation, the unwritable `PLC0415` local import,
  and the circular module-level imports that ruled the roster's old home out), and that the tuple is
  identical and still re-exported from `mcp/tools/base.py`, so no consumer changed. Verification
  metadata remains closeout-owned; no acceptance claim.
