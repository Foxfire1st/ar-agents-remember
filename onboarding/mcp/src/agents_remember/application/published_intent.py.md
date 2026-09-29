# mcp/src/agents_remember/application/published_intent.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/published_intent.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:01:17+02:00 |
| lastVerifiedCommitHash | `719acba61e491d0b7f1ee82dbeea5314ecec5083` |
| lastVerifiedCommitDate | 2026-09-29T20:27:14+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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
root without the marker keeps the database selection unchanged, and only the read switches: the write
side's `resolve_published_intent` still selects the database, and no writer reaches the index.

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
   exists. `PUBLISHED_INTENT_MAX_ITEMS` (8) and `PUBLISHED_INTENT_MAX_UTF8_BYTES` (8192) bound each page;
   a page that leaves items behind reports `hasMore` and hands back the continuation that reaches them.

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
and each family's stale members, computed by `knowledge_currentness.read_currentness`. **The tree it observes
is the one this route already resolved for the source it returns** (architect ruling 1, 2026-09-29T18:42:37):
the `sourceResolution` pair, the code root's `HEAD^{tree}`. That is the read's own resolved tree, not a
fallback. The block names it (`codeTree.treeId`) and states its scope in `treeScope` (`_TREE_SCOPE`: "states
observed at the committed code tree <id> this read resolved; uncommitted working-tree edits are not
reflected"). When the route resolves no pair, `codeTree` is `null`, there is no `treeScope`, and every realized
invariant is `unverifiable` ("no code tree was requested"). `read_currentness` never raises (ruling N2,
19:13:41), so this function holds no `try` of its own. MIK-R29 may add an explicit tree selector later.

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
- **`continuationOperation` is stated because the answer is not the obvious one.** The cursor a page mints
  is a `read_knowledge_scope` cursor, while the mounted `knowledge_read` tool continues *views* and refuses
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
per-seed page bound can truncate, and the intended deeper read is by identity because the mounted tool does
not consume a scope cursor; and a genuine decoder defect inside the read is reported as an input fact
(`unusable`) rather than surfacing as a bug — a deliberate trade for "the paired read must not fail because
of a foreign file".

## Docs References

No domain documentation source is configured for this repository: `system/sources.md` carries no
`Domain Documentation` entries, so there is no live source to retrieve. The statements below are grounded in
repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The one file name a repository's published dataset occupies inside its memory layer, with the comment that now states the current truth: this route declares the location it reads, and the ordinary write side publishes there through `--publish`.** | `PUBLISHED_DATASET_NAME` | mcp/src/agents_remember/application/published_intent.py:147-147 |
| **The location resolver: repository-scoped by construction, following the resolved memory root with no fallback between the canonical root and a leaf's memory worktree.** | `published_dataset_path` | mcp/src/agents_remember/application/published_intent.py:246-262 |
| **The resolution and the guard that make a missing, corrupt or foreign publication a named state rather than an empty success.** | `resolve_published_intent`; `_absence_state` | mcp/src/agents_remember/application/published_intent.py:211-235; mcp/src/agents_remember/application/published_intent.py:265-289; mcp/src/agents_remember/application/published_intent.py:394-424 |
| **The dataset's own identity is read from the file rather than taken from a caller; since MIK-R23 a selection may also name the converted memory tree it reads through the index (`memory_tree`, `None` for a database).** | `PublishedIntentSelection`; `PublishedMemoryTree` | mcp/src/agents_remember/application/published_intent.py:182-196; mcp/src/agents_remember/application/published_intent.py:199-210 |
| **The authority-home guard that makes "never silently select another repository" verified rather than claimed.** | `_authority_mismatch`; `_bound_authority_home` | mcp/src/agents_remember/application/published_intent.py:525-542; mcp/src/agents_remember/application/published_intent.py:545-553 |
| **The source-resolution pair, resolved together or left unrequested because the read context refuses either half alone.** | `_source_pair`; `PublishedIntentSourcePair` | mcp/src/agents_remember/application/published_intent.py:169-179; mcp/src/agents_remember/application/published_intent.py:501-522 |
| **The ordinary route's whole public surface: resolve the publication — a converted memory tree first, the database otherwise — seed it with the paths the caller already asked about, and read one bounded page per path with every failure returned as a named state.** | `published_intent_block` | mcp/src/agents_remember/application/published_intent.py:427-442 |
| **The read itself: the shipped taskless context constructor plus the shipped selective read, with `task_ref` left unset and identity seeds passed through; every page is then bound to the tree's index state.** | `read_published_intent`; `_bind_index_state` | mcp/src/agents_remember/application/published_intent.py:445-473; mcp/src/agents_remember/application/published_intent.py:484-498 |
| **The converted-tree route: which path names a converted tree, the one dataset resolution every knowledge read applies, the refusal without a coordination root, and the index selection that recomputes the tree key.** | `converted_memory_tree`; `select_knowledge_dataset`; `SelectedKnowledgeDataset`; `_index_selection` | mcp/src/agents_remember/application/published_intent.py:320-325; mcp/src/agents_remember/application/published_intent.py:328-341; mcp/src/agents_remember/application/published_intent.py:313-318; mcp/src/agents_remember/application/published_intent.py:344-363; mcp/src/agents_remember/application/published_intent.py:379-391 |
| **The ordinary read's converted-tree selection: `None` for an unconverted root, an `unusable` state when the tree cannot be indexed, and no authority-home check because the index is keyed by its tree alone.** | `resolve_published_memory_tree`; `_TREE_FAILURES` | mcp/src/agents_remember/application/published_intent.py:159-159; mcp/src/agents_remember/application/published_intent.py:166-166; mcp/src/agents_remember/application/published_intent.py:292-317 |
| **The module docstring paragraph that states the switch: only the read selects a tree, and the write side still selects the database.** | "A converted memory tree is selected as a tree" | mcp/src/agents_remember/application/published_intent.py:54-63 |
| **MIK-R03: the `currentness` block at the resolved source tree, named with its `treeScope`; with no pair, every realized invariant is unverifiable.** | `read_published_intent`; `read_currentness`; `_TREE_SCOPE` | mcp/src/agents_remember/application/published_intent.py:445-473; mcp/src/agents_remember/application/published_intent.py:478-481 |
| **The module docstring paragraph for the currentness block.** | "Returned invariants carry their currentness" | mcp/src/agents_remember/application/published_intent.py:54-58 |
| The published-intent case: the resolved tree and `treeScope`, an uncommitted edit that changes nothing, and no resolved tree. | `test_the_published_intent_block_flags_returned_invariants_at_its_resolved_tree` | mcp/tests/test_knowledge_currentness.py:583-630 |
| **A page from a partial index is never presented as complete.** | "enumerationComplete" | mcp/src/agents_remember/application/published_intent.py:495-497 |
| **The two shipped owners this module delegates the read to, reused unchanged.** | `open_read_context`; `read_knowledge_scope` | mcp/src/agents_remember/application/knowledge_read.py:103-136; mcp/src/agents_remember/application/knowledge_read.py:139-192 |
| **The per-seed bound, and the page that reports `hasMore`, the counts and the continuation which reaches the rest.** | `PUBLISHED_INTENT_MAX_ITEMS`; `PUBLISHED_INTENT_MAX_UTF8_BYTES`; `_page_block` | mcp/src/agents_remember/application/published_intent.py:152-153; mcp/src/agents_remember/application/published_intent.py:689-712 |
| **The limitation that travels with a bounded page: the cursor continues the scope read, and the mounted read tool continues views.** | "continuationOperation" | mcp/src/agents_remember/application/published_intent.py:711-711 |
| **A path no recorded anchor could carry is refused as a seed instead of being answered with an absence this read never observed.** | `_source_seed`; `_UnseedablePath` | mcp/src/agents_remember/application/published_intent.py:233-243; mcp/src/agents_remember/application/published_intent.py:573-587 |
| **A value that is not one of the typed seeds is a named refusal naming its own Python type, never an `AttributeError` from inside the read.** | `_seed_json`; `_unaddressable_seed_block` | mcp/src/agents_remember/application/published_intent.py:624-637; mcp/src/agents_remember/application/published_intent.py:640-660 |
| **One item exactly as the read selected it: dumped by its own model, excluding `None` without dropping a recorded value.** | `_item_json` | mcp/src/agents_remember/application/published_intent.py:715-723 |
| **The recorded block that names the dataset, its snapshot, the source pair and — only for a converted memory tree — the `memoryTree` binding, and the block a publication that could not be read answers with.** | `_recorded_block`; `_memory_tree_block`; `memory_tree_block`; `_unavailable_block` | mcp/src/agents_remember/application/published_intent.py:740-761; mcp/src/agents_remember/application/published_intent.py:764-768; mcp/src/agents_remember/application/published_intent.py:366-376; mcp/src/agents_remember/application/published_intent.py:771-780 |
| **The failure set modelled as input facts, so a paired read never aborts because a repository's knowledge file was foreign.** | `_PUBLICATION_FAILURES` | mcp/src/agents_remember/application/published_intent.py:165-165 |
| The dataset identity reader reused here: it answers an identity or a reason, and never raises for a caller. | `read_dataset_identity` | mcp/src/agents_remember/application/knowledge_before_half.py:210-223 |
| The read-only connection the authority check opens, and the authority-home row it reads. | `open_read_only_database`; `bound_repository` | mcp/src/agents_remember/memory/knowledge/connection.py:52-63; mcp/src/agents_remember/memory/knowledge/logical.py:178-197 |
| The one Git command this route runs, through the shared owner. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:150-214 |
| The scope-selection rule the read reports when a seed selects nothing, and the recorded-but-real selection it serves instead of refusing. | `_absence_refusal`; `_invariant_identity_is_recorded`; `_family_identity_is_recorded` | mcp/src/agents_remember/application/knowledge_read.py:357-389; mcp/src/agents_remember/application/knowledge_read.py:392-414; mcp/src/agents_remember/application/knowledge_read.py:417-439 |
| The typed seeds and budget this route constructs, and the policy version the recorded block carries. | `PathSeed`; `KnowledgeReadBudget`; `KnowledgeReadRequest`; `KNOWLEDGE_READ_POLICY_VERSION` | mcp/src/agents_remember/models/knowledge/read.py:128-155; mcp/src/agents_remember/models/knowledge/read.py:250-259; mcp/src/agents_remember/models/knowledge/read.py:262-272; mcp/src/agents_remember/models/knowledge/read.py:91-91 |
| The refusal and item shapes this route renders without re-spelling. | `KnowledgeRefusal`; `ReadItem` | mcp/src/agents_remember/models/knowledge/result.py:235-245; mcp/src/agents_remember/models/knowledge/read.py:329-367 |
| The storage failure class the input-fact set is built around. | `KnowledgeStorageError` | mcp/src/agents_remember/memory/knowledge/refusals.py:27-32 |
| **The resolver rule this card's memory-root paragraph states: the contract's memory worktree when one is in scope, the canonical external memory root otherwise.** | `_effective_memory_root` | mcp/src/agents_remember/kernel/coordination_context/resolver.py:356-359 |
| **The application-layer cases that measure this module's route: the exact identities, the named absences, the seed refusals and the identity-seeded page.** | `test_the_ordinary_read_returns_the_published_intent_at_its_exact_identities`; `test_a_repository_that_publishes_nothing_reports_not_recorded`; `test_a_dataset_that_is_not_a_dataset_names_the_failed_binding`; `test_a_directory_at_the_publication_path_is_not_reported_as_nothing_recorded`; `test_a_seed_that_is_not_a_typed_seed_is_refused_rather_than_raising`; `test_a_dataset_bound_to_another_repository_is_never_silently_read`; `test_a_path_the_snapshot_records_nothing_about_is_a_named_absence`; `test_an_identity_the_snapshot_does_not_hold_is_a_named_absence`; `test_a_path_no_recorded_anchor_could_carry_is_refused_as_a_seed`; `test_the_resolved_source_pair_is_what_recorded_anchors_are_observed_against`; `test_an_identity_seeded_page_carries_exact_retained_revisions` | mcp/tests/test_read_ar_files.py:434-469; mcp/tests/test_read_ar_files.py:471-480; mcp/tests/test_read_ar_files.py:482-489; mcp/tests/test_read_ar_files.py:491-507; mcp/tests/test_read_ar_files.py:509-527; mcp/tests/test_read_ar_files.py:554-565; mcp/tests/test_read_ar_files.py:567-575; mcp/tests/test_read_ar_files.py:577-602; mcp/tests/test_read_ar_files.py:604-611; mcp/tests/test_read_ar_files.py:613-637; mcp/tests/test_read_ar_files.py:639-665 |
| **The mounted-route cases. Since MIK-R24 the ordinary `read_ar_files` call on an unconverted memory tree returns no knowledge section (`legacy-format`), so the two cases assert that; this module's block is measured directly by the route cases.** | `test_the_mounted_route_returns_no_knowledge_section_for_unconverted_memory`; `test_the_mounted_route_names_the_legacy_format_before_anything_is_published` | mcp/tests/test_read_ar_files.py:709-723; mcp/tests/test_read_ar_files.py:725-729 |
| The carrier-parity case that holds the retrieval instructions to the payload's real field spellings. | `test_the_carrier_uses_the_field_spellings_the_payload_actually_returns` | mcp/tests/test_read_ar_files.py:529-552 |
| The route the ordinary read attaches this block from, the import it attaches it through, and the response field it travels on. | `read_ar_files_tool`; `published_intent_block`; `published_intent` | mcp/src/agents_remember/application/read_files.py:99-170; mcp/src/agents_remember/application/read_files.py:31-31; mcp/src/agents_remember/models/read_files.py:74-74 |
| **The MIK-R23 cases for the converted-tree selection: the ordinary read reads a converted tree through its index, a partial index's pages say so, an unconverted root keeps the database selection, and a real database in an unconverted root reads byte-identically through the tools.** | `test_the_ordinary_read_selects_a_converted_memory_tree_through_its_index`; `test_a_partial_tree_selection_says_it_is_partial`; `test_an_unconverted_memory_root_keeps_the_database_selection`; `test_a_real_database_in_an_unconverted_root_reads_identically` | mcp/tests/test_knowledge_index_reuse.py:294-310; mcp/tests/test_knowledge_index_reuse.py:313-322; mcp/tests/test_knowledge_index_reuse.py:325-333; mcp/tests/test_knowledge_index_surfaces.py:531-553 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The read is addressed at one dataset inside the
memory layer this repository's own coordination declaration resolves, and reaches no sibling repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-29T18:08:49+00:00: Generated citation repair: `PUBLISHED_DATASET_NAME` repointed to mcp/src/agents_remember/application/published_intent.py:147-147. No content impact: mechanical anchor-range projection bound to citation source snapshot 704ba74355bb1716854facdd857416a0cc403be7304c687768829065b4665abc; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:08:49+00:00: Generated citation repair: `_item_json` repointed to mcp/src/agents_remember/application/published_intent.py:715-723. No content impact: mechanical anchor-range projection bound to citation source snapshot 704ba74355bb1716854facdd857416a0cc403be7304c687768829065b4665abc; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:08:49+00:00: Generated citation repair: `_PUBLICATION_FAILURES` repointed to mcp/src/agents_remember/application/published_intent.py:165-165. No content impact: mechanical anchor-range projection bound to citation source snapshot 704ba74355bb1716854facdd857416a0cc403be7304c687768829065b4665abc; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): **the block now carries `currentness` for a converted tree (MIK-R03).** Added the Logic paragraph, an Invariants bullet and three rows. It records architect ruling 1 of 2026-09-29T18:42:37: the block observes the tree this route resolved for its source (`HEAD^{tree}`), names it, and states in `treeScope` that uncommitted edits are not reflected; with no pair it is `unverifiable`. Also ruling N2 of 19:13:41: `read_currentness` never raises, so the route adds no `try` of its own. Rows below the inserted lines were re-pointed by the installed fixer.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Reopened claim re-read (MIK-R24 rule 9).** The two mounted-route cases this row named were renamed and rewritten: `read_ar_files` now returns `legacy-format` with no knowledge section on an unconverted tree (the architect ruling that legacy-format reads are active in this build). The row now names the new cases and says what they assert. This module is unchanged: `published_intent_block` is still what the route cases measure, and a converted tree still reaches it through `read_ar_files`.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): **the module now selects a converted memory tree as a tree (MIK-R23 rule 6).** Added the Purpose paragraph, the "converted-tree route" Logic paragraph (`converted_memory_tree`, `select_knowledge_dataset`, `SelectedKnowledgeDataset`, `_index_selection`, `resolve_published_memory_tree`, `_TREE_FAILURES`, `_bind_index_state`, `memory_tree_block`), the `memoryTree` field of the recorded block, and two new invariants (an unconverted root reads exactly as before; a partial index is never presented as complete). **Corrected a claim this change made untrue:** "no second store, no cache" now names the derived index cache that `memory/knowledge_index/cache.py` owns. Re-read and reworded the reopened rows `PublishedIntentSelection` (+ `PublishedMemoryTree`), `published_intent_block`, `read_published_intent` (+ `_bind_index_state`) and `_recorded_block` (+ both block helpers), each re-measured against the working tree; the fixer's three generated bullets for the first three were written minutes earlier in this same pass and are folded into this entry, because a "claim bytes unchanged" note would be false for reworded claims. Added rows for the new constructs, the docstring paragraph and the MIK-R23 tests. Other rows whose ranges the +160-line delta moved were re-pointed by exact base-to-working line mapping; no other claim wording changed. The verification stamp is not advanced: closeout owns it.
- 2026-09-29T05:53:09+00:00: Generated citation repair: `published_dataset_path` repointed to mcp/src/agents_remember/application/published_intent.py:239-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 08ce78606da3cc2a7c0249e0af5ee18d9cd313bdb4222c759c5a89e3e75efdf0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T05:53:09+00:00: Generated citation repair: `_item_json` repointed to mcp/src/agents_remember/application/published_intent.py:690-698. No content impact: mechanical anchor-range projection bound to citation source snapshot 08ce78606da3cc2a7c0249e0af5ee18d9cd313bdb4222c759c5a89e3e75efdf0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T05:53:09+00:00: Generated citation repair: `_PUBLICATION_FAILURES` repointed to mcp/src/agents_remember/application/published_intent.py:158-158. No content impact: mechanical anchor-range projection bound to citation source snapshot 08ce78606da3cc2a7c0249e0af5ee18d9cd313bdb4222c759c5a89e3e75efdf0; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`models/knowledge/read.py` lost the moved anchor vocabulary; the evidence TOMLs gained one row) were re-measured against the candidate by the curator so each anchor lands on its construct again; no claim wording changed.

- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `_PUBLICATION_FAILURES` repointed to mcp/src/agents_remember/application/published_intent.py:135-135. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **the consequence repair this leaf's landing forced, and the two claims it made untrue are restated as current truth.** `ICR-R20@v1` wired the ordinary write side to the location this route declares, so the module docstring's fourth paragraph ("the ordinary write side **has to** publish there … wiring the ordinary publisher to this one location is ICR-R20@v1's obligation") and the `PUBLISHED_DATASET_NAME` comment are now past-tense statements of ownership with a present-tense statement of the route: the ingest command selects this location with `--publish`, resolving it through `published_dataset_path` and reading the published identity back through `resolve_published_intent`, while a run that names no destination and passes no `--publish` still commits without publishing — which is why the destination stays a *selection* rather than a default. `ICR-R25@v1`'s two-consecutive-task journey is unchanged as an outstanding obligation. **This is text only:** the module's code is untouched by the R20 landing, so no behaviour claim on this card changed. **Citation accounting:** the file is 594 → **602** lines (two comment/docstring insertions), so the rows whose cited ranges the insertions moved were re-derived rather than carried — the per-seed bound row `:111-115` / `:498-521` → `:122-123` / `:506-529`, the continuation row `:520-520` → `:528-528`, and the dataset-name row `:102-109` → `:110-117`, whose own prose was corrected with its range because the comment it cites is the sentence this leaf restated. **Stamp accounting:** the recorded working candidate names this leaf's candidate on production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`, which is the line this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded and no stamp was advanced, because no commit contains the body as it now stands. No commit was made.

- 2026-09-21T15:14+02:00 — 260921-ICR-L19 curator (uncommitted change set on `ar/260921-icr-l19`, code base `0fca5c69`): **created this one-to-one card for the new module, the leaf's primary-requirement owner (ICR-R19@v1).** It records the three decisions the module owns — which dataset (`<memory_root>/knowledge.sqlite`, with the memory-worktree-versus-canonical-root rule and no fallback between them), which source identity (the pair resolved together or left unrequested) and what a caller reads (one bounded page per seed through the shipped selective read) — plus the rules that make its answers safe: every failure is a named state (`not-recorded` only when the location holds no file system entry at all; `unusable` for a non-file entry, undecodable bytes or another repository's dataset), a refusal is never reported as an absence (an unseedable path and an unaddressable seed are both refusals), the module holds no second store and adds no refusal vocabulary, and the bounded page's cursor continues the scope read rather than the mounted view read. **Stamp accounting:** this file does not exist at the recorded `lastVerifiedCommitHash`; that hash is the line this reading was performed against and the recorded working candidate names the uncommitted candidate, because no commit contains the module yet and the governed closeout owns the real stamp. No commit was made.
