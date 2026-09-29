# mcp/src/agents_remember/application/knowledge_worklist/leaf.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/leaf.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**A leaf's worklist: its four sides, its run, and the persisted `knowledge-worklist/v1` file (MIK-R08
definition 1, rules 4, 7 and 8).** This module derives B, K_B, C and K_C from a leaf's series contract (or
takes them explicitly), decides whether a worklist applies at all, runs `compute_worklist`, and writes the
result to `knowledge-worklist.json` beside the contract. `recompute_leaf_worklist` is the one recompute
entry point every trigger calls.

## Code Commentary

### Logic

- **Sides (MIK-R07 rule 0).** B is the contract's `code_base_commit` (the fork point, advanced by each
  managed sync). K_B is `paired_memory_commit`: the newest commit of the official memory line
  (`memory_source_branch`, walked by `kernel/memory_attribution.attributed_commits`) whose `Code-Commit`
  trailer names B or an ancestor of B. C is the code worktree captured as a tree through the private-index
  capture (`worktree_candidate_tree`); K_C is the memory worktree's directory snapshot. No pairing commit
  makes the run `incomplete` naming `pairing`.
- **Applicability.** `leaf_worklist` returns `None` for a non-leaf contract, a leaf without its own memory
  worktree, or a leaf whose memory worktree and official line tip both lack the layout marker (a cheap
  probe, one `is_file` and one `git cat-file`, before any capture). `_sides` returns `None` when both
  memory sides are unconverted.
- **Converted base (MIK-R24 rule 7).** When K_B is unconverted and K_C converted, `_converted_base_side`
  compares K_B as its conversion at K_B's own paired code commit (its trailer when the code store holds it,
  otherwise B), exactly as `GitBaseConverter` chooses, at K_C's pinned conversion version. It reads the
  converted-base cache first (`base_cache.py`) and stores a fresh conversion there. The pairing records
  `convertedBase` and the `conversion` version.
- **The pairing document** records the code repository, B commit and tree, C tree, the memory repository,
  K_B commit, tree, `convertedBase` and `conversion`, and the K_C tree and location.
- **Explicit sides.** `ExplicitSides` names the four sides directly (the CLI and evidence runs on scratch
  copies; K_B is taken as given, not searched). `worklist_for_sides` turns every `_Unreadable` or
  `CodeReadError` into `incomplete_worklist`.
- **Maintenance scope.** `leaf_maintenance_scope` reads the leaf's task document (`find_leaf_doc`) and is
  true only when it sets `knowledgeMaintenanceScope: true`.
- **Persistence.** `worklist_path` is `<enclosure>/knowledge-worklist.json` for a leaf contract;
  `persist_worklist` writes it atomically as sorted, indented JSON; `read_leaf_worklist` reads it back.
- **Recompute.** `recompute_leaf_worklist(contract)` computes with `persist=False`; any exception becomes the
  `incomplete` worklist naming `worklist run`. It then persists once under an `OSError` guard and returns
  `(document, path)`, with the path `None` when the enclosure cannot be written. `LeafWorklistRecompute`
  is the worktree layer's `KnowledgeWorklistPort` adapter and returns `worklist_summary`.

### Conventions

- The cache directory is `default_base_cache_directory(contract.coordination_root)`; `ExplicitSides`
  enables it only when `cache_directory` is set.
- Only the latest worklist is kept: each run replaces the file (no run history).

### Invariants And Boundaries

- **The worklist is inert while both memory sides are unconverted.** That is every production leaf before
  MIK-R37, so the installed runtime's memory-quality run and sync are unchanged; the reviewer confirmed that
  `recompute_leaf_worklist` on the real, unconverted L08 contract returns `None` and writes nothing.
- **The worklist recompute never fails the route that triggered it** (review R1 F2). A run failure is a
  persisted `incomplete` worklist, never a silently missing list (rule 4); an unwritable enclosure returns
  the document unpersisted.
- **Trigger split (architect ruling 1).** L08 wires the curator's memory-quality run and managed-sync
  completion. Closeout validation and each landing route's pre-commit evaluation are MIK-R09's (L09),
  which calls `recompute_leaf_worklist`.
- **Persisted in the task artifacts, never in the memory repository** (rule 7): the file sits beside the
  series contract in the leaf's enclosure. The reviewer found that no archive or cleanup path deletes it.
- **K_B search order.** "Most recent" is the first match in `attributed_commits`' `--date-order` walk over
  the official line's whole ancestry, as the ledger does.

### Todos

- L09 must call `recompute_leaf_worklist` from closeout validation and each landing route's pre-commit
  evaluation.

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
| The four sides, applicability and persistence rules. | "whose two memory sides are both unconverted gets no worklist" | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:1-27 |
| Where a leaf's worklist lives. | `worklist_path`; `WORKLIST_FILE_NAME` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:93-93; mcp/src/agents_remember/application/knowledge_worklist/leaf.py:102-107 |
| Reading the latest persisted worklist. | `read_leaf_worklist` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:116-123 |
| The task-document flag. | `leaf_maintenance_scope`; `knowledgeMaintenanceScope` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:126-130 |
| The explicitly named sides. | `ExplicitSides` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:133-152 |
| K_B by trailer, or `incomplete` naming the pairing. | `paired_memory_commit`; `attributed_commits` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:194-220 |
| The sides, the both-unconverted `None`, and the pairing document. | `_sides` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:231-277 |
| The converted base, cached by K_B commit, version and paired code commit. | `_converted_base_side`; `base_cache_key` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:280-318 |
| The run over named sides; unreadable input is `incomplete`. | `worklist_for_sides` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:321-344 |
| A leaf's run from its contract, with the cheap applicability probe. | `leaf_worklist`; `_official_converted` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:347-390; mcp/src/agents_remember/application/knowledge_worklist/leaf.py:393-400 |
| The one recompute entry point, which never raises. | `recompute_leaf_worklist` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:403-434 |
| The port adapter the composition binds. | `LeafWorklistRecompute` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:437-446 |
| Pairing by trailer, following the sync, and persistence beside the contract. | `test_a_leaf_pairs_k_b_by_trailer_follows_its_sync_and_persists_beside_its_contract` | mcp/tests/test_knowledge_worklist_leaf.py:239-281 |
| No pairing commit is `incomplete` naming the pairing. | `test_a_base_no_memory_commit_pairs_with_is_incomplete_naming_the_pairing` | mcp/tests/test_knowledge_worklist_leaf.py:284-290 |
| An unconverted base is compared as its conversion. | `test_an_unconverted_base_is_compared_as_its_conversion` | mcp/tests/test_knowledge_worklist_leaf.py:305-326 |
| The recompute never raises and never fails a completed sync. | `test_the_recompute_never_raises_and_a_failure_never_fails_a_completed_sync` | mcp/tests/test_knowledge_worklist_leaf.py:663-700 |
| Both memory sides unconverted: no worklist. | `test_two_unconverted_memory_sides_get_no_worklist` | mcp/tests/test_knowledge_worklist.py:618-632 |

## Cross-Repo References

The leaf worklist reads the code repository and the memory repository of one leaf (the external memory
repository and its official line) and writes into the coordination task root. These are the configured
code/memory pair of one repository, not a boundary to another code repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| The run reads the paired code and memory repositories named by the leaf's contract. | `leaf_worklist`; `memory_repo_path` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:347-390 |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
