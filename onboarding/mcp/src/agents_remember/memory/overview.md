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
- **`knowledge/publication.py` (retired).** `publish_prepared_snapshot` refuses a destination
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

## Retired canonical review collections

The former detection/evidence owners isolated individual damaged database rows. Those classes and readers are retired. Current review preserves curator assessments/evidence, marks canonical channels unavailable without counts, and never substitutes proof/worklist rows for them. [28] [31]

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

This route owns memory-repository lifecycle, text-tree parsing/indexing and retained read schema. Higher-ranked curator file writing authors records/entries/history. The canonical candidate, batch mutation, publication, portable import/export and changeset merge routes are retired. knowledge supplies read-only index connections/codecs, logical identity and one pinned schema; knowledge_index builds/queries the selected tree's derived view. conversion handles bounded legacy input and structural crossing; knowledge_census carries text-format census artifacts. [28] [65]

## Purpose

Memory lifecycle and file-derived knowledge reads. The selected text tree is authority and its SQLite index is disposable.

## Hot Path Summary

Index build/cache/query read the selected converted text tree. Projection fills retained tables and store opens them read-only. The schema module declares exactly v9 and logical computes its row identity. File authoring belongs to application/knowledge_writer; sync structurally merges knowledge files, never SQLite changesets. [65]

## Historical canonical substrate — retired

The earlier store used sealed rows, lock-guarded batches, generation dispatch, copied candidates, publication, portable roundtrips and changeset merging. MIK-R26 retired those mechanisms. Retained declarations/codecs now support one derived-index schema, never a canonical writer or a legacy database as current knowledge. Text authoring, indexing and structural merging carry current responsibilities. [65]

## Invariants And Boundaries

- Text files are knowledge authority; the index cannot author an obligation.
- Reads use read-only handles and validate one schema; another version refuses with conversion guidance.
- Logical identity excludes physical layout, paths, timestamps and Git locations.
- Scope/family relationships are authored, never inferred from directory proximity.

- Retained logical encoder, one pinned schema and read-only store. [65]


## Evidence

### Repo-Internal References

The declarations below establish the current behaviour; this inventory is not execution evidence.

**The 260915-KS-L5 merge half**, cited in the current `Finding | Anchor | Source` shape. The older rows below remain in the superseded
two-column shape and are recorded as a pre-existing repository-wide migration item in the Update History rather than converted from inside
one leaf's curation pass.

- The two operations and twelve codes the merge added to the shared vocabulary. [39]
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

- Retained logical encoder, one pinned schema and read-only store.
- The two portable operations and the one code they added to the shared vocabulary. [68]

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

## Historical canonical operation — retired

This earlier canonical operation is retired. Current knowledge is text, indexing is derived, and sync conflicts are structural file items; no database mutation or row-decision recovery remains. [65]

## Historical canonical operation — retired

This earlier canonical operation is retired. Current knowledge is text, indexing is derived, and sync conflicts are structural file items; no database mutation or row-decision recovery remains. [65]

## 260928-MIK-L04 The Index Matches The Root Family Route

**Route impact (MIK-R04@v2, review R3-1).** [`knowledge_index/query.py`](knowledge_index/query.py.md)'s
`families_governing` matches a path against the path itself, its ancestor directories and now the root route
`.`, so a family routed at `.` governs every path, exactly as the validator's `route_covers` reads it. The
index schema, the key and the cache are unchanged.

- The candidate list is the path and every ancestor, nearest first, ending with the root route `.`; `families_governing` matches routes against exactly this list. [84]
- A family routed at the root governs a root-level file and a deep file. [85]

## Text knowledge census

knowledge_census owns Git-reading and artifact-writing for the file-based census; memory_quality owns its bounded measurement/report. The earlier migration-to-canonical-store writer is retired. [65]

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

## Historical canonical operation — retired

This earlier canonical operation is retired. Current knowledge is text, indexing is derived, and sync conflicts are structural file items; no database mutation or row-decision recovery remains. [65]

## Historical canonical operation — retired

This earlier canonical operation is retired. Current knowledge is text, indexing is derived, and sync conflicts are structural file items; no database mutation or row-decision recovery remains. [65]

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

- Source-path observation cases moved with meaning preserved. [100]


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
- **Historical:** `adapters.py` (retired) opens an index as a read-only `OpenedKnowledgeStore` for
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


- Current record owner marks retired classes unavailable. [28]


- Real authority availability and unmeasured count contract. [31]
