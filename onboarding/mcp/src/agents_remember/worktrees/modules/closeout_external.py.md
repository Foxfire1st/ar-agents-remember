# mcp/src/agents_remember/worktrees/modules/closeout_external.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns the external-memory content leg of journaled closeout after code acceptance, then refreshes the disposable ledger view for consumers. A new memory-content commit carries exactly one `Code-Commit:` trailer naming the accepted code commit; cache rendering creates no commit.

## CCR-R12@v5 Current External Transaction Boundary

`external_closeout_commits` receives the accepted code change and normalized input. It refreshes existing onboarding metadata, route-overview metadata, entity fingerprints, and generated route indexes, then creates a memory-content commit only if real memory content changed. The prepared staged-index commit uses `--no-verify`; this owner does not introduce an additional quality or curator gate, except MIK-R09's closing and exact-tree validation on converted memory (section below).

Attribution is rendered before the commit object is created: `effective_input.memory_content_message(code_commit)` supplies the accepted message body and the `Code-Commit:` trailer, and `prove_git_commit` records the exact output. The later cache refresh derives from Git history and returns only informational state. Failure to render or write that cache cannot undo or block a proven memory output.

## 260928-MIK-L09 The Closeout Memory Commit Closes The Leaf's History File And Validates Its Exact Tree (MIK-R09 Rule 3)

On a converted leaf (`worktrees.knowledge_gate.leaf_memory_converted`: the memory worktree's layout marker, or the
official memory line's tip), `external_closeout_commits` now:

- closes the leaf's history file before the memory commit (`close_owner_history`, MIK-R07 rule 7): it sets
  `closed: true`, creating `knowledge/history/<leaf>.json` with no rows when the leaf wrote none; the rows are never
  rewritten. A converted leaf that names no leaf ID refuses (`_owner`);
- passes the `HistoryClosing` into `_commit_memory_content(..., closing=...)`, which, once real content is dirty,
  validates **the exact tree it is about to commit** (`_refuse_invalid_memory_commit`: captured through a private
  index with the commit's own exclusions, validated through `memory_commit_refusal(..., leaf_publication=True)`
  against the parent line's memory tip, paired with the closeout's code commit; the carried L22 obligation and the
  L27 admission base) before `begin_git_mutation`;
- restores the file on a refusal or on any failure before the commit begins (a failed tree capture, a failed or
  timed-out tip read, which is named, or `prepare_memory_cache`), so a refused closeout leaves the file as the leaf
  wrote it (review R1 F2, ruling 2026-09-30T16:07:55). The closing flag is written inside the same memory commit,
  which keeps its `Code-Commit` trailer (MIK-R09 Preservation: the paired c-12 transaction).

The curator coherence validated before this (`curator_coherence._require_knowledge_gate`) already ran the full gate over
the same bytes; this is the exact-tree backstop. **Unconverted leaves in a repository that holds no converted memory are unchanged:** `leaf_memory_converted` is
false, no file is written, and `unconverted.sh` finds the real memory commit (tree `20ccf39a…`, message and trailer)
identical between the base build and this build. Tests: `test_the_closeout_memory_commit_closes_the_history_file_and_validates_its_exact_tree`,
and through the public entry `test_the_worktree_closeout_refuses_restores_the_file_and_commits_it_closed_once_valid`
and `test_the_closeout_s_exact_tree_re_anchor_checks_the_file_it_has_just_closed` (N08).

- The converted leaf's history file is closed before the memory commit. [1]
- The owner, and the exact tree validated as a leaf publication against the parent tip. [2]
- Any failure before the commit restores the file. [3]

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

- `external_closeout_commits` resumes or creates the memory output (since MIK-R09 closing a converted leaf's history file first; since L37 after asking the cutover lock for unconverted memory), then refreshes its informational cache. [4]
- `_commit_memory_content` reuses clean content or commits attributed memory with root memory.md excluded; since MIK-R09 it validates a converted leaf's exact tree first and restores the closing on any failure before the commit. [5]
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
