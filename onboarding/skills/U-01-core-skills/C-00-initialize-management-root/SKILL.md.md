# C-00-initialize-management-root/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-00-initialize-management-root/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T22:57                           |
| lastVerifiedCommitHash | `bb95b9956d55c70555bbbbcd236ca9ab62cd7261` |
| lastVerifiedCommitDate | 2026-05-09T22:15                           |

## Purpose

This skill describes first-run scaffold creation for Agents Remember memory and coordination roots.

## Code Commentary

### Logic

The skill now separates internal durable memory under `ar-memory/` from local coordination under `ar-management/`. It keeps memory `system/` files together and creates local coordination folders for system hints, memory repos, tasks, notes, and worktrees.

### Conventions

Default internal setup is local-first. Shared setup is explicit and creates coordination infrastructure plus per-repo shared memory repo settings under `memory-repos/ar-<repo-name>/system/`.

### Invariants And Boundaries

C-00 creates missing scaffolding only and must not overwrite existing files without approval. It does not create onboarding content; C-03 owns bootstrap onboarding.

### Todos

If C-00 gets an executable helper later, mirror this wording in code and add smoke tests for internal and shared scaffold shapes.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| C-00 creates the minimal memory and coordination scaffolds, defaults to internal topology, and leaves onboarding content to C-03. | L8-L12; L14-L30 | [C-00 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-00-initialize-management-root/SKILL.md) |
| The skill defines separate memory-root and coordination-root inspection/creation surfaces. | L35-L90 | [C-00 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-00-initialize-management-root/SKILL.md) |
| Internal and explicit shared settings examples keep storage and path rules under memory-layer `system/settings.json`. | L122-L176 | [C-00 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-00-initialize-management-root/SKILL.md) |
| Common outcomes preserve existing docs, tasks, and onboarding content when a partial scaffold is repaired. | L226-L244 | [C-00 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-00-initialize-management-root/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T21:59: Created onboarding after C-00 was aligned to the ar-memory/ar-management split.
- 2026-05-09T22:57: Refreshed verification metadata and replaced design-spec-only evidence with current skill citations.
