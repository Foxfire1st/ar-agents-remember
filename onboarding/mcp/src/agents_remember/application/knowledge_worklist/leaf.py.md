# mcp/src/agents_remember/application/knowledge_worklist/leaf.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/leaf.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:13:48+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**A leaf's worklist: its four sides, its run, and the persisted `knowledge-worklist/v1` file (MIK-R08
definition 1, rules 4, 7 and 8).** This module derives B, K_B, C and K_C from a leaf's series contract (or
takes them explicitly), decides whether a worklist applies at all, runs `compute_worklist`, and writes the
result to `knowledge-worklist.json` beside the contract. `recompute_leaf_worklist` is the one recompute
entry point every trigger calls. Since MIK-R10 it also reads K_B's route coverage for the run and, after the
onboarding items are merged, settles each uncovered unexplained item on its file's onboarding trace.

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
  otherwise B), exactly as `GitBaseConverter` chooses, at K_C's pinned conversion version. Since MIK-R30 it
  does so through `base_cache.converted_base_files`, the read-or-convert path it shares with the onboarding
  gate. The pairing records
  `convertedBase` and the `conversion` version.
- **The pairing document** records the code repository, B commit and tree, C tree, the memory repository,
  K_B commit, tree, `convertedBase` and `conversion`, and the K_C tree and location.
- **Explicit sides.** `ExplicitSides` names the four sides directly (the CLI and evidence runs on scratch
  copies; K_B is taken as given, not searched). `worklist_for_sides` turns every `_Unreadable` or
  `CodeReadError` into `incomplete_worklist`.
- **Maintenance scope.** `leaf_maintenance_scope` reads the leaf's task document (`find_leaf_doc`) and is
  true only when it sets `knowledgeMaintenanceScope: true`. It keeps the fail-soft lookup; the declaration
  below uses the strict one (MIK-R11, ruling F2).
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

## 260928-MIK-L30 The Onboarding Gate's Sides And Items (MIK-R30)

- **Items in the one list (ruling 2026-09-29T18:49:50 (2)).** After a `complete` run `leaf_worklist` calls
  `onboarding_trace.worklist_onboarding(document, contract, _trace_request(...))`, which computes the
  onboarding gate over the worklist's own B..C changes and merges its `onboarding_trace` items, sorted by
  `(kind, subject)` with L08's items, into the persisted document. A side or gate failure makes the worklist
  `incomplete` with a named reason.
- **`_trace_request`** builds the gate's `TraceSideRequest` from the contract: owner, memory repository,
  K_B, the memory candidate (the worktree, or an explicit `memory_tree`), code repository, B and the default
  base-cache directory.
- **`leaf_onboarding_trace_sides(contract, *, memory_tree=None)`** is what the memory-quality run and the
  closeout validator call to choose a gate. It returns `None` (today's gate) for a non-leaf contract, a leaf
  without its own memory worktree, or a leaf whose candidate and official line tip both lack the layout
  marker (the same cheap probe as the worklist, before any read). Otherwise it pairs K_B by trailer, exactly
  as the worklist does, and returns the sides; any exception becomes an `incomplete` side naming the error,
  so the gate reports a finding and never lapses. It lives here, beside `paired_memory_commit`, to avoid an
  import cycle.
- **The converted base** now goes through `base_cache.converted_base_files` (ruling 18:49:50 (4)).
- **Unconverted leaves are unchanged:** `recompute_leaf_worklist` still returns `None` and
  `leaf_onboarding_trace_sides` returns `None`, so every production leaf before MIK-R37 keeps today's gate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The one-list step after a complete run, over the same K_B; since MIK-R11 the run reads the leaf's declaration before the pairing, and since MIK-R10 the unexplained items are settled after the onboarding items. | "def leaf_worklist("; "document = worklist_onboarding(" | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:400-454 |
| The gate's side request from the contract. | `_trace_request` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:483-499 |
| The gate chooser: `None` keeps today's gate; a failure is an incomplete side. | `leaf_onboarding_trace_sides` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:502-535 |
| An unconverted leaf gets no sides and no worklist. | `test_an_unconverted_leaf_keeps_todays_gate_unchanged` | mcp/tests/test_onboarding_trace_gate.py:751-758 |

## 260928-MIK-L11 The Leaf's Declared Effects (MIK-R11)

- **`leaf_expected_effects(contract)`** reads the leaf task document's `expectedKnowledgeEffects` through
  `tasks/leaf_decisions.strict_leaf_doc` and returns them as `Declaration`s, or `None` when the document
  declares none (or the leaf has no document).
- **Fail closed (ruling F2, 2026-09-29T22:35:34+02:00).** `leaf_worklist` resolves the declaration inside
  its `try`, before the pairing lookup. A `LeafDocumentUnresolved` (a claiming document that cannot be read,
  or two documents claiming the leaf) makes the run `incomplete` with the input `leaf task document` and a
  detail naming the file, with no items and no `plannedEffects`; it never reads as `declared: false`.
- **The run's input.** `ExplicitSides.expected_effects` carries the declaration for named sides (evidence
  runs on scratch copies), and `worklist_for_sides` passes it into `WorklistInputs`; `compute.py` step 5
  reconciles it.
