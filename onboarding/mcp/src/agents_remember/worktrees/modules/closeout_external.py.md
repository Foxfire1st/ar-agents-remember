# mcp/src/agents_remember/worktrees/modules/closeout_external.py

## Governing Overview

[Governing route overview](overview.md)
## Purpose

Owns the external-memory content leg of the admitted closeout transaction after the code output is accepted. The shared `leaf_pair_refusal` also judges recovery, recorded leaf landing and leaf integration with caller-supplied validator bases and a worklist recomputed over the exact commit trees. A new memory-content commit carries the accepted code commit in its `Code-Commit:` trailer; the later disposable ledger refresh is informational and creates no commit.
## Code Commentary

A series delegates to its series owner. An ordinary leaf resumes a recorded memory output only after the recovery gate; otherwise it refreshes entity fingerprints and generated route indexes, closes the latest owner history file, and calls `_commit_memory_content`. Card/overview stamping is removed and the corresponding refreshed lists are empty. Unconverted leaf input refuses before refresh/publication.

For converted memory, the history closing and cache ignore rule are present before `_exact_memory_tree` captures the intended output. `_refuse_ungated_memory` validates that exact tree against the parent memory tip and runs the leaf invariant gate with the exact accepted code tree. Even a clean output reused as HEAD is judged. This is the closeout's mandatory invariant gate, not an additional full MQC or curator-coherence operation. Preview reads the same candidate verdict; recovered outputs are judged against the parent line as it stands when recovery reads it. An earlier pass does not guarantee a later pass on moved inputs. A refusal after code publication names the actual code commit, says nothing is integrated and explains that rerunning completes the pair.

`_commit_memory_content` binds the contract work branch and the tip observed before judgment. It rechecks that admission, prepares the cache exclusion, and refuses a staged output different from the judged tree before mutation intent. It publishes the judged object through `publish_tree_commit`; content written after the final check cannot enter that commit and stays uncommitted. The exact accepted memory message supplies code attribution. The legacy staging helper was deleted. The admitted ordinary content leg always captures and gates the exact judged tree, sets `use_current_candidate=False`, and publishes `tree=judged`; unconverted input refuses before publication.

The restoring block runs from the first preparation until publication returns. `_restore_preparations` restores history/ignore bytes only while each still holds what this call wrote, preserving concurrent content. A provably unpublished refusal restores those preparations. A partial publication can raise after the branch moves: a switched HEAD and failed expected-old take-back may leave the memory commit reachable while preparations restore. Proof runs after successful publication return, outside that restoring block; a proof failure leaves preparations in place for recovery. Universal rollback is therefore not this contract. Code is committed before memory; a memory refusal can leave the accepted code output awaiting a successful memory leg.

The publication primitive's Git behavior is separate from prepared closeout policies; this owner does not call the removed `commit_verified_staged` helper. Root `memory.md` remains excluded from real content commits, including force-staged cache data. No cache repair can undo or become a prerequisite for a proven memory output.
## CCR-R12@v5 Current External Transaction Boundary

`external_closeout_commits` receives the accepted code change and normalized input. It refreshes entity fingerprints and generated route indexes, returning empty card/overview refreshed lists, then creates a memory-content commit only if real memory content changed. The prepared staged-index commit is published through `publish_tree_commit`; this owner does not introduce an additional quality or curator gate, except MIK-R09's closing, exact-tree validation and mandatory gate on converted memory (sections below).

Attribution is rendered before the commit object is created: `effective_input.memory_content_message(code_commit)` supplies the accepted message body and the `Code-Commit:` trailer, and `prove_git_commit` records the exact output. The later cache refresh derives from Git history and returns only informational state. Failure to render or write that cache cannot undo or block a proven memory output.
## 260928-MIK-L09 The Closeout Memory Commit Closes The Leaf's History File And Validates Its Exact Tree (MIK-R09 Rule 3)

