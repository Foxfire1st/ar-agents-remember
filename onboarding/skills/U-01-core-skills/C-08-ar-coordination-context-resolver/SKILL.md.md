# C-08-ar-coordination-context-resolver/SKILL.md

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember-md                                             |
| path                   | `skills/U-01-core-skills/C-08-ar-coordination-context-resolver/SKILL.md` |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated            | 2026-05-12T18:51+02:00                                         |
| lastVerifiedCommitHash | `3eb9e862887736f0a488ec8144683fb22bb35b16`                     |
| lastVerifiedCommitDate | 2026-05-12T02:01:56+02:00                                      |

## Purpose

This skill defines C-08, the authoritative facts-only resolver for memory roots, coordination roots, settings, path rules, task roots, temporary artifact roots, worktree contract fields, ledger paths, and branch-gated cross-repo allowances.

## Code Commentary

### Logic

The skill tells agents to resolve context once and pass the resulting facts downstream instead of re-deriving topology in every workflow. It documents `code_repository_name`, `code_repository_root`, `coordination_root`, `memory_root`, `temp_root`, optional contract/worktree fields, JSON-first settings, path rules, storage settings, and cross-repo v2 result states. Shared root discovery now uses explicit input, `agents-remember-md/.env`, or the built-in `../ar-coordination` default; `.env.example` is not runtime input. Resolution validates supported memory locations and fails with a missing-memory error instead of inventing an empty context.

### Conventions

C-08 is facts-only. It may report worktree-related context from a contract, but creation or mutation of worktrees belongs to C-09.

### Invariants And Boundaries

Consumers should rely on C-08 for paths and topology. They should not infer onboarding roots from current working directory names. C-08 does not create onboarding content, drift reports, or worktree state.

### Todos

Add more examples after the first real worktree-backed task contract exists in the workspace.

### Docs References

No external domain documentation applies to this repository-local skill contract.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

C-08 is the base dependency for C-02, C-05, C-03, and task workflows.

| Finding                                                                                                                                                                 | Citations                          | Source Path                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The skill accepts `code_repository_name`, optional `code_repository_root`, and `task_name` for current wrapper task folders and persisted `*-ar` contract folders.      | L14-L23                            | [C-08 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/SKILL.md)                                                          |
| The skill returns topology, code repository identity/root, settings paths, task/temp/docs/system roots, worktree fields, ledger path, path rules, and cross-repo data.  | L29-L53                            | [C-08 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/SKILL.md)                                                          |
| Resolution rules validate explicit onboarding roots, load worktree contract coordination first, use `.env` or the built-in shared root default, require supported memory roots, and fail clearly when no memory exists. | L55-L65 | [C-08 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/SKILL.md) |
| Consumers include C-02, C-03, C-05, W-02, and C-09; boundaries keep C-08 out of mutation work.                                                                          | L84-L94                            | [C-08 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/SKILL.md)                                                          |
| The implementation exposes the same `code_repository_name` and `code_repository_root` fields through `CoordinationContext`, context construction, and JSON/text output. | L88-L112; L1002-L1156; L1216-L1267 | [ar_coordination_context_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/scripts/ar_coordination_context_resolver.py) |

## Cross-Repo References

C-08 may read shared settings, but no external repository behavior is required to understand this skill's current contract.

| Finding                                                                | Citations | Source Path |
| ---------------------------------------------------------------------- | --------- | ----------- |
| No meaningful cross-repo references found for current skill semantics. | n/a       | n/a         |

## Update History

- 2026-05-12T18:51+02:00: Updated after the skill frontmatter moved to lowercase, shared-root runtime discovery stopped using `.env.example`, and resolution rules began requiring supported memory roots with an explicit missing-memory failure.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T19:27: Renamed onboarding to C-08 AR coordination context resolver and updated resolver identity fields.
- 2026-05-10T00:47: Updated after task-name contract resolution moved to wrapper folders with persisted `*-ar` contract discovery.
- 2026-05-10T00:36: Refreshed verification metadata after the `temp_root` resolver contract landed on main.
- 2026-05-09T23:22: Updated after C-08 added `temp_root` to the resolver output contract.
- 2026-05-09T21:15: Created first file-level onboarding baseline for C-08 skill documentation.
- 2026-05-09T21:59: Updated after the resolver contract added memory/coordination roots, contract fields, ledger path, and cross-repo v2 shape.
- 2026-05-09T22:57: Refreshed verification metadata and updated citations for the current resolver layout.
