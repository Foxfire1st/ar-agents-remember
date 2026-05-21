# context_providers.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-21T23:18+02:00                     |
| lastVerifiedCommitHash | `00aae9dad3d8740e10a41ab285f87ecab8608745` |
| lastVerifiedCommitDate | 2026-05-21T23:53:08+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

`context_providers.py` centralizes local provider runtime layout, settings expansion, runtime cleanup, and patch helpers for optional context providers. It gives provider lifecycle tooling a deterministic way to create contained CodeGraphContext and GrepAI provider surfaces while keeping disposable provider runtime scaffolding under `ar-coordination/providers/`, runtime-owned binaries under `providers/_bin/`, and durable provider database state under `ar-coordination/provider-data/`.

## Code Commentary

### Logic

The module defines provider ids, the full pinned CGC requirements set, pinned GrepAI requirement, CGC patch ids, FalkorDB Docker defaults, GrepAI PostgreSQL Docker defaults, provider artifact names that are forbidden in indexed roots, and the default managed `.cgcignore`. The CGC patch ids include the visualizer repo-query patch, which replaces the default full-repo variable-length traversal with a bounded path-prefix query for large repositories, plus visualizer route patches that redirect the local server root to the explorer and make unknown `/api/*` routes return JSON 404 instead of the SPA HTML fallback. `CgcRuntimeLayout` computes all runtime paths from a coordination root, stable repo id, and code repository root: provider instance root, `.codegraphcontext` root, shared provider venv, requirements file, patches root, state file, config files, shared backend root under `provider-data`, backend data root, backend state file, run/home/appdata directories, and logs directory.

`cgc_runtime_layout_from_provider_settings` expands `contextProviders.providers.codegraphcontext-code` entries. It requires each configured root path to resolve to an existing directory, reads resolved FalkorDB ports from backend state when available, folds provider-level and root-level `cgcignorePatterns` together, and builds the per-repo process environment from `processEnvTemplate`. The process environment uses `falkordb-remote`, per-repo `FALKORDB_GRAPH_NAME`, and isolated `HOME`/`USERPROFILE`/`APPDATA`/`LOCALAPPDATA` directories under the CGC runtime root.

`ensure_cgc_runtime_layout` creates provider directories and writes default requirements, managed `.cgcignore`, `config.yaml`, and persisted `.env` files. Its fallback requirements writer emits the full CGC provider set, including Tree-Sitter parser dependencies, so a partial/older runtime does not silently reinstall a file-only CGC graph. The managed `.cgcignore` inherits useful top-level `.gitignore` entries from the indexed source repo and adds configured `cgcignorePatterns`, while runtime-only CGC/FalkorDB keys stay in process env because CGC v0.4.10 rejects them as persisted config keys.

`GrepaiRuntimeLayout` models workspace-mode GrepAI memory indexing. It expands one `grepai-memory` provider into explicit `{ projectId, path }` memory roots, keeps the GrepAI binary at `providers/_bin/grepai`, writes the applied workspace config under `providers/grepai/home/.grepai/workspace.yaml`, keeps GrepAI logs/state/cache/home under `providers/grepai/`, and stores the shared PostgreSQL/pgvector backend data under `provider-data/grepai/postgres/data`. Managed settings default to provider-owned mirror roots under `providers/grepai/index-roots/` because GrepAI still writes `.grepai/config.yaml` and `.grepai/symbols.gob` beside each configured project path. Workspace config generation names each mirror root as a GrepAI project, points the store at PostgreSQL through a DSN, writes concrete embedder endpoint/dimension values for local Ollama defaults, and carries embedder settings without writing config into durable memory roots.

`cleanup_cgc_runtime_artifacts` is the live-runtime reconciliation guard for already-installed provider scaffolding. It removes unconfigured generated CGC instance directories under `providers/codegraphcontext/`, such as an accidentally materialized example `my-app`, and removes legacy embedded-backend artifacts named `db`, `global`, `kuzu`, or `kuzu.wal` from configured instances. `remove_grepai_root_provider_artifacts` performs the GrepAI equivalent for deprecated root `.grepai/` state: it only removes recognized direct-child GrepAI artifacts from configured indexed roots after path validation, because GrepAI cache/index state is disposable tooling rather than durable onboarding. Durable FalkorDB and PostgreSQL/pgvector data are not under those cleanup trees; reinstall handles broader idempotence by wiping and recreating `providers/` while preserving `provider-data/`.

