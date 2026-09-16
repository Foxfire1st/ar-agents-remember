# mcp/src/agents_remember/memory_quality/style/citations/fixer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/fixer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `723fd2f1becc130d85d7a6b285b93115be0df852` |
| lastVerifiedCommitDate | 2026-09-13T02:07:03+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Regenerate citation ranges from exact anchors. Tree-wide mode considers failing and duplicate-bearing claims; `--document` also normalizes passing claims in that exact document. Unrelated documents remain unchanged. Repair uses the held source-index generation and the shared exact-name oracle; malformed source lists, missing anchors and unresolved or ambiguous locations remain complete curator work orders.

Since 260831-LOCR-L33 the walk also carries the **verification provenance** a tree-wide relocation has to prove itself against: `Walk.histories` is one `provenance.Histories` over the code and memory roots, and `Walk.continuity(document)` resolves one memory document's `repair.Continuity` from its own `lastVerifiedCommitHash`, cached per document so it is resolved at most once per run. `fix_onboarding_root` passes that continuity into `repair.plan`, which is what lets a legitimate move repair while an unprovable or kind-changing match refuses.

Accepted edits are published as per-document transactions. A projection decline is recorded before staging and never leaves a write behind. Each repaired projection and its generated history, when a section exists, share the complete final-byte digest.

## Code Commentary

### Logic

`Walk` (class, lines 201-220) is the per-run bundle: the trees, sources, documents, result, plus `histories: provenance.Histories` and an `origins` cache. Its `__post_init__` builds the histories object; `Walk.continuity(document)` memoizes `repair.continuity_for(document, trees, histories)` per document.

`fix_onboarding_root` validates scope and an optional expected snapshot before opening one source-index lease. `candidates` preserves malformed evidence by excluding the complete malformed claim. `_decide` selects repair or scoped normalization, asks `_projection` to bind repaired claims, and only then stores an accepted `Edit` in `Staging.documents` with original bytes and snapshot ID. Each repairing claim is planned with `walk.continuity(one.document)`; the scoped normalization path deliberately passes `None`, because `_scoped_citation`'s empty `Sightings` can never relocate and therefore reaches no cross-file decision that needs continuity authority — passing `None` there is a proof that no relocation is possible, not a gap.

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
- **Continuity is resolved per document and cached for the run.** `Walk.continuity` memoizes on the
  document path, so a relocation decision reads one document's verification provenance without
  re-reading its metadata or re-resolving its stamp per claim.
- **The scoped pass carries no continuity authority on purpose.** `_scoped_citation` passes `None`
  because its empty `Sightings` make relocation impossible; a caller that reaches a cross-file
  decision must supply real continuity or the relocation is refused.
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
| The per-run bundle now carries the verification histories and a per-document continuity cache. | `Walk`; `Walk.continuity` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:201-220 |
| Malformed source segments exclude the whole claim instead of deleting evidence. | "def candidates(" | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:223-258 |
| Only accepted per-document transactions await publication. | `Staging` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:261-266 |
| One validated scope and source-index lease cover planning, publication and postcheck, and each repairing claim is planned with its own document's continuity. | `fix_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:269-325 |
| Projection refusal returns before an Edit enters staging. | `_decide` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:354-399 |
| The repair outcome supplies exact projection authority and one run timestamp. | `_projection` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:402-423 |
| Validated previews and successful publications alone contribute repair/projection results. | `_publish` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:426-451 |
| An observed scoped disappearance is unmeasurable, not an empty successful scan. | `_postcheck` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:328-351 |
| Scoped normalization regenerates only anchors verified by each original source segment; it passes no continuity authority because its empty sightings can never relocate. | `_scoped_citation` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:486-544 |
| Null recheck and actual publication counts remain explicit in the returned result. | `payload` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:547-595 |
| The continuity a relocation must prove, and the reader that resolves one document's stamp. | `Continuity`; `continuity_for` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:159-240; mcp/src/agents_remember/memory_quality/style/citations/repair.py:243-253 |
| The existing atomic writer receives only a revalidated complete document batch. | `DocumentTransaction` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:30-99 |

## Cross-Repo References

This file introduces no separate cross-repository protocol. Local temporary code/memory roots and their application write-scope contract remain distinct from a cross-repository authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No new cross-repository protocol. | N/A | N/A |

## Update History

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded that `Walk` now carries
  `provenance.Histories` (built in `__post_init__`) plus a per-document `origins` cache, that
  `Walk.continuity(document)` resolves one document's `repair.Continuity` at most once per run, and
  that `fix_onboarding_root` passes it into `repair.plan` so a tree-wide relocation has to prove
  continuity. Recorded that `_scoped_citation` passes `None` **deliberately** — its empty `Sightings`
  can never relocate, so it reaches no cross-file decision that needs continuity authority — and
  added the corresponding invariants. All stale reference ranges re-measured against the current
  source. Verification metadata remains closeout-owned; no acceptance claim.

- 2026-09-09T02:49:53+02:00 — CCR-L38 bounded inherited claim reconciliation: replaced the generic local-variable anchor with the exact candidate collector declaration and current body range. Source hashes: mcp/src/agents_remember/memory_quality/style/citations/fixer.py=db1b9921b32325b4b7ab7f39969296dc154b004bea6a3b4eb55ad917b9f5a682; verification metadata remains unchanged.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=db1b9921b32325b4b7ab7f39969296dc154b004bea6a3b4eb55ad917b9f5a682; verification metadata remains unchanged because commit-owned realization is pending.


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
