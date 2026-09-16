# mcp/src/agents_remember/models/worktree.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/worktree.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Owning overview](overview.md)

## Purpose

`worktree.py` defines context-packet worktree summaries, public worktree tool response envelopes,
and the closed wire vocabulary for resumable sync control, phases, sides, and stable journal
projection.

## Code Commentary

### Logic

`WorktreeCheckpointLandingResponse` carries `integrationStrategy`, `integratedCodeCommit`,
and `integratedMemoryContentCommit`. It has no integrated-ledger field; the response names the
two real branch outputs of the checkpoint. Cache refresh does not add a commit identity to this
wire contract, and stop-only pause remains a separate response.

cit:([`WorktreeSummary`], mcp/src/agents_remember/models/worktree.py:233-287) is the strict context-packet shape for the
`c-09-git-worktree-manager` lifecycle. Its vocabulary fields are typed, and
**since 260731-EFA-L4 every shared lifecycle vocabulary is imported from the
module that produces it; only `WorktreeState` remains local** cit:([`WorktreeState`], mcp/src/agents_remember/models/worktree.py:230-230). `WorktreeSummary` itself is declared at
cit:([`WorktreeSummary`], mcp/src/agents_remember/models/worktree.py:233-287). The command response models
remain flexible because worktree service results can carry operation-specific
planning and closeout fields.

### Where each vocabulary is declared

| Field | Alias | Declared in |
| --- | --- | --- |
| `workflowKind` | `WorkflowKind` = `chat-task \| light-task` | this file L29 |
| `memoryMode` | `MemoryMode` = `internal \| external \| disabled` | imported from the kernel (L9) and re-exported here |
| `humanReviewStatus` | `HumanReviewStatus` = `pending-review \| approved` | this file L30 |
| `closeoutStatus` | `CloseoutStatus`, imported **as `LifecycleStatus`** (the published wire name) = `not-started \| completed` | this file L31-L32 |
| `integrationStatus` | `IntegrationStatus` = `not-started \| completed \| blocked \| checkpointed` | this file L38 |
| `cleanup` | `CleanupStatus` = `pending \| completed \| abandoned \| reopened` | this file L39 |
| `phase` | `WorktreePhase` (8 members) | this file L40 |
| `nextOperation` | `NextOperation` (7 members) | this file L50 |
| `nextTool` | `NextTool` (7 members) | this file L59 |
| `state` | `WorktreeState` — the ONE alias still declared here | this file L229 |

Ranges in this table were re-derived at 260831-LOCR-L36: the contract-scoped activation re-key
removed one name from the `models.structural.atomic_series_activation` import above the vocabulary
block and deleted the admission-blocking model below it, so every alias after the import shifted
back up by one and `WorktreeState` moved from L234 to L229.

The next-move triple is **not** a vocabulary alias and does not appear above. It is declared on the
command envelope — `nextAction: str | None`, `nextTool: str | None`, `nextArgs: dict[str, Any] | None`
at L326-L328 — with the membership validator at L355-L364. `WorktreeSyncResponse` (`nextTool` at
L420) and `WorktreeOperationControlResponse` (`nextTool` at L479-L481) narrow it further.

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
cit:([`_project_terminal_contract_status`], mcp/src/agents_remember/application/worktree_status.py:377-419),
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
cit:(["\"worktree_status\": WorktreeStatusResponse"], mcp/src/agents_remember/models/tools/tool_registry.py:185-185;
mcp/src/agents_remember/models/worktree.py:375-378). Resolving down through
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
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:356-365), a
`@field_validator("nextTool")` raising `nextTool must name a registered public tool; <value> is not in
PUBLIC_TOOLS`. `None` still passes, and `WorktreeSyncResponse` / `WorktreeOperationControlResponse`
narrow `nextTool` further exactly as they did before.

*`PUBLIC_TOOLS` had to move for this to be expressible.* The validator needs the roster, and
`models/worktree.py` may not import `mcp` (`layers.toml` ranks models = 2, mcp = 22). The tuple's one
definition is now the zero-import leaf
`agents_remember/models/tools/public_roster.py`
cit:([`PUBLIC_TOOLS`], mcp/src/agents_remember/models/tools/public_roster.py:22-86), imported here at
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
  cit:(["developer-decision"], mcp/src/agents_remember/models/worktree.py:278-278), and
  `WorktreeSummary` is never on this path — it is constructed only inside `worktree_status_packet`'s
  own helpers for the `context_packet` surface (`application/worktree_status.py:79`, `:120`, `:199`,
  `:242`). Its single-value literal is honest where it lives.

