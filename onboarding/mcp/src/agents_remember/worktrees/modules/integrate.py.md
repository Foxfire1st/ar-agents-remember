# mcp/src/agents_remember/worktrees/modules/integrate.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/integrate.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a`
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns integration of completed worktree task branches back into their source
branches.

## Code Commentary

The module validates closeout state, checks fast-forward eligibility, reports
blocked non-fast-forward cases, optionally replays code and memory content for
reviewed parallel changes, merges integrated commits, verifies the memory
ledger mapping, and updates integration fields in the contract.

**Quality altitude ladder (260731-EFA-L17/L24/L23 reopen).** Integration owns acceptance only at
master altitude. A leaf integration returns `certified-at-leaf-closeout` and lands the exact
closeout commit without calling the quality decider, settings loader, or Dagger executor again.
`quality_gate_mode` refuses leaf use and returns `GATE_FULL` only for series/master contracts.
`_run_integration_quality_gate` therefore runs `run_strict_code_quality_gate` once for master
integration, with the optional settings-owned memory cap and `master-integration` invocation.
Dry-run reports the same ownership without executing it. A full-gate refusal returns
`blocked-quality-gate` before any source ref moves. `memory_quality_check` remains leaf-closeout
owned and is not repeated here.

**Two frozen parameter objects and one extracted phase (260731-EFA-L2):**

- **`IntegrationSources(current_code_source, current_memory_source, code_replay_required,
  memory_replay_required)`** — where each side's source branch stands when integration starts: its
  current head, and whether that head has already moved past the commit closeout landed (which is
  exactly what makes a fast-forward impossible and `--strategy replay` necessary). Head and verdict
  are read in the same breath per side and every consumer needs both.
  `IntegrationSources.replay_required` is a property (`code_replay_required or
  memory_replay_required`) — the ff-only block now reads `sources.replay_required` rather than
  re-OR-ing at the call site. `_integration_replay_requirements` returns it;
  `_blocked_non_ff_result` and `_dry_run_result` consume it.
- **`IntegratedCommits(code, memory_content, ledger)`** — the three commits one integration lands.
  Every step past the replay decision — the merge, the contract rewrite, the result payload —
  consumes all three or none, so `_merge_integrated_commits(contract, commits)` and
  `_integrated_result(contract, args, commits, *, handover_warning)` take the triple.
- **`_apply_integration(contract, args, sources, *, handover_warning)`** — the real (non-dry-run)
  path lifted out of `integrate_result`: land the code commit, then the memory commits, then merge
  both into their sources. `integrate_result` now reads as guard, replay decision, dry-run branch,
  delegate.

The merge of integrated commits is all-or-nothing: both the code and memory
fast-forwards are pre-validated as ancestors before either branch is mutated,
and if the memory-side merge or ledger-mapping check fails after the code
branch has advanced, both branches are reset hard to their pre-merge heads
before the failure re-raises, so integration never leaves a half-integrated
state.

**Lineage and source-tip gate.** `integrate_result` refuses stale or unavailable transitive
super→master→leaf code/external-memory ancestry during preflight. `_apply_integration` then
re-proves that lineage and the exact code/memory source tips after the potentially long quality
gate, before replaying memory, and once more immediately before `source-merge`. Movement returns
`source-moved-during-quality` with a retry preview and performs no source ref movement; the quality
result therefore cannot certify a candidate assembled from older source tips.

**Contract writes go through `ContractCells` (260731-EFA-L4).** This module moves two of the six
persisted vocabulary cells, and both now take the typed path:

- `blocked_integration_payload` — `amend_contract(contract, ContractCells(integration_status="blocked"))`.
- `_integrated_result` — `amend_contract(replace(contract, integration_strategy=…,
  integrated_code_commit=…, integrated_memory_content_commit=…, integrated_ledger_commit=…),
  ContractCells(integration_status="completed", cleanup="pending"))`.

