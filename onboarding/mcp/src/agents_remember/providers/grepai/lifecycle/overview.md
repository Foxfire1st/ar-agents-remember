# mcp/src/agents_remember/providers/grepai/lifecycle/ - GrepAI Lifecycle Modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/lifecycle/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[GrepAI Provider Overview](../overview.md)

## Purpose

`grepai/lifecycle/` contains the Docker-owned GrepAI provider lifecycle
implementation, organized behind a GrepAI package facade with prefix-free
filenames.

## Hot Path Summary

`__init__.py` re-exports the GrepAI public lifecycle surface. `core.py` derives
settings, layout, workspace config, container DSNs, and Docker image settings.
`backend.py` manages PostgreSQL/pgvector, `embedder.py` manages Ollama and model
readiness, `runner.py` manages the GrepAI runner image and watcher container,
and `actions.py` composes top-level install/status/start/stop/refresh/run
behavior. Status helpers include normalized container state so MCP
current-state packets can report running state, health, and uptime; since
2.5.1 `runner.py` also reads the watcher's initial-scan log markers
(`Performing initial scan` / `Initial scan complete` since container start)
into an `initialScan` field, giving GrepAI real `indexing`/`indexed` states
instead of `unknown`.
For new `auto` host-port allocations, backend/embedder startup prefer host
`61432` for Postgres and host `61434` for Ollama while preserving the container
service ports (`5432` and `11434`) used inside the Docker network.

## Route Model

- `core.py` is configuration, layout, and workspace derivation. Since L13 its settings-backed path requires an EXPLICIT `--from-settings` file — the implicit coordination-root fallback (fail-open on a missing file) is removed.
- `backend.py` owns the Postgres container.
- `embedder.py` owns the Ollama container and configured model.
- `runner.py` owns the GrepAI image and watcher container.
- `actions.py` owns top-level GrepAI action composition.

## Invariants And Boundaries

- GrepAI remains Docker-or-bust; do not add host GrepAI or host Ollama fallbacks.
- Container-visible paths, Docker service names, and the shared Docker network
  are part of the provider contract.
- Preferred host ports avoid common neighboring service ports; container ports
  remain the service ports exposed inside the GrepAI Compose network.
- Status surfaces should include backend, embedder, and watcher container state
  so MCP current-state packets can report what is running now.
- Keep `__init__.py` as the package export facade.
- Modules in this route import context helpers from the leaf modules
  (`grepai.context`, `context.common`), never the `providers.context`
  aggregator: the aggregator star-imports this provider's context back, so
  routing through it is a circular import that breaks any entry point touching
  grepai modules first (2.5.1 fix).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The parent lifecycle facade imports the GrepAI package facade. | `_EXPORT_MODULES` | mcp/src/agents_remember/providers/lifecycle/__init__.py:9-24 |
| Provider lifecycle tests cover Docker-only GrepAI install, run, and watcher behavior. | `test_grepai_settings_backed_run_uses_docker_without_host_binary`; `test_grepai_direct_run_does_not_special_case_native_watcher_commands`; `test_grepai_runner_image_build_no_cache_inserts_flag_in_dry_run` | mcp/tests/test_provider_lifecycle_parser_1.py:109-143; mcp/tests/test_provider_lifecycle_parser_2.py:18-46; mcp/tests/test_provider_lifecycle_parser_2.py:346-358 |

## 260731-EFA-L2 — The Vocabulary Of A Stack Start

Every container in this package is started from a *resolved invocation*, and each of those used to
be a tuple or a run of parallel keywords. They are now named frozen values, and the names carry
facts the tuple positions did not:

