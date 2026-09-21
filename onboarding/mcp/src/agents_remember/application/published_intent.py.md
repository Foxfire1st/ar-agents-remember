# mcp/src/agents_remember/application/published_intent.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/published_intent.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T18:09+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l20`, uncommitted; production line `71a4433e686b3380af97a0836bb82bab2c8f2aad` |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l19`, uncommitted; base `0fca5c69766aa95eebe950c19fbcdc83864ec35a` |
| lastVerifiedCommitHash | `945ddad6a9c90fbf5d7eef7546b9e69714c6c4fc` |
| lastVerifiedCommitDate | 2026-09-21T18:46:40+02:00|
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
  `sourceResolution` (`repositoryRoot` plus `codeTreeId`, or `null` when the pair was unrequested). It
  claims nothing about history and never claims that `context_packet` retrieved invariants.
- **`continuationOperation` is stated because the answer is not the obvious one.** The cursor a page mints
  is a `read_knowledge_scope` cursor, while the mounted `knowledge_read` tool continues *views* and refuses
  it. A caller that needs more than the page carries reads on **by identity** — the exact
  `invariant_id`/`revision_id` the page returned — rather than paging this cursor through a tool that does
  not accept it.
- `read_git`-style subprocess access goes through the shared `kernel.git_command.run_git` owner; this module
  runs exactly one Git command (`rev-parse HEAD^{tree}`) and never a working-tree read.

### Invariants And Boundaries

