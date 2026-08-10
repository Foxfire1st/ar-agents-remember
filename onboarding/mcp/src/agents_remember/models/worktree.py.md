# mcp/src/agents_remember/models/worktree.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/worktree.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-10T05:45+02:00     |
| lastVerifiedCommitHash | `b537abe20cf2498ef38e86e29ca586b5eec38466` |
| lastVerifiedCommitDate | 2026-08-10T08:37:35+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`worktree.py` defines context-packet worktree summaries and public worktree
tool response envelopes.

## Code Commentary

cit:([`WorktreeSummary`], mcp/src/agents_remember/models/worktree.py:38-76) is the strict context-packet shape for the
`c-09-git-worktree-manager` lifecycle. Its vocabulary fields are typed, and
**since 260731-EFA-L4 every shared lifecycle vocabulary is imported from the
module that produces it; only `WorktreeState` remains local** (cit:([`WorktreeSummary`, `WorktreeState`], mcp/src/agents_remember/models/worktree.py:35-35; mcp/src/agents_remember/models/worktree.py:38-76)). The command response models
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
`RecoveryOperation` / `RecoveryTool` aliases (cit:([`RecoveryOperation`, `RecoveryTool`], mcp/src/agents_remember/worktrees/modules/guidance.py:62-69)) precisely so
a wider `NextOperation` cannot put "requires developer approval" back into the set
the context packet's `nextOperation` claims to be.

`nextRequiredArgs` (cit:([`nextRequiredArgs`], mcp/src/agents_remember/models/worktree.py:70-70)) is **omitted rather than `[]`** when there is
nothing to supply. `next_guidance` writes the key only when the next call needs a
caller-supplied argument; the projection now reports what the producer said
instead of substituting a value for it. This is a stated wire change: measured
across the 213 contracts, 48 responses that previously carried
`"nextRequiredArgs": []` now omit the key, and it stays omitted. An absent
`nextRequiredArgs` means what the empty list meant — the next call needs nothing
beyond `nextArgs` — and there is no third state to confuse it with. The same rule
now covers `nextTool` and `nextArgs`, where the old substitution had put an
un-declarable `""` on the wire.

`unknownContractCells: list[str] | None` (cit:([`unknownContractCells`], mcp/src/agents_remember/models/worktree.py:75-75)) is new. It is present only
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

`WorktreeSyncResponse` (GitHub #54 sub-task D) is the flexible envelope for the
new `worktree_sync` tool, following the same `WorktreeCommandResponse` shape as
its siblings. The `DirectCloseoutPreviewResponse` / `DirectCloseoutApplyResponse`
envelopes were removed with the direct-closeout tool surface (issue #62).

ARG-L1 makes the stable completion cleanup products discoverable on
`WorktreeIntegrateResponse` despite the worktree envelope remaining flexible:
`autoClosedSeats`, `autoCloseDeferredSeats`, `autoCloseFailedSeats`, and `autoLandedSeats` are
declared default-empty lists. This prevents the close-vs-land wire contract from hiding as an
incidental extra field.

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
- Do not reintroduce raw shell command strings into context-packet next hints.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The sole writer of `WorktreeSummary`: `worktree_status_packet` returns the MODEL now, and `_summary_from_status_payload` projects field by field, reading `nextTool`/`nextArgs`/`nextRequiredArgs` with `.get` so an omitted key stays omitted. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:21-56 |
| The six persisted contract vocabularies (`WorkflowKind` … `CleanupStatus`) with their `VALID_*` frozensets, the `ContractCells` typed write record and `amend_contract`. | `VALID_WORKFLOW_KINDS`; `VALID_MEMORY_MODES`; `VALID_HUMAN_REVIEW_STATUSES`; `VALID_CLOSEOUT_STATUSES`; `VALID_INTEGRATION_STATUSES`; `VALID_CLEANUP_STATUSES`; `ContractCells`; `amend_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:72-77; mcp/src/agents_remember/worktrees/worktree_contract.py:183-198; mcp/src/agents_remember/worktrees/worktree_contract.py:201-229 |
| The guidance state machine that declares and writes `WorktreePhase`, `NextOperation` and `NextTool`, plus the separate `RecoveryOperation`/`RecoveryTool` that deliberately do NOT reach this model. | `WorktreePhase`; `NextOperation`; `NextTool`; `RecoveryOperation`; `RecoveryTool` | mcp/src/agents_remember/worktrees/modules/guidance.py:28-53; mcp/src/agents_remember/worktrees/modules/guidance.py:62-69 |
| The suite pinning every value a producer can emit against the field it crosses, including the omitted-`nextRequiredArgs` shape and the degrade-and-report contract cell. | "class AdvertisedVocabularyTests(unittest.TestCase):" | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:45-45 |
| Public worktree MCP application entry points delegate to the package worktree manager. | `worktree_status_tool` | mcp/src/agents_remember/application/worktree_tools.py:233-235 |

## Series-Contract Notes

Worktree response models expose `kind`, `leafId`, and `enclosurePath` in addition to `contractPath`, reflecting the distinction between root series contracts and leaf worktree contracts.

## Update History

- 2026-08-10T05:45+02:00 — 260805-ARG-L1: declared all four completion-seat result lists on
  `WorktreeIntegrateResponse`; the wider worktree response remains intentionally flexible.
  Verification remains pinned until closeout stamps ARG-L1.

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
  are now imports (cit:([`WorktreeSummary`, `WorktreeState`], mcp/src/agents_remember/models/worktree.py:35-35; mcp/src/agents_remember/models/worktree.py:38-76)); only cit:([`WorktreeState`], mcp/src/agents_remember/models/worktree.py:35-35) is still declared here, because
  `worktrees.status` is its sole writer. Added the declaration table, which also records three
  published-vocabulary changes the card had no way to state: `WorkflowKind` is now `chat-task |
  light-task` (the bare `chat`/`light` had zero occurrences across the 213 contracts and no
  writer), `CleanupStatus` gained `reopened`, and `request_commit_approval` /
  `worktree_closeout_preview` / `commit-approval-pending` left `NextOperation`/`NextTool`/
  `WorktreePhase` for the separate `RecoveryOperation`/`RecoveryTool` aliases that never reach
  this model. Recorded `nextRequiredArgs` (cit:([`nextRequiredArgs`], mcp/src/agents_remember/models/worktree.py:70-70)) now being OMITTED rather than `[]` — a stated
  wire change on 48 of the 213 responses — and the new `unknownContractCells` field (cit:([`unknownContractCells`], mcp/src/agents_remember/models/worktree.py:75-75)),
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
