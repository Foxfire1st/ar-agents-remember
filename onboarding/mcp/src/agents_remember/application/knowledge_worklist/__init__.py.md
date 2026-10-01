# mcp/src/agents_remember/application/knowledge_worklist/__init__.py

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

- The package map's MIK-R30 entry. [1]
- The registering import and the two new public names. [2]

## 260928-MIK-L11 The Planned-Effects Kind Is Registered With The Package (MIK-R11)

The package now imports `planned_effects`, whose import registers the `planned_untouched` kind
(`PLANNED_UNTOUCHED_KIND`), so the kind is registered whenever the worklist is, exactly as MIK-R30's kind
is. `__all__` gains `PLANNED_UNTOUCHED_KIND`. The package map names the module before `onboarding_trace`.

- The package map's MIK-R11 entry. [3]
- The registering import and the new public name. [4]

## 260928-MIK-L06 The Family Route Kind And Its Predicate Are Public (MIK-R06)

The package map names `route_conditions` last. The module's `family_route_condition` kind is registered when
`compute` imports it, which the package's own first import already does, so the kind is registered whenever
the worklist is, like MIK-R30's and MIK-R11's kinds. `__all__` gains `FAMILY_ROUTE_CONDITION_KIND` and
`family_route_item_open`, the stored-item predicate MIK-R09's generic gate (L09) will call. Unlike L30's
`onboarding_item_open`, which takes a subject-to-row map, it takes the parsed history file, because it needs
the family row's disposition (the worker's note 8).

- The package map's MIK-R06 entry. [5]
- The import and the two new public names. [6]

## 260928-MIK-L10 The Unexplained-Change Kinds Are Registered With The Package (MIK-R10)

The package map names `unexplained` last. The package imports it, and its import registers the
`unexplained_hunk` and `unexplained_file` kinds, so they are registered whenever the worklist is, like the
other registrants' kinds. `__all__` gains `UNEXPLAINED_HUNK_KIND`, `UNEXPLAINED_FILE_KIND` and
`answering_trace_subjects`: the memory-quality controller uses the last to keep an `onboarding:<path>` row
that answers an uncovered item out of MIK-R30's unnecessary-row report (ruling 2026-09-30T01:56:39 Q3). The
stored-item predicate for the gate, `unexplained_item_open`, lives in `models/knowledge_files/unexplained.py`,
not here.

- The package map's MIK-R10 entry. [7]
- The registering import and the three new public names. [8]

## 260928-MIK-L14 The Reconsideration Kind Is Registered With The Package (MIK-R14)

The package map names `reconsideration` last. Its `reconsideration_candidate` kind is registered when `compute`
imports the module (step 8 of the run), which the package's own first import already does; the package also
imports `RECONSIDERATION_KIND` itself, so the kind is registered whenever the worklist is, like the other
registrants' kinds. `__all__` gains `RECONSIDERATION_KIND`. The stored-item predicate for the gate,
`reconsideration_item_open`, lives in `models/knowledge_files/reconsideration.py`, not here.

- The package map's MIK-R14 entry. [9]
- The registering import and the new public name. [10]

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The package map and the three raising cases. [11]
- The re-exported public names. [12]
- The run entry point it re-exports (since MIK-R09 a Git call that fails or times out makes the run `incomplete` naming `git`). [13]
- The one recompute entry point it re-exports for L08's triggers (since MIK-R09 a Git failure is named `git`; the mandatory gate recomputes through `leaf_worklist` over its exact candidate). [14]

### Cross-Repo References

No meaningful cross-repo references found: the module only re-exports its own package.

No cross-repo boundary is crossed by this file.
