# mcp/src/agents_remember/worktrees/modules/abandon.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/abandon.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-05T08:46+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`abandon.py` is the discard-without-integration lifecycle operation for
worktree-backed tasks. Unlike `cleanup.py` (which requires a completed
integration), abandon runs at any lifecycle stage and reclaims the isolated
provider stack, removes code and memory worktrees, deletes task branches, and
removes the worktree group directory.

Successful series abandonment and exact already-abandoned terminal replay pass through
`with_terminal_atomic_series_release` after lifecycle locks are gone. Release is conditional on the
selector still naming this exact contract: a paused old series cannot clear a newer master, and
missing/unreadable/different evidence is preserved and reported rather than reconstructed from task
or queue state. Leaves, dry-runs, and blocked abandon results do not mutate the selector.

## Code Commentary

### Logic

`abandon_result(args: WorktreeArgs)` requires explicit approval (or dry-run),
then delegates to four sub-operations: `teardown_worktree_providers` reclaims
Docker containers, networks, and the `provider-runtime/` tree; `_abandon_worktrees`
calls `remove_registered_worktree` with the `force` flag passed through;
`_abandon_branches` calls `_abandon_branch` for the code work branch, memory
work branch, and memory integration branch; `_abandon_directories` removes the
worktree group dir (force-removes with `remove_tree` when `force=True`,
otherwise `remove_empty_dir`).

`_abandon_branch` checks for unmerged commits via `git log --oneline
<base>..<branch>`. Without `force` it refuses to delete a branch that has
unmerged commits, recording them in the result under `unmergedCommits` with a
`hint`. With `force` it calls `delete_branch_force` (which uses `git branch
-D`). An already-absent branch is always a no-op.

`_abandon_blockers` collects worktrees and branches that are neither removed
nor would-remove — i.e. kept because of a real blocking reason. If any blockers
exist, the contract is not marked `cleanup="abandoned"` and the state is
`"abandon-blocked"`. On a clean run the contract is stamped and state is
`"abandoned"`. Dry-run yields `"would-abandon"`.

Non-force abandon removes the reserved `<worktree_group>/reports` tree before its empty-group check, so
the operational curator checklist cannot keep an otherwise reclaimable enclosure alive. Since
260815-DAG-L10 a series contract's reports tree is the master worktree group's `reports/`
(holding the series operation record/log, citation source-index cache, and Dagger test sandbox),
preserved only when `legacy_series_reports_is_child_enclosure` proves a legacy series contract
(group still recorded as the task enclosure root) shares that path with a child leaf named
`reports`. Force
abandon already removes the complete worktree group and therefore reclaims the same report without
a second deletion path.

Since 260731-EFA-L4 that stamp is
`amend_contract(contract, ContractCells(cleanup="abandoned"))`, not `dataclasses.replace`; the
module no longer imports `replace` at all. `cleanup` is one of the six persisted vocabulary cells,
and typeshed declares `replace` as `**changes: Any`, so `replace(contract, cleanup=<anything>)` was
checked by nothing — including against the wire model that reports the value. The written contract
is unchanged.

### Invariants And Boundaries

- Requires explicit `--approved` or `dry_run`; refuses silently-destructive
  real runs.
- Without `force`, dirty worktrees and unmerged branches are blockers; commits
  are surfaced so the caller can decide whether to lose them.
- With `force`, `git worktree remove --force` and `git branch -D` are used;
  the contract is stamped as abandoned only when no blockers remain.
- Provider teardown runs before worktree/branch removal so the provider stack
  is reclaimed even when Git operations subsequently fail.
- The only report tree this module removes independently is the contract's
  `<worktree_group>/reports` tree — for a series contract since 260815-DAG-L10 that is the master
  worktree group's reports (`worktrees/<repo>/<master>-ar/reports`), not a task-enclosure child;
  force mode removes it only as part of that same group.
- The contract `cleanup` field is set to `"abandoned"` on success; this value
  causes a subsequent `start` call to recreate rather than reattach. `"abandoned"` is a member of
  `worktree_contract.CleanupStatus`, and the write must go through `ContractCells` /
  `amend_contract` — no `replace` call here may carry a `cleanup=` keyword, because typeshed's
  `**changes: Any` means pyright would check nothing.