- **No second store, no cache, no durable state.** The module opens the dataset read-only
  (`open_read_only_database`, for the authority check) and writes nothing; the page is built by the shipped
  read.
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
| **The one file name a repository's published dataset occupies inside its memory layer, with the comment that now states the current truth: this route declares the location it reads, and the ordinary write side publishes there through `--publish`.** | `PUBLISHED_DATASET_NAME` | mcp/src/agents_remember/application/published_intent.py:110-117 |
| **The location resolver: repository-scoped by construction, following the resolved memory root with no fallback between the canonical root and a leaf's memory worktree.** | `published_dataset_path` | mcp/src/agents_remember/application/published_intent.py:192-208 |
| **The resolution and the guard that make a missing, corrupt or foreign publication a named state rather than an empty success.** | `resolve_published_intent`; `_absence_state` | mcp/src/agents_remember/application/published_intent.py:211-235; mcp/src/agents_remember/application/published_intent.py:238-268 |
| **The dataset's own identity is read from the file rather than taken from a caller.** | `PublishedIntentSelection` | mcp/src/agents_remember/application/published_intent.py:143-156 |
| **The authority-home guard that makes "never silently select another repository" verified rather than claimed.** | `_authority_mismatch`; `_bound_authority_home` | mcp/src/agents_remember/application/published_intent.py:334-351; mcp/src/agents_remember/application/published_intent.py:354-362 |
| **The source-resolution pair, resolved together or left unrequested because the read context refuses either half alone.** | `_source_pair`; `PublishedIntentSourcePair` | mcp/src/agents_remember/application/published_intent.py:310-331; mcp/src/agents_remember/application/published_intent.py:130-140 |
| **The ordinary route's whole public surface: resolve the publication, seed it with the paths the caller already asked about, and read one bounded page per path with every failure returned as a named state.** | `published_intent_block` | mcp/src/agents_remember/application/published_intent.py:271-286 |
| **The read itself: the shipped taskless context constructor plus the shipped selective read, with `task_ref` left unset and identity seeds passed through.** | `read_published_intent` | mcp/src/agents_remember/application/published_intent.py:289-307 |
| **The two shipped owners this module delegates the read to, reused unchanged.** | `open_read_context`; `read_knowledge_scope` | mcp/src/agents_remember/application/knowledge_read.py:103-136; mcp/src/agents_remember/application/knowledge_read.py:139-192 |
| **The per-seed bound, and the page that reports `hasMore`, the counts and the continuation which reaches the rest.** | `PUBLISHED_INTENT_MAX_ITEMS`; `PUBLISHED_INTENT_MAX_UTF8_BYTES`; `_page_block` | mcp/src/agents_remember/application/published_intent.py:122-123; mcp/src/agents_remember/application/published_intent.py:506-529 |
| **The limitation that travels with a bounded page: the cursor continues the scope read, and the mounted read tool continues views.** | "continuationOperation" | mcp/src/agents_remember/application/published_intent.py:528-528 |
| **A path no recorded anchor could carry is refused as a seed instead of being answered with an absence this read never observed.** | `_source_seed`; `_UnseedablePath` | mcp/src/agents_remember/application/published_intent.py:382-396; mcp/src/agents_remember/application/published_intent.py:179-189 |
| **A value that is not one of the typed seeds is a named refusal naming its own Python type, never an `AttributeError` from inside the read.** | `_seed_json`; `_unaddressable_seed_block` | mcp/src/agents_remember/application/published_intent.py:433-446; mcp/src/agents_remember/application/published_intent.py:449-469 |
| **One item exactly as the read selected it: dumped by its own model, excluding `None` without dropping a recorded value.** | `_item_json` | mcp/src/agents_remember/application/published_intent.py:524-532 |
| **The recorded block that names the dataset, its snapshot and the source pair, and the block a publication that could not be read answers with.** | `_recorded_block`; `_unavailable_block` | mcp/src/agents_remember/application/published_intent.py:549-569; mcp/src/agents_remember/application/published_intent.py:572-581 |
| **The failure set modelled as input facts, so a paired read never aborts because a repository's knowledge file was foreign.** | `_PUBLICATION_FAILURES` | mcp/src/agents_remember/application/published_intent.py:127-127 |
| The dataset identity reader reused here: it answers an identity or a reason, and never raises for a caller. | `read_dataset_identity` | mcp/src/agents_remember/application/knowledge_before_half.py:210-223 |
| The read-only connection the authority check opens, and the authority-home row it reads. | `open_read_only_database`; `bound_repository` | mcp/src/agents_remember/memory/knowledge/connection.py:52-63; mcp/src/agents_remember/memory/knowledge/logical.py:178-197 |
| The one Git command this route runs, through the shared owner. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:150-214 |
| The scope-selection rule the read reports when a seed selects nothing, and the recorded-but-real selection it serves instead of refusing. | `_absence_refusal`; `_invariant_identity_is_recorded`; `_family_identity_is_recorded` | mcp/src/agents_remember/application/knowledge_read.py:357-389; mcp/src/agents_remember/application/knowledge_read.py:392-414; mcp/src/agents_remember/application/knowledge_read.py:417-439 |
| The typed seeds and budget this route constructs, and the policy version the recorded block carries. | `PathSeed`; `KnowledgeReadBudget`; `KnowledgeReadRequest`; `KNOWLEDGE_READ_POLICY_VERSION` | mcp/src/agents_remember/models/knowledge/read.py:144-171; mcp/src/agents_remember/models/knowledge/read.py:266-275; mcp/src/agents_remember/models/knowledge/read.py:278-288; mcp/src/agents_remember/models/knowledge/read.py:87-87 |
| The refusal and item shapes this route renders without re-spelling. | `KnowledgeRefusal`; `ReadItem` | mcp/src/agents_remember/models/knowledge/result.py:235-245; mcp/src/agents_remember/models/knowledge/read.py:363-401 |
| The storage failure class the input-fact set is built around. | `KnowledgeStorageError` | mcp/src/agents_remember/memory/knowledge/refusals.py:27-32 |
| **The resolver rule this card's memory-root paragraph states: the contract's memory worktree when one is in scope, the canonical external memory root otherwise.** | `_effective_memory_root` | mcp/src/agents_remember/kernel/coordination_context/resolver.py:356-359 |
| **The application-layer cases that measure this module's route: the exact identities, the named absences, the seed refusals and the identity-seeded page.** | `test_the_ordinary_read_returns_the_published_intent_at_its_exact_identities`; `test_a_repository_that_publishes_nothing_reports_not_recorded`; `test_a_dataset_that_is_not_a_dataset_names_the_failed_binding`; `test_a_directory_at_the_publication_path_is_not_reported_as_nothing_recorded`; `test_a_seed_that_is_not_a_typed_seed_is_refused_rather_than_raising`; `test_a_dataset_bound_to_another_repository_is_never_silently_read`; `test_a_path_the_snapshot_records_nothing_about_is_a_named_absence`; `test_an_identity_the_snapshot_does_not_hold_is_a_named_absence`; `test_a_path_no_recorded_anchor_could_carry_is_refused_as_a_seed`; `test_the_resolved_source_pair_is_what_recorded_anchors_are_observed_against`; `test_an_identity_seeded_page_carries_exact_retained_revisions` | mcp/tests/test_read_ar_files.py:426-461; mcp/tests/test_read_ar_files.py:463-472; mcp/tests/test_read_ar_files.py:474-481; mcp/tests/test_read_ar_files.py:483-499; mcp/tests/test_read_ar_files.py:501-519; mcp/tests/test_read_ar_files.py:546-557; mcp/tests/test_read_ar_files.py:559-567; mcp/tests/test_read_ar_files.py:569-594; mcp/tests/test_read_ar_files.py:596-603; mcp/tests/test_read_ar_files.py:605-631; mcp/tests/test_read_ar_files.py:633-659 |
| **The mounted-route cases: the ordinary `read_ar_files` call reads the memory layer's publication, and names the absence before anything is published.** | `test_the_mounted_route_reads_the_memory_layer_publication`; `test_the_mounted_route_names_the_absence_before_anything_is_published` | mcp/tests/test_read_ar_files.py:703-719; mcp/tests/test_read_ar_files.py:721-736 |
| The carrier-parity case that holds the retrieval instructions to the payload's real field spellings. | `test_the_carrier_uses_the_field_spellings_the_payload_actually_returns` | mcp/tests/test_read_ar_files.py:521-544 |
| The route the ordinary read attaches this block from, the import it attaches it through, and the response field it travels on. | `read_ar_files_tool`; `published_intent_block`; `published_intent` | mcp/src/agents_remember/application/read_files.py:93-162; mcp/src/agents_remember/application/read_files.py:31-31; mcp/src/agents_remember/models/read_files.py:74-74 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The read is addressed at one dataset inside the
memory layer this repository's own coordination declaration resolves, and reaches no sibling repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **the consequence repair this leaf's landing forced, and the two claims it made untrue are restated as current truth.** `ICR-R20@v1` wired the ordinary write side to the location this route declares, so the module docstring's fourth paragraph ("the ordinary write side **has to** publish there … wiring the ordinary publisher to this one location is ICR-R20@v1's obligation") and the `PUBLISHED_DATASET_NAME` comment are now past-tense statements of ownership with a present-tense statement of the route: the ingest command selects this location with `--publish`, resolving it through `published_dataset_path` and reading the published identity back through `resolve_published_intent`, while a run that names no destination and passes no `--publish` still commits without publishing — which is why the destination stays a *selection* rather than a default. `ICR-R25@v1`'s two-consecutive-task journey is unchanged as an outstanding obligation. **This is text only:** the module's code is untouched by the R20 landing, so no behaviour claim on this card changed. **Citation accounting:** the file is 594 → **602** lines (two comment/docstring insertions), so the rows whose cited ranges the insertions moved were re-derived rather than carried — the per-seed bound row `:111-115` / `:498-521` → `:122-123` / `:506-529`, the continuation row `:520-520` → `:528-528`, and the dataset-name row `:102-109` → `:110-117`, whose own prose was corrected with its range because the comment it cites is the sentence this leaf restated. **Stamp accounting:** `reviewedWorkingCandidate` names this leaf's candidate on production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`, which is the line this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded and no stamp was advanced, because no commit contains the body as it now stands. No commit was made.

- 2026-09-21T15:14+02:00 — 260921-ICR-L19 curator (uncommitted change set on `ar/260921-icr-l19`, code base `0fca5c69`): **created this one-to-one card for the new module, the leaf's primary-requirement owner (ICR-R19@v1).** It records the three decisions the module owns — which dataset (`<memory_root>/knowledge.sqlite`, with the memory-worktree-versus-canonical-root rule and no fallback between them), which source identity (the pair resolved together or left unrequested) and what a caller reads (one bounded page per seed through the shipped selective read) — plus the rules that make its answers safe: every failure is a named state (`not-recorded` only when the location holds no file system entry at all; `unusable` for a non-file entry, undecodable bytes or another repository's dataset), a refusal is never reported as an absence (an unseedable path and an unaddressable seed are both refusals), the module holds no second store and adds no refusal vocabulary, and the bounded page's cursor continues the scope read rather than the mounted view read. **Stamp accounting:** this file does not exist at the recorded `lastVerifiedCommitHash`; that hash is the line this reading was performed against and the `reviewedWorkingCandidate` row names the uncommitted candidate, because no commit contains the module yet and the governed closeout owns the real stamp. No commit was made.
