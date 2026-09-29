# mcp/tests/test_knowledge_worklist_leaf.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_worklist_leaf.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
| governingOverview | `overview.md` |

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
    section while `curatorActionableCount` stays 0;
  - a completed sync recomputes through the bound port; the recompute never raises and a failure never fails
    a completed sync (F2); the `continue` replay recomputes too;
  - converted bases cached by commit, version and code commit, and a cache location inside a working tree
    refused (F6).

### Conventions

- The controller case stubs the scope revalidation, census, style checks, onboarding probes, coherence
  authority, catalog steps and L28's `_without_proof`; `_knowledge_worklist` and `write_curator_checklist`
  run for real.
- The module is registered in the `unit-regression` lane; the census derives it as a consumer of
  `fixtures/repository_profiles/node/package-lock.json` because it drives the controller (the Thirty-fifth
  catalog re-pin).

### Invariants And Boundaries

- Services bound for a case are reset afterwards (`reset_worktree_services`), so no binding leaks to other
  modules.

### Todos

- None recorded.

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
| The leaf fixture: real repositories plus the task root and enclosure. | "exactly the inputs the curator's memory-quality run hands the worklist" | mcp/tests/test_knowledge_worklist_leaf.py:1-6 |
| The leaf's contract and task document. | `Leaf` | mcp/tests/test_knowledge_worklist_leaf.py:178-218 |
| Pairing by trailer and persistence. | `test_a_leaf_pairs_k_b_by_trailer_follows_its_sync_and_persists_beside_its_contract` | mcp/tests/test_knowledge_worklist_leaf.py:239-281 |
| The task document's maintenance scope. | `test_the_task_documents_maintenance_scope_classifies_every_entry` | mcp/tests/test_knowledge_worklist_leaf.py:293-302 |
| The writer's carry. | `test_the_writer_carries_moved_blobs_and_the_rows_that_cover_them` | mcp/tests/test_knowledge_worklist_leaf.py:329-385 |
| The tool and the checklist section. | `test_the_tool_returns_the_latest_worklist_and_the_checklist_shows_it` | mcp/tests/test_knowledge_worklist_leaf.py:388-415 |
| Other owners' rows and closed files are untouched. | `test_carrying_never_edits_another_owners_row_or_a_closed_history_file` | mcp/tests/test_knowledge_worklist_leaf.py:473-495 |
| A writer-authored proof raises its invariant. | `test_a_proof_authored_through_the_writer_raises_its_invariant_when_its_test_changes` | mcp/tests/test_knowledge_worklist_leaf.py:498-542 |
| The bound sync port. | `test_a_completed_sync_recomputes_through_the_bound_port` | mcp/tests/test_knowledge_worklist_leaf.py:545-564 |
| The controller-level run. | `test_the_memory_quality_controller_persists_the_worklist_and_renders_it_in_the_checklist` | mcp/tests/test_knowledge_worklist_leaf.py:572-660 |
| Never raises; never fails a completed sync. | `test_the_recompute_never_raises_and_a_failure_never_fails_a_completed_sync` | mcp/tests/test_knowledge_worklist_leaf.py:663-700 |
| The `continue` replay. | `test_the_continue_replay_of_a_completed_sync_recomputes_too` | mcp/tests/test_knowledge_worklist_leaf.py:703-717 |
| The converted-base cache. | `test_converted_bases_are_cached_by_commit_version_and_code_commit` | mcp/tests/test_knowledge_worklist_leaf.py:720-754 |
| The census-derived consumer row. | "mcp/tests/test_knowledge_worklist_leaf.py" | mcp/tests/evidence-lifecycle.toml:831-831 |

## Cross-Repo References

No meaningful cross-repo references found: every repository and the task root are built under `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
