# context_providers.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-21T02:50+02:00                     |
| lastVerifiedCommitHash | `0462de46a1da1bf1997e3979f4cc5bc53d1132f6` |
| lastVerifiedCommitDate | 2026-05-21T08:30:44+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

`context_providers.py` centralizes local provider runtime layout, settings expansion, runtime cleanup, and patch helpers for optional context providers. It gives provider lifecycle tooling a deterministic way to create contained CodeGraphContext and GrepAI provider surfaces while keeping disposable CGC runtime scaffolding under `ar-coordination/providers/` and durable database state under `ar-coordination/provider-data/`.

## Code Commentary

### Logic

The module defines provider ids, the full pinned CGC requirements set, pinned GrepAI requirement, CGC patch ids, FalkorDB Docker defaults, source artifact names that are forbidden in indexed code repos, and the default managed `.cgcignore`. `CgcRuntimeLayout` computes all runtime paths from a coordination root, stable repo id, and code repository root: provider instance root, `.codegraphcontext` root, shared provider venv, requirements file, patches root, state file, config files, shared backend root under `provider-data`, backend data root, backend state file, run/home/appdata directories, and logs directory.

`cgc_runtime_layout_from_provider_settings` expands `contextProviders.providers.codegraphcontext-code` entries. It requires each configured root path to resolve to an existing directory, reads resolved FalkorDB ports from backend state when available, folds provider-level and root-level `cgcignorePatterns` together, and builds the per-repo process environment from `processEnvTemplate`. The process environment uses `falkordb-remote`, per-repo `FALKORDB_GRAPH_NAME`, and isolated `HOME`/`USERPROFILE`/`APPDATA`/`LOCALAPPDATA` directories under the CGC runtime root.

`ensure_cgc_runtime_layout` creates provider directories and writes default requirements, managed `.cgcignore`, `config.yaml`, and persisted `.env` files. Its fallback requirements writer emits the full CGC provider set, including Tree-Sitter parser dependencies, so a partial/older runtime does not silently reinstall a file-only CGC graph. The managed `.cgcignore` inherits useful top-level `.gitignore` entries from the indexed source repo and adds configured `cgcignorePatterns`, while runtime-only CGC/FalkorDB keys stay in process env because CGC v0.4.10 rejects them as persisted config keys.

`cleanup_cgc_runtime_artifacts` is the live-runtime reconciliation guard for already-installed provider scaffolding. It removes unconfigured generated CGC instance directories under `providers/codegraphcontext/`, such as an accidentally materialized example `my-app`, and removes legacy embedded-backend artifacts named `db`, `global`, `kuzu`, or `kuzu.wal` from configured instances. Durable FalkorDB data is not under that tree; reinstall handles broader idempotence by wiping and recreating `providers/` while preserving `provider-data/`.

Patch helpers locate CGC's installed `cgcignore.py` and FalkorDB writer module inside the provider venv, detect Agents Remember patch markers, and idempotently patch CGC v0.4.10 so managed `.cgcignore` files live in the runtime root and Windows delete queries use legal relationship syntax.

### Conventions

- One CGC provider venv is shared per coordination root at `providers/_venvs/codegraphcontext`.
- One CGC provider instance root exists per configured code repo at `providers/codegraphcontext/<repo-id>`.
- One FalkorDB Docker backend is shared by all configured CGC instances with durable state at `provider-data/codegraphcontext/falkordb/`.
- Each configured code repo gets a separate FalkorDB graph name, `cgc_<repo-id>`, with dashes normalized to underscores.
- CGC runtime config, ignore rules, logs, run files, and per-instance state are kept under the provider runtime root.
- GrepAI requirements are managed through the same provider requirements helper pattern as CGC.
- Provider output is discovery evidence only; this helper does not normalize query results or make source-truth claims.

### Invariants And Boundaries

The helper must not write provider artifacts into indexed source repositories. If `.cgcignore`, `.codegraphcontext`, or `CGC_REPORT.md` appears in a code repo, `assert_no_source_provider_artifacts` raises a provider error and managed CGC mode should not be trusted until cleaned up. Runtime cleanup may delete provider-owned stale scaffolding and legacy embedded-backend files under `providers/`, but it must not delete durable database state under `provider-data/` or arbitrary paths outside the provider runtime tree.

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
| Constants define the CGC provider id, full pinned CGC requirements set, FalkorDB backend defaults, pinned GrepAI requirement, forbidden source artifact names, and process-only `.env` exclusions. | L13-L39 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| `CgcRuntimeLayout` derives the provider instance, `.codegraphcontext`, venv, requirements, patches, state, provider-data FalkorDB backend, run/home/appdata, and logs paths plus process env. | L167-L210 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| `cgc_runtime_layout_from_provider_settings` expands configured roots, rejects unresolved or missing code repository paths, resolves backend ports, merges `cgcignorePatterns`, and builds watch paths. | L351-L466 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| `ensure_cgc_runtime_layout` creates default provider files, writes the full CGC requirements fallback, inherits source `.gitignore` entries into the managed `.cgcignore`, and excludes CGC/FalkorDB runtime keys from persisted `.env`. | L490-L542 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| Runtime cleanup removes unconfigured generated CGC instances and legacy embedded backend artifacts from disposable provider scaffolding. | L559-L595 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| Patch helpers find CGC's installed ignore and writer modules, detect patch markers, and apply the managed `.cgcignore` plus Windows delete-query patches idempotently. | L595-L707 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |

## Cross-Repo References

No sibling repository evidence is needed for this helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T02:50+02:00: Updated for full CGC requirements fallback including Tree-Sitter parser dependencies.
- 2026-05-21T02:10+02:00: Updated for `provider-data/` as the durable FalkorDB backend root and `providers/` as disposable reinstall scaffolding.
- 2026-05-21T01:47+02:00: Updated for FalkorDB-only CGC backend behavior, multi-root settings expansion, managed `.cgcignore` inheritance, runtime cleanup of stale `my-app`/Kuzu artifacts, and the second CGC patch.
- 2026-05-20T19:11+02:00: Created onboarding for the new context provider layout and patch helper. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
