# mcp/tests/merge_case_test_support.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

**The case harness for guarded common-base merge cases**, registered as the `shared-support` owned artifact of `contract:common-base-merge-cases`. Every merge case needs the same three things, and this module owns them so no case re-derives them:

- **Authored datasets.** Each state is written through the real store operation — schema created by the store, rows inserted by the store's own create operations with real provenance envelopes — and then closed through a SQLite backup, so a case measures datasets the package itself produced rather than hand-built files.
- **A real Git branching scenario.** The base dataset is committed, and each side is a *child commit of that same commit* holding its own dataset, so the common base is a fact of the commit graph rather than of the fixture's own bookkeeping. The three files a case merges are checked back out of those commits through Git, which is what makes the ancestry evidence and the datasets agree.
- **The measurements a claim needs.** Logical identities, per-table row sets, file digests and journal peers are read through separate read-only connections, so "both sides' edits survived" and "the inputs did not move" are measured rather than asserted.

It is test support, not production code: it decides nothing, holds no policy, and the only writes it performs are the ones a case explicitly asks for.

## Code Commentary

### Logic

`new_case` creates one case's world (a repository namespace and private paths); `build_case(base_shape=…, shape=…)` builds the complete case. **Both shape callbacks run before the Git scenario is built**, so a case that needs an unusual state gets it inside the commits instead of having to rewrite the repository afterwards — that ordering is what keeps the ancestry evidence and the datasets true statements about each other. `base_shape` runs on the base state and `shape` runs after the two sides are derived; the two sides always diverge by their own successor revisions and their own identities, and anything more specific (a same-field label conflict, a tampered sealed revision, a removed anchor) arrives through `shape` so the commit graph is built from the states the case means to merge.

State authoring goes through the store: `author_base_state` (through the real operations, then closed through SQLite's own backup), `derive_state` (copy one closed dataset to a path a case will change through the store), and the per-edit helpers `add_revision` (a successor is a new revision naming its predecessor — nothing here edits a sealed row, which is the only legitimate side shape for revision content), `add_invariant`, `set_label` (the one mutable authored edit), `delete_anchor`, `add_anchor`, `add_realization_claim`, `add_family_member`, `add_family`, `add_family_revision`. `_execute` runs one explicit statement with foreign keys enforced.

The Git half: `build_git_world` commits the three datasets into one temporary repository, `_commit_state` commits one dataset as the working tree's only file, and `materialize_commit` exports one commit's dataset file through Git and writes it to a case path. `_git` runs every scenario Git command through the package's **single** runner and refuses a failure.

The measurement half: `table_rows`, `row_counts`, `file_digest`, `journal_peer_names`, `statements_of`, `labels_of` and `revision_id_for`, each read through a separate read-only connection.

### Conventions

- `GitBranchWorld` / `MergeCase` hold one case's world; `state_path(role)`, `identity(role)`, `merge_inputs()` and `databases_by_role()` are the readers the cases use, so no case addresses a raw path.
- `copy_closed` normalises the copy's journal mode, because a case must merge closed files and a backup destination inherits the source's journal mode.
- **`_read_committed_blob` is the one binary read in the harness, and it deliberately does not go through the package's text-decoding runner**: a dataset is bytes, and a runner that decodes to text with `surrogateescape` would hand back something that is not the blob Git stored. The read is read-only and scoped to a repository this fixture created.

### Invariants And Boundaries

- **The base commit is a real commit and each side is a child of it**, so a history with exactly one common base is a property of the repository rather than of the fixture's bookkeeping. Nothing outside `work` is touched: the repository is created here, its objects are its own, and no ref outside it exists.
- **Rows are authored through the store, not by direct INSERT**, so a case measures datasets this package could have produced. `_insert_revision` in the unit module is the documented exception, and it belongs to that case's subject (two independent authors colliding) rather than to this harness.
- **It decides nothing.** No policy, no expectation and no refusal lives here; a case states its own assertions.
- **Boundary.** This is test support and it is not importable by production code. Its registered consumers are exactly the two merge test modules.

### Todos

None recorded for this slice.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The harness's three responsibilities and the statement that it holds no policy. [1]
- The one case world and the readers a case uses instead of raw paths. [2]
- The base state authored through the real store operations and closed through SQLite's own backup. [3]
- The successor rule: a new revision naming its predecessor, never an edit of a sealed row. [4]
- The three-commit world whose base is the sides' parent, and the per-commit dataset export. [5]
- The one binary read, and why it does not go through the text-decoding runner. [6]
- The build order that puts an unusual state inside the commits. [7]
- The measurement helpers that make input preservation and survival measured rather than asserted. [8]
- The registered artifact that makes this harness an owned contract rather than a private helper. [9]
- The unit-side consuming module, which drives the disjoint-edit survival case. [10]
- The integration-side consuming module, whose docstring states which integrity checks a case can reach. [11]
- The store operations the authored states go through. [12]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
- The registered artifact that makes this harness an owned contract rather than a private helper. [13]
- **The consuming module that drives the harness's own deletion case, cited at the definition the claim is about.** [14]
- **The boundary module that supplies the conflict-row and final-integrity cases, cited at its own module docstring.** [15]
