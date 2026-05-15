# C-03-repo-bootstrap/SKILL.md

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-15T11:46+02:00                                 |
| lastVerifiedCommitHash | `947b0e52ef06b1160819bd83ac90b5cefa7db811`             |
| lastVerifiedCommitDate | 2026-05-15T12:19:03+02:00|

## Purpose

This skill describes repository onboarding bootstrap. It defines a minimum root-overview bootstrap, a larger route-local memory build, and an existing-memory slice maintenance mode for added, moved, deleted, refreshed, or newly important source routes.

## Code Commentary

### Logic

C-03 resolves context with C-08, writes all bootstrap paths relative to the resolved `onboarding_root`, and builds bootstrap memory in phases. The minimum output is `overview.md`; larger runs proceed through source inventory, area research, coverage planning, governing route mapping, route-local overview cards, route-local overview waves, docs and boundary evidence packs, file cards, file-level onboarding waves, curator reviews, and handoff. Existing-memory slice maintenance starts from verified existing memory and handles expansion, refresh, move, or cleanup for a bounded source slice. Root and route-local overviews record route-based verification metadata so C-02 can later detect deterministic overview drift by `sourceRoute`.

### Conventions

Internal bootstrap uses `ar-memory/`; external-memory bootstrap uses the selected per-repo memory repo under `ar-coordination/memory-repos/ar-<repo-name>/`, and the skill describes those repositories as external-memory repositories. Durable route-local overview files belong in the mirrored onboarding hierarchy directly under the resolved onboarding root, while `bootstrap/` artifacts are promotion, review, and handoff artifacts.

### Invariants And Boundaries

C-03 writes durable onboarding, not task coordination state. Task artifacts stay in the coordinator. Source inventory review is the pre-automation intake gate; automated bootstrap stops at handoff and asks whether separate closeout should run. Candidate eligibility comes from `settings.json` path rules; the skill's exclude list is a settings checklist/example, not a hidden replacement filter. Route-local overviews may become durable memory, but file-level onboarding remains separate and self-sufficient; C-03 prepares file cards and waves while C-05 owns canonical file-level content.

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
| C-03 defines root overview as the minimum bootstrap, under the resolved onboarding root, and introduces targeted work for existing-memory source slices. | L8-L31 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| The design requires durable route-local overview placement directly in the mirrored onboarding hierarchy and keeps file-level onboarding self-sufficient. | L37-L128 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| C-03 preserves thin orchestrator behavior, confidence tags, C-08 topology resolution, cross-repo read-only semantics, and C-05 ownership of file-level onboarding. | L132-L143 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| Automated mode starts only after source inventory is accepted or corrected, writes artifacts relative to the resolved `onboarding_root`, and treats common excludes as `settings.json` path-rule defaults. | L181-L307 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| The skill lists all bootstrap templates used for ledgers, state, plans, route maps, evidence packs, cards, waves, reviews, and handoff. | L348-L366 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| Phase 3 and Phase 4D require route-based overview verification metadata so C-02 can compare recorded `sourceRoute` scopes deterministically. | L678-L680; L863-L865 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| Existing-memory slice maintenance reuses current memory and covers expansion, refresh, move handling, deleted-slice cleanup, and C-05 routing. | L464-L513 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |
| Phase 4 classifies deleted, moved, and stale onboarding routes; Phase 5 handoff records removed/moved/retired memory and keeps closeout outside automated bootstrap. | L756-L808; L1042-L1057 | [C-03 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-03-repo-bootstrap/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-15T11:46+02:00: Refreshed after C-03 overview templates and instructions gained route-based verification metadata for deterministic C-02 overview drift. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-14T21:38+02:00: Refreshed after the skill frontmatter was tightened and the exclusion baseline was clarified as `settings.json` path-rule defaults rather than a hidden skill filter. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T21:16+02:00: Refreshed for resolved onboarding-root paths, source inventory as the pre-automation gate, default bootstrap excludes, existing-memory slice maintenance, deleted-slice cleanup, C-05 routing, and handoff-before-closeout semantics. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Refreshed for the route-local bootstrap memory model, evidence packs, file cards, onboarding waves, curator reviews, and new template set. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-03-repo-bootstrap` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-09T21:59: Created onboarding after C-03 was aligned to the resolved memory root model.
- 2026-05-09T22:57: Refreshed verification metadata and expanded source-backed references.