**The branch is reachable, and it is now covered.** The terminal archive and receipt are published
(locator → `terminal-archived`) *before* the surviving contract is amended: `cleanup.py` completes its
guard around `amend_contract(contract, ContractCells(cleanup="completed"))`
cit:(["amend_contract(contract, ContractCells(cleanup=\"completed\"))"], mcp/src/agents_remember/worktrees/modules/cleanup.py:933-933),
and `abandon.py` does the same around `cleanup="abandoned"`
cit:(["amend_contract(contract, ContractCells(cleanup=\"abandoned\"))"], mcp/src/agents_remember/worktrees/modules/abandon.py:347-347).
Both writes are wrapped in `guard.complete(..., rollback_publish=...)`, so a **failed publication
deliberately restores the archived contract while the locator stays `terminal-archived`** — exactly
the state the projector serves, `"terminal-archive-ready"`
cit:(["terminal-archive-ready"], mcp/src/agents_remember/application/worktree_status.py:384-384).
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
`RecoveryOperation` / `RecoveryTool` aliases (cit:([`RecoveryOperation`, `RecoveryTool`], mcp/src/agents_remember/worktrees/modules/guidance.py:36-47; mcp/src/agents_remember/worktrees/modules/guidance.py:48-53)) precisely so
a wider `NextOperation` cannot put "requires developer approval" back into the set
the context packet's `nextOperation` claims to be.

`nextRequiredArgs` (cit:([`nextRequiredArgs`], mcp/src/agents_remember/models/worktree.py:265-265)) is **omitted rather than `[]`** when there is
nothing to supply. `next_guidance` writes the key only when the next call needs a
caller-supplied argument; the projection now reports what the producer said
instead of substituting a value for it. This is a stated wire change: measured
across the 213 contracts, 48 responses that previously carried
`"nextRequiredArgs": []` now omit the key, and it stays omitted. An absent
`nextRequiredArgs` means what the empty list meant — the next call needs nothing
beyond `nextArgs` — and there is no third state to confuse it with. The same rule
now covers `nextTool` and `nextArgs`, where the old substitution had put an
un-declarable `""` on the wire.

`unknownContractCells: list[str] | None` (cit:([`unknownContractCells`], mcp/src/agents_remember/models/worktree.py:270-270)) is new. It is present only
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
  cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:323-323) and
  `_require_registered_public_next_tool`
  cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:356-365)
  refuses a value outside `PUBLIC_TOOLS`. The rule
  is **per surface, deliberately**: the `task_doc` surface may name the registered-but-non-public
  `session_retire` (`TaskDocResponse` is not a `WorktreeCommandResponse`), so do not widen
  `PUBLIC_TOOLS` and do not special-case that name here. `WorktreeSummary` is never on this path and
  its single-value `nextAction` literal stays honest there.
- **`PUBLIC_TOOLS` is read from its `models` leaf, never imported from `mcp`.** `layers.toml` ranks
  models = 2 and mcp = 22, so `models → mcp` is a violation; a function-local import trips
  `ruff PLC0415` and suppressions are forbidden. The tuple's one definition is
  `models/tools/public_roster.py`
  cit:([`PUBLIC_TOOLS`], mcp/src/agents_remember/models/tools/public_roster.py:22-86). Do not move it
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

## Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external domain source applies. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Checkpoint responses record only the real integrated code and memory-content commits. | L459-L463 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| Sync control, side, phase, operation-state, and strict projection shapes are declared together. | L79-L79; L80-L80; L81-L81; L82-L91; L92-L101; L136-L149; L152-L167 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| Series status and command responses carry optional activation facts and bounded admission evidence. | L170-L178; L206-L218; L233-L287; L290-L365 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The activation fact and the admission envelope are keyed by the addressed contract's `contractFingerprint`, not by a source pair; the nested activation snapshot is the only activation evidence. | L206-L218; L181-L193 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The deleted blocking vocabulary left no field behind: the admission envelope declares neither `classification`, `blocking` nor a source pair. | L206-L218 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The sync response declares recovery guidance without exposing a public operation id. | L415-L426 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The record-landing envelope declares the landing evidence and its operation literal. | L478-L482 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The checkpoint-landing envelope declares the two output commits an unfinished master landed and its operation literal. | L459-L463 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The pause envelope declares the stop's one own field, `paused`, and inherits the ordinary command envelope; only the route that releases the selection claims it. | L466-L475 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The `checkpointed` member the checkpoint writer records and the persisted-contract vocabulary derives. | L38-L38 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The two `NextOperation`/`NextTool` members the L31 leaf moved: `finalize` in place of `retry_cleanup`, and `lifecycle_finalize_task` added. | L50-L58; L59-L74 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The L34 addition: `worktree_checkpoint_landing` joined `NextTool` (`:69`) while `NextOperation` was deliberately left at seven members. | L59-L74; L50-L58 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The producer that keeps `NextTool."worktree_cleanup"` live after `guidance.py` stopped emitting it, and the closed two-member cleanup-operation vocabulary it copies from. | worktree_status.py: L377-L419; enclosure.py: L14-L14 | [mcp/src/agents_remember/application/worktree_status.py](mcp/src/agents_remember/application/worktree_status.py); [mcp/src/agents_remember/models/lifecycles/enclosure.py](mcp/src/agents_remember/models/lifecycles/enclosure.py) |
| The response registry selects WorktreeStatusResponse and the shared response validator validates its envelope. | tool_registry.py: L185-L185; tool_response.py: L23-L23; worktree.py: L376-L379 | [mcp/src/agents_remember/models/tools/tool_registry.py](mcp/src/agents_remember/models/tools/tool_registry.py); [mcp/src/agents_remember/models/tools/tool_response.py](mcp/src/agents_remember/models/tools/tool_response.py); [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The `extra="allow"` config on the flexible envelope. It is **no longer** what decides the next-move keys' fate: the three keys are declared below, so they are no longer extras. | L22-L22 | [mcp/src/agents_remember/models/base.py](mcp/src/agents_remember/models/base.py) |
| The three next-move keys declared on the command envelope, which is what stops the projector's write from riding as an undeclared extra. | L323-L323 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The membership validator that refuses a next move outside the advertised roster — the enforcement half of the invariant, and the reason the roster had to move into `models`. | L356-L365 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The advertised public roster this model reads, in its zero-import `models` leaf (the tuple's single definition; `mcp/tools/base.py` re-exports it). | public_roster.py: L22-L22; base.py: L19-L19 | [mcp/src/agents_remember/models/tools/public_roster.py](mcp/src/agents_remember/models/tools/public_roster.py); [mcp/src/agents_remember/mcp/tools/base.py](mcp/src/agents_remember/mcp/tools/base.py) |
| The registered-but-deliberately-non-public name that must stay outside the worktree invariant, and the `task_doc` surface that legitimately emits it (its `nextTool` is a plain `str \| None`, on a class that is not a `WorktreeCommandResponse`). | tool_registry.py: L134-L134; L158-L158; task_doc.py: L115-L190 | [mcp/src/agents_remember/models/tools/tool_registry.py](mcp/src/agents_remember/models/tools/tool_registry.py); [mcp/src/agents_remember/models/task_doc.py](mcp/src/agents_remember/models/task_doc.py) |
| The executor for the declared-and-enforced next move: it reaches the archive-ready state through real production calls for both cleanup verbs, binds the emitted args to the real tool signature, and drives the validator in both directions. | L192-L219; L231-L244; L247-L278 | [mcp/tests/test_worktree_status_terminal_next_tool.py](mcp/tests/test_worktree_status_terminal_next_tool.py) |
| The `nextAction` literal this file **does** declare, and which stays honest because its only producer hard-codes it — do not widen it. | L278-L278 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |
| The reachable terminal state the projector serves once a failed contract amendment is rolled back while the locator stays `terminal-archived`. | L384-L384 | [mcp/src/agents_remember/application/worktree_status.py](mcp/src/agents_remember/application/worktree_status.py) |
| The two guarded contract amendments whose rolled-back publication produces that state, for cleanup and abandon respectively. | cleanup.py: L933-L933; abandon.py: L347-L347 | [mcp/src/agents_remember/worktrees/modules/cleanup.py](mcp/src/agents_remember/worktrees/modules/cleanup.py); [mcp/src/agents_remember/worktrees/modules/abandon.py](mcp/src/agents_remember/worktrees/modules/abandon.py) |
| The module that should enforce produced == declared for `NextTool` and currently has **zero** test bodies — only this docstring, helpers and "moved verbatim" breadcrumbs remain. | L1-L1 | [mcp/tests/test_wire_vocabulary_exhaustiveness.py](mcp/tests/test_wire_vocabulary_exhaustiveness.py) |
| The sole writer of `WorktreeSummary`: `worktree_status_packet` returns the MODEL now, and `_summary_from_status_payload` projects field by field, reading optional next and activation fields without inventing values. | L65-L152; L217-L281 | [mcp/src/agents_remember/application/worktree_status.py](mcp/src/agents_remember/application/worktree_status.py) |
| The six persisted contract vocabularies (`WorkflowKind` … `CleanupStatus`) with their `VALID_*` frozensets, the `ContractCells` typed write record and `amend_contract`. | L70-L70; L71-L71; L72-L72; L73-L73; L74-L74; L75-L75; L180-L194; L197-L225 | [mcp/src/agents_remember/worktrees/worktree_contract.py](mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The guidance state machine imports and writes `WorktreePhase`, `NextOperation` and `NextTool` (declared in this model since L9), plus the separate `RecoveryOperation`/`RecoveryTool` that deliberately do NOT reach this model. | L9-L9; L36-L47; L48-L53 | [mcp/src/agents_remember/worktrees/modules/guidance.py](mcp/src/agents_remember/worktrees/modules/guidance.py) |
| Public worktree MCP application entry points delegate to the package worktree manager. | L277-L300 | [mcp/src/agents_remember/application/worktree_tools.py](mcp/src/agents_remember/application/worktree_tools.py) |

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `SourceLineageEdge`, `SourceLineageRecovery`, `SourceLineageProjection` at this ownership boundary. | L104-L116; L119-L124; L127-L133 | [mcp/src/agents_remember/models/worktree.py](mcp/src/agents_remember/models/worktree.py) |

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

`IntegrationStatus` gained a fourth member, `checkpointed` cit:([`IntegrationStatus`], mcp/src/agents_remember/models/worktree.py:38-38). It names the state a series
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
cit:(["if contract.integration_status == \"checkpointed\":"], mcp/src/agents_remember/worktrees/modules/guidance.py:298-298).
`WorktreePhase` is a closed `Literal` cit:([`WorktreePhase`], mcp/src/agents_remember/models/worktree.py:40-49) whose members the dashboard mirrors at five files / six sites
cit:([`LIFECYCLE_PHASES`], dashboard/src/panels/EngineRoom.tsx:59-66): `EngineRoom.tsx:59-66`
(`LIFECYCLE_PHASES`, `"integration-pending"` at `:63`), `BootTimeline.tsx:88` and `:110`,
`useEngineTimeline.ts:41`, `buildEngineRoomModel.ts:16` (`PHASE_ORDER`) and `geometry.ts:218`
(`LANDING_PHASES`). A ninth member would therefore be a
cross-codebase change, and a series that is still working is honestly `worktree-started`; the
checkpoint truth rides in the guidance summary instead. Do not add a member for it here.

The declaration site in the table above is this file, not `worktree_contract.py`: all the shared
lifecycle vocabularies that card lists are declared here cit:([`WorkflowKind`, `HumanReviewStatus`, `CloseoutStatus`, `IntegrationStatus`, `CleanupStatus`], mcp/src/agents_remember/models/worktree.py:29-29; mcp/src/agents_remember/models/worktree.py:30-30; mcp/src/agents_remember/models/worktree.py:31-31; mcp/src/agents_remember/models/worktree.py:38-38; mcp/src/agents_remember/models/worktree.py:39-39)
(`MemoryMode` is imported from the kernel and re-exported) and imported back by
`worktrees/worktree_contract.py` cit:(["from agents_remember.models.worktree import ("], mcp/src/agents_remember/worktrees/worktree_contract.py:19-19), which only derives the runtime `VALID_*` frozensets from
them.

`WorktreeCheckpointLandingResponse` (operation literal `worktree_checkpoint_landing`) declares the
checkpoint landing evidence cit:([`WorktreeCheckpointLandingResponse`], mcp/src/agents_remember/models/worktree.py:459-463): `integrationStrategy`, `integratedCodeCommit`,
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
cit:([`WorktreePauseResponse`], mcp/src/agents_remember/models/worktree.py:466-475) is the stop's wire envelope. It declares exactly one
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
cit:([`NextTool`], mcp/src/agents_remember/models/worktree.py:59-74) (the literal sits at `:70`, after
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

## 260831-LOCR-L32 The Next-Move Triple Is Typed And Enforced

`WorktreeCommandResponse` declares `nextAction` / `nextTool` / `nextArgs`
cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:323-323), and
`_require_registered_public_next_tool`
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:356-365)
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

