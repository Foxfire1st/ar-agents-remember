# mcp/src/agents_remember/memory/ - Memory Repository Lifecycle And Knowledge Storage Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/memory/` |
| the recorded working candidateNote | the verification tuple above was recorded by 260915-KS-L45; this row names the 260915-KS-L43 reading performed against the same line |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## 260928-MIK-L37 The Cutover: Card Authoring, The Frozen Publication Sink, And History Files By Path

`260928-MIK-L37` (MIK-R37). What earlier sections of this overview call "inert until the cutover" is what the code does on converted memory: a
memory tree that holds `knowledge/layout.json`.

- **[`conversion/card_authoring.py`](conversion/card_authoring.py.md) (new).** The fixer on a converted tree
  authors a card's citation table into `- <finding> [n]` lines and sidecar references with resolved anchors:
  a new card's sidecar, a reference re-authored by its number, and, for one named card, the removal of references
  its Markdown no longer cites. Every card is checked before anything is written, and a card whose citation table
  touches another table with no blank line between them is refused by name.
- **[`knowledge/publication.py`](knowledge/publication.py.md).** `publish_prepared_snapshot` refuses a destination
  inside a converted memory tree as `database_frozen` (MIK-R37 rule 3), at the one install sink.
- **[`carryover.py`](carryover.py.md).** `memory_carryover_apply` refuses a converted target, naming the file
  writer, and takes the cutover lock for an unconverted one.
- **[`knowledge_index/build.py`](knowledge_index/build.py.md).** The parsed tree holds each history file by path
  and each owner's merged history, so a reopened leaf's closed file and later attempts are all indexed.
- **[`knowledge_index/tree.py`](knowledge_index/tree.py.md) and [`knowledge_index/query.py`](knowledge_index/query.py.md).**
  The working-tree capture copies the repository's index with its modification time, so a file rewritten in the
  second the index was written changes the key (INV-656CYW); `KnowledgeIndex.history_row` answers one history row
  by its ID.
- [`conversion/crossing_sync.py`](conversion/crossing_sync.py.md): a docstring correction only.

- The card authoring's entry. [114]
- The publication sink refuses a converted destination. [115]
- Carryover writes legacy-format memory only, and only while the repository is not locked. [116]
- The index keeps each history file by path. [117]

- Two tables with no blank line between them are refused when either holds citations. [118]
- The capture copies the index with its time. [119]


## Requirement Endpoints, Approval State And Their Recorded Reads

[`knowledge/requirement_endpoint.py`](knowledge/requirement_endpoint.py.md) resolves a requirement endpoint of a
knowledge record, `{task: {repository, path}, packet, id, version}`, and answers which version of a requirement its
owning task approves.

- **Resolution.** `resolve_requirement_endpoint` locates the owning task root
  `<coordination root>/tasks/<repository>/<path>` and hands `{packet, id, version}` to
  [`knowledge/requirement_owner.py`](knowledge/requirement_owner.py.md)'s `consume_owner_resolution`, whose answer
  it carries back unchanged. The requirement owner is the resolver. The module's own answers are about the root only:
  `requirement-task-plane-unavailable` without a coordination root, and `requirement-task-outside-tasks` for a
  repository that is not one directory name. An endpoint that does not resolve is reported as `unresolved`; the
  function does not raise for it. `task_root` is set whenever the root could be located.
- **Approval.** `requirement_approval(task_root, stable_id)` reads the owning task's `requirements/manifest.json`
  (format `approved-requirement-corpus`, the `packets` list only) and answers `approved` with the highest approved
  version of the ID and its packet path, `not_approved` when the manifest approves no entry of the ID, or `unknown`
  with the reason when there is no manifest it can read. Versions compare by the integer after `v`, and `newer_than`
  is true only for a higher approved version, so a task without a readable manifest never counts as approving a newer
  one. `latest_approved_requirement_version` returns the same lookup's latest version.
- **Callers.** The knowledge writer (`application/knowledge_writer/requirement_links.py`) resolves endpoints. The
  worklist's reconsideration step (`application/knowledge_worklist/reconsideration.py`) resolves an endpoint and asks
  for the approval from the resolved `task_root`; an unresolved endpoint triggers nothing.
- **Recorded reads.** The approval state and the packets live outside every Git tree. `_manifest` reads the
  manifest's bytes once and records, through `kernel/recorded_reads.record_read`, the SHA-256 of exactly those bytes,
  `absent` for a missing manifest, or `unreadable (<error type>)` for a failed read. The module does not record the
  linked packet. The owner it hands the packet to (`_approved_packet_ref` in `tasks/task_intent.py`) records the
  resolution of the task root and of the packet locator and the bytes it reads. Outside a recording block nothing is
  recorded.
- **The gate's kept verdict.** The mandatory gate evaluates inside a recording block and keeps its verdict with that
  read set. Before it serves a kept verdict it repeats every recorded path resolution and existence probe, and hashes
  the recorded files again only when those still give the recorded answers. A newly approved version, a manifest that
  appears and a packet link that is retargeted, also to a file with identical bytes, therefore force a recomputation.

- The endpoint's state, code, detail, task root and key. [134]
- The task root, or none for a repository that is not one directory name. [135]
- The resolution: no root, a root outside tasks, or the owner's answer; no packet is recorded here. [136]
- The approval answer and the comparison with a version. [137]
- The manifest read records the bytes, an absent manifest or a failed read. [138]
- The approval lookup with its three states. [139]
- The latest approved version of one ID. [140]
- The owner the packet question is handed to. [141]
- The owner records the two resolutions and the packet's bytes. [142]
- The reconsideration step resolves the endpoint and asks for the approval. [129]
- A kept gate verdict is served only when no recorded observation changed. [130]
- The manifest lookup returns the highest approved version. [131]
- A requirement endpoint triggers only on a newer approved version. [132]
- The gate's warm pass becomes the refusal when a packet locator is retargeted to identical bytes. [133]

## A Missing Object Is Told From A Git Failure

`CodeObjects.has_blob` ([`conversion/code_objects.py`](conversion/code_objects.py.md)) answers `False` for Git's
documented not-found answer (`cat-file -e` exits 1) and for an object that is not a blob. Any other failure of Git
raises `CodeObjectError` with Git's message, and a timeout raises `subprocess.TimeoutExpired`. A caller therefore reports an unreadable input and never an
absent one; the worklist's code reader (`application/knowledge_worklist/code.py`) turns the failure into a
`CodeReadError`.

- A missing object against a Git failure. [2]

## 260928-MIK-L29 Five Index Lookups For The Knowledge Reader

**Route meaning extended (MIK-R29).** The path-based knowledge reader (`application/knowledge_reader/`) is served
from the derived index of the selected tree, and [`knowledge_index/query.py`](knowledge_index/query.py.md) gains five
additive lookups for it. Each is an ordinary `Answer[T]` carrying the index state, so a partial index is never read as
a complete answer:

- `entries_under(directory)`: every entry at or below a directory (the root route `.` holds all). A path prefix never
  matches a sibling that merely shares its spelling (`dash` holds `dash/x`, not `dashboard/x`).
- `entries_in_directory(directory)`: the entries of the files directly in a directory, for the reader's bounded
  directory view (review F2).
- `live_entry_paths_under(directory)`: the source path of each entry whose invariant is a live record, for the
  counts the explorer, the directory summary and the subtree agree on.
- `links_to_path(path)`: every relationship whose target is the anchor or route at the path.
- `records_of_kind(kind)`: every record of one kind, built on `record_ids`.

`_incoming` now delegates to a shared `_links` with the same SQL and order, so earlier callers are unaffected. The
index schema, `INDEX_FORMAT`, the key and the cache are unchanged; building a commit's index writes only the
coordination runtime's cache, which the architect confirmed is L23's design and not a repository write (ruling
2026-09-30T09:42:58 Q2).

- Entries at or under a directory, and of the files directly in it. [5]
- Live entry paths, links to a path, and every record of a kind. [6]
- The shared link query `_incoming` delegates to. [7]

## 260928-MIK-L25 The Index's Revision Rows Carry The Store's Own Seal, And A Record-ID Lookup

