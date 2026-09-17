# mcp/src/agents_remember/worktrees/modules/guidance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/guidance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Build lifecycle status payloads and typed next-operation guidance from the worktree contract and observed Git state.

## Code Commentary

### Logic

`lifecycle_guidance` preserves three ordered groups: reclaimed/abandoned contracts first, attempted integration next, then pre-integration work. Dirty worktree diagnostics do not manufacture a commit-approval gate. A completed integration whose accepted outputs are carried home routes to `lifecycle_finalize_task`; a checkpointed series remains `worktree-started` with `continue_work`, because its master is still open.

`carryover_done` proves that the recorded code and memory outputs are ancestors of their named source tips. It uses integrated output cells when populated and otherwise the recorded closeout outputs. Missing repositories, output identities, source refs, or ancestry return false. Internal/disabled memory passes without an external-memory milestone. The timestamp is read from the accepted memory commit, not a cache row. Missing or malformed `memory.md` cannot change this completion proof.

`NextGuidance`, `LifecycleGuidance`, `WorktreeStatusFacts`, and `WorktreeStatusPayload` retain typed response boundaries. `WorktreePhase`, `NextOperation`, and `NextTool` are imported from `models.worktree`; only the recovery vocabulary is declared locally. The separate `recovery_guidance` builder serves blocked/gated flexible responses without widening lifecycle phases.

Status retains `ledger_path` as consumer metadata, exposes contract/enclosure identity, providers, source lineage, local base freshness, and optional landing observations. `unknown_contract_cells` remains an explicit degraded-read diagnostic. Interactive status calls the landing observation owner; projected status accepts an already-observed snapshot.

### Conventions

Next-move keys are omitted when they have no value. Guidance keys are merged after factual status keys. Local base freshness is separate from upstream fetch and remote landing observation.

### Invariants And Boundaries

- Lifecycle position, rather than raw dirtiness, selects the next operation.
- Code and memory completion require real Git reachability; cached mappings carry no completion authority.
- Finalization owns reclamation; a checkpoint does not close the master or make cleanup pending.
- Lifecycle wire vocabulary has one model owner; recovery guidance keeps its separate response vocabulary.
- Consumer ledger paths and raw status diagnostics remain available without becoming admission facts.

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
| Typed payloads and separate lifecycle/recovery builders. | `NextGuidance` | mcp/src/agents_remember/worktrees/modules/guidance.py:56-67 |
| Carryover completion is a real two-repository ancestry proof. | `carryover_done` | mcp/src/agents_remember/worktrees/modules/guidance.py:189-212 |
| Phase precedence, finalization guidance, and the still-working checkpoint branch. | `lifecycle_guidance` | mcp/src/agents_remember/worktrees/modules/guidance.py:215-225 |
| Freshness, consumer paths, identity fields, and interactive/projected observation. | `base_freshness` | mcp/src/agents_remember/worktrees/modules/guidance.py:378-428 |
| The canonical lifecycle wire vocabularies. | `WorktreePhase` | mcp/src/agents_remember/models/worktree.py:40-49 |
| External completion remains valid with damaged caches and rejects unlanded commits. | `test_external_completion_proves_landed_commits_without_reading_the_cache` | mcp/tests/test_post_integration_cleanup_guidance.py:84-119 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Replaced official-ledger carryover detection with accepted code/memory ancestry; corrected the vocabulary-owner description and retained phase precedence, checkpoint/finalization semantics, and projected-status distinctions. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 3 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T15:05+02:00 — No content impact: mechanical citation re-derivation after the
  260913-LCA-L8 change set added one import line to `worktrees/modules/cleanup.py`, shifting
  `carryover_done(contract)` from line 669 to 670. The anchor was re-read at
  `cleanup.py:670-670`, where that call still sits; the cited symbol and its meaning are unchanged.
- 2026-09-13T17:48+02:00 — 260831-LOCR-L36 pause wording: the `_post_integration_phase` comment above
  the `checkpointed` branch was reworded to stop reading the landing as a pause. Pausing a master is a
  separate matter that stops the master's work and returns control while publishing nothing, keeping
  its branch, worktrees and enclosure private; folding the pause into this landing is the hidden side
  effect the split exists to prevent. Recorded that rule as a third property of the checkpoint
  projection next to "no new `WorktreePhase` member" and "not a fallthrough". Comment only in the
  source: the branch, its phase, its next tool and its summary are unchanged. Verification metadata
  remains closeout-owned; no acceptance claim.