- **Unconverted leaves are unchanged.** The applicability probe returns `None` before the declaration is
  read, so a production leaf before MIK-R37 never reads it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The declaration, read through the strict lookup. | `leaf_expected_effects`; `strict_leaf_doc` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:152-161 |
| The named sides carry the declaration. | `ExplicitSides`; `expected_effects` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:164-187 |
| An unresolved leaf document is an `incomplete` run naming it. | `LeafDocumentUnresolved`; "leaf task document" | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:400-454 |
| The fail-closed run, tested. | "leaf task document" | mcp/tests/test_planned_knowledge_effects.py:579-587 |

## 260928-MIK-L10 Coverage At K_B And The Settled Unexplained Items (MIK-R10)

- **Coverage is read at K_B (ruling 2026-09-30T01:56:39 Q4).** `_sides` now also returns K_B's
  `RouteCoverage` in `_Resolved.coverage`, and `worklist_for_sides` passes it into `WorklistInputs.coverage`:
  - a natively converted K_B: `_git_coverage` lists K_B's Git tree (`read_git_tree_bytes`), keeps every blob
    path, reads the `knowledge/census/` blobs in one batch, and calls `unexplained.route_coverage`;
  - a converted base: `_converted_base_side` returns the side **and** `_files_coverage` over the same cached
    conversion files. A conversion writes no census, so every route of a converted base is `pending`.
  - An unreadable census (`CoverageUnreadable`) makes the run `incomplete`, naming K_B.
- **Settling after the onboarding trace (`_settled_unexplained`).** After `worklist_onboarding`, a complete
  document goes through `unexplained.settle_uncovered`: each uncovered unexplained item bound to MIK-R30's
  `onboarding_trace` item for its file takes that item's counted change and answer. The digest is recomputed
  over the settled list, and `unexplained.openCount` is recounted.
- **Needed onboarding rows are not unnecessary (ruling Q3).** The persisted
  `onboardingTrace.unnecessaryRows` drops every row whose subject is in `answering_trace_subjects`: an
  `onboarding:<path>` row that answers an uncovered item in a card-less path is that item's trace. Rows about
  files the leaf did not change are still listed.
- **Unconverted leaves are unchanged.** `_sides` still returns `None` before any coverage read when both
  memory sides are unconverted, so no production leaf before MIK-R37 reads a census or gets an item.

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved sides carry K_B's route coverage. | `_Resolved`; "coverage: RouteCoverage" | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:258-264 |
| Coverage over K_B's Git tree and its census blobs; over a converted base's files. | `_git_coverage`; `_files_coverage` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:270-283; mcp/src/agents_remember/application/knowledge_worklist/leaf.py:286-288 |
| Coverage chosen per base kind; an unreadable census names K_B. | `CoverageUnreadable`; "coverage = _git_coverage(" | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:307-320 |
| The coverage passed into the run. | "coverage=resolved.coverage" | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:397-397 |
| The settling step after the onboarding items. | "document = _settled_unexplained(document)" | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:454-454 |
| Settled items, a recomputed digest and open count, and needed rows kept out of the unnecessary list. | `_settled_unexplained`; `answering_trace_subjects` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:461-480 |
| Coverage by entries, a migrated route, a later status, and an unreadable census. | `test_coverage_is_entries_in_k_b_or_the_latest_census_status_of_the_governing_route` | mcp/tests/test_unexplained_change_disposition.py:222-271 |
| The leaf route: an uncovered new file answered by writing its card. | `test_an_uncovered_new_file_is_satisfied_by_its_onboarding_trace` | mcp/tests/test_unexplained_change_disposition.py:463-505 |

## 260928-MIK-L14 The Coordination Root Reaches The Run (MIK-R14)

