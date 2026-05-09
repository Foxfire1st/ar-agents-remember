# ar_management_resolver.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-08-ar-management-resolver/scripts/ar_management_resolver.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T23:22                           |
| lastVerifiedCommitHash | `bb95b9956d55c70555bbbbcd236ca9ab62cd7261` |
| lastVerifiedCommitDate | 2026-05-09T22:15                           |

## Purpose

`ar_management_resolver.py` implements the C-08 helper. It resolves a target repository into an explicit memory/coordination context object and emits text or JSON for downstream skills and workflows.

## Code Commentary

### Logic

The script defines dataclasses for storage, cross-repo entries, management selection, and management context; parses JSON-first settings and Markdown fallback content; detects internal or shared selection; resolves memory, coordination, and temporary artifact roots; preserves legacy shared-onboarding fallback during migration; loads task contract facts when present; resolves branch-gated cross-repo entries; and exposes a CLI.

### Conventions

All paths are normalized for portable output. The helper prefers explicit inputs, then shared settings, then internal fallback. It keeps path eligibility and storage mode separate, keeps `management_root` as a compatibility alias for `coordination_root`, and exposes `temp_root` as the coordination-local place for non-durable work artifacts.

### Invariants And Boundaries

The script must not mutate repositories, write onboarding files, create worktrees, or repair memory ledgers. Its output is a contract consumed by C-02, C-05, W-02, and C-09.

### Todos

Add more fixture coverage for cross-repo inclusion with real code and memory repos.

### Docs References

The script uses Python standard-library modules only for the behavior covered here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external library documentation is required for this current helper. | n/a | n/a |

## Repo-Internal References

The implementation is the authoritative source for current resolver behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `ManagementContext` records topology, target repo, coordination root, memory root, onboarding root, settings paths, task/temp/docs/system roots, storage, path rules, cross-repo data, worktree fields, and ledger path. | L81-L105 | [ar_management_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-management-resolver/scripts/ar_management_resolver.py) |
| JSON settings parsing extracts storage mode, path rules, and `crossRepo.allow` from the same settings document. | L368-L396 | [ar_management_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-management-resolver/scripts/ar_management_resolver.py) |
| Context resolution prefers memory-repo onboarding when present, preserves legacy onboarding fallback during migration, and then builds the final context. | L1048-L1073 | [ar_management_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-management-resolver/scripts/ar_management_resolver.py) |
| Final context construction derives task and temp roots, worktree fields, ledger path, effective memory/docs/onboarding roots, sources, tools, and resolved cross-repo settings. | L1091-L1148 | [ar_management_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-management-resolver/scripts/ar_management_resolver.py) |
| CLI JSON and text output serialize `temp_root` alongside the other resolved context paths. | L1205-L1218; L1234-L1247 | [ar_management_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-management-resolver/scripts/ar_management_resolver.py) |

## Cross-Repo References

The helper can resolve sibling repositories selected by shared settings, but current implementation evidence lives in this repo.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found for current implementation details. | n/a | n/a |

## Update History

- 2026-05-09T23:22: Updated after C-08 added `temp_root` for coordination-local temporary artifacts.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the C-08 helper implementation.
- 2026-05-09T21:59: Updated after C-08 gained memory/coordination roots, contract fields, ledger path, and cross-repo v2 result parsing.
- 2026-05-09T22:57: Refreshed verification metadata and updated citations for the expanded resolver implementation.
