# mcp/src/agents_remember/models/worktree.py
## Governing Overview

[Owning overview](overview.md)
## Purpose

Defines the strict public worktree response and sync projection vocabulary.
## Code Commentary

SourceLineageProjection reports the applicable code/memory edges and recovery facts. SyncOperationProjection carries the journal's actual state, phase, conflicts and next arguments. SyncResolutionProjection describes the side, worktree and files requiring content resolution, with wipRestore distinguishing parked-WIP recovery. Resolution input admits only its declared action. The old SyncKnowledgeConflict and canonical dataset reconciliation fields were retired; these DTOs do not decide conflict content or authorize staging.
### Logic
`WorktreeCheckpointLandingResponse` carries `integrationStrategy`, `integratedCodeCommit`,
and `integratedMemoryContentCommit`. It has no integrated-ledger field; the response names the
two real branch outputs of the checkpoint. Cache refresh does not add a commit identity to this
wire contract, and stop-only pause remains a separate response.
`WorktreeSummary` (declared at line 268) is the strict context-packet shape for the
`c-09-git-worktree-manager` lifecycle. Its vocabulary fields are typed, and
the shared wire vocabularies are declared in this module (see the table below), except `MemoryMode`, which is imported from the kernel. `WorktreeState` itself is declared at
line 265. The command response models
remain flexible because worktree service results can carry operation-specific
planning and closeout fields.
### Where each vocabulary is declared

| Field | Alias | Declared in |
| --- | --- | --- |
| `workflowKind` | `WorkflowKind` = `chat-task \| light-task` | this file L35 |
| `memoryMode` | `MemoryMode` = `internal \| external \| disabled` | imported from the kernel (L9) and re-exported here |
| `humanReviewStatus` | `HumanReviewStatus` = `pending-review \| approved` | this file L36 |
| `closeoutStatus` | `CloseoutStatus`, imported **as `LifecycleStatus`** (the published wire name) = `not-started \| completed` | this file L37-L38 |
| `integrationStatus` | `IntegrationStatus` = `not-started \| completed \| blocked \| checkpointed` | this file L44 |
| `cleanup` | `CleanupStatus` = `pending \| completed \| abandoned \| reopened` | this file L45 |
| `phase` | `WorktreePhase` (8 members) | this file L46 |
| `nextOperation` | `NextOperation` (7 members) | this file L56 |
| `nextTool` | `NextTool` (8 members) | this file L65 |
| `state` | `WorktreeState` — the ONE alias still declared here | this file L307 |