- **Requirement endpoints resolve from the leaf's coordination root.** `leaf_worklist` passes
  `contract.coordination_root` into `ExplicitSides.coordination_root`, and `worklist_for_sides` passes it into
  `WorklistInputs.coordination_root`, so MIK-R14's step 8 can resolve a `reconsider_on` requirement endpoint and
  read its owning task's manifest. Named sides (`knowledge-worklist --coordination-root`, evidence runs) carry it
  explicitly; `None` resolves no endpoint, so a requirement link never fires there.
- **Read-only.** The root is only read (task packets and manifests); a live review read of a leaf's worklist (L31)
  now also resolves requirement endpoints read-only (review R6 post-sync note).
- **Unconverted leaves are unchanged.** `_sides` still returns `None` for a both-unconverted leaf before any
  endpoint is read; the real unconverted L14 contract gives `None` on the base and L14 builds (`unconverted.txt`).

| Finding | Anchor | Source |
| --- | --- | --- |
| The named sides carry the coordination root. | "Where requirement endpoints' owning tasks live (MIK-R14)" | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:186-187 |
| The run over named sides passes it on. | "coordination_root=sides.coordination_root" | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:398-398 |
| A leaf's run takes it from the contract. | "coordination_root=contract.coordination_root," | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:446-446 |

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
| Where a leaf's worklist lives. | `worklist_path`; `WORKLIST_FILE_NAME` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:112-112; mcp/src/agents_remember/application/knowledge_worklist/leaf.py:121-126 |
| Reading the latest persisted worklist. | `read_leaf_worklist` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:135-142 |
| The task-document flag. | `leaf_maintenance_scope`; `knowledgeMaintenanceScope` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:145-149 |
| The explicitly named sides. | `ExplicitSides` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:164-187 |
| K_B by trailer, or `incomplete` naming the pairing. | `paired_memory_commit`; `attributed_commits` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:229-255 |
| The sides, the both-unconverted `None`, and the pairing document. | `_sides` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:291-340 |
| K_B as its conversion, through the read-or-convert path shared with the onboarding gate; since MIK-R10 the same cached files also give the route coverage. | `_converted_base_side`; `converted_base_files` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:341-369 |
| The run over named sides, which since MIK-R11 also passes the leaf's declared effects; unreadable input is `incomplete`. | "def worklist_for_sides(sides: ExplicitSides)"; "expected_effects=sides.expected_effects" | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:374-374; mcp/src/agents_remember/application/knowledge_worklist/leaf.py:396-396 |
| A leaf's run from its contract, with the cheap applicability probe; then (MIK-R11) the declaration, whose unresolved document makes the run `incomplete`; a complete run then gains the onboarding items. | `leaf_worklist`; `_official_converted` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:403-458; mcp/src/agents_remember/application/knowledge_worklist/leaf.py:538-545 |
| The one recompute entry point, which never raises. | `recompute_leaf_worklist` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:548-579 |
| The port adapter the composition binds. | `LeafWorklistRecompute` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:582-591 |
| Pairing by trailer, following the sync, and persistence beside the contract. | `test_a_leaf_pairs_k_b_by_trailer_follows_its_sync_and_persists_beside_its_contract` | mcp/tests/test_knowledge_worklist_leaf.py:240-282 |
| No pairing commit is `incomplete` naming the pairing. | `test_a_base_no_memory_commit_pairs_with_is_incomplete_naming_the_pairing` | mcp/tests/test_knowledge_worklist_leaf.py:285-291 |
| An unconverted base is compared as its conversion. | `test_an_unconverted_base_is_compared_as_its_conversion` | mcp/tests/test_knowledge_worklist_leaf.py:306-327 |
| The recompute never raises and never fails a completed sync. | `test_the_recompute_never_raises_and_a_failure_never_fails_a_completed_sync` | mcp/tests/test_knowledge_worklist_leaf.py:672-709 |
| Both memory sides unconverted: no worklist. | `test_two_unconverted_memory_sides_get_no_worklist` | mcp/tests/test_knowledge_worklist.py:629-643 |

## Cross-Repo References

The leaf worklist reads the code repository and the memory repository of one leaf (the external memory
repository and its official line) and writes into the coordination task root. These are the configured
code/memory pair of one repository, not a boundary to another code repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| The run reads the paired code and memory repositories named by the leaf's contract. | "def leaf_worklist("; `memory_repo_path` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:400-454 |