- 2026-09-13T12:29:52+00:00: Generated citation repair: `status_payload` repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:502-504. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `request_commit_approval` repointed to mcp/src/agents_remember/worktrees/modules/closeout.py:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: "if contract.integration_status == \"checkpointed\":" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:308-308. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: "if contract.integration_status == \"checkpointed\":" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:308-308. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T19:50+02:00 — 260831-LOCR-L31 root integration to `lifecycle_finalize_task`: the
  `cleanup-pending` branch no longer describes a failed automatic post-integration cleanup. It now
  projects the ordinary moment before the terminal edge — landed refs, carryover done, task edge not
  yet finalized — and routes `finalize` / `lifecycle_finalize_task` with
  `required_args=["contract_path"]` so an operator is handed the argument that names the edge.
  Recorded that `finalize` replaced `retry_cleanup` in `NextOperation` (removed rather than parked,
  because the branch that emitted it was its only writer) and that `lifecycle_finalize_task` joined
  `NextTool`; corrected this card's `NextTool` transcription, which read `memory_carryover_apply` for
  the member `guidance._post_integration_phase` actually emits, `memory_carryover_plan`. Added an
  invariant that a vocabulary member goes when its last writer goes, plus two reference rows.
  Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T05:05+02:00 — 260831-LOCR-L30 mirror-list completeness: the "no new `WorktreePhase`
  member" bullet's dashboard list was incomplete (three of six sites). Replaced it with the full
  five-file / six-site list — `EngineRoom.tsx:59-66` (`LIFECYCLE_PHASES`, `"integration-pending"` at
  `:63`), `BootTimeline.tsx:88` and `:110`, `useEngineTimeline.ts:41`,
  `buildEngineRoomModel.ts:16`, `geometry.ts:218` — and made the summary sentence above defer to it.
  Content change, not a range repoint; verification metadata remains closeout-owned.
- 2026-09-12T04:10+02:00 — 260831-LOCR-L30 follow-up: `_post_integration_phase` gained a
  `checkpointed` branch projecting the existing `worktree-started` phase with
  `continue_work`/`worktree_status` and a summary carrying the checkpoint truth. Recorded the two
  deliberate properties: no new `WorktreePhase` member (closed `Literal` mirrored by the dashboard at
  six sites across five files, listed in full in the bullet above) and that this is a real branch, not
  a fallthrough — before it, a checkpointed contract read as `integration-pending` pointing at
  `worktree_integrate`, which refuses while the series is open. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-12T01:26:36+00:00: Generated citation repair: `request_commit_approval` repointed to mcp/src/agents_remember/worktrees/modules/closeout.py:255-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b5cbe38ab438de766feb0fc3860228f5125b623ebbee641f90211d51326d68e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: "choose_memory_recovery", "choose_provider_setup_recovery", "choose_stale_base_recovery" repointed to mcp/src/agents_remember/worktrees/modules/start.py:274-274, mcp/src/agents_remember/worktrees/modules/start.py:328-328, mcp/src/agents_remember/worktrees/modules/start.py:468-468. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `status_payload` repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:472-474. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "carryover_done(contract)" repointed to mcp/src/agents_remember/worktrees/modules/cleanup.py:669-669. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "from agents_remember.models.worktree import (" repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:19-19. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `unknown_cells` repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:283-283. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T14:56+02:00 — Automatic post-integration cleanup vocabulary at code commit `76ce662a`: the `cleanup-pending` phase now says the automatic cleanup did not complete and routes to `retry_cleanup` (`worktree_cleanup`, contract args, no dry-run preview); `request_cleanup_decision` left `NextOperation` and the integration projection carries no `cleanup_question`. Verification metadata remains pinned because this is a targeted single-claim repair; source documentation only, no acceptance claim.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `request_commit_approval` repointed to mcp/src/agents_remember/worktrees/modules/closeout.py:245-245. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `status_payload` repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:468-470. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `request_commit_approval` repointed to mcp/src/agents_remember/worktrees/modules/closeout.py:354-354. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T17:36:08+02:00 — CCR-L24 inherited citation reconciliation: repointed `request_commit_approval` to the current L38 closeout source range while preserving the L38 guidance authorship. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `request_commit_approval` repointed to mcp/src/agents_remember/worktrees/modules/closeout.py:349-349. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:36+02:00 — L23 final candidate review: status guidance exposes task-addressed
  lifecycle-operation phase/report/failure recovery and current source-lineage relations without
  private operation or commit ids. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: recorded task-derived lineage status and sync guidance; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: corrected the worktree-status and carryover
  source owners, removed the false skill-tool claim, and split persisted vocabularies from unknown cells.

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 10 citation rows with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:30+02:00 — 260731-EFA-L4 curator: the card described the phase machine but not the
  vocabulary it now declares, and the three L2 helper signatures it quoted (`-> dict | None` /
  `-> dict`) had become false — they are `-> LifecycleGuidance | None` / `-> LifecycleGuidance`.
  Corrected those and added the section for what this leaf put above the state machine: the
  `WorktreePhase` / `NextOperation` / `NextTool` / `RecoveryOperation` / `RecoveryTool` `Literal`s
  (members transcribed from the source, not from the summary) and the `NextGuidance` /
  `LifecycleGuidance` / `WorktreeStatusFacts` / `WorktreeStatusPayload` `TypedDict`s, backed by the
  new `from typing import Any, Literal, NotRequired, TypedDict` and the six vocabulary imports from
  `worktree_contract`. Recorded the new `recovery_guidance` function and, checked against all five
  of its call sites, why it is separate rather than a widened `next_guidance`: identical keys on the
  wire, but its callers render as `FlexibleToolResponse` and never reach `WorktreeSummary`, whose
  `nextOperation` would otherwise have had to admit them. Also recorded `next_guidance`'s narrowed
  signature, the new `unknown_contract_cells` key in `_status_payload_with_landing`, the
  `{**facts, **guidance}` merge that replaced `payload.update(guidance)` (key order unchanged), and
  the `-> WorktreeStatusPayload` return on both `status_payload` and `projected_status_payload`.
  Added an Invariants section and six reference rows. Verification metadata pinned until closeout
  stamps the L4 commit.
