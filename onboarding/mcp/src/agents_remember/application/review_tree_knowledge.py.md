# mcp/src/agents_remember/application/review_tree_knowledge.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Compose the selected four-tree comparison as a leaf-wide currentness/worklist/code-facts view or exactly the requested cards, lane or changed-file answer, without embedding the standalone aggregate diff.

## Code Commentary

`read_review_trees` scopes immutable Git lookups and shared blob reads to one request. _comparison uses ordinary candidate resolution without a number; a numbered leaf-wide query uses the matching current resolution only while the leaf is live, and another number or a focused numbered query reopens the recorded comparison through its own leaf contract. A closed leaf's numbered read therefore records nothing, where it used to resolve (and so record) the delivered default first (MIK-R195 F04). Missing/legacy operands keep their named refusal or not-converted policy.

Dispatch order is file, lane, named invariants, then leaf-wide. The focused cards call now returns CardEntries: _focused forwards entries and entry_memory together. Lane/file answers and the leaf-wide answer leave entry_memory absent. Focused answers retain their comparison and side identities, with no leaf-wide excerpt population.

The leaf-wide view projects per-side currentness, worklist and code-change facts. `_view` also names the leaf's highest recorded number and the delivered notice for the shown comparison, so the page can separate the number on screen from the highest record and state whether the comparison is the pair the leaf delivered. Its two-attempt memo loop returns matching kept parts, computes otherwise, retries once when consumed inputs moved and refuses inputs_changing after another move. WorklistProcessError propagates its own code/action without an in-process fallback. Reads replay even on failure. Retention requires readable knowledge sides, a settled worklist, no delivered undecided verdict and non-null facts-state code changes.

The isolated child owns both live and recorded worklist reads over supplied trees. Live work requires base commits and a complete live document must bind the four trees; recorded operands can use tree fallbacks. The wrapper validates code facts and typed item verdicts, reports computed/persisted/absent source, and projects item/history/linkage keys through snake_keys. _bound remains the shared worklist_bound predicate. Currentness/history owners remain extracted imports, not a second local implementation.

The standalone knowledge_tree_diff API remains separate. It reads raw NUL-delimited exact paths, one aggregate patch and batched blobs, groups record/source/history/other changes and bounds patch text. Patch headers match exact paths under both Git quoting spellings; type changes take two sections. A failed patch retries the identical batch once and stays incomplete; failed blob batching falls back per blob and stays incomplete. These completeness facts do not control the leaf-wide memo. Identifier-shaped camelCase keys are projected recursively while path/id keys remain intact.

## Invariants And Boundaries

This owner writes no review database or captured replacement comparison. Supplied typed adjuncts and memo eligibility are not independent semantic approval. No aggregate memory-tree patch enters the leaf-wide response. Historical source/performance accounts below remain provenance, including already-superseded local recorded-worklist and worklist-only-settling descriptions.

## Historical predecessor account

The complete predecessor follows as provenance. Worklist-only settling, a local recorded read and local helper declarations below are superseded by the active account; the prose reference markers are historical.

### mcp/src/agents_remember/application/review_tree_knowledge.py

#### Governing Overview

[application route overview](overview.md)

#### Purpose

The reviewer's tree view of one leaf whose memory is converted. `read_review_trees` is the port behind
`GET /api/review/trees`. For the comparison a query names it answers one of four things: the leaf-wide view
(currentness of each side and worklist, not a knowledge diff), the realization and proof entries of named
invariants, the unexplained-changes lane, or the classification of one changed file. Each memory side is
read through the index of its Git tree; the module opens no other database and writes no review copy.

#### Code Commentary

Currency checks/counts still include every entry on each bound side; serialized entries list only non-current rows. Request-local immutable lookup reuse does not change those byte-level response operands, absence/refusal policy or the independently owned worklist-child memo.


##### Which comparison, which answer

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

##### The leaf-wide parts and their memo

`_leaf_wide_parts` returns the worklist view of a comparison, or a refusal. The standalone
`knowledge_tree_diff` remains exported for shared consumers but is not called on this leaf-wide path.

1. It takes the memo key (`leaf_view_key`) and returns the kept parts when `remembered` has them. A
   comparison without a key is computed and never kept.
