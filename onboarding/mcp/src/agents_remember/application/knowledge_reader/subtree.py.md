# mcp/src/agents_remember/application/knowledge_reader/subtree.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Every entry under a directory, in bounded pages resumed by the shared continuation (MIK-R29, review
F2).** A directory's path view is bounded to its own level (`paths.path_view`); this is the recursive list of
every live realization and proof entry at or under it. It pages exactly as every other bounded read of a
memory tree does (MIK-R02, `application/knowledge_paging`): L02's pager (`cut_page`), continuation
(`mint_continuation` / `read_continuation`) and bindings, under the selection policy
`knowledge-reader-subtree` version `1` and the view name `reader-subtree`.

## Code Commentary

### Logic

- **The selection.** `_live_entries` reads `entries_under` and keeps entries whose invariant is a live record
  (not retired, not missing), ordered by source path and then entry ID, one indivisible row per entry.
- **The binding.** A `PageBinding` of the memory tree key, the policy and version, the manifest digest of the
  ordered selection (the path and every entry ID) and the code tree ID.
- **The cut.** `cut_page` takes the longest run of whole rows whose rendered page fits the shared token
  threshold, **less the reader's own envelope**: `response_tokens` of the view, state and selection block is
  subtracted first, so the whole answer stays inside the bound (tested, F17). Each page carries the MIK-R03
  state of each invariant its rows name, computed for that page only (`_Page._states`), so the work per page
  is bounded too.
- **Resuming.** `read_continuation` refuses another view's or a garbage token (`continuation_unreadable`).
  `_resume` refuses another memory tree, policy or version (`request_binding_refusal`), another seed path, and
  a position or manifest that no longer matches (`position_refusal`), each `continuation_binding_mismatch`.
  A refusal is a typed 200 answer, `state: refused`, with no rows (accepted open point).
- **The walk's code tree (ruling 2026-09-30T10:44:14, F16).** `_at_walk_tree` makes a resumed page measure at
  the code tree the walk began at (the token's `code_tree_id`), as L02 walks do, so a code commit between
  pages cannot change what later pages measure against. A walk that began with no code tree measures at
  none. A tree the code repository no longer holds is refused by name (`continuation_binding_mismatch`,
  "no longer holds"; tested since R3-2). The replaced selection carries a note: "the code tree this walk began
  at (…); the checkout has moved since".
- **The answer's selection (ruling 2026-09-30T11:24:12, R3-1).** `subtree_page` returns
  `"selection": selection.to_document()` of the **measured** selection, which overrides the entry point's
  default envelope, so a resumed page's `selection.codeTree` and `codeNote` name the same tree as its
  `page.codeTreeId`.

### Conventions

- `threshold` is the shared bound; only a test names a smaller one (800 tokens) to cut a small selection into
  several pages.
- Continuation tokens are unsigned, as L02 designs them (ruling 11:24:12): a hand-edited token can name any
  tree the repository holds, and nothing is read that a fresh request could not read.

### Invariants And Boundaries

- **Candidate invariant (not ingested): the full subtree is paged by a continuation bound to tree, policy and
  path, and a resumed page measures at the walk's tree.** Realized by the `PageBinding`, `_resume` and
  `_at_walk_tree`, and by the measured selection block in the answer. Proved by
  `test_a_directorys_subtree_pages_through_the_shared_continuation` (rows complete and ordered, every page's
  whole answer within the bound, the sibling-prefix guard),
  `test_a_subtree_walk_measures_every_page_at_the_code_tree_it_began_at` (page 2 after a code commit reports
  page 1's tree in both `page.codeTreeId` and `selection.codeTree`, a fresh walk the new HEAD, and a token
  naming an absent tree refused) and `test_a_subtree_continuation_of_another_walk_is_refused` (another path,
  another memory tree, garbage).
- **Every answer names the code tree it measured** (R3-1): the measured selection is the one returned.
- Nothing here writes.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement of the selection, the cut and the continuation. [1]
- The view name, the policy and its version. [2]
- One page: the resume, the binding, the envelope counted inside the bound, and the measured selection returned (R3-1). [3]
- A refusal with no rows. [4]
- A resumed page at the walk's code tree, or a tree no longer held refused (F16). [5]
- Live entries by path then ID; the code tree ID bound into the token. [6]
- Another walk, tree, policy, path or position refused. [7]
- The rows and the renderer the pager measures, with states per page. [8]
- The shared pager and continuation this view uses. [9]
- The paging, walk-tree and refusal cases. [10]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
