# mcp/src/agents_remember/application/review_tree_knowledge.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Compose the review/trees answer for the selected four-tree comparison: a leaf-wide currentness/worklist/code-facts view, or the requested focused invariant entries, lane or changed file. The standalone aggregate memory-diff helper remains public for other consumers but is not invoked by this leaf-wide path.

## Code Commentary

### Comparison selection and focused reads

`read_review_trees` scopes immutable Git lookups and shared blob reads for one request, then delegates. Without a number, comparison selection uses the existing candidate resolver; a numbered leaf-wide query can reuse its matching live resolution, while other numbered/focused questions reopen the retained comparison through the recorded leaf contract. Missing contract and unresolved/legacy inputs retain their actual refusal policy, not a substitute current store.

Dispatch order is file, lane, named invariants, then leaf-wide view. Focused answers retain comparison/sides and their requested entry, lane or file payload, not all leaf-wide excerpts. `snake_keys` rewrites identifier-shaped mapping keys recursively while preserving path/ID keys.

### Live and recorded worklist ownership

`_worklist_view` constructs candidate/base operands from the supplied comparison and passes `trees` to `isolated_leaf_worklist` for both live and recorded paths. Live work requires captured base commits. Recorded operands may use tree fallbacks, and the child reads the persisted worklist for non-live supplied trees rather than recomputing it; moving that read into the child is not an unchanged local read location.

The wrapper returns the document plus optional `_review` adjuncts. Code-change facts are model-validated, and may be present beside a worklist-absent view. A complete live document with mismatching pairing refuses. Otherwise the view contains projected items/history/linkage plus typed `item_states` supplied by that adjunct; this composer does not invent a second gate predicate. The declared source is computed for live and persisted for recorded, with absent used when no document state exists.

Currentness and governing history have moved to `review_tree_state`; this module imports/reexports `side_currentness` and imports history under its private alias. The history owner follows each item subject and `facts.row`, keeping each owner's latest attempt. `_bound` delegates to `worklist_bound`, whose actual current comparison checks include the memory-base tree as well as its commit. Do not call that stronger predicate a token-identical move of the old local body.

### Kept parts and failure

`_view` projects worklist and code-change facts alongside currentness. `_compute_leaf_parts` records/replays consumed reads even on failure, creates `LeafViewParts(worklist, worklist.code_changes)`, and admits settling only with readable knowledge sides, a settled worklist result, no delivered undecided item state, and non-null code changes in facts state. These are caller checks; constructing the dataclass does not enforce them.

`_leaf_wide_parts` returns a matching kept value, otherwise computes under the current memo key. An unmoved, settled result with a key is offered to `remember`, whose observation checks remain separate. A moved input retries once with a fresh key; a second move returns inputs_changing. A WorklistProcessError becomes its typed refusal rather than a fallback in the serving interpreter. No aggregate memory-tree diff enters those kept parts.

### Separately retained aggregate diff

`knowledge_tree_diff` still delegates to `_measured_tree_diff`. That independent path lists knowledge/onboarding changes, reads their aggregate patch and blobs, groups record/source/history/other changes, bounds patch text and tracks read completeness. It is not removed merely because ReviewTreesResult has no knowledge_diff field.

The raw listing uses NUL-delimited paths and parsed-diff options. Patch sections are bound to exact listed paths, including C-quoted names and two-section type changes. A failed aggregate patch is retried once and remains incomplete even if retry succeeds; failed blob batching falls back per blob and also marks incompleteness. This standalone completeness does not control the leaf-wide memo.

The current BASE delta adds code facts/verdicts and changes memo eligibility, recorded-read location and binding checks; it is not preservation of every other response field or memo condition. The maintained INV-2K9NMR record is explicitly narrowed to its surviving no-aggregate-diff boundary. Historical performance observations and removed-test descriptions below are not fresh execution evidence.

## Evidence

No domain documentation source is configured. The complete current owner and actual BASE diff were read; current delegated owners are cited directly. Prior prose is retained historically, not as a second operative contract.

- Request-local lookup reuse, comparison selection and focused dispatch use the actual current path. [53]
- The root view projects currentness, worklist and supplied code-change facts. [54]
- Memo lookup, moved-input retry and process-refusal handling remain explicit. [55]
- Settling checks include decided item states and supplied code-change facts; recorded reads replay in finally. [56]
- Focused payloads and identifier-shaped key projection stay separate from the leaf-wide body. [57]
- The public standalone diff delegates to its separately measured aggregate implementation. [58]
- Aggregate diff groups records, sources, history and other without becoming a leaf-wide answer field. [59]
- Exact path listing and bounded retry retain actual standalone patch completeness. [60]
- Quoted Git paths, blob recovery and changed-entry grouping belong to the standalone diff. [61]
- Both live and recorded worklist paths consume isolated review adjuncts, typed verdicts and the current binding owner. [62]
- Side currentness is computed against its own code tree and serializes only non-current entries. [63]
- The extracted history owner follows item/row subjects and latest owner attempts. [64]
- The current pairing predicate also checks the memory-base tree. [65]
- The child reads persisted work for recorded trees and computes live work before supplying adjunct facts. [66]

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
