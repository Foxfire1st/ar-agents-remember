# mcp/src/agents_remember/mcp/registration/worktrees.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/mcp/registration/worktrees.py`       |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_worktree_tools(server, config)` declares the **working half** of a worktree-backed task:
`worktree_start`, `worktree_attach`, `worktree_status`, `worktree_sync`. The landing half
(closeout, integrate, cleanup, abandon) is a separate family in `closeout.py`.

## Code Commentary

### Logic

`worktree_start` is the widest declaration in the family and splits into the three parameter objects
its application entry point takes — who the task is, what it is cut from, and how the start runs:

- `TaskIdentity(repo_id, task_name, worktree_name, leaf_id, parent_task, workflow_kind)` —
  `workflow_kind` defaults to `light-task` (the other value is `chat-task`).
- `TaskBases(source_branch, work_branch, memory_mode, memory_choice, stale_base_choice)`.
- `StartExecution(dry_run, skip_provider_setup, retry_provider_setup)`.

Its docstring carries two contracts that are invisible in the types. The **stale-base preflight**:
a start refuses when the source branch is behind or diverged from its remote tracking branch, and
the blocked `choose_stale_base_recovery` result is cleared by re-running with
`stale_base_choice='fast-forward'` or `'proceed-stale'`. And the **async provider setup**: start
returns within seconds with the providers block reporting `starting` plus a `progressFile`; the
caller polls `worktree_status` until a terminal state (a seed copy takes seconds, a refused seed
falls back to a full reindex flagged `seedFallback`), and re-runs with `retry_provider_setup=true`
after a failed or stale setup.

`worktree_attach` and `worktree_status` both pack their five locators into a `TaskRef` — the same
bundle `resolve_context` uses. Attach is read-only (it mutates no git) and takes `on_unsaved`
(`save` promotes an unsaved fleeting lifecycle, `discard` abandons it) to clear the save gate.
Status reports phase, dirty flags, next-step hints, and the live provider-setup block.

`worktree_sync(contract_path, memory_sync_choice, resolution_action, dry_run)` forwards flat with
shared `Literal` types. Its help now describes retained code/chosen-memory conflicts: the agent
resolves and stages in the reported worktree, then calls the same contract with
`resolution_action='continue'`, or restores pinned pre-sync heads with `cancel`. It does not expose
an operation id or promise abort-on-conflict behavior. `skip-memory` is an admission/preflight
choice, not a way to change an already-running generation.

### Invariants And Boundaries

- Flat signature, packing in the body — `TaskIdentity`/`TaskBases`/`StartExecution` and `TaskRef`
  belong to the application entry point boundary.
- `worktree_start` and `worktree_sync` are mutating and register `dry_run=False`; `worktree_attach`
  and `worktree_status` are read-only and take no dry-run flag.
- Contract creation, git mechanics, provider setup, and lifecycle promotion live in
  `application/worktree_tools.py` and the `worktrees/` package.
- Registration publishes the shared closed memory-choice/continue/cancel vocabulary; no free-string
  compatibility parameter or alternate sync tool is registered.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public sync declaration exposes typed memory choice and contract-addressed continue/cancel with retained-conflict help. | `worktree_sync` | mcp/src/agents_remember/mcp/registration/worktrees.py:233-259 |
| The start payload forwards task identity, bases and execution configuration to the application owner. | "def worktree_start_payload" | mcp/src/agents_remember/mcp/tools/worktree.py:51-61 |
| The attach payload forwards the requested worktree attachment to the application owner. | "def worktree_attach_payload" | mcp/src/agents_remember/mcp/tools/worktree.py:84-93 |
| The status payload reads status through the application owner. | "def worktree_status_payload" | mcp/src/agents_remember/mcp/tools/worktree.py:96-105 |
| The sync payload forwards the synchronization request to the application owner. | "def worktree_sync_payload" | mcp/src/agents_remember/mcp/tools/worktree.py:64-81 |
| The identity parameter object `TaskIdentity` (repo_id, task_name, worktree_name, leaf_id, parent_task, workflow_kind defaulting to `light-task`), defined in the application request boundary. | `TaskIdentity` | mcp/src/agents_remember/application/worktree_tool_requests.py:15-29 |
| The bases parameter object `TaskBases` (source_branch, work_branch, memory_mode, memory_choice, stale_base_choice), defined in the application request boundary. | `TaskBases` | mcp/src/agents_remember/application/worktree_tool_requests.py:32-47 |
| The execution parameter object `StartExecution` (dry_run, skip_provider_setup, retry_provider_setup), defined in the application request boundary. | `StartExecution` | mcp/src/agents_remember/application/worktree_tool_requests.py:50-56 |
| `TaskRef` — the shared task locator attach and status pack. | `TaskRef` | mcp/src/agents_remember/application/task_docs/task_ref.py:15-28 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned registration surface.

