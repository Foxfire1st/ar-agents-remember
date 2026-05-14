# ar_coordination_context_resolver.py

| Field                  | Value                                                                                                       |
| ---------------------- | ----------------------------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                                          |
| path                   | `skills/U-01-core-skills/C-08-ar-coordination-context-resolver/scripts/ar_coordination_context_resolver.py` |
| doc_type               | `file-level-onboarding`                                                                                     |
| lastUpdated            | 2026-05-12T10:59                                                                                            |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a`                                                                  |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

`ar_coordination_context_resolver.py` implements the C-08 helper. It resolves a code repository name or code repository root into an explicit memory/coordination context object and emits text or JSON for downstream skills and workflows.

## Code Commentary

### Logic

The script defines dataclasses for storage, cross-repo entries, coordination selection, and coordination context; parses JSON-first settings and Markdown content; detects internal or external selection; resolves memory, coordination, and temporary artifact roots; uses coordination-root onboarding when memory-root onboarding is absent; loads task contract facts when present; checks current wrapper task roots before persisted `*-ar` roots when resolving by task name; resolves branch-gated cross-repo entries using actual checkout branches plus ledger commit metadata; and exposes a CLI.

### Conventions

All paths are normalized for portable output. The helper prefers explicit inputs, then coordinator settings, then internal fallback. It keeps path eligibility and storage mode separate, exposes `code_repository_name` and `code_repository_root` as the resolver-facing code repository identity, and exposes `temp_root` as the coordination-local place for non-durable work artifacts.

### Invariants And Boundaries

The script must not mutate repositories, write onboarding files, create worktrees, or repair memory ledgers. Its output is a contract consumed by C-02, C-05, W-02, and C-09.

### Todos

Add more fixture coverage for cross-repo inclusion with real code and memory repos.

### Docs References

The script uses Python standard-library modules only for the behavior covered here.

| Finding                                                                | Citations | Source Path |
| ---------------------------------------------------------------------- | --------- | ----------- |
| No external library documentation is required for this current helper. | n/a       | n/a         |

## Repo-Internal References

The implementation is the authoritative source for current resolver behavior.

| Finding                                                                                                                                                                                                                                  | Citations                | Source Path                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CoordinationContext` records topology, code repository name/root, coordination root, memory root, onboarding root, settings paths, task/temp/docs/system roots, storage, path rules, cross-repo data, worktree fields, and ledger path. | L81-L105                 | [ar_coordination_context_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/scripts/ar_coordination_context_resolver.py) |
| JSON settings parsing extracts storage mode, path rules, and `crossRepo.allow` from the same settings document.                                                                                                                          | L368-L396                | [ar_coordination_context_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/scripts/ar_coordination_context_resolver.py) |
| Context resolution prefers memory-repo onboarding when present, uses coordination-root onboarding when memory-root onboarding is absent, and then builds the final context.                                                              | L1048-L1073              | [ar_coordination_context_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/scripts/ar_coordination_context_resolver.py) |
| Contract resolution checks current wrapper task roots first and persisted `*-ar` roots second when only a task name is supplied.                                                                                                         | L24-L40; L808-L825       | [ar_coordination_context_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/scripts/ar_coordination_context_resolver.py) |
| Final context construction derives task and temp roots, worktree fields, ledger path, effective memory/docs/onboarding roots, sources, tools, and resolved cross-repo settings.                                                          | L1099-L1156              | [ar_coordination_context_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/scripts/ar_coordination_context_resolver.py) |
| CLI JSON and text output serialize `code_repository_name`, `code_repository_root`, and `temp_root` alongside the other resolved context paths.                                                                                           | L1205-L1218; L1234-L1247 | [ar_coordination_context_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/scripts/ar_coordination_context_resolver.py) |

## Cross-Repo References

The helper can resolve sibling repositories selected by coordinator settings, but current implementation evidence lives in this repo.

| Finding                                                                       | Citations | Source Path |
| ----------------------------------------------------------------------------- | --------- | ----------- |
| No meaningful cross-repo references found for current implementation details. | n/a       | n/a         |

## Update History

- 2026-05-12T10:59: Updated cross-repo resolver notes after `memory.md` branch metadata stopped being part of ledger compatibility.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T19:27: Renamed onboarding to the coordination context resolver helper and updated the resolver contract terminology.
- 2026-05-10T00:47: Updated after resolver task-name lookup gained wrapper-folder first behavior with persisted `*-ar` contract discovery.
- 2026-05-10T00:36: Refreshed verification metadata after the `temp_root` implementation landed on main.
- 2026-05-09T23:22: Updated after C-08 added `temp_root` for coordination-local temporary artifacts.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the C-08 helper implementation.
- 2026-05-09T21:59: Updated after C-08 gained memory/coordination roots, contract fields, ledger path, and cross-repo v2 result parsing.
- 2026-05-09T22:57: Refreshed verification metadata and updated citations for the expanded resolver implementation.
