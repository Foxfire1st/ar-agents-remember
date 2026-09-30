# mcp/src/agents_remember/application/knowledge_reader/selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_reader/selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:06:02+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Which memory tree the reader shows, and the code tree its MIK-R03 states are measured at (MIK-R29
rule 1).** A reader selection names one repository and one memory tree, and this module opens it into a
`ReaderSelection`: the tree's derived index (MIK-R23), where its files are read from, the code tree, and the
facts every answer's `selection` block reports. It also lists what the commit selector offers.

Three spellings are accepted:
- `published` (the default): MIK-R23 rule 6's published memory-tree selection, the scope's own memory root in
  its current captured state, through `select_knowledge_dataset`;
- a memory **commit**, by its full or abbreviated hexadecimal name only (a branch name is refused as
  `invalid-request`, review F6), read through Git objects with `KnowledgeIndexCache.for_git_tree`;
- `leaf:<scope>`: the memory worktree of an active leaf enclosure whose worktree group is `<scope>`, in its
  captured state.

## Code Commentary

### Logic

- **Converted trees only.** `_directory_selection` checks `converted_memory_tree` and `_commit_selection`
  checks that the commit holds `LAYOUT_MARKER_PATH`; a tree without it answers `not-converted` before any
  index is built. This is how unconverted memory reads stay unchanged.
- **The code tree (ruling 2026-09-30T09:42:58 Q1/N1).** For a commit, `_paired_code_tree` reads the commit's
  own `Code-Commit` pairing (`own_paired_code_commit`) and resolves its tree in the code repository; with no
  trailer, or a paired commit the code store does not hold, there is no code tree and the note says why, so
  every state reads `unverifiable`. For `published` and a leaf, `_checkout_code_tree` takes `HEAD^{tree}` of
  the scope's code checkout: the tree L03's published-intent block measures at, so the two surfaces never
  disagree. A leaf's note says that its uncommitted code is not included; capturing it would write objects
  and refs, and the reader must not write.
- **`codeSource`** is `paired-code-commit`, `checkout-head` or `none`, and `to_document` reports it beside
  `codeTree` and `codeNote`. Every answer carries this block.
- **The pinned link (N2).** A working-tree selection whose captured tree equals its `HEAD` tree carries
  `pinnedCommit` = that `HEAD`; the dashboard offers it as "pin this view to memory …", so a shared view is
  reproducible. A dirty tree offers none. A commit selection is its own pin.
- **Leaves.** `_leaf_selection` accepts only a scope listed by `_leaves`, which reads the active enclosure
  contracts directly (not abandoned, with a code worktree present), not the files catalog's cache.
- **The selector's choices.** `selection_options` returns the published tree (and whether it is converted),
  the last 40 memory commits of `HEAD` each marked converted or not (one `cat-file --batch-check` probe), and
  the live leaves. A commit list that cannot be read is `commitsState: unavailable` with the reason, never
  an empty list (review F11). Older commits are reachable by address (F10, accepted as a note).
- **`READ_FAILURES`** names what can go wrong reading a tree (APSW, OS, subprocess, authority, memory-tree,
  index mismatch, Git preparation, Unicode and `ReaderReadError`). `ValueError` and `LookupError` were
  removed so programming errors surface (F11).

### Conventions

- A refusal is a `ReaderUnavailable` with a typed `state` and a `detail`, never an empty view.
- Git is asked with `rev-parse --verify --quiet --end-of-options`, so a spelling can never become an option.

### Invariants And Boundaries

- **Every answer names the code tree it measured and its source** (a candidate invariant recorded on the
  package entry card): `to_document` always carries `codeTree`, `codeSource` and `codeNote`. Proved by
  `test_any_commit_is_selectable_by_its_hexadecimal_name_only` (`paired-code-commit`),
  `test_the_published_tree_reads_uncommitted_state_writes_nothing_and_offers_a_pin` (`checkout-head`,
  `pinnedCommit` clean against dirty) and
  `test_a_live_leafs_candidate_is_selectable_and_names_what_its_code_tree_leaves_out`.