The split inside `_integrated_result` is the pattern: the two vocabulary cells go through
`ContractCells` so pyright checks them, while the commit hashes and the strategy string — which have
no vocabulary to be checked against — stay on `replace`. That is the whole reason for the change:
typeshed declares `dataclasses.replace` as `**changes: Any`, so `replace(contract,
integration_status="bloqued")` was zero pyright errors even though the wire model rejects it. The
persisted contract is byte-identical either way. `replace` is still imported and still used for the
free-text fields.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wire model declares `IntegrationStatus` / `CleanupStatus`; worktree_contract imports them and exposes `ContractCells` / `amend_contract` as the typed amendment path. | "class ContractCells"; "def amend_contract"; "IntegrationStatus = Literal["; "CleanupStatus = Literal[" | mcp/src/agents_remember/models/worktree.py:18-19; mcp/src/agents_remember/worktrees/worktree_contract.py:182-182; mcp/src/agents_remember/worktrees/worktree_contract.py:199-199 |
| This module uses that typed path for both persisted vocabulary writes: blocked integration and completed integration with cleanup pending. | `blocked_integration_payload`; `_integrated_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:213-231; mcp/src/agents_remember/worktrees/modules/integrate.py:479-511 |
| Leaf integration reuses its closeout proof without calling a gate; series/master integration alone runs full Dagger, with an optional settings-owned cap and enclosure-owned reports. | `quality_gate_mode`, `_quality_gate_preview`, `_run_integration_quality_gate` | mcp/src/agents_remember/worktrees/modules/integrate.py:91-95; mcp/src/agents_remember/worktrees/modules/integrate.py:107-133; mcp/src/agents_remember/worktrees/modules/integrate.py:1116-1157 |
| The planned gate is carried in the dry-run payload and the integrated result without running on the dry-run path. | `IntegratePreview`, `_dry_run_result`, `_integrated_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:136-142; mcp/src/agents_remember/worktrees/modules/integrate.py:404-448; mcp/src/agents_remember/worktrees/modules/integrate.py:479-511 |
| The altitude proofs cover leaf no-rerun, series full, host-managed absence, explicit settings caps, refusal-before-merge, and dry-run preview. | `IntegrationQualityGateAltitudeTests` | mcp/tests/test_worktree_integrate_quality_gate.py:203-718 |
| Direct legacy integration tests now prove CLI callers cannot fast-forward or classify source movement without a plane-owned operation; the remaining non-fast-forward case proves no mutation. Journaled production-path suites own successful movement and recovery. | `test_direct_integrate_cannot_fast_forward_code_or_memory`; `test_direct_integrate_cannot_classify_parallel_non_overlapping_changes`; `test_direct_integrate_cannot_classify_parallel_conflicting_changes`; `test_integrate_refuses_non_fast_forward_code_without_mutating` | mcp/tests/test_worktree_support_tests_2.py:624-659; mcp/tests/test_worktree_support_tests_2.py:669-712; mcp/tests/test_worktree_support_tests_2.py:714-749; mcp/tests/test_worktree_support_tests_3.py:955-1007 |

As of cycle 6 the master-exit seam consumer is re-addressed by MASTER identity: the pure `handover_gate_guard` helper folds EVERY gate log (`GateStore.all_current()` — the raiser's lifecycle differs from the integrating contract's) and selects `master-handover-approval` gates whose `enclosure` matches the contract's `task_name` or `parent_task_name`; the latest matching gate must be policy-valid-approved under the CONFIGURED policy (`args.gate_policy`, now threaded from the application entry point) or the non-dry run returns handover-gate-blocked. Gateless — no gate addressed to this master — stays additive. Cycle 7 makes the exact-string address and the preview honest (AR4-1b/AR4-2): the pure sibling `unmatched_handover_gate_warning` reports, when NO gate addresses this contract but open `master-handover-approval` gates exist in the fold, a `handover_gate_warning` payload field (`unmatched_open_gates` + a verify-the-enclosure-spelling note) on the dry-run and integrated results, so a typo'd enclosure is loud instead of silently gateless; and the guard is now EVALUATED on the dry-run path too — enforced only on the real run — with the preview carrying `handover_gate` (`permitted`/`gateId`/`reason`) and a summary naming `handover-gate-blocked` when the real run would refuse, while the dry-run path persists no contract mutation.