- The docstring points at the `l-01-agent-lifecycles` skill's
  read-only/abandon exit as the lifecycle entry that drives this operation.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| Successful abandon and exact terminal replay are wrapped with exact source-pair release. | `abandon_result` | mcp/src/agents_remember/worktrees/modules/abandon.py:87-146 |
| The terminal bridge preserves missing, unreadable, or different selection and never clears a newer owner. | `with_terminal_atomic_series_release` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_terminal.py:17-65 |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Provider teardown is delegated to the provider-runtime teardown function. | `teardown_worktree_providers` | mcp/src/agents_remember/application/provider_runtime.py:161-180 |
| `remove_registered_worktree`, `delete_branch_if_merged`, `delete_branch_force`, and `remove_empty_dir` are reused from cleanup. | `remove_registered_worktree`; `delete_branch_if_merged`; `delete_branch_force`; `remove_empty_dir` | mcp/src/agents_remember/worktrees/modules/cleanup.py:177-198; mcp/src/agents_remember/worktrees/modules/cleanup.py:201-223; mcp/src/agents_remember/worktrees/modules/cleanup.py:265-291; mcp/src/agents_remember/worktrees/modules/cleanup.py:443-458 |
| `WorktreeArgs` types the abandon input. | `WorktreeArgs` | mcp/src/agents_remember/worktrees/modules/args.py:31-103 |
| The closeout registrar exposes `worktree_abandon` with `force` forwarded from the MCP layer. | "def worktree_abandon" | mcp/src/agents_remember/mcp/registration/closeout.py:281-281 |
| Series reports-tree preservation is decided by the legacy child-enclosure guard imported from terminal validation. | `legacy_series_reports_is_child_enclosure` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:73-84 |
| The cleanup vocabulary includes abandoned and reopened as declared terminal/reopen states. | "CleanupStatus = Literal[" | mcp/src/agents_remember/models/worktree.py:28-28 |
| The typed contract amendment record holds the six optional vocabulary cells. | "class ContractCells:" | mcp/src/agents_remember/worktrees/worktree_contract.py:181-196 |
| The typed amendment helper preserves unspecified cells and applies supplied vocabulary values. | "def amend_contract(" | mcp/src/agents_remember/worktrees/worktree_contract.py:199-227 |

## 260815-DAG-L4 Authority History, Reconciled By CLIVE

Task-derived integration refs remain mechanically non-ordinary, but final terminal admission is not
a queue-release transaction. For an atomic series, `abandon_result` proves the current child/operation
census and exact archived terminal predecessor, then receives an ephemeral operation-, contract-,
thread-, and context-bound terminal permit. That permit is consumed inside the publication and cannot
be stored or reused. No mutable queue blocker is acquired, released, or consulted as terminal evidence.

## 260821-CLIVE-L1 Lease API Migration

Abandon now acquires the pure contract lifecycle lease and separately calls `require_lifecycle_operation_compatible` while held before terminal publication. Its abandonment behavior is otherwise unchanged; the migration removes reliance on the lease performing an active-operation census.

## 260821-CLIVE-L2 Current Contract

The current source seams include `abandon_result`. The public module consumes closed configured-contract admission and performs its authoritative reread at the existing mutation seam. Destructive terminal cleanup/abandon remains fail closed until external archive proof exists; no inferred locator, raw scan, or compatibility reader is permitted.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `abandon_result` at this ownership boundary. | `abandon_result` | mcp/src/agents_remember/worktrees/modules/abandon.py:87-146 |

## 260821-CLIVE Archive-Before-Abandon

Abandon now proves terminal/no-ambiguous-operation authority, publishes and reads back the external
archive/receipt, and only then removes providers, worktrees, branches, reports, and the enclosure
root. The archive binds the accepted `force` argument; retry with different input refuses, while an
exact terminal retry/status works after the live root is gone. Atomic series require the ephemeral
terminal release capability, never a persistent queue blocker. Already-abandoned results retain and
surface terminal archive proof.

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: "def worktree_abandon" repointed to mcp/src/agents_remember/mcp/registration/closeout.py:281-281. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 1 declined citation claim against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Separated cleanup vocabulary, amendment data, and mutation helper into exact source claims. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.

- 2026-08-31T20:30+02:00 — No content impact: repointed the `worktree_abandon` registration
  citation after the direct-landing tool description shifted its source line. Abandon behavior is
  unchanged.

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 type-alias syntax migration for terminal abandon outputs and confirmed that the documented abandon contract is unchanged. Verification remains closeout-owned.

