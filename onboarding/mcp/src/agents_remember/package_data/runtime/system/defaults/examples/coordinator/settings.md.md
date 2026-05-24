# settings.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `31846c1136f0fe75503a63fb557303a79fa022e8` |
| lastVerifiedCommitDate | 2026-05-24T23:07:31+02:00|

## Purpose

This file is the human-facing coordinator settings example for `ar-coordination/system/settings.md`, including the human-readable doctrine for optional context providers.

## Code Commentary

### Logic

The example describes the coordinator as workspace-wide routing and workflow state. It lists global instructions, shared tools, workspace source registries, task/worktree roots, notes, selected memory repos, and operator conventions as coordinator-owned surfaces. The context provider section frames providers as local discovery accelerators, maps semantic discovery to GrepAI, relationship discovery to CodeGraphContext, and intent retrieval back to onboarding plus bounded source confirmation. Machine-readable provider authority belongs to the MCP settings file outside the coordinator root, not to this human-facing coordinator example.

The provider install guidance says installs should be coordination-owned: pinned requirements under `providers/requirements/`, runtime-owned binaries under `providers/_bin/`, one reusable virtual environment per Python provider type under `providers/_venvs/`, and patches under `providers/patches/`. Providers that need databases or daemonized infrastructure should prefer Docker-wrapped backends and must not require host-level PostgreSQL, FalkorDB, OS services, launch agents, package-manager services, or global user daemons for normal managed mode.

The GrepAI guidance says one `grepai-memory` provider can declare multiple memory roots in workspace mode, covering both external memory repos and repo-internal `ar-memory/` roots with explicit `{ projectId, path }` entries. Managed lifecycle tooling mirrors those roots into provider-owned index roots before launching GrepAI because GrepAI still writes per-project symbol/config artifacts beside each configured project path. GrepAI config, state, cache, home files, and mirrored index roots live under `providers/runners/grepai/`; logs live under `providers/logs/grepai/`; all memory roots share one lifecycle-owned PostgreSQL/pgvector Docker DBMS with durable state under `providers/data/grepai/postgres/`. A `.grepai/` directory inside any indexed memory root is a containment failure rather than durable memory.

The CodeGraphContext guidance says one `codegraphcontext-code` provider can declare multiple code repository roots. Lifecycle tooling expands those roots into one watcher/runtime instance per configured code repo under `providers/runners/codegraphcontext/<repo-id>/`, while all instances share one lifecycle-owned FalkorDB Docker DBMS with durable state under `providers/data/codegraphcontext/falkordb/`. Reinstall/update may delete and recreate package-owned provider defaults plus runner scaffolding while preserving `providers/data` and `providers/logs`; MCP install generates lifecycle settings from MCP authority rather than coordinator-local JSON authority. Deleting FalkorDB data, graph namespaces, repository indexes, or GrepAI PostgreSQL data requires an explicit destructive lifecycle action.

### Conventions

Repo-specific rules belong in the selected memory layer rather than this coordinator settings file. Provider settings should stay declarative in MCP settings, while start/stop/status/refresh/install behavior belongs in MCP/package-owned lifecycle tooling. Concrete GrepAI and CGC root entries should name existing memory or code repository directories; placeholder examples should not be applied as live settings.

### Invariants And Boundaries

C-08 remains the route from coordinator context into the target repository's active memory settings, tools, sources, onboarding, and ledger paths. Context providers must not replace source proof, verified onboarding, drift checks, branch validity, or memory promotion rules. Disposable GrepAI runtime artifacts must stay under `providers/runners/grepai/`, disposable CGC runtime artifacts must stay under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/`, durable database state must stay under `providers/data/`, and process-only env keys must not be persisted into `.env` when CGC v0.4.10 rejects them as invalid config.

### Todos

None.

### Docs References

No external documentation is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The example states that coordinator settings are workspace-wide and do not replace per-repository memory settings. | L1-L8 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md) |
| The scope list names global instructions, shared commands, workspace sources, roots, notes, selected memory repos, and operator conventions as coordinator concerns. | L10-L25 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md) |
| The routing section tells agents to invoke C-08 and treat repository-specific memory guidance as more specific. | L40-L48 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md) |
| The context provider section defines semantic, relationship, and intent retrieval substrates, keeps provider authority in MCP settings, routes lifecycle behavior through MCP/package-owned tooling, and requires provider installs to be coordination-owned with runtime-owned binaries, provider venvs, patches, and Docker-wrapped backend services instead of host-level services or global daemons. | L49-L81 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md) |
| The GrepAI notes require a workspace-mode `roots` array for external memory repos and repo-internal `ar-memory/` roots, mirror roots into provider-owned index roots, keep GrepAI config/state/mirrors under `providers/runners/grepai/`, store logs under `providers/logs/grepai/`, store durable PostgreSQL/pgvector data under `providers/data/grepai/postgres/`, and treat `.grepai/` inside indexed memory roots as a containment failure. | L83-L94 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md) |
| The CGC notes require configured code roots, per-repo runtime instances under `providers/runners/codegraphcontext`, a shared lifecycle-owned FalkorDB Docker DBMS with durable state under `providers/data/`, process-env separation, and explicit destructive actions for database deletion. | L96-L123 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T00:37+02:00: Refreshed provider doctrine after lifecycle setup moved fully behind MCP/package-owned operations and coordinator scripts were removed from runtime installs.
- 2026-05-23T04:43+02:00: Updated coordinator provider doctrine for MCP-owned install authority and the `providers/runners`, `providers/data`, and `providers/logs` layout.
- 2026-05-21T12:35+02:00: Updated GrepAI doctrine for provider-owned mirror roots that absorb GrepAI's per-project `.grepai/` artifacts.
- 2026-05-21T11:50+02:00: Updated provider doctrine for Docker-wrapped provider backends, runtime-owned GrepAI binaries/artifacts, workspace-mode multi-root GrepAI indexing, and PostgreSQL/pgvector provider data.
- 2026-05-21T04:53+02:00: Updated provider setup doctrine so installer, benchmark preparation, and worktree preparation use the shared `provider-setup.py` entrypoint.
- 2026-05-21T02:14+02:00: Updated reinstall doctrine so enabled provider dependencies are reinstalled after disposable provider scaffolding is recreated.
- 2026-05-21T02:10+02:00: Updated the provider lifecycle doctrine when durable provider database state still lived under the former `provider-data/` root.
- 2026-05-21T01:47+02:00: Updated CGC doctrine for FalkorDB Docker only, multi-root settings, one watcher/runtime per code repo, shared backend data preservation, and explicit destructive database operations.
- 2026-05-20T19:11+02:00: Documented context provider doctrine for semantic, relationship, and intent retrieval plus CGC containment and `.env` caveats.
- 2026-05-13T13:38: Created onboarding for the coordinator settings Markdown example.
