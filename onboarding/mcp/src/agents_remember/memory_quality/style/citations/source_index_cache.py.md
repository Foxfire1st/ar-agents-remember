# mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Managed citation source-index namespace, leases, and terminal fencing.

## Code Commentary

### Logic

Module-level surface:

- `ManagedCacheAuthority` (class, lines 40-75)
- `CacheControlState` (class, lines 79-101)
- `ContractCacheFacts` (class, lines 104-121)
- `managed_cache_authority` (function, lines 124-142)
- `_resolved_authority` (function, lines 145-177)
- `contract_cache_authority` (function, lines 180-189)
- `open_shared_namespace` (function, lines 192-231) — Open one persistent same-leaf lease and perform brief root-locked admission.
- `open_index_lock` (function, lines 234-247)
- `lock_exclusive` (function, lines 250-256)
- `TerminalNamespaceGuard` (class, lines 260-441) — One exact-leaf terminal reservation held through mutation and publication.
- `terminal_namespace_guard` (function, lines 445-477) — Reserve one exact contract namespace before any terminal mutation.
- `reclaim_managed_namespace` (function, lines 480-508) — Compatibility reclamation for non-contract direct callers.
- `_acquisition_transition` (function, lines 511-544)
- `_validate_active_state` (function, lines 547-560)
- `_validate_terminal_contract` (function, lines 563-584)
- `_require_current_active_contract` (function, lines 587-598)
- `_require_current_legacy_active_contract` (function, lines 601-610)
- `_current_contract` (function, lines 613-620)
- `_required_lifecycle` (function, lines 623-628)
- `_control_handle` (function, lines 631-633)
- `_read_control_state` (function, lines 636-669)
- `_write_control_state` (function, lines 672-679)
- `_restore_control_state` (function, lines 682-689)
- `_exclusive_before_deadline` (function, lines 692-699)
- `_namespace_ids` (function, lines 702-717)
- `_root_lock` (function, lines 721-729)
- `_try_exclusive` (function, lines 732-737)
- `_base_result` (function, lines 740-745)
- `_absent_result` (function, lines 748-749)
- `_lease_timeout` (function, lines 752-753)
- `_remove_tree` (function, lines 756-762)
- `_under` (function, lines 765-767)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `ManagedCacheAuthority` (lines 40-75). [1]
- Defines the class `CacheControlState` (lines 79-101). [2]
- Defines the class `ContractCacheFacts` (lines 104-121). [3]
- Defines the function `managed_cache_authority` (lines 124-142). [4]
- Defines the function `_resolved_authority` (lines 145-177). [5]
- Defines the function `contract_cache_authority` (lines 180-189). [6]
- Defines the function `open_shared_namespace` (lines 192-231) — Open one persistent same-leaf lease and perform brief root-locked admission.. [7]
- Defines the function `open_index_lock` (lines 234-247). [8]
- Defines the function `lock_exclusive` (lines 250-256). [9]
- Defines the class `TerminalNamespaceGuard` (lines 260-441) — One exact-leaf terminal reservation held through mutation and publication.. [10]
- Defines the function `terminal_namespace_guard` (lines 445-477) — Reserve one exact contract namespace before any terminal mutation.. [11]
- Defines the function `reclaim_managed_namespace` (lines 480-508) — Compatibility reclamation for non-contract direct callers.. [12]
- Defines the function `_acquisition_transition` (lines 511-544). [13]
- Defines the function `_validate_active_state` (lines 547-560). [14]
- Defines the function `_validate_terminal_contract` (lines 563-584). [15]
- Defines the function `_require_current_active_contract` (lines 587-598). [16]
- Defines the function `_require_current_legacy_active_contract` (lines 601-610). [17]
- Defines the function `_current_contract` (lines 613-620). [18]
- Defines the function `_required_lifecycle` (lines 623-628). [19]
- Defines the function `_control_handle` (lines 631-633). [20]
- Defines the function `_read_control_state` (lines 636-669). [21]
- Defines the function `_write_control_state` (lines 672-679). [22]
- Defines the function `_restore_control_state` (lines 682-689). [23]
- Defines the function `_exclusive_before_deadline` (lines 692-699). [24]
- Defines the function `_namespace_ids` (lines 702-717). [25]
- Defines the function `_root_lock` (lines 721-729). [26]
- Defines the function `_try_exclusive` (lines 732-737). [27]
- Defines the function `_base_result` (lines 740-745). [28]
- Defines the function `_absent_result` (lines 748-749). [29]
- Defines the function `_lease_timeout` (lines 752-753). [30]
