# mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:45+02:00 |
| lastVerifiedCommitHash | `e0820b04a499cbfb2079c78485346c50917a238a` |
| lastVerifiedCommitDate | 2026-09-13T18:02:04+02:00|
| governingOverview | `overview.md` |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public census and target projection derive exact protected surfaces. | `integration_surfaces`, `integration_targets` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:64-67; mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:68-133 |
| Topology publication validates candidate ownership before task facts can create a protected collision. | `require_topology_publication_authority`, `require_topology_migration_authority` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:441-476; mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:477-504 |
| New-surface validation recognizes only the exact canonical atomic series contract and branch. | `_atomic_surface_has_series` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:582-598 |
| Sync admits either an ordinary leaf workbench or exact task-owned series authority. | `require_sync_worktree` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:348-359 |
| The parent-series resolver renamed from `require_parent_series_accepting_leaves`: it resolves and validates the exact parent series (organizational direct-super returns `None`; a missing contract and a stale identity raise) and no longer consults a child-admission seal. | `require_parent_series`; "authority.sprint_ref is not None and authority.execution_nature == \"organizational\"" | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:309-330; mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:317-317 |
| The atomic-owner resolver that follows the rename at its call site, and the leaf target that follows it at integration. | `atomic_leaf_parent`; `require_parent_series` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:333-345; mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:829-833 |
| The end-to-end playthrough that proves a leaf commanded after a checkpoint landing still starts. | `LifecyclePlaythroughTests` | mcp/tests/test_lifecycle_playthrough_end_to_end.py:62-169 |
| The terminal-task guard refuses abandon once the integration cell records a landed line, in either landing state. | `_require_series_task_terminal`; "contract.integration_status in {\"completed\", \"checkpointed\"}" | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:232-278; mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:265-265 |

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned branch authority.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260821-CLIVE-L2 Unified Topology Resolution

Live leaf identity validation now calls the topology's single `resolve` API with the accepted
override set. Integration authority no longer depends on a second candidate-resolution vocabulary;
the exact accepted task generation remains the input to one resolver boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Live leaf publication resolves the candidate through the unified topology API with accepted overrides. | `require_topology_publication_authority` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:441-476 |

## 260821-CLIVE Queue-Binding Removal

Topology publication continues to validate current task, source, repository, and protected-branch
authority, but legacy queue candidate/sprint binding cells are no longer ownership proof. Branch
authority derives from canonical task and integration sources; disposable projection membership
cannot authorize publication.


## PDLS Reconciliation

Topology collision and deleted-owner repair logic moved into dedicated owners; this module retains the public branch-authority policy and delegates exact collision/repair mechanisms without compatibility duplication.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
## Update History
- 2026-09-13T20:42+02:00 — Child-admission seal removal (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): recorded that
  `require_parent_series_accepting_leaves` is renamed `require_parent_series` (code lines 309-330),
  that the deleted `worktrees/atomic_series_seal.py::require_series_accepting_leaves` call and its
  import are gone, and that the helper now resolves and validates the exact parent series without
  deciding whether it accepts leaves. Recorded the two docstring corrections that dropped the word
  "open", the surviving behaviour (organizational direct-super returns `None`, `_require_atomic_master`
  refuses a non-atomic master, a missing parent contract and a stale series identity still raise), the
  two in-module call sites (lines 342 and 829), and the playthrough module as the proof that a master
  is not locked by its own landing. Added two reference rows. Also re-derived every other citation on
  this card: the change removed one import above the former line 233 and one call above the former
  line 330, so ranges before that call shifted by one and ranges after it by two —
  `_require_series_task_terminal` 233-279 → 232-278 with its
  `contract.integration_status in {"completed", "checkpointed"}` anchor 266-266 → 265-265,
  `integration_surfaces`/`integration_targets` 65-68 and 69-134 → 64-67 and 68-133,
  `require_sync_worktree` 350-361 → 348-359, `require_topology_publication_authority` 443-478 →
  441-476, `require_topology_migration_authority` 479-506 → 477-504 and `_atomic_surface_has_series`
  584-600 → 582-598. Claim wording is unchanged for those rows; only the ranges moved. Verification
  metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T18:02+02:00 — 260831-LOCR-L36 terminology: `checkpointed` keeps an unfinished master's
  landed content honest (the checkpoint is a partial publication, not a pause). Wording only; the
  abandon refusal this invariant protects is unchanged and no verification stamp advanced.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: recorded that the shared
  `_require_series_task_terminal` guard now refuses abandon when the integration cell reads
  `checkpointed` as well as `completed`, why a landed line blocks abandonment in both landing states,
  and the widened refusal wording; re-derived the reference ranges in this card. Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `require_sync_worktree` repointed to mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:347-356. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `require_topology_publication_authority` repointed to mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:440-473. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `_atomic_surface_has_series` repointed to mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:543-557. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `require_sync_worktree` repointed to mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:309-318. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T08:45+02:00 — Normalized the Docs heading and restored the canonical Cross-Repo
  reference section for this changed authority card.

