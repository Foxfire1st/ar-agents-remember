# mcp/src/agents_remember/memory_quality/style/citations/fixer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/fixer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Regenerate citation ranges from exact anchors. Tree-wide mode considers failing and duplicate-bearing claims; `--document` also normalizes passing claims in that exact document. Unrelated documents remain unchanged. Repair uses the held source-index generation and the shared exact-name oracle; malformed source lists, missing anchors and unresolved or ambiguous locations remain complete curator work orders.

Accepted edits are published as per-document transactions. A projection decline is recorded before staging and never leaves a write behind. Each repaired projection and its generated history, when a section exists, share the complete final-byte digest.

## Code Commentary

### Logic

`fix_onboarding_root` validates scope and an optional expected snapshot before opening one source-index lease. `candidates` preserves malformed evidence by excluding the complete malformed claim. `_decide` selects repair or scoped normalization, asks `_projection` to bind repaired claims, and only then stores an accepted `Edit` in `Staging.documents` with original bytes and snapshot ID.

`_publish` calls `DocumentTransaction.preview` or `publish`. A detected conflict refuses every accepted edit in that document while other document batches may succeed. Repairs and projections enter the result only after a validated preview or completed publication. `documentsWritten` counts actual publications, so it is zero for dry runs; preview projection digests describe prospective bytes.

`_postcheck` normally reuses the same source-index lease for the range checker. If a scoped document disappeared after a detected conflict, the final scope cannot be checked: `findingsRemaining` is null, `postFixRecheck.reusedLease` is false and `ok` remains false. Initially missing scoped input still refuses before acquisition. The payload contains the complete refusal and repair lists, not a sample.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to
this module. The caller owns the write guard: `fix_onboarding_root` writes wherever it is
pointed, so the onboarding root must be a leaf memory worktree, never the official memory repo.

### Invariants And Boundaries

- A projection decline changes neither that claim nor its history and contributes no successful repair count.
- A document conflict suppresses the entire accepted batch for that document, including normalization edits.
- The final digest covers every accepted source-cell edit and generated history bullet in one document.
- The caller owns write-scope authorization; a leased source index supplies immutable source authority, not a memory-file mutex.
- Final-read conflict detection and atomic replacement do not exclude an uncooperative writer after validation. A publication exception propagates; it is not converted to a successful count.

### Todos

None.

## Docs References

No external Domain Documentation source is configured. This card describes the repository's own implementation and forcing contracts without an external documentation claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

The fixer composes existing source authority with the document publication owner.

| Finding | Anchor | Source |
| --- | --- | --- |
| Malformed source segments exclude the whole claim instead of deleting evidence. | `candidates` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:209-244 |
| Only accepted per-document transactions await publication. | `Staging` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:247-252 |
| One validated scope and source-index lease cover planning, publication and postcheck. | `fix_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:255-307 |
| Projection refusal returns before an Edit enters staging. | `_decide` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:336-381 |
| The repair outcome supplies exact projection authority and one run timestamp. | `_projection` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:384-405 |
| Validated previews and successful publications alone contribute repair/projection results. | `_publish` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:408-433 |
| An observed scoped disappearance is unmeasurable, not an empty successful scan. | `_postcheck` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:310-333 |
| Scoped normalization regenerates only anchors verified by each original source segment. | `_scoped_citation` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:468-524 |
| Null recheck and actual publication counts remain explicit in the returned result. | `payload` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:527-575 |
| The existing atomic writer receives only a revalidated complete document batch. | `DocumentTransaction` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:30-99 |

## Cross-Repo References

This file introduces no separate cross-repository protocol. Local temporary code/memory roots and their application write-scope contract remain distinct from a cross-repository authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No new cross-repository protocol. | N/A | N/A |

## Update History

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Documented admission before staging, per-document conflict isolation, actual write accounting, preview digest semantics and explicit unavailable postcheck after scoped disappearance. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: refreshed for the CCR-R10
  deterministic anchor-range projection change-set (code commit 709dd076). Body now reflects the
  `Staging` seam (`fix_onboarding_root`/`_decide`), `Result.projections`,
  the per-document digest binding for staged projections, and the `payload` additions
  (`projectionCount`/`projections`/`repairToolVersion`); every module-surface
  bullet and reference row re-anchored to the post-change source ranges; verification metadata
  pinned to 709dd076.

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
