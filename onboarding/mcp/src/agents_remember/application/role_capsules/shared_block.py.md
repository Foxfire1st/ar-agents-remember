# mcp/src/agents_remember/application/role_capsules/shared_block.py

## Governing Overview

[application overview](../overview.md)

## Purpose

Filters the admitted `core/every-role.md` shared instruction block deterministically per canonical role so each role seat receives only universal clauses and clauses addressed to its own role, without altering the admitted full source or compiler seal.

## Code Commentary

`filter_shared_block(text, role)` returns `text` unchanged when `role is None` or `text` is empty, and normalizes `role` through `canonical_role(role.strip().lower())` so `system-specialist` resolves to `investigator`.

Lines are parsed within the Markdown heading hierarchy while tracking fenced code blocks (` ``` ` and `~~~`, up to three leading spaces, backtick info strings rejecting backticks, and closing fences matching character and minimum length) verbatim inside their owning entry so headings and role prefixes inside code fences are never interpreted.

A non-blank line starting with `<Role1>[, <Role2>, ...]: <rest>` where every comma-separated token belongs to `_RECOGNIZED_ROLE_LABELS` (the nine canonical roles including `consolidator`, plus `system-specialist`) starts a role-scoped entry. Non-role prefixes remain universal. Blank lines end the active entry and start a new rendering group; consecutive non-blank role-prefixed lines parse as distinct entries sharing one group so each filters independently while surviving siblings stay separated by single newlines. Any heading (`##`, `###`, ...) with neither kept direct entries nor kept child subsections is pruned, the top-level `#` heading is retained whenever any content survives, and trailing-newline presence matches the input.

## Relationships

- Depends on `agents_remember.models.role_identity.canonical_role`.
- Called by `application/role_capsules/compilation.py::compile_admitted_capsule` only for `CapsuleRoleSeat` (leaving full-source compiler admission/sealing, `CapsuleLauncherSeat`, and absent-source compilations untouched).
- Verified by `scripts/agent_evals/text.py::_captured_origins` during Curator evaluation text capture against the full `core/every-role.md` source revision.

## Evidence

- `filter_shared_block` passes through `role is None` or empty text, normalizes `role` via `canonical_role`, and preserves trailing-newline state. [1]

- `_RECOGNIZED_ROLE_LABELS` and `_parse_role_prefix` recognize the nine canonical roles plus `system-specialist` and leave non-role prefixes universal. [2]

- `_consume_line` preserves fenced code blocks verbatim inside their owning entry and splits consecutive role-prefixed lines into independent entries. [3]
- `_filter_section` prunes empty headings and `_render_entries` preserves tight single-newline separation within shared groups. [4]
