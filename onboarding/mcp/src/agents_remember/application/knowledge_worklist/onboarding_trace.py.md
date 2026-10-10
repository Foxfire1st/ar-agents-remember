# mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

The worklist's `onboarding_trace` item kind: its registration, the two memory sides the onboarding gate
compares, the storage settings it reads, and the merge of its items into the worklist document.

## Code Commentary

- **Registration.** `ONBOARDING_TRACE_KIND` registers the kind with the subject `onboarding:<path>` for a
  file card and `onboarding:<route>/overview` for a route overview, the facts `sources`, `markdown`,
  `sidecar` and `countedChange`, and its satisfying rule: a counted change of the card or overview between
  K_B and K_C, or the leaf's row with that subject and disposition `no_impact`.
- **Sides.** `onboarding_trace_sides(request)` reads K_C from a directory or a Git tree and K_B from its
  commit. It returns `None` when neither side is converted. A converted K_B with an unconverted K_C, and a
  K_C without a pinned conversion version, are `incomplete` sides. An unconverted K_B is replaced by its
  conversion: read from `request.held_base_tree` with `knowledge_tree_from_git` when the caller holds the
  converted tree, and otherwise produced by `converted_base_files` through the converted-base cache. Only
  onboarding files, history files and the layout marker of each side are passed on.
- **Settings.** `trace_context(contract)` returns the storage settings the gate applies. The memory
  worktree's own `system/settings.md` is probed with `observed_exists`; when it is a file, it is parsed with
  `parse_coordination_settings`. Otherwise the contract's coordination context is resolved
  (`contract_context`); when that fails with an `AgentsRememberError`, the default storage settings are
  used, under which every changed file is gated. The function records nothing itself: the probe, the
  settings parsers and the resolver record their own absent files, consumed bytes and path selections, so
  inside a recording block the rows are exactly what this call looked at. A file it never opened has no
  row.
- **One list.** `worklist_onboarding(document, contract, request)` leaves a document that is not `complete`
  as it is, computes the gate over the worklist's own changed paths and merges the result with
  `with_onboarding_items`. A side that cannot be read gives an `incomplete` worklist naming `K_B`; a
  history file the gate cannot read gives one naming `K_C`. The merged items are sorted with the others
  by kind and subject, the digest covers them, and rows about files the leaf did not change are listed
  under `onboardingTrace.unnecessaryRows`.

### Logic

- **Registration (MIK-R30 rule 7).** `ONBOARDING_TRACE_KIND` is `register_item_kind(ItemKind(...))` at
  import: name `onboarding_trace`, subject pattern `^onboarding:\S`, facts `sources`, `markdown`, `sidecar`,
  `countedChange`, owner `MIK-R30`, and `row_lookup=subject_row(ITEM_KIND)`. The row lookup covers the row
  half of the satisfying rule only; `onboarding_item_open` applies both halves. The package `__init__`
  imports this module, so the kind is registered whenever the worklist is.
- **Sides.** `onboarding_trace_sides(TraceSideRequest)` reads K_C from the memory candidate directory and
  K_B from its commit (`knowledge_tree_from_directory`, `knowledge_tree_from_git`). Since MIK-R09 (L09)
  `TraceSideRequest.memory_candidate` may also be a Git tree of the memory repository, the gate's exact candidate,
  which is read with `knowledge_tree_from_git`; the pairing's `memoryCandidate` is then the tree ID:
  - neither converted: `None`, and the caller keeps today's gate;
  - K_B converted and K_C not: an incomplete side, "K_C is unconverted while K_B is converted; the crossing
    sync converts it";
  - K_C marked but without a pinned conversion version: an incomplete side naming that;
  - K_B unconverted, K_C converted: K_B is replaced by its conversion through
    `base_cache.converted_base_files`, which reads or fills the converted-base cache (MIK-R24 rule 7).
  Both sides are then restricted to `onboarding/`, `knowledge/history/` and the layout marker
  (`_onboarding_and_history`). The pairing records `base`, `memoryBase`, `convertedBase` and
  `memoryCandidate`.
