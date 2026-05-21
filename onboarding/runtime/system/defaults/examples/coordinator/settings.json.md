# settings.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/system/defaults/examples/coordinator/settings.json` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T11:50+02:00                     |
| lastVerifiedCommitHash | `5ff4ed4ef94b5576a45059de8ac7c03e8c4c04a1` |
| lastVerifiedCommitDate | 2026-05-21T18:12:00+02:00|

## Purpose

This JSON example models machine-readable coordinator layout hints, including optional context provider declarations for semantic and relationship discovery.

## Code Commentary

### Logic

The example has a `coordination` block for task, worktree, notes, and memory-repo folder names, plus a `memoryRepos` block for external-topology defaults and selected repository entries. It also defines optional `contextProviders` examples: a GrepAI semantic provider in workspace mode with explicit roots for external memory repos and repo-internal `ar-memory/` roots, and a CodeGraphContext relationship provider with a `roots` array of repository entries.

The GrepAI provider example is disabled and uses non-runnable placeholders so copying the example verbatim should not silently index real memory. When activated in a real coordinator, each root needs a concrete `projectId` and existing `path`. The provider config keeps GrepAI runtime state under `providers/grepai/`, installs the pinned GrepAI release binary through the runtime requirements path, records provider state under the runtime root, enables provider-owned mirror roots, writes explicit Ollama endpoint and dimension settings, and points GrepAI at a lifecycle-owned PostgreSQL/pgvector Docker backend with durable data under `provider-data/grepai/postgres/`. Its watch block runs by workspace name and writes logs under the provider runtime root rather than inside an indexed memory root.

The CGC provider example is disabled and uses non-runnable placeholders for repository roots so copying the example verbatim should not silently create concrete provider instances. When activated in a real coordinator, each root needs a concrete `repoId` and existing `path`; lifecycle tooling expands those entries into one runtime instance per repo. The provider config points all instances at one lifecycle-owned FalkorDB Docker backend with browser support, durable backend data under `provider-data/`, a shared provider venv, pinned requirements file, patch root, state-file template, explicit process environment, managed foreground watch mode, and watcher-first freshness hooks.

### Conventions

The file intentionally describes coordinator routing rather than onboarding storage or repository-specific path rules. Provider output is configured as discovery-only and source-proof-required so specialized retrieval tools produce candidates rather than final truth. GrepAI `roots` make multi-location memory indexing explicit instead of relying on a generated `memory-repos/.grepai` project state. Per-root `cgcignorePatterns` allow a repository to exclude generated or heavy paths in addition to the managed `.cgcignore` defaults and inherited source `.gitignore` entries.

### Invariants And Boundaries

Durable repo policy should remain in the selected memory repo's `settings.json`; this coordinator JSON is for workspace-level routing and defaults. Disposable provider paths must remain under the coordination runtime, and provider instances must keep logs, config, run files, state, `.cgcignore`, `.codegraphcontext`, and `.grepai/` out of indexed code repositories and memory roots. FalkorDB and GrepAI PostgreSQL data are stored under `provider-data/`, preserved by reinstall/update flows, and should be deleted only through explicit destructive provider actions.

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
| The JSON example declares coordinator folder names under `coordination` and keeps memory-repo routing separate from repo-specific memory settings. | L1-L12 | [runtime/system/defaults/examples/coordinator/settings.json](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.json) |
| The GrepAI provider example is a disabled semantic memory provider in workspace mode with explicit external-memory and repo-internal roots, `mirrorRoots`, runtime-owned GrepAI paths under `providers/grepai`, a pinned requirements file, provider state file, concrete Ollama embedder endpoint/dimensions, Docker PostgreSQL/pgvector backend, provider-owned watch logs, and C-03/C-05 freshness hooks. | L13-L72 | [runtime/system/defaults/examples/coordinator/settings.json](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.json) |
| The CGC provider example is a disabled relationship provider with a `roots` array, non-runnable placeholder root entries, per-root `cgcignorePatterns`, provider runtime root, shared venv, pinned requirements file, patch root, and state-file template. | L73-L95 | [runtime/system/defaults/examples/coordinator/settings.json](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.json) |
| The CGC backend example selects a shared FalkorDB Docker backend with pinned image, image lock file, `provider-data` backend root, container name, and auto-allocated FalkorDB/browser ports. | L96-L117 | [runtime/system/defaults/examples/coordinator/settings.json](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.json) |
| The CGC process env template selects `falkordb-remote`, isolates HOME-like directories under the instance runtime root, sets per-repo FalkorDB graph names, and disables CGC auto-watch. | L117-L132 | [runtime/system/defaults/examples/coordinator/settings.json](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.json) |
| The watch and freshness blocks require managed foreground watchers before source edits and branch switches, with hard refreshes left explicit-only. | L133-L144 | [runtime/system/defaults/examples/coordinator/settings.json](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.json) |
| The provider policy marks provider output as discovery-only and still requires source proof. | L147-L157 | [runtime/system/defaults/examples/coordinator/settings.json](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.json) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T12:35+02:00: Added `mirrorRoots` to the GrepAI example so managed mode indexes provider-owned mirrors instead of letting GrepAI create `.grepai/` artifacts in durable memory roots.
- 2026-05-21T12:20+02:00: Added explicit Ollama endpoint and dimensions to the GrepAI embedder example so direct workspace config generation does not rely on interactive defaults.
- 2026-05-21T11:50+02:00: Updated the GrepAI example for workspace-mode multi-root memory indexing, runtime-owned GrepAI artifacts, and Docker PostgreSQL/pgvector provider data.
- 2026-05-21T02:10+02:00: Updated the CGC backend example so durable FalkorDB data lives under `provider-data/` instead of the disposable `providers/` tree.
- 2026-05-21T01:47+02:00: Updated the CGC provider example for FalkorDB Docker only, multiple configured roots, non-runnable placeholders instead of concrete `my-app` examples, process-env templates, and watcher-first freshness behavior.
- 2026-05-20T19:11+02:00: Documented the optional `contextProviders` settings shape for GrepAI semantic discovery and CodeGraphContext relationship discovery.
- 2026-05-13T13:38: Created onboarding for the coordinator settings JSON example.
