# mcp/src/agents_remember/mcp/registration/core.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/src/agents_remember/mcp/registration/core.py`       |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-08-02T01:05+02:00                                   |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`               |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                            |

## Governing Overview

[registration route overview](overview.md)

## Purpose

`register_core_tools(server, config)` declares server identity, the orientation reads, and the two
installers: `ping`, `server_info`, `context_packet`, `read_ar_files`, `resolve_context`,
`runtime_install`, `skills_install`.

## Code Commentary

### Logic

Seven `@server.tool()` declarations, each forwarding to its `mcp/tools/core.py` payload builder.
The docstrings are the model-visible contract and carry the semantics that are not in the types:

- `ping` — liveness only; no configuration, no side effects.
- `server_info` — the settings loaded **at startup**; a settings edit needs a harness restart.
- `context_packet` — one orientation call. `include_providers` defaults true; `include_drift` and
  `include_freshness` default false because they cost a drift scan and a remote fetch respectively.
- `read_ar_files` — the research-phase read: ≤5 repo-relative paths, each paired with its file-level
  onboarding plus the auto-attached repo and governing route overviews (deduplicated per session,
  `refresh=true` re-serves after a compaction). Native read is the edit precondition once building
  begins.
- `resolve_context` — the one declaration here that packs: the five flat locators (`repo_id`,
  `task_name`, `parent_task`, `leaf_id`, `contract_path`) become a `TaskRef`, while `worktree_name`
  and `topology` stay separate arguments because they are not part of "which task".
- `runtime_install` — the operator text distinguishes preserved user data (`memory-repos/`,
  `providers/data/`) from replaced managed scaffold, explains that `install_provider_deps=true` may
  refresh `providers/runners/` after stopping watchers, and that `no_cache=true` forces a
  from-scratch image rebuild past the skip-if-tag-exists shortcut.
- `skills_install` — flat packaged skills copied by frontmatter name; most harnesses only discover
  them after a restart.

### Invariants And Boundaries

- The signature is the published MCP schema. `resolve_context` keeps its five locators flat and
  builds the `TaskRef` inside the body; typing the parameter as `TaskRef` would republish the tool
  as a nested object.
- `runtime_install` and `skills_install` register `dry_run=False` — act-by-default. The docstrings
  say to preview first; the default does not.
- No behaviour here. `read_ar_files`'s onboarding-lookup status vocabulary, the route-index rule,
  and the per-session dedup all live in `application/read_files.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Six of the seven payload builders (all but `read_ar_files_payload`). | `read_ar_files_payload` | mcp/src/agents_remember/mcp/tools/read_files.py:13-22 |
| `read_ar_files_payload`, imported through the `mcp.tools` facade. | `read_ar_files_payload` | mcp/src/agents_remember/mcp/tools/read_files.py:13-22 |
| `TaskRef` — the locator bundle `resolve_context` packs. | `TaskRef` | mcp/src/agents_remember/application/task_ref.py:14-28 |
| What each declaration hands its builder, proved through a live server. | `RegistrationWiringTests` | mcp/tests/test_mcp_registration_wiring.py:61-1307 |

## Update History

- 2026-08-03T02:42:00+02:00 — W3-B01 curator: curated 2 Repo-Internal table citations with exact `TaskRef` and registration-wiring test anchors. Verification metadata remains unchanged for closeout.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. These seven declarations
  moved verbatim out of `server.py`; `resolve_context` additionally packs its locators into the new
  `TaskRef`. Verification metadata pinned to the pre-change commit until closeout stamps the L2 code
  commit.
