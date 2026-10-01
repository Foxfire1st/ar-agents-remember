# mcp/src/agents_remember/mcp/tools/worktree.py

## Governing Overview

[MCP tools overview](overview.md)

## Purpose

Worktree lifecycle payload builders.

## Code Commentary

`worktree_closeout_apply_payload` forwards the keyword-only `corrective_dispositions` tuple of `RedCatalogDisposition` unchanged to the application entry point. The adapter does not decide whether a failed catalog item may be corrected or accepted.

L23 types integration strategy at the payload edge and adds task-addressed lifecycle-operation cancellation with explicit intent and dry-run forwarding.

### Logic

Integration and checkpoint payload builders forward only contract path, integration strategy,
and `dry_run`. Closeout message objects contain code and memory intent only. These transport
adapters neither request nor synthesize a ledger commit.

Holds `worktree_start_payload`, `worktree_attach_payload`,
`worktree_pause_payload`, `worktree_status_payload`, `worktree_closeout_preview_payload`,
`worktree_closeout_apply_payload`, `worktree_integrate_payload`,
`worktree_checkpoint_landing_payload`, `worktree_record_landing_payload`,
`worktree_cleanup_payload`, and `worktree_abandon_payload`. Each forwards typed
arguments to the matching `application.worktree_tools` function and returns
through `base._tool_payload`. The former `direct_closeout_preview_payload` /
`direct_closeout_apply_payload` builders were removed with the direct-closeout
tool surface (issue #62): closeout is worktree-only.

`worktree_checkpoint_landing_payload` (260831-LOCR-L30) forwards `contract_path`, the typed
`strategy`, and `dry_run` to `worktree_checkpoint_landing_tool`, the
partial-master landing route; like its integrate sibling it is transport-thin and owns no authority
or completion decision of its own.

`worktree_pause_payload` (260831-LOCR-L37) is the thinnest builder in the module: it takes only
`contract_path`, forwards it to `worktree_pause_tool`, and wraps the result through `_tool_payload`
under the operation name `worktree_pause`. It owns no decision — not whether the master may be
paused, not what the release writes, and above all not whether anything is published. The
publication in this same module is `worktree_checkpoint_landing_payload`; the two are separate
builders for separate tools and neither routes to the other.

`worktree_start_payload` now wraps its application entry point result with
`summarize_command_logs` (imported from `providers.lifecycle.log_capture`)
before returning, trimming large stdout/stderr from provider setup output that
would otherwise make the response too large to render.

`worktree_cleanup_payload` now accepts and forwards `teardown_providers`
(default `True`).

`worktree_abandon_payload` is newly added; it forwards `contract_path`,
`dry_run`, and `force` to `worktree_abandon_tool`.

`worktree_start_payload` forwards `retry_provider_setup` to the application entry point — the relaunch path for a failed or stale background provider setup (GitHub #53). It also forwards `stale_base_choice` — the stale-base preflight recovery selector (GitHub #54). **`worktree_sync_payload` now forwards one paired `resolution: SyncResolutionInput | None`** where it used to forward a bare `resolution_action`: the action and the authored decision it may carry travel as one value through this layer — including the registration's `resolution_action` + `knowledge_resolution` arguments, which it pairs before forwarding — because `application.worktree_tools.worktree_sync_tool` is at the `PLR0913` ceiling and because the two are refused as a pair. Beyond the pairing this adapter owns no journal or selector behavior. `worktree_attach_payload` forwards a new `on_unsaved` argument to `worktree_attach_tool` (slice 2c — the save-gate decision when attaching over an unsaved fleeting lifecycle); plumbing only.

### Parameter Objects (260731-EFA-L2)

Every builder here now takes the concept object its application entry point takes, not a keyword list:

| Builder | Signature |
| --- | --- |
| `worktree_start_payload` | `(config, identity: TaskIdentity, *, bases: TaskBases = DEFAULT_TASK_BASES, execution: StartExecution = DEFAULT_START_EXECUTION)` |
| `worktree_attach_payload` | `(config, task: TaskRef, *, on_unsaved=None)` |
| `worktree_status_payload` | `(config, task: TaskRef)` |
| `worktree_closeout_preview_payload` | `(config, contract_path, messages: CloseoutCommitMessages)` |
| `worktree_closeout_apply_payload` | `(config, contract_path, messages: CloseoutCommitMessages, approval: CloseoutApproval)` |

`worktree_sync_payload`, `worktree_integrate_payload`, `worktree_cleanup_payload` and
`worktree_abandon_payload` keep their flat arguments — each already sat at or under the limit.

The split is meaningful, not cosmetic. `TaskIdentity` is who the task is, `TaskBases` what it is cut
from, `StartExecution` how the start runs. `CloseoutApproval` (intent note + dry_run) is kept apart
from `CloseoutCommitMessages` so a preview can never read as an approved apply. `TaskRef` is the
shared task locator `resolve_context` also uses.

The MCP tools themselves still publish flat signatures; the packing happens one layer up in
`mcp/registration/worktrees.py` and `mcp/registration/closeout.py`, because a model-typed tool
parameter would republish the tool as a nested object.

### Conventions

Each payload builder forwards the application contract and wraps its result through the common payload owner, without adding Git or cache interpretation.

### Invariants And Boundaries

- Transport-thin: worktree/closeout behavior lives in
  `application.worktree_tools` and `worktrees/modules`.
- Closeout/apply builders carry the explicit `intent_note` commit-approval
  argument through to the application entry point — it now travels inside `CloseoutApproval`, which must stay a
  separate parameter from `CloseoutCommitMessages`.
- `worktree_start_payload`/`worktree_integrate_payload`/`worktree_cleanup_payload`/`worktree_abandon_payload`
  default `dry_run=False` (act-by-default); the `*_closeout_apply` builders keep
  `dry_run=False` paired with their `*_preview` builders. `dry_run=true` previews.
- Sync payload transport preserves the shared literal types and canonical contract address; it
  cannot select by operation id or supply a compatibility fallback.

### Todos

No additional file-local TODO is established by this candidate review.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

The source itself and its governing route are sufficient for this thin payload adapter.

- Integration payloads forward contract, strategy, and preview choice without ledger intent. [1]
- Start, sync, attach, pause, and status payload builders preserve typed application inputs, and the sync builder now takes one paired resolution value instead of a bare action. [2]
- The checkpoint-landing payload builder forwards the contract and typed integration arguments without owning a completion decision. [3]
- The pause payload builder forwards one contract path to the stop tool and owns no decision; it is the transport edge of the route that publishes nothing. [4]
- **The paired resolution value this builder forwards, and the application entry point that unpacks it into the driver's two arguments.** [5]

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned transport adapter.

## Series-Contract Notes

Worktree payload builders keep closeout/integration path-explicit while start/attach/status can resolve a leaf enclosure from `task_name`, optional `parent_task`, and optional `leaf_id` — carried by `TaskIdentity` for start and by `TaskRef` for attach/status.

## L23 Lifecycle Model Package Review

The transport adapter now imports `IntegrateStrategy` from `models.lifecycles.operation`, its
dedicated package owner. Tool payloads, task identity, and forwarding behavior are unchanged.

## 260821-CLIVE-L2 Current Contract

The current source seams include `worktree_start_payload`, `worktree_sync_payload`, `worktree_attach_payload`. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

- The current module exposes `worktree_start_payload`, `worktree_sync_payload`, `worktree_attach_payload` at this ownership boundary. [6]

## 260831-CCR-L15 Status-Wait Payload Export

**Superseded.** The `worktree_status_wait_payload` builder and the `worktree_status_wait` tool it
served were removed; this module exports no wait payload today and the name appears nowhere in the
worktree payload surface. Recorded so the L15 paragraph above is not read as current.