- **Storage settings.** `trace_context(contract)` parses the memory worktree's own `system/settings.md`, as
  closeout resolves it, then falls back to `contract_context`, and only with neither to the resolver's
  default `StorageSettings()`, which gates every source (the strictest reading). Since MIK-R09 every settings file
  it reads is recorded through `kernel.recorded_reads.record_read`: the worktree's own file (read, or `absent`, which
  is why the fallback is taken), the context's settings paths, and the coordination fallback
  `system/settings.md`. None lies in a tree, so the mandatory gate's memo re-hashes them before reusing a verdict
  (L09 review R1 notes, ruling 2026-09-30T16:07:55). Outside a recording block nothing changes.
- **One list (ruling Q2).** `worklist_onboarding(document, contract, request)` runs only on a `complete`
  worklist. It computes the gate over the worklist's own B..C `changes[].path` and calls
  `with_onboarding_items`, which appends each item's document (`id`, `kind`, `subject`, `facts`,
  `satisfiedBy`), sorts the whole list by `(kind, subject)`, adds `onboardingTrace` (`openCount`,
  `unnecessaryRows`) and recomputes the digest. Any side failure, or any gate problem, turns the worklist
  `incomplete` with a named reason (K_B for sides, K_C for a gate problem), so the list is never silently
  short.

### Conventions

- `leaf.py` builds the `TraceSideRequest` (`_trace_request`) and exposes `leaf_onboarding_trace_sides`; this
  module does not import `leaf.py`, which avoids an import cycle.

### Invariants And Boundaries

- **`onboarding_trace` items go into the persisted worklist** (architect ruling 2026-09-29T18:49:50 (2)),
  with their satisfaction state, so L09 consumes one list.
- **The converted-base cache is extended to the Markdown the gate compares** (ruling 18:49:50 (4)); see
  `base_cache.py`.
- **Mixed formats give an incomplete side, never a vacuous pass** (ruling 19:23:45 N1): comparing a legacy
  card with its converted counterpart would make every card look changed.
- **Items are sorted by `(kind, subject)`**, L08's items and the gate's together, before the digest (ruling
  19:23:45 N2).
- **A side failure names its error kind** on the `incomplete` worklist (ruling 19:23:45 N4).
- **Unconverted trees keep today's gate.** `onboarding_trace_sides` returns `None` when neither side holds
  the layout marker, and the worklist itself is `None` there.

### Todos

- None recorded.

## Evidence

- The registered kind, its subjects, facts and satisfying rule. [12]
- The request, with the held converted base tree. [13]
- The sides: not converted, the two incomplete cases, and the held tree or the cache for an unconverted K_B. [14]
- The settings: the memory worktree's own, the resolved context, or the default. [15]
- The merge into one sorted list with its digest. [16]
- The gate over the worklist's own changed paths. [17]
- The call records the absent memory settings and the contract it read, and not the coordination settings it never opened. [18]
- Settings that are changed and restored while they are parsed are recorded with the bytes parsed. [19]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R30@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`30_onboarding-refresh-gate-on-history-files.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: registration, sides and the one list. [20]
- The kind's four registry fields, registered on import. [21]
- The explicit inputs of the side resolution. [22]
- The sides: `None`, the two mixed-format refusals, and the converted base. [23]
- K_C may be a Git tree, the gate's exact candidate (MIK-R09). [24]
- The storage settings the gate reads; since MIK-R09 each settings file read is recorded. [25]
- The gate's items merged, sorted and digested into the one list. [26]
- The worklist step, which names any side failure. [27]
- The worklist run that calls it after a complete run, since MIK-R09 inside `worklist_over`. [28]
- The persisted worklist carries the gate's items in order. [29]
- Mixed formats are an incomplete side and the persisted worklist is `incomplete`. [30]

### Cross-Repo References

The sides are read from the leaf's paired code and memory repositories (the configured pair of one
repository), not from another code repository.

No cross-repo boundary is crossed by this file.
