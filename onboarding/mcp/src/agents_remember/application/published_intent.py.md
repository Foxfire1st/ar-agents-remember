# mcp/src/agents_remember/application/published_intent.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Select published text knowledge for the ordinary paired read. Its coordination context names the exact memory root; the route captures that tree and reads its derived index beside the requested source.

## Code Commentary

### Logic

`resolve_published_intent` selects a converted memory tree or reports `legacy-format`. `converted_memory_tree` accepts only a directory holding `knowledge/layout.json`; a `knowledge.sqlite` file and a parent inferred from its filename are not accepted tree inputs. Selection requires a coordination root for the derived cache, and partial indexes stay incomplete.

Source resolution is a root/tree pair or is unrequested, never half-invented. Path seeds prepare family-complete leaf selections; identity seeds use the scope walk. The whole knowledge block fits the shared threshold and resumes through `knowledge_read`.

### Invariants And Boundaries

Text in Git is the publication. No canonical published dataset path, database publication owner or read fallback remains. Unconverted memory is legacy format even before a database was published. A knowledge refusal does not erase returned source bytes. Currentness reports observations against the exact code tree without withholding stale content or changing intent.

### Todos

None recorded.

### Logic


**Returned invariants carry their currentness (MIK-R03).** For a converted tree, `read_published_intent`
adds a `currentness` block beside the pages: the state of every invariant and family the pages return
(`stale`, `unverifiable`, `unrealized` or `current`), each entry that is not current, the counts by state
and each family's stale members, computed once per block by `knowledge_paging.currentness.WalkCurrentness`
inside `_tree_block`, so the block is measured with it (MIK-R02, ruling F3 of 2026-09-29 20:40:40). **The tree it observes
is the one this route already resolved for the source it returns** (architect ruling 1, 2026-09-29T18:42:37):
the `sourceResolution` pair, the code root's `HEAD^{tree}`. That is the read's own resolved tree, not a
fallback. The block names it (`codeTree.treeId`) and states its scope in `treeScope` (`_TREE_SCOPE`: "states
observed at the committed code tree <id> this read resolved; uncommitted working-tree edits are not
reflected"). When the route resolves no pair, `codeTree` is `null`, there is no `treeScope`, and every realized
invariant is `unverifiable` ("no code tree was requested"). The computation never raises (ruling N2,
19:13:41), so this function holds no `try` of its own. MIK-R29 may add an explicit tree selector later.

**A memory tree's block is bounded as a whole and continues through `knowledge_read` (MIK-R02).** For a
converted tree, `_seed_block` hands each seed to `_tree_page_block`, which returns the seed's whole
selection prepared for the block (or the read's own refusal block): since MIK-R01 a **path** seed is
prepared by `knowledge_leaf.pages.prepare_leaf` (below), and an **identity** seed keeps
`knowledge_paging.scope_pages.prepare_scope`.
`read_published_intent` then returns `bounded_block(blocks, envelope)` (`knowledge_paging/block_pages.py`),
with `_tree_block` as the envelope: the recorded block around the laid-out seeds, plus `threshold` and the
`currentness` with its `treeScope`, so everything the block carries beside its seeds is inside the measured
block. **The threshold bounds the knowledge block of a `read_ar_files` response as a whole, not each seed**
(architect ruling Q1, 2026-09-29 19:56:40); source files and onboarding are outside it. Seeds are laid out in
order; once the block is full, each remaining seed is `state: "deferred"` with only its counts and a
position-0 continuation, and when those would not fit they collapse into one deferred entry listing its
`seeds` (ruling F2, 20:40:40). Every page carries `page` (the threshold, the binding and the walk's counts),
`continuationOperation: "knowledge_read"` and `continuationView`, and its `continuation` is the shared
`knowledge-continuation/v2` token the mounted tool resumes. `_candidates` hands every row a **scope** seed
could carry to the one scope currentness computation (`_code_tree` is the source pair's tree); a leaf seed
computed its own selection's currentness when it was prepared. `PUBLISHED_INTENT_MAX_UTF8_BYTES`
left the public API (ruling Q2): the database page keeps the bound privately until MIK-R26 (L26) retires that
route. The database path is unchanged and keeps a `cast`, because it never prepares a scope.

**A path on a memory tree is read family-complete (MIK-R01).** For a converted tree, `_tree_page_block`
prepares a `PathSeed` with `prepare_leaf(LeafRequest(...))`: the index file, the tree key, the index state, the
path and the source pair's code tree. The result is the family-complete leaf read
(`application/knowledge_leaf/`): the path's own invariants, each containing family's header and remaining
members with their entries, then the advertised families, then (MIK-R05) the route-chain families, in one declared row order, under the same
manifest digest `knowledge_read`'s `source_context` view returns (rule 6; ruling Q4 of 2026-09-29 23:21:57:
conformance is the equal manifest, and entry states follow each surface's code tree). A path with no live
entry **and no governing family** is `registration_absent` through `_refusal_block`, and since MIK-R05 the
refusal also carries `knowledge_leaf.pages.absent_chain(seed.path)`, a `routeChain` stating
`no_governing_family`, the same one `knowledge_read` returns; a path with no entry but a governing family is a
page of its `chain_family` rows stating `registration: registration_absent`. A `PagingRefusal` is unreachable on page 1 (no
continuation), and refused if it ever occurred. `read_published_intent` builds the block's currentness as a
pair, `LeafCurrentness` over the prepared leaves and the scope `WalkCurrentness`, and `_tree_block` renders
`leaves.document(block["seeds"], scopes)`, which merges the two subsets. `_block_policy(seeds)` sets the
block's top-level `policyVersion` (rulings Q5 and N5): `LEAF_POLICY_VERSION_LABEL`
(`family-complete-leaf/v2` since MIK-R05's bump, ruling Q4 of 2026-09-30 03:32:18) when every seed asked is a path (`PathSeed` or `_UnseedablePath`), even when
every path was refused, and `recorded-family-frontier/v1` when the block also has an identity seed, which the
scope read answers (ruling N2 pinned this mixed-block policy with a test). Each page states its own policy in
`page` either way; with no seeds at all, `all()` is true and the leaf label is stated (review R2-I1, not
reachable through `read_ar_files`). `_seed_block` now catches `_SEED_FAILURES`, the input-fact set plus
`IndexMismatchError`, so an index that is not the selected tree's is `snapshot_unavailable` like the other
seed failures.

**A refusal is never an absence.** A path that is not a spelling a recorded source anchor can carry (a Git
pathspec such as `:(exclude)src/integration.py`) is refused **as a seed** by `_source_seed` with
`invalid_payload`, rather than answered with a `registration_absent` this read never observed.  A value
passed to `read_published_intent` that is not one of the typed seeds is answered by
`_unaddressable_seed_block` as a refusal naming its Python type, instead of raising `AttributeError` from
inside the read — `_seed_json` asks the value for its own `model_dump` and answers `None` when it has none.

### Conventions

- **The item is dumped by its own model.** `_item_json` calls `item.model_dump(mode="json", exclude_none=True)`
  rather than re-spelling fields, so a field the read adds later travels without this module deciding
  whether it matters; `exclude_none` keeps the page readable without dropping a recorded value. The
  payload's spellings are therefore the read's own (`kind`, `item_id`, `invariant_id`, `record_id`,
  `revision_id`), never a re-cased copy.
- **The recorded block names what was read and nothing more**: `datasetPath`, `repositoryId`,
  `schemaVersion`, `snapshot` (the logical digest every page was verified against), `policyVersion` and
  `sourceResolution` (`repositoryRoot` plus `codeTreeId`, or `null` when the pair was unrequested), plus
  `memoryTree` only when the selection is a converted memory tree. It claims nothing about history and never
  claims that `context_packet` retrieved invariants.
- `read_git`-style subprocess access goes through the shared `kernel.git_command.run_git` owner; this module
  runs exactly one Git command itself (`rev-parse HEAD^{tree}`) and never a working-tree read; the Git
  commands that capture a converted tree's key run inside `memory/knowledge_index/tree.py`.

### Invariants And Boundaries

- **No second store and no durable state of its own.** The module opens the dataset read-only
  (`open_read_only_database`; no authority-home check applies — the index is keyed by its tree alone) and writes nothing; the page is built by the shipped
  read. The one cache it reaches is the derived knowledge index of a converted tree, which
  `memory/knowledge_index/cache.py` owns, keeps under the coordination runtime (never in a Git working tree)
  and can rebuild from the tree at any time.
- **A partial index is never presented as complete.** Every page read from a tree carries `indexState`, and a
  `partial` one forces `enumerationComplete` to `false`.
- **No enclosure is required to read intent.** The route's only input is a `CoordinationContext`; no task,
  leaf or contract owner is consulted, and `task_ref` is left unset.
- **The absence vocabulary is the shipped one.** This module adds no refusal code and no new state word, so
  existing surfaces do not need a new branch to render it.

## Evidence

### Docs References

No domain documentation source is configured for this repository: `system/sources.md` carries no
`Domain Documentation` entries, so there is no live source to retrieve. The statements below are grounded in
repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- The selected index supplies its own identity; no canonical dataset or caller-asserted identity is selected. [4]


- **The source-resolution pair, resolved together or left unrequested because the read context refuses either half alone.** [6]


- The ordinary route selects converted text knowledge or reports legacy format without a database fallback. [7]


- **The read itself: the shipped taskless context constructor plus the shipped selective read, with `task_ref` left unset and identity seeds passed through; every page is then bound to the tree's index state.** [8]


- **The converted-tree route: which path names a converted tree, the one dataset resolution every knowledge read applies, the refusal without a coordination root, and the index selection that recomputes the tree key.** [9]


- **The ordinary read's converted-tree selection: `None` for an unconverted root, an `unusable` state when the tree cannot be indexed, and no authority-home check because the index is keyed by its tree alone.** [10]


- **MIK-R03: the `currentness` block at the resolved source tree, named with its `treeScope` and computed once inside the bounded block; with no pair, every realized invariant is unverifiable.** [12]



- The complete text-tree knowledge block is bounded by the shared threshold. [13]


- **MIK-R02: a memory-tree seed is prepared for the block, not read as a budgeted page; since MIK-R01 a path seed by the leaf read, an identity seed by the scope read.** [14]

- **MIK-R01: the block's currentness merges the leaf and scope subsets, and its top-level policy follows the seeds asked (rulings Q5 and N5).** [15]

- **MIK-R01: an index that is not the selected tree's is a named seed failure.** [16]
- **MIK-R05: a path seed's `registration_absent` refusal carries its route chain.** [19]

- The published-intent case: the resolved tree and `treeScope`, an uncommitted edit that changes nothing, and no resolved tree. [22]

- **A page from a partial index is never presented as complete.** [23]

- **The two shipped owners this module delegates the read to, reused unchanged.** [24]

- **A path no recorded anchor could carry is refused as a seed instead of being answered with an absence this read never observed.** [27]
- **A value that is not one of the typed seeds is a named refusal naming its own Python type, never an `AttributeError` from inside the read.** [28]
- **One item exactly as the read selected it: dumped by its own model, excluding `None` without dropping a recorded value.** [29]
- **The recorded block that names the dataset, its snapshot, the source pair and — only for a converted memory tree — the `memoryTree` binding, and the block a publication that could not be read answers with.** [30]
- **The failure set modelled as input facts, so a paired read never aborts because a repository's knowledge file was foreign.** [31]

- The dataset identity reader reused here: it answers an identity or a reason, and never raises for a caller. [32]


- The one Git command this route runs, through the shared owner. [34]

- The scope-selection rule the read reports when a seed selects nothing, and the recorded-but-real selection it serves instead of refusing. [35]
- The typed seeds and budget this route constructs, and the policy version the recorded block carries. [36]
- The refusal and item shapes this route renders without re-spelling. [37]
- The storage failure class the input-fact set is built around. [38]
- **The resolver rule this card's memory-root paragraph states: the contract's memory worktree when one is in scope, the canonical external memory root otherwise.** [39]


- The selective block's direct cases: a malformed seed and a path that cannot be a seed are refused, a path with no recorded anchor is a named absence, and an unconverted root refuses `legacy-format` instead of opening a legacy database. [40]



- The carrier-parity case that holds the retrieval instructions to the payload's real field spellings. [42]



- Unconverted roots refuse retired database selection and mounted tools open no legacy database. [44]




- Only a converted root directory is admitted as a knowledge selection; a database path is refused. [46]


### Cross-Repo References

No cross-repository behavior is implemented in this file. The read is addressed at one dataset inside the
memory layer this repository's own coordination declaration resolves, and reaches no sibling repository.

No meaningful cross-repo references found.

### Repo-Internal References

- No read selects the database of a converted tree. [47]
