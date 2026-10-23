# mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Retained exact-leaf cache authority and terminal cleanup fencing; no live citation index acquisition, admission or capacity-reclamation service is exposed.

## Code Commentary

### Logic

Module-level surface:

- `ManagedCacheAuthority` (class, lines 38-65)
- `CacheControlState` (class, lines 68-91)
- `ContractCacheFacts` (class, lines 94-111)
- `managed_cache_authority` (function, lines 114-132)
- `_resolved_authority` (function, lines 135-167)
- `contract_cache_authority` (function, lines 170-179)



- `TerminalNamespaceGuard` (class, lines 186-406) — One exact-leaf terminal reservation held through mutation and publication.
- `terminal_namespace_guard` (function, lines 410-447) — Reserve one exact contract namespace before any terminal mutation.



- `_validate_terminal_contract` (function, lines 432-463)


- `_current_contract` (function, lines 466-473)
- `_required_lifecycle` (function, lines 476-481)
- `_control_handle` (function, lines 484-486)
- `_read_control_state` (function, lines 489-522)
- `_write_control_state` (function, lines 525-532)
- `_restore_control_state` (function, lines 535-542)
- `_exclusive_before_deadline` (function, lines 545-552)

- `_root_lock` (function, lines 555-564)
- `_try_exclusive` (function, lines 567-572)



- `_remove_tree` (function, lines 575-581)
- `_under(path, root)` resolves the candidate path and returns true for equality with the supplied root or when that root is a resolved ancestor. `_resolved_authority` supplies resolved roots and uses this predicate to reject managed cache placement inside either code or memory. This retained containment contract survives removal of the old source-index acquisition module.

### Conventions

Terminal cleanup derives exact contract/code/memory namespace identity and requires a nonempty lifecycle. `terminal_namespace_guard` holds an exclusive control lease through mutation/publication and validates current contract/fence authority. `TerminalNamespaceGuard.complete` quarantines the live namespace, publishes contract plus terminal fence, commits a retired identity, then removes only retired garbage. When the caller passes its native terminal commit, that commit publishes after the contract and fence commit and before cleanup, and its own `committed` flag decides the failure path: an already-committed native commit marks the guard completed and re-raises with no rollback, while a pre-commit failure attempts publication/state/namespace rollback. Post-commit cleanup failure stays visible and never restores partial garbage to service. Control records are bounded at 4096 bytes and validated against exact roots, namespace and contract.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

- Resolved-path equality or ancestry detects cache placement under a supplied resolved root; authority rejects cache roots inside code or memory. [31]

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `ManagedCacheAuthority` (lines 38-65). [1]

- Defines the class `CacheControlState` (lines 68-91). [2]

- Defines the class `ContractCacheFacts` (lines 94-111). [3]

- Defines the function `managed_cache_authority` (lines 114-132). [4]

- Defines the function `_resolved_authority` (lines 135-167). [5]

- Defines the function `contract_cache_authority` (lines 170-179). [6]




- Defines the class `TerminalNamespaceGuard` (lines 182-388) — One exact-leaf terminal reservation held through mutation and publication. [10]

- Defines the function `terminal_namespace_guard` (lines 391-429) — Reserve one exact contract namespace before any terminal mutation. [11]




- Defines the function `_validate_terminal_contract` (lines 432-463). [15]



- Defines the function `_current_contract` (lines 466-473). [18]

- Defines the function `_required_lifecycle` (lines 476-481). [19]

- Defines the function `_control_handle` (lines 484-486). [20]

- Defines the function `_read_control_state` (lines 489-522). [21]

- Defines the function `_write_control_state` (lines 525-532). [22]

- Defines the function `_restore_control_state` (lines 535-542). [23]

- Defines the function `_exclusive_before_deadline` (lines 545-552). [24]


- Defines the function `_root_lock` (lines 555-564). [26]

- Defines the function `_try_exclusive` (lines 567-572). [27]