- 2026-08-26T06:25+02:00 — Rebound the card to its nearest integration-route governor after the
  source-pair authority refresh; verification metadata remains closeout-owned.

- 2026-08-26T03:37+02:00 — Extended sync admission to exact task-owned atomic series refs while
  preserving the separate ordinary-leaf branch and fail-closed unsupported-kind refusal.
  Verification remains post-Dagger/closeout-owned.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: removed queue binding from the documented branch-authority predicate. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled unified topology resolution for accepted leaf overrides. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: nature decisions now read the effective execution
  nature — commanded membership derives from `orchestrates` aliases on graph-less sprints
  (atomic-sequential default), nature-less legacy masters resolve atomic, terminal series
  artifacts no longer count as live organizational series, and a live organizational series
  refusal names `worktree_cleanup`/`worktree_abandon`. Verification remains closeout-owned.

- 2026-08-16T09:55+02:00 — Corrected exact atomic-series owner resolution to retain the repository task-tree segment; real positive-series forcing accompanies the retained foreign/missing refusals.
- 2026-08-16T07:02+02:00 — Moved the immutable authority data contracts once into `integration_branch_types.py`; policy, Git facts, and public imports remain single-owned while this resolver returns below the enforced file-size limit.
- 2026-08-16T06:15+02:00 — No policy change: split atomic series shape, code-source, repository-side, and external-memory identity proofs into bounded owners to satisfy the enforced complexity contract without adding a parallel resolver.
- 2026-08-16T05:27+02:00 — L4 exact-review repair: live-leaf publication now requires the row
  document to remain in its exact owning master root and consumes proposed documents through the
  shared canonical override resolver, closing sibling traversal, symlink escape, and foreign-repo
  override routes.
- 2026-08-16T05:18+02:00 — Dagger repair: live-leaf publication identity now resolves an exact confined candidate reference before disk existence and consumes only the matching candidate override; ordinary missing documents still fail through the canonical resolver.
- 2026-08-16T04:24+02:00 — No policy impact: extracted current-publication authority selection into `_current_publication_master_authority` so the candidate-repair route remains below the configured Ruff complexity limit; the same empty-current, repaired-owner exclusion, and normal-current branches are preserved.
- 2026-08-16T04:06+02:00 — 260815-DAG-L4 Dagger repair: candidate task-document publication may repair an invalid current graph only when every override is a genuinely new on-disk document; the resolver excludes exactly those new owners from current authority while retaining full collision and new-surface validation. No fallback accepts an invalid existing override.
- 2026-08-16T03:36+02:00 — Re-read the split authority owner and retained its delegation and structural-guard descriptions in commentary and invariants; removed two pre-commit evidence rows that could not truthfully carry the old HEAD provenance. Closeout owns the first committed verification stamp.
- 2026-08-16T03:24+02:00 — 260815-DAG-L4: delegated exact Git repository and branch queries to `integration_branch_repository.py` while retaining all task-derived authority policy here; this is a move, not a compatibility duplicate. Verification remains closeout-owned.
- 2026-08-16T00:45+02:00 — Re-read the frozen resolver after Dagger exposed an import cycle; retained its structural claims, removed the inverted queue dependency, and recorded the separate queue-owned terminal permit boundary. Verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created task-derived integration branch authority onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
