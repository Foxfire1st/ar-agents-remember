# mcp/tests/test_knowledge_worklist_leaf.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Tests of a leaf's worklist from its contract: pairing the memory base by trailer, following a sync,
persistence beside the contract, the surfaces that show the worklist, the writer's carrying of moved
anchors, the converted-base cache, and the read-ahead of changed blobs. The fixture (`Leaf`) is a real code
repository and a real converted memory repository on `main`, with a task root that holds the leaf's task
document and its series contract in the leaf's enclosure.

## Code Commentary

The changed writer calls explicitly supply the current `leaf_worklist(load_contract(...))`. The controller case now starts from a fresh shared memory clone with no copied route-index cache, excludes derived indexes, and lets the real index builder and proof-count computation run. Its report-enabled arm asserts the persisted worklist, built root index, zero stale indexes and informational wording that gates nothing. Both report modes return the computed proof count; the disabled arm only additionally checks that no report exists, rather than inheriting every persistence assertion. A separate cache-store case deletes an old file between listing and stat and asserts the new cache entry remains loadable. These are source cases, not a controller/cache/Git run or MEMORY certification.

- **Pairing and persistence.** A leaf pairs its memory base by the `Code-Commit` trailer, follows its sync,
  and persists the worklist beside its contract. A base that no memory commit pairs with gives an
  `incomplete` worklist naming the pairing.
- **Scope and conversion.** The task document's maintenance scope classifies every entry. An unconverted
  base is compared as its conversion. Converted bases are cached by memory commit, conversion version and
  code commit; the second run reads the cache.
- **Writer.** The writer carries moved blobs and the rows that cover them, never edits another owner's row
  or a closed history file, and a proof authored through the writer raises its invariant when its test
  changes. A frozen-text carry assertion does not hold for a hand-closed file under a rule that voids
  it there: the assertion names the reopen way out while byte and refusal checks stand.
- **Surfaces.** The tool returns the latest worklist and the checklist shows it. The memory-quality run
  recomputes, persists and names its own failure, and the controller path persists the worklist and
  renders it in the checklist.
- **Sync.** A completed sync recomputes through the bound port; the recompute never raises and a failure
  never fails a completed sync; the continue replay of a completed sync recomputes as well.
- **Read-ahead.** `test_warming_reads_the_changed_blobs_in_one_batch_and_never_fails_the_run` opens
  `CodeTrees` on two commits that change two files. `warm` with those two paths and one path that is in
  neither tree makes exactly one call of the batched blob reader, whose arguments include the base and
  candidate blobs of the changed code file and the candidate blob of the other file. Reading those blobs
  afterwards makes no further call. `warm` on trees the store does not hold returns without raising, and
  the read of such a tree raises `CodeReadError`.

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

- The controller case stubs scope revalidation, census, style checks, onboarding probes, coherence authority and catalog steps, but no longer stubs `_without_proof` or `build_route_indexes`. `_knowledge_worklist`, proof-count computation, index building and `write_curator_checklist` run for real within the declared fixture. Since MIK-R09 the exact candidate trees are captured for real too (`_curator_candidate_inputs` is
  no longer stubbed with placeholder IDs), because the gate judges exact trees.
- The module is registered in the `unit-regression` lane; the census derives it as a consumer of
  `fixtures/repository_profiles/node/package-lock.json` because it drives the controller (the Thirty-fifth
  catalog re-pin).

### Invariants And Boundaries

- Services bound for a case are reset afterwards (`reset_worktree_services`), so no binding leaks to other
  modules.

### Todos

- None recorded.

## Evidence

- The controller source exercises a fresh shared clone, real index building, informational proof counts and distinct report modes; cache store tolerates listing/stat disappearance. [41]


- The module docstring: the fixture's repositories and task root. [17]
- Pairing by trailer, following a sync and persisting beside the contract. [18]
- A base without a paired memory commit is incomplete. [19]
- An unconverted base is compared as its conversion. [20]
- Converted bases are cached. [21]
- The recompute never raises. [22]
- One batch for the changed blobs, answers from the cache, and no failure from the read-ahead. [23]
- The read-ahead under test. [24]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The tool case counts two onboarding items. [25]
- The cache case patches the conversion where it now lives. [26]
- The leaf fixture: real repositories plus the task root and enclosure. [27]
- The leaf's contract and task document. [28]
- Pairing by trailer and persistence. [29]
- The task document's maintenance scope. [30]
- The writer's carry. [31]
- The tool and the checklist section. [32]
- Other owners' rows and closed files are untouched. [33]
- A writer-authored proof raises its invariant. [34]
- The bound sync port. [35]
- The controller-level run; since MIK-R09 its four open items count (4). [36]
- Never raises; never fails a completed sync. [37]
- The `continue` replay. [38]
- The converted-base cache. [39]
- The census-derived consumer row. [40]

### Cross-Repo References

No meaningful cross-repo references found: every repository and the task root are built under `tmp_path`.

No cross-repo boundary is crossed by this file.

## 260928-MIK-L30 The Onboarding Items Join The Worklist Assertions (MIK-R30)

Two of these cases now count the onboarding gate's items in the persisted worklist (architect ruling
2026-09-29T18:49:50 (2)): `itemsByKind` in `test_the_tool_returns_the_latest_worklist_and_the_checklist_shows_it`
and in `test_the_memory_quality_controller_persists_the_worklist_and_renders_it_in_the_checklist` now includes
`onboarding_trace: 2`, the edited file's card and its root route. The cache case patches
`base_cache.converted_base` instead of `leaf.converted_base`, because the conversion moved into
`base_cache.converted_base_files` (ruling 18:49:50 (4)). The fixture and the other cases are unchanged.
