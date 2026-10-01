# mcp/src/agents_remember/application/knowledge_worklist/leaf.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**A leaf's worklist: its four sides, its run, and the persisted `knowledge-worklist/v1` file (MIK-R08
definition 1, rules 4, 7 and 8).** This module derives B, K_B, C and K_C from a leaf's series contract (or
takes them explicitly), decides whether a worklist applies at all, runs `compute_worklist`, and writes the
result to `knowledge-worklist.json` beside the contract. `recompute_leaf_worklist` is the one recompute
entry point every trigger calls. Since MIK-R10 it also reads K_B's route coverage for the run and, after the
onboarding items are merged, settles each uncovered unexplained item on its file's onboarding trace. Since MIK-R09
(L09) it also computes over an **exact candidate** given as Git trees (`CandidateTrees`), which is how the mandatory
gate recomputes, and every probe and read it makes fails closed.

## Code Commentary

### Logic

- **Sides (MIK-R07 rule 0).** B is the contract's `code_base_commit` (the fork point, advanced by each
  managed sync). K_B is `paired_memory_commit`: the newest commit of the official memory line
  (`memory_source_branch`, walked by `kernel/memory_attribution.attributed_commits`) whose `Code-Commit`
  trailer names B or an ancestor of B. C is the code worktree captured as a tree through the private-index
  capture (`worktree_candidate_tree`); K_C is the memory worktree's directory snapshot. No pairing commit
  makes the run `incomplete` naming `pairing`.
- **Applicability.** `leaf_worklist` returns `None` for a non-leaf contract, a leaf without its own memory
  worktree, or a leaf whose memory worktree (or given candidate tree) and official line tip both lack the layout
  marker (a cheap probe before any capture, `_leaf_converted`). Since MIK-R09 the probe goes through
  `has_layout_marker` (`ls-tree`, `_holds_marker`), and a probe Git cannot answer raises `LayoutProbeError`: the
  worklist is then `incomplete` naming `layout marker`, never taken for unconverted memory (L09 review R1 F9).
  `_sides` returns `None` when both memory sides are unconverted.
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
  `CodeReadError` into `incomplete_worklist`, and since MIK-R09 a `subprocess.SubprocessError` into the one naming
  `git` (`git_failure`, the L03 carry).
- **Maintenance scope.** `leaf_maintenance_scope` reads the leaf's task document and is true only when it sets
  `knowledgeMaintenanceScope: true`. Since MIK-R09 it uses the strict lookup (`strict_leaf_doc`) and is read inside
  the run's fail-closed `try` (`_leaf_document`), so a document that exists but cannot be read makes the run
  `incomplete` naming `leaf task document`, never the default scope. This resolves the L11 carry (decision
  2026-09-29T22:35:34, gathered by the L09 start decision 13:15:47).
- **Persistence.** `worklist_path` is `<enclosure>/knowledge-worklist.json` for a leaf contract;
  `persist_worklist` writes it atomically as sorted, indented JSON; `read_leaf_worklist` reads it back.
- **Recompute.** `recompute_leaf_worklist(contract)` computes with `persist=False`; a `SubprocessError` becomes the
  `incomplete` worklist naming `git` (MIK-R09), any other exception the one naming `worklist run`. It then persists once under an `OSError` guard and returns
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
  completion. Closeout validation and each landing route's pre-commit evaluation are MIK-R09's (L09), whose
  gate recomputes through `leaf_worklist(contract, persist=False, candidate=CandidateTrees(...))` over the exact
  trees the route captured (`knowledge_gate.gate.recompute_for_gate`), and direct landing through `worklist_over`.
- **Persisted in the task artifacts, never in the memory repository** (rule 7): the file sits beside the
  series contract in the leaf's enclosure. The reviewer found that no archive or cleanup path deletes it.
- **K_B search order.** "Most recent" is the first match in `attributed_commits`' `--date-order` walk over
  the official line's whole ancestry, as the ledger does.

### Todos

- Resolved by MIK-R09 (L09): the gate recomputes the worklist at the curator publication, the closeout validator and
  direct landing (see the section below); master and checkpoint landing check net staleness instead (rule 4).

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

- The one-list step after a complete run, over the same K_B; since MIK-R11 the run reads the leaf's declaration before the pairing, and since MIK-R10 the unexplained items are settled after the onboarding items; since MIK-R09 both steps live in `worklist_over`, which `leaf_worklist` and direct landing share. [1]
- The gate's side request from the contract. [2]
- The gate chooser: `None` keeps today's gate; a failure is an incomplete side, and since MIK-R09 so is a marker probe Git cannot answer (`layout marker: …`). [3]
- An unconverted leaf gets no sides and no worklist. [4]

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

- The declaration, read through the strict lookup. [5]
- The named sides carry the declaration. [6]
- An unresolved leaf document is an `incomplete` run naming it (since MIK-R09 inside `_leaf_document`, together with the maintenance scope). [7]
- The fail-closed run, tested. [8]

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

