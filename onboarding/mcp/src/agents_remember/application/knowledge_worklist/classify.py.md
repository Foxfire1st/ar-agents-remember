# mcp/src/agents_remember/application/knowledge_worklist/classify.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/classify.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Entry classification and the knowledge-side changes (MIK-R08 definitions 4, 6 and 7).** `Classifier`
gives each K_B entry its class for one run, with the facts that decided it; `knowledge_changes` compares K_B
with K_C and reports, per K_B invariant, whether its record changed and which entries were added, retired or
re-anchored, and which K_B families' records changed.

## Code Commentary

### Logic

- **Classes, first that applies** (`Classifier._classify`):
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
- `Classification` holds the entry ID and kind (`realization` or `proof`, from `ProofEntry`), invariant,
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
| Raising and covering classes. | `RAISING_CLASSES`; `COVERING_CLASSES` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:63-64 |
| One entry's class and facts; the per-side content identity. | `Classification`; `contents` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:68-110 |
| Classify once per run. | `classify` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:135-140 |
| The class decision, with the unchanged-blob `untouched` rule. | `_classify` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:142-179 |
| The hunks that hit the range; `None` for a binary pair. | `_hits` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:186-205 |
| The writer's carry-forward is not a re-anchor. | `_only_mechanical` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:239-250 |
| Added, retired and changed-record invariants; changed families. | `knowledge_changes` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:253-287 |
| A re-anchor is a change unless a covering class or the carry explains it. | `_reanchor` | mcp/src/agents_remember/application/knowledge_worklist/classify.py:290-304 |
| Stale takes precedence. | `test_stale_at_base_takes_precedence_and_reaches_its_families_without_widening` | mcp/tests/test_knowledge_worklist.py:371-387 |
| Deletion, rename, ambiguity and a deleted range are `moved_or_absent`, with a mechanical match. | `test_moved_or_absent_covers_deletion_rename_ambiguity_and_a_deleted_range` | mcp/tests/test_knowledge_worklist.py:390-408 |
| Added, retired and re-anchored entries raise; new records do not. | `test_added_retired_and_reanchored_entries_raise_and_new_records_do_not` | mcp/tests/test_knowledge_worklist.py:477-509 |
| The writer's carry in K_C is not a change. | `test_a_mechanical_carry_forward_in_k_c_is_not_a_change` | mcp/tests/test_knowledge_worklist.py:512-518 |
| An unchanged blob is `untouched`; an edit elsewhere with changed range bytes is `touched`. | `test_an_unchanged_blob_is_untouched_whatever_its_recorded_content_says` | mcp/tests/test_knowledge_worklist.py:640-659 |

## Cross-Repo References

No meaningful cross-repo references found: classification reads the two parsed sides and the code trees
of one run.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
