# mcp/src/agents_remember/models/worktree.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/worktree.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-26T03:37+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`worktree.py` defines context-packet worktree summaries, public worktree tool response envelopes,
and the closed wire vocabulary for resumable sync control, phases, sides, and stable journal
projection.

## Code Commentary

cit:([`WorktreeSummary`], mcp/src/agents_remember/models/worktree.py:148-198) is the strict context-packet shape for the
`c-09-git-worktree-manager` lifecycle. Its vocabulary fields are typed, and
**since 260731-EFA-L4 every shared lifecycle vocabulary is imported from the
module that produces it; only `WorktreeState` remains local** (cit:([`WorktreeSummary`, `WorktreeState`], mcp/src/agents_remember/models/worktree.py:145-145; mcp/src/agents_remember/models/worktree.py:148-198)). The command response models
remain flexible because worktree service results can carry operation-specific
planning and closeout fields.

### Where each vocabulary is declared

| Field | Alias | Declared in |
| --- | --- | --- |
| `workflowKind` | `WorkflowKind` = `chat-task \| light-task` | `worktrees/worktree_contract.py` L50 |
| `memoryMode` | `MemoryMode` = `internal \| external \| disabled` | `worktree_contract.py` L51 |
| `humanReviewStatus` | `HumanReviewStatus` = `pending-review \| approved` | `worktree_contract.py` L52 |
| `closeoutStatus` | `CloseoutStatus`, imported **as `LifecycleStatus`** (the published wire name) = `not-started \| completed` | `worktree_contract.py` L53 |
| `integrationStatus` | `IntegrationStatus` = `not-started \| completed \| blocked` | `worktree_contract.py` L54 |
| `cleanup` | `CleanupStatus` = `pending \| completed \| abandoned \| reopened` | `worktree_contract.py` L55 |
| `phase` | `WorktreePhase` (8 members) | `worktrees/modules/guidance.py` L28-L37 |
| `nextOperation` | `NextOperation` (7 members) | `guidance.py` L38-L46 |
| `nextTool` | `NextTool` (5 members) | `guidance.py` L47-L53 |
| `state` | `WorktreeState` — the ONE alias still declared here (L33) | this file |

`WorktreeState` stays local on purpose: `application.worktree_status.worktree_status_packet`
constructs this model directly and is its only writer, so the projection there is
already the single writer the type checker can see.

**What the hand-written copies had cost.** They had drifted from their producers
in six places at once, all of them writable and none of them validated:
`chat-task` (the kind `worktree_start`'s own docstring advertises, present on 8
contracts), `reopened` (written by `worktrees/reopen.py`), `carryover-pending`,
`abandoned`, `request_carryover_decision` and `memory_carryover_apply`. The
result was that `WorktreeSummary` rejected **165 of the 213 `series-contract.md`
files on disk (77.5%)** with a `ValidationError` that nothing on the
`context_packet` tool path catches. Two set differences ran the other way and are
now gone as well: the old local `WorkflowKind` carried a bare `chat` and `light`
with **zero** occurrences across those 213 contracts and no production writer,
and the old `NextOperation`/`NextTool`/`WorktreePhase` carried
`request_commit_approval` / `worktree_closeout_preview` /
`commit-approval-pending`, which belong to the closeout preview's commit gate and
the blocked-start recovery payloads — those keep their own
`RecoveryOperation` / `RecoveryTool` aliases (cit:([`RecoveryOperation`, `RecoveryTool`], mcp/src/agents_remember/worktrees/modules/guidance.py:38-55)) precisely so
a wider `NextOperation` cannot put "requires developer approval" back into the set
the context packet's `nextOperation` claims to be.

`nextRequiredArgs` (cit:([`nextRequiredArgs`], mcp/src/agents_remember/models/worktree.py:181-181)) is **omitted rather than `[]`** when there is
nothing to supply. `next_guidance` writes the key only when the next call needs a
caller-supplied argument; the projection now reports what the producer said
instead of substituting a value for it. This is a stated wire change: measured
across the 213 contracts, 48 responses that previously carried
`"nextRequiredArgs": []` now omit the key, and it stays omitted. An absent
`nextRequiredArgs` means what the empty list meant — the next call needs nothing
beyond `nextArgs` — and there is no third state to confuse it with. The same rule
now covers `nextTool` and `nextArgs`, where the old substitution had put an
un-declarable `""` on the wire.

