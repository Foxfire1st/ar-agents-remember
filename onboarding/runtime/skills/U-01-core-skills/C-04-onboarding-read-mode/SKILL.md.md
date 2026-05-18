# C-04 onboarding read mode SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-18T18:05+02:00                     |
| lastVerifiedCommitHash | `fa305b91cd6b0ec839db1fd2f19496bf292ef3fc` |
| lastVerifiedCommitDate | 2026-05-18T17:47:59+02:00|

## Purpose

This skill defines the C-04 onboarding read mode for source work that uses
Agents Remember memory. The runtime folder and skill-facing name now present
C-04 as `C-04-onboarding-read-mode` / `c-04-onboarding-read-mode`.

## Code Commentary

### Logic

The skill makes existing onboarding the primary navigation layer for source
reading. Agents follow an explicit read-state machine: known onboarding roots
go directly to `<onboarding_root>/overview.md`; route overviews define the
smallest relevant source area; candidate source files are read with their
deterministic sidecars; and source `rg` or `find` is a single-question fallback
after paired reads leave a named gap.

### Conventions

The skill is framed forward as a read protocol, not as historical discovery
guidance. It intentionally has two top-level chapters: the read protocol itself
and the hard boundaries that keep fallback search behind the onboarding path.
The read protocol now carries the operational checklist so agents can follow it
without inventing separate memory discovery steps.

### Invariants And Boundaries

C-04 does not carry startup prerequisites; coordinator and workflow instructions
own root selection, resolver usage, and trust gates. Inside the read mode,
known onboarding roots must not be rediscovered by inventory. Broad file
inventory, onboarding-tree inventory, repository-root source search,
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
| The read protocol now uses a state machine: known onboarding root, selected route overview, candidate source/sidecar pairs, then one-question targeted source confirmation. | L18-L78 | [runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md) |
| Hard boundaries place broad file inventory, onboarding inventory, repository-root or multi-subsystem source search, and cross-repo search behind the overview and paired-read path, with an explicit fallback search budget. | L80-L104 | [runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this runtime skill.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-18T18:05+02:00: Added the read-state checklist, known-root/no-inventory invariant, source/sidecar evidence format, and fallback search budget while preserving the two top-level C-04 chapters.
- 2026-05-18T16:42+02:00: Reframed C-04 from general discovery into a forward-facing onboarding read mode, with hard boundaries at the end and no startup prerequisite section.
- 2026-05-15T01:55+02:00: Created with pending verification metadata for the runtime skill-tree move.