- The resolved sides carry K_B's route coverage. [9]
- Coverage over K_B's Git tree and its census blobs; over a converted base's files. [10]
- Coverage chosen per base kind; an unreadable census names K_B. [11]
- The coverage passed into the run. [12]
- The settling step after the onboarding items, since MIK-R09 the last step of `worklist_over`. [13]
- Settled items, a recomputed digest and open count, and needed rows kept out of the unnecessary list. [14]
- Coverage by entries, a migrated route, a later status, and an unreadable census. [15]
- The leaf route: an uncovered new file answered by writing its card. [16]

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

- The named sides carry the coordination root. [17]
- The run over named sides passes it on. [18]
- A leaf's run takes it from the contract. [19]

## 260928-MIK-L09 The Gate's Exact Candidate, And Every Probe Fails Closed (MIK-R09)

- **`CandidateTrees(code, memory)`** names C and K_C as Git trees already in their repositories' object stores (the
  closeout's own candidate captures). `leaf_worklist(contract, *, persist=True, candidate=None)` given one reads
  exactly those trees instead of capturing both worktrees again (`ExplicitSides.code_candidate`, and a
  `memory_candidate` that may be a tree ID); this is how the mandatory gate recomputes (`recompute_for_gate`,
  always recomputed, never a persisted worklist: the L11 carry).
- **`leaf_gate_applies(contract, candidate)`** is the gate's cheap applicability probe: K_C's tree, or the official
  line K_B pairs on, holds the layout marker (`_leaf_converted`).
- **The run split.** `leaf_worklist` probes, then `_leaf_document` reads the declaration, the maintenance scope
  (strict) and the pairing inside one fail-closed `try` (`LeafDocumentUnresolved` → `leaf task document`;
  `_Unreadable` or `SubprocessError` → `_missing`, which names the side or `git`), then `worklist_over`.
- **`worklist_over(contract, sides)`** is the full worklist over explicit sides: L08's run (`worklist_for_sides`),
  MIK-R30's onboarding items (`worklist_onboarding` over a `TraceSideRequest` built from the sides, whose K_C may be
  a Git tree) and MIK-R10's settling (`_settled_unexplained`). `None` when both memory sides are unconverted. Direct
  landing (`knowledge_gate/direct.py`) reuses it.
- **Probes fail closed (review R1 F9, ruling 16:07:55).** `_holds_marker` is `has_layout_marker` (`ls-tree`), which
  raises `LayoutProbeError` with a named reason; `leaf_worklist` then returns the `incomplete` worklist naming
  `layout marker` (and persists it), and `leaf_onboarding_trace_sides` returns an incomplete side
  (`layout marker: …`, through `_trace_gate_converted`). None of these falls through to the unconverted path.
- **Unconverted leaves are unchanged:** the probe returns `None` before any capture or read, as before; the leaf's
  `unconverted.sh` evidence finds base and this build identical (worklist `null`).

- The applicability docstring: a probe Git cannot answer is never unconverted memory. [20]
- The exact candidate as Git trees. [21]
- The cheap probe and the gate's applicability. [22]
- A probe Git cannot answer is an `incomplete` worklist naming `layout marker`. [23]
- The fail-closed reads, with the strict maintenance scope. [24]
- The full worklist over explicit sides, shared with direct landing. [25]
- The marker probe through `has_layout_marker`. [26]
- A marker probe Git cannot answer is never unconverted memory, at the worklist and the trace sides. [27]

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

- The four sides, applicability and persistence rules. [28]
- Where a leaf's worklist lives. [29]
- Reading the latest persisted worklist. [30]
- The task-document flag. [31]
- The explicitly named sides. [32]
- K_B by trailer, or `incomplete` naming the pairing. [33]
- The sides, the both-unconverted `None`, and the pairing document. [34]
- K_B as its conversion, through the read-or-convert path shared with the onboarding gate; since MIK-R10 the same cached files also give the route coverage. [35]
- The run over named sides, which since MIK-R11 also passes the leaf's declared effects; unreadable input is `incomplete`. [36]
- A leaf's run from its contract, with the cheap applicability probe (since MIK-R09 through `has_layout_marker`, and a probe Git cannot answer is `incomplete` naming `layout marker`); then (MIK-R11) the declaration and (MIK-R09) the strict maintenance scope, whose unresolved document makes the run `incomplete`; a complete run then gains the onboarding items. [37]
- The one recompute entry point, which never raises; since MIK-R09 a Git failure is named `git`. [38]
- The port adapter the composition binds. [39]
- Pairing by trailer, following the sync, and persistence beside the contract. [40]
- No pairing commit is `incomplete` naming the pairing. [41]
- An unconverted base is compared as its conversion. [42]
- The recompute never raises and never fails a completed sync. [43]
- Both memory sides unconverted: no worklist. [44]

### Cross-Repo References

The leaf worklist reads the code repository and the memory repository of one leaf (the external memory
repository and its official line) and writes into the coordination task root. These are the configured
code/memory pair of one repository, not a boundary to another code repository.

- The run reads the paired code and memory repositories named by the leaf's contract. [45]
