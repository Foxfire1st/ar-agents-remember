# mcp/src/agents_remember/application/knowledge_paging/block_pages.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**One bounded knowledge block for several seeds (MIK-R02 rule 2 applied to `read_ar_files`).** The threshold bounds the whole knowledge block of a `read_ar_files` response, not each seed's page, so N seeds never make N thresholds (ruling Q1, 19:56:40). Source bytes and onboarding are not knowledge rows and are outside it.

## Code Commentary

### Logic

- `bounded_block(entries, envelope)`: seeds are laid out in request order. Each seed's page is cut against the rendered whole block: the seeds already laid out, this page, every block-level summary the envelope adds (the threshold and MIK-R03 `currentness`), and the entries still to come.
- **The tail.** Once a seed's next row no longer fits (`cut.blocked`) or a seed's page is partial, that seed and every later one are the tail: each returns `state: "deferred"` with only its counts and a position-0 continuation. `_tail` sizes the tail so the seed's next row still has room.
- **Two kinds of prepared seed (MIK-R01).** `Prepared` is `PreparedLeaf | PreparedScope`: a path seed is prepared by the family-complete leaf read, an identity seed by the scope read. Both have the same shape (`rows`, `position`, `render`, `deferred`, `collapsed`), so `bounded_block`, `_first_row` and `_placeholder` treat them alike.
- **The collapse (ruling F2, 20:40:40).** When the deferred entries alone would not fit, the tail collapses (`_collapsed_tail`): the carried entries stay as they are, then **each kind's** prepared seeds collapse into one deferred entry listing its `seeds`, whose single continuation walks every tail seed of that kind in turn (`PreparedLeaf.collapsed`, `PreparedScope.collapsed`). Extracting `_collapsed_tail` keeps `_tail` at or below 10 under radon (L01 ruling N1, 2026-09-30 00:08:39).
- **`seed_queue_exceeded` (carried from L02 R2-1, ruling 2026-09-29 21:32:34; accepted 23:21:57).** `_collapsed` refuses a kind whose tail would queue more than `MAX_QUEUED_SEEDS` (64) seeds behind its first: one entry with `state: "refused"`, `refusalCode: "seed_queue_exceeded"`, `seedCount`, `firstSeed` and a detail telling the caller to read at most 65 seeds per request. Nothing is minted for them, so nothing raises, and the entry's size does not grow with the seed count.
- Entries that are not pages (a refusal, an unseedable path) are carried as they are.
- `alone` renders a seed's page as a block of its own, so `oversized_row` is flagged only for a row too large on its own; a row that merely does not fit beside other seeds is deferred.

### Conventions

- `envelope` is supplied by `published_intent._tree_block`, so the measured block is exactly the block returned.

### Invariants And Boundaries

- **The knowledge block stays within the threshold for any seed count.** `read_ar_files` caps files at 5; the L02 reviewer measured 2 to 64 seeds within 7,499–7,901 tokens, and since L01 a longer tail is the bounded `seed_queue_exceeded` entry (104 deep seeds stay within 8,000 tokens in `test_knowledge_leaf_read.py`).
- Every seed's selection is returned exactly once across the block and its continuations.

### Todos

- **R2-1 resolved by L01:** a tail of more than 64 queued seeds is now refused by name, `seed_queue_exceeded`, instead of raising a `ValidationError` while minting (ruling 2026-09-29 23:21:57 chose the named refusal over chaining).
- R2-2 (accepted as documented in c-04): a collapsed entry's `counts` carries `total` and `returned` but no `remaining`.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R02@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`02_bounded-continuation-accepted-by-the-mounted-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module statement: the block, the tail, the collapse, the queue refusal, and the two kinds of seed. [1]
- Laying seeds out within one threshold. [2]
- Deferred entries, or the collapsed tail when those would not fit. [3]
- The two prepared kinds, and the refusal code a tail too long for one queue earns. [4]
- Each kind's tail collapsed into one entry, or refused `seed_queue_exceeded` beyond `MAX_QUEUED_SEEDS`. [5]
- A leaf's or a scope's next row, and the smallest form of a later entry. [6]
- The envelope the block is measured in. [7]

### Cross-Repo References

No meaningful cross-repo references found: the block holds one memory tree's pages.

No cross-repo boundary is crossed by this file.
