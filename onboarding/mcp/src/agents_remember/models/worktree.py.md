# mcp/src/agents_remember/models/worktree.py

| Field | Value |
| --- | --- |
| Field | Value |
| ---------------------- | ------------------------------------------ |

## Governing Overview

[Owning overview](overview.md)

## Purpose

`worktree.py` defines context-packet worktree summaries, public worktree tool response envelopes,
and the closed wire vocabulary for resumable sync control, phases, sides, and stable journal
projection.

## 260915-KS-L40 The Sync Conflict Vocabulary And Its One Decided Input

**`SyncResolutionAction` gained a third member, `reconcile`** cit:([`SyncResolutionAction`], mcp/src/agents_remember/models/worktree.py:95-95), and it is the only action that carries a decided input. The vocabulary is a closed `Literal`, so the member's presence is what makes the action addressable at all; nothing else about `continue`/`cancel` changed.

**`SyncResolutionInput` pairs the action with the decision it may carry** cit:([`SyncResolutionInput`], mcp/src/agents_remember/models/worktree.py:171-181): `action: SyncResolutionAction | None` and `knowledge: AuthoredReconciliation | None`. The pairing exists because the two are refused *as a pair* — `reconcile` without a decision and a decision with any other action are both `sync-input-invalid` — so one value travels instead of two parameters every layer has to keep consistent, and the reason it is a model rather than a widened argument list is `PLR0913`: `worktree_sync_tool` was already at the argument ceiling.

**`SyncKnowledgeConflict` is the diagnosis, published verbatim** cit:([`SyncKnowledgeConflict`], mcp/src/agents_remember/models/worktree.py:184-203): `path`, the engine's `conflict` (table, operation and the exact refused key), the typed `refusal` with the action it advertises, this seam's `detail` when the engine never answered, and `decisions` — the authored decisions that conflict admits. Every field is a value the engine or the seam produced, carried rather than re-rendered, and an **empty `decisions` is meaningful**: it says nothing an authored decision can settle, which is exactly the schema-disagreement case whose refusal's own `next_action` says the difference is reported rather than reconciled. The class exists because this explanation used to stop one layer below the agent.

**Two envelopes gained the projection.** `SyncResolutionProjection.knowledge` cit:([`SyncResolutionProjection`], mcp/src/agents_remember/models/worktree.py:206-222) is what the retained-conflict response and its dry run report, and `SyncOperationProjection.knowledgeConflict` cit:([`SyncOperationProjection`], mcp/src/agents_remember/models/worktree.py:152-168) is the same explanation on a status read — which is the point, because the journal re-projects the side on every later call. `WorktreeSyncResponse.invalidField` gained `knowledge_resolution` as its third admitted value, so a refused decision names the field the caller got wrong.

### Reviewed And Deliberately Not Changed

| Candidate change | Verdict | Why |
| --- | --- | --- |
| Widen `SyncResolutionAction` further (e.g. a `restore-left-rows`) | **No** | The referential refusal's other orientation is deliberately not expressible: retracting an arriving `UPDATE`/`DELETE` would remove or overwrite content the left authored. See the leaf's evidence, "What is not covered". |
| Let `decisions` be optional and inferred | **No** | An empty list is a fact the agent acts on (nothing to reconcile), not missing data; `expressible_decisions` is the one place it is computed. |
| Carry the diagnosis on the response only, not the journal | **No** | A resumed sync re-projects the side from the journal, so a response-only field would lose the row on the second call — which is the failure this leaf closes. |

## Code Commentary

### Logic

`WorktreeCheckpointLandingResponse` carries `integrationStrategy`, `integratedCodeCommit`,
and `integratedMemoryContentCommit`. It has no integrated-ledger field; the response names the
two real branch outputs of the checkpoint. Cache refresh does not add a commit identity to this
wire contract, and stop-only pause remains a separate response.

