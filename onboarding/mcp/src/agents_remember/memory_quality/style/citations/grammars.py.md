# mcp/src/agents_remember/memory_quality/style/citations/grammars.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/grammars.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Parse citation definitions and extents with tree-sitter.

## Code Commentary

### Logic

Module-level surface:

- `Binding` (class) — One name a construct binds: its extent, and the line the declaration itself begins on. The two differ for a decorated Python definition, whose extent is widened through `decorated_definition` to cover the decorator while the declaration begins on the `def`/`class` line below it.
- `CallLiteral` (class, lines 123-131) — One direct quoted argument, its syntax identity, and its call's line extent.
- `grammar_of` (function, lines 134-136) — The grammar that reads ``path``, or ``None`` when nothing does.
- `parsed` (function, lines 139-141) — Whether a definition in ``path`` is distinguishable from a mention of it.
- `typescript_anchor_identifier` (function, lines 144-185) — The direct identifier rooted by a complete TS call or generic type spelling.
- `call_argument_literals` (function, lines 188-213) — Every direct string argument and the call it belongs to, in document order.
- `language` (function, lines 216-228) — The loaded grammar, built once. A failure to load is fatal, never a fallback.
- `definitions` (function, lines 231-256) — Every name ``path`` binds, and the WIDENED line span of the construct that binds it, so a decorated definition's extent covers its decorator. A caller needing the declaration's own first line as well reads `bindings`.
- `bindings` (function) — Every name ``path`` binds, with both its widened extent and its declaration line, from ONE walk. The declaration line is the first line of the unwidened construct: the ``def``/``class`` line for a decorated definition, and the extent's start for every other construct — including an exported TypeScript declaration, whose ``export`` keyword shares the declaration's own first line.
- `_walk` (function, lines 259-272) — Every node in the tree, at any depth, in DOCUMENT ORDER.
- `_widened` (function, lines 275-279) — ``node`` grown outwards through the syntax that decorates or exports it.
- `_span` (function, lines 282-286) — The one-based line range ``node`` occupies.
- `_text` (function, lines 289-290)
- `_python_names` (function, lines 293-299) — The names one Python construct binds.
- `_python_targets` (function, lines 302-314) — The plain names an assignment target binds, unpacking nested tuples and lists.
- `_script_names` (function, lines 317-323) — The names one JavaScript or TypeScript construct binds.
- `_script_targets` (function, lines 326-343) — The names a declarator binds, unpacking destructuring one alternative at a time.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `CallLiteral` (lines 123-131) — One direct quoted argument, its syntax identity, and its call's line extent.. | `CallLiteral` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:139-147 |
| Defines the function `grammar_of` (lines 134-136) — The grammar that reads ``path``, or ``None`` when nothing does.. | `grammar_of` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:150-152 |
| Defines the function `parsed` (lines 139-141) — Whether a definition in ``path`` is distinguishable from a mention of it.. | `parsed` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:155-157 |
| Defines the function `typescript_anchor_identifier` (lines 144-185) — The direct identifier rooted by a complete TS call or generic type spelling.. | `typescript_anchor_identifier` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:144-185 |
| Defines the function `call_argument_literals` (lines 188-213) — Every direct string argument and the call it belongs to, in document order.. | `call_argument_literals` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:188-213 |
| Defines the function `language` (lines 216-228) — The loaded grammar, built once. A failure to load is fatal, never a fallback.. | `language` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:232-244 |
| Defines the function `definitions` (lines 231-256) — Every name ``path`` binds, and the line span of the construct that binds it.. | `definitions` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:231-256 |
| Defines the function `_walk` (lines 259-272) — Every node in the tree, at any depth, in DOCUMENT ORDER.. | `_walk` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:292-305 |
| Defines the function `_widened` (lines 275-279) — ``node`` grown outwards through the syntax that decorates or exports it.. | `_widened` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:308-312 |
| Defines the function `_span` (lines 282-286) — The one-based line range ``node`` occupies.. | `_span` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:282-286 |
| Defines the function `_text` (lines 289-290). | `_text` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:322-323 |
| Defines the function `_python_names` (lines 293-299) — The names one Python construct binds.. | `_python_names` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:326-332 |
| Defines the function `_python_targets` (lines 302-314) — The plain names an assignment target binds, unpacking nested tuples and lists.. | `_python_targets` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:335-347 |
| Defines the function `_script_names` (lines 317-323) — The names one JavaScript or TypeScript construct binds.. | `_script_names` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:350-356 |
| Defines the function `_script_targets` (lines 326-343) — The names a declarator binds, unpacking destructuring one alternative at a time.. | `_script_targets` | mcp/src/agents_remember/memory_quality/style/citations/grammars.py:359-376 |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: `CallLiteral` repointed to mcp/src/agents_remember/memory_quality/style/citations/grammars.py:139-147. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `grammar_of` repointed to mcp/src/agents_remember/memory_quality/style/citations/grammars.py:150-152. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `parsed` repointed to mcp/src/agents_remember/memory_quality/style/citations/grammars.py:155-157. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `language` repointed to mcp/src/agents_remember/memory_quality/style/citations/grammars.py:232-244. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_walk` repointed to mcp/src/agents_remember/memory_quality/style/citations/grammars.py:292-305. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_widened` repointed to mcp/src/agents_remember/memory_quality/style/citations/grammars.py:308-312. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_text` repointed to mcp/src/agents_remember/memory_quality/style/citations/grammars.py:322-323. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_python_names` repointed to mcp/src/agents_remember/memory_quality/style/citations/grammars.py:326-332. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_python_targets` repointed to mcp/src/agents_remember/memory_quality/style/citations/grammars.py:335-347. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_script_names` repointed to mcp/src/agents_remember/memory_quality/style/citations/grammars.py:350-356. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_script_targets` repointed to mcp/src/agents_remember/memory_quality/style/citations/grammars.py:359-376. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T19:21+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): added the two symbols this change introduces and corrected the one claim it widened. `Binding` and `bindings()` are new module surface the card did not carry: one walk now answers both the widened extent (which `definitions` still returns unchanged, so every projection range keeps quoting the decorator) and the declaration's own first line, which is the `def`/`class` line for a decorated Python definition and the extent's start for every other construct, an exported TypeScript declaration included. `definitions`' description now says its span is the WIDENED one and points a caller needing the declaration line at `bindings`. This is item 14's mechanism made visible: the reopen check reads the declaration line because the extent is deliberately widened through `decorated_definition`. Documentation only: no source byte was touched by this pass. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are NOT advanced — these sources are uncommitted, so no commit carries their bytes; the candidate is named in the `reviewedWorkingCandidate` metadata row and the governed closeout owns the real commits.
- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
