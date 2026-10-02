# mcp/src/agents_remember/application/published_intent.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The dataset selection the ordinary paired read never had (ICR-R19@v1).** `application/knowledge_read.py`
has served a *taskless read at one exact snapshot* since KS-R07, but nothing on the ordinary route ever
chose a dataset, so a fresh planner had no way to read what this repository had already intended. This
module is that choice: from the `CoordinationContext` the ordinary read already carries, it resolves the
repository's published knowledge dataset, resolves the source-resolution pair recorded anchors are
observed against, seeds the shipped selective read with the paths the caller asked about (or with exact
record identities), and shapes one bounded page per seed with every absence named.

It is not a second read. It decides **three** things — which dataset, which source identity, what a caller
reads — and delegates the read itself to the shipped owners: `open_read_context` (the taskless,
exact-snapshot context constructor) and `read_knowledge_scope` (the selective read). It selects and
shapes; it never selects rows itself, holds no second store, no cache and no durable state, opens the
dataset read-only, and adds no refusal vocabulary — every code it emits
(`selected_input_unavailable`, `snapshot_unavailable`, `registration_absent`, `selector_absent`,
`page_budget_too_small`, `invalid_payload`) is the shipped one, so surfaces that already branch on those
codes need no new member.

**Since MIK-R23 it also selects a converted memory tree as a tree.** When the memory root holds the
text-knowledge layout marker (`knowledge/layout.json`), there is no published database to select: the
ordinary read's published intent is the memory tree itself, read through the derived knowledge index
(`memory/knowledge_index/`) built from the tree's captured state and cached under the coordination
runtime. The index file is a dataset of the store's schema, so the same `open_read_context` +
`read_knowledge_scope` pair reads it. The same resolution (`select_knowledge_dataset`) is what the mounted
`knowledge_read`, `knowledge_diff` and `knowledge_project` tools apply to a caller's `databasePath`. A memory
root without the marker keeps the database selection unchanged, and no writer reaches the index.

**The write side never selects a converted tree's database either (260928-MIK-L37; MIK-R37 rule 3; decision
record DEC-YZA7E4).** `resolve_published_intent` first asks `converted_memory_tree(context.memory_root)`. For a
converted root it returns `PublishedIntentUnavailable(state="not-recorded", code="selected_input_unavailable")`
without opening the file: the detail names the tree and says that its knowledge is text, read through the derived
index of that tree (MIK-R23), that no knowledge dataset is published at the path, and that the database file
frozen there is not read. Its callers therefore report the publication location of a converted tree as
`not-recorded`: the final-output receipt, the sync rebinding, the bootstrap and `memory_init` foundation reads,
and the ingest read-back. An unconverted root resolves exactly as before.

## Code Commentary

### Logic

**Three decisions, and the module owns exactly these.**

1. **Which dataset.** `published_dataset_path` returns `context.memory_root / PUBLISHED_DATASET_NAME`
   (`knowledge.sqlite`). Selection is repository-scoped by construction: there is no argument a caller can
   aim at another repository's dataset, and a repository that declares no memory layer has no published
   intent to read rather than a neighbour's to borrow. *Which* memory root that is follows the resolved
   scope and the difference is load-bearing — `resolve_coordination_context` returns the contract's memory
   **worktree** whenever an enclosure is in scope and the canonical external memory root otherwise
   (`kernel/coordination_context/resolver.py`, `_effective_memory_root`). This route substitutes neither
   for the other, so a publication that is not on the line being read is reported `not-recorded`.
   **This route declares the location it reads, and since `ICR-R20@v1` the ordinary write side publishes
   there.** Before that leaf no shipped owner computed or defaulted a publication destination at all:
   `IngestPublication.destination_path` was whatever the caller's `--publish-to` named, and an ingest run
   that named none committed without publishing. The ingest command now selects this one location with
   `--publish` — resolving it through `published_dataset_path`, the same declaration this read uses, and
   reading the published identity back through `resolve_published_intent` — while a run that names no
   destination and passes no `--publish` still commits without publishing, which is why the destination
   stays a *selection* rather than a default. The two-consecutive-task journey that has to prove task A's
   publication lands where task B's planner looks is still ICR-R25@v1's; declaring it here is what gives
   both sides one shared spelling.
2. **Which source identity.** The read context requires the source-resolution pair *together or not at
   all*, so `_source_pair` resolves the code repository root and `HEAD^{tree}` as one value, and answers
   `None` — leaving the pair *unrequested* — for a root that is None, a Git that cannot answer, a non-zero
   exit, or an answer that is not an object id. A pair that cannot be resolved is never completed with a
   fabrication.