`WorktreeLegacyOperationResponse` is declared (L492) but unregistered — no tool maps to it. Noted, not
part of this leaf.


## Cross-Repo References

No separate cross-repository implementation claim is made.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external implementation source applies. | N/A | N/A |

## Update History

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Removed the integrated-ledger identity from the documented checkpoint response. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.

- 2026-09-14T15:05+02:00 — No content impact: mechanical citation re-derivation after the
  260913-LCA-L8 change set shifted the two guarded contract amendments — `cleanup.py:925-930` →
  `929-934` (the `TerminalResult` import line plus the `_cleanup_outputs_result` rewrite) and
  `abandon.py:344-349` → `347-352` (the `TerminalResult` import line). Both ranges were re-read at
  their new positions, where each `amend_contract(contract, ContractCells(cleanup=...))` statement
  and its `guard.complete(...)` publication block still sit; the cited constructs and their meanings
  are unchanged. History entries below keep their as-of values.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "TOOL_RESPONSE_MODELS[tool_name].model_validate(payload)"; "\"worktree_status\": WorktreeStatusResponse" repointed to mcp/src/agents_remember/models/tools/tool_response.py:23-23; mcp/src/agents_remember/models/tools/tool_registry.py:185-185. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: recorded `WorktreePauseResponse` (operation literal
  `worktree_pause`, `paused: bool = False`, everything else inherited from `WorktreeCommandResponse`)
  and why its one field is the design: only the route that releases the atomic-series selection
  claims `paused`, so a publication that moved refs cannot report a stop. Recorded that a successful
  pause omits `nextStep` rather than setting it to `None`, and added the reference row. Reference
  health on the neighbouring envelopes in this revision: `WorktreeCheckpointLandingResponse` at
  `459-466`, `WorktreeRecordLandingResponse` at `479-483`. The new class is additive, so no earlier
  citation range in this card moved. Verification metadata remains closeout-owned; no acceptance
  claim.
