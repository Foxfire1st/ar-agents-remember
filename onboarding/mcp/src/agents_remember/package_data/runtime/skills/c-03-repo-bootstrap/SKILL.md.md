# c-03-repo-bootstrap/SKILL.md

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                     |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-05T01:32+02:00 |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063` |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|

## Purpose

This skill describes repository onboarding bootstrap. It defines a minimum root-overview bootstrap, a larger route-local memory build, and an existing-memory slice maintenance mode for added, moved, deleted, refreshed, or newly important source routes, with preservation-first handling for moved or deleted route memory.

## Code Commentary

### Logic

`c-03-repo-bootstrap` skill resolves context with `c-08-ar-coordination-context-resolver` skill, writes all bootstrap paths relative to the resolved `onboarding_root`, and builds bootstrap memory in phases. The minimum output is `overview.md`; larger runs proceed through source inventory, area research, coverage planning, governing route mapping, route-local overview cards, route-local overview waves, docs and boundary evidence packs, file cards, file-level onboarding waves, curator reviews, and handoff. Existing-memory slice maintenance starts from verified existing memory and handles expansion, refresh, move, or cleanup for a bounded source slice. For moved or deleted routes, it now asks whether documented behavior moved, split, merged, or actually disappeared before removing stale artifacts. Root and route-local overviews record route-based verification metadata and a compact `## Hot Path Summary` so `c-02-memory-quality-control` skill can later detect deterministic overview drift by `sourceRoute` and `c-04-retrieval-strategy-router` skill can use generated route-index hot-path hints as part of the Intent substrate.

### Conventions

Internal bootstrap uses `ar-memory/`; external-memory bootstrap uses the selected per-repo memory repo under `ar-coordination/memory-repos/ar-<repo-name>/`, and the skill describes those repositories as external-memory repositories. Durable route-local overview files belong in the mirrored onboarding hierarchy directly under the resolved onboarding root, while `bootstrap/` artifacts are promotion, review, and handoff artifacts. Generated `overview.index.json` files live beside overviews and include coverage plus `hotPath` fields.

### Invariants And Boundaries

`c-03-repo-bootstrap` skill writes durable onboarding, not task coordination state. Task artifacts stay in the coordinator. Source inventory review is the pre-automation intake gate; automated bootstrap stops at handoff and asks whether separate closeout should run. Candidate eligibility comes from `settings.json` path rules; the skill's exclude list is a settings checklist/example, not a hidden replacement filter. Route-local overviews may become durable memory, but file-level onboarding remains separate and self-sufficient; `c-03-repo-bootstrap` skill prepares file cards and waves while `c-05-create-or-update-onboarding-files` skill owns canonical file-level content. Existing onboarding produced by `c-03-repo-bootstrap` skill is later consumed through `c-04-retrieval-strategy-router`. Route cleanup must not remove old memory until preservation, movement, retirement, or removal has been explicitly classified.

### Todos

