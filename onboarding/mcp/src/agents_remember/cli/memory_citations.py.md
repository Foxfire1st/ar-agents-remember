# mcp/src/agents_remember/cli/memory_citations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/memory_citations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

CLI adapter: check a leaf's memory citations, regenerate their ranges, or migrate them.

## Code Commentary

### Logic

Module-level surface:

- `add_arguments` (function, lines 53-117) — declares the citation modes plus `--repo`, `--contract`,
  `--document`, `--expected-snapshot`, `--build-index`, `--fix`, `--migrate`, `--dry-run`, and since
  260915-CAPS-L14 the repeatable **`--exclude GLOB`**.
- `run` (function, lines 120-184) — validates the selected mode, builds the `CitationOperationScope`
  (carrying the caller's excludes), and dispatches to the matching citation tool.

`--exclude` adds a code-root-relative path glob to **this call's** exclusion register, on top of the
register every call already honours (the memory layer's `settings.json → onboarding.pathRules.exclude`
and the code repo's `.gitignore`). It is deliberately named `--exclude` rather than `--ignore`: it
narrows the candidate population, it does not reimplement Git's ignore rules. Repeat the flag for
more than one pattern; the register's rule set is reported in the result, so a reader can see which
patterns produced the population. The scope constructor refuses a pattern that cannot mean anything
(empty, absolute, or escaping the code root) **by name** rather than letting it match nothing.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module. Caller excludes ride on `CitationOperationScope.excludes`, the same value object every other citation operation uses.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- **There is no argument list that names the official memory repo**, and nothing here can widen the register for another caller: the excludes are scoped to the one invocation.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Declares the citation modes and the repeatable caller-exclude option. | `add_arguments` | mcp/src/agents_remember/cli/memory_citations.py:53-117 |
| Validates the selected mode, builds the scope and dispatches to the citation tool. | `run` | mcp/src/agents_remember/cli/memory_citations.py:120-184 |
| The scope that carries the caller's excludes and refuses a meaningless pattern. | `CitationOperationScope` | mcp/src/agents_remember/application/memory_tools.py:44-55 |
| The refusal rule for a pattern that cannot mean anything. | `validate_caller_excludes` | mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py:171-193 |

## Update History

- 2026-09-17T12:35+02:00 — 260915-CAPS-L14 curator: recorded the new repeatable **`--exclude GLOB`** option, why it is named `--exclude` rather than `--ignore` (it narrows the candidate population; it does not reimplement Git's ignore rules), that it is scoped to one invocation, and that a pattern which cannot mean anything is refused by name. **Re-derived both ranges against the 184-line source** (this leaf's diff grew `add_arguments` by 20 lines and `run` by 4) and added the scope and refusal rows. Verification metadata is left at this leaf's synced base `0346da9c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code commit.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