- 2026-09-13T17:46+02:00 — LOCR-L36 pause/publication correction. The `NextTool."worktree_checkpoint_landing"` declaration comment was reworded: the intent that carries a finished master to `worktree_integrate` carries an **unfinished** one to the checkpoint, which is a partial **publication** rather than the pause — pausing a master moves no ref and is no integration decision at all, so the vocabulary is deliberately not widened for it either. The card's prose and the "checkpoint-landing envelope" row no longer call the landed master "paused". The +1 line this edit added above the roster shifted five citations by one: `WorktreeState` 229→230, `"developer-decision"` 277→278, `nextRequiredArgs` 264→265, `unknownContractCells` 269→270, the checkpoint envelope 458-463→459-466, and the next-move triple comment 322-322→323-323 in the sibling cards that cite it; the `NextTool` literal itself moved 69→70. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T14:21:37+02:00 — LOCR-L36 contract-scoped activation re-key: corrected the activation/admission response vocabulary. `AtomicSeriesActivationFact` and `AtomicSeriesAdmissionActivation` now carry `contractFingerprint` (not `sourcePairFingerprint`), `AtomicSeriesAdmission` lost `classification`, `sourcePair`, `sourcePairFingerprint` and `blocking` and gained `contractFingerprint`, and the `AtomicSeriesAdmissionBlocking` model no longer exists — so the CCR-R25 paragraph, the invariants, and the reference rows were re-worded to say that selection evidence is per contract and that a foreign live master is never a blocker or retry precondition. Re-derived the vocabulary-declaration table (the re-key removed one name from the activation import above the block and the blocking model below it, so every alias shifted back up by one and `WorktreeState` moved from L234 to L229) and re-verified every citation row in this card against the 514-line source: `WorktreeSummary` 232-286, `WorktreeState` 229, the next-move triple 322-328, `_require_registered_public_next_tool` 355-364, `NextOperation` 50-58, `NextTool` 59-73, `SyncOperationProjection`/`SyncResolutionProjection` 135-166, `WorktreeSyncResponse` 414-425, `WorktreeCheckpointLandingResponse` 458-463, `WorktreeRecordLandingResponse` 466-470, `WorktreeStatusResponse` 375-378, `IntegrationStatus` 38, `WorktreePhase` 40-49, `SourceLineageEdge`/`Recovery`/`Projection` 103-115 / 118-123 / 126-132, and `worktree_status_tool` 277-300. No verification stamp advanced.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:50+00:00 — 260831-LOCR-L34: `NextTool` gained its seventh member,
  `worktree_checkpoint_landing` (`:70`), because the repaired checkpoint route's preview and its
  `integration-ref-race` refusal both emit it, and it is a registered public tool. Recorded that
  `NextOperation` was deliberately **not** widened — pausing a master is the existing
  `request_integration_decision` intent, not a phase — and added the matching
  reviewed-and-deliberately-not-changed row. Corrected the member count in the vocabulary table
  (6 → 7) and the `NextTool` range (60-67 → 60-74). Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `WorktreeRecordLandingResponse` repointed to mcp/src/agents_remember/models/worktree.py:478-482. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `WorktreeCheckpointLandingResponse` repointed to mcp/src/agents_remember/models/worktree.py:470-475. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "developer-decision" repointed to mcp/src/agents_remember/models/worktree.py:289-289. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `WorktreeState` repointed to mcp/src/agents_remember/models/worktree.py:241-241. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "developer-decision" repointed to mcp/src/agents_remember/models/worktree.py:289-289. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `nextRequiredArgs` repointed to mcp/src/agents_remember/models/worktree.py:276-276. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `unknownContractCells` repointed to mcp/src/agents_remember/models/worktree.py:281-281. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `WorktreeCheckpointLandingResponse` repointed to mcp/src/agents_remember/models/worktree.py:470-475. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: **the terminal next-move seam is now typed and
  enforced, and the card's account of it is corrected.** Declared `nextAction` / `nextTool` /
  `nextArgs` on `WorktreeCommandResponse` plus the `PUBLIC_TOOLS` membership validator
  `_require_registered_public_next_tool`; replaced the card's "undeclared pair / missing
  types / recommended fix — recorded, not implemented" account with the implemented one, recorded that
  the roster had to move to `models/tools/public_roster.py` for the check to be expressible, recorded
  the per-surface rule and the explicit instruction not to widen `PUBLIC_TOOLS` for `session_retire`,
  recorded the three deliberate non-changes (`NextTool` did not gain `worktree_abandon`; the flexible
  envelope was not narrowed; `WorktreeSummary.nextAction` was not widened), noted that
  `normalize_closeout_input` / `worktree closeout` are `CloseoutCorrectedCall.tool` rather than
  `nextTool`, and noted the still-unregistered `WorktreeLegacyOperationResponse`. Re-derived the
  vocabulary declaration table (one added import at L27 shifted every alias by one) and added five
  reference rows. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `WorktreeSyncResponse` repointed to mcp/src/agents_remember/models/worktree.py:419-430. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `WorktreeRecordLandingResponse` repointed to mcp/src/agents_remember/models/worktree.py:471-475. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `WorktreeCheckpointLandingResponse` repointed to mcp/src/agents_remember/models/worktree.py:463-468. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `IntegrationStatus` repointed to mcp/src/agents_remember/models/worktree.py:39-39. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "developer-decision" repointed to mcp/src/agents_remember/models/worktree.py:282-282. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `WorktreeState` repointed to mcp/src/agents_remember/models/worktree.py:234-234. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "developer-decision" repointed to mcp/src/agents_remember/models/worktree.py:282-282. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `nextRequiredArgs` repointed to mcp/src/agents_remember/models/worktree.py:269-269. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `unknownContractCells` repointed to mcp/src/agents_remember/models/worktree.py:274-274. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `IntegrationStatus` repointed to mcp/src/agents_remember/models/worktree.py:39-39. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `WorktreeCheckpointLandingResponse` repointed to mcp/src/agents_remember/models/worktree.py:463-468. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:12+02:00 — **Final correction: the seam accounts in the two entries below are
  superseded by the verified mechanism.** An earlier revision of this card claimed the projector's
  write violated `WorktreeSummary`'s typed `nextAction` on a strict model; that is false, because
  `WorktreeSummary` is never on that path. The settled account — `WorktreeStatusResponse` inherits
  `extra="allow"` and declares none of the three keys, so the pair passes through verbatim and
  unchecked; `WorktreeSummary.nextAction` is honest where it lives; the branch is reachable via the
  rolled-back contract amendment that leaves the locator `terminal-archived`; the emitted guidance is
  correct and retrying the named tool resumes; only the typing is missing; and
  `test_wire_vocabulary_exhaustiveness.py` has no test bodies left to enforce the invariant — is in
  the Code Commentary, the invariant list and the 20:02 entry. I verified that mechanism statically
  against the leaf: the single `model_validate` site, the registry row, the `extra="allow"` config,
  zero `nextAction`/`nextTool`/`nextArgs` declarations on the envelope, the `terminal-archive-ready`
  projector branch, both guarded amendments, and the absence of `def test_` in the exhaustiveness
  module. Verified stamps untouched; no acceptance claim.
