# mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash |                                            `8bf6edad7e7e65e27cf735be0822f604531d0c8a`|
| lastVerifiedCommitDate |                                            2026-08-16T10:54:02+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Payload builder for the public `lifecycle_finalize_task` MCP tool.

## Code Commentary

`lifecycle_finalize_task_payload(config, contract_path, *, docs: FinalizeTaskDocs = NO_TASK_DOCS,
dry_run=False, teardown_providers=True)` is intentionally transport-thin. It forwards the runtime
config and contract path positionally, the three task-document inputs as one `FinalizeTaskDocs`
(`task_doc_path`, `master_doc_path`, `subtask_number` — 260731-EFA-L2; `NO_TASK_DOCS` is the shared
"finalize without touching documents" value), and the dry-run and provider-teardown flags, to
`application.worktree_tools.lifecycle_finalize_task_tool`, then validates the returned payload
through `base._tool_payload` under the `lifecycle_finalize_task` public tool name.

The published MCP tool still takes the three document arguments flat; `mcp/registration/tasks.py`
builds the `FinalizeTaskDocs`.

This module owns no lifecycle or Git behavior. The application entry point owns path
containment, and the worktree finalizer owns readiness, cleanup, and
task-document reconciliation.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Application entry point validates coordination-contained paths, delegates to the worktree finalizer, and then performs configured completion cleanup. | `lifecycle_finalize_task_tool` | mcp/src/agents_remember/application/worktree_tools.py:552-583 |
| The shared payload helper is `_tool_payload`. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:73-75 |
| The response boundary is `complete_tool_response`. | "def complete_tool_response" | mcp/src/agents_remember/application/tool_response.py:53-53 |
| The response model is registered in the public tool registry. | `lifecycle_finalize_task` | mcp/src/agents_remember/models/tool_registry.py:203-203 |

## Update History

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: re-anchored citation range(s) to current source after the L16 line movement (cited files changed, card source unchanged); verification metadata unchanged.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:35:04+02:00 — 260731-EFA-L6 S18-B10 curator: source-first semantic citation curation; repaired this card's scoped citation findings with frozen-source evidence and corrected stale or pooled claims where needed.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: the three task-document keyword arguments became one
  `FinalizeTaskDocs` (default `NO_TASK_DOCS`), and `contract_path` moved to a positional argument.
  Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-06-23T22:50+02:00 — Created as the payload-builder surface for `lifecycle_finalize_task`. Verification metadata is pending until closeout stamps the source commit.
