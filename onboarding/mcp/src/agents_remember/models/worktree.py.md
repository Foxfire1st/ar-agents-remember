# mcp/src/agents_remember/models/worktree.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Defines the strict public worktree response and sync projection vocabulary.

## Code Commentary

`WorktreeSummary` is the strict context-packet shape for the `c-09-git-worktree-manager` lifecycle. Its vocabulary fields are typed, and the shared wire vocabularies are declared in this module — except the memory mode, which is imported from the kernel. `WorktreeState` is the one alias still declared here. The command response models remain flexible because worktree service results can carry operation-specific planning and closeout fields.

Where each vocabulary is declared: `workflowKind` is `WorkflowKind` (`chat-task`/`light-task`); `memoryMode` is `ReadableMemoryMode` (`external`/`disabled`), imported from `kernel.memory_mode` — the readable vocabulary, not the startable one, so an existing contract that carries the removed `disabled` mode is shown as it is today; `humanReviewStatus`, `closeoutStatus` (imported as the published wire name `LifecycleStatus`), `integrationStatus` (now incl. `checkpointed`), `cleanup`, `phase` (`WorktreePhase`, 8 members), `nextOperation`, `nextTool`, and `state` (`WorktreeState`, local on purpose: `application.worktree_status` constructs this model directly and is its sole writer).

**No vocabulary is retyped here, and none is retyped elsewhere.** Every literal on the worktree models is declared in this module (see above) except the memory mode, whose one declaration lives in the kernel. Adding a member is a one-place edit; re-declaring one in a second module recreates the exact set difference that once made the packet reject most contracts on disk.

The next-move triple (`nextAction`/`nextTool`/`nextArgs`) is declared on `WorktreeCommandResponse` and enforced by membership in `PUBLIC_TOOLS`, which lives in `models` as a zero-import leaf (a `models → mcp` import would violate `layers.toml`). `WorktreeSummary.nextAction` stays a single-value literal because its one producer hard-codes `developer-decision`. Absent is the shape for `nextTool`/`nextArgs`/`nextRequiredArgs`: the projection reports what the producer wrote and never fills a hole. `unknownContractCells` is a report, not a state: it coexists with `state="active"` as notice that a cell was substituted.

`WorktreeCheckpointLandingResponse` carries `integrationStrategy`, `integratedCodeCommit`, and `integratedMemoryContentCommit` — the two real branch outputs of the checkpoint, no ledger field. `WorktreePauseResponse` declares exactly one own field, `paused`, claimed only by the route that releases the master's selection. Every advertised public worktree tool's response envelope is declared here and registered in `models/tools/tool_registry.py`.

## Evidence


- Readable mode imported from the kernel [113]


- Strict context-packet shape incl. readable `memoryMode` [114]


- State alias stays local on purpose [115]


- Checkpoint response names the two real outputs [116]


- Pause envelope claims only the stop [117]


The following source-backed definitions and producer seams retain the broader response and vocabulary account alongside the readable-mode correction; they are declarations, not evidence of an executor run.

