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
