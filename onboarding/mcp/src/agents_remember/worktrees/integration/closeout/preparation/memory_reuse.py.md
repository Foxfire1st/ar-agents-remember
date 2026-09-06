# mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | |
| lastVerifiedCommitDate | |
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Read-only proof of genuine existing memory output.

## Code Commentary

### Logic

A dirty memory candidate returns no reuse proof and leaves creation to its owner. Clean reuse proves HEAD/tree/index/physical bytes, the actual memory.md ledger blob and repository identity. Existing mappings must identify an ancestor M whose binary non-ledger entries equal the current head; older M may predate the ledger file. An absent mapping is explicitly unmapped-head. Invalid mapped content refuses instead of becoming an empty commit or an unmapped fallback.

### Conventions

Use the named source owners directly. This card describes the current uncommitted implementation; commit-based verification remains pending.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `_memory_entries` owns the corresponding behavior described above. | `_memory_entries` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py:21-38` |
| `observe_existing_memory_proof` owns the corresponding behavior described above. | `observe_existing_memory_proof` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py:41-97` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
