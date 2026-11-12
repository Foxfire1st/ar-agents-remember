# mcp/src/agents_remember/cli/memory_citations.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

CLI adapter for citation checks and fixes. Fixing uses an ordinary leaf contract or the existing fixer's measured pre-baseline admission; other modes still require a contract.

## Code Commentary

### Logic

Module-level surface:

- `add_arguments` declares `--repo`, optional `--contract`, optional `--config`, `--fix`, repeatable `--document`, `--census`, `--census-artifact` and `--dry-run`.
- `run` chooses report, census or fix, constructs document-only `CitationOperationScope`, requires a contract without fix, loads `--config` or else the user's one MCP authority settings file that `discover_config()` selects, prints the whole JSON result and returns 0 only when its `ok` is true. Source-index build, snapshot, exclusion and migration operands are absent.

Citation selection uses onboarding-relative `--document` names. Repeated names form the finite fix list; no caller-glob register or expected snapshot is accepted. Converted authoring and mechanical repair retain their application-owned admissions.

- **Finite selection.** One `--document` preserves the singleton operation; repeated occurrences
  become the multi-card selection admitted only for `--fix`. Other operations refuse a list.
  The CLI continues to print the whole result, not the MCP status projection. Each listed card is
  handled as a singleton and a refused member does not prevent the other members.
- **Converted memory (L37 fix round P1b, MIK-R46).** On converted memory `--fix`
  takes `--document` alone and authors card citation rows into sidecar references,
  then refreshes mechanical anchor moves. The procedure is in the l-01 Curator card procedure,
  `reference/curator/card-formats-and-citations.md`. The current `--document` help states that fix takes document selection alone; application check/fix refuse unconverted memory, including `--fix --dry-run`, with
  `legacy-format` and the conversion procedure regardless of converted branches
  elsewhere. Convert first, then repeat the operation.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private. Document selection rides on the shared `CitationOperationScope`; no caller-exclude field remains.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- Omitting `--contract` is admitted only for `--fix` before the configured converted root's first attributed baseline, with no linked memory worktree. A failed admission or a later contractless fix refuses; report mode still requires `--contract`.

### Todos

None.

## Evidence



- The CLI declares report/fix and optional contract with repeatable document selection. [6]


- Citation scope carries only singleton or finite document-list selection. [7]


### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.


- CLI declarations make --contract optional at the parser (required except for --fix on the configured memory root before its first attributed baseline) and keep --document as a repeatable per-call selection. [1]


- Dispatch requires a contract for modes other than fix and forwards the fixer's optional contract to its application owner. [2]


- The scope that carries the caller’s named documents and refuses both selectors, an empty list, and a list outside citation_fix. [3]



- The --document help states the converted form: --document alone. [5]
