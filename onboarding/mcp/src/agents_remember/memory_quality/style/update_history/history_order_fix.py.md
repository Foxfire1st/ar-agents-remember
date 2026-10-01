# mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`history_order_fix.py` is the dedicated mutating script for sorting onboarding
`## Update History` bullet blocks newest-first after the diagnostic
`memory_quality_check` reports history-order findings.

## Code Commentary

### Logic

The script scans Markdown files under an onboarding root, reuses the
`history_order.py` section and timestamp parsing helpers, groups each history
bullet with its continuation lines, and sorts only sections where every bullet
has a valid timestamp. Sections with missing or invalid timestamps are reported
as skipped so the model or developer can edit them by hand. Finding paths are
relativized to the onboarding root via the shared `rel` helper imported from
`..integrity.onboarding_drift_check.discovery` rather than a local copy.

The module exposes `fix_onboarding_root()` for tests and `python -m
agents_remember.memory_quality.style.update_history.history_order_fix
<onboarding-root>` for direct use. `--dry-run` reports which files would change
without writing them.

### Invariants And Boundaries

- The checker stays diagnostic; this module owns the mechanical rewrite.
- Missing or invalid timestamps are not guessed.
- Continuation lines stay attached to their bullet block.
- The script operates on the onboarding root passed by the caller; normal
  closeout should pass the `c-08-ar-coordination-context-resolver` skill/MCP-resolved onboarding root.

## 260928-MIK-L30 Not Applicable On A Converted Tree (MIK-R30 Rule 5)

`fix_onboarding_root` first checks whether the onboarding root's parent holds `knowledge/layout.json`. On
such a converted tree there is no Update History to sort: it returns `ok: true` with status
`not-applicable-converted`, zero files checked and nothing changed, and reads or writes nothing. The
diagnostic check was already not applicable there (MIK-R24). On an unconverted tree the fixer is unchanged.

Rule 5 retires these checks and fixers at the cutover. Deleting `memory_quality/style/update_history/` is
left to MIK-R37 (architect ruling 2026-09-29T18:49:50 (5)): deleting it now would change today's gate on
unconverted trees.

- The module docstring's converted-tree paragraph. [1]
- The early return before any file is read. [2]
- No stamps and no history sort on a converted tree. [3]

## Evidence

### Repo-Internal References

- The diagnostic checker provides the timestamp and section parsing helpers. [4]
- The `rel` path-relativization helper is now imported from the drift-check discovery module instead of defined locally. [5]
