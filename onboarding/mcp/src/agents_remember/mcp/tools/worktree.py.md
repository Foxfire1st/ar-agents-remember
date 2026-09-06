# mcp/src/agents_remember/mcp/tools/worktree.py

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/mcp/tools/worktree.py` |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview      | `overview.md`                                   |

## Governing Overview

[MCP tools overview](overview.md)

## Purpose

Worktree lifecycle payload builders.

## Code Commentary

`worktree_closeout_apply_payload` forwards the keyword-only `corrective_dispositions` tuple of `RedCatalogDisposition` unchanged to the application entry point. The adapter does not decide whether a failed catalog item may be corrected or accepted.

L23 types integration strategy at the payload edge and adds task-addressed lifecycle-operation cancellation with explicit intent and dry-run forwarding.

### Logic

Holds `worktree_start_payload`, `worktree_attach_payload`,
`worktree_status_payload`, `worktree_closeout_preview_payload`,
`worktree_closeout_apply_payload`, `worktree_integrate_payload`,
`worktree_cleanup_payload`, and `worktree_abandon_payload`. Each forwards typed
arguments to the matching `application.worktree_tools` function and returns
through `base._tool_payload`. The former `direct_closeout_preview_payload` /
`direct_closeout_apply_payload` builders were removed with the direct-closeout
tool surface (issue #62): closeout is worktree-only.

`worktree_start_payload` now wraps its application entry point result with
`summarize_command_logs` (imported from `providers.lifecycle.log_capture`)
before returning, trimming large stdout/stderr from provider setup output that
would otherwise make the response too large to render.

`worktree_cleanup_payload` now accepts and forwards `teardown_providers`
(default `True`).

`worktree_abandon_payload` is newly added; it forwards `contract_path`,
`dry_run`, and `force` to `worktree_abandon_tool`.

`worktree_start_payload` forwards `retry_provider_setup` to the application entry point — the relaunch path for a failed or stale background provider setup (GitHub #53). It also forwards `stale_base_choice` — the stale-base preflight recovery selector (GitHub #54). `worktree_sync_payload` forwards the canonical `contract_path`, typed `MemorySyncChoice`, typed `SyncResolutionAction`, and `dry_run` unchanged to `worktree_sync_tool`; it owns no journal or selector behavior. `worktree_attach_payload` forwards a new `on_unsaved` argument to `worktree_attach_tool` (slice 2c — the save-gate decision when attaching over an unsaved fleeting lifecycle); plumbing only.

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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

The source itself and its governing route are sufficient for this thin payload adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| Start, sync, attach, and status payload builders preserve typed application inputs. | `worktree_start_payload`; `worktree_sync_payload`; `worktree_attach_payload`; `worktree_status_payload` | mcp/src/agents_remember/mcp/tools/worktree.py:44-54; mcp/src/agents_remember/mcp/tools/worktree.py:57-74; mcp/src/agents_remember/mcp/tools/worktree.py:77-86; mcp/src/agents_remember/mcp/tools/worktree.py:89-98 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned transport adapter.

| Finding | Anchor | Source |
| --- | --- | --- |

## Series-Contract Notes

Worktree payload builders keep closeout/integration path-explicit while start/attach/status can resolve a leaf enclosure from `task_name`, optional `parent_task`, and optional `leaf_id` — carried by `TaskIdentity` for start and by `TaskRef` for attach/status.

## L23 Lifecycle Model Package Review

The transport adapter now imports `IntegrateStrategy` from `models.lifecycles.operation`, its
dedicated package owner. Tool payloads, task identity, and forwarding behavior are unchanged.

## 260821-CLIVE-L2 Current Contract

The current source seams include `worktree_start_payload`, `worktree_sync_payload`, `worktree_attach_payload`. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `worktree_start_payload`, `worktree_sync_payload`, `worktree_attach_payload` at this ownership boundary. | `worktree_start_payload`; `worktree_sync_payload`; `worktree_attach_payload` | mcp/src/agents_remember/mcp/tools/worktree.py:44-54; mcp/src/agents_remember/mcp/tools/worktree.py:57-74; mcp/src/agents_remember/mcp/tools/worktree.py:77-86 |

## 260831-CCR-L15 Status-Wait Payload Export

The module now imports `LifecycleStatusWaitRequest` /
`worktree_status_wait_tool` and exports
`worktree_status_wait_payload`, which wraps the read-only wait application tool into the
standard `_tool_payload` envelope for the public `worktree_status_wait` tool.

## Update History

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the `worktree_status_wait_payload` export for the new public wait tool.
- 2026-08-26T08:45+02:00 — Restored canonical Docs/Repo/Cross-Repo reference sections for the
  changed worktree payload adapter.

- 2026-08-26T03:37+02:00 — Added typed `resolution_action` forwarding beside
  `memory_sync_choice`; payload transport remains contract-addressed and journal-free. Verification
  remains post-Dagger/closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-13T09:05+02:00 — L23 curator: recorded the integration-strategy import move and confirmed
  the public tool contract is unchanged; final provenance remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: the builders here took parameter objects.
  `worktree_start_payload` now takes `TaskIdentity` + `bases: TaskBases` + `execution:
  StartExecution`; attach/status take one `TaskRef`; the closeout pair take
  `CloseoutCommitMessages`, with apply keeping a separate `CloseoutApproval`. The published MCP
  signatures are unchanged — packing moved to `mcp/registration/`. Verification metadata pinned
  until closeout stamps the L2 code commit.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree payload builders now include `parent_task` and `leaf_id` for start/attach/status, matching the new resolver contract while closeout/integration continue taking explicit enclosure paths. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: `worktree_attach_payload` forwards a new `on_unsaved` argument to `worktree_attach_tool` (the save-gate decision); plumbing only. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-11T06:47+02:00 — Removed `direct_closeout_preview_payload` / `direct_closeout_apply_payload` and their controller imports (issue #62 worktree-only closeout); module docstring no longer mentions direct closeout.
- 2026-06-10T09:56+02:00 — Added `worktree_sync_payload` (GitHub #54 sub-task D); plumbing only.
- 2026-06-10T09:30+02:00 — `worktree_start_payload` forwards `stale_base_choice` (GitHub #54 stale-base preflight recovery); plumbing only.
- 2026-06-10T07:30+02:00 — `worktree_start_payload` forwards the new `retry_provider_setup` flag to the controller (GitHub #53 async setup recovery path).
- 2026-06-01T00:00+02:00 — `worktree_start_payload` now applies `summarize_command_logs`; `worktree_cleanup_payload` gained `teardown_providers`; `worktree_abandon_payload` newly added.
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the worktree payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
