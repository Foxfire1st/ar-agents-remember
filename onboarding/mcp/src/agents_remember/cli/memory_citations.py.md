# mcp/src/agents_remember/cli/memory_citations.py

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

- **Converted memory (L37 fix round P1b).** The `--document` help now says that on converted memory `--fix`
  takes `--document` alone (one card and its sidecar), and on unconverted memory it comes with
  `--expected-snapshot`. The behaviour is `application/memory_tools.citation_fix_tool`'s: on a converted tree
  the fixer authors the card's citation rows into sidecar references and re-records moved anchors. The
  curator's procedure is the c-05 skill's `converted-card-workflow.md`.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module. Caller excludes ride on `CitationOperationScope.excludes`, the same value object every other citation operation uses.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- **There is no argument list that names the official memory repo**, and nothing here can widen the register for another caller: the excludes are scoped to the one invocation.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Declares the citation modes and the repeatable caller-exclude option. [1]
- Validates the selected mode, builds the scope and dispatches to the citation tool. [2]
- The scope that carries the caller's excludes and refuses a meaningless pattern. [3]
- The refusal rule for a pattern that cannot mean anything. [4]

- The --document help states the converted form: --document alone. [5]