`unknownContractCells: list[str] | None` (cit:([`unknownContractCells`], mcp/src/agents_remember/models/worktree.py:186-186)) is new. It is present only
when the contract file carried a cell outside its declared vocabulary, formatted
`"<field>=<raw token> read as <fallback>"`. The `state` is still `active` and
every other field was computed from the substituted values — this field is the
notice that they were substituted. Refusing such a file instead would have made
the packet honest about a task that `worktree_closeout_apply`,
`worktree_integrate`, `worktree_cleanup`, `worktree_sync` and `worktree_abandon`
had all simultaneously stopped being able to touch; the file heals the next time
a lifecycle tool rewrites it.

`WorktreeCommandResponse.providers` carries the background provider setup
state (GitHub #53): `starting` plus a progressFile from `worktree_start`, then
running / stale (dead heartbeat) / ok / ready-with-failed-phases / failed via
the `worktree_status` projection. The strict `WorktreeSummary` (context
packets) deliberately does not project it — provider truth in packets comes
from the providers section.

`SyncResolutionAction`, `MemorySyncChoice`, `SyncSide`, `SyncPhase`, and `SyncOperationState` are
the single public vocabularies used by application, registration, journal models, and result
construction. `SyncOperationProjection` is the strict read-only enclosure-root journal view;
`WorktreeSummary` and `WorktreeStatusResponse` expose it even when the live contract cannot be
read. `SyncResolutionProjection` says which agent-owned side/worktree/conflict files need action.

`WorktreeSyncResponse` remains a flexible command envelope but now declares its stable recovery
surface: phase, structured resolution, agent ownership, contract-addressed next/cancel args,
evidence path, invalid input field, and manual-repair facts. It deliberately exposes no public
operation id; the canonical contract plus journal identity addresses the generation. The
`DirectCloseoutPreviewResponse` / `DirectCloseoutApplyResponse`
envelopes were removed with the direct-closeout tool surface (issue #62).

`WorktreeCommandResponse.lifecycleId` (slice 2c) declares the observable-lifecycle
enclosure anchor for wire discoverability. The worktree `status_payload` emits it
snake_case (`lifecycle_id`) like its sibling fields, so on the flexible envelope
the declared camelCase field documents the wire key without disturbing the
all-snake payload shape.

## Invariants And Boundaries

- `WorktreeSummary` is the stable context-facing shape.
- **No vocabulary is retyped here.** Every `Literal` on `WorktreeSummary` except
  `WorktreeState` is imported from its producer. Adding a member is a one-place
  edit at the producer; re-declaring one locally recreates the exact set
  difference that made the packet raise on 77.5% of the contracts on disk.
- **`WorktreeState` is the only local alias**, and only because
  `application.worktree_status` constructs this model directly and is its sole writer.
- Absent is the shape for `nextTool` / `nextArgs` / `nextRequiredArgs`. The
  projection reports what the producer wrote and never fills a hole the producer
  left; `""`, `{}` and `[]` are not substitutes for an omitted key.
- `unknownContractCells` is a report, not a state: it coexists with
  `state="active"` and with fully populated sibling fields.
- Worktree command payloads may remain flexible while the service API is still
  carrying operation-specific result blocks.
- Sync control/state literals are declared once here and consumed by journal/result/public seams;
  do not retype or widen them into arbitrary strings downstream.
- Stable sync projection is descriptive only. Models do not locate the journal, select a series,
  authorize Git mutation, or infer state from task/queue data.
- Closeout and integration quality result blocks are a deliberate strict exception: both read the
  shared `QualityGateResult`, preserving stable/published path meanings and rejecting extra fields.
- Do not reintroduce raw shell command strings into context-packet next hints.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync control, side, phase, operation-state, and strict projection shapes are declared together. | `SyncResolutionAction`; `MemorySyncChoice`; `SyncSide`; `SyncPhase`; `SyncOperationState`; `SyncOperationProjection`; `SyncResolutionProjection` | mcp/src/agents_remember/models/worktree.py:56-78; mcp/src/agents_remember/models/worktree.py:113-126; mcp/src/agents_remember/models/worktree.py:129-133 |
| Context and status responses carry the optional stable sync projection. | `WorktreeSummary`; `WorktreeStatusResponse` | mcp/src/agents_remember/models/worktree.py:148-198; mcp/src/agents_remember/models/worktree.py:239-242 |
| The sync response declares recovery guidance without exposing a public operation id. | `WorktreeSyncResponse` | mcp/src/agents_remember/models/worktree.py:256-267 |
| The sole writer of `WorktreeSummary`: `worktree_status_packet` returns the MODEL now, and `_summary_from_status_payload` projects field by field, reading `nextTool`/`nextArgs`/`nextRequiredArgs` with `.get` so an omitted key stays omitted. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:42-117 |
| The six persisted contract vocabularies (`WorkflowKind` … `CleanupStatus`) with their `VALID_*` frozensets, the `ContractCells` typed write record and `amend_contract`. | `VALID_WORKFLOW_KINDS`; `VALID_MEMORY_MODES`; `VALID_HUMAN_REVIEW_STATUSES`; `VALID_CLOSEOUT_STATUSES`; `VALID_INTEGRATION_STATUSES`; `VALID_CLEANUP_STATUSES`; `ContractCells`; `amend_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:72-77; mcp/src/agents_remember/worktrees/worktree_contract.py:182-198; mcp/src/agents_remember/worktrees/worktree_contract.py:199-226 |
| The guidance state machine imports and writes `WorktreePhase`, `NextOperation` and `NextTool` (declared in this model since L9), plus the separate `RecoveryOperation`/`RecoveryTool` that deliberately do NOT reach this model. | "from agents_remember.models.worktree import ("; `RecoveryOperation`; `RecoveryTool` | mcp/src/agents_remember/worktrees/modules/guidance.py:10-10; mcp/src/agents_remember/worktrees/modules/guidance.py:38-55 |
| The suite pinning every value a producer can emit against the field it crosses, including the omitted-`nextRequiredArgs` shape and the degrade-and-report contract cell. | "class AdvertisedVocabularyTests(unittest.TestCase):" | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:49-49 |
| Public worktree MCP application entry points delegate to the package worktree manager. | `worktree_status_tool` | mcp/src/agents_remember/application/worktree_tools.py:293-316 |

## Series-Contract Notes

Worktree response models expose `kind`, `leafId`, and `enclosurePath` in addition to `contractPath`, reflecting the distinction between root series contracts and leaf worktree contracts.

## L23 Source-Lineage Projection

The model route now owns strict edge, recovery, and aggregate shapes for
plane-resolved super-to-master and master-to-leaf ancestry. The projection
classifies code/external-memory edges without asking agents to carry commit or
runtime ids, and both status summaries and operation responses can expose the
same ordered, contract-addressed `worktree_sync` recovery evidence.

## L23 Lifecycle Model Package Review

Worktree response models now import `LifecycleOperationProjection` from
`models.lifecycles.operation`. The worktree vocabulary and strict source-lineage wire projection
remain owned here and are unchanged by the import move.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE-L1 Public Worktree Shapes

Closeout and direct-landing response models expose the normalized effective plan and structured refusal data. Optional raw request fields do not mean blank input is accepted: route-aware validation decides which legs are enabled and requires explicit stripped messages for those legs before any effect.

## 260821-CLIVE-L2 Current Contract

The current source seams include `SourceLineageEdge`, `SourceLineageRecovery`, `SourceLineageProjection`. The model change keeps public vocabulary closed and validates nonblank identity/evidence fields. Models describe state but do not locate journals, authorize mutation, or supply compatibility fallbacks.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `SourceLineageEdge`, `SourceLineageRecovery`, `SourceLineageProjection` at this ownership boundary. | `SourceLineageEdge`; `SourceLineageRecovery`; `SourceLineageProjection` | mcp/src/agents_remember/models/worktree.py:81-93; mcp/src/agents_remember/models/worktree.py:96-101; mcp/src/agents_remember/models/worktree.py:104-110 |

## 260821-DAGQC-L2 Typed Quality Result

`WorktreeCloseoutResponse.code_quality_gate` and `WorktreeIntegrateResponse.quality_gate` now share
the strict `QualityGateResult`. This closes the former open mapping, retains both the stable wrapper
`reportPath` and optional immutable `publishedResultPath`, and gives memory policy/cap their exact
public types. The surrounding command envelopes remain flexible for unrelated operation data.

## MCAR-L03 Closeout Pair Projection

Closeout preview and apply schemas now declare the exact pair plus bounded pair-refusal fields and
repair arguments. The fields are scoped to closeout responses rather than being generalized to
unrelated worktree operations.

## Update History

- 2026-08-29T21:46+02:00 — MCAR-L03: made exact-pair success and refusal fields discoverable on
  preview/apply response schemas. Verification remains closeout-owned.

- 2026-08-26T03:37+02:00 — Added single-owned resumable-sync vocabularies and strict stable-journal
  projections to context/status, plus the declared conflict/continue/cancel/manual-repair surface on
  `WorktreeSyncResponse`. Verification remains post-Dagger/closeout-owned.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: typed both lifecycle quality result blocks with the shared strict public model while preserving prior CLIVE curation. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 curator: recorded the operation-projection package move and confirmed
  the worktree wire contract is unchanged; final provenance remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented the strict transitive source-lineage projection and its contract-addressed recovery boundary; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: removed the internal contradiction by distinguishing imported shared lifecycle vocabularies from the intentionally local `WorktreeState` alias.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:20+02:00 — 260731-EFA-L4 curator: body rewritten; this file was the epicentre.
  The Code Commentary said `WorktreeSummary` "uses literal state fields" — it declared nine
  `Literal`s locally, all hand-copied from producers, and they had drifted in six writable places:
  `chat-task`, `reopened`, `carryover-pending`, `abandoned`, `request_carryover_decision` and
  `memory_carryover_apply`. That made this model reject 165 of the 213 `series-contract.md` files
  on disk (77.5%) with an uncaught `ValidationError` on the `context_packet` tool path. All nine
  are now imports (cit:([`WorktreeSummary`, `WorktreeState`], mcp/src/agents_remember/models/worktree.py:145-145; mcp/src/agents_remember/models/worktree.py:148-198)); only cit:([`WorktreeState`], mcp/src/agents_remember/models/worktree.py:146-146) is still declared here, because
  `worktrees.status` is its sole writer. Added the declaration table, which also records three
  published-vocabulary changes the card had no way to state: `WorkflowKind` is now `chat-task |
  light-task` (the bare `chat`/`light` had zero occurrences across the 213 contracts and no
  writer), `CleanupStatus` gained `reopened`, and `request_commit_approval` /
  `worktree_closeout_preview` / `commit-approval-pending` left `NextOperation`/`NextTool`/
  `WorktreePhase` for the separate `RecoveryOperation`/`RecoveryTool` aliases that never reach
  this model. Recorded `nextRequiredArgs` (cit:([`nextRequiredArgs`], mcp/src/agents_remember/models/worktree.py:181-181)) now being OMITTED rather than `[]` — a stated
  wire change on 48 of the 213 responses — and the new `unknownContractCells` field (cit:([`unknownContractCells`], mcp/src/agents_remember/models/worktree.py:186-186)),
  the degrade-and-report notice that keeps a contract with an off-vocabulary cell reachable by
  every lifecycle tool. Added four invariants. Citations: `WorktreeSummary` pinned to L36-L73,
  the import block to L9-L29, `WorktreeState` to L33; the `status.py` row re-pointed to
  `worktree_status_packet` L14-L49 / `_summary_from_status_payload` L52-L103 with the note that
  it returns the model now; new rows for `worktree_contract.py` (L50-L55, L59-L64, L171, L188),
  `guidance.py` (L28-L37, L38-L46, L47-L53, L61-L68) and
  `test_wire_vocabulary_exhaustiveness.py`. Verification metadata pinned until closeout stamps
  the L4 commit.
- 2026-08-01T09:20+02:00 — 260731-EFA-L4 curator: body rewritten; this file was the epicentre.
  The Code Commentary said `WorktreeSummary` "uses literal state fields" — it declared nine
  `Literal`s locally, all hand-copied from producers, and they had drifted in six writable places:
  `chat-task`, `reopened`, `carryover-pending`, `abandoned`, `request_carryover_decision` and
  `memory_carryover_apply`. That made this model reject 165 of the 213 `series-contract.md` files
  on disk (77.5%) with an uncaught `ValidationError` on the `context_packet` tool path. All nine
  are now imports (cit:([`WorktreeSummary`, `WorktreeState`], mcp/src/agents_remember/models/worktree.py:145-145; mcp/src/agents_remember/models/worktree.py:148-198)); only cit:([`WorktreeState`], mcp/src/agents_remember/models/worktree.py:146-146) is still declared here, because
  `worktrees.status` is its sole writer. Added the declaration table, which also records three
  published-vocabulary changes the card had no way to state: `WorkflowKind` is now `chat-task |
  light-task` (the bare `chat`/`light` had zero occurrences across the 213 contracts and no
  writer), `CleanupStatus` gained `reopened`, and `request_commit_approval` /
  `worktree_closeout_preview` / `commit-approval-pending` left `NextOperation`/`NextTool`/
  `WorktreePhase` for the separate `RecoveryOperation`/`RecoveryTool` aliases that never reach
  this model. Recorded `nextRequiredArgs` (cit:([`nextRequiredArgs`], mcp/src/agents_remember/models/worktree.py:181-181)) now being OMITTED rather than `[]` — a stated
  wire change on 48 of the 213 responses — and the new `unknownContractCells` field (cit:([`unknownContractCells`], mcp/src/agents_remember/models/worktree.py:186-186)),
  the degrade-and-report notice that keeps a contract with an off-vocabulary cell reachable by
  every lifecycle tool. Added four invariants. Citations: `WorktreeSummary` pinned to L36-L73,
  the import block to L9-L29, `WorktreeState` to L33; the `status.py` row re-pointed to
  `worktree_status_packet` L14-L49 / `_summary_from_status_payload` L52-L103 with the note that
  it returns the model now; new rows for `worktree_contract.py` (L50-L55, L59-L64, L171, L188),
  `guidance.py` (L28-L37, L38-L46, L47-L53, L61-L68) and
  `test_wire_vocabulary_exhaustiveness.py`. Verification metadata pinned until closeout stamps
  the L4 commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree response models now include `enclosurePath`, `leafId`, and `kind` alongside legacy `contractPath`, reflecting the root-series versus leaf-enclosure split. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: declared `WorktreeCommandResponse.lifecycleId` (the observable-lifecycle enclosure anchor, design §1.1) for wire discoverability; emitted snake `lifecycle_id` by `status_payload` like its siblings. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-11T06:47+02:00 — Removed `DirectCloseoutPreviewResponse` / `DirectCloseoutApplyResponse` (issue #62 worktree-only closeout).
- 2026-06-10T09:56+02:00 — Added `WorktreeSyncResponse` for the new worktree_sync tool (GitHub #54 sub-task D).
- 2026-06-10T07:30+02:00 — `WorktreeCommandResponse.providers` documented as the background provider setup state (GitHub #53): `starting` + progressFile from worktree_start, then running / stale / ok / ready-with-failed-phases / failed via the worktree_status projection. `WorktreeSummary` (context packets) deliberately does not project it.
- 2026-06-02T04:25+02:00: `WorkflowKind` dropped the retired `heavy`/`heavy-task` literals (now `chat`/`light`/`light-task`) after the heavy workflow was retired. `l-01-session-job-lifecycle` skill series, Sub-task B/S6, mcp 1.1.0.
- 2026-06-01T20:45+02:00 — `CleanupStatus` gained the `abandoned` literal and a `WorktreeAbandonResponse` model was added for the discard-without-integration tool.
- 2026-05-28T19:52+02:00: Created after worktree context summaries gained typed Pydantic literal fields.

## Governing Overview

[governing overview](overview.md)
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.


## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
