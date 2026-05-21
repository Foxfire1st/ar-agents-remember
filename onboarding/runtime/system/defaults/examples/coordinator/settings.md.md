# settings.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/system/defaults/examples/coordinator/settings.md`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T11:50+02:00                     |
| lastVerifiedCommitHash |                                            `5ff4ed4ef94b5576a45059de8ac7c03e8c4c04a1`|
| lastVerifiedCommitDate |                                            2026-05-21T18:12:00+02:00|

## Purpose

This file is the human-facing coordinator settings example for `ar-coordination/system/settings.md`, including the human-readable doctrine for optional context providers.

## Code Commentary

### Logic

The example describes the coordinator as workspace-wide routing and workflow state. It lists global instructions, shared tools, workspace source registries, task/worktree roots, notes, selected memory repos, and operator conventions as coordinator-owned surfaces. The context provider section frames providers as local discovery accelerators, maps semantic discovery to GrepAI, relationship discovery to CodeGraphContext, and intent retrieval back to onboarding plus bounded source confirmation.

The provider install guidance says installs should be coordination-owned: pinned requirements under `providers/requirements/`, runtime-owned binaries under `providers/_bin/`, one reusable virtual environment per Python provider type under `providers/_venvs/`, and patches under `providers/patches/`. Providers that need databases or daemonized infrastructure should prefer Docker-wrapped backends and must not require host-level PostgreSQL, FalkorDB, OS services, launch agents, package-manager services, or global user daemons for normal managed mode.

The GrepAI guidance says one `grepai-memory` provider can declare multiple memory roots in workspace mode, covering both external memory repos and repo-internal `ar-memory/` roots with explicit `{ projectId, path }` entries. Managed lifecycle tooling mirrors those roots into provider-owned index roots before launching GrepAI because GrepAI still writes per-project symbol/config artifacts beside each configured project path. GrepAI config, logs, state, cache, home files, and mirrored index roots live under `providers/grepai/`, while all memory roots share one lifecycle-owned PostgreSQL/pgvector Docker DBMS with durable state under `provider-data/grepai/postgres/`. A `.grepai/` directory inside any indexed memory root is a containment failure rather than durable memory.

The CodeGraphContext guidance says one `codegraphcontext-code` provider can declare multiple code repository roots. Lifecycle tooling expands those roots into one watcher/runtime instance per configured code repo, while all instances share one lifecycle-owned FalkorDB Docker DBMS with durable state under `provider-data/codegraphcontext/falkordb/`. Reinstall/update may delete and recreate `providers/` scaffolding, requirements, venvs, patches, containers, and missing runtime files; regular reinstall then installs dependencies for providers enabled in live coordinator settings through `scripts/provider-setup.py`. Benchmark and worktree setup flows should also use `provider-setup.py` when their relevant settings enable providers, so CGC bundle seeding and fallback refresh policy stay centralized. Deleting FalkorDB data, graph namespaces, repository indexes, or GrepAI PostgreSQL data requires an explicit destructive lifecycle action.

### Conventions

Repo-specific rules belong in the selected memory layer rather than this coordinator settings file. Provider settings should stay declarative: configured roots, runtime locations, watch modes, freshness hooks, and transport policy belong in settings, while start/stop/status/refresh behavior belongs in shared setup/lifecycle tooling. Concrete GrepAI and CGC root entries should name existing memory or code repository directories; placeholder examples should not be applied as live settings.

### Invariants And Boundaries

C-08 remains the route from coordinator context into the target repository's active memory settings, tools, sources, onboarding, and ledger paths. Context providers must not replace source proof, verified onboarding, drift checks, branch validity, or memory promotion rules. Disposable GrepAI runtime artifacts must stay under `providers/grepai/`, disposable CGC runtime artifacts must stay under `providers/codegraphcontext/<repo-id>/.codegraphcontext/`, durable database state must stay under `provider-data/`, and process-only env keys must not be persisted into `.env` when CGC v0.4.10 rejects them as invalid config.

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
| The example states that coordinator settings are workspace-wide and do not replace per-repository memory settings. | L1-L8 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |
| The scope list names global instructions, shared commands, workspace sources, roots, notes, selected memory repos, and operator conventions as coordinator concerns. | L10-L25 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |
| The routing section tells agents to invoke C-08 and treat repository-specific memory guidance as more specific. | L40-L48 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |
| The context provider section defines semantic, relationship, and intent retrieval substrates, keeps provider settings declarative, routes setup through `provider-setup.py`, and requires provider installs to be coordination-owned with runtime-owned binaries, provider venvs, patches, and Docker-wrapped backend services instead of host-level services or global daemons. | L50-L86 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |
| The GrepAI notes require a workspace-mode `roots` array for external memory repos and repo-internal `ar-memory/` roots, mirror roots into provider-owned index roots, keep GrepAI config/log/state/mirrors under `providers/grepai/`, store durable PostgreSQL/pgvector data under `provider-data/grepai/postgres/`, and treat `.grepai/` inside indexed memory roots as a containment failure. | L88-L99 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |
| The CGC notes require a `roots` array of concrete code repositories, per-repo runtime instances, a shared lifecycle-owned FalkorDB Docker DBMS with durable state under `provider-data/`, process-env separation, disposable `providers/` scaffolding, default provider dependency installation during reinstall, and explicit destructive actions for database deletion. | L98-L122 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T12:35+02:00: Updated GrepAI doctrine for provider-owned mirror roots that absorb GrepAI's per-project `.grepai/` artifacts.
- 2026-05-21T11:50+02:00: Updated provider doctrine for Docker-wrapped provider backends, runtime-owned GrepAI binaries/artifacts, workspace-mode multi-root GrepAI indexing, and PostgreSQL/pgvector provider data.
- 2026-05-21T04:53+02:00: Updated provider setup doctrine so installer, benchmark preparation, and worktree preparation use the shared `provider-setup.py` entrypoint.
- 2026-05-21T02:14+02:00: Updated reinstall doctrine so enabled provider dependencies are reinstalled after disposable provider scaffolding is recreated.
- 2026-05-21T02:10+02:00: Updated the provider lifecycle doctrine so `providers/` is disposable reinstall scaffolding and durable provider database state lives under `provider-data/`.
- 2026-05-21T01:47+02:00: Updated CGC doctrine for FalkorDB Docker only, multi-root settings, one watcher/runtime per code repo, shared backend data preservation, and explicit destructive database operations.
- 2026-05-20T19:11+02:00: Documented context provider doctrine for semantic, relationship, and intent retrieval plus CGC containment and `.env` caveats.
- 2026-05-13T13:38: Created onboarding for the coordinator settings Markdown example.
