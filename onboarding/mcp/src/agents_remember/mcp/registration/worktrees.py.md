# mcp/src/agents_remember/mcp/registration/worktrees.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/mcp/registration/worktrees.py`       |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated | 2026-08-24T15:04+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
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

`worktree_sync(contract_path, memory_sync_choice, dry_run)` forwards flat. Its docstring states the
atomic base-pair advance, the mid-cycle block (the new code tip must be ledger-mapped at the
official memory tip, otherwise run carryover first), the `merge-memory` / `skip-memory` recovery,
and the sync-early doctrine.

### Invariants And Boundaries

- Flat signature, packing in the body — `TaskIdentity`/`TaskBases`/`StartExecution` and `TaskRef`
  belong to the application entry point boundary.
- `worktree_start` and `worktree_sync` are mutating and register `dry_run=False`; `worktree_attach`
  and `worktree_status` are read-only and take no dry-run flag.
- Contract creation, git mechanics, provider setup, and lifecycle promotion live in
  `application/worktree_tools.py` and the `worktrees/` package.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The payload builders these forward to. | `worktree_start_payload`, `worktree_attach_payload`, `worktree_status_payload`, `worktree_sync_payload` | mcp/src/agents_remember/mcp/tools/worktree.py:43-53; mcp/src/agents_remember/mcp/tools/worktree.py:74-83; mcp/src/agents_remember/mcp/tools/worktree.py:86-95; mcp/src/agents_remember/mcp/tools/worktree.py:56-71 |
| `TaskIdentity`, `TaskBases`, `StartExecution`. | `TaskIdentity`, `TaskBases`, `StartExecution` | mcp/src/agents_remember/application/worktree_tools.py:100-113; mcp/src/agents_remember/application/worktree_tools.py:117-131; mcp/src/agents_remember/application/worktree_tools.py:135-142 |
| `TaskRef` — the shared task locator attach and status pack. | `TaskRef` | mcp/src/agents_remember/application/task_docs/task_ref.py:15-28 |
| The three-way split is proved through live registration. | `test_worktree_start_splits_identity_bases_and_execution` | mcp/tests/test_mcp_registration_wiring_tests_1.py:632-675 |
| The light-task default is proved through live registration. | `test_worktree_start_defaults_to_a_real_light_task_start` | mcp/tests/test_mcp_registration_wiring_tests_2.py:84-101 |

## L23 Final Candidate Disposition

Public worktree registrations remain task-addressed and immediate-returning. Durable operation
identity, candidate trees, worker processes, and recovery state stay behind the application/service
boundary and are not added to the tool schema.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE-L2 Current Contract

The current source seams include `register_worktree_tools`. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `register_worktree_tools` at this ownership boundary. | L26-L29 | `mcp/src/agents_remember/mcp/registration/worktrees.py` |

## 260821-CLIVE Stable-Address Registration Contract

Registered help now makes the address chain explicit: start reserves the configured contract
address and enclosure manifest before exposing work; attach resumes only through that exact locator
and never scans task/worktree/report paths; status resolves the independent locator and then either
the live root journal or exact terminal archive/receipt. Conflicting reservations and invalid
terminal proof fail closed, with no inferred enclosure-root fallback.

## Update History

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