Ranges in this table were re-derived at 260831-LOCR-L36: the contract-scoped activation re-key
removed one name from the `models.structural.atomic_series_activation` import above the vocabulary
block and deleted the admission-blocking model below it, so every alias after the import shifted
back up by one and `WorktreeState` moved from L234 to L229.
The next-move triple is **not** a vocabulary alias and does not appear above. It is declared on the
command envelope — `nextAction: str | None`, `nextTool: str | None`, `nextArgs: dict[str, Any] | None`
at L400-L406 — with the membership validator at L431-L442. `WorktreeSyncResponse` (`nextTool` at
L499) and `WorktreeOperationControlResponse` (`nextTool` at L573-L575) narrow it further.
`WorktreeState` stays local on purpose: `application.worktree_status.worktree_status_packet`
constructs this model directly and is its only writer, so the projection there is
already the single writer the type checker can see.
**Cleanup vocabulary, and the one member deliberately kept (260831-LOCR-L31).**
`request_cleanup_decision` left `NextOperation` one leaf earlier and `retry_cleanup` took its place;
this leaf removed `retry_cleanup` again and `finalize` took *its* place, so the count is still seven.
`retry_cleanup` had exactly one writer — the `cleanup-pending` phase of
`guidance._post_integration_phase` — and that branch now routes `finalize` /
`lifecycle_finalize_task`, so the member was removed rather than left declared beside its own
replacement. `NextTool` gained `lifecycle_finalize_task` (six members at L31), because a `NextOperation`
the wire cannot pair with a tool is half a move; **260831-LOCR-L34 added the seventh,
`worktree_checkpoint_landing`, without widening `NextOperation`** — see
[the L34 section below](#260831-locr-l34-the-checkpoint-tool-in-nexttool).
**`NextTool."worktree_cleanup"` is kept, and it is not orphaned.** `guidance.py` no longer emits it
anywhere; its remaining producer is
`application/worktree_status.py::_project_terminal_contract_status`
,
which sets `"nextTool": archive.cleanupOperation` for a terminal contract, and `cleanupOperation` is
`TerminalCleanupOperation = Literal["worktree_cleanup", "worktree_abandon"]`
. Do not
"tidy" the member away: it is one of the two values that route actually emits.
**The terminal-status next move is now declared AND enforced here (260831-LOCR-L32).** This section
replaces three earlier accounts of the same seam. The first two were wrong in opposite directions
(the write does **not** land on `WorktreeSummary` and does **not** violate one of its declared
fields); the third — "verified mechanism, correct behaviour, missing types, fix recorded but not
implemented" — was right about the mechanism and is now superseded by the fix itself.
*The defect it closed.* `worktree_status` is validated at exactly one place,
`TOOL_RESPONSE_MODELS[tool_name].model_validate(payload)`
,
and that registry maps `"worktree_status"` to `WorktreeStatusResponse`
. Resolving down through
`WorktreeCommandResponse` → `FlexibleToolResponse` → `FlexibleResponseEnvelope` →
`FlexibleResponseModel`, whose `model_config` is
`ConfigDict(extra="allow")`
,
the envelope declared **none** of `nextAction` / `nextTool` / `nextArgs`. So the projector's triple
passed through **verbatim and unchecked**: `worktree_abandon` reached the wire as a `nextTool` without
ever having been a `NextTool` member, `"nextAction" in WorktreeStatusResponse.model_fields` was
`False`, and `model_validate({"ok": True, "nextTool": "not_a_tool"})` succeeded. The emitted guidance
was *correct* — the args matched the real tool signatures — so only the typing and the enforcement
were missing.
*The fix, declared on `WorktreeCommandResponse` at `models/worktree.py:326-328`.*

```python
nextAction: str | None = None
nextTool: str | None = None
nextArgs: dict[str, Any] | None = None
```

`WorktreeStatusResponse` inherits all three, so the keys the projector writes are no longer extras.
Out-of-roster values are refused by `_require_registered_public_next_tool`
, a
, a
`@field_validator("nextTool")` raising `nextTool must name a registered public tool; <value> is not in
PUBLIC_TOOLS`. `None` still passes, and `WorktreeSyncResponse` / `WorktreeOperationControlResponse`
narrow `nextTool` further exactly as they did before.
*`PUBLIC_TOOLS` had to move for this to be expressible.* The validator needs the roster, and
`models/worktree.py` may not import `mcp` (`layers.toml` ranks models = 2, mcp = 22). The tuple's one
definition is now the zero-import leaf
`agents_remember/models/tools/public_roster.py`
, imported here at
module scope
(`from agents_remember.models.tools.public_roster import PUBLIC_TOOLS`); `mcp/tools/base.py`
re-exports the same object. Do not move the roster back, and do not add a function-local import of it.
**The rule is PER SURFACE, deliberately — do not flatten it.** The producer survey behind the
invariant traced every `nextTool` writer in `mcp/src` and found a union of **20** values. **Only
`session_retire` is outside `PUBLIC_TOOLS`.** It is a *registered* but deliberately *non-public* tool
(`models/tools/tool_registry.py:133`, `:157`), emitted by
`application/task_docs/task_unstarted_evidence.py:575` via `_record_recovery_route`, and it reaches the
wire only through the **`task_doc`** surface (`task_doc_discard.py:353`, and inside `discardEvidence`).
`TaskDocResponse` is **not** a `WorktreeCommandResponse`, so this invariant never sees it. Two
consequences:

- The worktree surface's next move must name a registered **public** tool, because those values are
 advertised guidance an agent acts on and the roster is the already-enforced authority for what the
 agent can actually call.
- The `task_doc` surface may name a non-public tool. **Widening `PUBLIC_TOOLS` to cover
 `session_retire` would be the wrong fix**, and so would special-casing it in the validator.

Also not outliers, for the avoidance of doubt: `normalize_closeout_input` and `worktree closeout` are
`CloseoutCorrectedCall.tool` — a *different field*, not `nextTool`.
**Three deliberate non-changes, reviewed so nobody "fixes" them later.**

- **`NextTool` did not gain `worktree_abandon`.** That alias is the guidance machine's
 produced == declared vocabulary (`worktrees/modules/guidance.py`); the machine cannot emit abandon,
 so adding the member would break produced == declared rather than repair anything. The terminal
 cleanup operation reaches the wire through `WorktreeCommandResponse.nextTool` (now `str | None`),
 not through `NextTool`.
- **The flexible envelope was not narrowed to a literal.** This family legitimately emits many tools,
 and narrowing would manufacture new validation errors for every existing producer. Membership in
 `PUBLIC_TOOLS` is the enforcement; a literal is not.
- **`WorktreeSummary.nextAction` was not widened.** Its single producer hard-codes
 `developer-decision`
 , and
 , and
 `WorktreeSummary` is never on this path — it is constructed only inside `worktree_status_packet`'s
 own helpers for the `context_packet` surface (`application/worktree_status.py:79`, `:120`, `:199`,
 `:242`). Its single-value literal is honest where it lives.
**The branch is reachable, and it is now covered.** The terminal archive and receipt are published
(locator → `terminal-archived`) *before* the surviving contract is amended: `cleanup.py` completes its
guard around `amend_contract(contract, ContractCells(cleanup="completed"))`
,
and `abandon.py` does the same around `cleanup="abandoned"`
.
Both writes are wrapped in `guard.complete(..., rollback_publish=...)`, so a **failed publication
deliberately restores the archived contract while the locator stays `terminal-archived`** — exactly
the state the projector serves, `"terminal-archive-ready"`
.
`mcp/tests/test_worktree_status_terminal_next_tool.py` (260831-LOCR-L32) reaches that state through
the real production calls for both `worktree_cleanup` and `worktree_abandon` and pins the declarations,
the emitted args (bound against the real builder signature with
`inspect.signature(...).bind(...)`), and the validator in both directions. **That branch had zero
coverage before this leaf.**
**The invariant that would have caught this has no executor left.**
`mcp/tests/test_wire_vocabulary_exhaustiveness.py` retains only its docstring, helpers and "test moved
verbatim in L7 split" breadcrumbs — it contains **zero** `def test_` functions. Its docstring still
describes `GuidanceWalkTests`, `ProducedLiteralTests` and `AdvertisedVocabularyTests` in the present
tense, but the bodies are gone, so the produced == declared invariant for `NextTool` is currently
**unenforced**
.
That is why the fix above must be argued from doctrine rather than from a failing test, and it is the
gap to close first.
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
`RecoveryOperation` / `RecoveryTool` aliases () precisely so
a wider `NextOperation` cannot put "requires developer approval" back into the set
the context packet's `nextOperation` claims to be.
`nextRequiredArgs` () is **omitted rather than `[]`** when there is
`nextRequiredArgs` () is **omitted rather than `[]`** when there is
nothing to supply. `next_guidance` writes the key only when the next call needs a
caller-supplied argument; the projection now reports what the producer said
instead of substituting a value for it. This is a stated wire change: measured
across the 213 contracts, 48 responses that previously carried
`"nextRequiredArgs": []` now omit the key, and it stays omitted. An absent
`nextRequiredArgs` means what the empty list meant — the next call needs nothing
beyond `nextArgs` — and there is no third state to confuse it with. The same rule
now covers `nextTool` and `nextArgs`, where the old substitution had put an
un-declarable `""` on the wire.
`unknownContractCells: list[str] | None` () is new. It is present only
`unknownContractCells: list[str] | None` () is new. It is present only
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
read. `SyncResolutionProjection` says which agent-owned side/worktree/conflict files need action, and its `wipRestore` flag distinguishes a resolution that is re-applying the work-in-progress the sync parked from a plain merge conflict. `sync_transaction_results` emitted that flag from the start but the field was not declared here, so `StrictResponseModel`'s `extra="forbid"` refused the projection and a sync that needed agent action failed with a serialization error instead of the guidance it owed; the field is an optional bool so the two producers that omit it remain valid.
CCR-R25 adds the typed public admission vocabulary; the contract-scoped activation re-key makes it
per-contract. `AtomicSeriesActivationFact` carries the read-only per-contract activation observation
used by series status: the activation address, `contractFingerprint` (SHA-256 of the canonical
resolved contract path), the observed state, and the record or error evidence. `AtomicSeriesAdmission`
is the bounded wait/corrective-action explanation with the requested identity, the addressed
contract's own `contractFingerprint`, a nested `AtomicSeriesAdmissionActivation` snapshot
(`path`, `observedState`, `recordPresent`, `contractFingerprint`, optional revision/selection/error
evidence), the retry precondition, and an optional contract-bound `worktree_status` action. The model
carries no `classification`, `sourcePair*` or `blocking` field, and the `AtomicSeriesAdmissionBlocking`
model was deleted with them: selection is per contract, so a foreign live master is never named as a
blocker or as another contract's retry precondition. `WorktreeSummary` and `WorktreeCommandResponse`
expose these fields as optional additions; the model layer validates the shape but does not select,
repair, or authorize activation.
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
### Conventions

Wire envelopes mirror their public operation and import shared vocabularies from their owning model. The checkpoint response records published output identities, while pause records a stop.
### Invariants And Boundaries

- `WorktreeSummary` is the stable context-facing shape and may carry read-only atomic-series activation evidence.
- **Activation evidence is contract-scoped.** `AtomicSeriesActivationFact` and `AtomicSeriesAdmission`
 carry the addressed contract's `contractFingerprint`; the nested `AtomicSeriesAdmissionActivation`
 snapshot and the retry precondition describe only that contract's own state, so a foreign live
 master is never projected as a blocker. The deleted `AtomicSeriesAdmissionBlocking` model and the
 `classification` / `sourcePair*` / `blocking` fields must not be reintroduced.
- `AtomicSeriesAdmission` describes an observed admission boundary; it is not a scheduler, retry
 executor, or authority to mutate the selector.
- **No vocabulary is retyped here.** Every `Literal` on the worktree models is declared in this module
(see the table above). Adding a member is a one-place edit here; re-declaring one in a second module
recreates the exact set difference that made the packet raise on 77.5% of the contracts on disk.
- **`WorktreeState` stays local on purpose**, and only because
 `application.worktree_status` constructs this model directly and is its sole writer.
- **`NextTool."worktree_cleanup"` is deliberately retained (260831-LOCR-L31).** `guidance.py` no
 longer emits it, but `_project_terminal_contract_status` does, so removing the member would make a
 live projection unrepresentable. A member goes when its **last** producer goes, not its last
 guidance caller.
- **The worktree surface's next move must name a registered PUBLIC tool, and this is now declared
 and enforced here (260831-LOCR-L32).** `_project_terminal_contract_status` writes `nextAction` /
 `nextTool` / `nextArgs`; all three are declared on `WorktreeCommandResponse`
 and
 `_require_registered_public_next_tool`


 and
 refuses a value outside `PUBLIC_TOOLS`. The rule
 is **per surface, deliberately**: the `task_doc` surface may name the registered-but-non-public
 `session_retire` (`TaskDocResponse` is not a `WorktreeCommandResponse`), so do not widen
 `PUBLIC_TOOLS` and do not special-case that name here. `WorktreeSummary` is never on this path and
 its single-value `nextAction` literal stays honest there.
- **`PUBLIC_TOOLS` is read from its `models` leaf, never imported from `mcp`.** `layers.toml` ranks
 models = 2 and mcp = 22, so `models → mcp` is a violation; a function-local import trips
 `ruff PLC0415` and suppressions are forbidden. The tuple's one definition is
 `models/tools/public_roster.py`
 . Do not move it
 back into the adapter.
- Absent is the shape for `nextTool` / `nextArgs` / `nextRequiredArgs`. The
 projection reports what the producer wrote and never fills a hole the producer
 left; `""`, `{}` and `[]` are not substitutes for an omitted key.
- `unknownContractCells` is a report, not a state: it coexists with
 `state="active"` and with fully populated sibling fields.
- Worktree command payloads may remain flexible while the service API is still
 carrying operation-specific result blocks.
- Every advertised public worktree tool's response envelope is declared here AND registered in
 `models/tools/tool_registry.py`. A model declared without its registry row — or a row without
 its model — leaves the tool advertised and unable to return a payload, because
 `finalize_tool_response` indexes that registry by tool name.
- Sync control/state literals are declared once here and consumed by journal/result/public seams;
 do not retype or widen them into arbitrary strings downstream.
- Stable sync projection is descriptive only. Models do not locate the journal, select a series,
 authorize Git mutation, or infer state from task/queue data.
- Closeout and integration quality result blocks are a deliberate strict exception: both read the
 shared `QualityGateResult`, preserving stable/published path meanings and rejecting extra fields.
- Do not reintroduce raw shell command strings into context-packet next hints.
### Todos

No additional file-local TODO is established by this candidate review.
## 260928-MIK-L08 The Sync Response Carries The Recomputed Worklist (MIK-R08 Rule 8)

`WorktreeSyncResponse` gained `knowledgeWorklist: dict[str, Any] | None = None`. A completed managed sync
(and the `continue` replay of a completed generation) recomputes the leaf's change-to-knowledge worklist
at the base pair the sync wrote, and attaches its compact summary (state, path, digest, item counts,
unreadable inputs) here. With no worklist applicable (both memory sides unconverted, every production leaf
before MIK-R37) or no port bound, the field is `None` and the response is dumped with `exclude_none`, so
today's sync responses are unchanged.
## Evidence

### Repo-Internal References

- `SourceLineageProjection` owns the current boundary described above. [67]
- `SyncOperationProjection` owns the current boundary described above. [68]
- `SyncResolutionProjection` owns the current boundary described above. [69]
- `SyncResolutionInput` owns the current boundary described above. [70]
### Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

No configured external domain source applies.
### Cross-Repo References

No separate cross-repository implementation claim is made.

No external implementation source applies.
### Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.
### Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
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
## 260821-DAGQC-L2 Typed Quality Result

`WorktreeCloseoutResponse.code_quality_gate` and `WorktreeIntegrateResponse.quality_gate` now share
the strict `QualityGateResult`. This closes the former open mapping, retains both the stable wrapper
`reportPath` and optional immutable `publishedResultPath`, and gives memory policy/cap their exact
public types. The surrounding command envelopes remain flexible for unrelated operation data.
## MCAR-L03 Closeout Pair Projection

Closeout preview and apply schemas now declare the exact pair plus bounded pair-refusal fields and
repair arguments. The fields are scoped to closeout responses rather than being generalized to
unrelated worktree operations.
## 260831-LOCR-L29 Record-Landing Wire Response

`WorktreeRecordLandingResponse` (operation literal `worktree_record_landing`) declares the landing
evidence the `worktree_record_landing` tool returns: `integrationStrategy`, `landedCodeCommit`, and
`landingTargets`. It inherits `WorktreeCommandResponse`, so it stays flexible for unrelated
operation data and exposes no operation id, journal address, or Git-mutation authority.

The class exists because the tool was registered and advertised with no response model. The payload
builder routes every result through `finalize_tool_response`, which indexes `TOOL_RESPONSE_MODELS`
by tool name, so `worktree_record_landing` raised `KeyError` inside its `@server.tool()` handler
instead of returning a payload — the advertised tool could not answer at all. Declaring the
envelope here, together with its registry row in `models/tools/tool_registry.py`, is what makes the
advertised name reachable at the same strict boundary as `WorktreeIntegrateResponse`.
## 260831-LOCR-L30 Checkpointed Integration And Its Wire Envelope

`IntegrationStatus` gained a fourth member, `checkpointed` . It names the state a series
master enters when its accumulated line has landed into its super branch **and the master stays
open**. Before it existed, a partially landed master had to report `not-started` — "nothing of mine
has left" — while its content was already upstream, and that is exactly the state that made a
partial master's retirement look safe. The producer is
`worktrees/modules/landing_record.py::record_landed_integration`, which writes `checkpointed` for a
checkpoint and `completed` + `cleanup="pending"` for a final landing
.
Because `worktrees/worktree_contract.py` derives `VALID_INTEGRATION_STATUSES` from this alias, the
new member is immediately readable and writable on the persisted contract rather than a value the
read path would reject.

**`WorktreePhase` deliberately did not gain a member for the checkpoint state.** A checkpointed
contract projects through the existing `worktree-started` phase
.
`WorktreePhase` is a closed `Literal` whose members the dashboard mirrors at five files / six sites
: `EngineRoom.tsx:59-66`
(`LIFECYCLE_PHASES`, `"integration-pending"` at `:63`), `BootTimeline.tsx:88` and `:110`,
`useEngineTimeline.ts:41`, `buildEngineRoomModel.ts:16` (`PHASE_ORDER`) and `geometry.ts:218`
(`LANDING_PHASES`). A ninth member would therefore be a
cross-codebase change, and a series that is still working is honestly `worktree-started`; the
checkpoint truth rides in the guidance summary instead. Do not add a member for it here.

The declaration site in the table above is this file, not `worktree_contract.py`: all the shared
lifecycle vocabularies that card lists are declared here
(`MemoryMode` is imported from the kernel and re-exported) and imported back by
`worktrees/worktree_contract.py` , which only derives the runtime `VALID_*` frozensets from
them.

`WorktreeCheckpointLandingResponse` (operation literal `worktree_checkpoint_landing`) declares the
checkpoint landing evidence : `integrationStrategy`, `integratedCodeCommit`,
checkpoint landing evidence : `integrationStrategy`, `integratedCodeCommit`,
`integratedMemoryContentCommit`. It inherits
`WorktreeCommandResponse`, so it stays flexible for unrelated operation data and exposes no
operation id, journal address, or Git-mutation authority.

The class exists because the tool was registered and advertised with no response model — the same
hole `WorktreeRecordLandingResponse` closed one leaf earlier. `finalize_tool_response` indexes
`models/tools/tool_registry.py::TOOL_RESPONSE_MODELS` by tool name, so a published tool whose name
has no row raises `KeyError` inside its `@server.tool()` handler instead of returning a payload.
Declaring the envelope here, together with its registry row in
`models/tools/tool_registry.py`, is what keeps the advertised name answerable at the same strict
boundary as `WorktreeIntegrateResponse`.
## 260831-LOCR-L37 The Pause Envelope

`WorktreePauseResponse` (operation literal `worktree_pause`)
 is the stop's wire envelope. It declares exactly one
 is the stop's wire envelope. It declares exactly one
field of its own — `paused: bool = False` — and inherits `WorktreeCommandResponse`, so the stop's
result carries the ordinary envelope's `state`, `status`, `summary` and `nextStep` without this class
having to restate them.

The one field is the whole design, and the docstring says why: `paused` is claimed **only** by the
route that releases the master's atomic-series selection. A publication that moved refs has no
business setting it, because the two operations answer different questions and only one of them stops
anything. So `paused is True` on a result is evidence that the stop ran, and a checkpoint landing's
envelope — `WorktreeCheckpointLandingResponse` above, with its two output commit fields — cannot express it.

Like its siblings, the class exposes no operation id, journal address or Git authority. `nextStep` is
deliberately **absent** from a successful pause payload rather than set to `None`, which the flexible
envelope permits: the stop proposes no continued execution, and the tests assert the keys are not
present. `TOOL_RESPONSE_MODELS["worktree_pause"]` is this class, so the advertised name is answerable
at the same strict boundary as the rest of the worktree surface.
## 260831-LOCR-L34 The Checkpoint Tool In `NextTool`

`NextTool` gained a seventh member, `worktree_checkpoint_landing`
 (the literal sits at `:75`, after
`worktree_integrate`). It is a registered public worktree tool and an approval-gated protected-ref
landing, so the same `request_integration_decision` intent that carries a finished master to
`worktree_integrate` carries an **unfinished** one here: the checkpoint's preview emits
`next_guidance("request_integration_decision", tool="worktree_checkpoint_landing", ...)` and its
`integration-ref-race` refusal now names the checkpoint rather than the wrong tool. Both literals that
reach that payload are registered public tools, which is what the `_require_registered_public_next_tool`
validator requires.

**`NextOperation` was deliberately NOT widened.** The checkpoint is a partial **publication** under
the same `request_integration_decision` intent — an integration decision, not a new lifecycle phase —
so it rides the existing operation. Adding a member would put a non-phase value into the set
`WorktreeSummary` and the context packet claim to report — the same reason the recovery vocabulary is
a separate alias. **The pause is a different matter and is no integration decision at all**
(260831-LOCR-L36): a pause stops the master's work, publishes nothing and moves no ref, so nothing
about it belongs in this vocabulary either. This is a *typing* change only: the emitted guidance was
already correct, and the roster validator would already have admitted the name; declaring it here is
what makes the produced == declared vocabulary honest.

Note the asymmetry with `NextTool."worktree_cleanup"` above: that member is retained because a
producer still emits it, while this one is added because a producer now emits it for the first time on
the checkpoint route.
## 260915-KS-L23 The Coherence Validate Tool In `NextTool`

`NextTool` gained its **eighth** member, `curator_coherence`, at `:86` (the literal now spans
`65-87`): the standalone `validate` of a published curator-coherence authority. It is added for the
same reason as the checkpoint tool above — it is a registered public tool that a producer now emits —
and for one more that makes it the sharpest case in this vocabulary: **it is the one step whose window
closes at `lifecycle_finalize_task`.** Finalize's automatic cleanup collects the enclosure root, so a
leaf that integrates and finalizes without validating can never re-prove what it published (D-25), and
`worktrees/modules/guidance.py` no longer routes `closeout-completed` to this tool — the spelling
survives only as the landing arc's onward precondition.

**`NextOperation` was deliberately NOT widened a third time.** The move is still
`request_integration_decision`; the validation is its **precondition**, not a new lifecycle phase, so
adding a member would put a non-phase value into the set `WorktreeSummary` and the context packet
claim to report — the same reasoning the L34 section above records for the checkpoint tool.

The produced == declared invariant holds in both directions here: the guidance machine emits the name
and the literal declares it, and `_require_registered_public_next_tool` still admits it because
`curator_coherence` is a registered public tool.
## 260831-LOCR-L32 The Next-Move Triple Is Typed And Enforced

`WorktreeCommandResponse` declares `nextAction` / `nextTool` / `nextArgs`
, and
`_require_registered_public_next_tool`


, and
refuses any `nextTool` outside `PUBLIC_TOOLS` with
`nextTool must name a registered public tool`. `WorktreeStatusResponse` inherits all three, so the
`terminal-archive-ready` projection's write is no longer an unchecked extra. Declaring the triple here
rather than on `WorktreeStatusResponse` is what keeps `WorktreeSyncResponse` and
`WorktreeOperationControlResponse` narrowing `nextTool` exactly as they already did.

This closes the gap the two previous entries in this card's history describe. Those entries were
correct about the mechanism — the write passed through `extra="allow"` verbatim and unchecked, the
branch is reachable through the rolled-back contract amendment, and the emitted guidance was already
correct — and they recorded a recommended fix that is now the implementation. The superseded parts are
the phrases "undeclared", "unchecked", "missing types" and "recorded, not implemented"; the keys are
declared and the roster is enforced.

**`PUBLIC_TOOLS` moved into `models` to make the validator possible.** See
`models/tools/public_roster.py` and the `mcp/tools/base.py` card. `models → mcp` is a `layers.toml`
violation (models = 2, mcp = 22), a function-local import trips `ruff PLC0415`, and module-level
imports in either direction are circular — so the roster's move is a precondition of this fix, not a
companion cleanup.

**The rule is per surface and that is deliberate.** `session_retire` is registered but not public, and
it reaches the wire only through the `task_doc` surface, which is not a `WorktreeCommandResponse`. Do
not widen `PUBLIC_TOOLS`; do not special-case the name here.
### Reviewed And Deliberately Not Changed

| Candidate change | Verdict | Why |
| --- | --- | --- |
| Add `worktree_abandon` to `NextTool` | **No** | `NextTool` is the guidance machine's produced == declared vocabulary; the machine cannot emit abandon, so the member would break the invariant it exists to keep. The cleanup operation reaches the wire through `WorktreeCommandResponse.nextTool` instead. |
| Narrow the flexible envelope's `nextTool` to a literal | **No** | This family legitimately emits many tools; narrowing would manufacture new validation errors for every existing producer. Roster membership is the enforcement. |
| Widen `WorktreeSummary.nextAction` | **No** | Its single producer hard-codes `developer-decision`, and `WorktreeSummary` is never on this path. |
| Widen `PUBLIC_TOOLS` to admit `session_retire` | **No** | It is deliberately non-public; the `task_doc` surface is why the rule is per surface. |
| Widen `NextOperation` for the checkpoint route (260831-LOCR-L34) | **No** | Pausing a master is an integration decision, not a phase. The checkpoint reuses the existing `request_integration_decision` operation; a new member would put a non-phase value into the set `WorktreeSummary` and the context packet report. `NextTool` did gain the tool, because a tool a producer emits must be declared. |

- The six persisted contract vocabularies (`WorkflowKind` … `CleanupStatus`) with their `VALID_*` frozensets, the `ContractCells` typed write record and `amend_contract`. [71]
- The guidance state machine imports and writes `WorktreePhase`, `NextOperation` and `NextTool` (declared in this model since L9), plus the separate `RecoveryOperation`/`RecoveryTool` that deliberately do NOT reach this model. [72]
- The registered-but-deliberately-non-public name that must stay outside the worktree invariant, and the `task_doc` surface that legitimately emits it (its `nextTool` is a plain `str \\| None`, on a class that is not a `WorktreeCommandResponse`). [73]
- Public worktree MCP application entry points delegate to the package worktree manager, and `worktree_sync_tool` now passes the paired resolution input. [74]
- The current module exposes `SourceLineageEdge`, `SourceLineageRecovery`, `SourceLineageProjection` at this ownership boundary. [75]
- WorktreeSummary is the strict context-packet shape for the c-09-git-worktree-manager lifecycle. [76]
- The shared wire vocabularies are declared in this module (see the table above). [77]
- WorktreeSummary's vocabulary fields are typed; application.worktree_status constructs this model directly and is its sole writer. [78]
- The terminal-archive-ready projection serves the archive-ready state once a failed contract amendment is rolled back. [79]
- TerminalCleanupOperation is the two-member terminal-cleanup vocabulary (worktree_cleanup, worktree_abandon). [80]
- finalize_tool_response validates one declared response, applies optional caller enrichment, and counts tokens. [81]
- TOOL_RESPONSE_MODELS maps each tool name to its declared response model. [82]
- WorktreeStatusResponse carries the status operation literal with lifecycle and sync projections. [83]
- FlexibleResponseModel is the extra-allowing base class for provider-native diagnostic payloads. [84]
- The membership validator refuses a next move outside the advertised roster. [85]
- PUBLIC_TOOLS lives in models as a zero-import leaf tuple the validator reads. [86]
- The nextAction literal this file declares stays honest because its only producer hard-codes developer-decision. [87]
- The guarded cleanup amendment whose rolled-back publication produces the terminal-archive-ready state. [88]
- The guarded abandon amendment whose rolled-back publication produces the terminal-archive-ready state. [89]
- The terminal-archive-ready projection serves the archive-ready state once a failed contract amendment is rolled back. [90]
- R10: every value a producer can emit validates at the wire boundary it crosses. [91]
- RecoveryOperation and RecoveryTool deliberately do NOT reach this model. [92]
- RecoveryOperation and RecoveryTool deliberately do NOT reach this model. [93]
- nextRequiredArgs is an optional string list on the command envelope. [94]
- unknownContractCells (`list[str] | None`, default None) is present only when the contract file carried a cell outside its declared vocabulary, as notice that values were substituted. [95]
- WorktreeCommandResponse declares the next-move triple: nextAction, nextTool and nextArgs. [96]
- The membership validator refuses a next move outside the advertised roster. [97]
- PUBLIC_TOOLS lives in models as a zero-import leaf tuple the validator reads. [98]
- `IntegrationStatus` gained a fourth member, `checkpointed` . [99]
- record_landed_integration publishes that a contract’s code landed and returns the updated contract. [100]
- The post-integration phase routes the outcome after integration was attempted (blocked, or landed with carryover/cleanup). [101]
- WorktreePhase is a closed `Literal` whose members the dashboard mirrors at five files / six sites (`EngineRoom.tsx:59-66` via `LIFECYCLE_PHASES`). [102]
- The shared wire vocabularies are declared in this module (see the table above). [103]
- The shared wire vocabularies are declared in this module (see the table above). [104]
- The shared wire vocabularies are declared in this module (see the table above). [105]
- The shared wire vocabularies are declared in this module (see the table above). [106]
- The shared wire vocabularies are declared in this module (see the table above). [107]
- worktree_contract.py derives the runtime VALID_* frozensets from the declared vocabularies. [108]
- Checkpoint responses record only the real integrated code and memory-content commits. [109]
- The pause envelope declares the stop's one own field, paused, and inherits the ordinary command envelope. [110]
- worktree_checkpoint_landing joined NextTool while NextOperation was deliberately left at seven members. [111]
- WorktreeSyncResponse and WorktreeOperationControlResponse narrow nextTool exactly as they already did. [112]