cit:([`WorktreeSummary`], mcp/src/agents_remember/models/worktree.py:310-364) is the strict context-packet shape for the
cit:([`WorktreeSummary`], mcp/src/agents_remember/models/worktree.py:310-364) is the strict context-packet shape for the
`c-09-git-worktree-manager` lifecycle. Its vocabulary fields are typed, and
**since 260731-EFA-L4 every shared lifecycle vocabulary is imported from the
module that produces it; only `WorktreeState` remains local** cit:([`WorktreeState`], mcp/src/agents_remember/models/worktree.py:307-307). `WorktreeSummary` itself is declared at
cit:([`WorktreeSummary`], mcp/src/agents_remember/models/worktree.py:310-364). The command response models
cit:([`WorktreeSummary`], mcp/src/agents_remember/models/worktree.py:310-364). The command response models
module that produces it; only `WorktreeState` remains local** cit:([`WorktreeState`], mcp/src/agents_remember/models/worktree.py:307-307). `WorktreeSummary` itself is declared at
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
cit:([`_project_terminal_contract_status`], mcp/src/agents_remember/application/worktree_status.py:463-505),
which sets `"nextTool": archive.cleanupOperation` for a terminal contract, and `cleanupOperation` is
`TerminalCleanupOperation = Literal["worktree_cleanup", "worktree_abandon"]`
cit:([`TerminalCleanupOperation`], mcp/src/agents_remember/models/lifecycles/enclosure.py:14-14). Do not
"tidy" the member away: it is one of the two values that route actually emits.

**The terminal-status next move is now declared AND enforced here (260831-LOCR-L32).** This section
replaces three earlier accounts of the same seam. The first two were wrong in opposite directions
(the write does **not** land on `WorktreeSummary` and does **not** violate one of its declared
fields); the third — "verified mechanism, correct behaviour, missing types, fix recorded but not
implemented" — was right about the mechanism and is now superseded by the fix itself.

*The defect it closed.* `worktree_status` is validated at exactly one place,
`TOOL_RESPONSE_MODELS[tool_name].model_validate(payload)`
cit:(["TOOL_RESPONSE_MODELS[tool_name].model_validate(payload)"], mcp/src/agents_remember/models/tools/tool_response.py:23-23),
and that registry maps `"worktree_status"` to `WorktreeStatusResponse`
cit:(["\"worktree_status\": WorktreeStatusResponse"], mcp/src/agents_remember/models/tools/tool_registry.py:192-192;
mcp/src/agents_remember/models/worktree.py:406-409; mcp/src/agents_remember/models/tools/tool_registry.py:199-199). Resolving down through
`WorktreeCommandResponse` → `FlexibleToolResponse` → `FlexibleResponseEnvelope` →
`FlexibleResponseModel`, whose `model_config` is
`ConfigDict(extra="allow")`
cit:(["model_config = ConfigDict(extra=\"allow\")"], mcp/src/agents_remember/models/base.py:22-22),
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
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442), a
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442), a
`@field_validator("nextTool")` raising `nextTool must name a registered public tool; <value> is not in
PUBLIC_TOOLS`. `None` still passes, and `WorktreeSyncResponse` / `WorktreeOperationControlResponse`
narrow `nextTool` further exactly as they did before.

*`PUBLIC_TOOLS` had to move for this to be expressible.* The validator needs the roster, and
`models/worktree.py` may not import `mcp` (`layers.toml` ranks models = 2, mcp = 22). The tuple's one
definition is now the zero-import leaf
`agents_remember/models/tools/public_roster.py`
cit:([`PUBLIC_TOOLS`], mcp/src/agents_remember/models/tools/public_roster.py:22-97), imported here at
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
  cit:(["developer-decision"], mcp/src/agents_remember/models/worktree.py:355-355), and
  cit:(["developer-decision"], mcp/src/agents_remember/models/worktree.py:355-355), and
  `WorktreeSummary` is never on this path — it is constructed only inside `worktree_status_packet`'s
  own helpers for the `context_packet` surface (`application/worktree_status.py:79`, `:120`, `:199`,
  `:242`). Its single-value literal is honest where it lives.

