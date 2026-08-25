# mcp/tests/task_reopen_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/task_reopen_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:27+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Centralizes the real Git, enclosure, runtime-config, and task-document fixtures shared by task
reopen tests. It keeps reopening authority tests focused on their rule instead of repeating a
large terminal-predecessor world in every module.

## Code Commentary

### Logic

The helper publishes a terminal predecessor enclosure, constructs a completed leaf branch chain,
binds a repository-scoped runtime configuration, creates external-memory directories, and writes
leaf/master task documents with controlled identity/status variations.

### Conventions

Fixtures use real repository branches and canonical task/enclosure writers. Parameters expose only
the identity or status fact a forcing test needs to vary.

### Invariants And Boundaries

- This module is test support, not a production reopen or task-publication API.
- A reopen predecessor is terminalized through the same enclosure publication shape production
  readers consume.
- Branch lineage and task-document identity are explicit; tests must not replace them with an
  unqualified filename or guessed default branch.
- Shared construction must not weaken the assertions owned by the individual forcing modules.

### Todos

None recorded.

## Docs References

No external Domain Documentation source governs these repository-owned fixtures.

## Repo-Internal References

The source file is the direct evidence for the shared fixture boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The helper publishes an exact terminal predecessor and real super-to-leaf branch chain. | `_publish_terminal_reopen_predecessor`; `_completed_leaf_contract` | mcp/tests/task_reopen_test_support.py:30-94 |
| Runtime configuration and external-memory directories are built from the contract identity. | `_runtime_config`; `_external_memory_dirs` | mcp/tests/task_reopen_test_support.py:97-110 |
| Leaf and master documents expose controlled lifecycle, topology, and row-status variants. | `_leaf_doc`; `_master_doc` | mcp/tests/task_reopen_test_support.py:113-193 |

## Cross-Repo References

No real adjacent repository is involved; all repositories are temporary test fixtures.

## Update History

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: created for the extracted task-reopen fixture owner and verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this provenance does not certify the red Dagger gate.
