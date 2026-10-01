# mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py

## Governing Overview

[integration overview](overview.md)

## Purpose

Censuses repository-global protected code and external-memory refs and proves the exact owner permitted to use each lifecycle surface.

## Code Commentary

The resolver derives repository default, sprint-super, and active atomic-series surfaces from configured repository identity plus canonical task topology. Exact Git branch/default/worktree facts are delegated to `integration_branch_repository.py`, while the shared immutable request, surface, target, scope, and master-authority records live in `integration_branch_types.py`; this module owns their task-derived policy, rejects owner collisions, binds series and leaf contracts to their exact source/target, and supplies narrow structural guards for start, attach, sync, closeout, integrate, terminal mutation, carryover, and topology publication. Queue-release admission remains owned by the higher closeout-queue lifecycle entrypoints, preventing this low-level resolver from importing the queue and re-entering the start-contract import path. Ordinary work branches cannot alias or occupy any protected surface.

Candidate task-document publication confines each live leaf row's proposed JSON path to the exact
owning master task root as well as the configured repository task tree, then resolves the document
through `TaskDocumentTopology`'s canonical candidate resolver. This permits one atomic create
publication while preserving repository/id/kind and live-contract identity checks; sibling-master
traversal, symlink escape, foreign-repository overrides, and missing non-override documents fail
closed.

Existing atomic-series recognition resolves the canonical owner beneath
`tasks/<repository>/<owner-relative-path>`, so a task-owned series is recognized without dropping
the repository segment while foreign owners and missing contracts remain refused.

Since 260815-DAG-L13 every nature decision reads the **effective** execution nature
(`scheduling_mode.effective_execution_nature`): commanded masters resolve through
`commanded_sprint_masters` — graph sprints validate the authored graph while graph-less sprints
derive membership from the canonical `orchestrates` aliases (the atomic-sequential default,
L13-R1) — and a nature-less legacy master resolves atomic instead of failing as an unsupported
nature. An organizational master retains its sprint-super surface only under an authored graph,
and a terminal series artifact (cleanup completed/abandoned/reopened) no longer counts as a live
series when surfaces are derived; a genuinely live organizational series still refuses with
retirement guidance (`worktree_cleanup`/`worktree_abandon`).

`require_sync_worktree` now admits two exact shapes rather than assuming sync is leaf-only. A leaf
must remain an ordinary workbench. A series must prove its canonical task-owned atomic integration
refs through `require_series_contract_authority`; any other contract kind refuses. This structural
guard enables the source-pair selecting transaction without making a protected series branch an
ordinary workbench or weakening its task-derived ownership.

## 260831-LOCR-L30 Abandon Refuses A Checkpointed Master

`_require_series_task_terminal` cit:([`_require_series_task_terminal`], mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:232-278) is the guard shared by the cleanup and abandon arms of
`require_terminal_worktree`. It refuses to retire a series' integration branch when the master's task
document is `abandoned` **and** `contract.integration_status` is in `{"completed", "checkpointed"}`
cit:(["contract.integration_status in {\"completed\", \"checkpointed\"}"], mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:265-265).

Abandoning a master asserts that none of its work was taken. Once part of it landed — finally
(`completed`) or at a checkpoint of a master that is still open (`checkpointed`) — that assertion is
false, and the honest terminal route is completion: mark the rows that never integrated `abandoned`
and complete the master. The refusal message was widened with the value to match: it now reads "this
master already landed work into its source branch", because `checkpointed` is precisely the case a
partial landing used to hide — the master's line was already upstream while the contract still read
`not-started`, and that is what made a partial master's retirement look safe.

## Child-Admission Seal Removal And The `require_parent_series` Rename

The function formerly named `require_parent_series_accepting_leaves` is now
`require_parent_series` (code lines 309-330), and the seal call inside it is gone. The helper resolves
an atomic leaf's exact parent series and validates its identity: it returns `None` for organizational
direct-super work under a sprint graph
cit:(["authority.sprint_ref is not None and authority.execution_nature == \"organizational\""], mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:317-317),
refuses a non-atomic master through `_require_atomic_master`, raises
`"{operation} requires its exact parent series contract"` when the parent contract file is missing,
loads it, and proves the series identity against the leaf's task root and sprint branch. It no longer
decides whether that series accepts leaves, because the guard it used to call — the deleted
`worktrees/atomic_series_seal.py::require_series_accepting_leaves` — is gone together with its import.

