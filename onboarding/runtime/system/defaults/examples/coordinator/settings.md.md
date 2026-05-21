# settings.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/system/defaults/examples/coordinator/settings.md`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T04:53+02:00                     |
| lastVerifiedCommitHash |                                            `0462de46a1da1bf1997e3979f4cc5bc53d1132f6`|
| lastVerifiedCommitDate |                                            2026-05-21T08:30:44+02:00|

## Purpose

This file is the human-facing coordinator settings example for `ar-coordination/system/settings.md`, including the human-readable doctrine for optional context providers.

## Code Commentary

### Logic

The example describes the coordinator as workspace-wide routing and workflow state. It lists global instructions, shared tools, workspace source registries, task/worktree roots, notes, selected memory repos, and operator conventions as coordinator-owned surfaces. The context provider section frames providers as local discovery accelerators, maps semantic discovery to GrepAI, relationship discovery to CodeGraphContext, and intent retrieval back to onboarding plus bounded source confirmation.

The CodeGraphContext guidance says one `codegraphcontext-code` provider can declare multiple code repository roots. Lifecycle tooling expands those roots into one watcher/runtime instance per configured code repo, while all instances share one lifecycle-owned FalkorDB Docker DBMS with durable state under `provider-data/codegraphcontext/falkordb/`. Reinstall/update may delete and recreate `providers/` scaffolding, requirements, venvs, patches, containers, and missing runtime files; regular reinstall then installs dependencies for providers enabled in live coordinator settings through `scripts/provider-setup.py`. Benchmark and worktree setup flows should also use `provider-setup.py` when their relevant settings enable providers, so CGC bundle seeding and fallback refresh policy stay centralized. Deleting FalkorDB data, graph namespaces, or repository indexes requires an explicit destructive lifecycle action.

### Conventions

Repo-specific rules belong in the selected memory layer rather than this coordinator settings file. Provider settings should stay declarative: configured roots, runtime locations, watch modes, freshness hooks, and transport policy belong in settings, while start/stop/status/refresh behavior belongs in shared setup/lifecycle tooling. Concrete CGC root entries should name existing code repositories; placeholder examples should not be applied as live settings.

### Invariants And Boundaries

C-08 remains the route from coordinator context into the target repository's active memory settings, tools, sources, onboarding, and ledger paths. Context providers must not replace source proof, verified onboarding, drift checks, branch validity, or memory promotion rules. Disposable CGC runtime artifacts must stay under `providers/codegraphcontext/<repo-id>/.codegraphcontext/`, durable database state must stay under `provider-data/`, and process-only env keys must not be persisted into `.env` when CGC v0.4.10 rejects them as invalid config.

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
| The context provider section defines semantic, relationship, and intent retrieval substrates, keeps provider settings declarative, and requires provider installs to be coordination-owned. | L50-L74 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |
| The CGC notes require a `roots` array of concrete code repositories, per-repo runtime instances, a shared lifecycle-owned FalkorDB Docker DBMS with durable state under `provider-data/`, process-env separation, disposable `providers/` scaffolding, default provider dependency installation during reinstall, and explicit destructive actions for database deletion. | L76-L100 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T04:53+02:00: Updated provider setup doctrine so installer, benchmark preparation, and worktree preparation use the shared `provider-setup.py` entrypoint.
- 2026-05-21T02:14+02:00: Updated reinstall doctrine so enabled provider dependencies are reinstalled after disposable provider scaffolding is recreated.
- 2026-05-21T02:10+02:00: Updated the provider lifecycle doctrine so `providers/` is disposable reinstall scaffolding and durable provider database state lives under `provider-data/`.
- 2026-05-21T01:47+02:00: Updated CGC doctrine for FalkorDB Docker only, multi-root settings, one watcher/runtime per code repo, shared backend data preservation, and explicit destructive database operations.
- 2026-05-20T19:11+02:00: Documented context provider doctrine for semantic, relationship, and intent retrieval plus CGC containment and `.env` caveats.
- 2026-05-13T13:38: Created onboarding for the coordinator settings Markdown example.
