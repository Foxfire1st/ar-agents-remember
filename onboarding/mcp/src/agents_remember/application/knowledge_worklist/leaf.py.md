# mcp/src/agents_remember/application/knowledge_worklist/leaf.py

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

A leaf's worklist from its contract: which four trees are compared, when a worklist applies, how the
onboarding items join it, and where the latest document is persisted. The module also offers the same
computation over sides that a caller names directly.

## Code Commentary

### The four sides

- **B** is the contract's code base commit. **C** is the code worktree captured as a tree
  (`worktree_candidate_tree`), or a tree the caller names.
- **K_B** is the memory tree of the newest commit of the official memory line whose `Code-Commit` trailer
  names B or an ancestor of B (`paired_memory_commit`). **K_C** is the memory worktree read as a
  directory, or a Git tree the caller names.
- When K_B is unconverted and K_C is converted, K_B is compared as its conversion
  (`_converted_base_side`, through the converted-base cache). A worklist exists only where K_B or K_C
  holds the layout marker; `_sides` returns `None` when neither does.
- The document records the pairing: repositories, base commit and tree, candidate tree, memory base
  commit and tree with `convertedBase` and the pinned conversion version, and the memory candidate's tree
  and location.

### Sides given by the caller

- `CandidateTrees(code, memory)` names C and K_C as Git trees that are already in their object stores.
  With it the worklist captures neither worktree.
- `CapturedBase(code, memory, read_tree)` names B, K_B's commit, and the tree K_B is read as. With it
  `_leaf_document` takes K_B's commit from the caller instead of pairing it, and uses the caller's B
  instead of the contract's. `_leaf_converted` then probes the layout marker in `read_tree` instead of on
  the official line's tip.
- `ExplicitSides.held_base_tree` carries `read_tree` into `_sides` and into the onboarding gate's sides.
  When K_B is unconverted, `_sides` reads the held tree with `knowledge_tree_from_git` and derives the
  route coverage from its files; no conversion runs and the converted-base cache is not consulted. When
  K_B is converted, the held tree is not used and K_B is read from its own commit.

A caller that passes neither object gets the contract's own sides, captured and paired as described above.
The reviewer's worklist child passes both; the gate passes `CandidateTrees` only.

### Entry points

- `leaf_worklist(contract, persist=True, candidate=None, base=None)` returns `None` for a contract that is
  not a leaf, a leaf without a memory worktree, and a leaf whose two memory sides are unconverted. A marker
  probe that Git cannot answer gives an `incomplete` document naming `layout marker`. The document is
  written beside the contract when `persist` is true.
- `_leaf_document` reads the leaf's declared effects and maintenance scope through the strict task lookup.
  A leaf document that cannot be established gives an `incomplete` document naming `leaf task document`; a
  pairing or Git failure names its input.
- `worklist_for_sides(sides)` runs `compute_worklist` over explicit sides and turns an unreadable side, a
  `CodeReadError` and a Git failure into an `incomplete` document.
- `worklist_over(contract, sides)` adds the onboarding gate's items (`worklist_onboarding`) and settles
  uncovered unexplained changes (`_settled_unexplained`). On a complete run, `_candidate_code_blobs` reads
  every changed path from the document's captured C tree, including `None` for absent paths, and forwards
  the map as `code_blobs`; it does not recapture C. A missing tree or code-read/Git failure returns a
  named `C` incomplete document retaining owner and pairing. An already incomplete run returns without
  that read. Settlement propagates the file trace's current-row answer, recomputes digest and open count,
  and keeps answering rows out of the unnecessary list.
- `recompute_leaf_worklist(contract)` computes and persists and never raises: a Git failure and any other
  exception become an `incomplete` document, and an enclosure that cannot be written returns the document
  without a path. `LeafWorklistRecompute` is the port bound into the worktree layer.
- `leaf_gate_applies(contract, candidate)` is the marker probe alone.
- `leaf_onboarding_trace_sides(contract, memory_tree=None)` gives the onboarding gate's sides from the
  contract, `None` where neither side is converted, and an `incomplete` side for anything that cannot be
  established.

### Persistence

`worklist_path` is `knowledge-worklist.json` in the leaf's enclosure directory beside its series contract.
`persist_worklist` writes it atomically as sorted, indented JSON. `read_leaf_worklist` returns the persisted
document or `None`.

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

- The one-list step after a complete run, over the same K_B; since MIK-R11 the run reads the leaf's declaration before the pairing, and since MIK-R10 the unexplained items are settled after the onboarding items; since MIK-R09 both steps live in `worklist_over`, which `leaf_worklist` and direct landing share.
- The gate's side request from the contract.
- The gate chooser: `None` keeps today's gate; a failure is an incomplete side, and since MIK-R09 so is a marker probe Git cannot answer (`layout marker: …`).
- An unconverted leaf gets no sides and no worklist.

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

