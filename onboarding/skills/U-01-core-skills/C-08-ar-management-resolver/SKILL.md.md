# C-08-ar-management-resolver/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-08-ar-management-resolver/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-10T01:01                           |
| lastVerifiedCommitHash | `b6a5c21f9309642125a468e63c8aad1a3f3beb88` |
| lastVerifiedCommitDate | 2026-05-10T01:01                           |

## Purpose

This skill defines C-08, the authoritative facts-only resolver for memory roots, coordination roots, settings, path rules, task roots, temporary artifact roots, worktree contract fields, ledger paths, and branch-gated cross-repo allowances.

## Code Commentary

### Logic

The skill tells agents to resolve context once and pass the resulting facts downstream instead of re-deriving topology in every workflow. It documents `coordination_root`, `memory_root`, `temp_root`, optional contract/worktree fields, JSON-first settings, path rules, storage settings, and cross-repo v2 result states. For task-name resolution, current wrapper folders use `<task-name>/contract.md` while legacy `*-ar` task folders are still checked for compatibility.

### Conventions

C-08 is facts-only. It may report worktree-related context from a contract, but creation or mutation of worktrees belongs to C-09.

### Invariants And Boundaries

Consumers should rely on C-08 for paths and topology. They should not infer onboarding roots from current working directory names. C-08 does not create onboarding content, drift reports, or worktree state.

### Todos

Add more examples after the first real worktree-backed task contract exists in the workspace.

### Docs References

No external domain documentation applies to this repository-local skill contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

C-08 is the base dependency for C-02, C-05, C-03, and task workflows.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The skill accepts `task_name` for current wrapper task folders and legacy `*-ar` contract folders. | L21-L23 | [C-08 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-08-ar-management-resolver/SKILL.md) |
| The skill returns topology, repo roots, settings paths, task/temp/docs/system roots, worktree fields, ledger path, path rules, and cross-repo data. | L27-L54 | [C-08 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-08-ar-management-resolver/SKILL.md) |
| Resolution rules cover repo selection, explicit roots, shared root detection, worktree contract loading, and internal fallback. | L55-L61 | [C-08 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-08-ar-management-resolver/SKILL.md) |
| Consumers include C-02, C-03, C-05, W-02, and C-09; boundaries keep C-08 out of mutation work. | L84-L94 | [C-08 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-08-ar-management-resolver/SKILL.md) |
| The implementation exposes the same fields through `ManagementContext`, context construction, and JSON/text output. | L81-L105; L1091-L1148; L1205-L1247 | [ar_management_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-management-resolver/scripts/ar_management_resolver.py) |

## Cross-Repo References

C-08 may read shared settings, but no external repository behavior is required to understand this skill's current contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found for current skill semantics. | n/a | n/a |

## Update History

- 2026-05-10T00:47: Updated after task-name contract resolution moved to wrapper folders with legacy `*-ar` fallback.
- 2026-05-10T00:36: Refreshed verification metadata after the `temp_root` resolver contract landed on main.
- 2026-05-09T23:22: Updated after C-08 added `temp_root` to the resolver output contract.
- 2026-05-09T21:15: Created first file-level onboarding baseline for C-08 skill documentation.
- 2026-05-09T21:59: Updated after the resolver contract added memory/coordination roots, contract fields, ledger path, and cross-repo v2 shape.
- 2026-05-09T22:57: Refreshed verification metadata and updated citations for the current resolver layout.
