# C-03-repo-bootstrap/SKILL.md

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-14T18:00+02:00                                 |
| lastVerifiedCommitHash | `317503210bc959ec67286551e262de787548321b`             |
| lastVerifiedCommitDate | 2026-05-14T18:37:02+02:00|

## Purpose

This skill describes repository onboarding bootstrap. It now defines a minimum root-overview bootstrap and a larger route-local memory build that uses evidence packs, file cards, onboarding waves, curator reviews, and handoff artifacts.

## Code Commentary

### Logic

C-03 resolves context with C-08, uses the resolved onboarding root as the write target, and builds bootstrap memory in phases. The minimum output is `overview.md`; larger runs proceed through source inventory, area research, coverage planning, governing route mapping, route-local overview cards, route-local overview waves, docs and boundary evidence packs, file cards, file-level onboarding waves, curator reviews, and handoff.

### Conventions

Internal bootstrap uses `ar-memory/`; shared bootstrap uses the selected per-repo memory repo under `ar-coordination/memory-repos/ar-<repo-name>/`, and the skill describes those repositories as shared-memory repositories. Durable route-local overview files belong in the mirrored onboarding hierarchy, while `bootstrap/` artifacts are promotion, review, and handoff artifacts.

### Invariants And Boundaries

C-03 writes durable onboarding, not task coordination state. Task artifacts stay in the coordinator. Route-local overviews may become durable memory, but file-level onboarding remains separate and self-sufficient; C-03 prepares file cards and waves while C-05 owns canonical file-level content.

### Todos

If bootstrap gains executable helpers, use C-08's `memory_root`, `coordination_root`, `sources_path`, and `tools_path` fields directly rather than deriving paths from prose. After this working-tree update lands, refresh verification metadata to the committed C-03 source revision.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                                                                        | Citations        | Source Path                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------- |
| C-03 defines root overview as the minimum bootstrap and the route-local/evidence/file-card/wave/curator path for larger repositories. | L8-L31 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| The design requires durable route-local overview placement in the mirrored onboarding hierarchy and keeps file-level onboarding self-sufficient. | L37-L108 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| C-03 preserves thin orchestrator behavior, confidence tags, C-08 topology resolution, cross-repo read-only semantics, and C-05 ownership of file-level onboarding. | L132-L143 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| The skill lists all bootstrap templates used for ledgers, state, plans, route maps, evidence packs, cards, waves, reviews, and handoff. | L327-L339 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| Phase 4 is the bottom-up memory build that creates coverage plans, governing route maps, route-local overviews, evidence packs, file cards, onboarding waves, and curator reviews. | L655-L956 | [C-03 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-14T18:00+02:00: Refreshed for the route-local bootstrap memory model, evidence packs, file cards, onboarding waves, curator reviews, and new template set. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-03-repo-bootstrap` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-09T21:59: Created onboarding after C-03 was aligned to the resolved memory root model.
- 2026-05-09T22:57: Refreshed verification metadata and expanded source-backed references.