- 2026-09-12T20:02+02:00 — **Seam mechanism settled (supersedes the 19:50 wording and the earlier
  "strict model / type violation" account).** `worktree_status` validates at exactly one place,
  `TOOL_RESPONSE_MODELS[tool_name].model_validate(payload)` (`models/tools/tool_response.py:23`), and
  the registry maps it to `WorktreeStatusResponse` (`models/tools/tool_registry.py:184`,
  `models/worktree.py:335`), which resolves down through `WorktreeCommandResponse` →
  `FlexibleToolResponse` → `FlexibleResponseEnvelope` → `FlexibleResponseModel` with
  `extra="allow"` (`models/base.py:19-22`) and declares **none** of `nextAction` / `nextTool` /
  `nextArgs`. So the projector's pair passes through **verbatim and unchecked** — no error — and
  `WorktreeSummary` is never on that path (constructed only in `worktree_status_packet`'s helpers at
  `application/worktree_status.py:79, 120, 199, 242`), so its single-value `nextAction` literal at
  `models/worktree.py:281` is honest where it lives. The branch is reachable — the terminal archive
  publishes before the contract amendment, and both `cleanup.py:925-930` and `abandon.py:344-349` wrap
  the amendment so a failed publication rolls the contract back while the locator stays
  `terminal-archived`, which the projector reports as `terminal-archive-ready`
  (`worktree_status.py:384`) — and the emitted guidance is **correct**: the pair is emitted verbatim,
  `nextArgs` match the real tool signatures, and retrying the named tool resumes. Recorded the
  recommended fix (declare the three keys loosely on `WorktreeCommandResponse`; do not add
  `worktree_abandon` to `NextTool`; do not widen `WorktreeSummary.nextAction`; do not narrow the
  flexible envelope; the right invariant is that every emitted `nextTool` is a registered public
  tool) and the related gap that `test_wire_vocabulary_exhaustiveness.py` retains **zero** `def
  test_` bodies, leaving produced == declared unenforced. Verification metadata remains
  closeout-owned; no acceptance claim, and no terminal-status behavior was changed.
