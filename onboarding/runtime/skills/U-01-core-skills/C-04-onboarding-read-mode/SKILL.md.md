# C-04 onboarding read mode SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-18T16:42+02:00                     |
| lastVerifiedCommitHash | `590df5a74eac6e213ae95c24f60656c4f1eb9841` |
| lastVerifiedCommitDate | 2026-05-18T17:15:39+02:00|

## Purpose

This skill defines the C-04 onboarding read mode for source work that uses
Agents Remember memory. The runtime folder and skill-facing name now present
C-04 as `C-04-onboarding-read-mode` / `c-04-onboarding-read-mode`.

## Code Commentary

### Logic

The skill makes existing onboarding the primary navigation layer for source
reading. Agents read the repo overview, choose the smallest relevant route
overview, use route evidence such as load-bearing files and file-level maps to
build candidate source files, then read source files together with deterministic
sidecar onboarding. Source `rg` or `find` is a targeted confirmation step only
after paired reads leave a named unresolved question.

### Conventions

The skill is framed forward as a read protocol, not as historical discovery
guidance. It intentionally has two chapters: the read protocol itself and the
hard boundaries that keep fallback search behind the onboarding path.

### Invariants And Boundaries

C-04 does not carry startup prerequisites; coordinator and workflow instructions
own root selection, resolver usage, and trust gates. Inside the read mode, broad
file inventory, onboarding-tree inventory, repository-root source search,
multi-subsystem source search, and cross-repo search are fallback actions after
the overview chain and candidate source/onboarding pairs fail to answer a stated
question. Cross-repo reading requires explicit evidence from the task or
onboarding.

### Todos

Refresh verification metadata after this skill update is committed.

### Docs References

No external documentation is needed for this repository-local runtime skill.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

This onboarding is backed by the source skill itself.

| Finding | Citations | Source Path |
| ------- | --------- | ----------- |
| The frontmatter exposes C-04 as `c-04-onboarding-read-mode` and the runtime folder is `C-04-onboarding-read-mode`. | L1-L6 | [runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md) |
| The read protocol uses repo overview, route overview, route evidence, candidate source files, deterministic sidecars, paired reads, and scoped source confirmation. | L18-L40 | [runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md) |
| Hard boundaries place broad file inventory, onboarding inventory, repository-root or multi-subsystem source search, and cross-repo search behind the overview and paired-read path. | L42-L60 | [runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this runtime skill.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-18T16:42+02:00: Reframed C-04 from general discovery into a forward-facing onboarding read mode, with hard boundaries at the end and no startup prerequisite section.
- 2026-05-15T01:55+02:00: Created with pending verification metadata for the runtime skill-tree move.
