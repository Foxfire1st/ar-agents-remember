# mcp/src/agents_remember/memory_quality/style/citations/fixer.py

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

## Evidence

### Docs References

No external Domain Documentation source is configured. This card describes the repository's own implementation and forcing contracts without an external documentation claim.

No configured external domain source.

### Repo-Internal References

The fixer composes existing source authority with the document publication owner.

- The per-run bundle now carries the verification histories and a per-document continuity cache. [1]
- Malformed source segments exclude the whole claim instead of deleting evidence. [2]
- Only accepted per-document transactions await publication. [3]
- One validated scope and source-index lease cover planning, publication and postcheck, and each repairing claim is planned with its own document's continuity. [4]
- Projection refusal returns before an Edit enters staging. [5]
- The repair outcome supplies exact projection authority and one run timestamp. [6]
- Validated previews and successful publications alone contribute repair/projection results. [7]
- An observed scoped disappearance is unmeasurable, not an empty successful scan. [8]
- Scoped normalization regenerates only anchors verified by each original source segment; it passes no continuity authority because its empty sightings can never relocate. [9]
- Null recheck and actual publication counts remain explicit in the returned result. [10]
- The continuity a relocation must prove, and the reader that resolves one document's stamp. [11]
- The existing atomic writer receives only a revalidated complete document batch. [12]

### Cross-Repo References

This file introduces no separate cross-repository protocol. Local temporary code/memory roots and their application write-scope contract remain distinct from a cross-repository authority.

No new cross-repository protocol.
