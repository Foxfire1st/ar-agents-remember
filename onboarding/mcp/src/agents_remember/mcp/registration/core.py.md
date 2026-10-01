# mcp/src/agents_remember/mcp/registration/core.py

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_core_tools(server, config)` declares server identity, the orientation reads, and the two
installers: `ping`, `server_info`, `context_packet`, `read_ar_files`, `resolve_context`,
`runtime_install`, `skills_install`. Its identity family binds the one process-scoped
`ServingBuildPayload` used by `server_info`.

## Code Commentary

### Logic

Seven `@server.tool()` declarations, each forwarding to its `mcp/tools/core.py` payload builder.
`register_core_tools` obtains one strict payload through the application-owned
`mcp_serving_build_payload()` gateway and passes that immutable value into the identity registrar;
every `server_info` call therefore reports the same boot and candidate identity without
request-time reprobes or an MCP-to-serving domain import.
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
- `server_info` must receive the shared process build; constructing or re-resolving a new build in
  the handler would break correlation with the dashboard and harness acceptance evidence.
- Serving-domain ownership stays behind `application.runtime.startup`; this MCP adapter consumes
  only the strict model payload.

## Evidence

### Repo-Internal References

- Six of the seven payload builders (all but `read_ar_files_payload`). [1]
- `read_ar_files_payload`, imported through the `mcp.tools` facade. [2]
- `TaskRef` — the locator bundle `resolve_context` packs. [3]
- The registration gained the keyword-only `experiment` parameter and builds the run's request itself. [4]

## 260915-CAPS-L9 Experiment Parameter On `runtime_install`

The registered `runtime_install` tool gained one additive, keyword-only parameter —
`experiment: str | None = None` — and now constructs the run's `RuntimeInstallRequest` itself
instead of forwarding four booleans to the payload builder. Its docstring is the model-visible
contract for the parameter and says exactly what the ruling requires: it installs the
experimental instruction cutover **for THIS run** (the legacy AR startup chain is withheld and
the pinned eve application is installed beside the canonical assets); it is a per-call input,
**never a setting**; omitting it — with no `AR_EXPERIMENT` in the server environment — installs
the unmodified runtime; and the returned record's `selectionSource` names which input supplied
the mode. The registered tool count is unchanged: a parameter was added to an existing
declaration, not a tool.