If bootstrap gains executable helpers, use `c-08-ar-coordination-context-resolver` skill's `memory_root`, `coordination_root`, `sources_path`, and `tools_path` fields directly rather than deriving paths from prose.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                                                                        | Citations        | Source Path                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------- |
| `c-03-repo-bootstrap` skill defines root overview as the minimum bootstrap, under the resolved onboarding root, and introduces targeted work for existing-memory source slices. | L8-L31 | [`c-03-repo-bootstrap` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md) |
| The design requires durable route-local overview placement directly in the mirrored onboarding hierarchy, generated route indexes with hot-path hints, and self-sufficient file-level onboarding. | L37-L129 | [`c-03-repo-bootstrap` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md) |
| `c-03-repo-bootstrap` skill preserves thin orchestrator behavior, confidence tags, `c-08-ar-coordination-context-resolver` skill topology resolution, cross-repo read-only semantics, and `c-05-create-or-update-onboarding-files` skill ownership of file-level onboarding. | L132-L143 | [`c-03-repo-bootstrap` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md) |
| Automated mode starts only after source inventory is accepted or corrected, writes artifacts relative to the resolved `onboarding_root`, and treats common excludes as `settings.json` path-rule defaults. | L181-L307 | [`c-03-repo-bootstrap` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md) |
| The skill lists all bootstrap templates used for ledgers, state, plans, route maps, evidence packs, cards, waves, reviews, and handoff. | L348-L366 | [`c-03-repo-bootstrap` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md) |
| Phase 3 and Phase 4D require route-based overview verification metadata and `Hot Path Summary` sections so `c-02-memory-quality-control` skill can compare recorded `sourceRoute` scopes and `c-04-retrieval-strategy-router` skill can use compact route hints inside the Intent substrate. | L686-L721; L879-L907 | [`c-03-repo-bootstrap` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md) |
| Existing-memory slice maintenance reuses current memory, covers expansion, refresh, move handling, deleted-slice cleanup, asks whether moved/deleted route behavior relocated before removal, and supports cleanup, move, preservation, or removal plans. | L464-L527 | [`c-03-repo-bootstrap` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md) |
| Phase 4 classifies deleted, moved, and stale onboarding routes; Phase 5 handoff records removed/moved/retired memory and keeps closeout outside automated bootstrap. | L756-L808; L1042-L1057 | [`c-03-repo-bootstrap` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md) |

As of the 260703-L9 lifecycle convergence, the bootstrap-trigger table row names `l-01-agent-lifecycles` (an active orchestrator job entering an uncovered area may trigger targeted bootstrap); the bootstrap flow itself is unchanged.

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: the trigger table row now names l-01-agent-lifecycles. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-02T04:25+02:00: Replaced the `W-01-heavy-task-workflow` row in the related-skills table with `l-01-agent-lifecycles` after W-01 retirement. L-01 series, Sub-task B/S6, mcp 1.1.0.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T04:34+02:00: Updated references after `c-02-memory-quality-control` skill was renamed to memory quality control.
- 2026-05-22T16:39+02:00: Updated after existing-memory slice maintenance gained explicit preservation-first handling for moved or deleted route behavior. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-21T03:05+02:00: Updated the `c-04-retrieval-strategy-router` skill relationship to `c-04-retrieval-strategy-router`, with bootstrapped onboarding as its Intent substrate.
- 2026-05-19T02:45+02:00: Updated for route-index `hotPath` support, including required root/route overview `## Hot Path Summary` sections and generated index refresh expectations.
- 2026-05-18T21:44+02:00: Refreshed after pulling the committed `c-04-retrieval-strategy-router` skill onboarding read-mode rename from `origin/main`.
- 2026-05-18T21:38+02:00: Refreshed against the current committed `c-03-repo-bootstrap` skill, restoring the `c-04-retrieval-strategy-router` skill relationship to discovery techniques and updating verification metadata.
- 2026-05-18T16:42+02:00: Updated the `c-04-retrieval-strategy-router` skill relationship to point to `c-04-retrieval-strategy-router` as the consumer of bootstrapped overviews and file maps.
- 2026-05-15T11:46+02:00: Refreshed after `c-03-repo-bootstrap` skill overview templates and instructions gained route-based verification metadata for deterministic `c-02-memory-quality-control` skill overview drift. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-14T21:38+02:00: Refreshed after the skill frontmatter was tightened and the exclusion baseline was clarified as `settings.json` path-rule defaults rather than a hidden skill filter. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T21:16+02:00: Refreshed for resolved onboarding-root paths, source inventory as the pre-automation gate, default bootstrap excludes, existing-memory slice maintenance, deleted-slice cleanup, `c-05-create-or-update-onboarding-files` skill routing, and handoff-before-closeout semantics. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Refreshed for the route-local bootstrap memory model, evidence packs, file cards, onboarding waves, curator reviews, and new template set. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-03-repo-bootstrap` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-09T22:57: Refreshed verification metadata and expanded source-backed references.
- 2026-05-09T21:59: Created onboarding after `c-03-repo-bootstrap` skill was aligned to the resolved memory root model.