2. Otherwise `_compute_leaf_parts` computes the worklist inside one recording block and
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

The leaf-wide parts are settled only when both knowledge sides are readable and the worklist is a
computed, `complete` one. Standalone diff-read completeness does not enter that memo judgment.

##### The worklist view

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

##### The standalone knowledge diff

`knowledge_tree_diff` and its measured helper remain in this module for shared consumers. Their
patch machinery is not part of `read_review_trees`' leaf-wide answer or its worklist memo.

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

##### Currentness

`side_currentness` computes `invariant_currentness` for each readable side against that side's own code
tree, the before memory at the code base and the after memory at the code candidate, and adds the index
state. An unreadable side answers with the reason.

`read_review_trees` resolves live vs recorded-number comparisons and fans out to focused card/lane/file reads or the leaf-wide `_view`. `_view` answers comparison, knowledge sides, code sides, currentness and worklist with no `knowledge_diff`; `_leaf_wide_parts` computes only the worklist. This removes patch computation from that route, not the retained standalone diff API or its models. Comparison memory files open in the change-set viewer instead of an embedded leaf-wide patch panel.
#### Evidence

- Historical removed latency-test assertion: three Git children for the diff, with per-file reference answers; not current test proof.
- Historical removed latency-test assertion: literal file names select only their own patch; not current test proof.
- Leaf-wide parts resolve to the worklist or a refusal (historical reference 52)

- The port: refusal, not converted, one focused answer or the leaf-wide view. (historical reference 23)
- A numbered leaf-wide read is live only for the current number; a focused read reopens. (historical reference 24)
- The leaf-wide result with its re-keyed currentness. (historical reference 25)
- Kept parts, one computation, one more when an input moved, then the refusal; process failures are refusals. (historical reference 26)
- One recorded computation of worklist only; readable sides and settled worklist govern memo eligibility and reads replay to the caller.  Anchor: file (historical reference 27)
- Identifier-shaped keys only are re-spelled. (historical reference 28)
- Three Git questions and the completeness of their reads. (historical reference 29)
- The raw listing with the parsed-diff options. (historical reference 30)
- One patch read, repeated once after a failure and then marked incomplete. (historical reference 31)
- Patch sections are bound to the exact listed paths. (historical reference 32)
- The header spellings for either quoting setting. (historical reference 33)
- One blob batch, with the blob-by-blob recovery marked incomplete. (historical reference 34)
- Currentness of each side at its own code tree. (historical reference 35)
- The live worklist comes from the child on the captured trees and must bind them. (historical reference 36)
- The pairing test against the comparison's four trees. (historical reference 37)
- Rows about an item's subject and its row subject. (historical reference 38)
- Each owner's rows from its latest attempt file. (historical reference 39)
- A moved task document is computed once more; a second move answers inputs_changing and keeps nothing. (historical reference 40)
- A child that reads no task document gives the absent view, not a refusal. (historical reference 41)
- An overload from the process owner becomes the reviewer_busy refusal. (historical reference 42)

- Each leaf-wide tree-view body and subject-review body is unchanged between clean and hostile Git configurations. The case explicitly asserts that the tree view carries no knowledge_diff; it neither compares those two bodies to each other nor measures the standalone knowledge diff. (historical reference 43)

- The view captures nothing itself and is computed once per comparison. (historical reference 44)
- The current tree-view fixture proves per-side currentness, computed worklist and linked hunks with no knowledge_diff and no leaf-wide focused entries. (historical reference 47)
- Rows are found by the row subject an item names. (historical reference 48)
- No review path opens a database other than the derived index. (historical reference 49)
- The tree view answers comparison, currentness and worklist (historical reference 50)
- The leaf-wide answer carries comparison, sides and worklist only (historical reference 51)

## Evidence

- Request-local reads choose one comparison and dispatch to the requested answer. [67]
- Leaf-wide response and memo admission retain code facts, explicit retry/refusal and replayed reads. [68]
- Only card reads forward both entries and entry_memory. [69]
- Exact aggregate patch paths and grouping remain a separate public helper. [70]
- Standalone patch/blob recovery retains incomplete state and literal path matching. [71]
- The child-owned worklist keeps actual binding, source and typed adjunct facts. [72]
