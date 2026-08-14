# mcp/tests/_global_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_global_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-10T18:31+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Owned module-level mutable state that every test must leave as it found it.

## Code Commentary

### Logic

Module-level surface:

- `OwnedMutableState` (class, lines 14-19) — One deliberately-enumerated global and the operations needed to restore it.
- `_declared_snapshot` (function, lines 22-23) — Snapshot the kernel-owned checkout execution mode.
- `_declared_restore` (function, lines 26-28)
- `snapshot_owned_mutable_state` (function, lines 42-43)
- `restore_owned_mutable_state` (function, lines 46-54) — Restore every owned global, returning the complete list that changed.
- `preserve_owned_mutable_state` (function, lines 58-64) — Explicitly contain a production entry point whose contract is to set process state.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The owned process declaration now lives in `kernel.primitives.checkout_coordination`; the
  register restores its `mcp`/`dashboard`/`test` mode rather than a control-plane-local role dict.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `OwnedMutableState` (lines 14-19) — One deliberately-enumerated global and the operations needed to restore it.. | `OwnedMutableState` | mcp/tests/_global_state.py:14-19 |
| Defines the function `_declared_snapshot` (lines 22-23). | `_declared_snapshot` | mcp/tests/_global_state.py:22-23 |
| Defines the function `_declared_restore` (lines 26-28). | `_declared_restore` | mcp/tests/_global_state.py:26-28 |
| Defines the function `snapshot_owned_mutable_state` (lines 42-43). | `snapshot_owned_mutable_state` | mcp/tests/_global_state.py:42-43 |
| Defines the function `restore_owned_mutable_state` (lines 46-54) — Restore every owned global, returning the complete list that changed.. | `restore_owned_mutable_state` | mcp/tests/_global_state.py:46-54 |
| Defines the function `preserve_owned_mutable_state` (lines 58-64) — Explicitly contain a production entry point whose contract is to set process state.. | `preserve_owned_mutable_state` | mcp/tests/_global_state.py:58-64 |

## Update History

- 2026-08-10T18:31+02:00 — 260731-EFA-L21: moved owned-state snapshot/restore to the kernel
  checkout execution declaration, including explicit pytest mode. Verification metadata remains
  pinned until approved closeout.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
