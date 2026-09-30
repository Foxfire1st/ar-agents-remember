# mcp/src/agents_remember/application/knowledge_worklist/classify.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/classify.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:13:48+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Entry classification and the knowledge-side changes (MIK-R08 definitions 4, 6 and 7).** `Classifier`
gives each K_B entry its class for one run, with the facts that decided it; `knowledge_changes` compares K_B
with K_C and reports, per K_B invariant, whether its record changed and which entries were added, retired or
re-anchored, and which K_B families' records changed. Since MIK-R14 it also classifies a decision's
`reconsider_on` anchor target the same way (`classify_anchor`), without making it an entry.

## Code Commentary

### Logic

- **Classes, first that applies** (`Classifier._classify_anchor`; `_classify` passes it the entry's ID, kind,
  invariant, path and anchor):
  1. `stale_at_base`: the entry's `blob` differs from its path's blob at B, and at B its range content
     differs from the recorded `content` or its locator does not resolve.
  2. `moved_or_absent`: the path is absent at C or Git's rename detection renamed it, the symbol does not
     resolve uniquely at C, or the line range has no image at C. A symbol entry carries the mechanical
     unique match (`CodeTrees.unique_binder`) when there is one, labelled `mechanical`; an ambiguous or
     absent name gets none.
  3. `touched`: a B-to-C hunk hits the range on the B side or the C side (`_hits`). A binary pair (`None`
     hunks) counts as touched with no hunk listed.
  4. `untouched` when the C blob **is** the recorded `blob`, whatever the recorded content says.
  5. Otherwise `touched` when the range content at C differs from the recorded `content` (no hunk hit it,
     but the bytes changed), else `carried`.
- **A `reconsider_on` link's anchor (MIK-R14 rule 1, `classify_anchor`).** The link target is classified by
  the same `_classify_anchor` body, with kind `link`, no invariant, and the link's key
  (`reconsider:<DEC>#<i>/links.<j>`) as its ID. It is **not an entry**: it is not memoized in `classify` and never
  recorded among the run's classified entries. A link's anchor always names its path (asserted). The worklist's
  reconsideration registrant fires `anchor` on `touched`/`moved_or_absent` and `anchor_stale` on `stale_at_base`.
  The split of the old `_classify` body into `_classify_anchor` is moved code: radon went from 14 to 13, with no
  behaviour change (review R1).
- `Classification` holds the entry ID and kind (`EntryKind`: `realization` or `proof`, from `ProofEntry`, or
  `link`), invariant,
  path, class, anchor, both blobs, both resolutions, the hitting hunks, `renamed_to` and `unique_match`.
  `contents()` is the per-side content identity used in item IDs (`absent` where unresolved);
  `to_document()` is its facts form.
