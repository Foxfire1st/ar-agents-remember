# mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:45+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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

## Invariants And Boundaries

- Protected surfaces are repo-global for a Git common directory, not local to the current sprint.
- Repository default code refs are PR/landing-plane targets and never generic local integration targets.
- Organizational leaves source directly from the sprint super; atomic leaves source from the exact series ref; the effective nature (not the declared cell) picks the lane.
- Missing, stale, ambiguous, foreign, or colliding authority fails closed before mutation.
- Series terminal writers require both the structural guard here and the ephemeral
  transaction-bound permit issued by `atomic_series_terminal.py`; no queue owns terminal authority.
- Sync may operate on a series only through exact series-contract authority; ordinary leaf and
  protected series admission remain distinct branches.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public census and target projection derive exact protected surfaces. | `integration_surfaces`, `integration_targets` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:56-57; mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:60-123 |
| Topology publication validates candidate ownership before task facts can create a protected collision. | `require_topology_publication_authority`, `require_topology_migration_authority` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:377-422; mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:425-442 |
| New-surface validation recognizes only the exact canonical atomic series contract and branch. | `_atomic_surface_has_series` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:496-510 |
| Sync admits either an ordinary leaf workbench or exact task-owned series authority. | `require_sync_worktree` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:293-302 |

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
| Live leaf publication resolves the candidate through the unified topology API with accepted overrides. | `require_topology_publication_authority` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:386-419 |

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
