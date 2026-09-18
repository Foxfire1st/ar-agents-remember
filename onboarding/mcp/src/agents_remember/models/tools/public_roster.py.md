# mcp/src/agents_remember/models/tools/public_roster.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/tools/public_roster.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated |  2026-09-18T14:55+02:00 |
| lastVerifiedCommitHash | `f05ba167cd6dfb56b48a775f3da5d45528c09c82` |
| lastVerifiedCommitDate | 2026-09-18T17:19:31+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models overview](../overview.md)

## Purpose

`public_roster.py` holds the single definition of `PUBLIC_TOOLS` — the ordered tuple of the **66** tool
names the MCP server advertises as its public surface (63 until 260915-CAPS-L4 added
`role_capsule_compile`, `skill_catalog_list` and `skill_catalog_read`; 62 until 260831-LOCR-L37 added
`worktree_pause`). It is a **zero-runtime-import leaf**: it
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
disagreed.

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
)
```

`PUBLIC_TOOLS` spans **L22-L90**; the file is 90 lines. The only other statement is
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
| The roster's single definition, 66 ordered names, in a module that imports nothing. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-90 |
| The stop's advertised name, placed immediately after its sync sibling in the working half of the tuple. | `worktree_pause` | mcp/src/agents_remember/models/tools/public_roster.py:59-59 |
| The three newest advertised names, appended at the tail with the registrar and registry rows that publish them. | `role_capsule_compile`; `skill_catalog_list`; `skill_catalog_read` | mcp/src/agents_remember/models/tools/public_roster.py:88-90 |
| The adapter re-exports this object through `__all__` instead of declaring its own tuple. | "__all__ = [\"PUBLIC_TOOLS\", \"RESERVED_TOOLS\", \"TRANSPORT\"]" | mcp/src/agents_remember/mcp/tools/base.py:19-19 |
| The response model that reads the roster to enforce the worktree surface's next-move vocabulary. | `_require_registered_public_next_tool` | mcp/src/agents_remember/models/worktree.py:377-388 |
| The by-name response-model registry the roster is compared against, and the deliberate non-public names it excludes. | `INTERNAL_COMPAT_TOOL_NAMES`; `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:126-147; mcp/src/agents_remember/models/tools/tool_registry.py:155-238 |
| The live registered-order comparison that treats this tuple as the advertised authority. | `PublicSurfaceInventoryTests` | mcp/tests/test_tools.py:222-283 |
| The executor that pins the worktree surface's enforcement of this roster in both directions. | `test_next_tool_must_name_a_registered_public_tool`; `test_the_worktree_surface_refuses_a_registered_but_non_public_tool` | mcp/tests/test_worktree_status_terminal_next_tool.py:231-278 |
| The registrar that publishes the three newest names, whose order the tuple must match. | `register_capsule_and_skill_tools` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:85-90 |

## Cross-Repo References

No cross-repository implementation dependency governs this repository-local tuple.

## Update History
- 2026-09-18T14:49:10+00:00: Generated citation repair: `_require_registered_public_next_tool` repointed to mcp/src/agents_remember/models/worktree.py:377-388. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:55+02:00 — 260918-TSIP-L3 curator (citation repair, `ar/260918-tsip-l3-ar`, base `a12c511f`): `PublicSurfaceInventoryTests` was repointed `:220-281 → :222-283`. The claim's wording was re-read against the new bytes and is unchanged — only the range moved, because this leaf's edit to `mcp/tests/test_tools.py` inserted lines above it. `lastUpdated` advances with this repair; `lastVerifiedCommitHash` is deliberately unchanged because the candidate is uncommitted and the governed closeout owns the real code commit.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `worktree_pause` repointed to mcp/src/agents_remember/models/tools/public_roster.py:59-59. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `role_capsule_compile`; `skill_catalog_list`; `skill_catalog_read` repointed to mcp/src/agents_remember/models/tools/public_roster.py:88-88; mcp/src/agents_remember/models/tools/public_roster.py:89-89; mcp/src/agents_remember/models/tools/public_roster.py:90-90. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `register_capsule_and_skill_tools` repointed to mcp/src/agents_remember/mcp/registration/capsule_serving.py:85-90. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator (uncommitted change set on `ar/260915-caps-l4`, base
  `b00a4ac2`): the advertised tuple gained three names **appended at the tail** —
  `role_capsule_compile`, `skill_catalog_list` and `skill_catalog_read`, with the comment that names
  the pair of surfaces they serve — bringing 63 ordered names to **66** and the extent from `L22-L86`
  to `L22-L90`. Unlike the previous membership changes, this one appended rather than inserting, so no
  existing name's advertised position moved; the three names went into the roster, the new
  `mcp/registration/capsule_serving.py` registrar and `TOOL_RESPONSE_MODELS` in the same change, which
  is the L29 lesson applied by construction. Corrected the Purpose count and extent, the Logic
  literal's tail, and the two registry ranges on this card (`INTERNAL_COMPAT_TOOL_NAMES` 120-139 →
  126-147 and `TOOL_RESPONSE_MODELS` 147-225 → 155-238, both shifted by this leaf's own three registry
  rows and by earlier additions this card had not re-measured), and added the roster-tail and
  registrar reference rows. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: the advertised tuple gained `worktree_pause` (63 ordered
  names, extent `L22-L86`, the name at `:58` immediately after `worktree_sync`) in the same leaf that
  registered the tool and gave it a response model, so the roster, the registrar and the registry never
  disagreed. The relocation account above is unchanged: the object still has one definition and
  `mcp/tools/base.py` still re-exports it. Verification metadata remains closeout-owned; no acceptance
  claim.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: created the card for the new zero-import `models`
  leaf. Recorded that the relocation is what makes the worktree next-move vocabulary enforceable at
  the model boundary (the `models → mcp` layering violation, the unwritable `PLC0415` local import,
  and the circular module-level imports that ruled the roster's old home out), and that the tuple is
  identical and still re-exported from `mcp/tools/base.py`, so no consumer changed. Verification
  metadata remains closeout-owned; no acceptance claim.
