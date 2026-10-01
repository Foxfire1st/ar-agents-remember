# mcp/src/agents_remember/application/knowledge_paging/tree_read.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The mounted `knowledge_read` over a converted memory tree: pages and continuations (MIK-R02).** A read of a memory tree is always a bounded page of one selection, and a continuation is accepted whichever surface minted it: a view token resumes that view's walk; a **leaf** token (MIK-R01, minted by the published-intent block for a path, or by an earlier `source_context` page) resumes the family-complete leaf read (since MIK-R05, of a path or of a family seed); a scope token (for an identity seed of the published-intent route, or an earlier scope page) answers `state: "page"` with the scope page as `payload`. A fresh `source_context` read with `sourcePath` is the leaf read itself.

## Code Commentary

### Logic

- `read_tree_page(request, selected, context, *, extras, workspace_root)`: a fresh read is bound to the code tree the caller named, and only that one (`_at_code_tree`), and goes to `_fresh_response`: a `source_context` read with `sourcePath` is the leaf read (`_leaf_response`); since MIK-R05 a `source_context` read naming `familyRevisionId` and no `sourcePath` is a **family seed** (`_family_response`); anything else a view walk. A resumed read goes to `_resumed_response` by the token's response kind (`leaf`, `scope` or `view`); the two were split out to keep PLR0911. A resume decodes the token (`read_continuation`), then checks the memory tree, threshold and policy, the named subject (`_subject_refusal`), the ordering and the code tree, all before any selection is read.
- **The ordering (rulings Q5 and F1).** `DEFAULT_ORDERING = "stable_ordering"` applies only when `orderingInput` is absent (`None`); an empty string keeps the base refusal `unadmitted_ordering_input` on every path. A view token's seed carries the effective ordering, and a resume reads in it.
- **The code tree (rulings Q6, F2, F4 and 21:32:34).** The token binds only the Git tree ID. On resume the objects are read from the caller's `repositoryRoot`, else the mount's workspace, and `_missing_code_tree` checks `git cat-file -e <tree>^{tree}`: a root that does not hold it, or no known root, is refused `selected_input_unavailable`, naming the root and `repositoryRoot` as the relocation input.
- `_view_response`/`_view_page` and `_scope_response`: each prepares the page extras once (`_TreeRead.prepared`: `memoryTree`, `indexComplete`, and the caller's `TreeExtras` of proofs and currentness) and lets `cut_page` render candidates, so the extras count toward the threshold.
- **The leaf response (`_leaf_response`, MIK-R01).** It calls `knowledge_leaf.prepare_leaf` with the index, the tree key, the index state, the path, the walk's code tree and the token, and renders `state: "page"`, `view: "source_context"`, `snapshot` (the memory tree ID), `completeWithinDeclaredScope`, the `continuation` at the top, the leaf page (less `page` and `continuation`) as `payload`, `page`, `memoryTree`, `indexComplete` and the `LeafCurrentness` block, cut by `cut_page`.
  - **One declared order (ruling Q7, 2026-09-29 23:21:57).** A fresh leaf read with an `orderingInput` other than `stable_ordering` is refused `invalid_payload`; a resumed one is checked against the token like every walk.
  - A leaf token whose seed is neither a path nor a family (`{"kind": "family", "id"}`, MIK-R05) is refused `continuation_unreadable`. `_subject_refusal` binds a named `sourcePath` to a path seed, and a named `familyRevisionId` to a family seed (`_SCOPE_SUBJECTS["family"]`), as it does for a scope token.
  - **The chain on refusals (MIK-R05).** When `prepare_leaf` refuses a path `registration_absent` (no entry and no governing family), `_leaf_response` merges `knowledge_leaf.absent_chain(path)` into the refusal, so the refusal carries `routeChain` stating `no_governing_family`, as the published-intent block's refusal does.
  - The policy a token is checked against is looked up per response kind (`_POLICIES`: the leaf policy `family-complete-leaf/v2` since MIK-R05's bump, the scope policy, the view policy). A token minted under `v1` is refused `continuation_binding_mismatch` (review F2, 2026-09-30 04:12:49).
- **The family seed (MIK-R05 rule 3; ruling Q1, 2026-09-30 03:32:18).** `_family_response(read, named)` accepts a text family ID, `ID@revision`, or the projected UUID of either. Before, a tree read ignored the family on this input and returned the repository-wide source-context view; the ruling calls that a defect. Database reads are unchanged.
  - `_family_spelling(read, named)` resolves the spelling through `index.text_id` into `(family ID, revision)`: the revision is `None` when no `@` is present, and empty for a trailing bare `@`.
  - `_revision_absent(read, named)` is the **one rule for a named revision**: it returns `None` when no revision is named or it is the tree's own, and otherwise a detail naming what the tree holds, refused `selector_absent`. A tree holds one revision of a family, and a bare `ID@` names none (ruling R2-1, 2026-09-30 04:45:22). Since that fix a fresh `FAM-X@` is refused, where it used to read as the bare ID.
  - **Resuming a family seed (review F4, 2026-09-30 04:12:49).** `_subject_refusal` takes a `family_id` normaliser, and `_named_subjects` compares a named `familyRevisionId` on a family-seed `leaf` token by its bare family ID (`_family_spelling(read, …)[0]`), so `ID`, `ID@rev` and the projected UUID all resume the walk, while another family is refused `continuation_binding_mismatch`. After the binding checks, `_resumed_revision_absent` holds a resume that names a revision to the same rule as a fresh read: `@99` or a bare `ID@` is refused `selector_absent` (R2-1). A different family therefore still fails first with `continuation_binding_mismatch`. The check returns a detail string, not a `PagingRefusal`, because `PagingRefusalCode` admits only paging codes.
- **Family names in the `invariant` view (rule 7).** `_TreeRead.prepared` adds `families` (`_containing_families`: the live families by ID and title, through `family_names`) to every `invariant` view page.
- `_refused` adds `threshold` to every refusal (ruling F8), and since MIK-R01 it takes the tree read and adds `memoryTree` (root, tree ID, index state, problems) and `indexComplete` to every refusal of a converted-tree read (rule 9, ruling N3 of 2026-09-30 00:08:39). The architect's R2-3 fix reworded the F4 detail for a missing root.
- **A seed the tree does not hold is refused, never answered as an empty complete view (L37, P2 task 4).** A fresh
  read goes through `_fresh_read`: `_fresh_seed_absent` asks `tree_seeds.tree_seed_refusal` about the request's
  `invariantRevisionId` and, outside the leaf view, its `familyRevisionId`, and a seed the index does not hold
  returns `selector_absent`, naming where current seeds come from. A `source_context` family seed keeps its own
  spellings and is judged by `_revision_absent`, which now also refuses a family the tree does not hold (it used
  to answer `None` for a bare unknown family ID). After the cutover every remembered database-era revision ID is
  such a seed. A continuation and a database read are unchanged.

### Conventions

- `ToolReadRequest` is a `Protocol` of the tool arguments; `ReadSubject` is the caller's subject or the token's seed.

### Invariants And Boundaries

- **No partial page on a refusal**, and nothing is kept between calls.
- `limit` does not bound a tree read; the threshold does (ruling Q4).
- **Refusals on a converted tree name the memory tree** (candidate invariant, MIK-R01 rule 9).
- **A continuation is bound to tree, policy and seed** (candidate invariant, MIK-R05): resuming under another family, path, policy or tree is refused `continuation_binding_mismatch`.
- **A revision the tree does not hold is refused `selector_absent`, on fresh read and resume alike** (candidate invariant, ruling R2-1).
- **The base defect is fixed by L01:** a `repositoryRoot` whose repository has no commit, or that is not a repository, is refused `selected_input_unavailable` naming the root (`mcp/tools/knowledge.py`, `_NoCodeTreeError`), for database and tree reads alike, where it used to raise `ValidationError` from `open_read_context`.

### Todos

- Review R2-I2: `_scope_response`'s refusal branches are not covered by the N2 identity-seed case; scope-token refusals are covered at the binding level by the L02 tests.

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

- The module statement: any surface's token, bound ordering and code tree, threshold on every response. [1]
- The default ordering, applied only when none is named. [2]
- The subject a page is read about. [3]
- The dispatch and the checks before any selection. [4]
- The walk's code tree, and a root that does not hold it. [5]
- A view page and a resumed scope page. [6]
- Every refusal states the threshold, and names the memory tree and its index state (MIK-R01 rule 9, ruling N3). [7]
- The policy each paged response is checked against, and the subjects a scope or leaf token binds, the family seed's among them. [8]
- A named subject compared with the token's seed: a family seed's `familyRevisionId` by its bare family ID (review F4). [9]
- The family seed: any spelling of the family, and one rule refusing a revision the tree does not hold, on fresh read and resume alike (ruling R2-1). [10]
- Page 1 of a `source_context` path read is the leaf read, and of a read naming only `familyRevisionId` the family seed; a resumed page follows its token's kind, a leaf token's seed being a path or a family. [11]
- The leaf page of a path or a family seed, one declared order on a fresh read (ruling Q7), and a path's `registration_absent` refusal carrying its route chain. [12]
- The `invariant` view names its families (rule 7). [13]

- Page 1 of a fresh read, or the refusal of a seed the tree does not hold. [14]
- A family or revision the tree does not hold is refused selector_absent. [15]
- A converted tree refuses a seed it does not hold, and a database read is unchanged. [16]

### Cross-Repo References

No meaningful cross-repo references found: the code tree is read from the caller's `repositoryRoot` or the mount's workspace, both the same code repository.

No cross-repo boundary is crossed by this file.
