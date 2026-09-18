# mcp/src/agents_remember/worktrees/modules/integrate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/integrate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Land an accepted code/memory pair into its named source branches, or checkpoint an unfinished atomic master's live pair without closing the master.

## Code Commentary

### Logic

Ordinary integration validates completed approved closeout, the exact work branches and accepted code/memory heads, and clean substantive content. Memory cleanliness excludes root `memory.md`. `IntegrationSources` captures source tips and fast-forward/replay facts once; source movement routes through the owning sync and a fresh closeout or the explicit resolution handoff. Transitive lineage and current source tips are re-proved at publication.

A checkpoint obtains `CheckpointLanding` from the live series refs instead of closeout cells an unfinished master cannot have. The same captured pair feeds preview and apply, and publication rechecks it. A completed master cannot use this weaker route. Source code advancing without a matching memory trailer is not a refusal: the actual memory ref is still the accepted memory output.

Handover gates are folded across gate logs by matching master/task identity. Preview evaluates the addressed gate without writing; apply enforces it. Unmatched open gates produce the existing addressing diagnostic. Normal integration does not run code quality, memory quality, certification, curator coherence, or independent review.

`_publish_integration_edge` reloads the exact contract, checks atomic/series or ordinary authority, re-proves the source snapshot, and delegates expected-old CAS. A CAS race reports the operation that actually ran, including the checkpoint tool on that route. The shared landing writer records `completed` plus pending cleanup for final integration, or `checkpointed` while preserving cleanup for a checkpoint. Neither landing reclaims the task; finalization owns that step.

### Conventions

`IntegratedCommits(code, memory_content)` is the sole delivered pair. Preview's memory ancestry proof and the protected boundary use the same real-Git predicate. The final/checkpoint difference is captured data and recorded lifecycle state, not a second ref transaction.

### Invariants And Boundaries