- 2026-08-26T03:37+02:00 — Added exact post-terminal atomic-series selection release to abandon
  and terminal replay documentation. Selection remains disposable and separate from abandon
  authority. Verification remains post-Dagger/closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged exact terminal archive, typed force replay, and atomic terminal authority into abandon. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: re-anchored citation range(s) to current source after the L16 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-20T05:12+02:00 — L13 landed-wave refresh: the series closeout-report routing
  commit (0a746c9f) touched this source; card re-verified against the current file, verification
  stamp advanced to 0a746c9f. Body unchanged — the documented contract still holds.


- 2026-08-19T04:05+02:00 — 260815-DAG-L10 curator: the independent reports sweep now targets the
  contract's `<worktree_group>/reports` tree, which for a series contract is the master worktree
  group's reports (not a task-enclosure child); preservation is narrowed to legacy series
  contracts through the renamed `legacy_series_reports_is_child_enclosure` guard. Verification
  metadata stamped at the landed code commit `e41ea31d`.
- 2026-08-16T00:45+02:00 — Recorded the explicit atomic-series queue-release preflight and expiring publication permit after the Dagger import-cycle repair. Verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T16:54+02:00 — Made non-force abandon garbage-collect the reserved enclosure report
  tree; force abandon continues to remove it through the whole-group operation.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: regenerated the reused-cleanup
  helper ranges and the closeout registrar row via the scoped fixer; exact non-fixing check
  returns zero findings.

- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 5 repository-reference citations (5/5 anchored and sourced; scoped citation check clean).

- 2026-08-01T09:52+02:00 — 260731-EFA-L4 curator: the `cleanup="abandoned"` stamp changed mechanism.
  `abandon_result` now writes `amend_contract(contract, ContractCells(cleanup="abandoned"))`, the
  `from dataclasses import replace` import is gone, and `ContractCells` / `amend_contract` were
  added to the `worktree_contract` import block. Recorded it and tightened the matching invariant:
  `cleanup` is one of the six persisted vocabularies, and `dataclasses.replace` types `**changes` as
  `Any`, so the old call was checked by nothing — not by pyright and not against the wire model that
  reports the value. Behaviour and the written contract are unchanged, so every other claim in this
  card still stands; I re-verified `_abandon_branch`'s unmerged probe, the force path
  (`delete_branch_force`, `remove_registered_worktree(force=True)`) and the
  `abandoned`/`abandon-blocked`/`would-abandon` states against the current file. Added the
  `worktree_contract.py` reference row. Verification metadata pinned until closeout stamps the L4
  commit.
- 2026-07-31T20:59+02:00 — 260731-EFA-L3 curator: No content impact: the leaf's whole diff to
  `abandon.py` is one import line — `run_git` moved from `modules.git` to
  `agents_remember.kernel.git_command`, `branch_exists` still comes from `modules.git` — and this
  sidecar never described a git runner, a subprocess style or a timeout, so it had nothing to
  correct. Re-verified every behavioural claim against the current file: `_abandon_branch`'s
  unmerged probe is still `run_git(repo, ["log", "--oneline", f"{base_branch}..{branch}"])`
  (`_unmerged_commits`), the force path still routes to `delete_branch_force` (`git branch -D`) and
  `remove_registered_worktree(..., force=True)` (`git worktree remove --force`), and
  `_abandon_blockers` / `_abandon_state` still produce `abandoned` / `abandon-blocked` /
  `would-abandon` unchanged. The shared runner's guard and timeout classes are documented on their
  owner, `kernel/git_command.py`, and on `modules/git.py` which lost the local copy.
- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: docstring vocabulary updated to the l-01-agent-lifecycles orchestrator read-only/abandon exit; behavior unchanged. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-10T07:30+02:00 — `abandon_result` blocks (exit 2) without `force` while a live background provider setup owns the worktree (fresh heartbeat); `force=true` overrides, and a stale heartbeat does not block (GitHub #53).
- 2026-06-02T16:24+02:00: Docstring now references the `l-01-agent-lifecycles` skill in full for the read-only/abandon exit (was "L-01"). Reference-style normalization; behavior unchanged.
- 2026-06-01T00:00+02:00 — Created onboarding for the new abandon module.

## Governing Overview

[governing overview](overview.md)
## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