3. **What a caller reads.** `published_intent_block` (the ordinary route's whole public surface) seeds one
   `PathSeed` per requested path and calls `read_published_intent`, which opens the context and builds one
   page per seed with `read_knowledge_scope`, passing the caller's identity seeds through unchanged.
   `task_ref` is left unset, because planning has to be able to read recorded knowledge before a leaf
   exists. `PUBLISHED_INTENT_MAX_ITEMS` (8) and the byte bound (8192, private as `_DATABASE_PAGE_MAX_UTF8_BYTES`
   since MIK-R02) bound each **database** page; a page that leaves items behind reports `hasMore` and hands
   back the continuation that reaches them. A memory-tree page is cut by the shared token threshold instead
   (below).

**The converted-tree route (MIK-R23 rule 6).** `converted_memory_tree(path)` answers the tree a dataset
selection names: the path itself when it is a directory holding `knowledge/layout.json`, or its parent when
the path is the published `<memory-root>/knowledge.sqlite` location inside a converted tree (the file a caller
was handed before the conversion is no longer the source of truth); anything else is `None`.
`select_knowledge_dataset(path, coordination_root=…)` returns a `SelectedKnowledgeDataset` — the path
unchanged with no tree for an unconverted selection, or the index of the tree's current state — and refuses a
converted selection with `MemoryTreeError` when no coordination root is known to keep the index under.
`_index_selection` opens `KnowledgeIndexCache(default_cache_directory(coordination_root)).for_directory`,
which recomputes the tree key on every call (rule 5), and records the tree as a `PublishedMemoryTree`
(`memory_root`, `tree_key`, `index_state`, `problems`). `resolve_published_memory_tree(context)` wraps that
for the ordinary read: `None` for an unconverted memory root, a `PublishedIntentSelection` whose
`database_path` is the index file and whose `memory_tree` names the tree, or an `unusable` state when the tree
cannot be indexed (`_TREE_FAILURES` = the input-fact set plus `MemoryTreeError`). No authority-home check
applies there: the index is keyed by its tree alone, and its namespace is the index's constant one.
`published_intent_block` tries this route first and falls back to `resolve_published_intent` only when it
answers `None`. `read_published_intent` passes each seed block through `_bind_index_state`, which adds
`indexState` to every page read from a tree and forces `enumerationComplete` to `false` when the index is
`partial` — a partial index is never presented as complete. `memory_tree_block` is the one wire spelling of
the binding (`memoryRoot`, `treeId`, `indexState`, `problems[]`), shared with the mounted tools.

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

**Every way the selection can fail is a named state rather than an empty success.** `_absence_state`
separates two facts a caller acts on differently and one answer cannot state both: `not-recorded` is
returned **only** when the location holds no file system entry at all (`not exists() and not is_symlink()`),
so a repository whose knowledge begins later is not a repository whose history was measured as empty;
anything else that is not a regular file — a directory, a dangling link, a device — is `unusable` with
`selected_input_unavailable`, because something was *put there* and reporting it as "nothing is recorded"
would hide it. `resolve_published_intent` then reads the dataset's **own** namespace/schema/digest through
`read_dataset_identity` rather than trusting a caller, and `_authority_mismatch` compares the authority home
the dataset records against the context's repository name, refusing by name — that comparison is what makes
"never silently select another repository" a verified fact instead of a claim. `_PUBLICATION_FAILURES`
(`KnowledgeStorageError`, `apsw.Error`, `OSError`, `ValidationError`) is the failure set modelled as *input
facts*, deliberately including `ValidationError`: a dataset whose stored rows this build cannot decode is an
input the route was handed, and a paired read that aborted on a foreign file would trade one gap for a worse
one.

**A refusal is never an absence.** A path that is not a spelling a recorded source anchor can carry (a Git
pathspec such as `:(exclude)src/integration.py`) is refused **as a seed** by `_source_seed` with
`invalid_payload`, rather than answered with a `registration_absent` this read never observed. A record
identity the snapshot does not hold is the read's own `selector_absent`, the named absence of a generation
this snapshot does not carry; today's database is never substituted for a historical generation. A value
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
- **`continuationOperation` is stated because the answer is not the obvious one.** On a memory tree it is
  `knowledge_read`, which resumes the shared token (MIK-R02). On a database the cursor a page mints is a
  `read_knowledge_scope` cursor, while the mounted `knowledge_read` tool continues *views* and refuses
  it. A caller that needs more than the page carries reads on **by identity** — the exact
  `invariant_id`/`revision_id` the page returned — rather than paging this cursor through a tool that does
  not accept it.
- `read_git`-style subprocess access goes through the shared `kernel.git_command.run_git` owner; this module
  runs exactly one Git command itself (`rev-parse HEAD^{tree}`) and never a working-tree read; the Git
  commands that capture a converted tree's key run inside `memory/knowledge_index/tree.py`.

### Invariants And Boundaries

- **No second store and no durable state of its own.** The module opens the dataset read-only
  (`open_read_only_database`, for the authority check) and writes nothing; the page is built by the shipped
  read. The one cache it reaches is the derived knowledge index of a converted tree, which
  `memory/knowledge_index/cache.py` owns, keeps under the coordination runtime (never in a Git working tree)
  and can rebuild from the tree at any time.
- **An unconverted memory root reads exactly as before.** Without `knowledge/layout.json`,
  `resolve_published_memory_tree` answers `None`, the database selection runs unchanged, no `memoryTree` or
  `indexState` field appears and no cache is created.
- **Currentness never edits or withholds the pages, and never refuses the block.** A stale invariant stays in
  its page; a currentness failure is stated as `unverifiableReason`. An unconverted root carries no
  `currentness` key.
- **A memory tree's knowledge block never exceeds the threshold**, except a single row too large on its own,
  returned alone and flagged `oversized_row`; every seed's selected rows are returned exactly once across the
  block and its continuations (MIK-R02).
- **A path on a converted tree is read family-complete, and the database path is not.** The leaf read is
  reached only when `memory_tree` is set; a database selection keeps `read_knowledge_scope` pages and its
  block keeps `recorded-family-frontier/v1`. The worker and both review rounds measured unconverted reads
  byte-identical to base.
- **A partial index is never presented as complete.** Every page read from a tree carries `indexState`, and a
  `partial` one forces `enumerationComplete` to `false`.
- **No fallback between memory roots, and no cross-repository substitution.** A publication that is not on
  the line being read is `not-recorded`; a dataset bound to another authority home is refused by name with
  no rows served.
- **No enclosure is required to read intent.** The route's only input is a `CoordinationContext`; no task,
  leaf or contract owner is consulted, and `task_ref` is left unset.
- **The absence vocabulary is the shipped one.** This module adds no refusal code and no new state word, so
  existing surfaces do not need a new branch to render it.
- **Boundary.** The selection policy is here; the read (`application/knowledge_read.py`), the dataset
  identity reader (`application/knowledge_before_half.py`), the connection and authority readers
  (`memory/knowledge/connection.py`, `memory/knowledge/logical.py`), the read models
  (`models/knowledge/read.py`) and the refusal vocabulary (`memory/knowledge/refusals.py`) are all reused
  unchanged. `application/knowledge_read.py` was deliberately **not** touched by this leaf: the gap was the
  caller, not the read.

### Todos

No implementation scope is opened here. Three carried observations belong to the owning seats rather than
to this file: the identity-seed entry point is production code with no mounted caller (the MCP surface
reaches identity reads through `knowledge_read` plus the returned `datasetPath`/`repositoryId`); the
per-seed page bound of a **database** read can truncate, and the intended deeper read there is by identity
because the mounted tool does not consume a database scope cursor (a memory tree's pages continue through
`knowledge_read` since MIK-R02); and a genuine decoder defect inside the read is reported as an input fact
(`unusable`) rather than surfacing as a bug — a deliberate trade for "the paired read must not fail because
of a foreign file".

## Evidence

### Docs References

No domain documentation source is configured for this repository: `system/sources.md` carries no
`Domain Documentation` entries, so there is no live source to retrieve. The statements below are grounded in
repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The one file name a repository's published dataset occupies inside its memory layer, with the comment that now states the current truth: this route declares the location it reads, and the ordinary write side publishes there through `--publish`.** [1]
- **The location resolver: repository-scoped by construction, following the resolved memory root with no fallback between the canonical root and a leaf's memory worktree.** [2]
- **The resolution and the guard that make a missing, corrupt or foreign publication a named state rather than an empty success.** [3]
- **The dataset's own identity is read from the file rather than taken from a caller; since MIK-R23 a selection may also name the converted memory tree it reads through the index (`memory_tree`, `None` for a database).** [4]
- **The authority-home guard that makes "never silently select another repository" verified rather than claimed.** [5]
- **The source-resolution pair, resolved together or left unrequested because the read context refuses either half alone.** [6]
- **The ordinary route's whole public surface: resolve the publication — a converted memory tree first, the database otherwise — seed it with the paths the caller already asked about, and read one bounded page per path with every failure returned as a named state.** [7]
- **The read itself: the shipped taskless context constructor plus the shipped selective read, with `task_ref` left unset and identity seeds passed through; every page is then bound to the tree's index state.** [8]
- **The converted-tree route: which path names a converted tree, the one dataset resolution every knowledge read applies, the refusal without a coordination root, and the index selection that recomputes the tree key.** [9]
- **The ordinary read's converted-tree selection: `None` for an unconverted root, an `unusable` state when the tree cannot be indexed, and no authority-home check because the index is keyed by its tree alone.** [10]
- **The module docstring paragraph that states the switch: only the read selects a tree, and the write side still selects the database.** [11]
- **MIK-R03: the `currentness` block at the resolved source tree, named with its `treeScope` and computed once inside the bounded block; with no pair, every realized invariant is unverifiable.** [12]
- **MIK-R02: a memory tree's whole knowledge block is bounded by the shared threshold, with the database path unchanged; since MIK-R01 only scope seeds feed the scope currentness computation.** [13]
- **MIK-R02: a memory-tree seed is prepared for the block, not read as a budgeted page; since MIK-R01 a path seed by the leaf read, an identity seed by the scope read.** [14]
- **MIK-R01: the block's currentness merges the leaf and scope subsets, and its top-level policy follows the seeds asked (rulings Q5 and N5).** [15]
- **MIK-R01: an index that is not the selected tree's is a named seed failure.** [16]
- **The module docstring paragraph for the family-complete leaf read.** [17]
- **MIK-R05: the docstring states the route-chain families after the leaf content, an entry-less path still returning them, and the refusal of a path with neither.** [18]
- **MIK-R05: a path seed's `registration_absent` refusal carries its route chain.** [19]
- **The module docstring paragraph for the bounded block and its continuation.** [20]
- **The module docstring paragraph for the currentness block.** [21]
- The published-intent case: the resolved tree and `treeScope`, an uncommitted edit that changes nothing, and no resolved tree. [22]
- **A page from a partial index is never presented as complete.** [23]
- **The two shipped owners this module delegates the read to, reused unchanged.** [24]
- **The database page's bounds (the byte bound private since MIK-R02), and the page that reports `hasMore`, the counts and the database cursor.** [25]
- **The limitation that travels with a database page: its cursor continues the scope read, which the mounted read tool does not resume.** [26]
- **A path no recorded anchor could carry is refused as a seed instead of being answered with an absence this read never observed.** [27]
- **A value that is not one of the typed seeds is a named refusal naming its own Python type, never an `AttributeError` from inside the read.** [28]
- **One item exactly as the read selected it: dumped by its own model, excluding `None` without dropping a recorded value.** [29]
- **The recorded block that names the dataset, its snapshot, the source pair and — only for a converted memory tree — the `memoryTree` binding, and the block a publication that could not be read answers with.** [30]
- **The failure set modelled as input facts, so a paired read never aborts because a repository's knowledge file was foreign.** [31]
- The dataset identity reader reused here: it answers an identity or a reason, and never raises for a caller. [32]
- The read-only connection the authority check opens, and the authority-home row it reads. [33]
- The one Git command this route runs, through the shared owner. [34]
- The scope-selection rule the read reports when a seed selects nothing, and the recorded-but-real selection it serves instead of refusing. [35]
- The typed seeds and budget this route constructs, and the policy version the recorded block carries. [36]
- The refusal and item shapes this route renders without re-spelling. [37]
- The storage failure class the input-fact set is built around. [38]
- **The resolver rule this card's memory-root paragraph states: the contract's memory worktree when one is in scope, the canonical external memory root otherwise.** [39]
- **The application-layer cases that measure this module's route: the exact identities, the named absences, the seed refusals and the identity-seeded page.** [40]
- **The mounted-route cases. Since MIK-R24 the ordinary `read_ar_files` call on an unconverted memory tree returns no knowledge section (`legacy-format`), so the two cases assert that; this module's block is measured directly by the route cases.** [41]
- The carrier-parity case that holds the retrieval instructions to the payload's real field spellings. [42]
- The route the ordinary read attaches this block from, the import it attaches it through, and the response field it travels on. [43]
- **The MIK-R23 cases for the converted-tree selection: the ordinary read reads a converted tree through its index, a partial index's pages say so, an unconverted root keeps the database selection, and a real database in an unconverted root reads byte-identically through the tools.** [44]

- A converted memory tree publishes no dataset: the resolution answers not-recorded, naming the tree, and never opens the frozen database. [45]
- No read selects the database of a converted tree. [46]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The read is addressed at one dataset inside the
memory layer this repository's own coordination declaration resolves, and reaches no sibling repository.

No meaningful cross-repo references found.