- 2026-07-31T20:56+02:00 — 260731-EFA-L3 curator: the Code Commentary said `run_git` comes from
  `modules.git`; that import is gone (`from agents_remember.kernel.git_command import run_git`,
  `modules.git` now supplies only `worktree_dirty`) and `modules.git` no longer defines a runner at
  all, so the sentence was false. Corrected it and the slice-09 parenthetical, and recorded what the
  one call site — `carryover_done`'s `run_git(memory_repo_path, ["show", "-s", "--format=%cI",
  row.memory_commit])` — inherits from the shared runner: the `GIT_DIR`-family scrub and the 300s
  `GIT_LOCAL_TIMEOUT_SECONDS` default, uncaught because the `except LedgerError` does not cover it.
  Historical entries left as written. Verification metadata pinned until closeout stamps the L3
  commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0911`/`PLR0912` armed with no
  exemptions): `lifecycle_guidance` became a three-way `or` chain over `_reclaimed_phase`,
  `_post_integration_phase` and `_pre_integration_phase`. The first two return `None` for "not my
  group", preserving the old top-to-bottom precedence; the third always returns a phase. Every
  emitted phase, summary and `next_guidance` block is unchanged. Verification metadata pinned until
  closeout stamps the L2 commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: separated interactive status landing probes from projected status, which accepts only the latest immutable observation and its freshness truth.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: status and next-action payloads now include `kind`, `leaf_id`, `enclosure_path`, and `parent_contract_path`, while retaining `contract_path` for callers that have not yet renamed the field. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T07:25+02:00 — slice 09 (gate-signal adoption, S1 visibility fix): removed the dirty-tree → `commit-approval-pending` branch from `lifecycle_guidance` — a dirty worktree no longer fabricates a commit-approval gate and instead falls through to its honest lifecycle-position phase (closeout-completed → `integration-pending`, etc.). `commit-approval-pending` is owned by the closeout preview (`closeout.py`) and, once the gate plane is adopted, by a raised `closeout-approval` `GateNode` — never `git status`. Dropped the now-unused `contract_has_worktree_changes` import (`worktree_dirty`/`run_git` stay). Corrected the stale Code Commentary opening that still claimed the module reads worktree dirtiness into phases. Verification metadata pinned until closeout stamps the slice-09 code commit.
- 2026-06-21T06:40+02:00 — slice 05m (carryover-before-cleanup): added the public `carryover_done(contract) -> (done, carryoverDoneAt)` — it reads the OFFICIAL ledger (`memory_repo_path/memory.md` via `load_ledger`/`find_mapping`) to detect whether the landed code commit (`integrated_code_commit`, else `code_commit`) was carried home and returns the carry commit's `%cI`; external-only (internal/disabled → `(True, "")`). `lifecycle_guidance` now splits the `integration_status == "completed"` branch on it: not carried → phase `carryover-pending` (next: the existing `memory_carryover_apply`, args derived from the contract, `required_args=["intent_note"]`); carried → `cleanup-pending` with the new `carryoverDoneAt` in the guidance dict. New imports: `LedgerError`/`find_mapping`/`load_ledger` from `kernel.memory_ledger` and `run_git` from `modules.git`. Verification metadata pinned until closeout stamps the 05m code commit.
- 2026-06-21T04:10+02:00 — slice 05l P1 (backend teardown visibility, Gap A): `lifecycle_guidance` gained a `cleanup == "abandoned"` branch (right after the `cleanup == "completed"` branch) returning a dedicated `abandoned` phase (`nextOperation: "done"`). Previously an abandoned worktree fell through to the `worktree-started` default, so the dashboard rendered a deleted worktree as fully active; the explicit phase lets the observer project it for the teardown render (05k). Verification metadata pinned until closeout stamps the 05l-P1 code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1: `status_payload` emits a best-effort `landing` block from `landing.landing_refs(contract)` (the successful-landing arc's remote/PR refs, gated to closeout-completed onward; git ls-remote + best-effort gh, honest factState, stdin=DEVNULL). Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: `status_payload` emits `lifecycle_id` (the contract's observable-lifecycle enclosure anchor) so `worktree_attach` can resume it. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-10T09:56+02:00 — Issue #54 sub-task D: added `base_freshness` (fetch-free recorded-base vs local source tip counts with a `worktree_sync` `syncHint`) and wired it into `status_payload` as `freshness`.
- 2026-06-10T07:30+02:00 — `status_payload` includes a `providers` block from `provider_async.provider_setup_status(contract)` when present: the worktree_status poll surface for background provider setup (running with currentPhase/heartbeat/seedFallback, stale on dead heartbeat, terminal ok/ready-with-failed-phases/failed with retryArgs) (GitHub #53).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
