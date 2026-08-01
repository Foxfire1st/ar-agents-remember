# mcp/src/agents_remember/worktrees/modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `mcp/src/agents_remember/worktrees/modules` |
| lastUpdated            | 2026-08-01T00:00+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Purpose

The `worktrees/modules` package contains the extracted implementation modules
behind the `git_worktree_manager.py` facade. It separates Git adapters, lifecycle
status guidance, start preparation, onboarding refresh, strict code-quality gating, closeout, integration,
cleanup, lifecycle finalization, abandon, provider teardown, start-contract leaf-ref normalization, the typed cross-layer argument DTO, and CLI
argument wiring while preserving the public facade import path. Reopen is deliberately NOT here:
`task_reopen` lives in the tasks package (L11) because it reopens a task, and this route's start path
merely honors its `cleanup: reopened` tombstone (recreate fresh, restamp the leaf doc's lifecycle).

## Hot Path Summary

- `git.py` owns this route's Git vocabulary — the typed helpers and small repository
  state checks every operation module speaks — but **since 260731-EFA-L3 it no longer
  owns a Git runner**. It imports the one owner (`from agents_remember.kernel.git_command
  import run_git`, line 7), and its own `require_git` (line 18) is now just
  raise-on-nonzero over it. See the 260731-EFA-L3 section below for why that
  distinction is a correctness property and not bookkeeping. Its helpers include
  `committed_changed_paths` (issue #83: the unverified committed
  range — tree-diff `base..HEAD` ∩ `verified..HEAD`) and the
  `commit_text_or_none` baseline reader behind the closeout body gates.
  **Operations-integration L3** adds `changed_files_with_counts(repo, base, head=None)`
  (+ `_rename_aware_path`) — the change-set primitive behind the serving change-set API
  (`serving/changeset.py`): per-file `{path, insertions, deletions, status}` via
  `git diff --numstat --name-status --find-renames`, KEEPING deletions and reporting
  counts (binary → `None`, untracked → `A`, rename → post-rename path), unlike the
  name-only `changed_*_paths`.
- `code_quality_gate.py` is the fail-closed worktree closeout adapter for the
  project-owned quality wrapper. It previews the exact command, resolves
  interpreters in worktree, shared-clone, then active-Python order, puts the
  candidate worktree's `mcp/src` first on `PYTHONPATH`, and rejects a missing
  wrapper/interpreter or any nonzero result. This preserves linked worktree
  operation without weakening the gate or accidentally testing a sibling checkout.

  **Since 260731-EFA-L1 the gate is not scoped to one repository.** The deciders take the code
  worktree `Path` and gate on whether that checkout carries
  `mcp/src/agents_remember/code_quality/check.py`; the old `repo_name == "agents-remember"`
  condition made the gate a no-op for every consuming repository — the product's actual audience —
  while the product documented it as mandatory. The preview now reports one of three statuses:
  `enforced`, `no-code-commit`, or `wrapper-unavailable`. The last is deliberately *reported*
  rather than silent: closeout proceeds, and the payload states that the code commit was not
  quality-checked and why. Since 260731-EFA-L4 the `enforced` reason (line 77) also names the
  staging step that now precedes the run, because the gate derives its scope from the index and
  therefore certifies whatever the caller staged — see the L4 section below.

  One hazard lives at this route's boundary: `closeout.py` calls these functions with an
  unannotated `contract`, so passing `contract.repo_name` where a `Path` is expected type-checks
  clean and silently disables the mandatory gate. Only
  `test_worktree_closeout_quality_gate.py::test_closeout_hands_the_gate_the_code_worktree_not_the_repository_name`
  observes the real argument; do not weaken it into a stub.
- `guidance.py` renders lifecycle phase and typed next-operation payloads, and **since
  260731-EFA-L4 it is where the phase/next-move vocabulary is declared** — `WorktreePhase`
  (line 28), `NextOperation` (line 38) and `NextTool` (line 47) are `Literal`s owned by the
  state machine that produces them, and `models/worktree.py::WorktreeSummary` imports those
  three names instead of retyping them (`models/worktree.py` lines 15-19). Before that the
  wire model held a hand-written copy, and the two sets had drifted: `carryover-pending`,
  `abandoned`, `request_carryover_decision` and `memory_carryover_apply` were all emitted by
  the functions below and all rejected by the packet. `lifecycle_guidance` now returns the
  `LifecycleGuidance` TypedDict (line 85) rather than `dict[str, object]`, and the three
  phase-group helpers return it too, so a phase string this module invents but the wire cannot
  carry is a pyright error here rather than a pydantic `ValidationError` raised inside the
  `context_packet` tool handler, which has no `except` for one. Its
  `lifecycle_guidance` checks the disposal states first: `cleanup == "completed"`
  → the `cleanup-completed` phase, and (slice 05l P1) `cleanup == "abandoned"` →
  a dedicated `abandoned` phase (`nextOperation: "done"`). Before the abandoned
  branch a torn-down worktree fell through to the `worktree-started` default, so
  the dashboard rendered it as fully active; the explicit phase lets the observer
  reducer (`_GUIDANCE_PHASE`) project the teardown for the 05k render. **Slice 09**
  removed the dirty-tree → `commit-approval-pending` branch (a visibility bug):
  `lifecycle_guidance` no longer infers a commit-approval gate from `git status`,
  so a dirty worktree falls through to its honest lifecycle-position phase
  (closeout-completed → `integration-pending`, etc.). `commit-approval-pending` is
  owned by the closeout preview (`closeout.py`) and, once the gate plane is adopted,
  by a raised `closeout-approval` `GateNode` — never the working tree; the unused
  `contract_has_worktree_changes` import was dropped. **Slice 05m**
  adds the public `carryover_done(contract) -> (done, carryoverDoneAt)`: it reads the
  OFFICIAL ledger (`memory_repo_path/memory.md` via `load_ledger`/`find_mapping`) to
  detect whether the landed code commit (`integrated_code_commit`, else `code_commit`)
  was carried home, returning the carry commit's `%cI` as the milestone (external-only;
  internal/disabled → `(True, "")`). `lifecycle_guidance` now splits the
  `integration_status == "completed"` branch on it — not carried → phase
  `carryover-pending` routing the existing `memory_carryover_apply` (carryover must run
  while the parked memory branch still exists), carried → `cleanup-pending` carrying
  `carryoverDoneAt`.
  **L4 also splits the next-move builder in two.** `next_guidance` (line 142) is now typed
  `NextOperation`/`NextTool` and belongs to the phase machine; the five payloads that are a
  *gate or a block* rather than a phase — the closeout preview's `request_commit_approval` and
  the four blocked start/sync recoveries — call the sibling `recovery_guidance` (line 159)
  with its own `RecoveryOperation` (line 61) / `RecoveryTool` (line 68) vocabulary. Same keys,
  same order, byte-identical wire; the split exists so that widening the recovery set cannot
  widen `WorktreeSummary.nextOperation`, which would put "requires developer approval" and
  "blocked on a stale base" back into the set the context packet claims to report. Undo the
  split and the packet again advertises values its own state machine can never produce.
  `status_payload` and `projected_status_payload` return the `WorktreeStatusPayload` TypedDict
  (line 138) — `WorktreeStatusFacts` (line 98, the snake_case contract facts) merged with
  `LifecycleGuidance` — instead of `dict[str, object]`, and gain one optional key:
  `unknown_contract_cells`, present only when the contract file carried a cell outside its
  vocabulary that `worktree_contract._vocabulary_cell` substituted for. It is the one place a
  degraded contract read becomes visible to whoever called a worktree tool, and it says that
  the phase beside it was computed from the substituted values.
