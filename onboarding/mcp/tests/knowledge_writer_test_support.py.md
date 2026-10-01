# mcp/tests/knowledge_writer_test_support.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The world the MIK-R12 writer tests run in.** `build_world` creates two real Git repositories under
`tmp_path`: **code** (a small package `pkg/landing.py` and `tests/test_landing.py`, committed) and a
converted **memory** tree whose committed `HEAD` is the writer's base, holding one exported invariant
(`BASE_INVARIANT`) realized by `land_pair` (`RLZ-BASE01`) and one exported family (`BASE_FAMILY`) with
that member; plus a task root with `task.json`
and a leaf contract naming both worktrees, so the command line runs exactly as a leaf runs it.

## Code Commentary

### Logic

- `CODE` defines `land_pair`, `Helper` and `Other` (same-named methods, for the qualified-symbol rule).
- `entry(...)` builds a producer entry with curator keys; `SCOPE`, `ADMISSION` and `target(...)` are the
  shared curator values.
- **Since MIK-R27 (leaf 260928-MIK-L27) the base records are genuine exports.** They are
  `legacy-unassessed` and carry an `origin.legacyId` (`legacy-invariant-landing-pair`,
  `legacy-family-landing`), and their IDs are `derived_record_id(kind, legacyId)`, as the conversion
  writes them, so the admission rule treats them as exported (ruling 23:04:57 F2). The old literals
  `INV-BASE01`/`FAM-FAM001` are gone; only the constants and the docstring changed.
- **`ADMISSION` claims `prevents_costly_mistake`** with a prose justification, a criterion the validator
  does not check mechanically, so an invariant authored without a proof or a second realization file is
  admitted; the admission tests claim the checkable criteria themselves. It used to claim
  `guarded_by_test` with no proof behind it.
- `tree_bytes` and `read_json` read the memory tree for byte-identity and content assertions.

### Conventions

- Git runs through `git(root, *args)` with a fixed identity; `canonical` renders fixtures canonically.

### Invariants And Boundaries

- A support module (no collected cases).

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The world.

- The base records' legacy IDs and the IDs derived from them. [1]
- The shared admission claims a criterion the validator does not check. [2]
- The base memory: one exported invariant, one realization, one exported family. [3]
- The leaf contract naming both worktrees. [4]
- Both repositories and the task root. [5]
- A producer entry with curator keys. [6]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
