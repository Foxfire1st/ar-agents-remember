# mcp/src/agents_remember/application/knowledge_reader/selection.py

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
- a memory **commit** (full or abbreviated) or **branch**, resolved by Git to a commit and read through
  Git objects with `KnowledgeIndexCache.for_git_tree`;
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
  every state reads `unverifiable`. For `published` and a leaf, the selection observes the scope's code
  checkout through `application/worktree_code_state.py` (MIK-R73 rule 7): a clean checkout gives
  `HEAD^{tree}`, and a checkout that differs from `HEAD` is captured into a scratch index and object store
  whose store the selection holds until it closes. Nothing is written into the repository, and the block
  states `codeState` `commit` or `working-tree` beside the tree it observed, so a leaf's uncommitted code is
  measured rather than excluded.
- **`codeSource`** is `paired-code-commit`, `checkout-head` or `none`, and `to_document` reports it beside
  `codeTree` and `codeNote`. Every answer carries this block.
- **The pinned link (N2).** A working-tree selection whose captured tree equals its `HEAD` tree carries
  `pinnedCommit` = that `HEAD`; the dashboard offers it as "pin this view to memory …", so a shared view is
  reproducible. A dirty tree offers none. A commit selection is its own pin.
- **Leaves.** `_leaf_selection` accepts only a scope listed by `_leaves`, which reads the active enclosure
  contracts directly, not the files catalog's cache. The shared walk excludes notes and archives.
  Read/parse failures are skipped; a parsed contract whose task artifact resolves outside the
  repository tasks folder derived from its physical enclosure position is skipped with a warning
  naming the contract. Repository, abandoned and missing-code-worktree filters remain unchanged.
- **The selector's choices.** `selection_options` returns the published tree (and whether it is converted),
  the last 40 memory commits of `HEAD` each marked converted or not (one `cat-file --batch-check` probe), and
  the live leaves. A commit list that cannot be read is `commitsState: unavailable` with the reason, never
  an empty list (review F11). The recent list is a convenience, not an admissible-selection limit; explicit commit and branch names resolve independently of it.
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

### Name resolution and refusal

`open_selection` rejects NUL before subprocess serialization and otherwise leaves non-special names to Git. `_commit_selection` resolves `<name>^{commit}`; a name with no commit is `invalid-request` with the accepted forms. Published and leaf selections keep their existing special meanings, code-tree provenance and read-only capture rules. A branch becomes a concrete commit selection rather than a mutable branch-backed index.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- NUL is rejected explicitly; other non-special spellings are resolved as commit names. [14]
- Git resolves a concrete commit; an unresolved name is invalid-request with guidance. [15]


- The module's own statement of the three spellings and the code-tree rule. [1]
- **Historical reference account; not current evidence:** The recent-commit convenience list remains forty; accepted names include memory commits and branches. (historical reference 2)
- The named read failures (F11). [3]
- A refusal, typed and named. [4]
- The opened selection and the block every answer carries: code tree, source, note and pin. [5]

- Published and leaf spellings dispatch explicitly; other names, including branches, resolve as concrete Git commits. NUL and unresolved names return invalid-request guidance. [6]

- A leaf only when an active enclosure has the scope. [7]
- Published and leaf: not-converted first, the captured tree, `HEAD`, the pin when clean. [8]
- A commit: the layout marker, the Git-tree index, the paired code tree. [9]
- `HEAD` of the checkout, with the leaf note; the `Code-Commit` pairing, or the reason there is none. [10]
- The selector's choices, and a commit list that cannot be read named. [11]
- Active leaves exclude foreign task-document nonmembers with a named warning before the existing repository and liveness filters. [12]
- **Historical reference account; not current evidence:** Historical selection controls are retained as prior evidence only; current commit/branch admission is proved by open_selection and _commit_selection, not by a retired hexadecimal-only test name. (historical reference 13)

### Cross-Repo References

No cross-repo boundary is crossed by this file.