- 2026-09-12T17:57:35+00:00: Generated citation repair: `WorktreeState` repointed to mcp/src/agents_remember/models/worktree.py:233-233. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: `nextRequiredArgs` repointed to mcp/src/agents_remember/models/worktree.py:268-268. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: `unknownContractCells` repointed to mcp/src/agents_remember/models/worktree.py:273-273. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: "if contract.integration_status == \"checkpointed\":" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:308-308. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T19:50+02:00 — 260831-LOCR-L31 cleanup-vocabulary move: `NextOperation` dropped
  `retry_cleanup` (whose only writer, `guidance._post_integration_phase`'s `cleanup-pending` branch,
  now routes finalization) and gained `finalize`, so the member count stays seven; `NextTool` gained
  `lifecycle_finalize_task` and is now six. Recorded **`NextTool."worktree_cleanup"` as deliberately
  kept rather than orphaned** — its remaining producer is
  `application/worktree_status.py::_project_terminal_contract_status`, which copies
  `TerminalCleanupOperation` (`worktree_cleanup` | `worktree_abandon`) into `nextTool` — and recorded
  the seam that write opens; **its mechanism is settled in the 20:02 entry above, which supersedes
  this sentence's original wording** (the write lands on the flexible `WorktreeStatusResponse`
  envelope, not on `WorktreeSummary`). Added two invariants and four reference rows. Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T05:05+02:00 — 260831-LOCR-L30 mirror-list completeness: the "no new `WorktreePhase`
  member" note named three dashboard mirrors where there are six. Replaced it with the full
  five-file / six-site list (`EngineRoom.tsx:59-66` `LIFECYCLE_PHASES` with `"integration-pending"`
  at `:63`, `BootTimeline.tsx:88` and `:110`, `useEngineTimeline.ts:41`, `buildEngineRoomModel.ts:16`,
  `geometry.ts:218`). Content change, not a range repoint; verification metadata remains
  closeout-owned.
- 2026-09-12T04:10+02:00 — 260831-LOCR-L30 follow-up: recorded that `WorktreePhase` deliberately
  gained no member for the checkpoint state — a checkpointed contract projects as the existing
  `worktree-started` phase because the alias is a closed `Literal` mirrored by the dashboard, and the
  checkpoint truth rides in the guidance summary. Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-12T01:06:15+00:00: Generated citation repair: `WorkflowKind`; `HumanReviewStatus`; `CloseoutStatus`; `IntegrationStatus`; `CleanupStatus` repointed to mcp/src/agents_remember/models/worktree.py:29-29; mcp/src/agents_remember/models/worktree.py:30-30; mcp/src/agents_remember/models/worktree.py:31-31; mcp/src/agents_remember/models/worktree.py:38-38; mcp/src/agents_remember/models/worktree.py:39-39. No content impact: mechanical anchor-range projection bound to citation source snapshot 1740540b8733028dd833a3538d739271e8925ea5f51911a0f8dcd8c49e7e1c13; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: added `checkpointed` to `IntegrationStatus` in the
  declaration table (and corrected that row's declaration site, which still named
  `worktree_contract.py`), declared `WorktreeCheckpointLandingResponse` and the four commit fields it
  publishes, and recorded why the envelope is required for the advertised tool to answer. Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T01:41:08+02:00 — 260831-LOCR-L29 public-surface repair: declared the
  `WorktreeRecordLandingResponse` envelope (`worktree_record_landing` literal, `integrationStrategy`,
  `landedCodeCommit`, `landingTargets`) for the tool that `mcp/registration/closeout.py` already
  registered, added the model-declaration/registry-pairing invariant, and added its reference row.
  The tool had been advertised while `finalize_tool_response`'s by-name registry lookup had no entry,
  so it raised instead of returning a payload. Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `ContractCells`, `VALID_CLEANUP_STATUSES`, `VALID_CLOSEOUT_STATUSES`, `VALID_HUMAN_REVIEW_STATUSES`, `VALID_INTEGRATION_STATUSES`, `VALID_MEMORY_MODES`, `VALID_WORKFLOW_KINDS`, `amend_contract` repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:179-194, mcp/src/agents_remember/worktrees/worktree_contract.py:197-225, mcp/src/agents_remember/worktrees/worktree_contract.py:70-75. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `nextRequiredArgs` repointed to mcp/src/agents_remember/models/worktree.py:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `unknownContractCells` repointed to mcp/src/agents_remember/models/worktree.py:267-267. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T15:00+02:00 — Automatic post-integration cleanup vocabulary at code commit `76ce662a`: `NextOperation` replaced `request_cleanup_decision` with `retry_cleanup` (member count unchanged at seven), and the `cleanup_question` projection key is gone. Verification metadata remains pinned because this is a targeted single-claim repair; source documentation only, no acceptance claim.