- The declaration, read through the strict lookup.
- The named sides carry the declaration.
- An unresolved leaf document is an `incomplete` run naming it (since MIK-R09 inside `_leaf_document`, together with the maintenance scope).
- The fail-closed run, tested.

## 260928-MIK-L10 Coverage At K_B And The Settled Unexplained Items (MIK-R10)

- **Coverage is read at K_B (ruling 2026-09-30T01:56:39 Q4).** `_sides` now also returns K_B's
  `RouteCoverage` in `_Resolved.coverage`, and `worklist_for_sides` passes it into `WorklistInputs.coverage`:
  - a natively converted K_B: `_git_coverage` lists K_B's Git tree (`read_git_tree_bytes`), keeps every blob
    path, reads the `knowledge/census/` blobs in one batch, and calls `unexplained.route_coverage`;
  - a converted base: `_converted_base_side` returns the side **and** `_files_coverage` over the same cached
    conversion files. A conversion writes no census, so every route of a converted base is `pending`.
  - An unreadable census (`CoverageUnreadable`) makes the run `incomplete`, naming K_B.
- **Settling after the onboarding trace (`_settled_unexplained`).** After `worklist_onboarding`, a complete
  document goes through `unexplained.settle_uncovered`: each uncovered unexplained item bound to its
  file's `onboarding_trace` takes that trace's counted-change facts, source blobs and current eligible
  row answer. In the ordinary MIK-R53 candidate contract a counted card edit alone is not an answer.
  The digest is recomputed over the settled list, and `unexplained.openCount` is recounted.
- **Needed onboarding rows are not unnecessary (ruling Q3).** The persisted
  `onboardingTrace.unnecessaryRows` drops every row whose subject is in `answering_trace_subjects`: an
  `onboarding:<path>` row that answers an uncovered item in a card-less path is that item's trace. Rows about
  files the leaf did not change are still listed.
- **Unconverted leaves are unchanged.** `_sides` still returns `None` before any coverage read when both
  memory sides are unconverted, so no production leaf before MIK-R37 reads a census or gets an item.

- The resolved sides carry K_B's route coverage.
- Coverage over K_B's Git tree and its census blobs; over a converted base's files.
- Coverage chosen per base kind; an unreadable census names K_B.
- The coverage passed into the run.
- The settling step after the onboarding items, since MIK-R09 the last step of `worklist_over`.
- Settled items, a recomputed digest and open count, and needed rows kept out of the unnecessary list.
- Coverage by entries, a migrated route, a later status, and an unreadable census.
- The leaf-route source assertions: writing an uncovered new file's card alone leaves it open; its authored source-bound onboarding row answers it.

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

- The named sides carry the coordination root.
- The run over named sides passes it on.
- A leaf's run takes it from the contract.

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
  candidate-blob extraction from that run's captured C tree, MIK-R30's onboarding items (`worklist_onboarding`
  with `code_blobs` and a `TraceSideRequest` whose K_C may be a Git tree), then MIK-R10's settling
  (`_settled_unexplained`). An unreadable or unnamed C tree fails closed as `C` incomplete; no second
  capture supplies substitute blobs. `None` when both memory sides are unconverted. Direct landing
  (`knowledge_gate/direct.py`) reuses it.
- **Probes fail closed (review R1 F9, ruling 16:07:55).** `_holds_marker` is `has_layout_marker` (`ls-tree`), which
  raises `LayoutProbeError` with a named reason; `leaf_worklist` then returns the `incomplete` worklist naming
  `layout marker` (and persists it), and `leaf_onboarding_trace_sides` returns an incomplete side
  (`layout marker: …`, through `_trace_gate_converted`). None of these falls through to the unconverted path.
- **Unconverted leaves are unchanged:** the probe returns `None` before any capture or read, as before; the leaf's
  `unconverted.sh` evidence finds base and this build identical (worklist `null`).

- The applicability docstring: a probe Git cannot answer is never unconverted memory.
- The exact candidate as Git trees.
- The cheap probe and the gate's applicability.
- A probe Git cannot answer is an `incomplete` worklist naming `layout marker`.
- The fail-closed reads, with the strict maintenance scope.
- The full worklist over explicit sides, shared with direct landing.
- The marker probe through `has_layout_marker`.
- A marker probe Git cannot answer is never unconverted memory, at the worklist and the trace sides.

## Evidence