**The branch is reachable, and it is now covered.** The terminal archive and receipt are published
(locator → `terminal-archived`) *before* the surviving contract is amended: `cleanup.py` completes its
guard around `amend_contract(contract, ContractCells(cleanup="completed"))`
cit:(["amend_contract(contract, ContractCells(cleanup=\"completed\"))"], mcp/src/agents_remember/worktrees/modules/cleanup.py:941-941),
and `abandon.py` does the same around `cleanup="abandoned"`
cit:(["amend_contract(contract, ContractCells(cleanup=\"abandoned\"))"], mcp/src/agents_remember/worktrees/modules/abandon.py:348-348).
Both writes are wrapped in `guard.complete(..., rollback_publish=...)`, so a **failed publication
deliberately restores the archived contract while the locator stays `terminal-archived`** — exactly
the state the projector serves, `"terminal-archive-ready"`
cit:(["terminal-archive-ready"], mcp/src/agents_remember/application/worktree_status.py:470-470).
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
cit:(["R10: every value a producer can emit validates at the wire boundary it crosses."], mcp/tests/test_wire_vocabulary_exhaustiveness.py:1-1).
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
`RecoveryOperation` / `RecoveryTool` aliases (cit:([`RecoveryOperation`, `RecoveryTool`], mcp/src/agents_remember/worktrees/modules/guidance.py:40-51; mcp/src/agents_remember/worktrees/modules/guidance.py:52-57)) precisely so
a wider `NextOperation` cannot put "requires developer approval" back into the set
the context packet's `nextOperation` claims to be.

`nextRequiredArgs` (cit:([`nextRequiredArgs`], mcp/src/agents_remember/models/worktree.py:342-342)) is **omitted rather than `[]`** when there is
`nextRequiredArgs` (cit:([`nextRequiredArgs`], mcp/src/agents_remember/models/worktree.py:342-342)) is **omitted rather than `[]`** when there is
nothing to supply. `next_guidance` writes the key only when the next call needs a
caller-supplied argument; the projection now reports what the producer said
instead of substituting a value for it. This is a stated wire change: measured
across the 213 contracts, 48 responses that previously carried
`"nextRequiredArgs": []` now omit the key, and it stays omitted. An absent
`nextRequiredArgs` means what the empty list meant — the next call needs nothing
beyond `nextArgs` — and there is no third state to confuse it with. The same rule
now covers `nextTool` and `nextArgs`, where the old substitution had put an
un-declarable `""` on the wire.

`unknownContractCells: list[str] | None` (cit:([`unknownContractCells`], mcp/src/agents_remember/models/worktree.py:347-347)) is new. It is present only
`unknownContractCells: list[str] | None` (cit:([`unknownContractCells`], mcp/src/agents_remember/models/worktree.py:347-347)) is new. It is present only
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
- **No vocabulary is retyped here.** Every `Literal` on `WorktreeSummary` except
  `WorktreeState` is imported from its producer. Adding a member is a one-place
  edit at the producer; re-declaring one locally recreates the exact set
  difference that made the packet raise on 77.5% of the contracts on disk.
- **`WorktreeState` is the only local alias**, and only because
  `application.worktree_status` constructs this model directly and is its sole writer.
- **`NextTool."worktree_cleanup"` is deliberately retained (260831-LOCR-L31).** `guidance.py` no
  longer emits it, but `_project_terminal_contract_status` does, so removing the member would make a
  live projection unrepresentable. A member goes when its **last** producer goes, not its last
  guidance caller.
- **The worktree surface's next move must name a registered PUBLIC tool, and this is now declared
  and enforced here (260831-LOCR-L32).** `_project_terminal_contract_status` writes `nextAction` /
  `nextTool` / `nextArgs`; all three are declared on `WorktreeCommandResponse`
  cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-400) and
  `_require_registered_public_next_tool`
  cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442)
  cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442)
  cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-400) and
  refuses a value outside `PUBLIC_TOOLS`. The rule
  is **per surface, deliberately**: the `task_doc` surface may name the registered-but-non-public
  `session_retire` (`TaskDocResponse` is not a `WorktreeCommandResponse`), so do not widen
  `PUBLIC_TOOLS` and do not special-case that name here. `WorktreeSummary` is never on this path and
  its single-value `nextAction` literal stays honest there.
- **`PUBLIC_TOOLS` is read from its `models` leaf, never imported from `mcp`.** `layers.toml` ranks
  models = 2 and mcp = 22, so `models → mcp` is a violation; a function-local import trips
  `ruff PLC0415` and suppressions are forbidden. The tuple's one definition is
  `models/tools/public_roster.py`
  cit:([`PUBLIC_TOOLS`], mcp/src/agents_remember/models/tools/public_roster.py:22-97). Do not move it
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

- The optional worklist summary field and its comment. [1]
- Where the sync attaches it. [2]

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

No configured external domain source applies.

### Repo-Internal References