The deleted predicate refused a new or reopened atomic child leaf whenever the parent series'
`(closeout_status, integration_status, cleanup)` was not `("not-started", "not-started", "pending")`.
Once `checkpointed` joined the integration vocabulary, that same reading sealed every master that took
a checkpoint landing, so a master could never admit another leaf after its first landing. The
developer ruled the seal out entirely — a master is meant to be paused and resumed, never locked by
its own landing — so the module was deleted rather than narrowed. Two docstrings here lost the word
"open" with it: `require_parent_series` now reads "Return an atomic leaf's parent series, or None for
organizational direct-super work", and `atomic_leaf_parent` (code lines 333-345) reads "Resolve the
exact atomic owner before deferring leaf-wide acceptance".

Both in-module callers follow the rename and nothing else changes: `atomic_leaf_parent` at line 342
and `_leaf_target` at line 829. Leaf admission still requires the parent's contract-keyed activation
to have reconciled and become `active`; that authority lives in the activation plane, not in a
lifecycle-cell seal.

`mcp/tests/test_lifecycle_playthrough_end_to_end.py` is the regression proof: it plays the lifecycle
in order on one real temporary Git world and asserts that a leaf commanded after a checkpoint landing
still starts.

## Invariants And Boundaries

- Protected surfaces are repo-global for a Git common directory, not local to the current sprint.
- Repository default code refs are PR/landing-plane targets and never generic local integration targets.
- Organizational leaves source directly from the sprint super; atomic leaves source from the exact series ref; the effective nature (not the declared cell) picks the lane.
- Missing, stale, ambiguous, foreign, or colliding authority fails closed before mutation.
- Series terminal writers require both the structural guard here and the ephemeral
  transaction-bound permit issued by `atomic_series_terminal.py`; no queue owns terminal authority.
- Sync may operate on a series only through exact series-contract authority; ordinary leaf and
  protected series admission remain distinct branches.
- **A landed line blocks abandonment, in either landing state.** The abandon arm must keep refusing
  whenever the integration cell records that work left the master — `completed` or `checkpointed` —
  because `checkpointed` exists to keep an unfinished master's landed content honest and therefore cannot
  be treated as "nothing was taken".

## Evidence

### Repo-Internal References

- Public census and target projection derive exact protected surfaces. [1]
- Topology publication validates candidate ownership before task facts can create a protected collision. [2]
- New-surface validation recognizes only the exact canonical atomic series contract and branch. [3]
- Sync admits either an ordinary leaf workbench or exact task-owned series authority. [4]
- The parent-series resolver renamed from `require_parent_series_accepting_leaves`: it resolves and validates the exact parent series (organizational direct-super returns `None`; a missing contract and a stale identity raise) and no longer consults a child-admission seal. [5]
- The atomic-owner resolver that follows the rename at its call site, and the leaf target that follows it at integration. [6]
- The end-to-end playthrough that proves a leaf commanded after a checkpoint landing still starts. [7]
- The terminal-task guard refuses abandon once the integration cell records a landed line, in either landing state. [8]

### Docs References

No Domain Documentation source is configured for this memory root.

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned branch authority.

## 260821-CLIVE-L2 Unified Topology Resolution

Live leaf identity validation now calls the topology's single `resolve` API with the accepted
override set. Integration authority no longer depends on a second candidate-resolution vocabulary;
the exact accepted task generation remains the input to one resolver boundary.

- Live leaf publication resolves the candidate through the unified topology API with accepted overrides. [9]

## 260821-CLIVE Queue-Binding Removal

Topology publication continues to validate current task, source, repository, and protected-branch
authority, but legacy queue candidate/sprint binding cells are no longer ownership proof. Branch
authority derives from canonical task and integration sources; disposable projection membership
cannot authorize publication.


## PDLS Reconciliation

Topology collision and deleted-owner repair logic moved into dedicated owners; this module retains the public branch-authority policy and delegates exact collision/repair mechanisms without compatibility duplication.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
