# mcp/src/agents_remember/application/knowledge_worklist/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T23:27:43+02:00 |
| lastVerifiedCommitHash | `46ca74302e76cf40fb6370ea9ece16d8fa719f00`|
| lastVerifiedCommitDate | 2026-09-30T00:07:49+02:00|
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
  reconciliation of declared effects against rows). `base_cache` (the
  converted-base cache, review R1 F6) is imported by `leaf` and `onboarding_trace` and is not re-exported.
- `__all__` re-exports the run (`compute_worklist`, `incomplete_worklist`, `WorklistInputs`, `Item`,
  `Incomplete`, `WORKLIST_SCHEMA`), the leaf surface (`leaf_worklist`, `recompute_leaf_worklist`,
  `LeafWorklistRecompute`, `worklist_for_sides`, `ExplicitSides`, `persist_worklist`, `read_leaf_worklist`,
  `worklist_path`, `WORKLIST_FILE_NAME`) and the registry (`ITEM_KINDS`, `ItemKind`, `item_id`,
  `register_item_kind`, `satisfying_row`).

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
| The registering import and the two new public names. | `ONBOARDING_TRACE_KIND`; `leaf_onboarding_trace_sides` | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:46-48; mcp/src/agents_remember/application/knowledge_worklist/__init__.py:75-75 |

## 260928-MIK-L11 The Planned-Effects Kind Is Registered With The Package (MIK-R11)

The package now imports `planned_effects`, whose import registers the `planned_untouched` kind
(`PLANNED_UNTOUCHED_KIND`), so the kind is registered whenever the worklist is, exactly as MIK-R30's kind
is. `__all__` gains `PLANNED_UNTOUCHED_KIND`. The package map names the module before `onboarding_trace`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package map's MIK-R11 entry. | "-- MIK-R11's" | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:14-15 |
| The registering import and the new public name. | `PLANNED_UNTOUCHED_KIND` | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:49-51; mcp/src/agents_remember/application/knowledge_worklist/__init__.py:63-63 |

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
| The package map and the three raising cases. | "a change elsewhere in the same file raises nothing" | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:20-20 |
| The re-exported public names. | `__all__` | mcp/src/agents_remember/application/knowledge_worklist/__init__.py:60-84 |
| The run entry point it re-exports. | `compute_worklist` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:145-155 |
| The one recompute entry point it re-exports. | `recompute_leaf_worklist` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:477-508 |

## Cross-Repo References

No meaningful cross-repo references found: the module only re-exports its own package.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-29T21:47:45+00:00: Generated citation repair: "a change elsewhere in the same file raises nothing" repointed to mcp/src/agents_remember/application/knowledge_worklist/__init__.py:20-20. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** Added the section "260928-MIK-L11 The Planned-Effects Kind Is Registered With The Package" (the registering import and `PLANNED_UNTOUCHED_KIND` in `__all__`) and named `planned_effects` in the Logic bullet's package map. L30's package-map row was re-pointed by the exact +2 line shift (its anchor now also occurs in MIK-R11's entry); other rows were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T18:59:23+00:00: Generated citation repair: `recompute_leaf_worklist` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:452-483. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **body updated for MIK-R30.** Added the section "260928-MIK-L30 The Onboarding Kind Is Registered With The Package" (the registering import, `ONBOARDING_TRACE_KIND` and `leaf_onboarding_trace_sides` in `__all__`, architect ruling 2026-09-29T18:49:50 (6)) and named `onboarding_trace` in the Logic bullet's package map. Rows below the import were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