- Checkpoint responses record only the real integrated code and memory-content commits. [3]
- Sync control, side, phase, operation-state, and strict projection shapes are declared together, including the third resolution action and the diagnosis the journal carries. [4]
- **The action-and-decision pair a reconcile call carries, and why it is one value rather than two parameters.** [5]
- **The engine's own explanation of a retained knowledge conflict, with the decisions it admits and the empty list that means none.** [6]
- **The retained-conflict response field that carries the explanation, and the dry-run projection of the same value.** [7]
- Series status and command responses carry optional activation facts and bounded admission evidence. [8]
- Series status and command responses carry optional activation facts and bounded admission evidence. [9]
- The activation fact and the admission envelope are keyed by the addressed contract's `contractFingerprint`, not by a source pair; the nested activation snapshot is the only activation evidence. [10]
- The activation fact and the admission envelope are keyed by the addressed contract's `contractFingerprint`, not by a source pair; the nested activation snapshot is the only activation evidence. [11]
- The deleted blocking vocabulary left no field behind: the admission envelope declares neither `classification`, `blocking` nor a source pair. [12]
- The sync response class as it now reads: recovery guidance (`nextOperation`, `nextTool`, `nextArgs`, `cancelArgs`) with no public operation id, and, since MIK-R08, the optional `knowledgeWorklist` summary a completed sync attaches. [13]
- The sync response class as it now reads: recovery guidance with no public operation id, `knowledge_resolution` as the third field its `invalidField` may name, and, since MIK-R08, the optional `knowledgeWorklist` summary. [14]
- The record-landing envelope declares the landing evidence and its operation literal. [15]
- The checkpoint-landing envelope declares the two output commits an unfinished master landed and its operation literal. [16]
- The pause envelope declares the stop's one own field, `paused`, and inherits the ordinary command envelope; only the route that releases the selection claims it. [17]
- The pause envelope declares the stop's one own field, `paused`, and inherits the ordinary command envelope; only the route that releases the selection claims it. [18]
- The `checkpointed` member the checkpoint writer records and the persisted-contract vocabulary derives. [19]
- The `checkpointed` member the checkpoint writer records and the persisted-contract vocabulary derives. [20]
- The two `NextOperation`/`NextTool` members the L31 leaf moved: `finalize` in place of `retry_cleanup`, and `lifecycle_finalize_task` added. [21]
- The two `NextOperation`/`NextTool` members the L31 leaf moved: `finalize` in place of `retry_cleanup`, and `lifecycle_finalize_task` added. [22]
- The L34 addition: `worktree_checkpoint_landing` joined `NextTool` (`:70`) while `NextOperation` was deliberately left at seven members. [23]
- The L34 addition: `worktree_checkpoint_landing` joined `NextTool` (`:70`) while `NextOperation` was deliberately left at seven members. [24]
- The producer that keeps `NextTool."worktree_cleanup"` live after `guidance.py` stopped emitting it, and the closed two-member cleanup-operation vocabulary it copies from. [25]
- The response registry selects WorktreeStatusResponse and the shared response validator validates its envelope. [26]
- The `extra="allow"` config on the flexible envelope. It is **no longer** what decides the next-move keys' fate: the three keys are declared below, so they are no longer extras. [27]
- The three next-move keys declared on the command envelope, which is what stops the projector's write from riding as an undeclared extra. [28]
- The membership validator that refuses a next move outside the advertised roster — the enforcement half of the invariant, and the reason the roster had to move into `models`. [29]
- The advertised public roster this model reads, in its zero-import `models` leaf (the tuple's single definition; `mcp/tools/base.py` re-exports it). [30]
- The registry distinguishes internal names from public worktree tools, while TaskDocResponse.nextTool is a plain optional string. This model/registry boundary does not establish a current task_doc emission of any specific internal name. [31]
- The executor for the declared-and-enforced next move: it reaches the archive-ready state through real production calls for both cleanup verbs, binds the emitted args to the real tool signature, and drives the validator in both directions. [32]
- The `nextAction` literal this file **does** declare, and which stays honest because its only producer hard-codes it — do not widen it. [33]
- The reachable terminal state the projector serves once a failed contract amendment is rolled back while the locator stays `terminal-archived`. [34]
- The two guarded contract amendments whose rolled-back publication produces that state, for cleanup and abandon respectively. [35]
- The module that should enforce produced == declared for `NextTool` and currently has **zero** test bodies — only this docstring, helpers and "moved verbatim" breadcrumbs remain. [36]
- The sole writer of `WorktreeSummary`: `worktree_status_packet` returns the MODEL now, and `_summary_from_status_payload` projects field by field, reading optional next and activation fields without inventing values. [37]
- The six persisted contract vocabularies (`WorkflowKind` … `CleanupStatus`) with their `VALID_*` frozensets, the `ContractCells` typed write record and `amend_contract`. [38]
- The guidance state machine imports and writes `WorktreePhase`, `NextOperation` and `NextTool` (declared in this model since L9), plus the separate `RecoveryOperation`/`RecoveryTool` that deliberately do NOT reach this model. [39]
- Checkpoint responses record only the real integrated code and memory-content commits. [40]
- Series status and command responses carry optional activation facts and bounded admission evidence. [41]
- The activation fact and the admission envelope are keyed by the addressed contract's `contractFingerprint`, not by a source pair; the nested activation snapshot is the only activation evidence. [42]
- The deleted blocking vocabulary left no field behind: the admission envelope declares neither `classification`, `blocking` nor a source pair. [43]
- The sync response class as it now reads: recovery guidance (`nextOperation`, `nextTool`, `nextArgs`, `cancelArgs`) with no public operation id, and, since MIK-R08, the optional `knowledgeWorklist` summary a completed sync attaches. [44]
- The record-landing envelope declares the landing evidence and its operation literal. [45]
- The checkpoint-landing envelope declares the two output commits an unfinished master landed and its operation literal. [46]
- The pause envelope declares the stop's one own field, `paused`, and inherits the ordinary command envelope; only the route that releases the selection claims it. [47]
- The `checkpointed` member the checkpoint writer records and the persisted-contract vocabulary derives. [48]
- The two `NextOperation`/`NextTool` members the L31 leaf moved: `finalize` in place of `retry_cleanup`, and `lifecycle_finalize_task` added. [49]
- The producer that keeps `NextTool."worktree_cleanup"` live after `guidance.py` stopped emitting it, and the closed two-member cleanup-operation vocabulary it copies from. [50]
- The response registry selects WorktreeStatusResponse and the shared response validator validates its envelope. [51]
- The `extra="allow"` config on the flexible envelope. It is **no longer** what decides the next-move keys' fate: the three keys are declared below, so they are no longer extras. [52]
- The three next-move keys declared on the command envelope, which is what stops the projector's write from riding as an undeclared extra. [53]
- The membership validator that refuses a next move outside the advertised roster — the enforcement half of the invariant, and the reason the roster had to move into `models`. [54]
- The advertised public roster this model reads, in its zero-import `models` leaf (the tuple's single definition; `mcp/tools/base.py` re-exports it). [55]
- The registered-but-deliberately-non-public name that must stay outside the worktree invariant, and the `task_doc` surface that legitimately emits it (its `nextTool` is a plain `str \| None`, on a class that is not a `WorktreeCommandResponse`). [56]
- The executor for the declared-and-enforced next move: it reaches the archive-ready state through real production calls for both cleanup verbs, binds the emitted args to the real tool signature, and drives the validator in both directions. [57]
- The `nextAction` literal this file **does** declare, and which stays honest because its only producer hard-codes it — do not widen it. [58]
- The reachable terminal state the projector serves once a failed contract amendment is rolled back while the locator stays `terminal-archived`. [59]
- The two guarded contract amendments whose rolled-back publication produces that state, for cleanup and abandon respectively. [60]
- The module that should enforce produced == declared for `NextTool` and currently has **zero** test bodies — only this docstring, helpers and "moved verbatim" breadcrumbs remain. [61]
- The sole writer of `WorktreeSummary`: `worktree_status_packet` returns the MODEL now, and `_summary_from_status_payload` projects field by field, reading optional next and activation fields without inventing values. [62]
- The six persisted contract vocabularies (`WorkflowKind` … `CleanupStatus`) with their `VALID_*` frozensets, the `ContractCells` typed write record and `amend_contract`. [63]
- The guidance state machine imports and writes `WorktreePhase`, `NextOperation` and `NextTool` (declared in this model since L9), plus the separate `RecoveryOperation`/`RecoveryTool` that deliberately do NOT reach this model. [64]
- Public worktree MCP application entry points delegate to the package worktree manager, and `worktree_sync_tool` now passes the paired resolution input. [65]

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

- The current module exposes `SourceLineageEdge`, `SourceLineageRecovery`, `SourceLineageProjection` at this ownership boundary. [66]

## 260821-DAGQC-L2 Typed Quality Result

`WorktreeCloseoutResponse.code_quality_gate` and `WorktreeIntegrateResponse.quality_gate` now share
the strict `QualityGateResult`. This closes the former open mapping, retains both the stable wrapper
`reportPath` and optional immutable `publishedResultPath`, and gives memory policy/cap their exact
public types. The surrounding command envelopes remain flexible for unrelated operation data.

## MCAR-L03 Closeout Pair Projection

Closeout preview and apply schemas now declare the exact pair plus bounded pair-refusal fields and
repair arguments. The fields are scoped to closeout responses rather than being generalized to
unrelated worktree operations.

## 260831-CCR-L15 Status-Wait Wire Response

`WorktreeStatusWaitResponse` (operation literal `worktree_status_wait`) carries
the typed `outcome` (`LifecycleWaitOutcome`), optional `operationKind`,
`successorGeneration`, `meaningfulRevision`, `timeoutSeconds` /
`elapsedSeconds`, the projected `lifecycleOperation` snapshot, and opaque
`nextArgs`. It never carries an operation key, PID, or worker/queue/gate authority, and
on timeout returns the unchanged snapshot and cursor without claiming failure. The module now
imports `LifecycleOperationKind` and `LifecycleWaitOutcome` for the vocabulary.

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

`IntegrationStatus` gained a fourth member, `checkpointed` cit:([`IntegrationStatus`], mcp/src/agents_remember/models/worktree.py:44-44). It names the state a series
master enters when its accumulated line has landed into its super branch **and the master stays
open**. Before it existed, a partially landed master had to report `not-started` — "nothing of mine
has left" — while its content was already upstream, and that is exactly the state that made a
partial master's retirement look safe. The producer is
`worktrees/modules/landing_record.py::record_landed_integration`, which writes `checkpointed` for a
checkpoint and `completed` + `cleanup="pending"` for a final landing
cit:([`record_landed_integration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:36-66).
Because `worktrees/worktree_contract.py` derives `VALID_INTEGRATION_STATUSES` from this alias, the
new member is immediately readable and writable on the persisted contract rather than a value the
read path would reject.

**`WorktreePhase` deliberately did not gain a member for the checkpoint state.** A checkpointed
contract projects through the existing `worktree-started` phase
cit:(["if contract.integration_status == \"checkpointed\":"], mcp/src/agents_remember/worktrees/modules/guidance.py:340-340).
`WorktreePhase` is a closed `Literal` cit:([`WorktreePhase`], mcp/src/agents_remember/models/worktree.py:46-55) whose members the dashboard mirrors at five files / six sites
cit:([`LIFECYCLE_PHASES`], dashboard/src/panels/EngineRoom.tsx:59-66): `EngineRoom.tsx:59-66`
(`LIFECYCLE_PHASES`, `"integration-pending"` at `:63`), `BootTimeline.tsx:88` and `:110`,
`useEngineTimeline.ts:41`, `buildEngineRoomModel.ts:16` (`PHASE_ORDER`) and `geometry.ts:218`
(`LANDING_PHASES`). A ninth member would therefore be a
cross-codebase change, and a series that is still working is honestly `worktree-started`; the
checkpoint truth rides in the guidance summary instead. Do not add a member for it here.

The declaration site in the table above is this file, not `worktree_contract.py`: all the shared
lifecycle vocabularies that card lists are declared here cit:([`WorkflowKind`, `HumanReviewStatus`, `CloseoutStatus`, `IntegrationStatus`, `CleanupStatus`], mcp/src/agents_remember/models/worktree.py:35-35; mcp/src/agents_remember/models/worktree.py:36-36; mcp/src/agents_remember/models/worktree.py:37-37; mcp/src/agents_remember/models/worktree.py:44-44; mcp/src/agents_remember/models/worktree.py:45-45)
(`MemoryMode` is imported from the kernel and re-exported) and imported back by
`worktrees/worktree_contract.py` cit:(["from agents_remember.models.worktree import ("], mcp/src/agents_remember/worktrees/worktree_contract.py:23-23), which only derives the runtime `VALID_*` frozensets from
them.

`WorktreeCheckpointLandingResponse` (operation literal `worktree_checkpoint_landing`) declares the
checkpoint landing evidence cit:([`WorktreeCheckpointLandingResponse`], mcp/src/agents_remember/models/worktree.py:540-544): `integrationStrategy`, `integratedCodeCommit`,
checkpoint landing evidence cit:([`WorktreeCheckpointLandingResponse`], mcp/src/agents_remember/models/worktree.py:540-544): `integrationStrategy`, `integratedCodeCommit`,
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
cit:([`WorktreePauseResponse`], mcp/src/agents_remember/models/worktree.py:547-556) is the stop's wire envelope. It declares exactly one
cit:([`WorktreePauseResponse`], mcp/src/agents_remember/models/worktree.py:547-556) is the stop's wire envelope. It declares exactly one
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
cit:([`NextTool`], mcp/src/agents_remember/models/worktree.py:65-87) (the literal sits at `:75`, after
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
`worktrees/modules/guidance.py` now routes `closeout-completed` to this tool (action `validate`, with
the contract's canonical `caller`) whenever the leaf's authority is published.

**`NextOperation` was deliberately NOT widened a third time.** The move is still
`request_integration_decision`; the validation is its **precondition**, not a new lifecycle phase, so
adding a member would put a non-phase value into the set `WorktreeSummary` and the context packet
claim to report — the same reasoning the L34 section above records for the checkpoint tool.

The produced == declared invariant holds in both directions here: the guidance machine emits the name
and the literal declares it, and `_require_registered_public_next_tool` still admits it because
`curator_coherence` is a registered public tool.

## 260831-LOCR-L32 The Next-Move Triple Is Typed And Enforced

`WorktreeCommandResponse` declares `nextAction` / `nextTool` / `nextArgs`
cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-400), and
`_require_registered_public_next_tool`
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442)
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442)
cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-400), and
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

### Still Not Fixed

`WorktreeLegacyOperationResponse` is declared (L578) but unregistered — no tool maps to it. Noted, not
part of this leaf.


## 260918-TSIP-L4 — The Release Fact, And `nextTool`'s Fourth Successor

Two changes, both in the terminal-worktree contract.

**`AtomicSeriesActivationReleaseFact` is new** (**`:181-201`**, a `StrictResponseModel` with
`state: Literal["vacant", "already-vacant", "different-selection-preserved",
"unreadable-preserved", "release-failed"]` plus the optional `errorType`/`detail` triple). It is
produced by `with_terminal_atomic_series_release`
(`worktrees/activation/atomic_series_activation_terminal.py:36,64`) on every terminal series
operation. Declaring it beside `AtomicSeriesActivationFact` is what lets
`LifecycleFinalizeTaskResponse` stay inside its own contract on the
`activation-release-blocked` arm, where the bridge payload is spread whole.

**This insertion moved every line from the old `:181` down by `+23`** (and from the old `:493`
down by `+29`, after the second hunk) — `AtomicSeriesAdmissionActivation` `181 → 204`,
`contractFingerprint`'s admission-envelope field `211 → 234`, `nextAction`'s
`Literal["developer-decision"]` `278 → 301`, `WorktreeCommandResponse` `290 → 313`,
`WorktreeStatusResponse` `376-379 → 399-402`, `WorktreeCheckpointLandingResponse`
`459-463 → 482-486`, `WorktreeRecordLandingResponse` `478-482 → 501-505`, `paused`
`475 → 498`, `AtomicSeriesAdmission` `182-195 → 205-218`.

**`WorktreeOperationControlResponse.nextTool` is widened to its fourth reachable successor**
(**`:514-521`**, `"worktree_closeout_preview"`). The producer already emitted it —
`worktrees/integration/lifecycle/lifecycle_operations.py:498,508` set
`next_tool="worktree_closeout_preview"` — while the model's `Literal` admitted only three values,
so the response failed validation on the path that produces it. The `nextAction` literal beside it
is deliberately **not** widened, and `_require_registered_public_next_tool` (**`:379-387`**), which
refuses a next move outside `PUBLIC_TOOLS`, is unchanged.

## Governing Overview

[governing overview](overview.md)
