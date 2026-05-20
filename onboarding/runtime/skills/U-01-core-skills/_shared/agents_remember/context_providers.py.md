# context_providers.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-20T20:01+02:00                     |
| lastVerifiedCommitHash | `e4ae4955d888d3ce58b55b5ca99d20039cbcb214` |
| lastVerifiedCommitDate | 2026-05-20T20:01:26+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

`context_providers.py` centralizes local provider runtime layout and patch helpers for optional context providers, starting with CodeGraphContext. It gives provider lifecycle tooling a deterministic way to create contained CGC runtime roots, detect source-repo artifacts, verify the installed CGC patch, and write provider state.

## Code Commentary

### Logic

The module defines the CGC provider name, pinned package requirement, patch id, source artifact names that are forbidden in indexed code repos, and the default managed `.cgcignore`. `CgcRuntimeLayout` computes all runtime paths from a coordination root, stable repo id, and code repository root: provider instance root, `.codegraphcontext` root, shared provider venv, requirements file, patches root, state file, config files, KuzuDB path, run directory, and logs directory.

`ensure_cgc_runtime_layout` creates the provider directories and writes default requirements, `.cgcignore`, `config.yaml`, and `.env` files. Runtime-only keys such as `CGC_RUNTIME_DB_TYPE`, `KUZUDB_PATH`, and `CGC_RUNTIME_DB_PATH` stay in process env and are intentionally excluded from the persisted `.env` file because CGC v0.4.10 reports them as invalid persisted config keys.

Patch helpers locate `codegraphcontext/core/cgcignore.py` inside the provider venv, detect the Agents Remember patch marker, and idempotently replace CGC's repo-local `.cgcignore` creation snippet so an explicit ignore path can win before falling back to the indexed source repo.

### Conventions

- One CGC provider venv is shared per coordination root at `providers/_venvs/codegraphcontext`.
- One CGC provider instance root exists per code repo at `providers/codegraphcontext/<repo-id>`.
- CGC runtime config, ignore rules, KuzuDB data, logs, run files, and state are kept under the provider runtime root.
- Provider output is discovery evidence only; this helper does not normalize query results or make source-truth claims.

### Invariants And Boundaries

The helper must not write provider artifacts into indexed source repositories. If `.cgcignore`, `.codegraphcontext`, or `CGC_REPORT.md` appears in a code repo, `assert_no_source_provider_artifacts` raises a provider error and managed CGC mode should not be trusted until cleaned up.

### Todos

- Add lifecycle smoke coverage that runs CGC against a tiny temporary repository once the provider package is available without network setup.

## Docs References

No external documentation is cited here. The module encodes repository-local provider layout and patch behavior discovered during the C-04 provider spike.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Constants define the CGC provider id, pinned package, patch id, forbidden source artifact names, and process-only `.env` exclusions. | L13-L24 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| `CgcRuntimeLayout` and `cgc_runtime_layout` derive provider instance, `.codegraphcontext`, venv, requirements, patches, state, db, run, and logs paths. | L73-L145 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| `ensure_cgc_runtime_layout` creates default provider files and excludes process-only CGC runtime keys from the persisted `.env`. | L148-L175 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| Source artifact detection treats `.cgcignore`, `.codegraphcontext`, and `CGC_REPORT.md` as source-repo contamination. | L193-L204 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| Patch helpers find CGC's installed `cgcignore.py`, detect the patch marker, and replace the repo-local `.cgcignore` creation snippet idempotently. | L207-L235 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |

## Cross-Repo References

No sibling repository evidence is needed for this helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-20T19:11+02:00: Created onboarding for the new context provider layout and patch helper. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
