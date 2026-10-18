# mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Retained exact-leaf cache authority and terminal cleanup fencing; no live citation index acquisition, admission or capacity-reclamation service is exposed.

## Code Commentary

### Logic

Module-level surface:

- `ManagedCacheAuthority` (class, lines 34-61)
- `CacheControlState` (class, lines 64-87)
- `ContractCacheFacts` (class, lines 90-107)
- `managed_cache_authority` (function, lines 110-128)
- `_resolved_authority` (function, lines 131-163)
- `contract_cache_authority` (function, lines 166-175)



- `TerminalNamespaceGuard` (class, lines 178-384) — One exact-leaf terminal reservation held through mutation and publication.
- `terminal_namespace_guard` (function, lines 387-425) — Reserve one exact contract namespace before any terminal mutation.



- `_validate_terminal_contract` (function, lines 428-459)


- `_current_contract` (function, lines 462-469)
- `_required_lifecycle` (function, lines 472-477)
- `_control_handle` (function, lines 480-482)
- `_read_control_state` (function, lines 485-518)
- `_write_control_state` (function, lines 521-528)
- `_restore_control_state` (function, lines 531-538)
- `_exclusive_before_deadline` (function, lines 541-548)

- `_root_lock` (function, lines 551-560)
- `_try_exclusive` (function, lines 563-568)



- `_remove_tree` (function, lines 571-577)
- `_under(path, root)` resolves the candidate path and returns true for equality with the supplied root or when that root is a resolved ancestor. `_resolved_authority` supplies resolved roots and uses this predicate to reject managed cache placement inside either code or memory. This retained containment contract survives removal of the old source-index acquisition module.

### Conventions

Terminal cleanup derives exact contract/code/memory namespace identity and requires a nonempty lifecycle. `terminal_namespace_guard` holds an exclusive control lease through mutation/publication and validates current contract/fence authority. `TerminalNamespaceGuard.complete` quarantines the live namespace, publishes contract plus terminal fence, commits a retired identity, then removes only retired garbage. Pre-commit failure attempts publication/state/namespace rollback; post-commit cleanup failure stays visible and never restores partial garbage to service. Control records are bounded at 4096 bytes and validated against exact roots, namespace and contract.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

- Resolved-path equality or ancestry detects cache placement under a supplied resolved root; authority rejects cache roots inside code or memory. [31]

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `ManagedCacheAuthority` (lines 34-61). [1]

- Defines the class `CacheControlState` (lines 64-87). [2]

- Defines the class `ContractCacheFacts` (lines 90-107). [3]

- Defines the function `managed_cache_authority` (lines 110-128). [4]

- Defines the function `_resolved_authority` (lines 131-163). [5]

- Defines the function `contract_cache_authority` (lines 166-175). [6]




- Defines the class `TerminalNamespaceGuard` (lines 178-384) — One exact-leaf terminal reservation held through mutation and publication. [10]

- Defines the function `terminal_namespace_guard` (lines 387-425) — Reserve one exact contract namespace before any terminal mutation. [11]




- Defines the function `_validate_terminal_contract` (lines 428-459). [15]



- Defines the function `_current_contract` (lines 462-469). [18]

- Defines the function `_required_lifecycle` (lines 472-477). [19]

- Defines the function `_control_handle` (lines 480-482). [20]

- Defines the function `_read_control_state` (lines 485-518). [21]

- Defines the function `_write_control_state` (lines 521-528). [22]

- Defines the function `_restore_control_state` (lines 531-538). [23]

- Defines the function `_exclusive_before_deadline` (lines 541-548). [24]


- Defines the function `_root_lock` (lines 551-560). [26]

- Defines the function `_try_exclusive` (lines 563-568). [27]
