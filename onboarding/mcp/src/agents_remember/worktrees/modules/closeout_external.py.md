# mcp/src/agents_remember/worktrees/modules/closeout_external.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns the external-memory content leg of journaled closeout after code acceptance, then refreshes the disposable ledger view for consumers. A new memory-content commit carries exactly one `Code-Commit:` trailer naming the accepted code commit; cache rendering creates no commit.

## CCR-R12@v5 Current External Transaction Boundary

`external_closeout_commits` receives the accepted code change and normalized input. It refreshes existing onboarding metadata, route-overview metadata, entity fingerprints, and generated route indexes, then creates a memory-content commit only if real memory content changed. The prepared staged-index commit uses `--no-verify`; this owner does not introduce an additional quality or curator gate, except MIK-R09's closing, exact-tree validation and mandatory gate on converted memory (sections below).

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
- restores the file on a refusal or on any failure before the commit begins (a failed tree capture, a failed or
  timed-out tip read, which is named, or `prepare_memory_cache`), so a refused closeout leaves the file as the leaf
  wrote it (review R1 F2, ruling 2026-09-30T16:07:55). The closing flag is written inside the same memory commit,
  which keeps its `Code-Commit` trailer (MIK-R09 Preservation: the paired c-12 transaction).

The plain closeout does not require the curator coherence record, so this call is the enforcement, not a backstop
(L37 section below). **Unconverted leaves in a repository that holds no converted memory are unchanged:** `leaf_memory_converted` is
false, no file is written, and `unconverted.sh` finds the real memory commit (tree `20ccf39a…`, message and trailer)
identical between the base build and this build. Tests: `test_the_closeout_memory_commit_closes_the_history_file_and_validates_its_exact_tree`,
and through the public entry `test_the_worktree_closeout_refuses_restores_the_file_and_commits_it_closed_once_valid`
and `test_the_closeout_s_exact_tree_re_anchor_checks_the_file_it_has_just_closed` (N08).

- The converted leaf's history file is closed before the memory commit. [1]
- The owner of the history file the closeout closes. [2]

- Any failure before the commit restores the file. [3]

## 260928-MIK-L37 The Memory Commit Is Gated And Built From The Judged Tree (MIK-R09 Rules 3 And 5)

The worktree closeout runs the mandatory invariant gate itself, and nothing more: no memory-quality suite and no
coherence record (decision record DEC-TJ0CX7). Three stored invariants describe it: INV-HWAWFT (the gate at the
closeout), INV-49E649 (the commit is the judged tree) and INV-WV1YQE (the preview reads the same verdict). They are
members of the family FAM-61DY2V (Gated leaf publication). Its guarantee covers the worktree closeout, its recovery
paths and the commit it records; a recorded landing and direct landing are outside it.

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

  Any failure before the commit begins restores the history closing and the `.gitignore` bytes
  (`_restore_ignore_file`). The closeout commits the code before the memory (`closeout.py::_closeout_commit_phase`),
  so a refusal here leaves the code commit made and no memory committed; a rerun takes that commit as it is and
  completes once the gate passes. Unconverted memory has no judged tree and stages from the working tree as before.
- **`candidate_gate_verdict(contract, code_tree)`** asks the gate about the accepted code candidate tree and the
  memory worktree's current tree and writes nothing. It answers `None` (pass), the refusal text, or
  `GATE_NOT_APPLICABLE` for a contract the gate does not govern (not a leaf, no memory worktree, unconverted memory).
  `refuse_ungated_candidate` raises that refusal for the apply's preflight; the preview reads the same verdict.
- **`require_gated_recovery(contract, code_commit, memory_commit)`** judges the tree of a memory commit that a
  resumed closeout recovered, before `external_closeout_commits` resumes with it. A commit the gate passed passes
  again; one made without the gate is refused by name.

- The validator and the mandatory gate over the leaf's exact memory output. [10]
- The exact tree the memory commit records. [11]
- The one verdict the preview and the apply's preflight read. [12]
- The preflight before the approval is claimed or anything is committed. [13]
- A recovered closeout is judged like a fresh one. [14]

- A commit whose tree is not the judged tree is refused before the memory commit's Git mutation begins. [15]

- A refused closeout takes back the ignore rule it recorded. [16]
- The public closeout refuses an open item and commits once it is answered. [17]
- A file rewritten while the gate runs is never committed unjudged. [18]

## Code Commentary

### Logic

Series closeout delegates immediately to `series_memory_closeout`, which reads the exact named memory ref and its source ancestry. Ordinary leaves resume an already recorded memory output through `resume_external_commits`; otherwise they run the raw metadata refreshes and `_commit_memory_content`.

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
- **Unconverted memory is never stamped or committed once the repository holds converted memory (L37, MIK-R09
  rule 6).** `external_closeout_commits` asks `leaf_cutover_refusal(contract, "the closeout")` right after the
  conversion probe and before `_refresh_external_memory`, and raises its refusal. The closeout as a whole writes
  nothing in that case because the closeout validator refuses by the same lock before the commit phase starts; this
  call is the backstop at the memory side.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `external_closeout_commits` resumes or creates the memory output (since MIK-R09 closing a converted leaf's history file first; since L37 after asking the cutover lock for unconverted memory, and judging a recovered memory commit before it resumes), then refreshes its informational cache. [4]
- `_commit_memory_content` reuses clean content or commits attributed memory with root memory.md excluded; since MIK-R09 it validates a converted leaf's exact tree first and restores the closing on any failure before the commit; since L37 it also runs the mandatory gate and stages the commit from the judged tree. [5]

- `_refresh_external_memory` refreshes onboarding, overview, entity, and generated index data before content publication. [6]
- `_report_memory_commit` reports verified-existing code/memory outputs without fabricated mutation evidence. [7]

The memory mutation boundary and the cache renderer have separate owners.

- Cache rendering returns informational state and creates no Git commit. [8]

- The lock is asked before any stamping or commit of unconverted memory. [9]

### Cross-Repo References

The external-memory worktree is another repository governed by the same closeout contract.

No additional cross-repository evidence applies.

## 260821-CLIVE-L2 Current Contract

The current entry point is `external_closeout_commits`. Closed admission, immutable generation input, root-journal mutation evidence, and same-generation recovery still govern memory content. Ledger-specific intent, mapping reconciliation, and commits have been removed from this owner rather than retained as a parallel route.