## R39 Integration Altitude

Leaf integration returns certified-at-leaf-closeout and never invokes the gate runner.
Series/master integration owns the single full Dagger acceptance before merge, passes the
self-repository required-wrapper policy, and revalidates lineage/source tips after the long run.
A missing Agents Remember wrapper or failed full result blocks before merge.

## 260815-DAG-L3 Certified Integration Seam

Integration now claims the certified candidate, recomputes the full graph/readiness/evidence and
exact commit identity immediately before `_merge_integrated_commits`, and consumes the queue row
after the source move. Recovery of an already-completed integration consumes the same exact record
idempotently; no generic integration request may select or substitute a different leaf.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

The final reversible preparation checks the accepted code/external-memory source-tip snapshot before
the broader lineage diagnostic. A concurrent protected-ref move therefore returns the structured
`source-moved-during-quality` refusal expected by the retry protocol, before irreversible progress;
the lineage check still follows when the exact snapshot remains current.

Fresh journaled integrations now enter the normal claim-and-publication path. Recovery publication
is attempted only when the durable operation carries recovery commits that exactly match the worker
input. A completed contract without that durable tuple may still be previewed read-only, but apply
refuses before queue completion; immutable integration authority or self-asserted completed fields
alone are not recovery evidence.

## Update History

- 2026-08-16T08:12+02:00 — Dagger repair: reordered final source-state diagnostics so the exact accepted-tip race owns the structured pre-CAS refusal before persisted lineage diagnostics.

- 2026-08-16T07:05+02:00 — L4 review repair: completed apply/recovery now requires the operation's exact durable recovery tuple before descendant, ledger, or queue-completion publication.

- 2026-08-16T06:15+02:00 — Dagger repair: separated fresh integration from durable recovery admission so a newly queued graph candidate is claimed before queue-owned publication rather than being misclassified as torn recovery.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: recorded the certified claim, final irreversible
  revalidation, exact consume, and completed-integration recovery path; verification remains
  closeout-owned.

- 2026-08-14T11:25+02:00 — R39 curator: replaced leaf targeted reruns with certified-commit reuse
  and retained full acceptance solely at master integration. Verification remains closeout-owned.
- 2026-08-14T09:37+02:00 — Reopened L23 acceptance ownership: leaf integration now lands the exact
  closeout-certified commit without Dagger; master integration remains the only full accepting run.
  PR, push, tag, and publish paths do not become alternate integration acceptance owners.
- 2026-08-14T06:36+02:00 — L23 final candidate review: integration rechecks complete code and
  external-memory lineage before/after quality and before merge, pins source tips, runs targeted
  leaf or full master Dagger authority, and stays failure-atomic before refs move.
- 2026-08-13T08:40+02:00 — L23 integration-gate repair: documented fail-closed transitive-lineage admission, exact source-tip pinning across quality, and the two post-quality checks that prevent memory replay or source merge after in-flight movement. Verification metadata remains closeout-owned.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: made the
  integration-time memory cap optional; master integration now runs
  host-managed by default and forwards an explicit cap only when configured.
  Verification metadata remains pinned until closeout stamps L24.

- 2026-08-11T17:50+02:00 — 260731-EFA-L19 curator: recorded enclosure-targeted,
  atomically replaced test/quality transcripts for leaf and master integration gates. Verification
  metadata remains pinned until governed closeout.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the quality
  altitude ladder at the integration seam (kind-based mode routing, settings-owned
  cap, gate run before any merge, dry-run planned-gate payload, altitude
  invocation labels) and refreshed the persisted-write rows to the post-L17
  ranges. Verification metadata stays pinned until closeout stamps the
  260731-EFA-L17 commit.