- No cache row, file, header, ordering rule, or ledger-only output authorizes or blocks integration.
- Accepted output identities must match the route's captured or recorded candidate.
- Each protected ref update keeps its expected old value; a memory CAS race must not erase concurrent work or falsely claim that both refs landed.
- A checkpoint remains a publication with an open master; it is separate from a stop-only pause.
- Landing and task finalization remain distinct operations.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| Ordinary admission requires the accepted code/memory work heads and substantive cleanliness. | `validate_integrate_contract`; `validate_integrate_memory_contract` | mcp/src/agents_remember/worktrees/modules/integrate.py:168-190 |
| Source snapshots and replay/lineage decisions retain current Git facts. | `_integration_source_state_block`; `_integration_lineage_block`; `_replay_requirements` | mcp/src/agents_remember/worktrees/modules/integrate.py:268-274; mcp/src/agents_remember/worktrees/modules/integrate.py:216-238; mcp/src/agents_remember/worktrees/modules/integrate.py:283-314 |
| Checkpoint capture, route output selection, and shared memory ancestry. | `CheckpointLanding`; `_require_memory_ancestry` | mcp/src/agents_remember/worktrees/modules/integrate.py:386-409; mcp/src/agents_remember/worktrees/modules/integrate.py:473-486 |
| Addressed handover gates and publication preserve the operation's real identity. | `handover_gate_guard`; `handover_gates` | mcp/src/agents_remember/worktrees/modules/integrate.py:83-109; mcp/src/agents_remember/worktrees/modules/integrate.py:131-131 |
| Final and checkpoint result publication differ without performing reclamation. | `_integrated_result`; `_checkpoint_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:890-927 |
| The shared writer records the two accepted output commits. | `LandedIntegration`; `record_landed_integration` | mcp/src/agents_remember/worktrees/modules/landing_record.py:36-66 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Retired ledger candidate/output fields and mapping projection gates; preserved two-output ancestry, exact ref CAS, handover/ownership checks, checkpoint capture, and finalization separation. Superseded obsolete active-body acceptance and hard-reset rollback claims. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 19 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T11:58+02:00 — 260913-LCA-L11 curator (uncommitted change set on `ar/260913-lca-l11-ar`,
  base `4214d7a1`): the route's admission lost its ledger-history dimension. `_landing_admission`
  now takes only `checkpoint` — the contract argument is gone, because with the developer's ruling
  that the rebuild outranks the tracked ledger file there is no series ledger prefix left to read
  (`atomic_series_ledger_prefix` was deleted with its only consumer). `_require_ledger_projection`
  likewise no longer receives `expected_series_prefix`/`checkpoint`. The preview/apply parity the
  L34 section records is unchanged and is now stronger by construction: the preview refuses exactly
  what the apply refuses because both run the same proof with nothing route-shaped to agree on.
  Repointed the three reference ranges this card carried into `integrate.py` after the module shifted
  by roughly 20 lines, and recorded the fact on the reference row and in the L34 parity bullet.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp
  advanced.
- 2026-09-13T18:02+02:00 — 260831-LOCR-L36 terminology: `checkpoint_landing_result` partially
  publishes an unfinished master; the card no longer says it "pauses" one or calls the route's subject
  a "paused master". The mechanism is unchanged (it lands the accumulated line, keeps the master open,
  records `checkpointed`, retires nothing), and pausing remains a separate matter that moves no ref.
  Wording only; no verification stamp advanced.
- 2026-09-13T14:32+02:00 — Curator citation repoint after the contract-scoped atomic-series activation re-keying shrank `models/worktree.py`: rebound the wire-vocabulary row to `mcp/src/agents_remember/models/worktree.py:38-39`, `_blocked_non_ff_result` to `integrate.py:320-338`, the checkpoint eligibility row (`CheckpointLanding`, `checkpoint_landing_eligibility`, `_route_commits`) to `integrate.py:390-424`, `425-461` and `527-539`, the `_route_commits` mention to `527-539`, and the `are reclaimed when the task edge is finalized.` quote to `integrate.py:643`. Claim wording unchanged; the cited declarations moved without changing what each claim states.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:45+00:00 — 260831-LOCR-L34 reachability repair: recorded the `CheckpointLanding`
  value and `checkpoint_landing_eligibility` as the one eligibility decision both surfaces read, the
  removal of `validate_integrate_contract` from the checkpoint path, and the three parity repairs —
  `_checkpoint_dry_run_result` (instance 2), the shared `_require_ledger_projection` before the
  dry-run branch for both routes (instances 4 and 5), and the required `operation` name on
  `_publish_integration_edge` fixing the hardcoded `nextTool` on `integration-ref-race` (instance 3).
  Superseded the L30 section's claim that the checkpoint "differs in exactly two places" and that it
  runs the contract validation. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "IntegrationStatus = Literal["; "CleanupStatus = Literal[" repointed to mcp/src/agents_remember/models/worktree.py:39-39; mcp/src/agents_remember/models/worktree.py:40-40. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: `_blocked_non_ff_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:278-295. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T19:50+02:00 — 260831-LOCR-L31 root integration to `lifecycle_finalize_task`:
  `_integrated_result` no longer reclaims. Replaced the "Automatic post-integration cleanup" section
  with the landed-and-stop boundary, and recorded **why the removal is the fix**: because cleanup ran
  inline and had already reached `completed` when the function returned, the one guard that routes a
  landed leaf to `lifecycle_finalize_task` (`next_step.py::_gate_after`, keyed on
  `contract.cleanup != "completed"`) could never fire — a real landing reported `nextOperation: "done"`
  while the leaf document stayed `planning` and its master row stayed `inProgress`, silently, on L29
  and L30. Recorded that the payload no longer carries a `"cleanup"` report key (the key is now the
  untouched contract cell), the two re-worded wire surfaces (`cleanup_reminder` and the integrated
  `summary`), and the corrected `_checkpoint_result` docstring clause that had become vacuous once no
  landing route reclaims. Re-pointed the shifted `_integrated_result` (373-408 → 375-410),
  `_checkpoint_result` (674-714 → 678-717) and `_dry_run_result` ranges. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: added `checkpoint_landing_result` and
  `_checkpoint_result`, the keyword-only `checkpoint` flag threaded through
  `_continue_integration`/`_handover_or_apply_integration`/`_apply_integration`/`_publish_integration_edge`,
  and the `publish_series_checkpoint_under_authority` selection; recorded that the checkpoint path
  records `checkpointed` and runs no cleanup, and corrected the `ContractCells` section, which still
  described `_integrated_result` amending the landing cells inline after the L29 extraction moved
  those writes into `landing_record.py` (the L30 change then widened that writer to take
  `LandedIntegration`). Re-derived the shifted reference ranges. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-11T23:05:00+00:00: The completed-integration row anchored the bare symbol `run_automatic_cleanup`, which now resolves three times across the two cited files (import and call in `integrate.py`, definition in `automatic_cleanup.py`), so the claim's provenance could not be compared. The anchor is now the exact call text `cleanup = run_automatic_cleanup(updated)` at `integrate.py` line 386, which occurs once in the cited sources; the claim's wording and both cited extents are unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "class ContractCells:" repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:180-180. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def amend_contract(" repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:197-197. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_integrated_result`; "def blocked_integration_payload(" repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:369-400; mcp/src/agents_remember/worktrees/integration/master_review_gate.py:14-14. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_blocked_non_ff_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:275-292. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-11T14:52+02:00 — Automatic post-integration cleanup at code commit `76ce662a`: `_integrated_result` now calls `run_automatic_cleanup` on the successful path after writing `integration_status=completed`, reloads the contract so the payload reflects the post-cleanup cell, nests the cleanup report as a top-level `cleanup` key, and reports a cleanup refusal without failing the landing; a refused or partial integration cleans up nothing. Repointed the stale `_integrated_result` ranges (420-450 → 372-407). Verification metadata remains pinned because this is a targeted single-claim repair; source documentation only, no acceptance claim.
- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: retired the evidence row citing the deleted `integration_quality.py` and recorded the module has no quality reference at all; corrected the L3 seam and CLIVE-L2 admission wording, which had this module binding a claimed closeout door and source journal into an integration intent — that module was deleted and no door claim is matched on this path; added the boundary-facts/publication-intent/claim-transfer removal section. Verification metadata remains pinned because only the cut-affected claims were reconciled; source documentation only, no acceptance claim.
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: retired the evidence row citing the deleted `test_worktree_integrate_quality_gate.py` altitude matrix. Verification metadata remains pinned because only the cut-affected reference was reconciled; source documentation only, no acceptance claim.

- 2026-09-10T15:06+02:00 — Integration guidance curation: the `blocked-non-ff` / `source branch moved` refusal now routes through `worktree_sync` plus a new targeted closeout instead of `--strategy replay`; recorded that `replay` remains supported and is the carryover vehicle. Re-derived the integrate.py anchors against the current working tree. Verification metadata remains closeout-owned.

- 2026-09-10T07:41:10+00:00: Generated citation repair: `_integrated_result`; "def blocked_integration_payload(" repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:418-448; mcp/src/agents_remember/worktrees/integration/master_review_gate.py:25-25. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 1 declined citation claim against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Separated wire state vocabulary from the typed amendment record and helper. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile_reference forwarding for the master full gate and removal of the requires_integrated_acceptance repo-name policy; refreshed integration_quality citations to the post-cutover ranges.
| The planned gate is carried in the typed dry-run payload without executing publication. | `IntegratePreview`; `_dry_run_result` | mcp/src/agents_remember/worktrees/modules/integration_publication.py:30-35; mcp/src/agents_remember/worktrees/modules/integrate.py:321-369 |
| The integrated result records the completed publication outcome and promises only the landing. | `_integrated_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:600-637 |
| The altitude-proof module this row cited was deleted with the removed closeout fixture chain (commit `9e1743c1`); the altitude matrix it described is no longer retained as test coverage. | — | — |
| Historical/removed: the direct-legacy-integration cases named here lived in `test_worktree_support_tests_2.py` / `_3.py`, which no longer exist. Journaled production-path suites own successful movement and recovery; this row records the earlier coverage rather than a current test. | N/A | N/A |


- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: replaced persistent blocker assumptions with live atomic protected-ref authority at the landing edge. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the queue-consume return (stale-by-evidence sibling
  facts) now lands on the fresh and completed-recovery integration payloads as
  `staleByEvidence`, each naming `worktree_sync` as recovery. Verification remains closeout-owned.

- 2026-08-17T12:09+02:00 — 260815-DAG-L5: the quality altitude ladder (`quality_gate_mode`, `quality_gate_preview`, `run_integration_quality_gate`) moved to `integration_quality.py` and `IntegratePreview`/`IntegrationPublication` to `modules/integration_publication.py`; re-pointed the two cited rows to the new owners. Verification remains closeout-owned.

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
