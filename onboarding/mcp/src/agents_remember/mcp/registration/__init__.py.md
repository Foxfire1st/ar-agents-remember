# mcp/src/agents_remember/mcp/registration/__init__.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/registration/__init__.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-09-12T22:55+02:00                                       |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`                   |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[registration route overview](overview.md)

## Purpose

The package door for the MCP tool surface. It declares the one registrar signature every family
module is called with and the ordered tuple `create_server` loops over.

## Code Commentary

### Logic

Two public names:

- `ToolRegistrar = Callable[[FastMCP, McpRuntimeConfig], None]` — the shape of a family module's
  `register_*_tools`.
- `TOOL_REGISTRARS: tuple[ToolRegistrar, ...]` — the **thirteen** registrars in advertise order: core,
  sessions, memory, providers, code_search, worktrees, closeout, tasks, benchmarks, lifecycle,
  gates, orchestration, capsule-and-skill-serving.

The newest entry is `register_capsule_and_skill_tools` from `capsule_serving.py`, **appended** last so
no existing tool's registration order moved — registration order is part of the advertised contract,
and the advertised tuple `PUBLIC_TOOLS` therefore gained its three names at its own tail as well
(`role_capsule_compile`, `skill_catalog_list`, `skill_catalog_read`; 63 → 66 names).

`__all__` exports both. The module docstring states the division this package exists to enforce:
`create_server` owns process wiring (the compact-content shim, the ambient lifecycle, the `FastMCP`
instance) and nothing else; every `@server.tool()` definition lives in a family module here.

### Invariants And Boundaries

- Adding a tool means editing one family module. Adding a family means a new module plus one entry
  in this tuple — `create_server` should never grow a special case.
- **The tuple's order is the order the server advertises tools in, and a new family is appended.** A
  new registrar inserted in the middle would renumber every later tool's advertised position, so the
  two surfaces that compare order (`PUBLIC_TOOLS` and the live-inventory suite) would both report a
  violation that is really a reordering.
- `PUBLIC_TOOLS` (defined at `mcp/src/agents_remember/models/tools/public_roster.py:22-90`,
  re-exported by `mcp/tools/base.py`)
  is the authority on the advertised name set; `mcp/tests/test_tools.py` compares it against a live
  server's `list_tools()` and against `server_info`'s exact list. The comparison is against a **live**
  registration, not against a payload that reports the tuple, so adding a registrar without adding its
  names to the tuple is a surface violation the suite catches.
- Importing this package imports every family module, which imports every payload builder. Keep it
  free of side effects beyond those imports. `capsule_serving.py` is the one family whose module also
  registers MCP **resources**, but the registration still happens inside its `register_*_tools`, so
  the package door's no-side-effects rule is unchanged.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `create_server` consumer iterates `TOOL_REGISTRARS`. | `create_server` | mcp/src/agents_remember/mcp/server.py:58-70 |
| The advertised tool-name list's one definition, re-exported unchanged by the adapter. | `PUBLIC_TOOLS`; "__all__ = [\"PUBLIC_TOOLS\", \"RESERVED_TOOLS\", \"TRANSPORT\"]" | mcp/src/agents_remember/models/tools/public_roster.py:22-90; mcp/src/agents_remember/mcp/tools/base.py:19-19 |
| The newest registrar, appended last so no existing registration order moved. | `register_capsule_and_skill_tools` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:85-90 |
| The three advertised names the new registrar publishes, at the tail of both surfaces. | `role_capsule_compile`; `skill_catalog_list`; `skill_catalog_read` | mcp/src/agents_remember/models/tools/public_roster.py:88-90 |
| The live registered-order comparison that makes a registrar-without-roster-name a surface violation. | `PublicSurfaceInventoryTests` | mcp/tests/test_tools.py:220-281 |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `register_capsule_and_skill_tools` repointed to mcp/src/agents_remember/mcp/registration/capsule_serving.py:85-90. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `role_capsule_compile`; `skill_catalog_list`; `skill_catalog_read` repointed to mcp/src/agents_remember/models/tools/public_roster.py:88-88; mcp/src/agents_remember/models/tools/public_roster.py:89-89; mcp/src/agents_remember/models/tools/public_roster.py:90-90. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator (uncommitted change set on `ar/260915-caps-l4`, base
  `b00a4ac2`): recorded the thirteenth registrar, `register_capsule_and_skill_tools` from the new
  `capsule_serving.py` family module, **appended** last so no existing tool's registration order moved;
  the advertised tuple accordingly gained `role_capsule_compile` / `skill_catalog_list` /
  `skill_catalog_read` at its own tail (63 → 66 names, extent now `L22-L90`). Corrected the body's
  twelve-registrar enumeration to thirteen and stated the append-only ordering rule with the reason
  (an inserted registrar renumbers every later advertised position, so both order-comparing surfaces
  would report a violation that is really a reordering). Also recorded that this family registers MCP
  resources as well as tools while keeping the package door's no-side-effects-beyond-imports rule.
  Verification metadata remains closeout-owned; no acceptance claim.

- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: renamed the roster's home. `PUBLIC_TOOLS` is no
  longer declared in `mcp/tools/base.py`; its one definition is the zero-import leaf
  `models/tools/public_roster.py:22-85`, which the adapter re-exports unchanged (same object, same
  order, same 62 names), so this package's exact-order comparison is unaffected; 260831-LOCR-L37 added
  `worktree_pause` to that tuple (63 names) and to `worktrees.py`'s registrars in the same leaf, so the
  exact-order comparison still holds and neither side was left ahead of the other. Repointed the
  invariant prose and the reference row; no behavioral claim changed. Verification metadata remains
  closeout-owned; no acceptance claim.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. Records `TOOL_REGISTRARS`
  as the single place that decides which families a server advertises. Verification metadata pinned
  to the pre-change commit until closeout stamps the L2 code commit.