- `landing.py` (slice 5h; hardened 5l P2) observes the successful-landing arc
  best-effort — `git ls-remote` branch tips (`origin/<feat>`, `origin/mem-main`) +
  a best-effort `gh pr list`, all timeout-bounded and `stdin=DEVNULL` (the #49
  stdio-pipe guard). Since 260731-EFA-L3 the two `ls-remote` probes get both of those
  properties from the shared runner rather than hand-rolling them —
  `run_git(repo, [...], timeout=_PROBE_TIMEOUT_SECONDS)` at `_remote_branch` (line 56)
  and `_default_branch` (line 79), keeping the deliberately short 8s probe bound
  (`_PROBE_TIMEOUT_SECONDS`, line 31) rather than inheriting a runner default. The
  `gh pr list` in `_pr_for` (line 93) is not git and still builds its own
  `subprocess.run`, but it now takes `env=git_environment()` (line 124) — `gh`
  resolves the repository *through* git, so an inherited `GIT_DIR` would have it list
  another repository's pull requests under this worktree's branch name, and `cwd=repo`
  does not outrank the selectors for `gh` any more than it does for `git`. It is the
  package's only non-git spawn that reads a repository.
  The probes are gated to the landing window (closeout-completed onward) so the
  status poll stays network-free during the build phase; `guidance.py`'s
  `status_payload` emits its result as the `landing` block, and the observer reducer
  composes it onto `EngineProcessNode.landing`. Probe failures degrade to
  `factState: "missing"` — never faked. **Slice 5l P2** hardens the probe so the
  dashboard can follow a REAL remote landing: the protected target `origin/<base>`
  is now probed **directly** via `ls-remote` (`_main_ref` + `_default_branch`,
  resolving origin's default branch from the remote HEAD symref, no `fetch`) —
  visible across the whole landing window before any PR and even when `gh` is
  absent, with its `state` honestly tracking whether THIS work landed
  (`merged`/`planned`/`unknown`) rather than merely whether main exists; and the PR
  ref carries gh's own open/merge timestamp (`at` = `mergedAt` once merged, else
  `createdAt`). It re-fires every projector tick (~1s), so no milestone hook is