- SourceLineageProjection carries state, summary, edges and recoveries. [118]
- SyncOperationProjection carries journal state, phase, conflicts, summary and next/cancel arguments. [119]
- SyncResolutionProjection describes agent-owned side/worktree/files and wipRestore without deciding conflict content. [120]
- SyncResolutionInput admits only its declared optional action. [121]
- WorkflowKind is the shared chat-task/light-task wire vocabulary. [122]
- The guidance module imports NextOperation, NextTool and WorktreePhase from the model and obtains guidance by calling lifecycle_guidance(contract). Recovery aliases remain separate. [123]
- TaskDocResponse is a ToolResponse rather than a WorktreeCommandResponse and declares nextTool as str or None; the worktree roster validator does not govern this class. [124]
- worktree_sync_tool admits its configured contract, delegates to the worktree manager and forwards resolution.action as resolution_action. [125]
- SourceLineageEdge, SourceLineageRecovery and SourceLineageProjection expose the typed source-lineage boundary. [126]
- WorktreeSummary is the strict context-packet shape with typed lifecycle and worktree vocabulary fields. [127]
- WorktreeState is locally declared as inactive, active, missingContract or invalidContract. [128]
- WorktreeSummary uses the declared wire vocabulary fields, including ReadableMemoryMode for persisted memory-mode reads. [129]
- The terminal-status projector distinguishes terminal-cleanup-completed from terminal-archive-ready and emits the archive cleanup operation as the next tool only when cleanup remains. [130]
- TerminalCleanupOperation is the two-member terminal-cleanup vocabulary (worktree_cleanup, worktree_abandon). [131]
- finalize_tool_response validates one declared response, applies optional caller enrichment, and counts tokens. [132]
- TOOL_RESPONSE_MODELS maps each tool name to its declared response model. [133]
- WorktreeStatusResponse carries the status operation literal with lifecycle and sync projections. [134]
- FlexibleResponseModel is the extra-allowing base class for provider-native diagnostic payloads. [135]
- The membership validator refuses a next move outside the advertised roster. [136]
- PUBLIC_TOOLS lives in models as a zero-import leaf tuple the validator reads. [137]
- WorktreeSummary.nextAction is the optional single-value developer-decision literal. [138]
- Cleanup completes the terminal guard with updated-contract publication and old-contract rollback; failed publication returns blocked evidence. [139]
- Abandon completes the terminal guard with updated-contract publication and old-contract rollback; failed publication returns abandon-blocked evidence. [140]
- The terminal-status projector distinguishes terminal-cleanup-completed from terminal-archive-ready and emits the archive cleanup operation as the next tool only when cleanup remains. [141]
- The wire-vocabulary module retains its R10 doctrine docstring; this range is doctrine text, not proof that any executor ran. [142]
- RecoveryOperation is a separate guidance recovery vocabulary, not the context-facing NextOperation alias. [143]
- RecoveryTool is a separate guidance recovery vocabulary, not the context-facing NextTool alias. [144]
- WorktreeSummary.nextRequiredArgs is an optional list of strings, defaulting to None. [145]
- unknownContractCells (`list[str] \\| None`, default None) is present only when the contract file carried a cell outside its declared vocabulary, as notice that values were substituted. [146]
- WorktreeCommandResponse declares the next-move triple: nextAction, nextTool and nextArgs. [147]
- The membership validator refuses a next move outside the advertised roster. [148]
- PUBLIC_TOOLS lives in models as a zero-import leaf tuple the validator reads. [149]
- `IntegrationStatus` gained a fourth member, `checkpointed` . [150]
- record_landed_integration publishes that a contract’s code landed and returns the updated contract. [151]
- The post-integration phase routes the outcome after integration was attempted (blocked, or landed with carryover/cleanup). [152]
- WorktreePhase declares the eight closed lifecycle-phase values; the checkpoint does not add a ninth phase. [153]
- WorkflowKind is declared once in models.worktree as the shared wire vocabulary. [154]
- HumanReviewStatus is declared once in models.worktree as the shared wire vocabulary. [155]
- CloseoutStatus is declared once in models.worktree as the shared wire vocabulary. [156]
- IntegrationStatus is declared once in models.worktree as the shared wire vocabulary. [157]
- CleanupStatus is declared once in models.worktree as the shared wire vocabulary. [158]
- worktree_contract imports lifecycle vocabularies from models.worktree, imports memory vocabularies from the kernel and derives VALID_* sets with get_args. [159]
- Checkpoint responses record only the real integrated code and memory-content commits. [160]
- The pause envelope declares the stop's one own field, paused, and inherits the ordinary command envelope. [161]
- NextTool includes worktree_checkpoint_landing while NextOperation remains its seven-member intent vocabulary. [162]
- WorktreeCommandResponse declares the next-move triple, while WorktreeSyncResponse and WorktreeOperationControlResponse narrow nextTool. [163]