## Update History
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): **body updated for MIK-R14.** New section "260928-MIK-L14 The Coordination Root Reaches The Run (MIK-R14)": `ExplicitSides.coordination_root`, `worklist_for_sides` and `leaf_worklist` pass the contract's root into the run so step 8 resolves requirement endpoints (read-only; also on L31's live review read, review R6), and unconverted leaves stay `None`. Three rows. The rows the fixer declined were re-pointed by the exact line shift of this leaf's diff; the others were projected or normalised by the installed fixer, and its generated bullets are kept. No verification stamp was advanced.
- 2026-09-30T10:05:17+00:00: Generated citation repair: `_Resolved`; "coverage: RouteCoverage" repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:258-264; mcp/src/agents_remember/application/knowledge_worklist/leaf.py:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:17+00:00: Generated citation repair: "coverage=resolved.coverage" repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:397-397. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:17+00:00: Generated citation repair: "document = _settled_unexplained(document)" repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:454-454. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): **body updated for MIK-R10.** Purpose extended; added the section "260928-MIK-L10 Coverage At K_B And The Settled Unexplained Items (MIK-R10)" (`_git_coverage`, `_files_coverage`, the coverage returned by `_converted_base_side`, `CoverageUnreadable` as an `incomplete` run naming K_B, `_settled_unexplained`, and the needed onboarding rows dropped from `unnecessaryRows`), with the rulings of 01:56:39 (Q3, Q4); eight rows. **Row re-measured, not shifted:** the `_converted_base_side` row (`302-326`, correct at the base, but no line shift could map it because its signature lines changed) now cites `341-369`, and its claim names the coverage. **Two reopened claims re-read:** the L30 one-list row (reworded to name the settling step) and the Cross-Repo row (retained), both about `leaf_worklist`, which MIK-R10 changed; they are re-anchored on the line-exact quote "def leaf_worklist(", and this pass's fixer bullet for the first was removed. Other rows were projected or normalised by the installed fixer, or re-pointed by exact line shift. No verification stamp was advanced.
- 2026-09-30T02:32:51+00:00: Generated citation repair: `_trace_request` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:479-495. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:51+00:00: Generated citation repair: `leaf_onboarding_trace_sides` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:498-531. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:51+00:00: Generated citation repair: `read_leaf_worklist` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:135-142. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:51+00:00: Generated citation repair: "def worklist_for_sides(sides: ExplicitSides)"; "expected_effects=sides.expected_effects" repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:372-372; mcp/src/agents_remember/application/knowledge_worklist/leaf.py:394-394. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:51+00:00: Generated citation repair: `recompute_leaf_worklist` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:544-575. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:51+00:00: Generated citation repair: `LeafWorklistRecompute` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:578-587. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:47:56+00:00: Generated citation repair: `_trace_request` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:412-428. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:47:56+00:00: Generated citation repair: `LeafWorklistRecompute` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:511-520. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** Added the section "260928-MIK-L11 The Leaf's Declared Effects" (`leaf_expected_effects` through the strict lookup, the fail-closed `incomplete` run, `ExplicitSides.expected_effects`), recording architect ruling 2026-09-29T22:35:34 (F2, with `leaf_maintenance_scope`'s fail-soft lookup carried to L09). **The reopened `worklist_for_sides` claim was re-read and reworded** (it now passes the declared effects) and re-anchored on its line-exact quotes, because the generated-repair bullet that binds it is committed. **The two reopened `leaf_worklist` rows** (L30's one-list row and the run row) were re-read and reworded (the run now reads the declaration first); only the one generated-repair bullet this pass's fixer wrote for them was removed. Other rows were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T18:59:33+00:00: Generated citation repair: `worklist_for_sides` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:309-332. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:59:33+00:00: Generated citation repair: `recompute_leaf_worklist` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:452-483. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:59:33+00:00: Generated citation repair: `LeafWorklistRecompute` repointed to mcp/src/agents_remember/application/knowledge_worklist/leaf.py:486-495. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **body updated for MIK-R30.** Added the section "260928-MIK-L30 The Onboarding Gate's Sides And Items" (`worklist_onboarding` after a complete run, `_trace_request`, `leaf_onboarding_trace_sides`, and the cache move), recording architect rulings 2026-09-29T18:49:50 (2, 4). **The reopened `leaf_worklist` claim was re-read and reworded** (it now says that a complete run gains the onboarding items) and re-measured, with its sibling cross-repo row; the converted-base row was reworded for `converted_base_files`. Other rows were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