**Route meaning extended (MIK-R25, a shared fix in L23's code; ruling 2026-09-29T22:22:37 Q6).** The reviewer reads
each memory side of a converted leaf through the derived index of its tree, and its family roster reads revisions
through the store's revision readers, which verify the logical payload seal on every decode. The index's projected
revision rows carried `sha256(record)` instead, so every index was refused there.

- [`knowledge_index/projection.py`](knowledge_index/projection.py.md): each projected `invariant_revision` and
  `family_revision` row now carries `revision_payload_digest`/`family_revision_payload_digest` over exactly the
  projected cells, so an index reads as a dataset for the revision readers too.
- [`knowledge_index/schema.py`](knowledge_index/schema.py.md): `INDEX_FORMAT` is `ar-knowledge-index/v2`, so a v1
  cache is treated as absent and rebuilt rather than reused.
- [`knowledge_index/query.py`](knowledge_index/query.py.md): `record_ids(kind)`, every record ID of one kind in the
  tree, for the reviewer's per-side currentness.

L23, L03 and L08 tests still pass (worker ruling round). No database copy is part of a review: the derived index is
the permitted read path (Q1).

- The store's own seal on each projected revision row. [8]
- The format bump that rebuilds v1 caches. [9]
- Every record ID of one kind, sorted; since MIK-R29 the reader's `records_of_kind` is built on it. [10]

## 260928-MIK-L01 The Path-Absence Refusal Can Name Proof Claims

**Route impact (MIK-R01@v2), one additive keyword.** The family-complete leaf read of a converted tree
(`application/knowledge_leaf/`) seeds on realization *and* proof entries at a path (ruling Q3 of 2026-09-29
23:21:57), so a path with neither is `registration_absent` with wording that says so:
[`knowledge/read_refusals.py`](knowledge/read_refusals.py.md)'s `registration_absent_refusal` takes
`with_proofs: bool = False`, and the leaf read passes `True` (ruling N6 of 2026-09-30 00:08:39). The default
wording, used by the recorded-scope read and the diff, is byte-for-byte unchanged. Nothing else on this route
changed: the leaf read reaches the derived index only through `KnowledgeIndex`'s existing answers
(`entries_at_path`, `invariant`, `family`, `record`, `text_id`), with no `INDEX_FORMAT` change.

- The absence refusal, naming proof claims when the leaf read asks. [13]

## 260921-ICR-L57 The Observation Row Codec Is Its Own Module, And `evidence_records` Still Answers For It

`knowledge/evidence_records.py` had reached 1210 lines, over the 1200-line rail. `260921-ICR-L57` moved
the one codec with no dependency on the others, the `verification_observation` row codec, verbatim into
`knowledge/evidence_observation_rows.py`: `observation_cells`, `OBSERVATION_COLUMNS`, `observation_row`,
`observation_row_digest`, `decode_observation_row` and the private column-group decoders.
`evidence_records` imports all five public names and keeps them in its `__all__`, so `evidence.py`,
`evidence_read.py` and the tests still reach the codec through `evidence_records`. No import site and
no behaviour changed (1006 lines remain). For this route the rule is unchanged: `evidence_records` is
the one public door to the supporting-record codecs; the new module is where one of them is defined.

- The re-export and the registered surface that keep callers on `evidence_records`. [14]
- The codec's own module statement. [15]

## 260921-ICR-L56 Anchor Observation Remembers Immutable Answers, Never Availability

Anchor observation now keeps a bounded, process-lifetime memo so one review's owners and one comparison's
subjects stop re-asking Git and re-parsing the same trees and blobs (ICR-R24@v3; first family/invariant
visit about 1.3–1.6 s → about 0.3 s, with sha256-identical responses). The split across this route is
deliberate: **`knowledge/read_anchor_memo.py` stores and bounds** (a weight-bounded LRU table, three
tables keyed by repository root plus complete object ids, the one complete-id admission test) and knows
nothing about anchors; **`knowledge/read_anchors.py` decides what may be remembered** — only content
answers (tree entries including a definite absence, blob lines, per-grammar definitions), only after Git
or the parser answered, only for complete ids. Whether a repository still *holds* a tree is never
remembered: every resolver probes it afresh and remembered answers are served only behind that probe. The
two uncovered residuals (a present tree whose blob was lost; resolver-less callers, i.e. curator ingest)
are stated in the owner's docstring and card. No store, daemon, invalidation or caller signature was
added.

- The owner's rule: answers only, keyed by complete ids, availability never remembered, and the two residuals. [16]
- The memo module's tables and admission test. [17]

## 260921-ICR-L44 The Anchor Resolver States The Region It Already Measured

`knowledge/read_anchors.py` now reports, beside its unchanged `detail` sentence, the line ranges an exact
recorded blob supports as structured values on `AnchorResolution.resolved_ranges`: every defining extent
for a `symbol` locator, the recorded range for a `line_range` locator **only when the blob holds those
lines**, and none for a `file` locator. A recorded range past the blob's end keeps `exact_recorded_blob`
— the blob-identity fact attribution and diff accounting act on — carries no range, and says why in
`detail`. The resolver still never re-anchors, searches or clips a recorded range and still publishes no
bytes; it reads the exact blob's lines only to measure a symbol's extents or a range's bounds.

- The bound-checked line-range observation. [18]
- The symbol observation carrying every defining extent. [19]

## Curator candidate source continuity

Leaf curation captures the exact working source through curator_candidate_source. candidate_progression is the explicit operation that advances only a draft candidate code tree after matching the predecessor receipt and logical dataset under the existing lock. Normal candidate opening remains strict; knowledge, allocation state and the original before half do not move with this operation. Receipt-to-resolution conversion is shared by first-generation establishment and progression.

## 260921-ICR-L4 The Partition Gets Its Own Module, The Observation Gets Its Own, And The Display Keeps The Seam

This route gained **two modules** and the leaf they belong to (`260921-ICR-L4`, primary requirement
ICR-R04@v1) corrects the attribution accounting: the measured change population is partitioned once
into attributed, confirmed unregistered and undetermined, at the declared changed-path granularity.
The per-file detail lives in the three sidecars; what belongs at this route's altitude is the split
and the rule that keeps the two halves from disagreeing.

- **The arithmetic is pure and the acquisition is elsewhere.** `memory/knowledge/diff_attribution.py`
  owns `partition_attribution` (measured denominator, resolved-attribution, licensed absence, subject
  link), `unavailable_attribution`, and the one licensing table with its one predicate
  `licenses_absence` — read twice, by the partition for the confirmed-unregistered bucket and by the
  acquisition owner for `subject_scope_complete`, so the two questions cannot disagree.
- **The observation is shared, not owned by any reader.** `memory/knowledge/tree_observation.py`
  owns `TreeSide`, `TreeChange`, `TreePaths` (with the two construction rules that keep paths and
  entries one measurement and unrepresentable implying partial), the `TreeDifferenceProbe` seam and
  `no_tree_difference_probe`.
- **The display keeps the seam and states the deletion.** `memory/knowledge/diff_display.py`
  (523 → 508 lines) re-exports every moved name so no importer changed, carries the partition onto
  the expansion through one `SourceObservation`, and says in its own docstring that
  `attributed_paths(comparison)` left and is deliberately not replaced — an unchanged mapped path is
  context and never a change, and what replaces the name is `SourceAttribution.attributed_paths`.

- **The partition arithmetic and its four rules, with the one predicate behind both the bucket and the exclusive-outside label.** [20]
- **The shared observation vocabulary and its two construction rules.** [21]
- **The display seam: one observation, the carried partition, the two established omissions, and the deliberate non-replacement.** [22]

## Route Impact: The Durable Root Gets One Exported Definition (260921-ICR-L11)

`memory/knowledge/durable_evidence.py` gained **one function and no behavior change**:
`durable_reports_root(task_root)` returns `<task_root>/notes/reports`, the durable directory this module
already fixed as `_TASK_RELATIVE_REPORTS`. It is exported because the destination is a **decision**
rather than a convenience — the enclosure root and `<worktree_group>/` are both removed by cleanup, so a
second module that spelled the path for itself would be a second place where "durable" could drift away
from the one that is.

The route-level fact worth carrying is the split the export creates: **the single-file publication stays
the route for one artifact** (`publish_durable_evidence`, with its one-plain-file-name rule), while a
producer whose evidence is a **directory** of related files roots that directory here. Its first consumer
is the durable comparison generation, whose whole layout —
`<task_root>/notes/reports/comparison-generations/<leaf>/<generation-id>` — derives from this function
rather than restating the path.

- **The exported root, and the shipped value it returns.** [23]
- The single-file publication the export deliberately does not replace. [24]
- **Its first consumer, which derives the whole generation layout from it.** [25]
- The per-file detail for the module that gained the export: the durable root and the shipped value it returns. [26]
- The per-file detail for the module that gained the export. [27]

## Route Impact: Two Owners Gain An Identity Listing, And It Is A Split Rather Than A Second Reader (260921-ICR-L14)

`ICR-R14@v1` adds one read to each of two owners on this route, and both are the same shape: **the
identities of a record collection, listed without decoding anything, so a composing reader can read one
record at a time through the owner's own single-record reader.**

- `memory/knowledge/detection.py` gains `recorded_run_ids(store)` over a new `_RECORDED_RUN_IDS`
  statement — the recorded run identities in identity order, scoped to the store's namespace and
  filtered by the module's own `DETECTION_RUN_KIND`. The signals a review carries have to be addressed
  by run, and each run is then read through the shipped `read_detection_run`, which is what lets one
  damaged run be named while its siblings' signals are still supplied. An unreadable listing table
  surfaces `KnowledgeStorageError` rather than an empty tuple standing for "no runs".
- `memory/knowledge/evidence_records.py` gains `claim_ids(store)`, which runs the **existing**
  `CLAIM_IDS_OF_REPOSITORY` statement that `all_claims` already reads whole. `all_claims` is unchanged,
  so the listing and the all-or-nothing read cannot come to disagree about which identities exist; the
  split is what makes a per-record guard possible without a second reader of the same tables.

Both owners keep every existing reader, writer, refusal and precondition: the additions are one
statement and one function each, and the write paths are untouched.

- **The detection owner's identity listing, decoding nothing, and the composing reader it exists for.** [28]
- **The evidence owner's identity listing beside the unchanged whole-collection read.** [29]
- **The single-record readers each listed identity is read through.** [30]
- The cases that measure the per-record isolation on both collections through the production port. [31]

## 260915-KS-L41 Membership Is Read From Its Own Table, And A Run's Inputs Become An Identity

This route owns the knowledge store's reader port implementation and the detection record module, and
this leaf changed both for the same reason: a question was being asked of a structure that could not
answer it. In `memory/knowledge/view_source.py`, **`FAMILY_MEMBERS` — the statement that reads the
dedicated `family_member` table — finally has its caller.** It is executed by
`StoreViewReader.family_member_rows()`, the one port method written for it, and `_member_row` is its one
row builder. The statement had been declared and referenced by nothing while the family view asked the
**generic envelope reader** for the record kind `family_member`; that reader answers only for
`knowledge_record`/`record_revision` kinds, membership is not duplicated into that envelope, and the
named-kind read therefore returned no rows on a dataset that holds membership. A family view built on
that empty answer reported a joint guarantee, no members, no implementation locations and
`completeWithinDeclaredScope: true` — an empty answer indistinguishable from a real absence at the call
site, which is exactly why the read is now a typed method on the port rather than a string a caller can
spell wrong. `_member_row` keeps only what was recorded: the two revision ids travel in the payload under
the names the view layer reads, and the row carries **no** `change_locus`, because which locus a
membership row belongs to is the view's classification decision and this module classifies nothing.

In `memory/knowledge/detection.py`, a recorded run's inputs are now an identity and a digest over it.
`detection_input_identity` returns one canonical JSON value — namespace and assessed namespace,
registered `governing_route_id`, the policy, extractor and condition-vocabulary versions, the declared
input sets, and per side the exact logical digest, the optional code tree and repository root, the task
reference and the selector digest and policy — and `detection_input_digest` hashes that value. Nothing is
read from the clock, the filesystem, the dataset the run happens to sit in, or the caller, so two runs
with different inputs get different digests and one run always gets the same one. The run's own `run_id`
travels inside the identity, so two executions over identical inputs still carry two digests: **the digest
stands for the execution, not only for the input pair.** That is a deliberate choice and it is recorded as
an open question the review owns rather than presented as settled — a caller wanting "the digest of these
inputs regardless of which run measured them" is asking a different question from the one this function
answers. The module still decides nothing about *which* recorded run in a scope should be reported; it
supplies the identity that lets the mounted tool let a caller name one exactly.

## What This Area Is

The route owns three distinct responsibilities, and they are deliberately not the same thing:

1. **Memory-repository lifecycle** (`baseline.py`, `carryover.py`, `carryover_authority.py`) — initializing a
   memory repository, adopting an existing onboarding tree as a first ledgered baseline, and carrying richer
   onboarding from a source branch into an open recovery leaf.
2. **Concrete knowledge storage** (`knowledge/`) — the APSW-backed SQLite candidate that holds repository,
   invariant, revision, family, anchor, membership and realization identity, and since 260915-KS-L10 also the
   `Route` scope entity and the typed record envelope. Added by 260915-KS-L1 as an experimental increment and
   extended by every leaf through 260915-KS-L10; it is a durable record store, so it ranks here with the record
   stores rather than with the application layer that admits its writes.
3. **Staged legacy migration and measurement** (`migration/`, added by 260915-KS-L21) — the scope inventory, the
   legacy-artifact parser, the explicit mapping registry, reference resolution with its three recorded states,
   the truth-coverage census's accounting and slices, and the cutover's criteria, plan and proposal. It
   **reads** the Markdown-era onboarding corpus and describes it against a frozen baseline; the only write path
   it uses is the shipped candidate batch operation, through `knowledge/census_records.py`.

The three responsibilities share a package rank and a charter paragraph, not a mechanism: nothing in the
lifecycle modules imports `knowledge/`, and nothing in `knowledge/` reads, writes or migrates Markdown onboarding.
`migration/` reads that corpus but never writes it, and it reaches the store only through the candidate batch
operation the storage package owns — it opens no transaction of its own, mints no identity of its own and
switches nothing live.

## Purpose

`memory/` is the durable-store route. Its members own the on-disk representation of two different things — a
repository's onboarding tree and an authored knowledge candidate — and both are stores that a higher-ranked
admitted authority writes through rather than authors.

## Hot Path Summary

`knowledge/candidate.py` owns the **one admitted multi-record write boundary** (`change_candidate`): one lock, one
`BEGIN IMMEDIATE`, a closed twelve-command union, and an all-or-nothing refusal. Everything else in the storage
package is composed by it or called through it. `knowledge/batch_preconditions.py` holds every read-only
precondition (including the completed-graph lineage pass), `knowledge/batch_commands.py` is the only module that
applies a batch and the pass that re-proves the rows it left, `knowledge/candidate_records.py` is the identity
vocabulary both read, and `knowledge/merge.py` owns **the guarded common-base merge** — the package's composition of base resolution,
structural preflight, changeset production, coverage replay, aborting application, postcondition validation and
publication, in that order — with `knowledge/merge_base.py` (dataset identity, the closed base claim and its Git
ancestry adjudication), `knowledge/merge_schema.py` (the declared-structure preflight that runs before any session),
`knowledge/merge_changeset.py` (deltas, their materialised operations and the coverage replay),
`knowledge/merge_validation.py` (the result's postconditions and the inputs' integrity) and
`knowledge/merge_refusals.py` (the merge's refusal vocabulary) beneath it; `knowledge/logical.py` owns the canonical logical dataset identity.
`knowledge/store.py` owns the one insert-only single-record revision operation, the package's shared candidate lock
and its one-immediate-transaction wrapper, and the invariant half's tables; `knowledge/{families,anchors,memberships,realizations}.py`
own the four graph concepts and their tables, `knowledge/lineage.py` owns the one acyclic-lineage rule both lineage
graphs apply (including the batch's declared-edge caller), `knowledge/labels.py` owns the two label edits and their
row-digest guard, and `knowledge/endpoints.py` owns the shared relation-endpoint check; `knowledge/schema.py` owns the
declaration of generation 1's ten STRICT tables, its fifteen immutability triggers and the structural manifest and
fingerprint of a *generation record*; `knowledge/schema_generations.py` owns **which generations exist** — generation
1 pinned as data with its fingerprint constant and drift gate, generation 2 = generation 1 plus `knowledge/schema_v2.py`'s
six appended tables, generation 3 = generation 2 plus `knowledge/schema_v3.py`'s four authored-judgment tables, and
generation 4 = generation 3 plus `knowledge/schema_v4.py`'s one detection-sequence table — and the dispatch that
selects one from the dataset rather than from the running build;
`knowledge/record_envelope.py` owns the one payload-admissibility seam and the four disjoint record groups it now
registers (the internal conformance kind, the eight authored facet kinds, the two mechanical-detection kinds and
the requirement-revision kind);
`knowledge/routes.py` owns the route
confinement rule, the acyclic-hierarchy walk and the route/association write and read operations;
`knowledge/connection.py` owns the pragma contract, the one-row reader, the read-only connection every identity
confirmation uses, and the open-time schema validation; `baseline.py` / `carryover.py` / `carryover_authority.py`
own baseline adoption and branch carryover. **The snapshot half** lives in `knowledge/candidate_workspace.py`
(create, resume, clone, disposal verdict), `knowledge/candidate_receipt.py` (the sealed receipt and its binding
comparison), `knowledge/closed_snapshot.py` (the one freeze procedure both publication and cloning use, and the
shared `require_closed_database` step every producer of a finished database file closes through),
`knowledge/publication.py` (atomic, verifiable install under a destination lock, plus the public admission reading),
`knowledge/materialization.py` (the read-side publication gate), and `knowledge/logical.py`'s `dataset_identity`
entry point. **The portable half** is `knowledge/export_portable.py` (the `ar-knowledge-export/v1` format, its one
encoder and the reader that accepts only that encoder's own rendering), `knowledge/export_import.py` (the export and
import operation, its private stage and its staged sealed-aggregate verification), and
`knowledge/export_refusals.py` (the boundary's refusal vocabulary), with the artifact's header carrying the *same*
logical digest `knowledge/logical.py` defines — there is one digest definition, not two. The import
direction is enforced: no package ranked below `memory` (rank 12) may import `memory.knowledge`, and `application`
(rank 21) is its only consumer. **The read half** is `knowledge/read.py` (the requirement's finite selection policy,
executed once over one snapshot, plus whole-item paging over an already-selected scope),
`knowledge/read_queries.py` (one statement per lookup, all on the caller's connection), `knowledge/read_anchors.py`
(the anchor observation against the requested code tree) and `knowledge/read_refusals.py` (the read's refusal
vocabulary), with `knowledge/logical.py`'s public `cell_value` as the one decoder a read page and the logical
digest share. **The mechanical-detection half** is `knowledge/detection_walk.py` (the deterministic walk that
decides which recorded comparison facts match which declared condition and emits facts-only signals in the
declared total order) and `knowledge/detection.py` (the detection *record*: one run's assembly, its ordered
write, its verified read, its reproducibility and currentness answers, and the two refusals that keep a
detection write out of the assessed dataset's own measurement transaction), with `knowledge/schema_v4.py`
declaring generation 4's one appended table — the recorded order of one run's signals.

**The requirement-revision half** is `knowledge/requirements.py` (the record group's whole operation surface —
one write entry point under one lock and one immediate transaction, the read, the reference resolution, and one
guard per distinct refusal fact), `knowledge/requirement_records.py` (the row codecs and the seal-verifying
decode), `knowledge/requirement_views.py` (the four derived views as pure functions of the stored rows),
`knowledge/requirement_owner.py` (the one place this record group asks the task plane) and
`models/knowledge/requirement.py` (the frozen payload vocabulary). It **adds no table and declares no
generation**: a requirement revision is an envelope record in the shipped `knowledge_record` /
`record_revision` tables, and the record group's kind is the fourth family to register through
`record_envelope.PAYLOAD_MODELS`.

## Detailed Route Context

### 260915-KS-L1 Experimental Knowledge Storage Responsibility

This route gained a new responsibility and no new authority. The leaf added `memory/knowledge/` (six modules), its
shared vocabulary `models/knowledge/` (nine modules) and its composition seam `application/knowledge.py`, then
declared the storage home in one *wording* paragraph of `[package.memory]` in `layers.toml` — no rank, order or
sequencing entry moved, which is the narrow charter change the leaf document permits.

What the storage package does and does not own, stated once here because a reader of this route needs the
boundary before the mechanism:

- **Owns:** the versioned SQL schema (`ar-knowledge-sqlite/v1`, `SCHEMA_USER_VERSION = 1`), the row codecs, the
  connection/pragma contract, and one atomic insert-only revision operation with its typed refusals.
- **Does not own:** approval, acceptance, task status, Git resolution or commit attribution. The store
  manufactures no acceptance and exposes no update, delete or upsert path; `kernel/memory_attribution.py` remains
  the Git attribution owner and nothing from it was copied into the store.
- **Serves:** the requirement `KS-R01@v1` — a canonical invariant revision stays immutable and unambiguously
  addressable after successor revisions are added, including concurrent successors carrying the same display
  version.

The four properties and their mechanisms: opaque UUID revision identity separates identity from the friendly
display version (two successors may both display `v2`); the `payload_digest` seal covers the whole authored
aggregate including the sorted predecessor set, so a re-pointed edge fails the read-time recomputation; database
triggers — not only the operation — refuse an update to a sealed row, so a changeset, a repair script or a
forgotten code path still cannot rewrite a citation; and every table keys on `repository_id`, so a foreign
namespace refuses as `unauthorized_scope` before any DML.

### 260915-KS-L2 The Graph Half Of The Knowledge Store

This route's storage package gained its **relation half**: family identity and sealed family revisions, source
anchors, exact-revision memberships and realization claims, plus the reads that answer from both directions. Six
modules were added (`families`, `anchors`, `memberships`, `realizations`, `endpoints`, `lineage`) and four existing
ones changed. `schema.py` was **not** touched: the six tables and their indexes already existed in version 1, so
the schema generation and `schema_fingerprint()` are unchanged. The leaf also repaired two latent L1 defects
(`SourceAnchor.anchor_id` was unconstructible; `map_sqlite_error` reported the wrong operation and table for every
non-invariant caller), and those repairs are recorded in `models/knowledge/source.py.md` and
`knowledge/refusals.py.md` rather than here.

What the graph half owns, stated once because a reader of this route needs the boundary before the mechanism:

- **One canonical stored identity per authored relationship.** `family_member` and `realization_claim` are the only
  owners of the two relations. Their declared unique tuples plus the operations' pre-checks make a second row for
  the same pair a `relationship_constraint` refusal naming the stored identity; there is no second, separately
  maintained list of semantic facts anywhere in the package, and the forward and reverse reads select the same
  table with the same column list. That is why the two directions can be compared by **identity** rather than
  reconciled.
- **A relation cites revisions, not identities.** A membership relates an exact family revision to an exact
  invariant revision, so a newer family revision needs its own explicitly authored membership instead of
  inheriting one through a moving `current` pointer.
- **A graph-valid claim is still only a claim.** The realization role is a closed authored vocabulary with an
  explicit `unclassified` member and the rationale is the author's sentence; no reader infers either from the
  source. Storage and resolution are separate concerns: an anchor records the repository-relative path, the source
  identity and the locator and is written and read back without consulting a filesystem, a Git object or a parser,
  so a missing source changes what a later resolver reports and never retires a stored attribution. Resolution
  belongs to `KS-R07`.
- **Removal is explicit and never repoints.** A removal names the row digest the caller expects, so a stale caller
  is told rather than obeyed; the earlier dataset keeps the removed row, which is what makes a before/after
  comparison meaningful without an always-current pointer.
- **One rule, two graphs.** The acyclic-lineage rule left `store.py` for `knowledge/lineage.py` so the invariant
  lineage and the family lineage apply it once. The reach is deliberately wider than adjacency: a candidate is
  refused when it would be on a cycle **or** when a retained revision reachable from it is already on one, and the
  refusal names which branch applied.

**Disclosed limitation — read this before treating the family identity row like the invariant one.** The `family`
identity table carries **no** immutability trigger, while `invariant` carries both a no-rebind and a no-delete
trigger. `UPDATE family SET display_label …`, `UPDATE family SET label_provenance …` and `DELETE FROM family` on a
row no `family_revision` references are therefore **permitted by the database**; the only protections are the
deferred foreign key from `family_revision` (which protects a family that has revisions) and the operation-level
label check. This matches the v1 design, whose trigger requirement covers revision rows and relation payloads only,
and `KS-R02@v1` forbids none of it — so it is recorded as a **disclosure and a `v2` decision**, not as a v1 defect.
Adding the two triggers changes `schema_fingerprint()`, which the `KS-R05` merge preflight compares, so it needs
the declared `ar-knowledge-sqlite/v2` route and belongs to the owning seat. The same reasoning records that an
anchor's, membership's and claim's **identity** columns are not covered by their payload-only triggers; a repointed
`repository_id` is caught only by the deferred foreign key at `COMMIT`.

All ten canonical tables are now reachable through operations. The six the graph half added are written by the
graph modules rather than by `store.py`, which still writes only `repository`, `invariant`, `invariant_revision`
and `invariant_predecessor`. The eager declaration of the whole schema in version 1 remains deliberate: a SQLite
session changeset can only carry operations for tables both sides already have, and a table present on one side
only is exactly the schema mismatch the merge preflight must refuse. Later leaves extend behaviour inside a stable
schema instead of migrating it.

The lineage rule is the one place where the code states a contract twice on purpose, because it lives in one module
and is applied by two. `store.create_revision` refuses as `lineage_cycle` when inserting the candidate would leave
**any** revision in the invariant's lineage graph on a cycle — the candidate itself, or a retained revision
reachable from it through predecessors — and `families.create_family_revision` applies the same rule over
`family_predecessor`. The guard is evaluated over the post-insert graph and before any row is written. A revision
that merely descends from a stored cycle is therefore refused even though its own lineage is acyclic, and the
refusal says so rather than claiming self-reachability.

### 260915-KS-L3 The One Typed Write Boundary

This route gained the substrate's **single mutation entry point** and no new authority. Six modules were added
(`knowledge/{candidate,candidate_records,batch_preconditions,batch_commands,labels,logical}.py`) and seven changed
(`knowledge/{store,anchors,families,memberships,realizations,lineage,refusals}.py`); `schema.py` was **not**
touched, so the schema stays `ar-knowledge-sqlite/v1`, `PRAGMA user_version = 1`, ten tables, fifteen triggers and
the same `schema_fingerprint()`.

What the batch boundary owns, stated once because a reader of this route needs the boundary before the mechanism:

- **One lock, one transaction, one writer.** `change_candidate` takes the candidate's exclusive lock, opens one
  `BEGIN IMMEDIATE`, and composes the per-concept helpers the single-record operations already use. Those helpers
  are published and assume the caller holds the lock and the transaction — that is what makes a multi-command batch
  possible without nesting a second transaction, and nothing enforces it (the disclosed exposure).
- **All-or-nothing is a measured property, not a promise.** A refusal returns `after == before` and the transaction
  has rolled back; the evidence is a node that fails when the rollback is mutated to a commit, plus refusal cases
  that measure table counts and the logical digest through a separately opened store.
- **Validation is over the completed graph.** A revision may declare a predecessor any command in the same batch
  creates, wherever it sits in the sequence; `lineage.declared_cycle` judges the batch's own declarations through the
  shared rule (`extra_predecessors` is supplied only there), and an intra-batch cycle is refused by name before any
  row exists. The after-integrity pass re-proves both stored graphs.
- **The lane boundary fails closed.** `baseline` is refused by name (`target_not_candidate`) before the lock, and
  `task-candidate` refuses `unauthorized_scope` until a resolved, owner-validated task binding can be required and
  checked — this increment writes **only** `draft-candidate`, and the packet's task-authority sentence is satisfied
  by refusing rather than by trusting a caller's reference.
- **The dataset identity is resolved, never asserted.** `application/knowledge.py` reads it from the live candidate
  and seals it into the context; the operation re-derives the seal and compares the logical digest inside its own
  transaction. A stale batch is refused with both digests named and is never silently rebased.
- **The receipt is factual and closed.** `MutationResult` reports before/after identities and the rows the batch
  wrote or removed, with `state` exactly `written | removed`; a removal is reported with the digest the row had, and
  a command whose effect was already stored contributes no entry. There is no field a semantic verdict could occupy.

**Two carried limitations belong in this account rather than being rediscovered.** The refusal *code* `no_change`
still has no producer — only the *result state* `MutationResult.state == "no_change"` is reachable, and a consumer
must not branch on the code. And `application/knowledge.py` still has **no non-test importer in `mcp/src`**: the
batch boundary exists inside the seam, but the seam is wired to no tool or entry point, which is what the packet
means by "public MCP names and transport wiring are later extensions".

### 260915-KS-L4 The Candidate Lifecycle And Snapshot Publication

This route gained the **snapshot half** and no new authority: six new modules
(`knowledge/{candidate_workspace,candidate_receipt,closed_snapshot,publication,materialization}.py` plus the
second composition seam in `application/knowledge_snapshot.py`), with `connection.py`, `store.py`, `logical.py`
and `refusals.py` changing and `schema.py` **not** touched — the schema stays `ar-knowledge-sqlite/v1`,
`PRAGMA user_version = 1`, ten tables, fifteen triggers and the same `schema_fingerprint()`.

What the snapshot half owns, stated once because a reader of this route needs the boundary before the mechanism:

- **A candidate is a local working object, and its identity is read rather than asserted.** The directory holds one
  writable database plus the sealed receipt that binds it to its admission; the receipt deliberately carries **no**
  dataset digest, so a caller cannot hand-write the identity its publication will be compared against. Creation is
  two-phase (build and verify privately, then expose the complete directory), an occupied destination is refused
  as a resume attempt, and a clone comes from a *closed* representation produced by the same freeze publication
  uses — never from a WAL-dependent main file.
- **A published snapshot is closed, and closedness is proven.** The freeze pins a read view, copies through
  SQLite's own backup so a committed-but-WAL-resident batch is included and an uncommitted writer's rows are not,
  establishes the `delete` journal mode on a fresh connection to the finished copy (a backup destination *inherits*
  the source's mode), reopens it read-only to prove no peer and the pinned dataset, and flushes the file's own data
  before anything renames it.
- **Publication is replace-or-nothing, against an admitted identity.** The destination lock is a hidden `flock`
  resource beside the file it protects, and an identical logical dataset returns `no_change` with the existing
  bytes retained — page layout is not knowledge, and rewriting would dirty a memory tree for nothing observable.
- **A read gates on the comparison and never resolves it.** `materialization.publication_state` reports
  `current` or `candidate_snapshot_unpublished` with both identities and leaves the decision to the caller; no read
  publishes rows or attaches them to an older memory tree.
- **Disposal is a verdict, not a deletion.** A `discard` must name the identity the candidate holds *now* (so an
  authorization cannot be replayed against newer unpublished work) and a `published` disposition must point at a
  database that reopens to that same logical dataset. Removing the directory stays with the enclosure owner.

**The durability correction this leaf carried is the reason two long-standing cards changed.** `store.close()` no
longer unlinks WAL/SHM peers, and `connection.discard_closed_wal_peers` now states a caller precondition instead of
a close-time rule: the unlink could not know whether another connection held the database, a reader holding a read
transaction blocks the checkpoint that would have made it safe, and an unconditional call destroyed a committed
batch. SQLite removes its own peers on the last clean close, so the call was removed rather than made conditional.
`connection` also gained `open_read_only_database` (the connection every identity confirmation uses, so a check
cannot repair what it checks) and `journal_mode`.

**Two carried limitations and one disclosure belong here rather than being rediscovered.** `application/
knowledge_snapshot.py` — like `application/knowledge.py` — has **no non-test importer in `mcp/src`**: the lifecycle
and publication exist inside the seam, with no tool wired to them. `authorization_ref` on a disposal is **carried
but never examined**, because permissibility is this layer's question and the approval chain is the caller's.
And the `kernel/atomic_write.py` directory fsync runs **after** `os.replace`, so a post-rename failure is reported
as a replace failure — which is why a create can answer `destination_occupied` for the destination holding the
complete candidate it just created, and why a publication can return `publication_failed` where
`publication_durability_unconfirmed` would be the honest code. The non-claim narrows again: the still-unclaimed
behaviour is now **L6–L8** (portable roundtrip, selective read and candidate diff): the Git-side merging half
is delivered by the L5 section below.

### 260915-KS-L5 The Guarded Common-Base Merge

This route gained the **merge half** and still no new authority: six new modules
(`knowledge/{merge,merge_base,merge_schema,merge_changeset,merge_validation,merge_refusals}.py`), the third
composition seam in `application/knowledge_merge.py`, and **no change to `schema.py`** — the schema stays
`ar-knowledge-sqlite/v1`, `PRAGMA user_version = 1`, ten tables, fifteen triggers and the same
`schema_fingerprint()`. This is the route's largest increment so far and it is deliberately built as a sequence in
which each step exists because the step before it cannot see what it prevents:

- **The base is proven, never chosen.** A merge is defined by its base, and the failure this route refuses is the
  quiet one: picking *some* commit (an arbitrary `git merge-base` result, or `HEAD` as a stand-in) and producing a
  delta against a base neither side descends from. The claim is a closed two-member union — a caller-supplied
  commit, or a claim the ancestry evidence must confirm as the **unique** common base — and zero bases, several
  bases, or one base that is not the claimed commit all refuse. Nothing here reads a Git object to decide what a
  dataset *is*: the datasets are identified by their own logical digest.
- **The declared structure is checked before a session exists.** SQLite's changeset application can silently skip a
  table it cannot match, so an input that is not this schema generation would produce a green merge over a dropped
  change set. Each input is compared against the one declared manifest (derived from the DDL that creates a
  database rather than from a second description of it), and an input carrying a table outside the manifest is
  refused rather than merged around. There is exactly one comparison per input and no pairwise pass: every accepted
  input is identical to that one declaration, so a second pass could only fire for an input the first had already
  refused.
- **A delta is a changeset, never a patchset, and its coverage is proven by replay.** A patchset carries only the
  new values, so applying it cannot detect that the target row moved; the session is asked for `changeset()` and
  never for `patchset()`, every operation is materialised before the cursor advances, and each delta is replayed
  into a fresh copy of the base, where it must reproduce its side's whole logical dataset. That replay is the only
  place an omitted table is observable: the application reports success either way.
- **Application aborts whole.** `flags=0`, no filter, and a conflict callback that returns
  `SQLITE_CHANGESET_ABORT` unconditionally: the first blocking conflict rolls the whole application back rather
  than continuing with `OMIT` to collect a cosmetically complete list, and neither side is ever preferred.
- **The conflict record names the row the engine refused.** The key is copied out of the change the callback held —
  read from the operation's **old** values, because a changeset omits the columns an operation does not change and
  an `UPDATE`'s key columns are unchanged, so its new side carries the not-supplied marker where the key is — and
  it is never reconstructed from the changeset, because the first operation a changeset carries for a table is not
  necessarily the operation that conflicted. Where the engine genuinely supplies nothing (a foreign-key conflict
  hands the callback no change at all) the record says so and names no row and no count.
- **Publication is the last step and reuses the existing contract.** The merged temporary is frozen through the
  same closed-snapshot procedure the snapshot half uses, under the temporary's own resource lock, and installed
  through the same destination-admitted publication. The two locks are sequential, never nested — this route takes
  one resource lock at a time, which is why the merge never needs a second.

**The result carries no verdict, and that is the contract rather than an omission.** `structurally_merged` is the
only non-refusal state; there is no compatibility, acceptance, approval or "harmless" field, and nothing on this
path decides whether the merged knowledge is *correct*. Two collision shapes are refused even though a weaker
policy would have merged them: a same-identity independent insert on both sides is a conflict **even when the two
payloads are byte-identical** (two authored acts that happen to collide are not one act), while two newly authored
successors of one invariant are **not** a data conflict and both survive — the two shapes are measured separately
rather than lumped together.

**Three facts about this increment belong here rather than being rediscovered.** First, the adapter is
**callable rather than wired**: no Git merge driver, attribute or config is installed anywhere on this path, and
that activation is an explicit later decision. Second, two postcondition guards are recorded as
**non-experiments** — the applied-change check and the merged-candidate immutability check cannot be reached by a
black-box case under this schema, and the freeze's contribution is invisible to a case — so their policies are
exercised directly and their call-site unreachability is stated where the code is, rather than a broken mutation
being scored as a covered guard. Third, two facts about the pinned SQLite build are recorded as **facts, not
excuses**: it supplies no foreign-key conflict row identity or count, and a stale `DELETE` is a silent no-op for
which the operation claims no guard. A merge that skipped a table and reported success — the requirement's own
non-conforming example — is refused by two independent measures, and that is the class this half exists to close.

### 260915-KS-L6 The Portable Logical Artifact

This route gained the **portable half** and still no new authority: three new modules
(`knowledge/{export_portable,export_import,export_refusals}.py`), the fourth composition seam in
`application/knowledge_export.py`, and **no change to `schema.py`** — the schema stays
`ar-knowledge-sqlite/v1`, `PRAGMA user_version = 1`, ten tables, fifteen triggers and the same
`schema_fingerprint()`. Three existing storage modules changed, and each change is small and load-bearing:
`logical.py` gained the shared body constructor, `closed_snapshot.py` gained the shared closure step, and
`publication.py` exposed its admission reading.

**The guarantee this leaf makes true is the thing to read first, and the only form a consumer may rely on:**

> **Every accepted artifact is the canonical rendering of the logical content it carries.** Two artifacts
> that both validate and declare the same `logicalDigest` are therefore the same bytes, and a dataset
> restored from an accepted artifact re-encodes to that artifact byte for byte.

The artifact is a **canonical form**, not a tolerant interchange document, and acceptance is **two** checks
that are both needed for that sentence:

- **The whole-document gate.** `parse_export` re-renders the document it parsed and refuses the text unless
  it is that rendering **exactly** — the envelope's key order, the declared manifest order of the ten tables,
  each row's declared column order, compact separators, no insignificant whitespace, literal Unicode, and the
  sorted keys inside every typed JSON value. A JSON escape that spells the same character, an extra space, a
  reordered header and a reordered table are each a **different document** of one dataset and all are refused
  (`invalid_export`, `record_id == "<canonical document>"`) with a bounded statement of where the text
  diverges. **Nothing is repaired**: normalising would accept a document nobody can reproduce from the bytes
  that were handed over.
- **The header check.** Every header *declaration* must be the one this build implements **and of the type
  this build writes**. `format`, `schema` and `schemaFingerprint` are compared by equality against this
  build's strings, `logicalDigest` and `repositoryId` by an `isinstance` guard, `tables` must be a JSON
  object, and **`userVersion` is compared type-strictly** — so `1.0` and `true`, which Python's `==` calls
  equal to `1`, are refused **by name** as unsupported generations rather than silently compared equal. All
  seven envelope keys respelled with a different JSON type are refused, and each passes the whole-document
  gate, which is what proves the refusal is the header check's.

**What the digest covers, and what the document form covers instead** — a consumer comparing a hash should
know which is which:

| Inside `logicalDigest` | Outside it, pinned by the document form |
| --- | --- |
| the schema fingerprint and every canonical record — all ten tables' rows, in the digest encoding's sorted-key order | the envelope's field order; the declared manifest order of the tables; each row's declared column order; the canonical spelling of every value; **and the JSON type of every header value** |

The digest excludes itself by design, and it does **not** cover the header's types; the reader does. Two
artifacts can share a digest while differing on those axes, and the reader refuses every such artifact —
which is exactly why a byte or content-hash comparison across **accepted** artifacts is sound.
`logical_digest` remains the primary contract and is what to compare when in doubt;
`artifact_digest(text)` is the sha256 of the artifact's exact UTF-8 bytes and is now a function of the
dataset. **A foreign producer must write the canonical form, header types included**; a later leaf that
needs to accept other spellings needs a **new format member with its own reader**, never a tolerant read of
`ar-knowledge-export/v1`.

**The import never patches a live destination, and it proves its stage before publishing.** The artifact is
validated completely *before* any database exists (document shape, manifest, canonical gate, header, declared
column order and types, primary-key uniqueness, namespace binding, recomputed seal); the destination is
admitted before any staging work, as a **closed two-mode choice** (`expected_destination=None` means "expected
absent", so an occupied destination is `destination_occupied`; an explicit identity means "expect exactly
this", so an absent one is `destination_stale`) with no third mode; the stage is a **private** database built
elsewhere, loaded in one transaction with deferred foreign keys, and verified there — foreign-key read,
**every retained revision's `payload_digest` re-derived through the shared decoders**, typed aggregates read
back, the whole logical digest recomputed, and the closure proved through the same
`require_closed_database` the freeze uses. Only then does `publish_prepared_snapshot` install it on exact
digest equality, retaining the existing bytes when they already hold that knowledge.

**One digest definition, not two.** `logical_body_from_tables` / `logical_digest_of_tables` are now the one
body constructor, and the export path seals a table mapping it *decoded from an artifact* through them —
the same value `logical_digest` / `dataset_identity` returns for a dataset, which is what makes the artifact
restorable at all. A second assembly of `body_version`/`schema`/`user_version`/`schema_fingerprint` would
have been a second digest definition, and a difference between the two would produce an export that cannot be
re-imported.

**Four facts about this increment belong here rather than being rediscovered.** First, the encoder has **no
filesystem side effect**: `ExportResult.artifact` is text, and a caller that wants it on disk writes it
through the repository's own atomic write. Second, the import creates **no Git commit and restores no Git
ancestry** — a database-only artifact reconstructs the dataset, not the memory-commit history — and importing
a row whose `state_at_origin` says `accepted` imports that *value* and grants the receiving context no
authority. Third, the destination directory holds the published database **and** L4's `.lock` resource, and
whether a memory-tree capture enumerates files or the directory is L4's open question Q1, carried forward
rather than answered here. Fourth, two staged checks are recorded as **documented non-experiments** rather
than coverage: the staged digest equality cannot be falsified by a black-box case (the rows loaded are the
rows validation already proved produce that digest), and `_binding`'s scalar guard is unreachable behind the
row reader. One guard the leaf does **not** claim is the header's namespace-binding check
(`export_portable.py:911`): reachable and verdict-changing, with no killing node — reported as an observation
for **L9**.

### 260915-KS-L7 The Selective Recorded-Scope Read

This route gained **the read half** and still no new authority: four new modules
(`knowledge/{read,read_queries,read_anchors,read_refusals}.py`), the fifth composition seam in
`application/knowledge_read.py`, and **no change to `schema.py`** — the schema stays
`ar-knowledge-sqlite/v1`, `PRAGMA user_version = 1`, ten tables, fifteen triggers and the same
`schema_fingerprint()`. Two existing storage modules changed, and each change is small and load-bearing:
`logical.py` gained the public `cell_value` (the one decoder a read page and the digest share), and
`base.py` gained `require_plain_git_path` (the one Git-pathspec rule both typed path boundaries apply).

**The selection policy is the requirement's own table, and its stopping rule is the load-bearing design
fact: the containing-family set is frozen *before* membership expansion.** Reading `P`, `I1` or exact `F`
in the packet's `P → I1`, `F → {I1, J1}`, `G → {J1, K1}` graph returns I1's and J1's realizations,
**advertises** J1's `G` membership, and **excludes K1** until `G` is selected explicitly in a subsequent
expansion. The frontier is `memberships_of(I) − F0`, advertised and never traversed — a sibling's
membership in another family is a recorded fact the caller can act on, not permission for this read to walk
that family.

**Three properties a consumer may rely on, each enforced at model construction rather than by discipline:**

- **A page's counts describe the declared selected set, not the remaining tail.** `primary_items_total` is
  the same number on every page of the walk, `primary_items_returned` is the walk's cumulative figure, and
  the slice size is `len(page.items)`. The three satisfy `returned + remaining == total` **at every
  position**, and `KnowledgeReadCounts` refuses its own arithmetic contradiction. Round 1 of this leaf's
  review sealed this as a defect: restating the total as the tail makes page 2 of a 17-item walk report 16
  and the last page 1 — the requirement's own non-conforming example, *"a one-item page implies that the
  invariant has only one implementation"*.
- **A truncated page can never be presentable as a complete family.** `KnowledgeReadPage` refuses to exist
  with `has_more == enumeration_complete`, or with `has_more` disagreeing with the presence of a
  continuation.
- **Nothing in the response can be read as a verdict or a current pointer.** Every statement, role,
  rationale and lifecycle crosses as the authored text it is stored as; the models have **no field** that
  could hold a "current", "accepted", "severity" or "ranked" marker, which is how the requirement's
  *Forbidden Overreach* is enforced structurally. An identity seed returns every retained revision grouped
  by identity, and a display version selects nothing.

**The path-refusal contract is the one review corrected most sharply, and the correction is the interesting
part — a refusal must describe the actual cause.** Git pathspec **magic** is the leading-`:` family
(`:(exclude)`, `:!`, `:(top)`, `:/`) plus `..`, absolute paths, `~`, drive/UNC spellings, backslashes and
NUL; the glob characters `*`, `?` and `[` are **literal characters** to `ls-tree` (measured on
`git 2.54.0`), so a legitimate anchor containing them must be authorable, seedable and resolvable. Round 1
refused them, which made such an anchor un-authorable and reported a file the tree really holds as
`path_absent` — *a false statement about the repository rather than a refusal of a malformed spelling*. The
read path therefore distinguishes **three genuinely different facts**, and a caller must never be told a
path is absent when the real reason is its spelling:

| Outcome | The fact |
| --- | --- |
| `path_absent` | Git answered, and the requested tree holds nothing at that path |
| `unsupported_locator` | the spelling is not addressable, so the tree was never asked; the cause is in `detail` |
| `recorded_object_unavailable` | the lookup did not answer: the tree is absent, or Git ran and failed, or Git could not be run at all |

The same rule was applied to the leaf's other refusal sites — `registration_absent` fires only for a path
with no recorded claim, `selector_absent` only for an identity the snapshot does not hold, and each
`snapshot_unavailable` variant names the comparison that fired.

**Two honest limits belong here rather than in a footnote.** `_tree_entry`'s **non-zero-exit** branch is
reachable by no input on this host and is an **explicitly disclosed unasserted defensive branch** (L9 ledger
**A6**); a published claim that a mutation made it reachable was **withdrawn** by the leaf's own evidence
erratum, because the kill that appeared to prove it also appears with the production line untouched — so it
must never be read as coverage. And `_manifest_digest`'s inclusion of each item's `selection_reasons` is a
**reachable covered gap** with no killing node (L9 ledger **A4**).

**Where the read is addressed and what it never does.** The context names one namespace, one exact logical
snapshot and optionally one exact code tree; all three are verified against the file that was actually
opened, through three separate comparisons where the schema generation is its own statement rather than a
corollary of the digest. `task_ref=None` is a **supported** baseline state — a read during planning needs no
leaf, no enclosure and no fabricated task. The connection is opened **read-only**, so "a refused read
persisted nothing" is a property of the handle rather than a rollback, and the evidence measures it. A
continuation is a **binding**, not a position: snapshot, context, selector, policy and schema are checked
before the file is opened and the manifest and position after the selection exists, and a cursor that binds
something else is refused with **no partial page**. Nothing on this path writes, falls back to a working
tree, to `HEAD` or to Markdown, resolves a symbol locator, or attaches a semantic verdict.

**The leaf's own population and its forward constraint.** 46 leaf cases (21 unit + 25 integration), across
three test modules whose shared fixture is registered as the governed artifact `knowledge-read-scope-cases`
— **L8 must split the unit module before adding cases**, because it sits at 1 163 of the 1 200-line limit.
**L8 paid that constraint rather than waiving it** (see the L8 section below): it added two new modules of
its own and no case to this one, so the read unit module is unchanged.

### 260915-KS-L8 The Baseline-To-Candidate Comparison, And The One Extension To The Read Policy

This route gained **the comparison half** and still no new authority: two new modules
(`knowledge/{diff,diff_display}.py`), the sixth composition seam in `application/knowledge_diff.py`, the
comparison vocabulary in `models/knowledge/diff.py`, and **no change to `schema.py`** — the schema stays
`ar-knowledge-sqlite/v1`, `PRAGMA user_version = 1`, ten tables, fifteen triggers and the same
`schema_fingerprint()`. Two existing storage modules changed, both additively: `read.py` gained
`SelectionQuery.seed_override` (one field, one derived property, and the single seed read the policy uses
— §"the one extension" below), and `read_queries.py` gained five readers (four existence probes and the
predecessor-edge union).

**The comparison's single claim, and everything that follows from it: a comparison is the union of two
independently selected sets, with each item retaining the snapshot it came from.** The selection on each
side is `KS-R07`'s policy, run by its owner on that side's own read-only connection; this half is handed
two already-selected sets and never re-decides relevance. Four consequences are the contract:

- **A relationship only the baseline reached stays in the union**, because the union is built from the
  two selected sets and never from a walk of the candidate. That is why deleting a realization link on
  the candidate cannot make the baseline's code disappear — the requirement's own non-conforming example.
- **A record one snapshot holds and the other side's selection did not reach is
  `present_outside_selection`** — a fact about the selection, reported with the path that reaches it —
  while a record the other snapshot does not hold at all is `absent_from_snapshot`. **Conflating the two
  is the design's own named misreading.**
- **Record changes and source changes are two separate collections.** A **statement-only** change still
  returns the attributed code on both sides; a **source-only** change is reported as a changed source
  observation and **cannot** be rendered as a changed obligation, because no record field changed.
- **No mechanically generated no-consequence judgment exists, by construction** — no field, code path or
  default can emit an invented *strengthening*, *harmlessness* or neutrality verdict. Missing attribution
  remains an advertised **gap** (the unattributed changed paths are listed and counted with their reason)
  rather than being resolved to "no impact".

**The coverage decision is three rules, and the reason is measured rather than argued.** Rule 1 (*did the
other side select another exact revision of this identity?*) is **load-bearing alone** — removing it turns
a missing selection into a real absence. Rule 2 (*do the other side's authored predecessor edges name this
revision?*) **cannot decide a state its neighbours do not**, because an authored edge is a foreign key into
the snapshot that declares it, so it is kept as a **cheap short-circuit over already-loaded lineage**; its
invariant half is asserted through the published read surface and its **family half is unexercised**,
because the fixture authors 0 family edges — a stated gap and not coverage. Rule 3 (*do the other
snapshot's own tables hold this record, by this item's own key?*) is load-bearing in the direction that
**forces its answer present**: forcing it present turns a genuinely deleted realization into a missing
selection (two kills), while forcing it absent changes no asserted state on this population (all 28 nodes
survive). **Collapsing the three into one is wrong because it turns a missing selection into a real
absence** — the reverse of what this leaf first claimed, and the correction is what its source comment now
says.

**The one extension to the read policy, recorded here so it is not re-opened.**
`SelectionQuery.seed_override` exists so that a comparison does **not** need a second selection rule: a
comparison runs R07's policy twice, once per snapshot, and the two sides may address *different exact
revisions of one identity*. `select_recorded_scope` still reads its seed **once** (`read.py:205`), every
later step is computed from that one local, no diff-shaped branch entered the policy owner, and the only
production construction site is the comparison's own `_select_side`. The independent reviewer attacked
the packet's *"R07's policy is the ONLY policy owner"* clause head-on and **could not falsify it**: a
per-side exact-revision address is a **parameterisation of R07's one rule, not a second relevance rule**,
and the override is load-bearing (mutation `R30` kills a named node on an assertion). **The owner recorded
the acceptance.**

**Two honest limits belong here rather than in a footnote.** The comparison's mutation taxonomy leaves
**three covered gaps** on its own lines (`M4` — a same-id pair with differing projected fields; `M8` —
the existence probe's line is reachable, called 3 times, but only its *differing* answer is unobserved;
`M27` — `record_change_only` is true for 0 of 22 items) and **one non-experiment** (`M23` —
`invariant_revision_is_recorded` is called 0 times), each with the input that would close it named. And
**three equivalent mutants are disclosed as equivalences rather than counted as kills** (`M9`, `M12`,
`M21`), each with the measurement that proves the equivalence. None of these is a behavioural defect, and
**the leaf's contested evidence items are carried to `KS-R09`/`L9`** (ledger entries **A9**/**A10**) —
this route claims the comparison's *behaviour*, which five independent review rounds could not falsify,
and not the leaf's evidence prose, which is explicitly contested there.

### 260915-KS-L10 The Generation Registry, The Record Envelope, And `Route` As A Scope Axis

This route's meaning changed in a way that **supersedes** what earlier leaves recorded about the schema, so this
section states the change first and then the contradiction it retires.

**The schema stopped being a build-time singleton and became a registry of frozen, selectable generations.**
`knowledge/schema_generations.py` owns the registry. `SchemaGeneration` is a frozen record of everything one
generation must answer about itself — schema name, `user_version`, the ordered table manifest, and per table the
declared column order, the primary-key tuple and the typed-JSON column set, plus the required-SQLite-feature set,
the table DDL, the index DDL, the trigger set and the structural fingerprint. The key and typed-JSON registries are
part of the pinned structure rather than derivations from DDL: generation 1's DDL never spells `json_valid`, and a
key tuple is declared data the encoder checks *against* the column list.

**Generation 1 is pinned as data, and dispatching to it is a read of the dataset.** `GENERATION_1` delegates every
declaration to `schema.py` — which keeps them verbatim, unchanged — and takes its fingerprint from the recorded
constant `GENERATION_1_FINGERPRINT` (`bae805d6…`, measured at revision `420669c4`, the pre-refactor head).
`require_pinned_generation_1_unchanged()` recomputes that fingerprint from the recorded record and **fails rather
than warns** on drift, raising `KnowledgeSchemaPinError`; the recorded recovery is to correct the change, never to
re-pin the constant to whatever the code now computes. Generation 2 is **composed** as an explicit append —
generation 1's tables plus `schema_v2.APPENDED_TABLES` — and its fingerprint is derived from the composition rather
than recorded.

**Two key spaces, deliberately not interchangeable.** An open SQLite file declares its generation through
`PRAGMA user_version` **alone**, because the application schema name is not stored in the file (the name
`inspect_schema` reports is the *build's*), so `generation_of_database` resolves by version. A portable artifact
carries `schema` as well, so `generation_of_artifact` resolves by the **pair**, and it is **type-strict on the
version before it is a lookup**: `1 == 1.0 == True` in Python, so an equality-keyed lookup would resolve `1.0` and
`true` to generation 1, which the shipped reader deliberately refuses. Selection happens once per operation and
every later digest, manifest, key registry and table-attachment decision in that operation uses the selected
generation.

**Initialization declares; it does not select.** An empty database has no version to read, so
`create_or_validate_schema` declares the newest supported generation (`CURRENT_GENERATION`, `GENERATIONS[-1]`).
This is the only place a build's own generation decides anything, and it decides only what brand-new data
declares. Consequence a reader must not miss: **a store created by this build is generation 2**, so
new tables are reachable only through generation-2 creation, while a generation-1 file stays generation 1.

**What this leaf contradicts in the previously recorded intent.** Two statements that older leaves wrote as
current intent are now false, and they are retired here rather than left to be believed:

1. **"`SCHEMA_USER_VERSION = 2` is how a schema change happens"** (the L1 charter paragraph at *Owns*, and the
   invariant this section previously stated as *the schema is a generation, not a file*). `SCHEMA_USER_VERSION`
   keeps its shipped meaning as **generation 1's** `user_version`, because generation 1's fingerprint is computed
   from it; it is no longer the build's current version and no longer moves when the schema grows. A new schema
   shape is a **new registered generation record** (`GENERATION_2` = `ar-knowledge-sqlite/v2` / `2`), and
   `CURRENT_GENERATION` — not `SCHEMA_USER_VERSION` — is what a created store declares.
2. **"All ten tables participate, because the body is derived from `schema.CANONICAL_TABLES`"**
   (`logical.py`'s invariant). The encoder is now **parameterised over the selected generation**: the body
   projects the table mapping into *that* generation's declared order, so a generation-1 dataset still digests
   over generation 1's ten tables including the empty ones, while a generation-2 dataset digests over sixteen. The
   property that survives, and that is the point, is that **the digest is total over its own generation's
   manifest** — a table that appears or disappears within a generation is still a difference, and no digest is
   ever computed over the intersection of two generations.

**An unchanged version-1 dataset keeps its version-1 identity, exactly, and that is the acceptance test.**
Its `body_version`, its `schema`, its `user_version = 1` and the pinned generation-1 fingerprint all stay what
they were, and opening it under this build reports generation 1. **No migration or cutover operation exists**:
nothing in opening, publishing, merging, exporting or reading upgrades a dataset's generation, and the honest
answer for a version-1 candidate met by generation-2 code is "it is version 1". Generation-2 datasets are
**different datasets with different digests**, never reported as equal to or as a continuation of the
generation-1 digest of the same rows.

**Additive-only, and mechanically checkable.** Generation 2's manifest **begins with** generation 1's ten tables
in generation 1's exact order, carrying generation 1's exact declared columns, keys and typed-JSON sets; it may
only append. `schema_v2.py` therefore expresses the governing-route association as three **new join tables**
(`source_anchor_route`, `invariant_route`, `family_route`), each taking the governed entity's key as its own
primary key, rather than as a `governing_route_id` column added to a generation-1 table — appending a column would
change that table's declared column set while generation 1's record must keep declaring it. A `knowledge_record`
is new in generation 2, so *it* carries `governing_route_id` directly. **No `ALTER TABLE` appears anywhere in the
package**; the phrase occurs once in `schema_v2.py`, inside its own docstring, as the prohibition.

**The record envelope has a real payload seam, and no identity of its own.** `knowledge_record` carries `kind`,
`authority_home`, `lifecycle`, `record_schema`, an optional governing route and provenance — and **no content
address, no logical digest and no fingerprint column**, so it cannot quietly become a second identity authority.
`record_schema` names which frozen shape the revision was written against; it is not a fingerprint. The payload
lives on `record_revision` (`payload` is the typed-JSON column, `TEXT NOT NULL CHECK (json_valid(payload))`, which
is why generation 2 adds `json_functions` to its feature set), and the revision is sealed by immutable triggers.
`knowledge/record_envelope.py` is the **one** place any write path decides admissibility: `PAYLOAD_MODELS` maps the
`(kind, record_schema)` pair to exactly one frozen Pydantic model, `KIND_SCHEMAS` is derived from that registry
rather than restated, and `validate_record_payload(...)` returns the validated model or a refusal with the shipped
code **`invalid_payload`** — no row written, before/after digest unchanged. This leaf registers exactly **one
marked-internal conformance kind** (`internal_conformance` / `internal-conformance/v1`) purely to exercise the
seam; the product kinds are later leaves and are added *beside* it, not by replacing it.

**`Route` is now an operable scope axis, not a table with a constraint.** `knowledge/routes.py` owns the two rules
and the three operations. Confinement walks a nine-entry rule table and refuses the first breached form — a
non-string, a NUL, a backslash, a drive letter, a UNC form, an absolute path, a trailing separator, a spelling that
is not already normalised, and an empty/dot segment or traversal — returning an admitted path **unchanged**:
normalisation is a *comparison*, never a repair, because rewriting is how two spellings become one route while a
caller believes it authored two. Acyclicity is a `UNION`-deduplicated recursive CTE anchored on the **edge**
`(route_id, parent_route_id)`, run inside the caller's transaction after the insertions and before the commit, so a
cycle refuses the whole batch; the one-node cycle is the table's own `CHECK`. `author_route` normalises, returns an
**existing** route's id when one is already authored for that path (writing no second row), refuses an unauthored
parent, inserts, then returns the cycle refusal for the caller to roll back. `set_governing_route` accepts exactly
three governed generation-1 entities, is idempotent when the same association is re-stated, and **refuses a
different route for an already-governed row** rather than re-pointing it. `find_governing_route` returns the
governing id or `None`, and `None` is a fact rather than a default: it is never "the repository root". **Scope is
never inferred** — nothing in this package derives route membership from a name, a folder ancestry, a path prefix
or a symbol string.

**The merge preflight reads each input's generation first and refuses a disagreement before any session exists.**
`merge_schema.selected_generation` names the positional role that disagreed and carries the expected and observed
versions as facts, leaving all three inputs byte-identical; it does not pick a winner, migrate an input or proceed.
The silent failure this closes is shipped and documented: changeset application carries no operation for a table it
never attached, so a table present on only one side is a change set that vanishes while SQLite returns success.
When the inputs *do* agree, **that agreed generation is the operation's selected generation**, and the structural
comparison and the session's table attachment both use it — so **a v1/v1/v1 merge on this generation-2 build still
attaches generation 1's ten tables and is byte-comparable to its pre-refactor result**, which is a required passing
case rather than a conservative default. Nothing here activates or widens a production merge driver; this is input
validation on the existing application-callable path.

**What remains deliberately unbuilt, recorded so it is not assumed.** No migration or cutover operation; no
production merge driver; no product record kinds; no second storage engine or binding. And one honest gap this
route carries: requirement 4.2's confinement rule names "no escaping symlink at resolution", and the module
docstring repeats it, but `normalize_route_path` refuses only the **lexical** forms and performs no symlink
resolution. A reader must not assume the code checks that clause.

### 260915-KS-L11 Generation 3, The Facet Write Path, And The Facet-Specific Selection

This route's storage package gained **generation 3** — the authored-judgment facet tables — plus the write
path, the row codecs and a selection of their own, and its meaning changed in one place that earlier
sections describe the other way round, so this section states the change first.

**The facet record kind does not live on the envelope alone; it is a sub-route of the write boundary.**
`knowledge/facets.py` owns **six authored acts**, each with the shipped pair of entry points: the operation
(`add_facet`, `attach_facet`, `remove_facet_attachment`, `author_explanation`, `add_explanation_revision`,
`designate_explanation`), which owns the candidate lock and one `BEGIN IMMEDIATE` transaction, and the
in-transaction step (`apply_facet_command` dispatching through `_STEPS`), which raises `KnowledgeRefused`
so the batch path rolls the whole batch back. The batch union in `models/knowledge/candidate.py` widened
from **twelve** command kinds to **eighteen**, and the shipped twelve keep their exact kinds.

**Four rules shape that write path, and each is a place a later edit could silently undo a guarantee:**

1. **The payload seam is the only payload decision point.** `record_envelope.validate_facet_payload`
   resolves the `(kind, record_schema)` pair, so an unknown or ninth subtype, an undeclared field, a missing
   meaning and a payload carrying its own `actor_ref` are all the same shipped **`invalid_payload`**
   refusal, raised before any row exists.
2. **Provenance comes from the admission, and `authority_home` from the namespace.** Neither is a field of a
   command, so no part of a submitted payload can become the record's author, authorization or instant.
3. **A facet is authored as proposed origin data.** `require_proposed_origin` refuses an accepted origin at
   **both** entry points with the shipped **`promotion_not_supported`**; the accepted-origin consistency
   rule is inherited from the vocabulary base rather than re-implemented.
4. **Every reference is checked before the row it belongs to.** A facet revision, a typed endpoint, an exact
   statement revision of the subject's own kind, a stored **decision** revision for a supersession, a
   revision of *this* explanation for a designation, and a named governing route are all verified first; a
   dangling reference is refused rather than stored and is never inferred from a name, a path or prose.

**Generation 3 appends four tables and retypes nothing.** `knowledge/schema_v3.py` declares
`facet_attachment`, `facet_decision_supersession`, `explanation` and `explanation_revision` in that
serialization order, with eleven indexes and seven triggers, and `GENERATION_3` composes them onto
generation 2 exactly as generation 2 composes onto generation 1 — so
`GENERATION_3.tables[: len(GENERATION_2.tables)] == GENERATION_2.tables` and generation 3's columns for
each of the first sixteen names are generation 2's. Three shapes are worth naming because they are how the
requirements are enforced structurally rather than by discipline:

- **Endpoint-kind compatibility is a checked foreign-key group per kind**, not a polymorphic
  `(facet_revision_id, endpoint_kind, endpoint_id)` triple: the forbidden shape has **no `endpoint_id`
  column to land in**, and a `CHECK` requires the populated group to match the stored kind.
- **An explanation's subject is the three-column `(repository_id, identity, revision_id)` reference** both
  revision tables already declare a `UNIQUE` key for, so "this revision really is a revision of the
  statement identity it claims" is a constraint of the table rather than a check the write path remembers.
- **`explanation.current_revision_id` is the one mutable field of that row**, and the
  `explanation_no_rebind` trigger names every other column — the exception is authored rather than
  inferred. Supersession adds an edge row and nothing else: the edge table refuses update and delete, so a
  superseded decision keeps its rows, its digest, its revisions and its attachments.

**Facets are reached by their own selection, not by extending `KS-R07@v1`'s.** `knowledge/facet_read.py`
declares its own seeds (a facet record, or an exact statement revision), its own item kinds and its own
declared policy `authored-judgment-facets/v1`, and it shares **no code path** with the recorded-scope read —
which is why a shipped seed's serialized page stays byte-identical, not because a guard prevents an
addition. Two properties of that selection are the contract: it is **complete or it refuses** (a selection
past its declared execution bound raises, and there is no cursor), and **nothing is derived** — an item's
order is fixed by its kind and stable identifiers, every retained revision is served as its own item, and
the only statement about which explanation revision matters is the designation the record *stores*.

**One measured divergence is recorded rather than smoothed over.** `_apply_facet_command` constructs a
`FacetWriteResult` with `state="no_change"` for an empty write, while the receipt model declares
`state: Literal["applied", "refused"]`; the mismatch is reachable only through an empty write, which the
digest-guarded designation and the pre-write reference checks make unreachable on every path this leaf's
cases drive. A later leaf that makes an empty write reachable meets a `ValidationError`, not a third state.

### 260915-KS-L14 Mechanical Detection, Generation 4, And Where A Detection Record Lives

This route's storage package gained **generation 4** and the detection *record* group, and the leaf's most
consequential decision is a **negative** one: where a detection record is written.

**A detection record is written into a store that is not the dataset it measured.** Requirement 7.1 is
enforced structurally rather than promised. The request names the databases the run assessed
(`DetectionRunRequest.assessed_database_paths`), and `record_detection_run` refuses **before any row is
written** when the detection store's own real path is one of them, with the code
`detection_self_reference` — a code only a detection write can reach, added to the shipped
`KnowledgeRefusalCode` beside the two operation names (`record_detection_run`, `read_detection_run`). The
reason is stated where the gate is: a detector whose own output moves the logical digest of the dataset it
just digested has invalidated its own signal. The gate order is scope → generation → separation →
agreement, and all four run before the store's exclusive candidate lock is taken.

**Generation 4 appends one table and retypes nothing.** `knowledge/schema_v4.py` declares
`detection_run_signal` with columns `repository_id`, `run_id`, `ordinal`, `signal_id`, the primary key
`(repository_id, run_id, ordinal)`, `UNIQUE (repository_id, run_id, signal_id)`, `CHECK (ordinal >= 0)`,
two composite foreign keys to `knowledge_record(repository_id, record_id)` and two immutability triggers,
and `GENERATION_4` composes it onto generation 3 exactly as generations 2 and 3 compose onto their
predecessors — so `GENERATION_4.tables[: len(GENERATION_3.tables)] == GENERATION_3.tables` and generation
4's columns, primary keys and typed-JSON registries for each of generation 3's twenty names are generation
3's. `ordinal` in the key plus the unique signal key together make the declared total order over signal
identity a **constraint of the table**; the two triggers are what make "never overwrites the recorded one"
hold against a later code path that forgot it as well as against this one. The generation is **read at
intake, not assumed**: the registry is ordered oldest first and `CURRENT_GENERATION = GENERATIONS[-1]`, so a
*created* store declares version 4 while an existing generation-3 dataset keeps declaring 3 and is read
through generation 3's own record.

**Why one table and not a record group.** A detection signal and a detection run are typed records the
`KS-R10@v1` envelope already holds, and their payload shapes are registered in
`knowledge/record_envelope.py`'s `PAYLOAD_MODELS` under `(detection_signal, detection-signal/v1)` and
`(detection_run, detection-run/v1)`. That makes the signal's required field set, its closed vocabularies and
its construction refusals declared **once**, in `models.knowledge.detection`, rather than restated
as SQL columns; what the envelope cannot express is the *sequence*, which is what generation 4 stores. The
envelope's registry now holds four disjoint groups — the internal conformance kind, the eight authored
facet kinds, the two detection kinds and the requirement-revision kind — and each group's derived set
(`FACET_RECORD_KINDS`, `DETECTION_RECORD_KINDS`, `REQUIREMENT_RECORD_KINDS`) is derived from the same
declarations the entries are built from rather than restated. The requirement pair goes one step further:
`REQUIREMENT_PAYLOAD_MODELS` is declared beside its payload model and merely unpacked into the registry, so
the registry cannot hold a requirement kind the vocabulary does not declare — and the fourth family was
registered the same way the third was, as a registry entry rather than as a generation column, because the
frozen payload model *is* the shape.

**One cross-store association is deliberately left unset, and nothing became optional.** A detection
record's governing route names a route in the **assessed** repository's namespace, while the record lives in
a store that is not the assessed dataset. Binding `knowledge_record.governing_route_id` would require copying
the assessed route into the detection store, and a second copy of one fact is a second authority — the thing
the design forbids for a shared knowledge view. The column is therefore written `NULL` for this record group,
with the reason recorded in the code, and the route stays a **required validated field** on the run and on
every signal, both of which fail construction without it.

**The write path and the read path are separated by protected property, not by call boundary.**
`knowledge/detection.py` owns the store's refusals, the one immediate transaction and the verified read;
`knowledge/detection_walk.py` owns the classification, holds no SQL and re-selects nothing. The walk reads
R08's recorded comparison facts and never the bytes behind them, derives each signal's identity from the
recorded group key and orders the sequence by the declared condition vocabulary; the record module writes
one `detection_run_signal` row per ordinal via `enumerate`, so the recorded order **is** the order the walk
produced. A read re-derives each stored revision's own content digest and reports a mismatch as a damaged
store rather than serving it. `compare_detection_runs` and `run_currentness` write nothing: a re-execution
that differs is reported as two distinct runs, and a moved policy version marks a run **stale** without any
signal being reinterpreted.

### 260915-KS-L17 Family Composition: One Appended Generation And One Authored Record Group
The route gained **generation 5's six appended tables** and the authored composition record group that
lives in them. Four facts are the whole of it, and each is stated because the plausible misreading is
the opposite of the truth:
- **Generation 5 is a strict append.** Six tables (`family_composition`,
  `family_composition_policy`, `family_composition_policy_version`, `family_revision_route`,
  `family_revision_context`, `family_revision_context_revision`) sit **on top of** generation 4's
  twenty-one, so a created store declares `ar-knowledge-sqlite/v5` at `user_version = 5` with **27**
  tables. Nothing redeclares, reorders, renames, retypes or drops an earlier generation's table, **no
  `ALTER TABLE` appears anywhere in the package**, and every generation is composed by the same one
  generic `_append_generation` call. `descends_from(generation, base, base.tables)` is the published
  predicate the generation case uses: the appended tables follow the base's exactly, and every one of
  the base's names keeps its exact column tuple, primary key and typed-JSON set. **A card that
  describes generation 5 as replacing or re-declaring an earlier generation is false.**
- **The declared policy defaults to off.** An edge that names no policy is stored, readable and **not
  traversable**: there is no resolution to a default, no fallback to the only version stored and no
  implicit "any declared policy". The policy is validated in **two places on purpose** — at the value
  boundary (`FamilyCompositionPolicyDraft` refuses a half-declared policy) and at the table's own
  `CHECK` constraints — so a malformed policy is unrepresentable *and* unwritable.
- **The projection reports and never traverses.** `family_view.family_revision_view` presents the
  stored links (with their direction and the policy version they were declared under), the canonical
  owning route **or** the explicit ungoverned state, and the authored explanatory context with its
  provenance. A missing link, route or context is reported **absent**; nothing is inferred from a
  label, a path, a prefix, a shared member or prose, and a revision whose members all live under one
  route's path but records no owning route is reported **ungoverned**.
- **The read-side successor is a different operation and a read, not a write.**
  `composition_traversal.follow_composition_scope` follows declared edges under one declared policy
  version, bounded by that version's declared depth bound, and reports the policy identity and version
  it executed under. It does **not** touch the retrieval selection: `KS-R07@v1`'s selected set, counts,
  ordering, revision groups, advertised frontier and manifest digest are unchanged by this leaf, no
  shipped read path consults the composition table, and the boundary suite measures that twice — by
  value and by call-site derivation. A card that implies composition edges are followed **as part of
  the retrieval selection** is false and is corrected here.
**Two SQLite subtleties this leaf found by executing the DDL, recorded because onboarding exists to
carry them:**
1. **An index may not carry a table's name.** SQLite refuses a second object under one identifier, so
   the index over the composition edge's `policy_version_id` is `family_composition_policy_version_edge`
   rather than named after the `family_composition_policy_version` table it points at.
2. **A table `UNIQUE` constraint over a nullable column does not enforce uniqueness for `NULL`s.**
   SQLite treats every `NULL` as distinct in a unique key, so a single constraint over the edge's
   nullable `policy_id` would not have stopped a second *bare* edge — the default state — from being
   stored beside the first. The declared unique tuple is therefore **two partial unique indexes**
   (`… WHERE policy_id IS NOT NULL` and `… WHERE policy_id IS NULL`), and the write path's own
   duplicate lookup refuses the state with a typed refusal before either is reached.
**One cycle rule, three graphs.** The composition graph is judged by the **shipped shared lineage
rule** — `find_cycle`, `declared_cycle`, `cycle_vertices` — at the batch's declared-graph level and at
`require_after_integrity`'s whole-graph level, fed by a third edge source
(`lineages.composition_edges`, scoped by `repository_id` alone). The ruling is that the rule applies
**uniformly**, including its branch where a candidate descends from a stored cycle, because a stored
cycle is a fact about the graph a new edge is being added to. A case asserts that **no second cycle
implementation exists** beside it.
### 260915-KS-L12 Generation 7, The Supporting-Record Write Path, And The Evidence Selection
**Generation 7** is generation 6, unchanged, plus the five tables `schema_v7.py` appends: `evidence_claim`,
its two subject join tables, `evidence_claim_coverage`, and `verification_observation`. The composition is
the same explicit append generations 2 to 6 are, so
`GENERATION_7.tables[: len(GENERATION_6.tables)] == GENERATION_6.tables` and generation 7's columns for
each inherited name *are* generation 6's. There is no `ALTER TABLE` in the module, and the leaf's
inheritance assertion is written **against the generation this leaf descends from, by name**, so a further
renumber changes two operand names and nothing else. `GENERATIONS` is now `(1, 2, 3, 4, 5, 6, 7)` and
`CURRENT_GENERATION` is its last entry rather than a second literal: a new store declares version 7 while a
generation-6 dataset keeps declaring 6 and is read through generation 6's own record.

**The number and the module's filename are the landing's, and this section states why.** `KS-R12@v1` was
built in parallel with `KS-R17@v1` and `KS-R18@v1`; all three read the registry as `(1, 2, 3, 4)` and each
registered *generation 5* on its own branch. The landing appended them in landing order —
`KS-R18@v1`'s `citation_binding` as generation 5, `KS-R17@v1`'s six composition tables as generation 6,
this leaf's five tables as generation 7 — so the module this leaf authored as `schema_v5.py` landed as
`schema_v7.py`. The renumber moved the module's name and its two composition operands and nothing else:
**a reader taking `generation 5` as this record group's number is reading a pre-sync branch state**, and
the generation-5 tables are the citation binding's.
**The three join tables are the structural half of a claim, and the table is the kind check.** The two
subject tables are one row per subject kind, each with its own foreign key onto `record_revision`, so a
claim whose subject is an invariant revision cannot reach the facet table: a misspelled kind, a dangling
identity and a wrong-kind target are unrepresentable rather than refused. The coverage table follows the
shipped attachment idiom — a stored kind with one nullable foreign-key column per kind and a `CHECK` that
the populated group matches the kind — plus `covered_identity`, `NOT NULL`, because a claim's coverage is a
*set* and SQLite does not compare `NULL`s for equality in a key.
The write path resolves every link before it writes: subject, evidence anchor and every claimed-coverage
endpoint, with an unresolved link a typed `invalid_reference` refusal and nothing written. Provenance comes
from the admission rather than the payload; accepted-origin data is refused with the shipped
`promotion_not_supported`; the generation gate refuses a dataset older than these tables and migrates
nothing. **The artifact digest is measured, not asserted**: when the caller supplies the bytes' root the
path reads the artifact, records `digest_checked_against_bytes` truthfully, and **refuses** a digest the
bytes contradict rather than storing one it observed to be false — so a stored digest is either verified or
never claimed verified. A missing artifact is recorded rather than refused, and no path re-pins a stored
digest to the bytes present now.
The evidence selection is a third selection, disjoint from the recorded-scope and facet selections by
construction rather than by a guard: it shares no policy name, calls neither, and is called by neither, so
their serialized pages stay byte-identical. One seed selects one complete aggregate or raises at the item
bound — there is no cursor and therefore no continuation contract — and the artifact resolution is computed
at read time and never written back. `read_queries.py` declares the five new tables' order columns, and
`refusals.py`'s own diff is **empty**: the three refusal factories this record group reaches live in
`evidence_refusals.py`, because the shared module sat at 1196 of the repository's 1200-line rail and the
next record-group leaf cannot extend it either.

### 260915-KS-L13 Generation 8, The Authored-Effect Write Path, And The One Table The Envelope Could Not Express
**Generation 8** is generation 7, unchanged, plus the one table `schema_v8.py` appends:
`change_set_predecessor`. The composition is the same explicit append generations 2 to 7 are, so
`GENERATION_8.tables[: len(GENERATION_7.tables)] == GENERATION_7.tables` and generation 8's columns for
each inherited name *are* generation 7's; the case asserts
`GENERATION_8.columns[table] == GENERATION_7.columns[table]` for every one of generation 7's
thirty-three names, which makes generation 8's manifest thirty-four tables. `GENERATIONS` is now
`(1, 2, 3, 4, 5, 6, 7, 8)` and `CURRENT_GENERATION` is its last entry rather than a second literal: a new
store declares version 8 while a generation-7 dataset keeps declaring 7 and is read through generation
7's own record. There is no `ALTER TABLE` in the module.

**Why one table and not a record group.** The change set, the effect claim, the preservation claim and
the unresolved question are *typed records*, and the envelope already carries them: `knowledge_record`
holds the kind, the authority home, the lifecycle and the governing route, and `record_revision` holds the
frozen payload and its content digest, so their four payload shapes register in `PAYLOAD_MODELS` under
`(invariant_effect_claim, invariant-effect-claim/v1)`, `(preservation_claim, preservation-claim/v1)`,
`(unresolved_question, unresolved-question/v1)` and `(semantic_change_set, semantic-change-set/v1)` and
none is restated as columns here. What the envelope **cannot** express is a record-to-record lineage
edge: `record_revision.predecessor_revision_id` is a revision-to-revision edge *inside* one record, and
the shipped envelope has no record-level predecessor at all. Requirement 4.8 makes the change-set
succession exactly that — the successor is a new `SemanticChangeSet` naming its exact predecessor, and
the superseded row stays addressable — so the edge is a row in its own table rather than a field on the
successor. **The schema refuses what it can, so the write path is not the only guard**: the composite
primary key `(repository_id, successor_change_set_id, predecessor_change_set_id)` stops one successor
recording the same predecessor twice, `CHECK (successor_change_set_id <> predecessor_change_set_id)`
refuses the one-node cycle in the DDL, both endpoints are foreign keys onto `knowledge_record`, and two
triggers raise `immutable_revision` on update and delete. The *longer* cycle is found by the shared
acyclic walk (`lineage.cycle_vertices`, the same scan the two predecessor graphs and the decision
supersession edge use) run inside the successor's own creation batch.

**The number and the module's filename are the landing's, and this section states why.** `KS-R13@v1` was
authored against generation 4 and renumbered to **8** at its sync, because three leaves landed
generations 5, 6 and 7 first (`KS-R18@v1`'s `citation_binding`, `KS-R17@v1`'s six composition tables,
`KS-R12@v1`'s five supporting-record tables). The module is an **append-only declaration** — the
`APPENDED_*` group with no `GENERATION_N` constant and no schema-name string of its own — so its number
lives in the composition (`GENERATION_8`, `GENERATION_8_SCHEMA_NAME = "ar-knowledge-sqlite/v8"`, the
descent from `GENERATION_7`), which made the renumber a composition edit plus a file rename from
`schema_v5.py` to `schema_v8.py`. The append's content is unchanged by it: **a reader taking
`generation 5` as this record group's number is reading a pre-sync branch state.**
**The write path resolves before it writes, and refuses by raising so the batch rolls back whole.**
`effects.py` validates the payload at the envelope seam, resolves references on the **validated** payload
— an effect claim's inputs and outputs, a member's change set, a change set's predecessors and its
candidate realization claims, all through `endpoints.py` — and then runs the duplicate scan. Assessment
references and requirement-revision references are deliberately **not** resolved: they are stored
verbatim and reported as unresolved, so no second requirement authority is created here. Two facts only
this group can state get their own factories in `effect_refusals.py`: an inadmissible declared claim
(`invalid_payload`, built from `cardinality_violation` rather than from a second copy of the predicate)
and a succession that reaches itself (`lineage_cycle`). **Nothing is derived** — no path computes,
infers, suggests, ranks or repairs an effect label from a comparison, and none converts an unchanged
file, row or revision into a preservation claim; those acts are absent from the vocabulary rather than
refused by it. Two **differently labelled** claims for one comparison are both stored, because that is
the authored disagreement the design requires to stay visible.
**The read is derived in full and carries its refusal as a state.** `read_effect_scope` returns a typed
`EffectReadResult` in the `refused` state when the dataset predates generation 8, rather than raising,
because a refused read must persist nothing; the scope itself is built by `effect_views.py` from the rows
the record group's own readers hand it, so deleting it changes no claim, no question and no change set and
a rebuild over unchanged rows is byte-identical. Membership is the **only** thing computed — read out of
each member's own stored `change_set_id` — and three *states* become readable there: an unresolved
assessment reference (no assessment record kind exists in this substrate yet, so every stored one is
unresolved by construction), an unresolved requirement-revision reference (stored verbatim under the
opaque-reference clause, never parsed), and an unresolved preservation subject (a per-kind existence
lookup, so resolution is never a guess). None of the three is refused, substituted or re-pointed, and the
views are also where the forbidden set is proven absent at the stored plane: every view is built from a
validated payload model, so a row carrying a truth verdict, a severity or a generated summary could not
have been decoded into one at all.
**One ordering rule is this record group's own.** A command that *cites* an identity the same batch also
creates must appear **after** the command that creates it — the shipped `ChangeBatch` contract, that
commands are applied in the order given — and a citation arriving first is refused as `invalid_reference`
naming the identity and the remedy, rather than left to a foreign key to report as an unnamed constraint
failure. The group contributes **no** table to `MutableRecordTable`: `EFFECT_WRITABLE_TABLES` is exactly
`knowledge_record` + `record_revision`, because the succession edge is written only as part of the
aggregate that owns it, on the same shipped rule that keeps the invariant and family predecessor rows out
of the mutable set.

## Invariants And Boundaries

- **A schema generation is data, and dispatch reads the dataset.** `knowledge/schema_generations.py` owns which
  generations exist; `GENERATION_1` is pinned with its fingerprint constant and guarded by a gate that **fails,
  never warns**; `GENERATION_2` is composed as an append. A dataset's generation is selected from what the dataset
  declares (version alone for an open file, the type-strict `(schema, userVersion)` pair for an artifact), and
  every later decision in that operation uses the selected generation. **`SCHEMA_USER_VERSION` is generation 1's
  `user_version`, not the build's current version**; `CURRENT_GENERATION` is what a *created* store declares, and
  creation is a declaration rather than a selection because an empty database has no version to read.
- **Generation 1 is immutable and additive-only.** Its ten tables keep their exact declaration order, columns,
  keys, constraints and triggers, and its recorded fingerprint never moves; a generation that would reorder,
  rename, retype, drop or weaken an earlier generation's declaration is a **schema divergence to escalate**, never
  a member of the registry and never a re-pin. **No `ALTER TABLE` against a generation-1 table exists in this
  package**, which is why the governing-route association lives in generation-2 join tables.
- **An unknown generation is refused, never migrated.** Not repaired, not re-created, and never re-read under a
  different generation to obtain a green result. No operation in this route upgrades a dataset, and an unchanged
  version-1 dataset keeps its version-1 digest byte for byte.
- **Every digest is total over its own generation's manifest.** No digest is computed over the intersection of two
  generations' tables, and no "same knowledge" verdict is returned across a generation boundary. Opening an
  existing database validates *that* generation's tables, columns and full trigger set.
- **Import direction is one-way.** `memory.knowledge` imports `kernel.canonical_json`, `kernel.file_lock` and
  `models.knowledge`; no package ranked below `memory` may import it back. A focused test guards this so a later
  reverse import fails a check rather than passing review.
- **Insert-only, one lock, one transaction.** Every mutation holds the candidate's exclusive file lock and runs
  inside one `BEGIN IMMEDIATE`; a refusal rolls back, so an expected failure never leaves a partial aggregate.
  The route operations follow the same rule: `author_route` and `set_governing_route` insert inside the caller's
  transaction and **return** their refusals rather than rolling back themselves, and the acyclicity walk is what
  makes a cycle a whole-batch rollback rather than a partial hierarchy.
- **Scope is never inferred.** Route membership, family composition and every association between records are
  authored, stored facts: a path prefix, a directory name, a symbol string or a prose mention is never a
  relationship, and a path comparison the read layer performs is a resolution fact rather than authored membership.
- **Refusals are returned values.** A caller branches on a typed code, never on message text; a storage failure
  with no contract code is reported as a defect (`KnowledgeStorageError`), not as an outcome to handle.
- **Vocabulary is defined where it decides.** Literal states, operation names, refusal codes and version strings
  live in `models.knowledge` and are imported by the decider, never defined by the decider and imported back down.
- **This is an experimental increment on the master's branch pair.** No IAS landing is implied, legacy Markdown
  remains operational authority, and the still-unclaimed behaviour is now **L9** (the foundation fix and
  certification pass) — the baseline-to-candidate comparison is claimed by this route as of `KS-R08@v1`, the
  selective recorded-scope read as of `KS-R07@v1`, the portable roundtrip as of
  `KS-R06@v1`, the Git-side merging half as of `KS-R05@v1`, and snapshot publication as of `KS-R04@v1`. The admitted batch contract *is* claimed by this route as
  of `KS-R03@v1` — one lock, one transaction, one closed command union and one resolved dataset identity — while the
  `task-candidate` lane deliberately refuses until a later leaf supplies a checkable binding. The graph half is
  claimed as of `KS-R02@v1`: families, anchors, memberships and realization claims are stored and readable from both
  directions; anchor **resolution** is claimed by this route as of `KS-R07@v1`, in
  `knowledge/read_anchors.py`, and is still deliberately absent from the write path.
- **A refusal describes the actual cause.** No path on this route reports an absence for a spelling it refused,
  and every refusal code names a distinct fact a caller acts on — the rule `KS-R07@v1` established across the read
  path and inherited by L8/L9. A boundary that refuses something must let the caller tell an absence from a
  malformed input.
- **The read half is read-only by construction.** Every statement the read issues is a `SELECT` on a connection
  opened through `open_read_only_database`; "a refused read persisted nothing" is therefore a property of the
  handle, not a rollback the code remembers.
- **A published write helper assumes the caller's lock and transaction.** The batch forced those helpers public; a
  future caller that invokes one outside a transaction would write an autocommitted row silently. Every shipped call
  site satisfies the precondition, and keeping the rule is what the one-lock/one-transaction invariant rests on.
- **A measurement never enters the transaction of what it measured.** A detection run is written into a store that
  is a different database from every assessed snapshot, and the check is the datasets' own resolved file identity
  rather than a caller's promise — so `detection_self_reference` is a structural refusal, not a documented
  convention. Nothing on this route migrates a dataset to obtain a writable target either: a dataset that predates
  generation 4 is refused with both generation numbers as facts.
- **A recorded order is a sealed fact.** `detection_run_signal` is keyed by ordinal, unique over the signal, and
  sealed by two triggers, so reordering or shortening a recorded detection sequence is refused by the database and
  not only by the operation that wrote it.

## Evidence

### Repo-Internal References

The declarations below establish the current behaviour; this inventory is not execution evidence.

**The 260915-KS-L5 merge half**, cited in the current `Finding | Anchor | Source` shape. The older rows below remain in the superseded
two-column shape and are recorded as a pre-existing repository-wide migration item in the Update History rather than converted from inside
one leaf's curation pass.

- The merge orchestration: the ordered sequence, the one-lock policy, the conflict taxonomy with the single key predicate its two lookups share, and the engine-supplied conflict key. [32]
- **The measured retraction precondition: the probe's own copy of the retained side, the measurement that runs the caller's own retraction to answer it, the call site that hands it to the conflict record, and the field the offer reads.** [33]
- The base resolution: the closed two-member claim and the two refusals a base claim can earn. [34]
- The structural preflight that runs before any session exists, and the declared manifest it compares against. [35]
- The changeset half: the directional delta build, the application whose conflict policy aborts on everything the caller did not decide, the old-side conflict key and the coverage replay. [36]
- The postcondition half, including the two call sites this leaf recorded as unreachable by a black-box case. [37]
- The merge's refusal vocabulary, one factory per observable failure point. [38]
- The two operations and twelve codes the merge added to the shared vocabulary. [39]
- The measurement the merge reports, and the merge's own third composition seam. [40]
- **The read half's selection policy: `F0` frozen before membership expansion, the advertised-and-untraversed frontier, and the declared item order.** [41]
- Whole-item paging over an already-selected scope. [42]
- **The corrected page counts: the declared total on every page, the walk's cumulative figure, and the slice size in `len(page.items)`.** [43]
- The count model that refuses its own arithmetic contradiction at construction. [44]
- **The three genuinely different facts of a path refusal, and the corrected predicate (`*`, `?`, `[` admitted; leading `:` refused).** [45]
- The read's refusal vocabulary, one factory per observable failure point. [46]
- **The one decoder a read page and the logical digest share.** [47]
- The read's path lookup, which is how a path seed selects. [48]
- The edge lookup the directly containing family set is derived from. [49]
- The read's composition seam and its three boundaries (read-only handle, task-free baseline, cursor-as-binding). [50]
- **The nodes that measure the requirement's stopping rule, the corrected counts and the three path facts.** [51]
- The shared case harness registered as `contract:common-base-merge-cases`, and its evidence node. [52]

- The governed-artifact row and the exact consumer list the L5 leaf registered in the shared catalog, which this leaf extended by two modules. [120]

**The 260915-KS-L6 portable half**, cited in the same `Finding | Anchor | Source` shape.

- **The `ar-knowledge-export/v1` format: the one encoder, the canonical-form guarantee, the two acceptance checks and the digest-coverage statement.** [54]
- The whole-document gate, its `<canonical document>` refusal identity and the bounded statement of how the text differs. [55]
- The envelope builder and the declared orders it re-imposes: columns, nested keys and the manifest. [56]
- The dataset-level checks: declared column order, declared types, primary-key uniqueness, namespace binding and the recomputed seal. [57]
- The reachable, verdict-changing namespace guard with no killing node (an observation for L9). [58]
- **The export and import operation: validation before any database work, a private stage, the closed two-mode destination admission and publication on exact digest equality.** [59]
- **The staged sealed-aggregate read: every retained revision's payload re-derived through the shared decoders before publish.** [60]
- The staged verification, including the documented non-experiment (the digest equality no black-box case can falsify). [61]
- The two-mode destination admission read before any staging, and the private stage that is never the destination. [62]
- The value-or-refusal file reader whose two failures carry different codes. [63]
- The portable boundary's refusal vocabulary, one factory per observable failure point. [64]
- **The one body constructor the export seals through, so the scan and the artifact cannot define the digest twice.** [65]
- **The shared "prove this finished file is a closed database" step the import's stage is closed through.** [66]
- The admission reading the import's destination check uses, exported from publication. [67]
- The two portable operations and the one code they added to the shared vocabulary. [68]
- The portable wire vocabulary: the request identities, the validation report and the two results. [69]
- The fourth composition seam, its five entry points and its two non-claims. [70]
- **The node the guarantee rests on: the canonical form is the only form the reader accepts, including all seven header types.** [71]
- **The node that proves an artifact whose sealed payload contradicts its digest is refused before publish.** [72]
- The node that proves the import's stage is closed before it is published, and the node that proves the freeze's closure on the published destination. [73]
- The node that proves destination admission refuses before any staging work. [74]
- The node that holds the round trip of a populated dataset to an equal logical dataset. [75]

- The registry rows this leaf added: two integration lane rows. [121]

- The registered support artifact the two integration lane rows land in, by its own artifact id. [122]

- The second registered support artifact those rows land in, by its own artifact id. [123]

- The third registered support artifact those rows land in, by its own artifact id. [124]

- The second registered support artifact those rows land in, by its own artifact id. [125]

- The third registered support artifact those rows land in, by its own artifact id. [126]

**The pre-L6 rows below remain in the superseded two-column shape** and are recorded as a pre-existing repository-wide migration item in the Update History rather than converted from inside one leaf's curation pass.

The canonical table list, column order and required feature set the store is validated against.
The declared DDL: ten STRICT tables with explicit NOT NULL keys, composite deferred FKs and the self-edge CHECK.
The fifteen immutability triggers whose names the merge preflight compares — and, by their absence, the disclosed `family` identity gap recorded above.
The structural manifest and the fingerprint over manifest plus DDL text.
The verified pragma contract, the shared one-row reader and the create-versus-validate open.
The one atomic insert-only revision operation with its ordered preconditions.
The lineage rule stated once, including its post-insert scope and before-any-write evaluation.
The shared lineage rule both graphs apply, and the family graph's application of it.
The family owner: identity, sealed revisions, family lineage and the narrow ownership read.
The anchor owner: authored locations stored as recorded, with explicit identity-plus-digest removal.
The membership owner: one exact pair, both read directions, stale-caller removal.
The realization owner: the anchored-claim transaction and both read directions over the same rows.
The shared relation-endpoint check the two relation writes both use.
The typed refusal vocabulary and the SQLite-error mapping, whose failure context now names the caller's operation and table.
The row codecs, including the read-time seal re-derivation over the stored row and its stored edges.
The composition seam that assigns provenance and is the only consumer of this storage package.
The shared knowledge vocabulary written by this store, including the graph shapes.
The kernel canonical encoder the seal and the schema fingerprint are computed through.
The branching fixture — now carrying both the identity and the graph half — the storage and graph cases build from.
The graph case support module, with its registered contract and exact consumer set.
The focused suite, registered in the unit lane, that exercises this route's storage behaviour.
The graph suites registered in the unit lane: family revision rules, relation writes, graph reads and the payload seals.
The node that isolates the sealed predecessor field on each payload, added by the fix-verification round.
---
The storage home is declared in the memory package charter as a wording addition only.
The fixture's registered stable contract, its evidence node and its five declared consumers.

### Cross-Repo References

No cross-repository authority is established by this route. The store writes one SQLite file inside the code
worktree it was opened against, and the memory-repository lifecycle can address a sibling external-memory
checkout, but neither establishes a boundary contract here.

No meaningful cross-repo references found.

- The second registered support artifact those rows land in, by its own artifact id. [127]

- The third registered support artifact those rows land in, by its own artifact id. [128]

## No Route Impact — 260915-KS-L15

No source of this route in `mcp/src/agents_remember/memory/` changed in 260915-KS-L15, and its route
model, entry points and check responsibilities are therefore unchanged. The route's reference rows
below did need re-pointing, because this leaf inserted rows into two test manifests
(`mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`) that four of those rows
cite; each re-cited row was re-derived from the current manifest while re-reading it. That is a
citation move, not a route change, and it is recorded as such rather than as new architecture.

## 260915-KS-L16 Constructing The Registered Review Scope From Recorded Links And One Declared Policy

`KS-R16@v1` §1 splits one act across two layers, and this route owns the half that *produces* the scope:
`memory/knowledge/registered_scope.py` turns a `RegisteredScopeRequest` plus a sequence of
`ScopeSnapshotSource` values into a `RegisteredScopeResult`, and reports nothing about what a detection run
over that scope could not resolve — that is `KS-R14@v1`'s half of the split, and neither half is restated in
the other's output. `CONSTRUCT_SCOPE_OPERATION` names the act for dispatch; `snapshot_source` is how a
resolved dataset is presented to it.

**The construction is deterministic in the strong sense, because every step is a declared lookup in a
declared order and every result is sorted by recorded identity** rather than by whatever order rows came
back in. Four ordered steps: the declared pair is resolved to two exact datasets, and a declaration whose
snapshot the run cannot produce is refused **by name** rather than approximated from another file; each
declared changed path is looked up by **exact equality** against the recorded anchor paths, and every hit
contributes a `source -> invariant` edge carrying the side it was read from; the invariant revisions reached
on one side contribute that side's own recorded `invariant -> family` memberships, each with its own side;
and composition edges are followed **only** from the declared seeds and the reached family revisions,
**only** when the declaration names a policy version, through `KS-R17@v1`'s own
`follow_composition_scope` — not a second walk and not a re-reading of its rule.

**Three absences are as load-bearing as the four steps.** The R07 retrieval read is never consulted: no
selection, no page cursor and no advertised expansion enters here, and the module imports nothing from that
read, so the two axes cannot be conflated by accident. Membership is never inferred from a name, a prefix, a
folder or a symbol — every member arrives through a recorded row. And an unresolvable declared input is a
refusal that **names it** (`ScopeConstructionRefusal`), never a partial scope: a scope that quietly held
less than it declared would make every later "the run examined the scope" claim false. The refusal builders
are the module's own and they reuse the **shipped** refusal codes rather than adding vocabulary, which is
why this leaf extends no `KnowledgeRefusalCode` member.

## 260915-KS-L20 The Managed Projection Writer, And The Reader Port That Decides Nothing

`KS-R20@v1` §5 turns `Doc13:269`'s eight vault-safety clauses and §1's reader requirement into the two
modules this route gains, and both are deliberately **dull where a decision could hide**. Nothing here
stores a record, mints an identity or reads the candidate tree.

**`memory/knowledge/managed_projection.py` is the `ProjectionWriter` implementation, and clause by clause
it is eight refusals rather than eight best efforts.** The manifest is the only authority on ownership:
every deletion decision is taken from it and the destination is **never enumerated**, so a file the
manifest does not list — the packet's own `user-notes/` example — is not reachable by any code path in the
module. That is also clause 7: there is no recursive clean, and there is no `rmtree` anywhere in the file.
Confinement is **resolved, not string-matched**: `resolve_inside_destination` resolves the real path of the
output's parent directory and proves it lies inside the resolved destination root, so a `..` segment, a
symlinked directory and a case-folded alias are all caught by one comparison, and a path that escapes is
`destination_escape` naming the path and the resolved root with nothing staged. Collisions are reported
**before either output is written**, with both paths and both identities: the substrate does not pick one,
does not overwrite one with the other and does not invent a disambiguating suffix. An escaping link is
never followed, for a write or for a delete; it is reported and the remaining outputs continue, so one
hostile entry does not block the rest. Publication is a **rename**: every artifact is rendered into a
staging directory inside the destination and moved into place, so an interruption leaves the prior
generation intact rather than a half-written mixture. A deletion needs **both halves** of the unchanged
test — the path in the prior manifest *and* the file on disk still matching what that manifest recorded.
And an externally edited file is reported by one of four discrepancy kinds and preserved; the only route to
an overwrite is an explicit per-path caller authorization, which the resulting manifest entry records.

**Retention is a state with memory, not an omission.** `RetainedOutput.recorded` carries the prior
generation's whole `ManagedOutput`, so a path retained at one generation and produced again at the next is
recognised as owned instead of being overwritten, and a retention the next generation does not re-produce
is carried forward rather than falling out of the manifest. Both defects were found by the acceptance case
in the worker's own implementation and fixed in the writer rather than worked around; they are the two
file-loss bugs §5 exists to prevent. `ProjectionHooks.before_publish` is the module's only test seam: it
runs after every output is staged and before the first rename, which makes checkpoint 4's interruption
deterministically inducible without a sleep, a thread or a signal.

**`memory/knowledge/view_source.py` is the reader port's implementation, and it performs no selection,
no ordering and no classification.** It reads the envelope and revision tables the R10 generation pair owns,
decodes each stored payload through the shipped typed-JSON decoder, and hands the view layer flat
`ViewSourceRow` values. That division is the contract rather than a style choice: if this module ordered
anything, the ordering would carry no provenance class and gap A-G5 would be open again, one layer lower and
harder to see. It is **read-only by handle, not by discipline** — `open_view_reader` opens the database
through `open_read_only_database`, so a refused view leaves the dataset byte-identical as a property of the
handle rather than as a rollback someone has to remember — and the snapshot it reports is the identity the
dataset actually holds, so a view cannot be handed a snapshot it did not read.

## 260915-KS-L21 The Census Apparatus, Generation 9, And The Cutover That Is Prepared And Not Executed

`KS-R21@v1` is the knowledge substrate's **measurement** leaf, and it is the first thing in this route that reads
the Markdown-era onboarding corpus rather than writing a knowledge dataset. It adds a subpackage of nine modules
(`memory/migration/`), one record group (`knowledge/census_records.py`), one generation declaration
(`knowledge/schema_v9.py`) and the payload vocabulary the three census record kinds cross the wire as
(`models/knowledge/census.py`). **Nothing in the leaf switches anything live**: the cutover's three artifacts are
data and an evaluation, with no trigger, no flag, no scheduled activation and no side effect.

**The package states its own boundary in its first paragraph, and the boundary is what a reader must not lose.**
`memory/migration/__init__.py` records that the package *reads* the corpus and **writes nothing to it**: an
artifact is read, parsed into claims and dispositions, and reported against a frozen baseline. The one write path
it uses is the shipped candidate batch operation, through this route's own census record group. Its docstring also
records why it is a subpackage of `memory` rather than a new top-level package — it ranks with the thing it
measures — and that **nothing here interprets**: the parser reports what it read, a mapping names where a read
artifact goes, a reference resolves to one of three recorded states, and a mismatch is reported as the mechanical
fact it is. Semantic categories, verdicts and mismatch classes are authored by a curator, in record kinds other
leaves own.

**The baseline is frozen by identity, not by ref.** `memory/migration/baseline.py` records a baseline as **two
exact Git tree ids** — the code revision and the memory revision the corpus was read at — because a baseline whose
code side is a branch name is not frozen at all, and because "mechanical mismatch at the baseline" has to be a
checkable statement rather than a moving target. It is resolved and passed in, never inferred from `HEAD`, so a
baseline cannot silently move when somebody commits. The baseline travels *inside* every census record's
provenance rather than as a parameter of the run that produced it, which is what makes two artifacts examined at
two baselines two observations. Both refusals on this path are filed under one operation name —
`BASELINE_OPERATION` = `read_knowledge_scope` — because reading a baseline is not one of the candidate write
operations.

**The parser reports structure, and its sharpest edge is where a card's front matter ends.** `parse.py`
classifies nothing: no keyword test, no scoring, no heading-to-topic mapping and no branch whose condition is a
statement about meaning. It declares the formats it admits, each with a reason, and the unsupported form is **an
entry in that list** rather than an exception — the generated bootstrap artifact, whose leading table is not a
card's front matter. Its one correctness detail is measured rather than hypothetical: the metadata reader
continues **only while a row's key is a name of the declared front-matter vocabulary**, so the evidence inventory
a legacy card carries in its body cannot be absorbed as front matter the card never declared. Every artifact gets
one of four outcomes (`parsed`, `unparsed`, `unsupported`, `unreadable`); the reader never raises for a bad
artifact, and stored text is bounded by the payload's declared width as the artifact's own prefix — never a
truncation marker, because a marker would be this parser writing into a field that means "what the artifact said".

**The inventory is taken over the scope, and that direction is the whole reason `inventory.py` exists.** A
corpus-derived list can only enumerate the sources that already have a card, so the sources with **no onboarding**
— the ones a coverage question is asked about — are exactly the ones it cannot see. Here a missing card is a
recorded row with `inventory_state="absent"` rather than an omission, and a card whose declared source is gone
still gets a row. A row's route is derived from the scope's own layout by matching **whole path segments** against
the declared route directories (`mcp/src/x.py` belongs to `mcp`; `mcpfoo/x.py` belongs to none, where a bare
string prefix would have filed the second under the first), and it is recorded as an observation about the layout
— deliberately *not* the knowledge substrate's route axis. An unreadable or non-UTF-8 artifact is a row carrying
its outcome and a capped prefix of the content it could not read, because a silent skip and a clean read are
indistinguishable in a count.

**The mapping registry is data a reviewer can read, and the absence of a scoring function is the design.**
`mappings.py` selects an entry by an equality test on a **declared** field of the artifact and returns `None`
where nothing matches; `UNMAPPED` is a named state, not an error. It does not construct a best-fit mapping, does
not choose a target kind by name similarity and does not create a record so a row looks complete — those are the
three things §2.2 forbids, and a "closest" mapping would be an inference with a distance metric on it. Each
entry's declared fields are checked against the payload model the target kind actually requires, so a mapping
cannot claim to supply a field the record kind does not have and a target kind whose required field nothing
supplies is discovered **here** rather than after a partial import. The registry carries its own version
(`MAPPING_REGISTRY_VERSION`) beside every outcome, so a re-run at a changed mapping is a difference to report
rather than a silent second import.

**Resolution has exactly three states, all reportable, and nothing is repaired by resemblance.**
`resolution.py` compares exact spellings against a caller-supplied candidate set and returns `resolved`,
`unresolved` or `ambiguous`; there is no fuzzy match, no prefix fallback and no canonicalisation step, and no
function that creates a row to receive a dangling reference. The mismatch report states the mechanical fact —
which artifact, which reference, which baseline, what contradicted what — and has **no field that could hold a
semantic verdict**, because `Doc13:460`'s four-way distinction belongs to a curator and §3.4 requires the
pipeline to report *that* something is contradicted and *where*, never *which* of the four it is.

**The accounting keeps its cells apart, and one of them it refuses to compute.** `census_measures.py` states the
eligibility rule once — a claim enters the cohort exactly when its record kind is `census_claim`, its
applicability is `assessable` and it carries a claim text — which is what makes `Doc12`'s Example 3 and
requirement 5.2 read alike. `T`, `F` and `U` come from a curator's authored assessment and from nothing else:
there is no code path from an import outcome to any of the three, and `unassessed` is derivable only as "no
assessment exists". The six measures are reported **together** and never composed into one number, a zero
denominator is `not_applicable` with its counts beside it rather than a perfect score, and a ratio that could be
read as a verdict is paired with the counts that qualify it. `K` is **never read here**: the coverage measure
takes the reference inventory's size as an argument, because a `K` this module could compute would be derived
from the corpus being measured.

**The census is a read, and its one deliberate absence is the denominator.** `census.py` computes nothing the
record kinds do not already carry. `reference_inventory` returns the independently reviewed inventory with its
review state, `coverage_is_publishable` is the one predicate that decides whether a `C / K` figure may be
reported at all, and it **refuses rather than warns** — `CR21-6` makes a missing reviewer seat a *blocked*
condition, not a figure to publish with a placeholder. The review must be by someone other than the inventory's
author, which is why `C / K` is `not_measurable` until that seat is settled.

**The cutover is three artifacts and an evaluation, and its non-execution is structural.** `cutover.py` carries
the six criteria, the seven-step plan with its rollback story, its archival step and its point of no return, and
the proposal with the exact quoted escalation boundary (`ESCALATION_BOUNDARY` = `design/storage-design.md:465`,
`ESCALATION_ITEM` = "starts migration/cutover"). `evaluate_criteria` returns the exact measures that fall short
rather than a boolean, so a criterion that cannot be met is reported unmet with its observed value and is never
narrowed until it passes — "cutover is not yet justified" is a **conforming** output. `ProposalDecision` has no
value that means "approved": the decision state is `absent`, and its absence is the state. There is no function
in the module that writes anything.

**Generation 9 is the ninth explicit append, and it appends three records and three relations rather than one
wide table.** `knowledge/schema_v9.py` declares the inventory row, the assessable claim and the migration
disposition, plus the three relations `Doc12` names as relations rather than fields — a claim's evidence, a
claim's realization attribution, and the records a disposition links to. `schema_generations.py` composes it with
the same generic append generations 2 to 8 use, so `GENERATION_9.tables[:len(GENERATION_8.tables)] ==
GENERATION_8.tables` and generation 9's columns for each of generation 8's thirty-four names are the generation
it descends from; `CURRENT_GENERATION` is now generation 9, so a *new* store declares version 9 while an existing
generation-8 dataset keeps declaring 8 and is read through generation 8's own record. **No census table carries a
content-address, a logical digest or a fingerprint column**, and none is added: "no second identity authority" is
a property of the declared columns, and the content digest stays on `record_revision` where the envelope puts it.
Three columns are recorded facts rather than derivations — `observed_doc_type` (what the parser read, so the
cardinality rule's input is auditable), `claim_kind` (whose closed vocabulary admits `unclassified` as a
**value**, never a NULL a reader could take for "not yet read") and `applicability` (the field the eligibility
rule reads). Every table is sealed against update and delete by the same trigger pair the earlier generations use.

**The record group joins the batch rather than opening its own transaction.** `knowledge/census_records.py` owns
the row codecs and the in-transaction write step, and reuses the two owners that already exist: the generic
envelope/revision codec from `facet_records` (so a stored revision's seal is verified against the one digest
definition) and the envelope seam for payload admissibility. It declares the `(kind, record_schema)` triples and
nothing else about admissibility. Its step is an `apply_*` function taking the caller's open store, because the
batch owns the transaction. In the batch, `batch_preconditions.require_census_generation` refuses a census
command against a dataset that predates the census's tables — the dataset's own generation is read from the open
store, so the refusal carries both numbers as facts — and the census dispatch entry validates the closed record
kind and the declared shape **before any row exists**, through the envelope seam, so an unregistered kind or an
undeclared field is the shipped `invalid_payload` refusal rather than a storage error. Reference resolution is
deliberately not there: it belongs to the record group's own write step, which runs in command order, so a
disposition that links to a claim the same batch creates resolves once that claim's command has run.
`candidate_records` adds the group's three record tables to the writable union and its three row digests to the
reader table, and deliberately omits its three relation tables — each is written only as part of the aggregate
that owns it, so no command addresses one and no expectation could name a state a command could produce.

## 260928-MIK-L04 The Index Matches The Root Family Route

**Route impact (MIK-R04@v2, review R3-1).** [`knowledge_index/query.py`](knowledge_index/query.py.md)'s
`families_governing` matches a path against the path itself, its ancestor directories and now the root route
`.`, so a family routed at `.` governs every path, exactly as the validator's `route_covers` reads it. The
index schema, the key and the cache are unchanged.

- The candidate list is the path and every ancestor, nearest first, ending with the root route `.`; `families_governing` matches routes against exactly this list. [84]
- A family routed at the root governs a root-level file and a deep file. [85]

## 260928-MIK-L20 The Census Inventory And Writer: A New Package, `knowledge_census/`

**Route impact (MIK-R20@v2).** The new package `knowledge_census/` is the census's Git-reading and writing
half; its reading, checks, measures and report are in `memory_quality/knowledge_census/`, which this package
may import because `memory` ranks above `memory_quality`. No separate `knowledge_census/overview.md` was
created: like `knowledge_index/`, `knowledge/` and `migration/`, it is governed by this overview.

- [`knowledge_census/inventory.py`](knowledge_census/inventory.py.md): `take_inventory` resolves the code and
  memory revisions to exact commits and lists both trees through Git objects only; a revision that names no
  commit, or a tree Git cannot list, is refused with `CensusBaselineError`. The inventory is mechanical: one
  row per in-scope source file and per onboarding artifact, each with its nearest governing onboarding route.
- [`knowledge_census/writer.py`](knowledge_census/writer.py.md): `CensusWriter` creates a census once (the
  inventory first, the baseline last as the commit point), appends claims, assessments and route statuses,
  and sets dispositions. Every write runs the same census checks the validator registers against the current
  tree and writes nothing when refused. It refuses a memory tree without `knowledge/layout.json`, so it never
  touches production memory before MIK-R37.
- [`knowledge_census/__init__.py`](knowledge_census/__init__.py.md) re-exports both.

The legacy database census described in "260915-KS-L21 The Census Apparatus" above (`migration/census*.py`,
`knowledge/census_records.py` and the generation-9 tables) is untouched and remains reachable until MIK-R26
(leaf L26) retires it, by architect ruling.

- An unreadable baseline is refused. [86]
- Every write is checked, then written atomically. [87]

## 260915-KS-L23 The Substrate's Own Contradictions, And The Two Behaviour Fixes Under Them

This route's knowledge substrate was already built by `L10`–`L22`; `KS-R23@v1` fixed **two behaviour
defects inside it** and repaired **three docstrings that disagreed with their own registries**. All of
it is uncommitted in the delivered code worktree (base `c5a74a85`), and each module's sidecar carries
the detail.

| Module | What changed | Why it matters |
| --- | --- | --- |
| `knowledge/merge_changeset.py` (`MaterializedChange.primary_key`) | the key is read from the side that carries it — the **old** side first, so a `DELETE` (old only), an `UPDATE` (both, and only the old holds the key) and an `INSERT` (no old side) all resolve | it read the **new** side, so every right-side `UPDATE` was refused with a spurious `changeset_postcondition_failed` whose `record_id` was `…<not-supplied>…`, and a side that edited an existing record in place could not be merged at all |
| `knowledge/routes.py` (`require_acyclic_routes`) | runs on the connection the delta was applied on, after the rows are written and **before that application commits** | a replayed `route.parent_route_id` change is a real operation on a table inside the merge's attached set, so a candidate whose hierarchy reaches itself must be rolled back rather than published |
| `knowledge/detection_walk.py` | the group key distinguishes the items the signal identity is supposed to name, rather than collapsing on a shared `record_id` | one realization claim can legitimately carry two coverage items, and the old key emitted **one** `signal_id` for both, so `build_detection_run` refused the whole run as not reproducible |
| `knowledge/record_envelope.py` | the module docstring states the registry's real membership: **22 pairs across 8 groups**, with `evidence_claim` registered | it had said 4 groups / 12 kinds and deferred `EvidenceClaim` as "later" |
| `knowledge/schema_generations.py` | the composition comment states the real shape: **eight** per-generation wrappers (generations 2–9), with generation 5's a hand-written 17-line composition | it had said "the four per-generation wrappers below … one line each" |
| `models/knowledge/citation.py` | the docstring matches the delivered schema: generation 5 appends **one** table (`citation_binding`) and the route is a **column** | it had claimed a per-binding association table |

**Two things a reader must not infer from this list.** The generated `citation_binding` table is not
a second identity authority and the route column is not a hierarchy — the schema generations stay
append-only, frozen and selectable, and generation selection comes from the dataset's own recorded
version, never from the caller and never from the running build. And the pyright repairs recorded
under this leaf are **real types, not suppressions**: no `# type: ignore`, no widened rule, no
narrowed scope — a report that says "pyright: 0" must say which **form** it ran, because the gate's
broad form (`pyright --project . --pythonpath <pinned python>`) and a scoped run disagree about the
same commit.

## 260915-KS-L45 Two Enumerating Reads On The Opened Store, For The Reviewer's Subject List

**This route's impact is two read-only methods on `OpenedKnowledgeStore`, and they exist because a
reader cannot list candidates it was not pointed at.** `list_invariants` returns every invariant
identity the bound namespace records — `repository_id`, `invariant_id`, `display_label`,
`label_provenance` — decoded through the same `records.decode_invariant_row` the other reads use and
**ordered by the identity's own column**, so two runs over one snapshot agree without a tiebreak this
reader chose. `list_families` is the same enumeration for the surface's other admitted subject kind,
read the same way rather than derived from the invariant list, because a family identity is not a
projection of an invariant and the two subject kinds are peers.

Neither is a selection rule, and the card for `memory/knowledge/store.py` says so explicitly: both
return **every** recorded identity, apply no filter and compute no count. The Intent Reviewer's entry
list is what compares each returned identity and drops the ones the shipped comparison refuses, and
that logic lives in `application/knowledge_review.py` — so a reader following the subject list back to
its source arrives at an enumeration, not at a policy that was smuggled into the store.

Why it belongs here rather than in the adapter: the identities are rows in this store's own tables, and
reading them through the store's own operations is what keeps "the identities this list offers" and
"the identities the namespace records" the same set rather than two readers' opinions of the same
bytes. The methods take no arguments and mutate nothing; they are reads on the same opened connection
every other read in this route uses.

- **Every invariant identity the namespace records, ordered by the identity's own column, with no filter and no count.** [88]
- **The same enumeration for the surface's other admitted subject kind.** [89]
- The row decoder both new reads use, so a listed identity is a decoded identity rather than a column tuple. [90]
- The consumer's entry half: the catalogue enumerates every recorded identity of both snapshots under the recorded namespace — no per-subject comparison runs and no subject is dropped to imply a smaller population (`ICR-R09@v1`). [91]

## 260915-KS-L43 The Merge Carries Every Accepted Decision, And Its Conflict Taxonomy Gets One Key

**This route's impact is the merge's authored-decision channel, plus one naming defect in its conflict taxonomy.**
Three files under `memory/knowledge/` changed, and each change is a fact a route reader needs.

**Accepted decisions travel as a sequence, because one retained conflict is rarely the last.** `MergeRequest.reconciliation`
became `MergeRequest.reconciliations: tuple[AuthoredReconciliation, ...]`, `apply_changeset(..., reconciliations=())`
replaces its single `reconciliation`, `_authored_decision` loops the sequence, and `merge_conflicted_stages` /
`settle_knowledge_conflict` forward it. Nothing about the decision boundary moved: **each** entry still names exactly
one row, `keep-left`/`keep-right` still apply only to the conflict in hand, a row-less decision still answers only a
row-less conflict, and every conflict no decision names is still refused exactly as it was. What the sequence repairs
is measured, not theoretical: with only the newest decision carried, a retained merge holding two conflicts re-refused
the row the previous decision had already answered, the two alternated forever, and the caller was offered a decision
it had already made and that had already had its effect — twelve applications to the cap and no settlement before,
two applications and a settled merge after (`evidence/after-independent/recovery-progress-after.json` against
`recovery-progress-before.json`).

**The taxonomy's two lookups had drifted apart, and they now share one key.** `_TAXONOMY` selects the refusal builder
and `_CONFLICT_NAMES` selects the name an operator reads, and both are keyed by `(SQLite code, whether the conflict is
the relationship one)` — but they asked the question differently: the builder asked
`code == _CONFLICT_CONSTRAINT and table in _RELATIONSHIP_TABLES`, while the name lookup asked
`table in _RELATIONSHIP_TABLES` alone. `realization_claim` is a relationship table, so a `duplicate_identity` on it was
refused correctly and *simultaneously* named `unmapped_conflict_3` — the operator was told the taxonomy does not name a
conflict it maps, which is a false statement about the tool rather than a fact about the data. `_conflict_key(code, table)`
is now the single home for the predicate, `_conflict_name(code, table)` the single namer, and `_conflict_refusal` and
`_conflict_facts` both go through them. The predicate is what it is because the relationship answer exists only for the
constraint code: a unique-declaration violation on a relationship table is `duplicate_relationship`, while the same table
colliding on a primary key is two independent insertions of one identity like any other table's.

**A candidate directory may carry an owning operation's own local record.** `candidate_workspace.py`'s docstring now
records that the layout it fixes is *which file is the working database*, not the file count: an operation that owns the
candidate may keep its own local, operation-scoped record beside the receipt and the lock, exactly as the receipt itself
is such a record. The curator ingest's `curator-allocation-journal.json` is the first instance. Nothing about admission,
disposal or the two-phase creation moved.

- The authored-decision channel as a sequence, and the one matching rule that still bounds it to a single row. [92]
- The taxonomy's one key predicate and the namer built on it, so the builder and the operator-facing name cannot disagree. [93]
- The candidate layout's fixed part and its owner-writable part. [94]

## 260915-KS-L42 The Row-Less Referential Conflict's Recovery Is Measured, Not Inferred From Its Code

**This route's impact is the merge's conflict offer, and it closes the residue round 2 left open.** In `memory/knowledge/merge.py` the same `delete_reference_conflict` arrives in two orientations no code can tell apart — the arriving side added a broken reference (its delta carries the INSERT), or it removed a row the retained side still cites (its delta carries only the DELETE) — and `keep-left` on that code is a *retraction* of rows the arriving delta inserted, so it applies in the first and provably cannot in the second. `_retraction_precondition` now measures the answer **before** the offer is built: it copies the retained side into the workspace's own `PROBE_LEFT_NAME` and `_retracts_arriving_rows` applies the shipped `apply_changeset` to that copy with the row-less `keep-left` decision, answering `arriving_insertion` only for a reference-clean result — a conflict, or an application that could not run, withholds the offer. `_conflict_facts(..., precondition=...)` carries the answer onto the conflict record and `expressible_decisions` reads it instead of the code.

**`_retract_referential_rows` was deliberately not widened.** Retracting an arriving `UPDATE` or `DELETE` would delete or overwrite content the retained side authored, so the orientation where the arriving side removed the parent keeps its refusal, and the missing row stays the caller's to restore by hand in the worktree. Measured before and after with the round-2 verifier's own scenario: before, `decisions: ["keep-left"]` with `nextOperation=reconcile_knowledge_resolution`, and driving exactly that advertised call returned a byte-identical response forever; after, `decisions: []`, no `knowledge_resolution` in `nextArgs`, `nextOperation=continue_sync_resolution`, and driving that reaches `sync-resolution-incomplete` — a different state and a different response, with HEAD and all inputs unchanged and the engine's diagnosis byte-identical.

**Open, not settled — named for the round-3 reviewer.** `cancelArgs`, carried beside `nextArgs` by every `sync-resolution-required` response, returns `sync-operation-refused` / `SyncGitProofError` in **both** orientations, including the INSERTED-row orientation round 2 verified as working. It is not introduced by this change and was not widened into it; it is most likely the fixture limitation round 2 already recorded (the sync fixture writes a bare contract with no canonical enclosure locator chain). The `continue` half of the manual continuation is real and drives state; the `cancel` half could not be proven to settle in that fixture.

## 260915-KS-L47 The Anchor Read Gets One Source Of Truth, And A Stored Anchor Binds What Is Stored

`memory/knowledge/anchors.py` gained a small public `read_anchor(connection, repository_id, anchor_id)`,
and `get_anchor` now delegates to it. The reason is not convenience: the curator intake holds a read-only
connection and no `OpenedKnowledgeStore`, and re-deriving the column list and decoder there would have
created a second source of truth for how an anchor row is read -- exactly the shape that lets a stored
identity be answered two ways. `get_anchor`'s own behaviour is unchanged.

The caller is the application layer's explicit-anchor-reuse repair: `knowledge_curator_ingest.py`'s
`_require_stored_anchor` resolves a target-level `anchor_id` through this reader against the datasets
`_Source.anchors` carries (candidate then baseline) and refuses a supplied path, blob or locator that
disagrees with the stored row, before any plan exists. The measured defect was a run that reported
`changed` and published a receipt naming symbol `other` while the stored realization cited the
`resolve_budget` anchor; the repair makes the receipt, the stored claim and the public read agree by
construction, and a matching reuse still succeeds without adding an anchor row. **No memory-layer
behaviour outside this read changed**, and allocation-per-creation, revision-keyed anchor identity and
the separate claim identities are untouched.

## 260921-ICR-L2 The Expansion's Observation Is One Implementation, And A Changed Path Carries Its Status

**Route meaning changed: this route's display vocabulary now describes a *status-bearing* change, and
the observation behind it has one implementation.** `memory/knowledge/diff_display.py` gained
`TreeChange` — the raw filename exactly as Git recorded it, Git's status, whether the content can be
rendered, a mode-change flag and the reason an `unknown` is unknown — plus three fields on `TreePaths`:
`entries` (the same measurement at full resolution, held in agreement with `paths` by a construction
check), `partial` (the path set was measured while part of it could not be reported whole) and
`unrepresentable` (the changed paths whose name is not valid UTF-8, kept in full, with
`unrepresentable ⇒ partial` enforced at construction). `_expansion_detail` states a partial
observation's limit beside its counts, so a smaller count is never read as the whole change set.

**The advertised command changed with it.** `TREE_DIFF_COMMAND` is now
`git diff --raw -z --no-renames {before_tree} {after_tree}` — the same delimiter-safe interface the
measurement reads — because the line-oriented `--name-only` form quotes and escapes a pathname
containing a tab or a newline, so a caller who ran the advertised command would hold a different string
from the address the response lists and the address the same file is expanded by. The measurement itself
moved to `application/review_source_inventory.py`, and `application/knowledge_diff.py`'s
`git_tree_difference_probe` — the production `TreeDifferenceProbe` this route's expansion is reached
through — is now a one-line delegation to it.

- **The status-bearing change: the raw path as the address, Git's status, the renderability and the reason an unknown is unknown.** [95]
- **The observation's two renderings and its two honesty rules: paths and entries cannot disagree, and an unrepresentable path implies a partial observation.** [96]
- **The advertised command, now the delimiter-safe interface the measurement itself reads.** [97]
- **The expansion detail that states a partial observation's own limit instead of only counting the paths it could carry.** [98]
- **The probe this route's expansion is reached through, now a one-line delegation to the review's own observation.** [99]
- The cases that measure the observation on real repositories, including the name a line-oriented interface loses and the non-UTF-8 boundary. [100]

## 260928-MIK-L23 The Derived Knowledge Index: A New Package, `knowledge_index/`

**Route meaning extended (MIK-R23@v1).** Knowledge is becoming text in Git (D18), each relationship written
once from its owner's side (D19). The new package `knowledge_index/` answers the reverse directions no file
records, from an SQLite file derived from one memory tree and nothing else. It has no route overview of its
own: like its siblings `knowledge/` and `migration/`, it is governed by this overview.

- [`tree.py`](knowledge_index/tree.py.md) reads a tree from a working directory or through Git objects and
  computes its key: the tree id, or for a directory the tree id of its captured state (`git add --all` into
  a disposable index whose object store has the real one only as an alternate, so computing a key writes
  nothing into the repository).
- [`build.py`](knowledge_index/build.py.md) parses the files through the MIK-R21/R07 models and writes the
  `ix_*` rows declared in [`schema.py`](knowledge_index/schema.py.md); a file that fails its schema, sits at
  a location its format forbids, or repeats an ID is named and marks the index `partial`.
- [`projection.py`](knowledge_index/projection.py.md) also writes the index as a dataset of this route's
  store schema (uuid5 identities, a constant namespace, retired records left out), so
  `knowledge/read.py`, the views, the comparison and the scope construction run over it unchanged.
- [`query.py`](knowledge_index/query.py.md) answers rule 3's lookups; every answer carries the index state.
- [`adapters.py`](knowledge_index/adapters.py.md) opens an index as a read-only `OpenedKnowledgeStore` for
  `knowledge/registered_scope.py`.
- [`cache.py`](knowledge_index/cache.py.md) keeps one file per key under the coordination runtime, refuses
  any location inside a Git working tree, recomputes a working tree's key on every lookup, and evicts by age
  and size.
- [`__init__.py`](knowledge_index/__init__.py.md) is the package door.

No knowledge writer writes the index, it is never merged, and deleting it loses nothing. Its callers are the
application's dataset selection (`application/published_intent.py`) and the CLI; before MIK-R37 no
production memory tree is converted, so the installed runtime never reaches it.

- The package map. [101]

- The captured-state key. [102]

- The build, which names every failing file. [103]
- Retired records are left out of the projection. [104]
- The cache refuses a Git working tree. [105]


## 260928-MIK-L24 Conversion And Boundary Crossing: A New Package, `conversion/`

**Route meaning extended (MIK-R24@v1).** The new package `conversion/` turns a memory tree and its legacy
`knowledge.sqlite` into the text knowledge format. It is deterministic, pinned to conversion-format version
`1`, loses no citation information and authors no knowledge. It also carries the two ways a comparison or a
sync crosses the boundary between an unconverted tree and a converted one. It has no route overview of its
own: like its siblings `knowledge/`, `migration/`, `knowledge_census/` and `knowledge_index/`, it is governed
by this overview.

- [`convert.py`](conversion/convert.py.md) is the pure `convert_memory`: version pin, no-op on a converted
  tree, whole-tree validation before anything is written, and the report.
- [`cards.py`](conversion/cards.py.md) handles the Markdown: metadata and Update History removed, citation
  tables become `- <finding> [n]`, one `## Evidence` section, and marker-shaped text escaped.
- [`citations.py`](conversion/citations.py.md) turns a row into a reference. Symbols bind through the shipped
  extractor, covered ranges add nothing, and any anchor text no target carries is kept in `note`.
- [`code_objects.py`](conversion/code_objects.py.md) is the only door to the code objects. It reads by exact
  identity, and an abbreviated commit is resolved against every prefix match.
- [`legacy_db.py`](conversion/legacy_db.py.md) is the read-only legacy database reader and the export at
  head revisions. Entries keep their recorded blobs, and derived-ID collisions refuse.
- [`inputs.py`](conversion/inputs.py.md) reads a tree from a directory or Git, and writes a finished
  conversion.
- [`base.py`](conversion/base.py.md) is the converted base of rule 7, and `GitBaseConverter` for the
  validator's commit route.
- [`crossing.py`](conversion/crossing.py.md) and [`crossing_sync.py`](conversion/crossing_sync.py.md) are
  rule 8's structural merge: markers first, conversion of every side, merge by key with mechanical fields
  never conflicting, and conflicts marked for the curator.
- [`crossing_port.py`](conversion/crossing_port.py.md) is the adapter the composition binds to the
  worktree layer's crossing port.
- [`__init__.py`](conversion/__init__.py.md) is the package map.

**Architect rulings carried on the cards:** anchor text is kept in `Reference.note`; conversion and crossing
are separate routes; crossing conflicts are marked and reported; the moved no-impact markers go in the
`onboarding_trace` row's `markers` list; version 1 is pinned by a golden digest. The consumers of
`comparison_sides` (MIK-R07, R30, R08, R25) wire it in their own leaves.

Its callers are the `knowledge-convert` CLI, the validator's commit route and the managed sync's crossing
branch (through `application/worktree_services.py`). Before MIK-R37 no production memory tree is converted,
so the installed runtime never reaches it.

- The package map. [106]
- The pure conversion, its version pin and its validation. [107]
- No anchor text lost: it is kept in the note. [108]
- The read-only reader. [109]
- Rule 7 for any comparison consumer. [110]
- Rule 8's item rules and conflict markers. [111]
- Rule 8's steps. [112]

## 260928-MIK-L28 The Index Answers Proofs, And The Invariants Without One

**Route meaning extended (MIK-R28@v1 rules 4 and 5).** [`knowledge_index/query.py`](knowledge_index/query.py.md)
gains two lookups over the `ix_entry` proof rows the MIK-R23 build already writes: `proofs_of(invariant_ids)`
and `invariants_without_proof()`, which lists the **live** invariants (a retired one is not listed) that no
proof entry names. Both carry the index state like every other answer. Their consumer is
`application/knowledge_proofs.py`, for `knowledge_read`'s `invariant` and `family` views and for the curator
checklist's "without proof" section. That list is **information, not a gate (architect ruling,
2026-09-29)**: the admission rule accepts criteria other than a proving test. The index is still derived,
never written by a knowledge writer, and unreached by the installed runtime before MIK-R37.

- The two proof lookups. [113]