| Type | Home | What it settles |
| --- | --- | --- |
| `GrepaiBackendContext` | `backend.py` | `settings_path`, `provider_settings`, `layout`, `backend`, `network_name`. `grepai_backend_start_context(args)` returns it; every backend command needs all of it. |
| `GrepaiEmbedderContext` | `embedder.py` | The same five for the Ollama container. `grepai_embedder_start_context(args)` returns it. |
| `GrepaiWatcherStart` | `runner.py` | `layout`, `runner`, `network`, `image` — everything a watcher start has in hand **before compose brings it up**, resolved once by `grepai_watcher_start_prerequisites` and reported verbatim in every watcher-start result. |
| `GrepaiStackResults` | `runner.py` | The lifecycle result of each container — `backend`, `embedder`, `watcher`, each optional. `grepai_docker_state(layout, stack, *, action, runner)` takes it. |
| `GrepaiServicePorts` | `core.py` | The host ports the stack publishes its dependencies on: `postgres`, `ollama`. |
| `GrepaiWorkspaceConfig` | `core.py` | What one `workspace.yaml` says — `dsn`, `embedder_settings`, `project_paths`. The three are only meaningful as one document: the watcher reads them together to know where to write vectors, how to produce them, and which container paths each indexed project lives at. |

Two of these encode a rule worth stating. `UNRESOLVED_SERVICE_PORTS` is the frozen empty
`GrepaiServicePorts` used as the default, and it means **"nothing published yet, so fall back to the
configured host port"** — the `ports.postgres or backend["postgresHostPort"]` fallback is preserved
exactly, and a caller that knows a live published port passes it. And `GrepaiWatcherStart` is
deliberately the *pre*-compose set: adding a post-start fact to it would make the watcher-start
result claim something compose had not yet done.

`backend.py` and the CGC backend both take `BackendStartReconciliation` from
`providers/lifecycle/compose_runtime.py` — the shared record of what a start already did to the
host (network adoption, unmanaged-project migration, forced removal of a container whose data mount
no longer matches).

`core.py` builds its layout through `GrepaiWorkspace(...)` / `GrepaiInstance(...)` (see the
[context route](../context/overview.md)). No container topology, port preference, DSN, initial-scan
reading or settings rule changed.

## Update History

- 2026-08-04T18:42+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the two malformed rows — the
  parent facade row bound to `_EXPORT_MODULES` (providers/lifecycle/__init__.py:8-35, the
  lazy-import list carrying the GrepAI facade) and the test-coverage row bound to the three
  Docker-only/watcher/install test methods with their exact extents in test_provider_lifecycle.py.
  Claim wording unchanged.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: the resolved-invocation tuples became named frozen values
  — `GrepaiBackendContext`, `GrepaiEmbedderContext`, `GrepaiWatcherStart`, `GrepaiStackResults`,
  `GrepaiServicePorts` (+ `UNRESOLVED_SERVICE_PORTS`) and `GrepaiWorkspaceConfig` — and both
  backends now share `BackendStartReconciliation` from the provider-agnostic lifecycle package.
  Container topology, ports, DSNs, `initialScan` reading and the `--from-settings` rule are
  unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-06T23:55+02:00 — L13 owner follow-up (body): core.py's explicit --from-settings requirement stated in the route model (the earlier ride-along was history-only). Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T23:10+02:00 — 260703-L13 ride-along: `core.py`'s
  `grepai_layout_from_args` reads provider settings via the explicit `--from-settings` path
  only (the implicit coordinator-settings fallback was deleted; manual `--root`/
  `--runtime-root` layouts now require the flag — an empty JSON object reproduces the old
  empty-default behavior explicitly). Route model unchanged. Verification metadata pinned
  until closeout stamps the L13 commit.

- 2026-06-25T09:55+02:00 — GrepAI backend/embedder startup now prefer host `61432`/`61434` for auto host publication while keeping Postgres/Ollama container ports at `5432`/`11434`.
- 2026-06-10T07:40+02:00 — No route impact: `actions.py`/`backend.py`/`core.py`/`embedder.py` only updated the shared-helper import path to `providers/context_common.py` (GitHub #58).
- 2026-06-10T05:30+02:00 — Route body caught up with 2.5.1: `initialScan` scan-marker reading in `runner.py` and the leaf-import invariant (circular-import fix). Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-06-06T12:15: Re-verified against the current GrepAI lifecycle package; backend, embedder, runner, and action composition still match.
- 2026-05-28T12:32+02:00: Updated after GrepAI backend/embedder/watcher status began surfacing container-state summaries for provider current-state reporting.
- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/grepai/lifecycle/` route.
- 2026-05-25T19:09+02:00: Created when flat `grepai_*` lifecycle modules moved under `lifecycle_modules/grepai/` with prefix-free filenames.
