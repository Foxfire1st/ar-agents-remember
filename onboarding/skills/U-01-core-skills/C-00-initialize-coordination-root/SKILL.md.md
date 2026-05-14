# C-00-initialize-coordination-root/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-00-initialize-coordination-root/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-12T18:51+02:00                     |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a` |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

This skill describes first-run scaffold creation for Agents Remember memory and coordination roots.

## Code Commentary

### Logic

The skill now separates internal durable memory under `ar-memory/` from local coordination under `ar-coordination/`. It names the repository path input `code_repository_root`, tells agents to use C-08 for an active coordination context, keeps memory `system/` files together, and creates local coordination folders for system hints, memory repos, tasks, notes, and worktrees. Explicit external-memory scaffolding reads `agents-remember-md/.env` when present and otherwise falls back to the built-in `../ar-coordination` default; `.env.example` is documentation, not runtime input.

### Conventions

Default internal setup is local-first. External-memory setup is explicit and creates coordination infrastructure plus per-repo external memory repo settings under `memory-repos/ar-<code-repository-name>/system/`.

### Invariants And Boundaries

C-00 creates missing scaffolding only and must not overwrite existing files without approval. It does not create onboarding content; C-03 owns bootstrap onboarding.

### Todos

If C-00 gets an executable helper later, mirror this wording in code and add smoke tests for internal and external-memory scaffold shapes.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| C-00 creates the minimal memory and coordination scaffolds, defaults to internal topology, and leaves onboarding content to C-03. | L8-L12; L14-L30 | [C-00 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-00-initialize-coordination-root/SKILL.md) |
| The skill defines separate memory-root and coordination-root inspection/creation surfaces and treats `.env.example` as non-runtime documentation. | L35-L90 | [C-00 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-00-initialize-coordination-root/SKILL.md) |
| Internal and explicit coordinator settings examples keep storage and path rules under memory-layer `system/settings.json`. | L122-L176 | [C-00 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-00-initialize-coordination-root/SKILL.md) |
| Common outcomes preserve existing docs, tasks, and onboarding content when a partial scaffold is repaired. | L226-L244 | [C-00 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-00-initialize-coordination-root/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-12T18:51+02:00: Updated after the skill frontmatter moved to a lowercase skill name and explicit external-memory scaffolding stopped treating `.env.example` as runtime input.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T19:27: Renamed onboarding from C-00 initialize management root to C-00 initialize coordination root and updated current coordination terminology.
- 2026-05-09T21:59: Created onboarding after C-00 was aligned to the ar-memory/ar-coordination split.
- 2026-05-09T22:57: Refreshed verification metadata and replaced design-spec-only evidence with current skill citations.