| Finding | Anchor | Source |
| --- | --- | --- |

## L23 Final Candidate Disposition

Public worktree registrations remain task-addressed and immediate-returning. Durable operation
identity, candidate trees, worker processes, and recovery state stay behind the application/service
boundary and are not added to the tool schema.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE-L2 Current Contract

The current source seams include `register_worktree_tools`. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `register_worktree_tools` at this ownership boundary. | `register_worktree_tools` | mcp/src/agents_remember/mcp/registration/worktrees.py:27-31 |

## 260821-CLIVE Stable-Address Registration Contract

Registered help now makes the address chain explicit: start reserves the configured contract
address and enclosure manifest before exposing work; attach resumes only through that exact locator
and never scans task/worktree/report paths; status resolves the independent locator and then either
the live root journal or exact terminal archive/receipt. Conflicting reservations and invalid
terminal proof fail closed, with no inferred enclosure-root fallback.

## 260831-CCR-L15 Status-Wait Server Tool

`_register_worktree_observation_tools` now registers the `@server.tool()`
`worktree_status_wait` tool addressed by `contract_path`,
`operation_kind`, `expected_generation`, `after_revision`, and
`timeout_seconds` (default 30.0), dispatching to
`worktree_status_wait_payload`. The tool docstring promises the read-only CCR-R15 wait
contract: heartbeats/log growth never wake it, a generation successor wakes an old-generation wait
with explicit successor information, and wrong contract/generation/cursor and unreadable journals
refuse typed.

## Update History
- 2026-09-05T06:24:16+00:00: Generated citation repair: `worktree_sync` repointed to mcp/src/agents_remember/mcp/registration/worktrees.py:233-259. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the `worktree_status_wait` server-tool registration under the observation tools.
- 2026-09-03T12:30+02:00 — 260831-CCR provenance-debt repair: replaced the terse multi-anchor `TaskIdentity`, `TaskBases`, `StartExecution` row with three rows, one per distinct definition, pointing each anchor at its unique class definition in application/worktree_tool_requests.py (15-29, 32-47, 50-56) and naming the per-object fields. The names previously resolved 3 times each because worktree_tools.py only imports and annotates them (import lines 113-115, signature annotations 121-124 and 229-232), so occurrence matching found three sites per name; each claim now maps to exactly one definition and verifies uniquely.

- 2026-08-26T08:45+02:00 — Restored canonical Docs/Cross-Repo reference sections for the changed
  public worktree registration card.

- 2026-08-26T08:30+02:00 — Rebounded the public worktree-registration citation to the frozen
  helper extent after final consolidation.

- 2026-08-26T03:37+02:00 — Updated the registered sync signature/help for typed retained-conflict
  continuation and exact cancellation. No operation-id or fallback surface was added. Verification
  remains post-Dagger/closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged stable locator, strict attach, and terminal-aware status semantics. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.
- 2026-08-14T06:32+02:00 — No public schema impact: L23 preserves the worktree registration surface
  while closeout/integration run as task-addressed durable operations behind it. Verification
  remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 3 citation rows; scoped citation fixing regenerated the source ranges.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The four working-half
  declarations moved out of `server.py`; start now packs into `TaskIdentity`/`TaskBases`/
  `StartExecution` and attach/status into `TaskRef`. Verification metadata pinned to the pre-change
  commit until closeout stamps the L2 code commit.
