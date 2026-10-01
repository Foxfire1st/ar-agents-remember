# mcp/src/agents_remember/application/knowledge_worklist/classify.py

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
    writer's carry-forward). **Since MIK-L33** `_reanchor` asks the public `reanchored(old, new, entry_class)` over
    the two anchor documents (source path filled in), which applies exactly this rule, and `reanchored` asks the
    public `carried_mechanically(old, new, entry_class)` for the carry exception; the worklist's behaviour is
    unchanged. The reviewer's change kinds (`application/review_change_kinds.py`) call `carried_mechanically` with
    the class this `Classifier` gives the K_B entry, keeping only that exception (review R1 F1: `touched`,
    `moved_or_absent` and `stale_at_base` exist for the worklist's own covering items, which the reviewer does not
    have), so the reviewer and the worklist share one definition-7 carry rule;
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
- **One carry rule for the worklist and the reviewer (MIK-L33):** `carried_mechanically` is the only statement of
  definition 7's carry exception; `reanchored` and MIK-R33's `implementation` fact both call it.
- **A link anchor is classified like an entry but never becomes one** (MIK-R14): proved by
  `test_a_linked_anchor_triggers_when_touched_or_absent_and_not_otherwise`, which asserts that the run's `entries`
  stay `RLZ-`/`PRF-` only.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The class order, the definition-4 ruling and the definition-7 rules. [1]
- Raising and covering classes. [2]
- One entry's class and facts; the per-side content identity. [3]
- Classify once per run. [4]
- An entry's kind handed to the shared body, which decides the class with the unchanged-blob `untouched` rule. [5]
- A `reconsider_on` link's anchor, classified like an entry with kind `link` and never recorded as one. [6]
- The hunks that hit the range; `None` for a binary pair. [7]
- The writer's carry-forward is not a re-anchor. [8]
- Added, retired and changed-record invariants; changed families. [9]
- A re-anchor is a change unless a covering class or the carry explains it; since MIK-L33 `_reanchor` asks the public `reanchored`, which asks `carried_mechanically`. [10]
- The link anchor triggers on `touched` and `moved_or_absent` and joins no entries. [11]
- Stale takes precedence. [12]
- Deletion, rename, ambiguity and a deleted range are `moved_or_absent`, with a mechanical match. [13]
- Added, retired and re-anchored entries raise; new records do not. [14]
- The writer's carry in K_C is not a change. [15]
- An unchanged blob is `untouched`; an edit elsewhere with changed range bytes is `touched`. [16]
- The two public helpers, exported (MIK-L33). [17]
- The reviewer's use: only the mechanical carry is exempt (review R1 F1). [18]

### Cross-Repo References

No meaningful cross-repo references found: classification reads the two parsed sides and the code trees
of one run.

No cross-repo boundary is crossed by this file.