- The module docstring: the four sides, applicability and persistence. [46]
- C and K_C given as Git trees. [47]
- B, K_B's commit and the tree K_B is read as, given by the caller. [48]
- The explicitly named sides, with the held base tree. [49]
- K_B's commit by the Code-Commit trailer. [50]
- The sides: the held tree for an unconverted K_B, the cache without one, the snapshot for a converted K_B, and the pairing. [51]
- The conversion of an unconverted K_B through the cache. [52]
- The marker probe, on the held tree when a base is given. [53]
- The entry point with its three not-applicable cases and the persistence. [54]
- Declared effects, scope and K_B's commit, from the caller's base when given. [55]
- The recompute entry point never raises. [57]
- The held tree gives the same document and reads as the conversion, at two sizes, with no second capture, pairing or conversion. [58]
- The reviewer passes the comparison's candidate trees and base commits. [59]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The one-list step after a complete run, over the same K_B; since MIK-R11 the run reads the leaf's declaration before the pairing, and since MIK-R10 the unexplained items are settled after the onboarding items; since MIK-R09 both steps live in `worklist_over`, which `leaf_worklist` and direct landing share. [60]
- The gate's side request from the contract. [61]
- The gate chooser: `None` keeps today's gate; a failure is an incomplete side, and since MIK-R09 so is a marker probe Git cannot answer (`layout marker: …`). [62]
- An unconverted leaf gets no sides and no worklist. [63]
- The declaration, read through the strict lookup. [64]
- The named sides carry the declaration. [65]
- An unresolved leaf document is an `incomplete` run naming it (since MIK-R09 inside `_leaf_document`, together with the maintenance scope). [66]
- The fail-closed run, tested. [67]
- The resolved sides carry K_B's route coverage. [68]
- Coverage over K_B's Git tree and its census blobs; over a converted base's files. [69]
- Coverage chosen per base kind; an unreadable census names K_B. [70]
- The coverage passed into the run. [71]
- The settling step after the onboarding items, since MIK-R09 the last step of `worklist_over`. [72]
- Coverage by entries, a migrated route, a later status, and an unreadable census. [74]
- The named sides carry the coordination root. [76]
- The run over named sides passes it on. [77]
- A leaf's run takes it from the contract. [78]
- The applicability docstring: a probe Git cannot answer is never unconverted memory. [79]
- The exact candidate as Git trees. [80]
- The cheap probe and the gate's applicability. [81]
- A probe Git cannot answer is an `incomplete` worklist naming `layout marker`. [82]
- The fail-closed reads, with the strict maintenance scope. [83]
- The full worklist over explicit sides, shared with direct landing. [84]
- The marker probe through `has_layout_marker`. [85]
- A marker probe Git cannot answer is never unconverted memory, at the worklist and the trace sides. [86]
- The four sides, applicability and persistence rules. [87]
- Where a leaf's worklist lives. [88]
- Reading the latest persisted worklist. [89]
- The task-document flag. [90]
- The explicitly named sides. [91]
- K_B by trailer, or `incomplete` naming the pairing. [92]
- The sides, the both-unconverted `None`, and the pairing document. [93]
- K_B as its conversion, through the read-or-convert path shared with the onboarding gate; since MIK-R10 the same cached files also give the route coverage. [94]
- The run over named sides, which since MIK-R11 also passes the leaf's declared effects; unreadable input is `incomplete`. [95]
- A leaf's run from its contract, with the cheap applicability probe (since MIK-R09 through `has_layout_marker`, and a probe Git cannot answer is `incomplete` naming `layout marker`); then (MIK-R11) the declaration and (MIK-R09) the strict maintenance scope, whose unresolved document makes the run `incomplete`; a complete run then gains the onboarding items. [96]
- The one recompute entry point, which never raises; since MIK-R09 a Git failure is named `git`. [97]
- The port adapter the composition binds. [98]
- Pairing by trailer, following the sync, and persistence beside the contract. [99]
- No pairing commit is `incomplete` naming the pairing. [100]
- An unconverted base is compared as its conversion. [101]
- The recompute never raises and never fails a completed sync. [102]
- Both memory sides unconverted: no worklist. [103]
- The run reads the paired code and memory repositories named by the leaf's contract. [104]

### Cross-Repo References

The leaf worklist reads the code repository and the memory repository of one leaf (the external memory
repository and its official line) and writes into the coordination task root. These are the configured
code/memory pair of one repository, not a boundary to another code repository.

- The captured-C changed-path blobs (including absent paths) reach onboarding items before current-row settlement; unreadable C is named incomplete. [56]
- Settled uncovered items inherit their file trace's current answer and source facts; digest/open count are recomputed and needed rows stay out of the unnecessary list. [73]
- The leaf-route source assertions: a counted card edit alone leaves the uncovered file open; its authored source-bound onboarding row answers it. [75]
- Current source delta inspected statically: Bind changed paths to captured C, fail closed on missing/unreadable blobs, and replace counted-card-only settlement and leaf-route captions. [105]
