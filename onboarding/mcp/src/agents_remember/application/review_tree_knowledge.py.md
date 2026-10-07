# mcp/src/agents_remember/application/review_tree_knowledge.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The reviewer's tree view of one leaf whose memory is converted. `read_review_trees` is the port behind
`GET /api/review/trees`. For the comparison a query names it answers one of four things: the leaf-wide view
(knowledge diff, currentness of each side, worklist), the realization and proof entries of named
invariants, the unexplained-changes lane, or the classification of one changed file. Each memory side is
read through the index of its Git tree; the module opens no other database and writes no review copy.

## Code Commentary

### Which comparison, which answer

- `_comparison` picks the comparison. Without a number it is the review's own resolution
  (`resolve_review_candidate`, live or the latest record). A leaf-wide read that names a number uses the
  live resolution when that is the number, and reopens the recorded comparison otherwise. A focused read
  that names a number always reopens it from its record. Reopening needs the leaf's recorded contract;
  without one the answer is a `candidate_unresolved` refusal.
- `read_review_trees` answers `refused` with the resolver's refusal. A resolution without trees is
  `refused` with the refusal `knowledge_unavailable_refusal` names, or `not-converted` when it names none.
  Otherwise the port dispatches in this order: `file` (`_file_view`), `lane`, `invariants`
  (`_focused`), and the leaf-wide view (`_view`).
- `_focused` returns the comparison, the sides and exactly one answer. `_file_view` returns `refused` with
  the refusal of `classify_changed_path` when that function refuses the path.
- `snake_keys` re-spells every identifier-shaped camelCase key in snake_case, recursively. A key that is
  not identifier-shaped, such as a path or an ID, is left as it is. The currentness documents and the
  worklist's items, rows, changes and incomplete entries pass through it.

### The leaf-wide parts and their memo

`_leaf_wide_parts` returns the knowledge diff and the worklist view of a comparison, or a refusal.

1. It takes the memo key (`leaf_view_key`) and returns the kept parts when `remembered` has them. A
   comparison without a key is computed and never kept.
2. Otherwise `_compute_leaf_parts` computes the diff and the worklist inside one recording block and
   returns the parts, whether they are settled, and the recorded rows. The rows are also replayed into the
   caller's own recording, on success and on failure.
3. `moved_inputs` compares the rows with the key and with the file system. When nothing moved, the parts
   are returned, and kept (`remember`) when there is a key and the parts are settled.
4. When an input moved, the whole step is done once more with a key taken again
   (`_COMPUTE_ATTEMPTS` is 2). When an input moved in the second attempt as well, the answer is a refusal
   with the code `inputs_changing`, the moved inputs as `offending_input` and the action "retry once the
   named inputs stop changing". Nothing is kept.
5. A `WorklistProcessError` from the computation ends the loop at once. It becomes a refusal with the
   error's own code and action and the offending input "reviewer worklist process"; it is not computed
   again and nothing is kept.

The parts are settled only when both knowledge sides are readable, every Git read of the diff succeeded on
its first attempt, and the worklist is a computed, `complete` one.

### The worklist view

- For a live comparison `_worklist_view` hands the comparison's captured trees to
  `isolated_leaf_worklist`: the two candidate trees as `CandidateTrees` and the base commits with the tree
  the before side is read as, as `CapturedBase`. The worklist is computed in a child process; this process
  parses no knowledge tree for it. A comparison without captured base commits raises `WorklistProcessError`.
- A `complete` document from the child whose pairing is not exactly the comparison's four trees (`_bound`)
  raises `WorklistProcessError`.
- For a recorded comparison the persisted worklist is read (`read_leaf_worklist`). No document gives a
  view with source `absent`.
- `_history_rows` reads the after index's rows about every item's subject and about the subject named in
  the item's `facts.row`. `_governing` keeps, for each owner, only the rows of that owner's latest attempt
  file.

### The knowledge diff

- `_measured_tree_diff` asks Git three questions whatever the number of changed files: the raw listing
  (`_listed_changes`), one patch of the two trees (`_patches`) and one batch of blobs (`_documents`).
- Both `git diff` commands pass `PARSED_DIFF_OPTIONS` (`--no-color`, `--no-ext-diff`, `--src-prefix=a/`,
  `--dst-prefix=b/`), detect renames (`-M`) and are limited to the knowledge and onboarding roots. The listing is
  `--raw --no-abbrev -z`, so paths arrive as exact NUL-delimited values with their blob IDs.
- `_cut_patch` cuts the patch at its `diff --git` headers and binds each section to the listed path. A
  header must be one of the two spellings `_Listed.headers` derives for the path, with and without quoting
  of high bytes (`_quoted_git_path`); a type change takes two sections. A patch whose sections do not
  match the listing raises `ValueError`.
- A failed patch read is repeated once. The result of a repeated read is returned and marked incomplete,
  so it is not kept; when the repeat fails too, the patches are empty. A blob batch that fails is read
  blob by blob, also marked incomplete.
- `_Groups` sorts each indexed change into history files, records (by record ID), sources (a sidecar,
  with the invariants of its changed `realizes` and `proves` entries) or other. A patch longer than
  `PROSE_MAX_LENGTH - 200` characters is cut and marked `truncated`.

### Currentness

`side_currentness` computes `invariant_currentness` for each readable side against that side's own code
tree, the before memory at the code base and the after memory at the code candidate, and adds the index
state. An unreadable side answers with the reason.

## Evidence

- The port: refusal, not converted, one focused answer or the leaf-wide view. [23]
- A numbered leaf-wide read is live only for the current number; a focused read reopens. [24]
- The leaf-wide result with its re-keyed currentness. [25]
- Kept parts, one computation, one more when an input moved, then the refusal; process failures are refusals. [26]
- One recorded computation of diff and worklist; the rows are replayed to the caller. [27]
- Identifier-shaped keys only are re-spelled. [28]
- Three Git questions and the completeness of their reads. [29]
- The raw listing with the parsed-diff options. [30]
- One patch read, repeated once after a failure and then marked incomplete. [31]
- Patch sections are bound to the exact listed paths. [32]
- The header spellings for either quoting setting. [33]
- One blob batch, with the blob-by-blob recovery marked incomplete. [34]
- Currentness of each side at its own code tree. [35]
- The live worklist comes from the child on the captured trees and must bind them. [36]
- The pairing test against the comparison's four trees. [37]
- Rows about an item's subject and its row subject. [38]
- Each owner's rows from its latest attempt file. [39]
- A moved task document is computed once more; a second move answers inputs_changing and keeps nothing. [40]
- A child that reads no task document gives the absent view, not a refusal. [41]
- An overload from the process owner becomes the reviewer_busy refusal. [42]
- The diff and the review are identical under a hostile Git configuration. [43]
- The view captures nothing itself and is computed once per comparison. [44]
- Three Git children for the diff, with the per-file reference answers. [45]
- Literal file names select only their own patch. [46]
- The tree view on the fixture: diff groups, currentness per side, worklist. [47]
- Rows are found by the row subject an item names. [48]
- No review path opens a database other than the derived index. [49]
