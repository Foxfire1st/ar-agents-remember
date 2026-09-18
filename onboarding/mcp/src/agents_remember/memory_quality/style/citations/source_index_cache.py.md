# mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../../overview.md` |

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `ManagedCacheAuthority` (lines 40-75). | `ManagedCacheAuthority` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:40-75 |
| Defines the class `CacheControlState` (lines 79-101). | `CacheControlState` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:104-127 |
| Defines the class `ContractCacheFacts` (lines 104-121). | `ContractCacheFacts` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:130-147 |
| Defines the function `managed_cache_authority` (lines 124-142). | `managed_cache_authority` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:150-168 |
| Defines the function `_resolved_authority` (lines 145-177). | `_resolved_authority` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:145-177 |
| Defines the function `contract_cache_authority` (lines 180-189). | `contract_cache_authority` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:206-215 |
| Defines the function `open_shared_namespace` (lines 192-231) — Open one persistent same-leaf lease and perform brief root-locked admission.. | `open_shared_namespace` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:192-231 |
| Defines the function `open_index_lock` (lines 234-247). | `open_index_lock` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:549-562 |
| Defines the function `lock_exclusive` (lines 250-256). | `lock_exclusive` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:565-571 |
| Defines the class `TerminalNamespaceGuard` (lines 260-441) — One exact-leaf terminal reservation held through mutation and publication.. | `TerminalNamespaceGuard` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:522-728 |
| Defines the function `terminal_namespace_guard` (lines 445-477) — Reserve one exact contract namespace before any terminal mutation.. | `terminal_namespace_guard` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:783-816 |
| Defines the function `reclaim_managed_namespace` (lines 480-508) — Compatibility reclamation for non-contract direct callers.. | `reclaim_managed_namespace` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:819-847 |
| Defines the function `_acquisition_transition` (lines 511-544). | `_acquisition_transition` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:850-883 |
| Defines the function `_validate_active_state` (lines 547-560). | `_validate_active_state` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:886-899 |
| Defines the function `_validate_terminal_contract` (lines 563-584). | `_validate_terminal_contract` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:902-923 |
| Defines the function `_require_current_active_contract` (lines 587-598). | `_require_current_active_contract` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:874-885 |
| Defines the function `_require_current_legacy_active_contract` (lines 601-610). | `_require_current_legacy_active_contract` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:888-897 |
| Defines the function `_current_contract` (lines 613-620). | `_current_contract` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:900-907 |
| Defines the function `_required_lifecycle` (lines 623-628). | `_required_lifecycle` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:962-967 |
| Defines the function `_control_handle` (lines 631-633). | `_control_handle` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:970-972 |
| Defines the function `_read_control_state` (lines 636-669). | `_read_control_state` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:975-1008 |
| Defines the function `_write_control_state` (lines 672-679). | `_write_control_state` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1011-1018 |
| Defines the function `_restore_control_state` (lines 682-689). | `_restore_control_state` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1021-1028 |
| Defines the function `_exclusive_before_deadline` (lines 692-699). | `_exclusive_before_deadline` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1031-1038 |
| Defines the function `_namespace_ids` (lines 702-717). | `_namespace_ids` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1068-1073 |
| Defines the function `_root_lock` (lines 721-729). | `_root_lock` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1076-1085 |
| Defines the function `_try_exclusive` (lines 732-737). | `_try_exclusive` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1088-1093 |
| Defines the function `_base_result` (lines 740-745). | `_base_result` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1096-1101 |
| Defines the function `_absent_result` (lines 748-749). | `_absent_result` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1104-1105 |
| Defines the function `_lease_timeout` (lines 752-753). | `_lease_timeout` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1108-1109 |

## Update History
- 2026-09-18T01:52:52+00:00: Generated citation repair: `open_index_lock` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:549-562. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `lock_exclusive` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:565-571. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `terminal_namespace_guard` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:783-816. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `reclaim_managed_namespace` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:819-847. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_acquisition_transition` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:850-883. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_validate_active_state` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:886-899. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_validate_terminal_contract` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:902-923. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_required_lifecycle` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:962-967. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_control_handle` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:970-972. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_read_control_state` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:975-1008. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_write_control_state` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1011-1018. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_restore_control_state` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1021-1028. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_exclusive_before_deadline` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1031-1038. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_namespace_ids` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1068-1073. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_root_lock` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1076-1085. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_try_exclusive` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1088-1093. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_base_result` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1096-1101. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_absent_result` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1104-1105. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `_lease_timeout` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1108-1109. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `CacheControlState` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:104-127. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `ContractCacheFacts` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:130-147. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `managed_cache_authority` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:150-168. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `contract_cache_authority` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:206-215. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `open_index_lock` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:497-510. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `lock_exclusive` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:513-519. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `TerminalNamespaceGuard` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:522-728. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `terminal_namespace_guard` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:731-764. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `reclaim_managed_namespace` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:767-795. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_acquisition_transition` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:798-831. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_validate_active_state` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:834-847. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_validate_terminal_contract` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:850-871. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_require_current_active_contract` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:874-885. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_require_current_legacy_active_contract` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:888-897. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_current_contract` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:900-907. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_required_lifecycle` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:910-915. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_control_handle` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:918-920. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_read_control_state` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:923-956. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_write_control_state` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:959-966. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_exclusive_before_deadline` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:979-986. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_namespace_ids` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:989-1004. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_try_exclusive` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1019-1024. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_base_result` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1027-1032. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_absent_result` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1035-1036. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_lease_timeout` repointed to mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:1039-1040. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