- 2026-09-11T11:04:01+02:00 — Declared `SyncResolutionProjection.wipRestore`, the parked-WIP marker `sync_transaction_results` has emitted since it introduced the parked-candidate path while `StrictResponseModel`'s `extra="forbid"` refused it, so a sync that parked a dirty leaf and needed the agent to settle the reapply failed on its own projection instead of returning the resolution (code commit `765f1743`). Citation range extended to the new class extent. Only the cut-affected claim was reconciled, so verification metadata remains pinned; source documentation only, no acceptance claim.

- 2026-09-08T16:24:06+02:00 — CCR-L38 preparation range refresh: regenerated model-side citations for the shifted lineage, summary, optional fields and sync-response definitions. This is a mechanical source-range correction; verification metadata remains closeout-owned.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: documented the typed atomic-series activation fact and bounded admission response fields added to the worktree wire models. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.

- 2026-09-05T07:08:26+00:00 — L31 final residual curation against frozen code `ea35964985f30080488270e71ac81657ac40682b`: Archived 8 historical citation wrappers as inert historical-source text under the bounded L31 ruling. Dated narrative, anchors and original coordinates remain unchanged. The recovered card carried verification commit e375f2ebdc87f6843bc76168b646d606fa79caec; this historical provenance is not a current-source claim. Current-body evidence and verification metadata are retained. This scoped repair does not promote the card's verification stamp or certify a gate.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `WorktreeSyncResponse` repointed to mcp/src/agents_remember/models/worktree.py:281-292. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `nextRequiredArgs` repointed to mcp/src/agents_remember/models/worktree.py:183-183. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `unknownContractCells` repointed to mcp/src/agents_remember/models/worktree.py:188-188. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded `WorktreeStatusWaitResponse` and its read-only wait wire shape.
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
  are now imports (historical source: ([`WorktreeSummary`, `WorktreeState`], mcp/src/agents_remember/models/worktree.py:145-145; mcp/src/agents_remember/models/worktree.py:148-198)); only historical source: ([`WorktreeState`], mcp/src/agents_remember/models/worktree.py:146-146) is still declared here, because
  `worktrees.status` is its sole writer. Added the declaration table, which also records three
  published-vocabulary changes the card had no way to state: `WorkflowKind` is now `chat-task |
  light-task` (the bare `chat`/`light` had zero occurrences across the 213 contracts and no
  writer), `CleanupStatus` gained `reopened`, and `request_commit_approval` /
  `worktree_closeout_preview` / `commit-approval-pending` left `NextOperation`/`NextTool`/
  `WorktreePhase` for the separate `RecoveryOperation`/`RecoveryTool` aliases that never reach
  this model. Recorded `nextRequiredArgs` (historical source: ([`nextRequiredArgs`], mcp/src/agents_remember/models/worktree.py:181-181)) now being OMITTED rather than `[]` — a stated
  wire change on 48 of the 213 responses — and the new `unknownContractCells` field (historical source: ([`unknownContractCells`], mcp/src/agents_remember/models/worktree.py:186-186)),
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
  are now imports (historical source: ([`WorktreeSummary`, `WorktreeState`], mcp/src/agents_remember/models/worktree.py:145-145; mcp/src/agents_remember/models/worktree.py:148-198)); only historical source: ([`WorktreeState`], mcp/src/agents_remember/models/worktree.py:146-146) is still declared here, because
  `worktrees.status` is its sole writer. Added the declaration table, which also records three
  published-vocabulary changes the card had no way to state: `WorkflowKind` is now `chat-task |
  light-task` (the bare `chat`/`light` had zero occurrences across the 213 contracts and no
  writer), `CleanupStatus` gained `reopened`, and `request_commit_approval` /
  `worktree_closeout_preview` / `commit-approval-pending` left `NextOperation`/`NextTool`/
  `WorktreePhase` for the separate `RecoveryOperation`/`RecoveryTool` aliases that never reach
  this model. Recorded `nextRequiredArgs` (historical source: ([`nextRequiredArgs`], mcp/src/agents_remember/models/worktree.py:181-181)) now being OMITTED rather than `[]` — a stated
  wire change on 48 of the 213 responses — and the new `unknownContractCells` field (historical source: ([`unknownContractCells`], mcp/src/agents_remember/models/worktree.py:186-186)),
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
