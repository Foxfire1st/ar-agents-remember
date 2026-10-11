# mcp/src/agents_remember/cli/memory_citations.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

CLI adapter for citation checks and fixes. Fixing uses an ordinary leaf contract or the existing fixer's measured pre-baseline admission; other modes still require a contract.

## Code Commentary

### Logic

Module-level surface:

- `add_arguments` (function, lines 53-117) — declares the citation modes plus `--repo`, `--contract`,
  `--document`, `--expected-snapshot`, `--build-index`, `--fix`, `--migrate`, `--dry-run`, and since
  260915-CAPS-L14 the repeatable **`--exclude GLOB`**.
- `run` (function, lines 120-184) — validates the selected mode, builds the `CitationOperationScope`
  (carrying the caller's excludes), and dispatches to the matching citation tool.

On a legacy `Trees` branch, `--exclude` adds a code-root-relative path glob to **this call's**
exclusion register alongside the memory layer's `settings.json → onboarding.pathRules.exclude`
and the code repo's `.gitignore`. Repeat it for several patterns. That branch narrows its candidate
population and reports the register; the flag does not reimplement Git's ignore rules. The scope
constructor refuses a meaningless pattern (empty, absolute or escaping the code root) **by name**.
Converted check/fix validates that syntax but returns before `Trees`, without forwarding caller
globs to converted reference acquisition or repair. Converted fixing is scoped by `--document`
and internally skips authoring-refused sidecars; neither is a promise that `--exclude` filters it.

- **Converted memory (L37 fix round P1b).** The `--document` help now says that on converted memory `--fix`
  takes `--document` alone (one card and its sidecar), and on unconverted memory it comes with
  `--expected-snapshot`. The behaviour is `application/memory_tools.citation_fix_tool`'s: on a converted tree
  the fixer authors the card's citation rows into sidecar references and re-records moved anchors. The
  curator's procedure is the c-05 skill's `converted-card-workflow.md`.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module. Caller excludes ride on `CitationOperationScope.excludes`, the same value object every other citation operation uses.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- Omitting `--contract` is admitted only for `--fix` before the configured converted root's first attributed baseline, with no linked memory worktree. A failed admission or a later contractless fix refuses; report, index-build and migration modes still require `--contract`. Caller excludes remain call-local on branches that use the register; converted check/fix does not apply them.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- CLI declarations make --contract optional for the two-admission fixer route and preserve the repeatable per-call exclusion option. [1]
- Dispatch requires a contract for modes other than fix and forwards the fixer's optional contract to its application owner. [2]
- The scope that carries the caller's excludes and refuses a meaningless pattern. [3]
- The refusal rule for a pattern that cannot mean anything. [4]

- The --document help states the converted form: --document alone. [5]
