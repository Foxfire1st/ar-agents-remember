# mcp/src/agents_remember/cli/memory_citations.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

CLI adapter for citation checks and fixes. Fixing uses an ordinary leaf contract or the existing fixer's measured pre-baseline admission; other modes still require a contract.

## Code Commentary

### Logic

Module-level surface:

- `add_arguments` (function, lines 53-117) — declares the citation modes plus `--repo`, `--contract`,
  repeatable `--document`, `--expected-snapshot`, `--build-index`, `--fix`, `--dry-run`, and since
  260915-CAPS-L14 the repeatable **`--exclude GLOB`**.
- `run` (function, lines 120-184) — validates one of the three modes (report,
  `--build-index`, `--fix`), builds the `CitationOperationScope` carrying caller
  excludes, and dispatches to check, source-index build or fix. `--migrate` is no
  longer registered or dispatched; conversion is `knowledge-convert`, not citation
  migration. The MCP migration tool is also unregistered; its internal code is
  retained for MIK-R65, not available as an alternative route.

On a legacy `Trees` branch, `--exclude` adds a code-root-relative path glob to **this call's**
exclusion register alongside the memory layer's `settings.json → onboarding.pathRules.exclude`
and the code repo's `.gitignore`. Repeat it for several patterns. That branch narrows its candidate
population and reports the register; the flag does not reimplement Git's ignore rules. The scope
constructor refuses a meaningless pattern (empty, absolute or escaping the code root) **by name**.
Converted check/fix validates that syntax but returns before `Trees`, without forwarding caller
globs to converted reference acquisition or repair. Converted fixing is scoped by `--document`
and internally skips authoring-refused sidecars; neither is a promise that `--exclude` filters it.

- **Finite selection.** One `--document` preserves the singleton operation; repeated occurrences
  become the multi-card selection admitted only for `--fix`. Other operations refuse a list.
  The CLI continues to print the whole result, not the MCP status projection. Each listed card is
  handled as a singleton and a refused member does not prevent the other members.
- **Converted memory (L37 fix round P1b, MIK-R46).** On converted memory `--fix`
  takes `--document` alone and authors card citation rows into sidecar references,
  then refreshes mechanical anchor moves. The procedure is c-05’s
  `converted-card-workflow.md`. The parser’s retained legacy `--document` help
  still mentions `--expected-snapshot`, but that is not admission: application
  check/fix refuse unconverted memory, including `--fix --dry-run`, with
  `legacy-format` and the conversion procedure regardless of converted branches
  elsewhere. Convert first, then repeat the operation.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module. Caller excludes ride on `CitationOperationScope.excludes`, the same value object every other citation operation uses.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- Omitting `--contract` is admitted only for `--fix` before the configured converted root's first attributed baseline, with no linked memory worktree. A failed admission or a later contractless fix refuses; report and index-build modes still require `--contract`; migration mode is removed. Caller excludes remain call-local on branches that use the register; converted check/fix does not apply them.

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