- 2026-08-04T03:26:26+02:00 — 260731-EFA-L6 S18-SR3-B06 curator: generated and source-inspected the two persisted integration-write ranges (1 repair, 0 normalisations, 0 declines); the locked immediate recheck was clean with frozen zero source/tokenize/parse/build telemetry.
- 2026-08-04T03:03:23+02:00 — 260731-EFA-L6 S18-SR3-B06 worker: replaced the
  underbound function-header/assignment fragments with both complete integration-write owners,
  retaining the blocked and completed-plus-cleanup-pending meanings. The changed binding is a
  provisional `:1-1` input for the fresh Luna curator; no citation mechanics ran.
- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T01:24:49+02:00 — 260731-EFA-L6 S18-SR2-B06 worker: source-first separated the
  worktree-contract type/helper definitions from this module's two actual `amend_contract` call
  sites. Preserved every generated definition range and added one honest `:1-1` binding for the
  blocked and completed writes; no citation mechanics ran.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the scoped worktree-integration citation claims; final exact frozen-snapshot check is clean.
- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 2 citation entries (4 findings); no Tier-3 findings.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:50+02:00 — 260731-EFA-L4 curator: this leaf's diff here is not an import move — both
  of the module's contract writes changed shape. `blocked_integration_payload` went from
  `replace(contract, integration_status="blocked")` to
  `amend_contract(contract, ContractCells(integration_status="blocked"))`, and `_integrated_result`
  from one seven-keyword `replace` to `amend_contract(replace(contract, <four commit/strategy
  fields>), ContractCells(integration_status="completed", cleanup="pending"))`. Documented both, and
  the rule behind them: typeshed types `dataclasses.replace`'s `**changes` as `Any`, so an
  off-vocabulary literal at either of these two cells was zero pyright errors; the typed record puts
  them back in front of the checker. The persisted contract is byte-identical, so no payload,
  ordering or blocking claim in this card changed — I re-verified the all-or-nothing merge, the
  `IntegrationSources` / `IntegratedCommits` / `_apply_integration` L2 structure, and the
  master-handover gate section against the current file, and all still hold. Extended the
  `worktree_contract.py` reference row. Verification metadata pinned until closeout stamps the L4
  commit.
- 2026-07-31T21:00+02:00 — 260731-EFA-L3 curator: No content impact: the leaf's whole diff to
  `integrate.py` is one import line — `run_git` moved out of the `modules.git` import block to
  `agents_remember.kernel.git_command` — and this sidecar names no runner, subprocess style or
  timeout. I specifically re-checked the one claim the shared runner's new 300s bound could have
  broken, the all-or-nothing merge: `_merge_integrated_commits` still wraps the memory-side
  `merge --ff-only` and the ledger-mapping check in `except Exception`, and
  `subprocess.TimeoutExpired` is an `Exception`, so even a merge that outruns the bound still hits
  `run_git(..., ["reset", "--hard", code_head_before])` and the memory equivalent before re-raising
  — integration still cannot leave a half-integrated state. `IntegrationSources` (with
  `replay_required`), `IntegratedCommits`, `_apply_integration` and the `rebase` /
  `rebase --onto` replay call sites are untouched.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0913` armed with no
  exemptions): added the frozen `IntegrationSources` (with its `replay_required` property) and
  `IntegratedCommits`, re-signed `_integration_replay_requirements` / `_blocked_non_ff_result` /
  `_dry_run_result` / `_merge_integrated_commits` / `_integrated_result` onto them, and lifted the
  real integration path into `_apply_integration`. The all-or-nothing merge, the replay decision
  and every payload field are unchanged. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: added pure `unmatched_handover_gate_warning` (the enclosure spelling-check on gateless integrates, AR4-1b) and the dry-run now evaluates-but-does-not-enforce the seam guard, carrying `handover_gate` + the warning in the preview with no contract mutation (AR4-2). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: extracted `handover_gate_guard` (pure, testable) — cross-lifecycle fold + enclosure addressing replaces the inert `contract.lifecycle_id` lookup (AR3-1(b)). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): master-handover-approval enforcement consumer added at the integrate edge. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-05-31T12:30+02:00 — Documented all-or-nothing merge: pre-validate both fast-forwards and roll both branches back on memory-side failure (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
