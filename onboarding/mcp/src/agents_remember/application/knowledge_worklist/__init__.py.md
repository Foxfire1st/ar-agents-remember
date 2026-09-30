# mcp/src/agents_remember/application/knowledge_worklist/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:13:48+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The package front of the change-to-knowledge worklist (MIK-R08@v2).** For a leaf, the worklist is the
complete list of knowledge items its change requires a disposition for, computed from the exact code and
memory trees of the leaf's base and candidate (B, K_B, C, K_C; MIK-R07 rule 0) and persisted as
`knowledge-worklist/v1` in the leaf's enclosure. This module holds the package overview and re-exports the
public names of its submodules; it contains no logic of its own.

## Code Commentary

### Logic

- The docstring maps the package: `code` (hunks, line-range mapping, anchor ranges, content identities),
  `knowledge` (K_B and K_C through the derived index's parser), `classify` (entry classes and knowledge-side
  changes), `registry` (item kinds and stable item IDs), `compute` (one run), `leaf` (a leaf's sides, run and
  persisted file), `surface` (what `knowledge_integrity_check` returns) and, since MIK-R30, `onboarding_trace`
  (the `onboarding_trace` item kind, the gate's sides and its items in the worklist) and, since MIK-R11,
  `planned_effects` (the `planned_untouched` item kind, the `planned`/`unplanned` marks and the
  reconciliation of declared effects against rows) and, since MIK-R06, `route_conditions` (the
  `family_route_condition` item kind, the four family route conditions and their satisfying rule; its
  kind is registered by `compute`'s import, before this module imports it) and, since MIK-R10, `unexplained`
  (the `unexplained_hunk` and `unexplained_file` kinds, the coverage lookup and the items for every unlinked
  change) and, since MIK-R14, `reconsideration` (the `reconsideration_candidate` kind, registered by `compute`'s
  import: a decision whose `reconsider_on` target changed). `base_cache` (the
  converted-base cache, review R1 F6) is imported by `leaf` and `onboarding_trace` and is not re-exported.
- `__all__` re-exports the run (`compute_worklist`, `incomplete_worklist`, `WorklistInputs`, `Item`,
  `Incomplete`, `WORKLIST_SCHEMA`), the leaf surface (`leaf_worklist`, `recompute_leaf_worklist`,
  `LeafWorklistRecompute`, `worklist_for_sides`, `ExplicitSides`, `persist_worklist`, `read_leaf_worklist`,
  `worklist_path`, `WORKLIST_FILE_NAME`) and the registry (`ITEM_KINDS`, `ItemKind`, `item_id`,
  `register_item_kind`, `satisfying_row`), and the registered kinds' names and predicates
  (`ONBOARDING_TRACE_KIND`, `PLANNED_UNTOUCHED_KIND`, `FAMILY_ROUTE_CONDITION_KIND`,
  `family_route_item_open`, MIK-R10's `UNEXPLAINED_HUNK_KIND`, `UNEXPLAINED_FILE_KIND` and
  `answering_trace_subjects`, and MIK-R14's `RECONSIDERATION_KIND`).

### Conventions

- Consumers outside the package import from here, except `mcp/tools/knowledge.py`, which imports
  `surface.leaf_worklist_fields` directly, and the tests, which reach into `code`, `leaf` and `registry`.

### Invariants And Boundaries

- **An entry is raised in exactly three cases** (changed lines intersect its own range, it moved or
  disappeared, or it changed outside the managed flow); a change elsewhere in the same file raises nothing.
- **No verdict.** What an open item means is the closeout gate's (MIK-R09); the worklist carries no
  severity or causal explanation (MIK-R08 Exclusions).
- **Inert until the cutover.** A leaf whose two memory sides are both unconverted gets no worklist, which
  is every production leaf before MIK-R37; the installed runtime's behaviour is unchanged.

### Todos

- None recorded.

## 260928-MIK-L30 The Onboarding Kind Is Registered With The Package (MIK-R30 Rule 7)

The package now imports `onboarding_trace`, whose import registers the `onboarding_trace` kind
(`ONBOARDING_TRACE_KIND`), so the kind is registered whenever the worklist is and the worklist's `kinds` list
never depends on import order. `__all__` gains `ONBOARDING_TRACE_KIND` and `leaf_onboarding_trace_sides`
(defined in `leaf.py`, which the curator's memory-quality run and the closeout validator call). The
architect accepted this import as necessary wiring (ruling 2026-09-29T18:49:50 (6)). The review's post-sync
round confirmed that importing L03's modules, which load this package, registers the same four kinds with no
import cycle.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package map's MIK-R30 entry. | "kind (registered on import), the" | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:16-17 |
| The registering import and the two new public names. | `ONBOARDING_TRACE_KIND`; `leaf_onboarding_trace_sides` | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:52-54; mcp/src/agents_remember/application/knowledge_worklist/__init__.py:99-99 |

## 260928-MIK-L11 The Planned-Effects Kind Is Registered With The Package (MIK-R11)

The package now imports `planned_effects`, whose import registers the `planned_untouched` kind
(`PLANNED_UNTOUCHED_KIND`), so the kind is registered whenever the worklist is, exactly as MIK-R30's kind
is. `__all__` gains `PLANNED_UNTOUCHED_KIND`. The package map names the module before `onboarding_trace`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package map's MIK-R11 entry. | "-- MIK-R11's" | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:14-15 |
| The registering import and the new public name. | `PLANNED_UNTOUCHED_KIND` | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:55-57; mcp/src/agents_remember/application/knowledge_worklist/__init__.py:82-82 |

## 260928-MIK-L06 The Family Route Kind And Its Predicate Are Public (MIK-R06)

The package map names `route_conditions` last. The module's `family_route_condition` kind is registered when
`compute` imports it, which the package's own first import already does, so the kind is registered whenever
the worklist is, like MIK-R30's and MIK-R11's kinds. `__all__` gains `FAMILY_ROUTE_CONDITION_KIND` and
`family_route_item_open`, the stored-item predicate MIK-R09's generic gate (L09) will call. Unlike L30's
`onboarding_item_open`, which takes a subject-to-row map, it takes the parsed history file, because it needs
the family row's disposition (the worker's note 8).

| Finding | Anchor | Source |
| --- | --- | --- |
| The package map's MIK-R06 entry. | "MIK-R06's" | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:18-19 |
| The import and the two new public names. | `FAMILY_ROUTE_CONDITION_KIND`; `family_route_item_open` | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:68-71; mcp/src/agents_remember/application/knowledge_worklist/__init__.py:79-79; mcp/src/agents_remember/application/knowledge_worklist/__init__.py:96-96 |

## 260928-MIK-L10 The Unexplained-Change Kinds Are Registered With The Package (MIK-R10)

The package map names `unexplained` last. The package imports it, and its import registers the
`unexplained_hunk` and `unexplained_file` kinds, so they are registered whenever the worklist is, like the
other registrants' kinds. `__all__` gains `UNEXPLAINED_HUNK_KIND`, `UNEXPLAINED_FILE_KIND` and
`answering_trace_subjects`: the memory-quality controller uses the last to keep an `onboarding:<path>` row
that answers an uncovered item out of MIK-R30's unnecessary-row report (ruling 2026-09-30T01:56:39 Q3). The
stored-item predicate for the gate, `unexplained_item_open`, lives in `models/knowledge_files/unexplained.py`,
not here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package map's MIK-R10 entry. | "MIK-R10's" | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:20-21 |
| The registering import and the three new public names. | `UNEXPLAINED_HUNK_KIND`; `answering_trace_subjects` | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:72-76; mcp/src/agents_remember/application/knowledge_worklist/__init__.py:84-85; mcp/src/agents_remember/application/knowledge_worklist/__init__.py:94-94 |

## 260928-MIK-L14 The Reconsideration Kind Is Registered With The Package (MIK-R14)

The package map names `reconsideration` last. Its `reconsideration_candidate` kind is registered when `compute`
imports the module (step 8 of the run), which the package's own first import already does; the package also
imports `RECONSIDERATION_KIND` itself, so the kind is registered whenever the worklist is, like the other
registrants' kinds. `__all__` gains `RECONSIDERATION_KIND`. The stored-item predicate for the gate,
`reconsideration_item_open`, lives in `models/knowledge_files/reconsideration.py`, not here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package map's MIK-R14 entry. | "MIK-R14's" | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:22-23 |
| The registering import and the new public name. | "from agents_remember.application.knowledge_worklist.reconsideration import"; "\"RECONSIDERATION_KIND\"," | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:58-60; mcp/src/agents_remember/application/knowledge_worklist/__init__.py:83-83 |

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package map and the three raising cases. | "a change elsewhere in the same file raises nothing" | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:26-26 |
| The re-exported public names. | `__all__` | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:78-108 |
| The run entry point it re-exports. | `compute_worklist` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:184-194 |
| The one recompute entry point it re-exports. | `recompute_leaf_worklist` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:548-579 |

## Cross-Repo References

No meaningful cross-repo references found: the module only re-exports its own package.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): **body updated for MIK-R14.** The Logic bullets name the `reconsideration` module and `RECONSIDERATION_KIND`; a new section, "260928-MIK-L14 The Reconsideration Kind Is Registered With The Package (MIK-R14)", with two rows. The four L30/L11/L06/L10 rows the fixer declined (each anchor occurs twice in the file: the import and `__all__`) were re-pointed by the exact line shift of this leaf's diff; the other rows were projected or normalised by the installed fixer, and its generated bullet is kept (its claim was not reworded). No verification stamp was advanced.
- 2026-09-30T10:04:58+00:00: Generated citation repair: "a change elsewhere in the same file raises nothing" repointed to mcp/src/agents_remember/application/knowledge_worklist/__init__.py:26-26. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): **body updated for MIK-R10.** The Logic bullets name the `unexplained` module and the three new public names; added the section "260928-MIK-L10 The Unexplained-Change Kinds Are Registered With The Package (MIK-R10)" with two rows (ruling 01:56:39 Q3). The earlier sections' rows were re-pointed by exact line shift or by the installed fixer. No verification stamp was advanced.
- 2026-09-30T02:32:22+00:00: Generated citation repair: "a change elsewhere in the same file raises nothing" repointed to mcp/src/agents_remember/application/knowledge_worklist/__init__.py:24-24. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:22+00:00: Generated citation repair: `compute_worklist` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:175-185. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:22+00:00: Generated citation repair: `recompute_leaf_worklist` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:544-575. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): **body updated for MIK-R06.** Added the section "260928-MIK-L06 The Family Route Kind And Its Predicate Are Public" and named `route_conditions` and the kind names and predicates in the Logic bullets. The L30 and L11 import and `__all__` rows were re-pointed by the exact shifts (+2 for the import ranges, +7 and +8 for the `__all__` lines); the fixer had declined them as multi-anchor rows. No verification stamp was advanced.
- 2026-09-29T23:15:22+00:00: Generated citation repair: "a change elsewhere in the same file raises nothing" repointed to mcp/src/agents_remember/application/knowledge_worklist/__init__.py:22-22. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c718f054d6f4666aac0289d7878fea56fae3168ee18c9058b74578d7e9f7b0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:15:22+00:00: Generated citation repair: `compute_worklist` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:164-174. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c718f054d6f4666aac0289d7878fea56fae3168ee18c9058b74578d7e9f7b0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:47:45+00:00: Generated citation repair: "a change elsewhere in the same file raises nothing" repointed to mcp/src/agents_remember/application/knowledge_worklist/__init__.py:20-20. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** Added the section "260928-MIK-L11 The Planned-Effects Kind Is Registered With The Package" (the registering import and `PLANNED_UNTOUCHED_KIND` in `__all__`) and named `planned_effects` in the Logic bullet's package map. L30's package-map row was re-pointed by the exact +2 line shift (its anchor now also occurs in MIK-R11's entry); other rows were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T18:59:23+00:00: Generated citation repair: `recompute_leaf_worklist` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:452-483. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **body updated for MIK-R30.** Added the section "260928-MIK-L30 The Onboarding Kind Is Registered With The Package" (the registering import, `ONBOARDING_TRACE_KIND` and `leaf_onboarding_trace_sides` in `__all__`, architect ruling 2026-09-29T18:49:50 (6)) and named `onboarding_trace` in the Logic bullet's package map. Rows below the import were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
