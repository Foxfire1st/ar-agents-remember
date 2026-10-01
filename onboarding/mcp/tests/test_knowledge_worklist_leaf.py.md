# mcp/tests/test_knowledge_worklist_leaf.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R08@v2 cases on a leaf (14 cases): pairing by trailer, sync, persistence, surfaces, the writer's
carry and the controller.** The fixture is a real code repository and a real converted memory repository on
`main` (the official line), plus a task root holding the leaf's task document and its series contract in the
leaf's enclosure: exactly the inputs the curator's memory-quality run hands the worklist.

## Code Commentary

### Logic

- **Fixture.** `converted_memory` builds a converted memory tree anchored at a code commit; `Leaf` writes
  the series contract (`contract`) and the task document (`task_document`, optionally with
  `knowledgeMaintenanceScope`) under the leaf `260928-MIK-L99`.
- **Covered obligations:**
  - K_B paired by `Code-Commit` trailer at the fork point, after a sync, and through an ancestor; the file
    persisted beside the contract; no pairing is `incomplete` naming `pairing`;
  - the task document's maintenance scope classifies every entry;
  - an unconverted base compared as its conversion;
  - the writer's carry of blobs and covering rows, and that it never edits another owner's row or a closed
    history file (ruling 5); a proof authored through L28's writer key raises its invariant when its test
    body changes;
  - `knowledge_integrity_check(contractPath)` returns the latest worklist, and the checklist section shows it;
  - the memory-quality recompute persists and names its own failure; the controller-level run
    (`_execute_memory_quality`, review R1 F1) persists the file, returns `knowledgeWorklist` and renders the
    section; since MIK-R09 (leaf 260928-MIK-L09) its four open items count, `curatorActionableCount` 4 and
    `knowledgeGate.openItemCount` 4 (it was 0 while the worklist was information only);
  - a completed sync recomputes through the bound port; the recompute never raises and a failure never fails
    a completed sync (F2); the `continue` replay recomputes too;
  - converted bases cached by commit, version and code commit, and a cache location inside a working tree
    refused (F6).

### Conventions

- The controller case stubs the scope revalidation, census, style checks, onboarding probes, coherence
  authority, catalog steps and L28's `_without_proof`; `_knowledge_worklist` and `write_curator_checklist`
  run for real. Since MIK-R09 the exact candidate trees are captured for real too (`_curator_candidate_inputs` is
  no longer stubbed with placeholder IDs), because the gate judges exact trees.
- The module is registered in the `unit-regression` lane; the census derives it as a consumer of
  `fixtures/repository_profiles/node/package-lock.json` because it drives the controller (the Thirty-fifth
  catalog re-pin).

### Invariants And Boundaries

- Services bound for a case are reset afterwards (`reset_worktree_services`), so no binding leaks to other
  modules.

### Todos

- None recorded.

## 260928-MIK-L30 The Onboarding Items Join The Worklist Assertions (MIK-R30)

Two of these cases now count the onboarding gate's items in the persisted worklist (architect ruling
2026-09-29T18:49:50 (2)): `itemsByKind` in `test_the_tool_returns_the_latest_worklist_and_the_checklist_shows_it`
and in `test_the_memory_quality_controller_persists_the_worklist_and_renders_it_in_the_checklist` now includes
`onboarding_trace: 2`, the edited file's card and its root route. The cache case patches
`base_cache.converted_base` instead of `leaf.converted_base`, because the conversion moved into
`base_cache.converted_base_files` (ruling 18:49:50 (4)). The fixture and the other cases are unchanged.

- The tool case counts two onboarding items. [1]
- The cache case patches the conversion where it now lives. [2]

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

- The leaf fixture: real repositories plus the task root and enclosure. [3]
- The leaf's contract and task document. [4]
- Pairing by trailer and persistence. [5]
- The task document's maintenance scope. [6]
- The writer's carry. [7]
- The tool and the checklist section. [8]
- Other owners' rows and closed files are untouched. [9]
- A writer-authored proof raises its invariant. [10]
- The bound sync port. [11]
- The controller-level run; since MIK-R09 its four open items count (4). [12]
- Never raises; never fails a completed sync. [13]
- The `continue` replay. [14]
- The converted-base cache. [15]
- The census-derived consumer row. [16]

### Cross-Repo References

No meaningful cross-repo references found: every repository and the task root are built under `tmp_path`.

No cross-repo boundary is crossed by this file.