Patch helpers locate CGC's installed `cgcignore.py`, FalkorDB writer, graph-builder, discovery, visualizer server, and CLI helper modules inside the provider venv. They detect Agents Remember patch markers and idempotently patch CGC v0.4.10 so managed `.cgcignore` files live in the runtime root, Windows delete queries use legal relationship syntax, additional source extensions are indexed, TableGen files are discoverable, the visualizer repo graph query uses bounded path-prefix matching instead of timing out on large repo traversals, and the local visualizer entrypoint opens at the actual explorer route instead of the packaged public landing page.

### Conventions

- One CGC provider venv is shared per coordination root at `providers/_venvs/codegraphcontext`.
- One CGC provider instance root exists per configured code repo at `providers/codegraphcontext/<repo-id>`.
- One FalkorDB Docker backend is shared by all configured CGC instances with durable state at `provider-data/codegraphcontext/falkordb/`.
- Each configured code repo gets a separate FalkorDB graph name, `cgc_<repo-id>`, with dashes normalized to underscores.
- CGC runtime config, ignore rules, logs, run files, and per-instance state are kept under the provider runtime root.
- GrepAI requirements are managed through the same provider requirements helper pattern as CGC, but the executable is a runtime-owned release binary under `providers/_bin/` rather than a global command or a Python venv command.
- One GrepAI workspace can index multiple external memory repos and repo-internal `ar-memory/` roots by assigning each configured root a stable project id.
- GrepAI config, logs, state, cache, home files, and managed mirror roots are provider artifacts under `providers/grepai/`; the shared PostgreSQL/pgvector database data is the durable provider-data surface under `provider-data/grepai/postgres/`.
- Provider output is discovery evidence only; this helper does not normalize query results or make source-truth claims.

### Invariants And Boundaries

The helper must not write authoritative provider artifacts into indexed source repositories or indexed memory roots. If `.cgcignore`, `.codegraphcontext`, or `CGC_REPORT.md` appears in a code repo, `assert_no_source_provider_artifacts` raises a provider error and managed CGC mode should not be trusted until cleaned up. If `.grepai/` appears in any configured GrepAI memory root, it is deprecated disposable GrepAI cache, not durable memory: assertion helpers can still flag it, and lifecycle cleanup can remove it after recognized-name and direct-child path validation. Runtime cleanup may delete provider-owned stale scaffolding, disposable GrepAI root artifacts, and legacy embedded-backend files, but it must not delete durable database state under `provider-data/` or arbitrary paths outside validated cleanup targets.

### Todos

- Add lifecycle smoke coverage that runs CGC against a tiny temporary repository once the provider package is available without network setup.
- Add explicit lifecycle-state reporting so operators can distinguish install, backend, index, watch, and stale-root states without reading raw provider JSON.

## Docs References