needed for cadence.
260712-TRH-L7 changes the landing guidance boundary: `status_payload` remains the explicit
interactive fresh-probe surface, while `projected_status_payload` consumes only a pre-observed
immutable landing snapshot. The recurring projector therefore never invokes `git ls-remote` or
`gh` through guidance; missing and stale observations remain explicit.
- `start.py`, `start_contract.py`, `leaf_ref_start.py`, `closeout.py`, `integrate.py`, `cleanup.py`,
  `finalize.py`, and `abandon.py`
  own the named `c-09-git-worktree-manager` skill lifecycle operations.
  `start.py` calls `start_contract.build_start_contract` to resolve the requested leaf ref through the
  `worktrees/leaf_refs.py` task-tree resolver before any start write; accepted refs persist the canonical
  task doc id in the leaf contract, while no-match/ambiguous refs return a `WorktreeCommandResult`
  refusal naming the expected `<repo>/<master-folder>/<doc-id>` form and candidates. Standalone/light
  task roots resolve through their non-master `task.json` doc id, slug/folder, and enclosure aliases, and
  resolver indexing skips sibling JSON artifacts unless they carry the task-document schema marker. After
  that, `start.py` runs a synchronous
  provider preflight, writes the contract, and
  then launches provider setup in the background (GitHub #53): dry runs stay
  synchronous, real starts return `starting` within seconds, and
  `retry_provider_setup` relaunches a failed/stale setup on an existing
  contract. Before any worktree exists, `start.py` also runs the stale-base
  preflight (GitHub #54): source branches behind/diverged from their upstream
  block the start with `stale_base_choice` recoveries (`fast-forward` /
  `proceed-stale`), and a missing external memory source branch is
  auto-created at the official memory tip using the code branch name as
  template. For master tasks, `start_contract.py` creates or loads the root
  `series-contract.md` integration contract first, creates the integration branch from the protected/source
  branch, and then starts each leaf from that integration branch with its own
  `enclosures/<leaf-id>/series-contract.md`. `cleanup.py`/`abandon.py` refuse to tear down while a live
  (fresh-heartbeat) background setup owns the worktree. **Slice 05m** makes
  `cleanup.py` carryover-guarded and work-branch-retiring: `cleanup_result` now HARD-REFUSES
  (raises) when integration is completed but `guidance.carryover_done` is false (external
  memory) — cleanup deletes the parked memory branch carryover reads from, so the carry
  must run first; the proof is the official ledger, not a contract stamp. After the guard
  it retires work branches only after proving they are reachable from the contract's
  recorded source branch (`merge-base --is-ancestor work_branch source_branch`), then
  deletes them with `git branch -D`; this avoids Git's ambient `HEAD`/upstream merge
  target while preserving unmerged work branches as `kept_branches`. Task 14 corrected
  cleanup to operate on the just-finalized child edge only: it removes the task work
  branches (`code`, `memory`, optional `memory_integration`) and keeps parent/source
  branches for their own lifecycle edge. Cleanup
  dry-runs also model scheduled removals: registered worktrees and `provider-runtime/`
  are subtracted before the worktree group directory is classified, so a group that will
  become empty reports `would_remove` rather than `not-empty`; real cleanup still removes
  directories only after they are actually empty. Task 32 also makes cleanup reclaim the
  observer drift snapshot generated by the code worktree it is deleting: dry-runs report
  the exact snapshot under `drift_snapshots["code"]`, and real cleanup removes only that
  contract-owned repository/branch snapshot. `integrate.py` refuses while an undecided or policy-invalid `master-handover-approval` gate addressed to the integrating master exists anywhere in the workspace: the pure `handover_gate_guard` folds every gate log (`GateStore.all_current`) and matches gates by `enclosure` against the contract's `task_name`/`parent_task_name` — never the consuming contract's lifecycle — evaluating the controller-threaded configured policy (the master-exit seam consumer, mirroring the closeout gate; gateless stays additive). Since cycle 7 the guard is evaluated on the dry run too — reported (`handover_gate` in the preview, whose summary names `handover-gate-blocked` when the real run would refuse) but enforced only on the real run, with no contract mutation on the dry-run path — and the pure sibling `unmatched_handover_gate_warning` puts a `handover_gate_warning` (unmatched OPEN handover gates + a verify-the-enclosure-spelling note) on gateless dry-run/integrated payloads, so a typo'd exact-string address cannot fail open silently. It then performs the code and
  memory fast-forwards atomically: it pre-validates that both fast-forwards are
  possible before mutating either branch and rolls both heads back on any
  memory-side failure, so integration never lands a half-integrated state.
  `abandon.py` is the discard-without-integration sibling: it reclaims the
  isolated provider stack and removes worktrees/branches without requiring a
  prior integration.
- `finalize.py` owns the terminal `lifecycle_finalize_task` operation. It
  refuses until closeout and integration are complete, the landed code commit is
  an ancestor of the recorded local source branch, and external-memory carryover
  is done; then it runs or verifies cleanup and marks the leaf task plus
  immediate parent row `Completed` when task-document paths are supplied. The
  proof is one parent-child branch edge at a time. PR-gated flows are identical
  after the PR merge has been pulled locally, while squash-merge equivalence is
  not inferred by default.
- `sync.py` (GitHub #54 sub-task D) owns `worktree_sync`: the mid-task base
  sync that fetches upstreams, requires the new code tip to be ledger-mapped at
  the official memory tip, merges the source branch into the code work branch
  (abort on conflicts), fast-forwards parked memory (or blocks with
  `memory_sync_choice` recoveries when local memory commits diverge), and
  advances the contract's recorded base pair with a `sync_log` entry.
  `guidance.py`'s fetch-free `freshness` block in `worktree_status` is the
  detection surface that recommends it.
- `provider_async.py` owns the background setup launch (daemon thread), the
  durable `setup-progress.json` under the worktree group's provider-runtime
  dir, the `worktree_status` providers projection (running / stale / ok /
  ready-with-failed-phases / failed + retryArgs), and the live-setup guard.
  The progress file format itself lives in `providers/setup_progress.py`.
- `provider_teardown.py` performs full-reclaim teardown of a worktree's
  isolated provider stack (Docker rm -f containers and networks derived from
  persisted settings, then rmtree the provider-runtime tree, reclaiming
  root-owned data via a docker chown when needed). Used by both `cleanup.py`
  and `abandon.py`.
- `onboarding.py` owns closeout-time onboarding metadata and entity fingerprint
  refresh planning, plus the four-case body/history gates
  (`classify_sidecar_updates` / `require_updated_sidecar_content` for file
  sidecars, `classify_route_overview_updates` /
  `require_updated_route_overview_content` for route overviews): a changed
  source's sidecar — and the route overview that is its **nearest governor** —
  must pair a meaningful body change with a new Update History entry, or carry
  an explicit `No content impact:` / `No route impact:` history entry.
  Ancestor-matched overviews are reported as `stamped_without_body_review`
  rather than gating. Previews and apply payloads surface marker-attested
  documents. Shared metadata/route parsing lives in `kernel/onboarding_doc.py`
  and is re-exported here. Closeout preview and apply also pass
  `context.storage` explicitly to route-index generation, preserving the same
  repository/path-rule authority used when the onboarding plan was resolved.
- The closeout worklist (issue #83) is `closeout.py`'s
  `closeout_changed_paths`: working tree ∪ the unverified committed range, so
  transported history (merges, pre-committed slices) gates and stamps like
  hands-on edits. The onboarding plan's two-tier split (`working_paths`) keeps
  missing-sidecar blocking on working-tree paths only; committed-range paths
  without onboarding surface as the non-blocking `unonboarded` report. Body
  gates baseline against `contract_memory_verified_commit` so memory work
  committed before closeout classifies honestly, and payload lists that scale
  with transported history are exposed as count + sample
  (`PATH_SAMPLE_LIMIT`). Slice 6b adds **server-side gate enforcement** to
  `closeout.py`: when the contract has a `lifecycle_id`, closeout refuses unless
  the lifecycle's `closeout-approval` gate is developer-approved or approved by
  a policy-valid delegated orchestration decision
  (`controlplane.evaluate_closeout_gate(..., policy=args.gate_policy)`), marks it `applied` on success, and
  reports a `closeout_gate` block; gateless lifecycles keep the chat commit gate.
  Task 30 adds the already-integrated re-closeout reset: closeout source-head
  validation accepts the recorded integrated tips, preview reports
  `integration_reopen.would_reopen`, and apply reopens `integration_status` only
  when the new code or memory-content commit is not yet on the recorded source
  branch. Clean no-op re-closeout keeps the completed integration state and does
  not duplicate an already-present ledger mapping.
  260718-CHATS-L5I inserts the strict `code_quality_gate.py` adapter after
  preview/approval validation and before every apply **commit**. A quality failure
  therefore creates no code, memory or ledger commit and leaves contract and
  applied-gate state untouched; only a clean wrapper result permits `commit_if_dirty`
  and the subsequent onboarding/ledger sequence. **Since 260731-EFA-L4 the gate is not
  reached directly**: `closeout_result` (line 727) calls `_gate_staged_code` (line 625),
  which stages the code worktree first, so the *index* is one mutation that now precedes
  the gate and survives a refusal. See the L4 section below for why staging is what makes
  the gate see created files, and why the two refusals must run ahead of the reset.
- `args.py` defines the frozen `WorktreeArgs` cross-layer DTO that operation
  modules consume in place of `argparse.Namespace`; `from_namespace` builds it
  from partial CLI/controller namespaces with per-field defaults. It carries `parent_task` and `leaf_id`
  for nested active task-root and leaf-enclosure resolution.
- `cli.py` keeps command-line parsing and JSON print adapters out of operation
  modules and converts each parsed namespace into `WorktreeArgs` at the boundary.
  Its `heal-leaf-ids` subcommand (260712-PTS-L1) is the deliberate invocation seam for
  `worktree_contract.heal_contract_leaf_ids` (`--coordination-root`, `--dry-run`; prints the heal
  report JSON) and intentionally bypasses `WorktreeArgs` — the heal is a one-shot legacy leaf-id
  migration sweep, never a per-read side effect, now that `load_contract` is walk-free and never
  normalizes.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The package is imported through the public worktree manager facade. | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Focused worktree tests exercise the facade and operation payloads. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Finalizer tests cover landed-commit proof, cleanup blocking, dry-run, and task-document reconciliation. | [test_lifecycle_finalize.py](agents-remember/mcp/tests/test_lifecycle_finalize.py) |
| Closeout onboarding refresh uses resolved storage authority for deterministic route-index preview and apply. | [onboarding.py](agents-remember/mcp/src/agents_remember/worktrees/modules/onboarding.py); [route_index.py](agents-remember/mcp/src/agents_remember/kernel/route_index.py) |
| Stage-before-gate: a created file's lint error fails the gate, the gate's scope equals the commit's content, both preconditions refuse before anything is staged, the reset runs after the conflict check, and a retry commits the tree a first run would. | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |
| This route's phase/next-move `Literal`s are the ones the wire model imports, and no producer here emits a value outside them. | [test_wire_vocabulary_exhaustiveness.py](agents-remember/mcp/tests/test_wire_vocabulary_exhaustiveness.py); [models/worktree.py](agents-remember/mcp/src/agents_remember/models/worktree.py) |

## 260731-EFA-L2 Lifecycle Parameter Objects

The worktree lifecycle's long argument lists became frozen value objects, most of which are
route-level vocabulary rather than local tidy-ups:

- `models.VerifiedChange` — the landed code change onboarding metadata is stamped against
  (`commit`, `commit_date`, `changed_paths`, `working_paths`). `closeout` builds it once;
  `onboarding`'s three refreshers take it, so a refresher cannot stamp one commit's hash beside
  another's path list.
- `worktree_contract.ContractTask` / `LeafIdentity` / `RepoBranchPlan` — what both contract
  constructors now take. On the series contract the old `protected_branch`/`integration_branch`
  pair is the code plan's `source_branch`/`work_branch`, and `memory=None` expresses the whole
  absent-memory state.
- `start_progress.StartingEnclosure` / `StartBeat` — the pre-contract observability payload, split
  into what the beat is about versus how far the start has got.
- `cleanup.RetiringBranch`, `integrate.IntegrationSources` / `IntegratedCommits`,
  `provider_async.ProviderSetupJob`.

`start_result` is now three stages (`_existing_contract_result`, `_preflighted_contract`,
`_create_start_enclosure`) and `lifecycle_guidance` three phase groups whose order is the
precedence contract. `context.py` builds the kernel resolver's `CoordinationHints` /
`EnclosureSelector`. Every payload, refusal, recovery choice and written contract is unchanged.

## 260731-EFA-L3 This Route No Longer Runs Its Own Git

**`git.py` used to define its own `run_git`, and it was the kernel's function with the
environment guard dropped.** Only `kernel/git_command.py`'s copy passed
`env=git_environment()`, which strips the eight `GIT_DIR`-family repository selectors
(`GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`,
`GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`, `GIT_PREFIX`).
`cwd=` does not defeat those variables — git consults them first — so with `GIT_DIR`
exported the *same logical operation* landed in a different repository depending on
which copy ran.

This route is where that mattered most, because this route is where the destructive
verbs live. All of these are reachable from the former unguarded copy and are still
here, now on the owner:

| Operation | Site |
| --- | --- |
| `commit` | `git.py` `commit_if_dirty` (line 85) |
| `merge --ff-only` | `integrate.py` (line 462, and memory at 467) |
| `reset --hard` | `integrate.py` rollback (lines 478-479) |
| `rebase` | `integrate.py` (lines 184, 236) |
| `branch -f` | `start.py` (line 393) |
| `branch -D` | `cleanup.py` (lines 77, 94) |
| `worktree remove [--force]` | `cleanup.py` (line 32) |
| `push origin --delete` | `cleanup.py` `_push_branch_deletion` (line 142) |

L4 moved every one of these except `git.py`'s: `integrate.py` +2, `start.py` +7, `cleanup.py` +5 and
`code_quality_gate.py` +11 lines above the cited sites. The symbols and the claims are unchanged.

All nine git-touching modules in this route now import from
`agents_remember.kernel.git_command`: `git.py`, `abandon.py`, `guidance.py`,
`integrate.py`, `start.py`, `sync.py` and `cleanup.py` take `run_git`, while
`landing.py` and `code_quality_gate.py` take both `run_git` and `git_environment`
(they each also spawn something that is not `git` — see below). Nothing about the
helpers themselves changed.

**The runner had to be made fit to be the only one before it could be the only one.**
Its `timeout` was hard-coded to `5`, which is right for `rev-parse` and absurd for a
rebase, so consolidating onto it unchanged would have turned every integrate into a
five-second timeout. `timeout` is now a per-call parameter with three named classes —
`GIT_LOCAL_TIMEOUT_SECONDS = 300` (the default: rebase/merge/status),
`GIT_REMOTE_TIMEOUT_SECONDS = 120`, `GIT_METADATA_TIMEOUT_SECONDS = 30`. This route's
local work takes the default; `landing.py` keeps its own shorter 8s probe bound.

Three route-visible consequences beyond "same behaviour, one runner":

- **`cleanup.py`'s remote calls are bounded for the first time.** `git ls-remote --heads
  origin` and `git push origin --delete` ran inside an MCP tool call, which the client
  cannot cancel, through a runner that set no timeout at all — an unreachable or wedged
  remote held the tool call open forever. `_remote_git` (line 113) runs them at
  `GIT_REMOTE_TIMEOUT_SECONDS` and returns `None` on `subprocess.TimeoutExpired`, which
  `delete_remote_branch_if_present` (line 127) and `_push_branch_deletion` (line 141)
  fold into the already-handled `{"remote_deleted": False, "reason": "remote-unreachable"}`.
  A stall therefore reads as an unreachable remote in the payload rather than escaping
  as an exception or hanging.
- **`code_quality_gate.py`'s repository probe is guarded.** `_git_common_dir` (line 187)
  hand-rolled `subprocess.run` without `env=`; it now calls
  `run_git(code_worktree, ["rev-parse", "--path-format=absolute", "--git-common-dir"])`
  (line 190). That value decides which repository the mandatory closeout quality gate
  then certifies, and this gate runs from the pre-push hook — where `GIT_DIR` *is* set
  by git itself.
- **`code_quality_gate.py` also stops handing the selectors to its child.**
  `quality_environment` (line 168) used to start from `dict(os.environ)`; it now builds
  from `git_environment()` (line 178), so the eight repository selectors are gone before
  the quality wrapper subprocess starts. That wrapper derives its own scope from
  `git ls-files` and its diff base from `merge-base`, and closeout spawns it from paths
  where `GIT_DIR` can be exported. Every git call inside that child strips the selectors
  itself today, so this is defence in depth — but the gate decides *which repository gets
  certified*, and that must not rest on the continued good behaviour of a process this
  one cannot see.

`mcp/tests/test_git_command.py` is the proof: it points every selector at a decoy
repository and asserts the real one received the commit and the decoy did not
(`test_a_commit_lands_in_the_real_repository_not_the_decoy`), plus
`test_a_stalled_push_reports_unreachable_instead_of_hanging` and
`test_both_remote_calls_carry_the_remote_bound` for the cleanup path. `conftest.py` also
strips the selectors, but the decoy test re-sets them inside its own scope precisely so
it cannot pass on the conftest's account — do not "simplify" that away.

## 260731-EFA-L4 Typed Vocabularies, And A Gate That Sees What It Certifies

Two independent things landed here, and both are about a check that could be defeated with
nothing reporting it.

### The six contract vocabulary cells stopped crossing `dataclasses.replace`

`abandon.py`, `cleanup.py`, `closeout.py`, `integrate.py` and `start.py` all amended the
contract with `dataclasses.replace(contract, cleanup=…, integration_status=…, …)`. Typeshed
declares `def replace(obj, /, **changes: Any)`, so **pyright checked nothing about those
keywords**: `replace(contract, cleanup="reclaimed-ish")` produced zero diagnostics even though
`WorktreeContract.cleanup` is a four-member `Literal` and the wire model that reports it
rejects everything else. Each module now routes the vocabulary cells through
`worktree_contract.ContractCells` + `amend_contract`, a frozen record whose six declared
fields put them back in front of the checker, while `replace` still performs the copy and
still carries the free-text cells beside it (commit hashes, approval notes, strategies —
these have no vocabulary to check against, which is exactly why they stay where they are).

| Call site | Cells it moves |
| --- | --- |
| `abandon.py` line 74 | `cleanup="abandoned"` |
| `cleanup.py` line 395 | `cleanup="completed"` |
| `integrate.py` line 120 | `integration_status="blocked"` |
| `integrate.py` line 490 | `integration_status="completed"`, `cleanup="pending"` |
| `closeout.py` line 765 | `human_review_status`, `closeout_status`, `integration_status`, `cleanup` |
| `start.py` line 141 | `memory_mode="disabled"` (the memory-disabled downgrade) |

Undo one of these back to a bare `replace` keyword and **nothing fails at the call site** —
that is the whole defect. It fails later, at the packet, as a pydantic `ValidationError`
raised inside an MCP tool handler that has no `except` for one. The rule that keeps it shut is
"no `replace` call anywhere may carry one of these six keywords", enforced together with
`mcp/tests/test_wire_vocabulary_exhaustiveness.py`.

`start_contract.build_start_contract` (line 187) gained a second `except` for the same reason.
`worktree_start`'s `workflow_kind` and `memory_mode` reach the MCP signature as free `str`
(the tool declares `workflow_kind: str = "light-task"` and documents `'light-task'` or
`'chat-task'`), and `worktree_contract._task_vocabulary` now *refuses* an unknown one at both
contract factories. Nothing between there and the `@server.tool()` handler catches a
`ContractError`, so line 198 converts it through the new
`leaf_ref_start.invalid_contract_request_result` (line 38) into the same
`WorktreeCommandResult(2, {"state": "invalid-request", …})` shape every other blocked start
already used, naming the legal set instead of producing a traceback. Note that this `except`
is broader than its docstring says: it also catches a `ContractError` raised by the
`write_contract` inside `_parent_series_contract` (line 176), which is a write-validation
failure rather than a bad caller argument — the message still names the field and the file, so
the refusal stays honest, but it is not only about arguments.

### `closeout.py` stages the worktree before the quality gate

`closeout_result` (line 727) no longer calls `run_strict_code_quality_gate` directly; it calls
`_gate_staged_code` (line 625), which does `git reset --mixed --quiet HEAD` then `git add -A`
(lines 679-680) and *then* runs the gate.

**Why:** every rail of the wrapper reads the index. `code_quality/check.py::derive_scope`
(line 199) enumerates what ruff and pyright are given with `git ls-files`, and `diff_coverage`
diffs the base against the tracked tree — both blind to a file git has never been told about.
Closeout commits with `git add -A`. So until it staged first, **every file a task created
rather than edited went into the commit without a single rail reading a line of it**, and the
gate reported green having never seen it. Check it against this route's own history:
`git show --diff-filter=A --name-only abc7cbcc` (L3's tail, the commit this leaf is based on)
lists four added files, two of them `.py` — `mcp/tests/test_cold_start.py` and
`mcp/tests/test_git_command.py` — and neither could have appeared in that closeout's
`git ls-files`, because `ls-files` does not report a path git has never been told about.
The index cut the other way too: a path the task *deleted* stayed in `ls-files` until the
deletion was staged, so ruff was handed a file that no longer existed and took an `E902`.

**Why the reset and not just the add:** git applies ignore rules only to paths it does not
already track or hold staged, so a file staged by a refused attempt stays staged even after
the retry adds it to `.gitignore`, and the commit carries it. `--mixed` is index-only, so the
tree the gate certifies is byte-for-byte what the task left on disk; the reset simply makes
each run recompute the index from the working tree under the ignore rules in force *now*.

**The ordering is load-bearing, and this is the part not to "simplify".** `_gate_staged_code`
runs `_refuse_outside_a_linked_worktree` (line 557) and `_refuse_conflicted_worktree`
(line 599) **before** the reset:

- The first compares `git rev-parse --git-dir` with `--git-common-dir`: they differ in a
  linked worktree and are the same path in a repository's own checkout. It tests the property
  that makes staging safe rather than the contract's `kind` label, because
  `worktree_contract.default_series_contract` records `code_worktree=code.repo_path` — the
  primary checkout itself — and nothing else stops such a contract reaching
  `worktree_closeout_apply`. Move the reset ahead of it and the reset inflicts exactly the
  damage the refusal exists to prevent: a mixed reset in a checkout somebody works in discards
  their `git add -p` selection.
- The second lists `git diff --name-only --diff-filter=U`. `git add -A` over an unmerged index
  does not fail — it *resolves* every conflict to whatever the working tree holds, markers and
  all, and closeout then commits that. Move the reset ahead of it and the check is **silently
  disarmed**: `git reset` drops the unmerged index entries and removes `MERGE_HEAD`, so
  `--diff-filter=U` reports nothing and the refusal never fires again.

**A refused gate leaves the worktree staged, deliberately.** There is no rollback and none is
wanted: this checkout is the task's own disposable worktree (which is what the first refusal
makes true rather than assumed), nothing is committed, and the next attempt resets and
restages from the working tree so it reaches the index a first run would have reached. An
earlier attempt saved the index file aside and copied it back; that machinery is **gone rather
than fixed**, because it could not survive `core.splitIndex` (the saved pointer outlives the
`sharedindex.<sha>` that `add -A` expires, leaving `status` exiting 128) nor `SIGTERM`, which
is how an MCP server actually dies.

Both refusals and the staging are **conditional on the gate running at all** —
`requires_strict_code_quality(contract.code_worktree, code_would_commit=…)` still decides, so a
consuming checkout carrying no `code_quality/check.py` wrapper stages nothing early, runs
neither refusal, and reaches `commit_if_dirty`'s own `git add -A` exactly as before.

Three surfaces were re-worded to match, and they are wire-visible:
`code_quality_gate.code_quality_gate_preview`'s `enforced` reason (line 77) now names the
staging; `closeout_preview_payload`'s `closeout_order` (line 312) lists the two refusals, the
reset-and-stage step and the gate as four entries where it listed one; and the preview
`summary` says a refused gate leaves the worktree staged and commits nothing.
`run_strict_code_quality_gate`'s docstring records the corresponding boundary — it certifies
the index it is handed and says nothing about how it came to look that way, so its failure
message claims only that nothing was committed, **not** that the staging was undone.

Pinned by `mcp/tests/test_worktree_closeout_quality_gate.py`:
`CloseoutGateSeesCreatedFilesTests` (a created file's lint error fails the gate; the gate's
scope is the commit's content), `TaskWorktreePreconditionTests` (the repository's own checkout
is refused before anything is staged; a series contract's `code_worktree` is exactly that
checkout), `ConflictedIndexTests::test_the_reset_runs_after_the_conflict_check_not_before_it`,
and `RetryStagesWhatAFirstRunWouldTests::test_a_retry_commits_the_tree_a_first_run_would`.

## Update History
- 2026-08-01T00:00+02:00 — 260731-EFA-L4 curator. **Corrected the closeout claim that a quality
  failure leaves everything untouched**: `closeout_result` now reaches the gate through
  `_gate_staged_code`, which resets and stages the code worktree first, so the index is one
  mutation that precedes the gate and deliberately survives a refusal (no commit is created —
  that part still holds). Added the L4 section: why staging is what makes the gate see files a
  task *created* (`derive_scope` reads `git ls-files`, closeout commits `git add -A`; `abc7cbcc`
  itself shipped four unread added files, two of them `.py`), why the mixed reset rather than a
  bare `add -A`, and why `_refuse_outside_a_linked_worktree` / `_refuse_conflicted_worktree`
  must both run *before* the reset — `git reset` drops the unmerged entries and `MERGE_HEAD`,
  which silently disarms the conflict check. Recorded that all five contract-amending modules
  moved their vocabulary cells off `dataclasses.replace` (typeshed's `**changes: Any` meant
  pyright checked none of them) onto `ContractCells`/`amend_contract`, with the six call sites,
  and that `build_start_contract` now returns a `ContractError` as an `invalid-request` result —
  noting that this `except` is broader than its docstring claims. Rewrote the `guidance.py`
  bullet: this module now *declares* `WorktreePhase`/`NextOperation`/`NextTool` and
  `models/worktree.py` imports them, `lifecycle_guidance` returns the `LifecycleGuidance`
  TypedDict, `status_payload` returns `WorktreeStatusPayload` with the new optional
  `unknown_contract_cells`, and the gate/block payloads moved to the sibling `recovery_guidance`
  so a wider recovery set cannot widen `WorktreeSummary.nextOperation`. **Citations: checked 26,
  repaired 18.** Still correct: `git.py` L7/L18/L85 and `landing.py` L31/L56/L79/L93/L124.
  Moved (L4 inserted lines above them; every new range re-read and confirmed to contain the
  named symbol): `integrate.py` +2 — merge `--ff-only` L460→**L462** and memory L465→**L467**,
  `reset --hard` L476-477→**L478-479**, rebase L182→**L184** and L234→**L236**; `start.py` +7 —
  `branch -f` L386→**L393**; `cleanup.py` +5 — `worktree remove` L27→**L32**, `branch -D`
  L72→**L77** and L89→**L94**, `_remote_git` L108→**L113**,
  `delete_remote_branch_if_present` L122→**L127**, `_push_branch_deletion` L136→**L141** and its
  `push origin --delete` L137→**L142**; `code_quality_gate.py` +11 — `quality_environment`
  L157→**L168**, `git_environment()` L167→**L178**, `_git_common_dir` L176→**L187**, its
  `run_git` L179→**L190**. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T22:52+02:00 — 260731-EFA-L3 curator (re-verification pass after the fix workers).
  **Repaired the two citations the fixes moved and confirmed the other eleven.** Still correct,
  each re-read against the current file and confirmed to contain the symbol the claim names:
  `git.py` `commit_if_dirty` L85, `integrate.py` merge L460/L465, `reset --hard` L476-L477, rebase
  L182/L234, `start.py` `branch -f` L386, `cleanup.py` `worktree remove` L27, `branch -D` L72/L89,
  `_remote_git` L108, `delete_remote_branch_if_present` L122, `_push_branch_deletion` L136-L137,
  and `landing.py`'s `_PROBE_TIMEOUT_SECONDS` L31 with its two `run_git` probes at L56 and L79.
  **Moved:** `code_quality_gate.py::_git_common_dir` L168 → **L176** and its `run_git` call L171 →
  **L179** (`quality_environment` gained a docstring above them); `landing.py::_pr_for` was cited at
  L104, which is inside the `gh` argv rather than at the definition — now **L93**. **Two new
  route-visible facts:** `quality_environment` (L157) now builds from `git_environment()` (L167)
  instead of `dict(os.environ)`, so the spawned quality wrapper no longer inherits the eight
  repository selectors — the gate decides which repository gets certified and must not depend on a
  child process behaving; and `_pr_for`'s `gh pr list` spawn now passes `env=git_environment()`
  (L124), because `gh` resolves the repository through git and would otherwise list another
  repository's pull requests under this worktree's branch name. Corrected the import roll-call,
  which named six modules: all nine git-touching modules in this route import from the kernel runner
  (`cleanup.py`, `code_quality_gate.py` and `landing.py` were missing). Verification metadata pinned
  until closeout stamps the L3 commit.
- 2026-07-31T20:52+02:00 — 260731-EFA-L3 curator: corrected the `git.py` Hot Path bullet,
  which claimed the module "owns raw Git subprocess operations" — it no longer owns a
  runner at all, only Git vocabulary over the one owner (`kernel/git_command.run_git`,
  imported at `git.py` line 7; `require_git` at line 18). Made the `landing.py` bullet
  precise about which of its probes are now shared-runner calls versus the `gh`
  subprocess it still builds itself. Added the "This Route No Longer Runs Its Own Git"
  section: the dropped `env=git_environment()` guard and the destructive operations that
  sat behind it, the three timeout classes that had to exist before consolidation was
  safe, `cleanup.py`'s newly bounded remote calls (`_remote_git`, stall folds into
  `remote-unreachable`), and `code_quality_gate.py`'s guarded `_git_common_dir`.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2: route-wide parameter-object pass (`VerifiedChange`,
  `ContractTask`/`LeafIdentity`/`RepoBranchPlan`, `StartingEnclosure`/`StartBeat`,
  `RetiringBranch`, `IntegrationSources`/`IntegratedCommits`, `ProviderSetupJob`) plus the
  `start_result` three-stage split, the `lifecycle_guidance` phase groups and the `sync` helper
  extractions. Behaviour is unchanged throughout. Verification metadata pinned until closeout
  stamps the L2 commit.
- 2026-07-31T04:28+02:00 — 260731-EFA-L1 curator: recorded that `code_quality_gate.py` no longer
  decides by repository name. Applicability is now wrapper availability in the target checkout, the
  preview reports `enforced` / `no-code-commit` / `wrapper-unavailable`, and both `closeout.py` call
  sites pass `contract.code_worktree`. Recorded the unannotated-call-site hazard and the single
  regression that guards it. Verification metadata remains pre-commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental CRAP/commit-gate curation:
  added the fail-closed `code_quality_gate.py` authority and corrected closeout's
  mutation order to quality-before-commit. Verification metadata remains
  pre-commit.

- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: closeout route-index preview and apply now forward the
  resolved `context.storage` authority explicitly to the deterministic builder.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1 route impact (small): `cli.py` gained the `heal-leaf-ids`
  subcommand — the explicit one-shot seam for `worktree_contract.heal_contract_leaf_ids` now that
  contract loads are walk-free and never normalize legacy leaf ids (detail in the `cli.py` and
  `worktree_contract.py` sidecars). The module split this overview describes is unchanged.
  Verification metadata pinned until closeout stamps the 260712-PTS-L1 commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: worktree guidance separates fresh interactive landing probes from projected status, which consumes only pre-observed landing facts.

- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2 route impact: start leaf-ref resolution now accepts
  standalone/light `task.json` roots through doc-id/slug/folder aliases and the shared resolver skips
  non-task sibling JSON artifacts by schema marker while keeping malformed task docs loud. Verification
  metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4 route impact: worktree start contract construction and
  leaf-ref validation moved out of `start.py` into `start_contract.py`/`leaf_ref_start.py`, backed by
  the dedicated `worktrees/leaf_refs.py` resolver; accepted refs
  persist doc ids, and invalid refs refuse before start writes. Verification metadata pinned until
  closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T19:30+02:00 — No route impact: 260707-HFX-L2 refines `start.py`'s memory mtime sync
  in place — divergent-content files keep fresh checkout mtimes so the grepai watcher re-embeds
  exactly the delta instead of silently skipping it (detail in the start.py sidecar and the new
  `test_provider_index_lifecycle.py`). No module added; the modules route model is unchanged.
- 2026-07-07T18:40+02:00 — No route impact: 260703-L18 finding 7 implements `start.py`'s
  missing-ledger-mapping recovery `memory_choice="reconciliation"` (records the unmapped code base ->
  the ledger's memory content tip the way closeout ledger syncs do, then proceeds to a started worktree)
  and prunes the block to only executable choices (`custom` removed). It reuses the existing
  `memory_choice` arg and adds no module, so the modules route model this overview describes is unchanged
  (detail in the `start.py` file sidecar).
- 2026-07-07T06:10+02:00 — No route impact: PR #100 review fixes (merge `e358c4a`) hardened
  `start.py`'s `_reconcile_missing_mapping` with a memory-source-branch guard (refuses when the
  official memory repo is checked out elsewhere; detail in the start.py sidecar). No module added;
  the modules route model is unchanged. Post-merge onboarding refresh, developer-approved.
- 2026-07-06T03:30+02:00 — No route impact: 260703-L11 reviewed `guidance.status_payload`'s `code_worktree_exists`/`memory_worktree_exists` probes as the existence-reporting contract the new projection flags mirror; no file in this route changed — the stat happens in `observer/snapshots.py`.
- 2026-07-05T19:55+02:00 — 260703-L8 route impact (cycle 7, small): integrate's dry run now evaluates-and-reports the seam guard (`handover_gate` in the preview; enforcement stays real-run-only; no dry-run contract mutation, AR4-2), and the new pure `unmatched_handover_gate_warning` surfaces unmatched OPEN handover gates as a `handover_gate_warning` enclosure spelling check on gateless results (AR4-1b). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 — 260703-L8 route impact (cycle 6, small): the integrate seam guard is re-addressed — the pure `handover_gate_guard` folds every gate log (`GateStore.all_current`) and matches `master-handover-approval` gates by `enclosure` against the contract's `task_name`/`parent_task_name`, replacing the inert `contract.lifecycle_id` lookup; the configured policy now reaches it from the controller. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:24+02:00 — 260703-L8 route impact (cycle 5, small): `integrate_result` enforces the master-exit seam — an existing `master-handover-approval` gate must be policy-valid-approved (mirror of the closeout gate; gateless stays additive) or the run returns handover-gate-blocked. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:32+02:00 — No route impact: abandon docstring vocabulary updated to the `l-01-agent-lifecycles` orchestrator read-only/abandon exit; no behavior change (260703-L9).
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: closeout preview/apply now
  threads the trusted gate policy through `WorktreeArgs` and evaluates
  `closeout-approval` through that policy, preserving human approvals while
  allowing only configured delegated orchestration approvals. Verification
  metadata pinned until closeout stamps the L4 commit.
- 2026-07-03T00:35+02:00 — L11 route impact: start's existing-contract branch recreates fresh for cleanup in {abandoned, reopened} and restamps the leaf doc's lifecycleId post-write; abandon's controller ends its anchored ambient lifecycle. The reopen implementation itself lives under tasks/.
- 2026-06-29T23:18+02:00 — No route impact: `start.py` now derives the recorded memory base from the memory source branch tip (`_memory_base_for_source`) instead of the repo HEAD; the module structure and route model are unchanged (detail in the start.py file sidecar; task 260629_post-landing-cleanup L3).
- 2026-06-29T15:30+02:00 — operations-integration L3: `git.py` gained `changed_files_with_counts` (+ `_rename_aware_path`), the counts/status change-set primitive (keeps deletions; binary → `None`; untracked → `A`; rename → post-rename path) feeding the L3 serving change-set API (`serving/changeset.py`). Refreshed the `git.py` Hot Path bullet. The module split this overview describes is unchanged. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
- 2026-06-27T23:09+02:00 — Task 32 route impact: refreshed the `cleanup.py` hot-path paragraph for exact observer drift-snapshot reclamation during worktree cleanup, including dry-run reporting and the contract-owned repository/branch boundary. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T21:10+02:00 — Task 30: refreshed the closeout hot-path summary for
  already-integrated re-closeout behavior: integrated source tips are valid
  closeout bases, closeout previews expose pending integration reopen, apply
  reopens only for unlanded new code/memory content, and clean no-op re-closeout
  avoids duplicate ledger mapping. Verification metadata pinned until closeout
  stamps the task-30 code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree modules now treat a master root `series-contract.md` as the integration branch contract and each leaf `enclosures/<leaf-id>/series-contract.md` as worktree material; `WorktreeArgs` carries `parent_task`/`leaf_id`, and finalization can archive completed root tasks. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T00:03+02:00 — Task 14 cleanup correction: refreshed the `cleanup.py` hot-path paragraph for child-edge cleanup. Cleanup still hard-guards on carryover and proves task work branches against the contract source branch before deleting them, but no longer retires parent/source branches; those branches are finalized by their own lifecycle edge.
- 2026-06-23T22:50+02:00 — Dashboard task 14: added `finalize.py` to the route model. The terminal finalizer proves one landed parent-child edge, runs or verifies cleanup, and marks the current task plus immediate parent row complete; PR-gated edges reduce to the same local ancestry proof after merge/pull, and squash equivalence is intentionally out of the default path. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T15:09+02:00 — Task 13 cleanup correctness: refreshed the `cleanup.py` hot-path paragraph for source-branch-proof work-branch deletion (`merge-base --is-ancestor work_branch source_branch`, then `branch -D`), preserved kept-branch reporting for unmerged work, separated the then-existing source-branch retirement path from task work-branch deletion, and noted dry-run directory classification now subtracts scheduled worktree/provider-runtime removals while real cleanup stays empty-dir-only. Task 14 later removed source-branch retirement from cleanup.
- 2026-06-23T07:25+02:00 — slice 09 (gate-signal adoption, S1 visibility fix): refreshed the `guidance.py` Hot Path bullet for the removal of the dirty-tree → `commit-approval-pending` branch — `lifecycle_guidance` no longer reads a commit-approval gate off `git status`; a dirty worktree falls through to its honest lifecycle-position phase (closeout-completed → `integration-pending`). The gate is owned by the closeout preview / a raised `closeout-approval` `GateNode`; the unused `contract_has_worktree_changes` import was dropped. The module split this overview describes is unchanged; detail in the `guidance.py` sidecar. Verification metadata pinned until closeout stamps the slice-09 code commit.
- 2026-06-21T06:40+02:00 — slice 05m (carryover-before-cleanup + work/source branch retirement): refreshed the `guidance.py` Hot Path bullet for the new public `carryover_done` (reads the official ledger to detect the carry; external-only) and the `integration_status == "completed"` split into the `carryover-pending` (routes `memory_carryover_apply`) vs `cleanup-pending` (carries `carryoverDoneAt`) phases; and the `cleanup.py` bullet for the carryover hard-guard (refuses cleanup before the carry, since it deletes the parked memory branch) plus the new `_retire_branch` / `delete_remote_branch_if_present` retirement of BOTH the worktree and (PR'd) source branches — local for code + memory, remote for the code source branch. Verification metadata pinned until closeout stamps the 05m code commit.
- 2026-06-21T05:30+02:00 — slice 05l P2 (landing-arc probe hardening): refreshed the `landing.py` Hot Path bullet for the direct `origin/<base>` probe (`_main_ref` + the new `_default_branch`, resolving origin's default via the remote HEAD symref with no `fetch`) — visible across the whole landing window before any PR and independent of `gh`, its `state` tracking whether THIS work landed rather than merely whether main exists — and the PR ref's new `at` timestamp (gh's mergedAt/createdAt). The probe re-fires every projector tick (~1s) so no milestone hook is needed. Carryover/cleanup lifecycle correctness is 05m's scope, not here. Detail in the `landing.py` sidecar. Verification metadata pinned until closeout stamps the 05l-P2 code commit.
- 2026-06-21T04:10+02:00 — slice 05l P1 (backend teardown visibility, Gap A): `guidance.py`'s `lifecycle_guidance` gained a `cleanup == "abandoned"` branch (right after `cleanup == "completed"`) returning a dedicated `abandoned` phase (`nextOperation: "done"`); before this an abandoned worktree fell through to the `worktree-started` phantom. The observer reducer maps the phase for the 05k teardown render. Detail in the `guidance.py` sidecar. Verification metadata pinned until closeout stamps the 05l-P1 code commit.
- 2026-06-18T12:10 — Task 6 slice 6b: `closeout.py` gained server-side gate enforcement (refuse unless the lifecycle's `closeout-approval` gate is developer-approved via `controlplane.evaluate_closeout_gate`; mark `applied`; `closeout_gate` payload). The module split this overview describes is unchanged. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1: added `landing.py` (best-effort successful-landing arc observation — `git ls-remote` branch tips + best-effort `gh` PR state, gated to the landing window) to this route; `guidance.py`'s `status_payload` emits its `landing` block. Detail in the file sidecars. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-16T03:25 — No route impact: slice 5f S6 (§9) adds the happy-path start-progress emits to `start.py` (`_record_start_progress` at the `preflight` / `code-worktree` success points, closing the gap where only blocked early returns emitted); the modules route model this overview describes is unchanged (detail in the `start.py` file sidecar).
- 2026-06-15T19:35 — No route impact: slice 5e (§5.4) adds best-effort start-progress writes to `start.py` (`_record_start_block` / `_clear_start_block` at the pre-contract blocked returns); the modules route model this overview describes is unchanged (detail in the `start.py` file sidecar).
- 2026-06-13T18:45+02:00 — No route impact: slice 2c threads `lifecycle_id` through `args.py`/`start.py` (`_build_start_contract` stamps the observable-lifecycle contract anchor) and emits it from `guidance.py`'s `status_payload`; the modules route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-12T19:06+02:00 — Issue #83: closeout worklist covers the unverified committed range (`closeout_changed_paths` in `closeout.py`, `committed_changed_paths`/`commit_text_or_none` in `git.py`), the onboarding plan gained the two-tier `working_paths` split with the non-blocking `unonboarded` report, body gates baseline at `contract_memory_verified_commit`, and scaling payload lists are bounded to count + sample.
- 2026-06-11T06:47+02:00 — No route impact: issue #62 removed the direct-closeout functions from `closeout.py`, the `direct-closeout` CLI subcommand from `cli.py`, and the facade re-exports — closeout is worktree-only; the module split this overview describes is unchanged (detail in the file sidecars).
- 2026-06-10T09:56+02:00 — GitHub #54 sub-task D: added `sync.py` (worktree_sync mid-task base sync) and `guidance.py`'s fetch-free `freshness` status block; `args.py` gained `memory_sync_choice`.
- 2026-06-10T09:30+02:00 — GitHub #54 sub-task B: `start.py` gained the stale-base preflight (`stale_base_choice` recoveries) and the memory source branch auto-template; `args.py` gained `stale_base_choice`.
- 2026-06-10T07:35+02:00 — GitHub #53: added `provider_async.py` (background provider setup launch, progress projection, teardown guard); `start.py` split preflight from launch and writes the contract before launching; cleanup/abandon gained the live-setup guard.
- 2026-06-10T05:20+02:00 — Issue #56 sub-task 2: route overviews get the same body gate scoped to nearest-governing routes (`No route impact:` marker; ancestors report as `stamped_without_body_review`), surfaced in closeout previews and apply payloads.
- 2026-06-10T04:47+02:00 — Issue #56 sub-task 1: `onboarding.py`'s content gate became the four-case body/history classification with in-band `No content impact:` attestation, shared parsing helpers moved to `kernel/onboarding_doc.py` (facade re-exports kept), and closeout payloads surface attested sidecars.
- 2026-06-01T00:00+02:00 — Added `abandon.py` (discard without integration) and `provider_teardown.py` (full-reclaim Docker + rmtree teardown) to the Purpose and Hot Path Summary listings.
- 2026-05-31T12:30+02:00 — Documented the new `args.py` typed `WorktreeArgs` cross-layer DTO replacing `argparse.Namespace` and `integrate.py`'s atomic all-or-nothing fast-forward behavior (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created when `c-09-git-worktree-manager` skill worktree lifecycle logic was split into focused implementation modules.
