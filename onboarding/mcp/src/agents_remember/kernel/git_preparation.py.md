# mcp/src/agents_remember/kernel/git_preparation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/git_preparation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[Owning overview](../../../overview.md)

## Purpose

Private Git preparation capability and physical output proof.

## Code Commentary

### Logic

The sealed binding names the logical repository/ref and expected old commit separately from the preparation parent, admitted tree and journal-named private root. Its live authorization callback governs create, materialize and commit actions through the sole Git runner. Physical proof reads no-follow file bytes and modes, checks directory stability, and refuses extra or missing entries, submodules and checkout transformations that alter admitted blobs; this module does not publish logical task refs or grant lifecycle approval.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870` and remains byte-identical at the recovery code candidate. Its behavior was re-read against that source during memory recovery; the existing metadata owner still owns the pending verification stamp.

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
| `GitPreparationError` owns the corresponding behavior described above. | `GitPreparationError` | `mcp/src/agents_remember/kernel/git_preparation.py:23-24` |
| `require_git_object_id` owns the corresponding behavior described above. | `require_git_object_id` | `mcp/src/agents_remember/kernel/git_preparation.py:27-30` |
| `_stat_identity` owns the corresponding behavior described above. | `_stat_identity` | `mcp/src/agents_remember/kernel/git_preparation.py:96-104` |
| `_hash_file_bytes` owns the corresponding behavior described above. | `_hash_file_bytes` | `mcp/src/agents_remember/kernel/git_preparation.py:107-116` |
| `_physical_blob` owns the corresponding behavior described above. | `_physical_blob` | `mcp/src/agents_remember/kernel/git_preparation.py:119-145` |
| `require_physical_tree` owns the corresponding behavior described above. | `require_physical_tree` | `mcp/src/agents_remember/kernel/git_preparation.py:148-188` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