- The classifier memoizes: each entry is classified once per run (`classify`, `classified`).
- **Knowledge-side changes** (`knowledge_changes`):
  - an invariant of K_B changed when its record file (location and bytes) differs;
  - an entry ID only in K_C is `added` to its invariant; an entry ID only in K_B is `retired`; an entry that
    changed invariant is retired from one and added to the other;
  - an entry present on both sides with a different anchor or source path is `reanchored` (`_reanchor`),
    unless its K_B class is `touched`, `moved_or_absent` or `stale_at_base` (`COVERING_CLASSES`: that item
    already covers it), or it is `carried` and only `blob` and line numbers moved (`_only_mechanical`: the
    writer's carry-forward);
  - an invariant absent from K_B raises nothing (`note` ignores it);
  - a K_B family changed when its record file differs.

### Conventions

- `RAISING_CLASSES` (`touched`, `moved_or_absent`) raise `touched_invariant`; `stale_at_base` raises
  `stale_invariant` instead.

### Invariants And Boundaries

- **Definition 4 wins (architect ruling on review R1, F3).** The "content differs means touched" fallback
  applies only when C's blob differs from the entry's recorded blob. With the blob unchanged the entry is
  `untouched`, so an entry whose recorded content never matched its own blob cannot raise an item in a file
  the leaf did not change.
- **`carried` promises identical range content**, never merely an unhit range; the conservative `touched`
  closes the gap where no hunk hit but the bytes differ (the worker's filled-in choice, accepted).
- **A curator's re-anchor at an unchanged path still owes a row**: it is a knowledge-side change unless a
  covering class or the mechanical carry explains it.
- **A link anchor is classified like an entry but never becomes one** (MIK-R14): proved by
  `test_a_linked_anchor_triggers_when_touched_or_absent_and_not_otherwise`, which asserts that the run's `entries`
  stay `RLZ-`/`PRF-` only.

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The class order, the definition-4 ruling and the definition-7 rules. | "When the C blob *is* the" | mcp/src/agents_remember/application/knowledge_worklist/classify.py:1-29 |
| Raising and covering classes. | `RAISING_CLASSES`; `COVERING_CLASSES` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:69-70 |
| One entry's class and facts; the per-side content identity. | `Classification`; `contents` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:74-116 |
| Classify once per run. | `classify` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:141-146 |
| An entry's kind handed to the shared body, which decides the class with the unchanged-blob `untouched` rule. | `_classify`; `_classify_anchor` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:158-161; mcp/src/agents_remember/application/knowledge_worklist/classify.py:163-200 |
| A `reconsider_on` link's anchor, classified like an entry with kind `link` and never recorded as one. | `classify_anchor`; `EntryKind` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:148-156; mcp/src/agents_remember/application/knowledge_worklist/classify.py:68-68 |
| The hunks that hit the range; `None` for a binary pair. | `_hits` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:207-226 |
| The writer's carry-forward is not a re-anchor. | `_only_mechanical` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:260-271 |
| Added, retired and changed-record invariants; changed families. | `knowledge_changes` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:274-308 |
| A re-anchor is a change unless a covering class or the carry explains it. | `_reanchor` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:311-325 |
| The link anchor triggers on `touched` and `moved_or_absent` and joins no entries. | `test_a_linked_anchor_triggers_when_touched_or_absent_and_not_otherwise` | mcp/tests/test_reconsideration_surfacing.py:296-311 |
| Stale takes precedence. | `test_stale_at_base_takes_precedence_and_reaches_its_families_without_widening` | mcp/tests/test_knowledge_worklist.py:382-398 |
| Deletion, rename, ambiguity and a deleted range are `moved_or_absent`, with a mechanical match. | `test_moved_or_absent_covers_deletion_rename_ambiguity_and_a_deleted_range` | mcp/tests/test_knowledge_worklist.py:401-419 |
| Added, retired and re-anchored entries raise; new records do not. | `test_added_retired_and_reanchored_entries_raise_and_new_records_do_not` | mcp/tests/test_knowledge_worklist.py:488-520 |
| The writer's carry in K_C is not a change. | "def test_a_mechanical_carry_forward_in_k_c_is_not_a_change(" | mcp/tests/test_knowledge_worklist.py:523-529 |
| An unchanged blob is `untouched`; an edit elsewhere with changed range bytes is `touched`. | `test_an_unchanged_blob_is_untouched_whatever_its_recorded_content_says` | mcp/tests/test_knowledge_worklist.py:651-670 |

## Cross-Repo References

No meaningful cross-repo references found: classification reads the two parsed sides and the code trees
of one run.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): **body updated for MIK-R14.** Purpose and Logic record `classify_anchor` (a `reconsider_on` link's anchor classified by the shared body with kind `link`, never an entry, MIK-R14 rule 1), the `_classify` / `_classify_anchor` split (moved code, radon 14 to 13, review R1) and `EntryKind`; a new Invariants bullet. The `_classify` row, which the fixer normalised onto the four-line wrapper, is reworded to cite both functions; two rows added. The other rows were projected or normalised by the installed fixer, and its generated bullets are kept. No verification stamp was advanced.
- 2026-09-30T10:05:04+00:00: Generated citation repair: `RAISING_CLASSES`; `COVERING_CLASSES` repointed to mcp/src/agents_remember/application/knowledge_worklist/classify.py:69-69; mcp/src/agents_remember/application/knowledge_worklist/classify.py:70-70. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:04+00:00: Generated citation repair: `classify` repointed to mcp/src/agents_remember/application/knowledge_worklist/classify.py:141-146. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:04+00:00: Generated citation repair: `_only_mechanical` repointed to mcp/src/agents_remember/application/knowledge_worklist/classify.py:260-271. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): No content impact: this card's source is unchanged. **Reopened claim re-read and retained:** `test_a_mechanical_carry_forward_in_k_c_is_not_a_change` changed because MIK-R10 narrowed its "raises nothing" assertion to the knowledge items (`knowledge_items`); the claim still holds. The row is re-anchored on the line-exact quote "def test_a_mechanical_carry_forward_in_k_c_is_not_a_change(", and this pass's fixer bullet for it (the only generated bullet naming it) was removed. No verification stamp was advanced.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
