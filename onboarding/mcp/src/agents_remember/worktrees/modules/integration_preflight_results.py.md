# mcp/src/agents_remember/worktrees/modules/integration_preflight_results.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Render the typed early integration result that excludes a blocked atomic-series landing.

## Code Commentary

### Logic

The module turns an atomic-series landing blocker into a structured public status payload. The former prepared-recovery helper (`prepared_integration_recovery`, which rebuilt the prepared commit pair from `args.recovery_commits`) was deleted with the closeout-door cut, so nothing here resumes a journaled generation any more; `atomic_landing_blocked_result` is the module's only export.

### Invariants And Boundaries

- A live series blocker is reported from contract/ref authority, not queue state.
- The module no longer owns prepared-recovery resumption: that seam is gone, and a resumed landing goes through the normal integration route from current refs.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain-documentation source applies to this repository-internal route.

### Repo-Internal References

- Atomic landing blockers are projected with exact contract and blocker evidence. [1]
- Prepared integration recovery is gone: the `prepared_integration_recovery` helper (which rebuilt the prepared commit pair from `args.recovery_commits`) was deleted with the closeout-door cut, and this module now exports `atomic_landing_blocked_result` alone. [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