On a converted leaf (`worktrees.knowledge_gate.leaf_memory_converted`: the memory worktree's layout marker, or the
official memory line's tip), `external_closeout_commits` now:

- closes the leaf's history file before the memory commit (`close_owner_history`, MIK-R07 rule 7): it sets
  `closed: true`, creating `knowledge/history/<leaf>.json` with no rows when the leaf wrote none; the rows are never
  rewritten. A converted leaf that names no leaf ID refuses (`_owner`);
- passes the `HistoryClosing` into `_commit_memory_content(..., closing=...)`, which validates and gates **the
  exact tree it is about to commit** before `begin_git_mutation` (`_exact_memory_tree`: captured through a private
  index with the commit's own exclusions; `_refuse_ungated_memory`: validated through `memory_commit_refusal` as a
  leaf publication against the parent line's memory tip, paired with the closeout's code commit; the carried L22
  obligation and the L27 admission base). The L37 section below describes the gate;
- restores its own unchanged prepared file on a refusal or failure before publication, preserving any concurrent edit (a failed tree capture, a failed or
  timed-out tip read, which is named, or `prepare_memory_cache`), so a refused closeout leaves the file as the leaf
  wrote it (review R1 F2, ruling 2026-09-30T16:07:55). The closing flag is written inside the same memory commit,
  which keeps its `Code-Commit` trailer (MIK-R09 Preservation: the paired c-12 transaction).

The plain closeout does not require the curator coherence record, so this call is the enforcement, not a backstop
(L37 section below). **Legacy closeout is now refused even in a never-converted repository (MIK-R46).** The earlier ungated `unconverted.sh` result is historical evidence of the retired permission, not a current closeout contract. Tests: `test_the_closeout_memory_commit_closes_the_history_file_and_validates_its_exact_tree`,
and through the public entry `test_the_worktree_closeout_refuses_restores_the_file_and_commits_it_closed_once_valid`
and `test_the_closeout_s_exact_tree_re_anchor_checks_the_file_it_has_just_closed` (N08).
## 260928-MIK-L37 The Memory Commit Is Gated And Built From The Judged Tree (MIK-R09 Rules 3 And 5)

- **`_refuse_ungated_memory(contract, code_commit, memory_tree)`** runs, over the exact memory tree with the history
  closing applied:
  - the knowledge validator as a leaf publication (`LeafPublication(memory_tree, bases, frozen=closed_out_memory(contract))`),
    against the parent line's memory tip;
  - then `leaf_gate_refusal(contract, code_tree=<the code commit's tree>, memory_tree=memory_tree)`: the worklist
    recomputed over exactly these two trees.

  An open item, an incomplete run or a validator failure raises, and the message names every finding. A failed or
  timed-out read of the parent tip or of the code commit's tree is a named refusal. No argument skips either check.
- **`_commit_memory_content`** judges before the memory commit's Git mutation begins, in this order:
  1. `ignore_memory_cache` writes the ledger cache's ignore rule when content is dirty, so the judged tree already
     holds the `.gitignore` line the commit will record;
  2. `_exact_memory_tree` captures the tree and `_refuse_ungated_memory` judges it. A converted leaf with nothing
     left to commit is judged all the same: the commit the closeout records is its `HEAD`;
  3. `prepare_memory_cache`, which removes the ledger file from the index (the one index write before the mutation
     begins; the commit excludes the ledger), then `_require_judged_tree`: the tree the commit would stage through
     the repository's own index must be the judged tree, or the closeout refuses ("changed while the gate ran");
  4. `begin_git_mutation` receives the judged tree as `expected_output_tree`, and `stage_tree` makes the index
     exactly that tree. A file written after step 3 is not committed and stays an uncommitted change.

  Any failure before the commit begins restores route-owned history/ignore bytes only while they still match this call's preparations; concurrent edits are preserved and named (`_restore_preparations`). The closeout commits the code before the memory (`closeout.py::_closeout_commit_phase`),
  so a refusal here leaves the code commit made and no memory committed; a rerun takes that commit as it is and
  completes once the gate passes. Unconverted memory has no admitted closeout content leg; its public preflight refuses first.
- **`candidate_gate_verdict(contract, code_tree)`** asks the gate about the accepted code candidate tree and the
  memory worktree's current tree and writes nothing. It answers `None` (pass), the refusal text, or
  `GATE_NOT_APPLICABLE` when the invariant gate does not govern; legacy external memory instead receives its format refusal, including the series format verdict before publication authority.
  `refuse_ungated_candidate` raises that refusal for the apply's preflight; the preview reads the same verdict.
- **`require_gated_recovery(contract, code_commit, memory_commit)`** judges the tree of a memory commit that a
  resumed closeout recovered, before `external_closeout_commits` resumes with it. A commit the gate passed passes
  again; one made without the gate is refused by name.
### Logic

Series closeout delegates immediately to `series_memory_closeout`, which reads the exact named memory ref and its source ancestry. Ordinary leaves resume an already recorded memory output through `resume_external_commits`; otherwise they run the entity-fingerprint and generated route-index refreshes and `_commit_memory_content`.

The memory writer ignores root `memory.md` when testing content dirtiness. If no actual content changed, it returns existing HEAD and reports that verified-existing output without mutation evidence. For a real content change it prepares the ignored cache location, publishes memory mutation intent, stages content with `memory.md` excluded, commits the attributed message, and proves that exact object. The final writer boundary strips a force-staged cache too. There is no lookup of cached pairings and no second ledger commit.

`refresh_memory_cache` runs only after the memory output is fixed. `MemoryCloseoutOutcome.ledger_repair` contains its informational result, not a ledger commit or recovery prerequisite.
### Conventions

Accepted messages and the `VerifiedChange` travel explicitly into their consumers. New commits publish intent and exact proof; verified-existing commits publish recovery cells without fabricated mutation evidence.
#### Invariants And Boundaries

- Only real code and memory outputs belong to the recoverable Git transaction.
- The attributed memory commit excludes root `memory.md`, including an ignored file force-staged after admission.
- Cache-only changes reuse HEAD and cannot create a maintenance commit.
- A series never enters leaf memory mutation or owns a synthetic leaf memory checkout.
- Real ref, tree, and ancestry contradictions remain recovery failures. Missing or malformed cache bytes do not.
- Direct landing retains its own journal owner; this module does not execute that route.
- **Unconverted memory is never stamped or committed by ordinary closeout, even when no converted memory exists elsewhere (MIK-R46).** `external_closeout_commits` asks `leaf_cutover_refusal(contract, "the closeout")` right after the
  conversion probe and before `_refresh_external_memory`, and raises its refusal. The closeout as a whole writes
  nothing in that case because the closeout validator refuses by the same lock before the commit phase starts; this
  call is the backstop at the memory side.
### Todos

None recorded.
## Evidence

### Repo-Internal References


- `_restore_preparations` supplies the exact current transaction boundary above. [25]

- `_require_judged_tree` supplies the exact current transaction boundary above. [26]
- `_refuse_ungated_memory` supplies the exact current transaction boundary above. [27]

- `require_gated_recovery` supplies the exact current transaction boundary above. [28]


### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.
The following current source boundaries establish the ledger-retirement behavior.
The memory mutation boundary and the cache renderer have separate owners.
### Cross-Repo References

The external-memory worktree is another repository governed by the same closeout contract.

No additional cross-repository evidence applies.
## 260821-CLIVE-L2 Current Contract

The current entry point is `external_closeout_commits`. Closed admission, immutable generation input, root-journal mutation evidence, and same-generation recovery still govern memory content. Ledger-specific intent, mapping reconciliation, and commits have been removed from this owner rather than retained as a parallel route.


- The owner of the history file the closeout closes. [31]

- Before publication, owned history closing restores only unchanged prepared bytes and preserves concurrent edits. [32]


- `_report_memory_commit` reports verified-existing code/memory outputs without fabricated mutation evidence. [36]


- The validator and the mandatory gate over the leaf's exact memory output. [38]
- The exact tree the memory commit records. [39]


- The preflight before the approval is claimed or anything is committed. [41]

- A recovered closeout is judged like a fresh one. [42]

- A commit whose tree is not the judged tree is refused before the memory commit's Git mutation begins. [43]

- Refusal preserves and names edited ignore bytes instead of overwriting them. [44]

- Cache rendering returns informational state and creates no Git commit. [45]
- The public closeout refuses an open item and commits once it is answered. [46]
- A file rewritten while the gate runs is never committed unjudged. [47]

- External refresh updates only entity fingerprints and generated indexes; card/overview refreshed lists are empty. [35]

- Card and route-overview refreshed lists are empty; actual derived work is entity fingerprints and generated indexes. [48]

- `external_closeout_commits` supplies the exact current transaction boundary above. [23]

- `_commit_memory_content` supplies the exact current transaction boundary above. [24]

- `candidate_gate_verdict` supplies the exact current transaction boundary above. [29]

- The converted leaf's history file is closed before the memory commit. [30]

- `external_closeout_commits` resumes or creates the memory output (since MIK-R09 closing a converted leaf's history file first; since L37 after asking the cutover lock for unconverted memory, and judging a recovered memory commit before it resumes), then refreshes its informational cache. [33]

- Closeout reuses clean memory or publishes the judged tree with root memory.md excluded; unpublished refusal restores only unchanged owned preparations. [34]

- The lock is asked before any stamping or commit of unconverted memory. [37]

- The one verdict the preview and the apply's preflight read. [40]