- **A failed source is shown as partial or unavailable, never as empty.** A partial index reports
  `indexState: partial` with its `problems`; no trailer reports `codeTree: null` with the reason. Proved by
  `test_a_partial_index_and_an_unavailable_code_tree_are_named_where_they_apply`.
- Reads only: `rev-parse`, `cat-file`, `log`; the index is built into the coordination runtime's cache.
- **Revisit together with L03 gap 1** (ruling Q1/N1): if the code-tree rule changes, it changes for both
  surfaces.

### Todos

- **Revisit the code-tree rule with L03 gap 1** (ruling 2026-09-30T09:42:58 Q1/N1): the rule is confirmed
  "for now"; a code-tree selector, or a leaf's uncommitted code, would change it for the reader and the
  published-intent block together.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the three spellings and the code-tree rule. | "**The code tree** each MIK-R03 state is measured at" | mcp/src/agents_remember/application/knowledge_reader/selection.py:1-26 |
| Hexadecimal names only, and the 40 recent commits. | `_HEX`; `_RECENT_COMMITS` | mcp/src/agents_remember/application/knowledge_reader/selection.py:77-78 |
| The named read failures (F11). | `READ_FAILURES` | mcp/src/agents_remember/application/knowledge_reader/selection.py:89-99 |
| A refusal, typed and named. | `ReaderUnavailable` | mcp/src/agents_remember/application/knowledge_reader/selection.py:103-114 |
| The opened selection and the block every answer carries: code tree, source, note and pin. | `ReaderSelection` | mcp/src/agents_remember/application/knowledge_reader/selection.py:118-164 |
| The three spellings, and a branch name refused. | `open_selection` | mcp/src/agents_remember/application/knowledge_reader/selection.py:167-187 |
| A leaf only when an active enclosure has the scope. | `_leaf_selection` | mcp/src/agents_remember/application/knowledge_reader/selection.py:190-201 |
| Published and leaf: not-converted first, the captured tree, `HEAD`, the pin when clean. | `_directory_selection` | mcp/src/agents_remember/application/knowledge_reader/selection.py:204-242 |
| A commit: the layout marker, the Git-tree index, the paired code tree. | `_commit_selection` | mcp/src/agents_remember/application/knowledge_reader/selection.py:245-278 |
| `HEAD` of the checkout, with the leaf note; the `Code-Commit` pairing, or the reason there is none. | `_checkout_code_tree`; `_paired_code_tree` | mcp/src/agents_remember/application/knowledge_reader/selection.py:281-292; mcp/src/agents_remember/application/knowledge_reader/selection.py:295-309 |
| The selector's choices, and a commit list that cannot be read named. | `selection_options`; `_commit_choices`; `_recent_commits` | mcp/src/agents_remember/application/knowledge_reader/selection.py:336-356; mcp/src/agents_remember/application/knowledge_reader/selection.py:359-368; mcp/src/agents_remember/application/knowledge_reader/selection.py:371-397 |
| The active leaves, read from their contracts. | `_leaves` | mcp/src/agents_remember/application/knowledge_reader/selection.py:400-423 |
| The selection cases: hexadecimal only, published with a pin, a leaf, and a partial index with no code tree. | `test_any_commit_is_selectable_by_its_hexadecimal_name_only`; `test_the_published_tree_reads_uncommitted_state_writes_nothing_and_offers_a_pin`; `test_a_live_leafs_candidate_is_selectable_and_names_what_its_code_tree_leaves_out`; `test_a_partial_index_and_an_unavailable_code_tree_are_named_where_they_apply` | mcp/tests/test_knowledge_reader.py:957-978; mcp/tests/test_knowledge_reader.py:981-1004; mcp/tests/test_knowledge_reader.py:1007-1017; mcp/tests/test_knowledge_reader.py:1064-1083 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new module MIK-R29 adds, recording rulings 09:42:58 Q1/N1 (a memory commit uses its Code-Commit pairing; published and a leaf use HEAD of the code checkout, matching L03; every answer names codeTree, codeSource and codeNote; revisit with L03 gap 1), Q2 (the index cache is L23's design), N2 (a pinned link when the tree is clean), F6 (hexadecimal names only), F10 (accepted note) and F11 (a commit list that cannot be read is named). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
