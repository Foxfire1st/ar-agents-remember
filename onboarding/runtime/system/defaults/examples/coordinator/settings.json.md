# settings.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/system/defaults/examples/coordinator/settings.json` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-20T20:01+02:00                     |
| lastVerifiedCommitHash | `e4ae4955d888d3ce58b55b5ca99d20039cbcb214` |
| lastVerifiedCommitDate | 2026-05-20T20:01:26+02:00 |

## Purpose

This JSON example models machine-readable coordinator layout hints, including optional context provider declarations for semantic and relationship discovery.

## Code Commentary

### Logic

The example has a `coordination` block for task, worktree, notes, and memory-repo folder names, plus a `memoryRepos` block for external-topology defaults and selected repository entries. It also defines optional `contextProviders` examples: a GrepAI semantic provider over `<coordination_root>/memory-repos`, and a CodeGraphContext relationship provider with a per-repo runtime root, shared provider venv, pinned requirements file, patch root, provider state file, explicit runtime env, managed foreground watch mode, and freshness hooks.

### Conventions

The file intentionally describes coordinator routing rather than onboarding storage or repository-specific path rules. Provider output is configured as discovery-only and source-proof-required so specialized retrieval tools produce candidates rather than final truth.

### Invariants And Boundaries

Durable repo policy should remain in the selected memory repo's `settings.json`; this coordinator JSON is for workspace-level routing and defaults. Provider paths must remain under the coordination runtime, and CGC provider instances must keep KuzuDB, logs, `.cgcignore`, config, and state out of indexed code repositories.

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
| The GrepAI provider example is a disabled semantic memory provider rooted at `<coordination_root>/memory-repos`, with runtime logs under `providers/grepai/memory-repos`. | L13-L30 | [runtime/system/defaults/examples/coordinator/settings.json](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.json) |
| The CGC provider example is a disabled relationship provider with one code root, a runtime root under `providers/codegraphcontext/<repo-id>`, shared venv, pinned requirements file, patch root, state file, and contained `.codegraphcontext` env/log/db paths. | L31-L58 | [runtime/system/defaults/examples/coordinator/settings.json](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.json) |
| The provider policy marks provider output as discovery-only and still requires source proof. | L59-L70 | [runtime/system/defaults/examples/coordinator/settings.json](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.json) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-20T19:11+02:00: Documented the optional `contextProviders` settings shape for GrepAI semantic discovery and CodeGraphContext relationship discovery.
- 2026-05-13T13:38: Created onboarding for the coordinator settings JSON example.
