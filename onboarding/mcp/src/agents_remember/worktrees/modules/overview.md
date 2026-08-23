# mcp/src/agents_remember/worktrees/modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `mcp/src/agents_remember/worktrees/modules` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview      | `../../../../overview.md`                  |

## Purpose

The `worktrees/modules` package contains the extracted implementation modules
behind the `git_worktree_manager.py` facade. It separates Git adapters, lifecycle
status guidance, start preparation, onboarding refresh, strict code-quality gating, closeout, integration,
cleanup, lifecycle finalization, abandon, provider teardown, start-contract leaf-ref normalization, the typed cross-layer argument DTO, and CLI
argument wiring while preserving the public facade import path. Reopen is deliberately NOT here:
`task_reopen` lives in the tasks package (leaf L11) because it reopens a task, and this route's start path
merely honors its `cleanup: reopened` tombstone (recreate fresh, restamp the leaf doc's lifecycle).
The committed L2 layout groups the start-contract, provider-preflight, leaf-ref, and result helpers
under `startup/`; `start.py` remains the coordinating mutation entrypoint.

## Hot Path Summary

Public worktree modules consume closed configured-contract admission and preserve their existing mutation locks/rereads. Cleanup and abandon remain fail closed before destructive seams until external terminal archive proof exists.

L23 makes Dagger the sole acceptance executor. `clean_quality_executor.py` materializes the exact
reviewed candidate and required ancestry into the pinned graph, starts a fresh attempt, bounds live
output, and atomically replaces the enclosure's current reports; there is no local compatibility
runner. `code_quality_gate.py` plans targeted or full Dagger authority with an explicit diff base.
`closeout_staged_quality.py` owns the linked/conflict refusals, accepted-tree rechecks, complete
staging, reviewed hook, and targeted gate. `closeout.py` and `integrate.py` preserve approval and
merge ordering while rechecking lineage after long quality work; integration remains failure-atomic
before source refs move. `git.py` owns exact candidate-tree and repository-identity helpers.
`startup/start_result.py` separates result projection from start coordination, and the external
`worktrees/closeout_recovery.py` reconciles post-claim code, memory, and ledger commits without
replaying completed irreversible steps.

- `git.py` owns this route's Git vocabulary — the typed helpers and small repository
  state checks every operation module speaks — but **since 260731-EFA-L3 it no longer
  owns a Git runner**. It imports the one owner (`from agents_remember.kernel.git_command
  import run_git`, line 7), and its own `require_git` is now raise-on-nonzero over
  it. Raw results preserve the runner's surrogateescape contract, while only the
  raised failure diagnostic passes through `_transport_safe_git_diagnostic` so
  invalid Git bytes become literal escapes before MCP JSON serialization. See the
  260731-EFA-L3 section below for why the runner/facade distinction is a correctness
  property and not bookkeeping. Its helpers include
  `committed_changed_paths` (issue #83: the unverified committed
  range — tree-diff `base..HEAD` ∩ `verified..HEAD`) and the
  `commit_text_or_none` baseline reader behind the closeout body gates.
  The certified closeout path also uses `run_pre_commit_hook_if_configured` followed by
  `commit_verified_staged`: the former runs the fast hook before the strict wrapper, while the
  latter commits exactly that verified index with hooks bypassed and never restages later edits.
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
  Captured output is decoded as UTF-8 with replacement so malformed diagnostics cannot suppress
  the completed report. On non-Windows hosts only ephemeral quality scratch is normalized to the
  short process-safe `/tmp` root; the durable latest transcript remains the enclosure-owned,
  atomically replaced `reports/test-results.md`.

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
- `start.py`, `startup/start_contract.py`, `startup/leaf_ref_start.py`, `closeout.py`, `integrate.py`, `cleanup.py`,
  `finalize.py`, and `abandon.py`
  own the named `c-09-git-worktree-manager` skill lifecycle operations.
  `start.py` calls `startup.start_contract.build_start_contract` to resolve the requested leaf ref through the
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
  template. For master tasks, `startup/start_contract.py` creates or loads the root
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
  contract-owned repository/branch snapshot. `integrate.py` refuses while an undecided or policy-invalid `master-handover-approval` gate addressed to the integrating master exists anywhere in the workspace: the pure `handover_gate_guard` folds every gate log (`GateStore.all_current`) and matches gates by `enclosure` against the contract's `task_name`/`parent_task_name` — never the consuming contract's lifecycle — evaluating the application-threaded configured policy (the master-exit seam consumer, mirroring the closeout gate; gateless stays additive). Since cycle 7 the guard is evaluated on the dry run too — reported (`handover_gate` in the preview, whose summary names `handover-gate-blocked` when the real run would refuse) but enforced only on the real run, with no contract mutation on the dry-run path — and the pure sibling `unmatched_handover_gate_warning` puts a `handover_gate_warning` (unmatched OPEN handover gates + a verify-the-enclosure-spelling note) on gateless dry-run/integrated payloads, so a typo'd exact-string address cannot fail open silently. It then performs the code and
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
  Route planning also includes overview documents changed since the task's
  verified memory baseline, even when their source drift predates the current
  leaf code range. Those directly edited overviews become domain-evident for the
  existing body/history classifier: the expansion makes them stampable in the
  transaction but never permits metadata-only or untraced refreshes. A narrow
  generated-data exception recognizes a task-edited overview whose only body
  delta is the final reference-cell `path:line[-line]` coordinate; sanctioned
  citation repair can advance those ranges without fabricating history, while
  prose, claim, anchor, path, table-shape, and other body changes still gate.
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
  (`controlplane.evaluate_closeout_gate(..., policy=args.gate_policy)`) and
  reports a `closeout_gate` block; gateless lifecycles keep the chat commit gate.
  **Since 260731-EFA-L5 the "marks it `applied` on success" half of that is retracted** — see the L5
  section below. The `applied` snapshot is now written by `_claim_closeout_gate` (line 449) through
  `GateStore.claim_approval`, one statement *above* the first commit (line 795), not after
  `write_contract`; `_mark_closeout_gate_applied` was deleted, and the early check is renamed
  `_refuse_unsatisfied_closeout_gate` (line 424) because it can only deny.
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
  reached directly**: `closeout_result` (line 743) calls `_gate_staged_code` (line 684) at line 786,
  which stages the code worktree first, so the *index* is one mutation that now precedes
  the gate and survives a refusal. See the L4 section below for why staging is what makes
  the gate see created files, and why the two refusals must run ahead of the reset.
  (These four line numbers all moved with 260731-EFA-L5's +98 lines in `closeout.py`; the symbols
  and the claims are unchanged.)
- `args.py` defines the frozen `WorktreeArgs` cross-layer DTO that operation
  modules consume in place of `argparse.Namespace`; `from_namespace` builds it
  from partial CLI/application namespaces with per-field defaults. It carries `parent_task` and `leaf_id`
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The package is imported through the public worktree manager facade. | `__all__` | mcp/src/agents_remember/worktrees/git_worktree_manager.py:96-167 |
| Focused worktree tests exercise the facade and operation payloads. | `WorktreeSupportTests` | mcp/tests/test_worktree_support.py:806-881 |
| Finalizer tests cover landed-commit proof, cleanup blocking, dry-run, and task-document reconciliation. | `LifecycleFinalizeTests` | mcp/tests/test_lifecycle_finalize.py:34-554 |
| Closeout onboarding refresh uses resolved storage authority for deterministic route-index preview and apply. | `refresh_route_indexes_for_context` | mcp/src/agents_remember/worktrees/modules/onboarding.py:492-500; mcp/src/agents_remember/kernel/route_index.py:182-230 |
| Stage-before-gate: a created file's lint error fails the gate, the gate's scope equals the commit's content, both preconditions refuse before anything is staged, the reset runs after the conflict check, and a retry commits the tree a first run would. | `CloseoutGateSeesCreatedFilesTests` | mcp/tests/test_worktree_closeout_gate_scope.py:131-209 |
| The lifecycle state carries the optional worktree phase the panels render. | "phase: WorktreePhase"; "WorktreePhase = Literal[" | mcp/src/agents_remember/models/worktree.py:25-25; mcp/src/agents_remember/models/worktree.py:124-124 |
| The gate replay window: the closeout approval is `applied` before `commit_if_dirty` runs, and a gate failure leaves it `approved` — the two halves of the one-attempt-not-one-success trade. | `ClaimPrecedesTheIrreversibleWorkTests` | mcp/tests/test_gate_replay_window.py:566-674 |
| `GateStore.claim_approval` — the compare-and-swap this route spends approvals through, and `CONSUMED_APPROVAL_GATE_KINDS`, which stops the resulting `applied` snapshot from being reclaimed. | `claim_approval` | mcp/src/agents_remember/controlplane/store.py:199-246; mcp/src/agents_remember/controlplane/interaction_retention.py:48-50; mcp/src/agents_remember/controlplane/interaction_retention.py:185-191 |

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
| `closeout.py` line 831 (`ContractCells` at 848) | `human_review_status`, `closeout_status`, `integration_status`, `cleanup` |
| `start.py` line 141 | `memory_mode="disabled"` (the memory-disabled downgrade) |

Undo one of these back to a bare `replace` keyword and **nothing fails at the call site** —
that is the whole defect. It fails later, at the packet, as a pydantic `ValidationError`
raised inside an MCP tool handler that has no `except` for one. The rule that keeps it shut is
"no `replace` call anywhere may carry one of these six keywords", enforced together with
`mcp/tests/test_wire_vocabulary_exhaustiveness.py`.

`startup.start_contract.build_start_contract` (line 187) gained a second `except` for the same reason.
`worktree_start`'s `workflow_kind` and `memory_mode` reach the MCP signature as free `str`
(the tool declares `workflow_kind: str = "light-task"` and documents `'light-task'` or
`'chat-task'`), and `worktree_contract._task_vocabulary` now *refuses* an unknown one at both
contract factories. Nothing between there and the `@server.tool()` handler catches a
`ContractError`, so line 198 converts it through the new
`startup.leaf_ref_start.invalid_contract_request_result` (line 38) into the same
`WorktreeCommandResult(2, {"state": "invalid-request", …})` shape every other blocked start
already used, naming the legal set instead of producing a traceback. Note that this `except`
is broader than its docstring says: it also catches a `ContractError` raised by the
`write_contract` inside `_parent_series_contract` (line 176), which is a write-validation
failure rather than a bad caller argument — the message still names the field and the file, so
the refusal stays honest, but it is not only about arguments.

### `closeout.py` stages the worktree before the quality gate

`closeout_result` (line 743) no longer calls `run_strict_code_quality_gate` directly; it calls
`_gate_staged_code` (line 684, called at line 786), which does `git reset --mixed --quiet HEAD` then
`git add -A` (lines 738-739) and *then* runs the gate.

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
staging; `closeout_preview_payload`'s `closeout_order` (line 315) lists the two refusals, the
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

## 260731-EFA-L5 Spending An Approval Is One Step Now, And One Consumer Still Does Not Spend It

This route holds two of the three reproduced ways one human approval could be spent twice. The
framing worth carrying at route level: **durability of a record is not atomicity of a decision.**
The gate log's own durability fix (`controlplane/durable_store.py`) made every record survive — and
this route's defects would have existed even if it had never lost a byte.

### `closeout.py`: the claim, and the semantics it changes

The check-then-act pair is gone. `_enforce_closeout_gate` → **`_refuse_unsatisfied_closeout_gate`**
(line 424), which now returns `None` and can only **deny**; `_mark_closeout_gate_applied` is
**deleted, not deprecated**. The spend is **`_claim_closeout_gate`** (line 449), which calls
`GateStore.claim_approval(lifecycle_id, kind=CLOSEOUT_GATE_KIND, now=…, policy=…)` — fold, policy
verdict and `applied` append inside one held lock on the gate log.

**The call site is the design** (line 795): one statement above the first commit, after
`_gate_staged_code` and immediately before `commit_if_dirty`, with a source comment forbidding a
move past the commit. Not earlier, because everything upstream — source-head validation, the
onboarding and route plans, the mixed reset and staging, the strict code-quality gate — only reads
or touches the index of the task's own disposable worktree, and a refused code-quality gate is the
common case, so claiming earlier would burn a developer's approval on a refusal that changed
nothing. Not later, because everything downstream writes a commit somebody would have to undo.

**The route-visible semantic change: an approval authorises ONE ATTEMPT, NOT ONE SUCCESS.** A
closeout that dies after the claim — crashed process, failed memory quality gate, git error, ENOSPC
— leaves the approval consumed and the next closeout needs a fresh gate;
`controlplane/enforcement.py` already words the remedy ("was already applied; open a fresh gate for
a new mutation"). Marking `applied` at the end instead means every way that late write can fail
leaves a live approval sitting on top of an unknown amount of completed, irreversible work — both
shapes were reproduced. A two-phase `claimed` state was considered and rejected: the release is the
same write at the same late position with the same failure modes, so it would need a reaper that
re-opens the window on a timer.

`mcp/tests/test_gate_replay_window.py` pins both halves: the gate is already `applied` by the time
`commit_if_dirty` runs, and a gate failure leaves it `approved`.

### `integrate.py`: an open decision, deliberately left open

**`integrate.py` never consumes the `master-handover-approval` gate at all.** `integrate_result`
(line 516) folds `gate_store.all_current()` (line 534), evaluates `handover_gate_guard` (line 535),
refuses when the verdict is not permitted, and integrates — there is no `apply_gate` and no
`claim_approval` anywhere in the module. This is **not** a record this leaf dropped and not a
regression: the consume was never written, on any commit. Today the handover gate is a *guard*, not
a *spend*, and nothing prevents one approved handover gate from permitting two integrations.

It is left open for two reasons a reader needs before closing it:

- **It needs a different key.** That gate is matched **cross-lifecycle by `enclosure`** against the
  contract's `task_name`/`parent_task_name` and lives on a different log than the integrating
  lifecycle's, so `claim_approval`'s `(lifecycle_id, kind)` key cannot address it.
- **`closeout.py`'s `integration_reopen` path means a legitimate re-integration exists.** Consuming
  on the first integration would make a re-integration of newly transported content start demanding
  a fresh handover approval, which nobody has decided is correct.

The retention half is already in place: `master-handover-approval` is in
`interaction_retention.SEAM_CONSUMED_GATE_KINDS`, hence in `CONSUMED_APPROVAL_GATE_KINDS`, so an
`applied` snapshot of that kind would be retained with no TTL the moment something writes one.

## 260731-EFA-L16 — Closeout's Citation Gate Before The Suite

`closeout_result` runs the citation gate (`range_resolution` + `claim_reopen`) before the strict
wrapper and the code commit — working-tree checks that clear without a commit — and keeps drift,
shape, and history order in the post-commit sanity phase. The L6 clearing condition required the
commit it was checking against, deadlocking every structural change; `_combined_memory_quality`
reports the two phases as one gate. The approval claim still precedes the first irreversible
act.

## 260731-EFA-L17 — The Altitude-Routed Quality Gate

This route owns the quality altitude ladder's machinery half. `code_quality_gate.py` gained
`QualityGatePlan` (mode `targeted`/`full` + optional cap), `GATE_TARGETED`/`GATE_FULL`, the
`memoryPolicy`/optional `memoryCap` payloads, cap-kill naming (returncode -9 / shell 137), and altitude invocation labels
(`AR_QUALITY_INVOCATION` = `closeout-staged` / `master-integration`).
`closeout.py` passes the leaf targeted plan at both call sites and through `_gate_staged_code`;
`memory_quality_check` stays a per-leaf closeout gate. Leaf integration lands the exact
closeout-certified commit without rerunning acceptance. `integrate.py` runs a gate only for
series/master contracts: the full wrapper once with host-managed RAM/swap by default;
an optional explicit cap is read from `load_agentic_settings(...).quality_gate.memory_cap_bytes`. A refusal returns
`blocked-quality-gate` and nothing merges.

## 260731-EFA-L9 Route Impact

`provider_teardown.py` moved to `application/provider_runtime.py` (absorbing the former
`provider_async.py` setup launcher) so worktrees stops importing providers; `provider_async.py`
is deleted. The new `worktrees/services.py` declares the `ProviderLifecyclePort`/
`MemoryQualityPort`/`CitationGuardPort`/`TerminalGuard` ports and the `WorktreeServices` bundle,
and `worktrees/modules/contract_reader.py` implements the kernel resolver's `ContractReaderPort`.
The closeout/integrate/guidance machinery is unchanged in behavior.

## L23 Parent-First Lineage Gate

Worktree start, attach, and reopen now consult task-derived ancestry before
resuming context or mutating task/contract state. Status publishes the same
projection and ordered `worktree_sync` contract path. Remote stale-base choice
is a later policy and cannot override super-to-master-to-leaf admission.

## L23 Long-Gate Source-Lineage Enforcement

Closeout and integration prove the complete transitive source-lineage chain at preflight, recheck
it after potentially long quality work, and check again immediately before approval claim or
source merge. Integration also pins exact code and external-memory source tips across the gate;
movement yields a retry without ref movement. Supporting cohesion changes route clean-quality
report promotion through the atomic-replace primitive and isolate strict-plan and closeout-result
construction without changing their enforcement authority.

Closeout separately pins the durable operation's full code candidate across quality at every
altitude. The final reversible check recomputes that tree before approval claim; leaf closeout also
revalidates its independent route-review record, while series/master closeout bypasses the
inapplicable terminal-leaf evidence and targeted acceptance. Series/master closeout also requires
a clean code checkout and records only its already-landed HEAD; it cannot create master code.

Repository linkage within that proof follows Git's resolved absolute common directory. Parent and
leaf contracts may address sibling linked worktrees of the same repository; distinct checkout
paths do not create a false repository mismatch, while missing or unresolvable Git identity still
fails closed.

## R39 Lifecycle Acceptance Route

Closeout and integration now split acceptance without duplication: a leaf is targeted-certified
once during closeout and lands without a rerun; a master runs full once during integration.
Series/master closeout requires clean landed code and runs no gate. The shared adapter refuses
host execution, applies an explicit self-wrapper-required policy to Agents Remember, and
revalidates the accepted candidate after long quality work before approval or merge.

## R42 Recovery Ownership

The route still coordinates closeout, but it no longer defines the typed memory outcome or proves
already-committed recovery cells itself. Both moved to sibling owner
`worktrees/closeout_recovery.py`; the coordinator imports them before amending the contract. The
exact staged-scope regression also moved to its own test module to satisfy the file-size rail.

## R43 Fail-Closed Repair

The closeout coordinator now narrows candidate-tree typing only after mandatory admission, and the
quality adapter consistently says `self-owned wrapper` while refusing non-Dagger executors in both
command and memory-policy builders. Self-repository enforcement and consumer opt-in remain distinct.

## 260815-DAG-L3 Queue-Owned Irreversible Boundaries (Superseded In Part By CLIVE L2)

This section records the earlier DAG queue design: leaf closeout claimed and certified queue rows,
integration claimed/consumed them, and task-fact writers published through queue governance. CLIVE
L2 moves operation recovery, generation controls, worker termination, direct landing, and durable
mutation evidence to the root journal, and its touched task-document publisher no longer uses the
former queue-store wrapper. Some selected/in-flight/certified queue schema and closeout
claim/certification transitions still exist in the L2 source. Their removal, along with task-change
invalidation and waiting-only rebuild, belongs to L3.

## 260815-DAG-L4 L4 Exact Worktree Lifecycle

Start, closeout, integrate, sync, cleanup, abandon, and reopen now share task-derived branch authority. Integration uses exact named-ref CAS and crash recovery; atomic series closeout records a complete leaf landing chain; lowest Git/worktree/terminal writers require capabilities instead of trusting caller-supplied branch names.

## 260815-DAG-L13 Atomic-Sequential Lane

`startup/start_contract.py` gates master series bootstrap on the effective execution nature (a nature-less
legacy master resolves atomic; organizational semantics exist only under an authored graph) and,
under the atomic-sequential default, returns a blocked `sequential-lane-owned`
`WorktreeCommandResult` naming the lane owner and legal next operations instead of starting a
second in-flight master; the block fails closed when the commanding sprint cannot be resolved.
Terminal series artifacts are ignored and reported through `startup/start_result.py`'s
`staleSeriesArtifact` fact. `integrate.py` surfaces the queue consume's stale-by-evidence siblings
on the result payload (`staleByEvidence`, each naming `worktree_sync`).

## 260815-DAG Master Full-Gate Repair Route Impact

`closeout_staged_quality.py` moved to the new `worktrees/queue/` sub-route; remaining module import paths updated to the moved `queue`/`integration` packages; `closeout.py` extracted `_closeout_quality_facts`.

## 260821-CLIVE-L1 Execution Modules

`args.py` transports one normalized effective closeout input, while legacy synchronous CLI apply fails closed. `closeout.py` coordinates journal-authorized execution and exact contract finalization and threads that effective value explicitly through every code/external/recovery consumer; external-memory refresh, memory commit, and ledger commit have moved to the new single owner `closeout_external.py`. That owner uses explicit accepted messages and mutation evidence with no generated ledger subject or fallback. Guidance remains contract-pure: it publishes only static `intent_note` and routes exact candidate-derived requirements to preview/apply. Abandon and cleanup call lifecycle compatibility explicitly under the pure serialization lease.

## 260821-CLIVE-L2 Current Architecture

Closeout and integrate start or resume journal generations; sync/cleanup/abandon use the same admission projector but retain their own serialization. No module enumerates lower configured-reader failures or adds a fallback reader. Terminal retirement preserves canonical evidence; deletion is a later archive-proven operation.

`integration_recovery.py` proves exact ref convergence and the external-memory head before finalization recovery. The `startup/` package split keeps start derivation/result collaborators separate from `start.py` without retaining the old flattened import paths.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| Closeout public execution boundary. | L363-L425; L1002-L1091 | `mcp/src/agents_remember/worktrees/modules/closeout.py` |
| Fail-closed cleanup result. | L624-L678 | `mcp/src/agents_remember/worktrees/modules/cleanup.py` |
| Integration recovery requires exact authority-ref convergence and exact journaled ledger-head proof. | L18-L25; L28-L45 | `mcp/src/agents_remember/worktrees/modules/integration_recovery.py` |
| Start helpers now live below the dedicated startup package marker. | L1 | `mcp/src/agents_remember/worktrees/modules/startup/__init__.py` |

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: recorded the `startup/` package move and new integration-recovery owner, repaired current route references, and verified the governed route at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: route claims reconciled to accepted candidate tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: `closeout_staged_quality` moved to `worktrees/queue`; module imports updated; `closeout.py` extracted `_closeout_quality_facts`. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: recorded the atomic-sequential lane block
  in `start_contract.py`, the `staleSeriesArtifact` fact in `start_result.py`, and the
  `staleByEvidence` payload on `integrate.py` results; the modules route purpose is unchanged.
  Verification remains closeout-owned.

- 2026-08-19T04:20+02:00 — No route impact: 260815-DAG-L10 updated the series worktree-group equality checks in `start_contract.py`/`terminal_validation.py` and narrowed reports-tree preservation in `cleanup.py`/`abandon.py` to legacy series contracts via `legacy_series_reports_is_child_enclosure`; the modules route purpose is unchanged.

- 2026-08-17T12:30+02:00 — No route impact: 260815-DAG-L5 added integration_publication.py to the modules route; the route purpose is unchanged.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: recorded queue claim/certify/revalidate/
  consume order, reversible terminal recovery, and governed lifecycle task writes. Verification
  remains closeout-owned.

- 2026-08-14T12:13:26+02:00 — R43 curator: recorded candidate typing and builder-level Dagger
  refusal repairs. Verification remains closeout-owned.

- 2026-08-14T11:48:55+02:00 — R42 curator: recorded the recovery-proof owner move and focused
  staged-scope test extraction. Verification remains closeout-owned.

- 2026-08-14T11:29+02:00 — R39 curator: reconciled the route with leaf reuse, master-only full
  acceptance, clean series closeout, and self-wrapper refusal. Verification remains closeout-owned.

- 2026-08-14T09:37+02:00 — Reopened L23 acceptance ownership: leaf closeout is the single targeted
  owner, leaf integration performs no rerun, clean series closeout performs no acceptance, and
  master integration retains the single full run. Verification remains closeout-owned.

- 2026-08-14T09:08+02:00 — Reopened L23 repair: recorded all-altitude candidate-tree revalidation
  after quality and the separate leaf-only route-review arm. Series closeout no longer needs a
  terminal leaf id and still refuses candidate drift before irreversible work. Verification
  remains closeout-owned.

- 2026-08-14T06:25+02:00 — L23 final route review: removed the stale local-executor description and
  documented Dagger-only exact-candidate quality, extracted staging/result owners, failure-atomic
  integration, lineage rechecks, bounded fresh attempts, and monotonic recovery. Verification
  remains closeout-owned.

- 2026-08-13T12:26+02:00 — L23 structural-rail repair: added the new
  `closeout_memory_quality.py` child and recorded its behavior-preserving ownership of quality-phase
  execution, bounded failure evidence, and two-phase result combination. Closeout retains commit,
  ledger, approval, lineage, and refresh ordering; verification provenance remains closeout-owned.

- 2026-08-13T09:27+02:00 — L23 curator: recorded git-common-dir repository identity for lineage
  edges, including sibling-worktree acceptance and fail-closed resolution. Verification provenance
  remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 integration-gate follow-up: closeout and integration now require
  complete transitive source lineage at preflight, recheck after their long quality work, and check
  again immediately before approval claim or merge. Integration pins exact code/memory source tips
  across the gate and retries without ref movement when they move. The route also records atomic
  clean-quality report promotion and the extracted strict-plan/closeout helper boundaries; final
  provenance remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: reconciled closeout/integration lineage rechecks, source-tip pinning across quality, extracted quality/result helpers, strict plan validation, and shared atomic report promotion. Verification metadata remains closeout-owned.


- 2026-08-12T22:45+02:00 — L23 curator follow-up: refined the baseline-relative route gate so sanctioned final-cell citation-coordinate shifts do not require fabricated history; the normalization is deliberately narrow and metadata-only, prose, anchor, path, table-shape, and other untraced changes still refuse. Verification remains closeout-owned.
- 2026-08-12T22:36+02:00 — No route impact: the final L23 pre-commit repair corrects `_route_overview_bucket`'s docstring to name its already-implemented typed evidence and citation-only behavior; the worktree module operating model documented above is unchanged. Verification remains closeout-owned.
- 2026-08-12T22:25+02:00 — L23 curator follow-up: route-overview closeout planning now includes memory overviews edited since the task's verified baseline even when their source drift predates the current leaf range; directly edited candidates remain subject to substantive body/history classification, so metadata-only and untraced refreshes refuse. Verification remains closeout-owned.
- 2026-08-12T20:20+02:00 — L23 curator: documented parent-first lineage admission and status recovery; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: documented explicit local/Dagger quality execution, immutable candidate capture, and lifecycle progress threading through closeout/integration; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24: made the master full-
  gate resource policy host-managed by default while retaining an explicit cap
  for constrained environments. Verification metadata remains pinned until
  closeout stamps L24.

- 2026-08-12T03:31+02:00 — 260731-EFA-L22 route repair: recorded the Git facade's transport-safe
  diagnostic boundary. Internal Git output remains surrogateescaped; only failure text crossing
  MCP is escaped, so no alternate runner or compatibility path was introduced.

- 2026-08-12T01:38+02:00 — No route impact: refreshed closeout staging citations after the test
  responsibility split; the worktree module route model is unchanged.

- 2026-08-11T22:28+02:00 — 260731-EFA-L19 final curator pass: recorded deterministic transcript
  decoding and non-Windows ephemeral scratch normalization while preserving the enclosure-owned
  reports-folder contract. Verification metadata remains pinned until governed closeout.

- 2026-08-10T22:09+02:00 — No route impact: L21 extracted the unchanged external-memory citation
  preflight from `closeout_result` into one module-local helper solely to restore the repository's
  hard 100-line function limit; closeout ordering, authority, and package responsibilities remain
  unchanged. Verification metadata stays pinned until closeout stamps the L21 code commit.

- 2026-08-10T12:46+02:00 — L9 closeout-order repair: recorded the configured-hook-before-wrapper
  and exact-index-after-wrapper contract; verification metadata stays pinned until closeout stamps
  the repair commit.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 route impact: recorded the provider-runtime move, the
  service-port surface, and the contract reader. Verification metadata pinned until closeout
  stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 route impact: recorded the altitude-routed gate plans
  (leaf targeted, master full+capped), the closeout targeted call sites, the per-leaf
  `memory_quality_check` carve-out, and the integration-step gate run. Verification metadata
  stays pinned until closeout stamps the 260731-EFA-L17 commit.
- 2026-08-05T22:55+02:00 — 260731-EFA-L16 curator: recorded the closeout memory-quality phase-order repair in `closeout.py` — before-phase skipped when its check list is empty, `_combined_memory_quality` tolerates the empty phase, and all memory-quality checks run in the single phase after the code commit and the metadata refresh to it. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 22 citation findings. Re-anchored the
  eight reference rows (facade `__all__`, `WorktreeSupportTests`, `LifecycleFinalizeTests`,
  `refresh_route_indexes_for_context`, closeout-gate suite, `WorktreePhase` wire vocabulary,
  replay-window tests, `claim_approval`/`CONSUMED_APPROVAL_GATE_KINDS`) with exact spans, and converted
  the three L3-history line-cites to cit form at current locations (`quality_environment` 168-188,
  `git_environment()` call 178, `_pr_for` 93-128). Scoped recheck clean.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No route impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T19:45+02:00 — 260731-EFA-L5 second curator pass (route governor for
  `worktrees/modules/closeout.py`). **Retracted "marks it `applied` on success"** from the
  slice-6b closeout bullet: `_mark_closeout_gate_applied` was deleted, `_enforce_closeout_gate` is
  renamed `_refuse_unsatisfied_closeout_gate` and can only deny, and the `applied` append now
  happens in `GateStore.claim_approval` under the gate log's lock. Added the L5 section with the
  route-level framing (durability of a record is not atomicity of a decision), the claim's call site
  one statement above the first commit and why neither earlier nor later is right, and the semantic
  change stated plainly: **an approval authorises one attempt, not one success**, with the
  fail-closed-versus-fail-open argument and the rejected two-phase `claimed` alternative. Recorded
  the **open decision** that `integrate.py` folds `all_current()` and evaluates
  `handover_gate_guard` but never consumes the `master-handover-approval` gate — never written on
  any commit, left open because the claim needs a cross-lifecycle `enclosure` key on a different log
  and because closeout's `integration_reopen` path means a legitimate re-integration would start
  requiring a fresh gate — and that the retention half is already ready via
  `SEAM_CONSUMED_GATE_KINDS`. Re-anchored every `closeout.py` line citation the leaf's +98 lines
  moved: `closeout_result` 727 → **743** (its `_gate_staged_code` call site is **786**),
  `_gate_staged_code` 625 → **684**, the reset/add pair 679-680 → **738-739**, the `amend_contract`
  call site 765 → **831** (`ContractCells` at **848**), and `closeout_order` 312 → **315**. The
  `integrate.py`, `start.py`, `cleanup.py`, `git.py` and `code_quality_gate.py` citations were
  re-checked and are unchanged — none of those files was touched by this leaf. Verification metadata
  untouched.
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
  route-visible facts:** the then-current `quality_environment` built from `git_environment()`
  instead of `dict(os.environ)`. L23 later removed that host-wrapper environment path entirely;
  acceptance now reconstructs the candidate inside Dagger. `_pr_for`'s `gh pr list` spawn still
  passes `env=git_environment()`
  (cit:([`_pr_for`], mcp/src/agents_remember/worktrees/modules/landing.py:93-150)), because `gh` resolves the repository through git and would otherwise list another
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