No external documentation is cited here. The module encodes repository-local provider layout and patch behavior discovered during the C-04 provider spike.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Constants define the CGC provider id, full pinned CGC requirements set, FalkorDB backend defaults, visualizer patch ids, pinned GrepAI requirement, GrepAI PostgreSQL backend defaults, forbidden provider artifact names, and process-only `.env` exclusions. | L15-L55 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| The visualizer repo-query patch replaces CGC's default `CONTAINS*0..` repo traversal with a bounded path-prefix query limited to 3000 repo nodes and 5000 returned rows, preventing large repos from timing out in `/api/graph`. | L233-L259; L1306-L1323 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| The visualizer route patches update CGC's FastAPI server to redirect `/` to the configured explorer route, return JSON 404 for unknown `/api/*` routes, and update the CLI helper to pass that default explorer route into `run_server`. | L260-L319; L1326-L1384 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| `CgcRuntimeLayout` derives the provider instance, `.codegraphcontext`, venv, requirements, patches, state, provider-data FalkorDB backend, run/home/appdata, and logs paths plus process env. | L264-L333 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| `GrepaiRuntimeLayout` derives provider-owned GrepAI workspace, config, state, logs, home, run, cache, binary, and PostgreSQL backend paths, plus HOME/XDG environment values that keep GrepAI runtime state under `providers/grepai`. | L336-L380 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| GrepAI settings expansion requires a non-empty `roots` array, expands workspace/coordinator placeholders, rejects missing paths or duplicate project ids, derives backend data roots under `provider-data/grepai/postgres`, defaults to provider-owned mirror roots under `providers/grepai/index-roots/`, syncs mirrors while excluding `.git`, `.grepai`, and `__pycache__`, and writes workspace config with PostgreSQL store, concrete local embedder endpoint/dimension defaults, and named projects. | L450-L722 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| `cgc_runtime_layout_from_provider_settings` expands configured roots, rejects unresolved or missing code repository paths, resolves backend ports, merges `cgcignorePatterns`, and builds watch paths. | L694-L829 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| `ensure_cgc_runtime_layout` creates default provider files, writes the full CGC requirements fallback, inherits source `.gitignore` entries into the managed `.cgcignore`, and excludes CGC/FalkorDB runtime keys from persisted `.env`. | L832-L868 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| Source and GrepAI artifact checks detect `.cgcignore`, `.codegraphcontext`, `CGC_REPORT.md`, or `.grepai/` in source and durable memory roots before managed provider output is trusted. | L1041-L1062 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| GrepAI disposable artifact cleanup removes only recognized direct-child `.grepai/` artifacts from configured indexed roots after path validation, and shared runtime removal treats symlinks as unlink targets rather than directory trees. | L1065-L1094 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| Runtime cleanup removes unconfigured generated CGC instances and legacy embedded backend artifacts from disposable provider scaffolding. | L1097-L1133 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| Patch helpers find CGC's installed ignore, writer, graph-builder, discovery, visualizer server, and CLI helper modules, detect patch markers, and apply the managed `.cgcignore`, Windows delete-query, C++ extension, TableGen discovery, visualizer repo-query, and visualizer route patches idempotently. | L1118-L1384 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |

## Cross-Repo References

No sibling repository evidence is needed for this helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T23:18+02:00: Updated after adding disposable GrepAI root artifact cleanup with direct-child path validation and symlink-safe runtime removal.
- 2026-05-21T13:22+02:00: Updated CGC patch coverage for local visualizer routing so `/` redirects to the explorer and unknown `/api/*` paths return JSON instead of SPA HTML.
- 2026-05-21T12:40+02:00: Updated CGC patch coverage for the visualizer repo graph query so large repositories use a bounded path-prefix query instead of the default traversal that times out.
- 2026-05-21T12:35+02:00: Updated for provider-owned GrepAI mirror roots so GrepAI's unavoidable per-project `.grepai/` artifacts stay under `providers/grepai/index-roots/` rather than durable memory roots.
- 2026-05-21T12:20+02:00: Updated GrepAI workspace config notes for explicit Ollama endpoint/dimension defaults when the runtime writes `workspace.yaml` directly.
- 2026-05-21T11:50+02:00: Updated for GrepAI workspace-mode multi-root memory indexing, runtime-owned GrepAI binaries/config/logs/state, Docker PostgreSQL/pgvector provider-data, and `.grepai/` containment checks for indexed memory roots.
- 2026-05-21T02:50+02:00: Updated for full CGC requirements fallback including Tree-Sitter parser dependencies.
- 2026-05-21T02:10+02:00: Updated for `provider-data/` as the durable FalkorDB backend root and `providers/` as disposable reinstall scaffolding.
- 2026-05-21T01:47+02:00: Updated for FalkorDB-only CGC backend behavior, multi-root settings expansion, managed `.cgcignore` inheritance, runtime cleanup of stale `my-app`/Kuzu artifacts, and the second CGC patch.
- 2026-05-20T19:11+02:00: Created onboarding for the new context provider layout and patch helper. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
