# mcp/src/agents_remember/application/knowledge_paging/tree_read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_paging/tree_read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T05:58:11+02:00 |
| lastVerifiedCommitHash | `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`|
| lastVerifiedCommitDate | 2026-09-30T06:21:14+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R02@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`02_bounded-continuation-accepted-by-the-mounted-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module statement: any surface's token, bound ordering and code tree, threshold on every response. | "over a converted memory tree: pages and continuations" | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:1-26 |
| The default ordering, applied only when none is named. | `DEFAULT_ORDERING`; `_requested_subject` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:112-112; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:278-287 |
| The subject a page is read about. | `ReadSubject` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:156-175 |
| The dispatch and the checks before any selection. | `read_tree_page` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:212-251 |
| The walk's code tree, and a root that does not hold it. | `_at_code_tree`; `_missing_code_tree`; `_holds_tree` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:290-306; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:309-326; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:329-334; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:319-324 |
| A view page and a resumed scope page. | `_view_response`; `_scope_response` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:393-437; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:470-522 |
| Every refusal states the threshold, and names the memory tree and its index state (MIK-R01 rule 9, ruling N3). | `_refused` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:646-660 |
| The policy each paged response is checked against, and the subjects a scope or leaf token binds, the family seed's among them. | `_POLICIES`; `_SCOPE_SUBJECTS` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:117-130 |
| A named subject compared with the token's seed: a family seed's `familyRevisionId` by its bare family ID (review F4). | `_subject_refusal`; `_named_subjects` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:348-367; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:370-382 |
| The family seed: any spelling of the family, and one rule refusing a revision the tree does not hold, on fresh read and resume alike (ruling R2-1). | `_family_response`; `_family_spelling`; `_revision_absent`; `_resumed_revision_absent` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:525-535; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:538-544; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:547-565; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:568-574 |
| Page 1 of a `source_context` path read is the leaf read, and of a read naming only `familyRevisionId` the family seed; a resumed page follows its token's kind, a leaf token's seed being a path or a family. | `_fresh_response`; `_resumed_response` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:254-262; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:265-275 |
| The leaf page of a path or a family seed, one declared order on a fresh read (ruling Q7), and a path's `registration_absent` refusal carrying its route chain. | `_leaf_response`; `absent_chain` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:577-633 |
| The `invariant` view names its families (rule 7). | `_containing_families`; `prepared` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:199-209; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:636-643 |

## Cross-Repo References

No meaningful cross-repo references found: the code tree is read from the caller's `repositoryRoot` or the mount's workspace, both the same code repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T05:58:11+02:00 — 260928-MIK-L05 curator (uncommitted change set on `ar/260928-mik-l05`, code base `31d761a241055d67b85ef3908033856b78a86a57` plus the staged and unstaged delta): MIK-R05. The family seed on `source_context` (`_family_response`, ruling Q1 of 2026-09-30 03:32:18), `_family_spelling`, and `_revision_absent`/`_resumed_revision_absent` refusing a revision the tree does not hold on fresh read and resume alike (ruling R2-1, 2026-09-30 04:45:22); `_named_subjects` normalising a named `familyRevisionId` on a family-seed resume (review F4, 04:12:49); leaf tokens with a family seed; `_SCOPE_SUBJECTS["family"]`; the `registration_absent` refusal carrying `routeChain`; `_POLICIES` at `family-complete-leaf/v2` (Q4) with the v1 token refused (F2). Two candidate invariants added. Reworded the reopened `_fresh_response` and `_leaf_response` rows and the `_POLICIES` row (re-measured `117-121` → `117-130` to hold `_SCOPE_SUBJECTS`).
- 2026-09-30T03:49:34+00:00: Generated citation repair: `_refused` repointed to mcp/src/agents_remember/application/knowledge_paging/tree_read.py:646-660. No content impact: mechanical anchor-range projection bound to citation source snapshot 778874e9f7067e0c11ceadc4ef5d81e0b76e5e12eb31479c7b3ae9bc268513ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): MIK-R01 adds the leaf response to the converted-tree read. Purpose and Logic now describe `_fresh_response`/`_resumed_response`, `_leaf_response` (with ruling Q7, one declared order), `_POLICIES`, the `invariant` view's `families` (rule 7) and the refusals that name the memory tree (ruling N3); the base-defect boundary is marked fixed (carried 2026-09-29 21:17:07) and a candidate invariant was added; the Todo now carries review R2-I2. Four rows were added and the module-statement row re-measured (`1-19` → `1-26`). **Reopened claim re-read and reworded:** the `_refused` row now says refusals name the tree; this pass's generated-repair bullet for it was removed because its claim was reworded.
- 2026-09-29T23:55:51+00:00: Generated citation repair: `ReadSubject` repointed to mcp/src/agents_remember/application/knowledge_paging/tree_read.py:151-170. No content impact: mechanical anchor-range projection bound to citation source snapshot af78c18a536ac2f00d794dbac67f4d678cae173b43b31e0e7de2b8d520b727b6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:55:51+00:00: Generated citation repair: `_at_code_tree`; `_missing_code_tree`; `_holds_tree` repointed to mcp/src/agents_remember/application/knowledge_paging/tree_read.py:280-296; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:299-316; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:319-324. No content impact: mechanical anchor-range projection bound to citation source snapshot af78c18a536ac2f00d794dbac67f4d678cae173b43b31e0e7de2b8d520b727b6; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): created this card for the new file MIK-R02 adds. It records the architect rulings of 2026-09-29 19:56:40 (Q4, Q5, Q6), 20:40:40 (F1 the empty ordering is refused; F2 no local path; F3 currentness at the walk's tree; F4 the named relocation refusal; F8 refusals state the threshold) and 21:32:34 (the tree ID plus a root check is the accepted binding; R2-3 cosmetic fixed). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
