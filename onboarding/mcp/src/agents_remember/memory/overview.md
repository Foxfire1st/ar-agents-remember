# Memory Repository Lifecycle And File-Derived Knowledge

## Governing Overview
[mcp/overview.md](../../../overview.md)

## Purpose

This area connects memory-repository lifecycle operations with knowledge read from a selected memory text tree. Knowledge files are authority; their SQLite index is a disposable representation for forward and reverse lookups and the retained logical readers. Deleting an index loses no authored knowledge. This area does not own task approval, task status or Git attribution policy.

The route includes baseline adoption, bounded legacy carryover, conversion and structural boundary crossing, text census inventory/publication, index capture/build/cache/query, and retained knowledge schemas, codecs, reads, anchor observations and comparison accounting. Application-layer knowledge writing owns ordinary record, entry and history authoring. Retired canonical database mutation, batch, copied-candidate, publication, portable import/export and changeset-merge accounts must not be read as current write routes.

## Hot Path Summary

MIK-R109 adds reverse-locator queries on `KnowledgeIndex`: `entry_sidecar`/`entry_sidecars` identify declaring sidecars, `record_paths` identifies authoritative record files, and `uuid_text_ids` resolves projected UUIDs to text IDs. They read the existing index tables; schema, derived-cache custody and text authority stay unchanged. Caller-visible naming/state projection remains in the application layer.

A selected Git tree is read through objects without checkout. A working directory is captured through a disposable Git index and object store, using the repository object store only as an alternate. Its key is the captured tree ID. JSON knowledge and onboarding documents supply indexed content; ordinary prose and other tracked content contribute to the tree key without becoming indexed documents. Generated route-index caches, hidden directories and census documents are excluded from indexed input.

The builder parses recorded files, writes `ix_*` relationships and projects the surviving logical tables. Parsing/schema/location/duplicate-ID problems name the offending file and make the index partial; cross-document integrity belongs to the knowledge validator. A complete build is consequently not a substitute for validator acceptance. The query surface carries tree key, converted state, completeness and problems in `Answer` values for its substantive lookups. The UUID-to-text-ID helper returns a plain optional string rather than an `Answer`.

The cache lives outside Git working trees, normally under `<coordination-root>/runtime/knowledge-index`. It recalculates a directory key for each lookup, rejects a cache inside a Git worktree before creating it, rebuilds files whose index format/key does not match, installs a completed temporary index by replacement, and evicts by age and size. Defaults are fourteen days and one GiB; the retained current file is excluded from eviction. `INDEX_FORMAT` is `ar-knowledge-index/v3`, with history identity `(path, id)`.

Readers open existing index datasets through SQLite read-only handles. The store validates the one declared schema, reads identities/revisions, rechecks revision payload seals, and computes logical identity. Recorded-scope selection and paging remain separate operations. Application consumers supply exact selected datasets and source bindings; the index does not promote a record into an obligation or an approval.

## Construction And Ownership

### Lifecycle and first baseline

`baseline.py` resolves lifecycle requests and consumes drift/ledger information. On converted memory, attributed history takes precedence as `already-adopted`; otherwise the payload distinguishes unavailable history, old-format cards, validator violations and actionable drift. Old-format-card detection belongs to first adoption, not ordinary validation of an existing baseline. Metadata-key first cells and Update History headings count; incidental prose mentions do not. `accept_drift` accepts stale anchors only, never legacy-card or validator refusals.

Converted first adoption validates the selected immutable tree with no comparison bases and with the code commit being attributed. An unbound validator refuses. Where changes require staging, preparation and validation use a private index; prepublication refusal or an exception during that interval leaves the worktree index untouched. Prepared `.gitignore` bytes are restored only when current bytes are provably those owned by preparation; concurrent external edits are preserved. When restoration returns normally, the original exception is re-raised; the unlink, write or chmod performed during restoration can themselves raise and mask it. This is the implementation boundary, not an unconditional original-exception guarantee.

Publication constructs a commit from the validated tree, uses a conditional branch update, and verifies the resulting commit tree. The implementation reads the parent HEAD inside `_publish_validated_tree`, after validation, and subsequently reads the branch name; it does not carry a ref/HEAD observation captured at validation into this helper. Thus exact tree publication is supported, while the inherited stronger claim that the branch must still point where validation saw it is not established by this local implementation. Publication and subsequent real-index preparation also lie outside `_prepare_stage_validate`'s restoration handler; the broad claim of rollback for every possible adoption exception exceeds that interval's source evidence.

`carryover.py` retains the legacy recovery planning account, but apply refuses both a converted target (directing file-based knowledge ingestion) and an unconverted target unconditionally with the central conversion message. The read plan stays separate; no never-converted write exception remains. This refusal check is not acquisition of a lock for the duration of carryover, and carryover authority remains separately checked.

An existing legacy root first answers `legacy-format` with conversion guidance; it cannot be adopted until it converts. An unattributed root converts in place before adoption; an official legacy line converts as one new leaf's first memory change and lands through normal converted validation. The command, read-only legacy database reader and conversion-format version 1 remain permanent because other clones and machines can retain unseen unconverted lines.

### Index and retained logical representation

`knowledge_index/tree.py` owns captured identity and matching bytes. Directory capture copies the real index with its timestamp, clears assume-unchanged and skip-worktree flags in the scratch copy for present paths, and preserves an absent skip-worktree path so sparse checkout does not become deletion. Its bytes then come from the committed blob. An ordinarily absent path is captured as deleted. Indexed bytes are checked against captured blob IDs; three unstable captures lead to refusal. These source predicates establish construction, not an execution verdict for any current worktree.

`build.py` retains both each history file by path and the merged history of an owner, including reopened-leaf attempts. History rows in the index retain their file path. `history_row(id)` returns all matching rows, since separate closed files may reuse an ID; the caller disambiguates by path.

`query.py` answers exact-path entries, invariant/family knowledge, incoming relationships, history by owner/subject/ID, proof entries, live invariants without proof, directory/subtree entries, direct-directory entries, live entry paths, path-target links and record enumeration. Directory prefixes respect boundaries: `dash` does not include `dashboard`. Live entry paths are returned once per entry, so repeated source paths can occur; this is an entry population, not distinct-file enumeration. Family governance checks the path, its ancestors and root route `.`. The root family route therefore covers root-level and deep paths. The list of live invariants without proof is information, not a gate: admission can use criteria other than a proving test.

`projection.py` maps text identities to deterministic UUID5 identities in a fixed namespace and derives revision identity from `<ID>@<revision>`. One text record contributes one revision in the selected tree. Projected provenance carries origin and record file, with a fixed epoch placeholder that must not be interpreted as recording time. Revision seals use the store's own invariant/family payload digest over the projected cells. Retired invariant/family records are omitted from the logical live representation, along with affected membership/realization rows; their records, entries, links and history remain visible in `ix_*`. Missing referenced invariants similarly leave their relationship visible in the index while preventing projection into referentially constrained logical tables. Proofs, routes, links, history and facet records use direct index tables rather than invented logical tables.

`knowledge/schema.py` owns one composed schema, its manifest, exact DDL, indexes, immutability triggers, required features and fingerprint pin. The surviving eight logical tables are repository, invariant, invariant revision, family, family revision, family member, source anchor and realization claim. The effective declaration remains `ar-knowledge-sqlite/v9`, `user_version = 9`; this is one current declaration, not a selectable generation registry. Other versions refuse with conversion guidance, rather than migration, repair or guessed interpretation. The index creates the logical tables it fills. Database triggers express immutability even for writes outside the usual operation. The pin checker rejects changed composition and explicitly directs callers not to repin the constant merely to accept a changed schema.

`connection.py` opens read-only handles with a one-second busy timeout. Its schema inspection checks the declared version, required tables, column order and required trigger names; these checks should not be inflated into a claim that opening recomputes every aspect of installed DDL. `store.py`, `families.py`, `memberships.py`, `records.py` and `view_source.py` provide the retained read vocabulary. Store identity enumeration returns every invariant or family identity in the bound namespace, ordered by its identity column, without a policy filter or computed count. Families are peer subjects, not inferred from invariants. The view reader reads membership from its dedicated table; it supplies recorded facts while application views own selection and classification. SQL ordering in row queries should not be confused with ownership of presentation policy.

`logical.py` canonicalizes declared tables, including empty tables, in manifest order, rows in primary-key order and columns in declared order, decoding typed JSON so equivalent JSON serialization does not change logical identity. It excludes physical database layout, database file location, journal/header state, mtimes, Git locations, ledger/cache state and rendered views. This exclusion does not mean authored path values or projected provenance fields disappear from the logical rows.

### Recorded reads, anchor observation and comparison

`knowledge/read.py` owns finite recorded-scope selection and whole-item paging. Directly containing families are frozen before membership expansion; families discovered through admitted members form an advertised, untraversed frontier rather than an invitation to recursive expansion. Identity selection does not choose a latest revision by insertion time or display version. Items have a declared stable order: invariant revisions, family revisions, memberships, realization claims, then advertised family links. Paging preserves the selection total on every page, reports cumulative emitted items separately, and leaves the current slice size in `len(page.items)`. A too-small budget cannot split an indivisible item or advance the position.

The application seam binds the read-only selected snapshot, permits a task-free baseline, and treats a cursor as a binding rather than a newly chosen scope. `read_refusals.py` keeps absence, snapshot mismatch, incomplete selection and budget failures distinct. An absent identity, a path without registration and a path invalid as a selector are different facts. Inherited path-selector intent admits literal `*`, `?` and `[` while refusing leading `:`; this proposal does not independently re-establish the entire selector-validation path. Registration absence never means no obligation or no semantic impact. `with_proofs=True` changes the path refusal wording to realization-or-proof claims for family-complete leaf reading; ordinary recorded-scope wording remains the default.

`read_anchors.py` observes recorded attribution against the requested tree, preserves its identity on every outcome, and never supplies content, reanchors ranges, searches for a replacement locator, or substitutes HEAD, a branch, a worktree or Markdown. No requested tree is a supported `not_requested` state. A resolver probes tree availability when constructed, not once per anchor. Exact symbols carry all defining extents; file locators carry no resolved range. An exact recorded blob with an out-of-bounds or unreadable line range remains `exact_recorded_blob` but has no resolved range and states why. Blob identity and usable locator extent are deliberately separate facts.

`read_anchor_memo.py` owns bounded, thread-safe LRU storage; `read_anchors.py` owns admission of successful content answers. Keys include repository root and complete object IDs, and grammar identity for parsed definitions. Refs and abbreviations are not admitted. Definite path absence can be remembered as an immutable tree-content answer, but object-store availability is not such an answer. Two named residuals remain: a tree still present after a previously read blob becomes unavailable may receive remembered blob content, and resolver-less observation skips the tree probe. The inherited account identifies curator ingest as the production resolver-less caller and says it measures membership in the same run; that caller-specific assertion is retained as historical intent rather than freshly adjudicated here.

`tree_observation.py` owns the shared source vocabulary and probe seam. `TreeChange` preserves the raw Git path, status, renderability, mode-change flag and reason for unknown content. Unavailable measurement differs from an empty measured change set. `TreePaths` checks agreement when entries are supplied, and requires partial state when unrepresentable paths are supplied; it does not require entries for every nonempty path-only value. Non-UTF-8 pathnames remain preserved separately and make the report partial. The display carries this limitation beside counts. The inherited production measurement uses delimiter-safe `git diff --raw -z --no-renames`, with acquisition owned by `application/review_source_inventory.py` rather than a second display-layer measurement.

`diff_attribution.py` owns pure arithmetic over that one supplied measurement: attributed, confirmed unregistered and undetermined are disjoint path buckets. Unchanged registered paths are context, not changes; multiple resolved links count a changed path once. Unresolved registered mappings remain visible rather than becoming absence. Attribution requires recorded bytes at the recorded path. Confirmed absence requires every required side to license it: `inspected` and independently established `known_empty` do, `unavailable` does not, and no supplied sides do not. The same `licenses_absence` predicate serves partitioning and the acquisition owner's subject-scope decision. A known selected-subject link establishes selected attribution; exclusive-outside labeling additionally requires complete subject scope. Unmeasured source population has no denominator, not zero. Non-text-carriable paths remain outside the reported path denominator with an explicit partial-measurement limit.

`diff_display.py` retains the shared seams through re-exports and carries one source observation with its partition. The former `attributed_paths(comparison)` was deliberately removed without replacement; `SourceAttribution.attributed_paths` is the measured partition's property, avoiding unchanged mapped context being counted as change.

`requirement_endpoint.py` locates the owning task under the coordination task plane and delegates packet/version resolution to `requirement_owner.py`. No coordination root and an invalid repository directory name produce named unresolved endpoint states. When the task root can be located it remains attached to an unresolved owner answer. Packet confinement and packet identity belong to the delegated owner, not an assumed absence of checks in this root helper.

Approval reads only `requirements/manifest.json` in approved-requirement-corpus format and its packets list. It reports the highest approved integer `v` version for the stable ID, no approved entry, or unknown with a reason for unreadable/missing/malformed input. `newer_than` requires comparable versions and a strictly higher approved version; unknown approval never supplies a newer-version trigger. Requirement links resolve endpoints; reconsideration first resolves, then checks approval at the resolved root, and unresolved endpoints trigger nothing.

The manifest read records the digest of exactly its read bytes, absence or named read failure. Packet observation is delegated: `tasks/task_intent.py` records task-root and packet-locator resolution, confines the Markdown packet, reads its bytes once and verifies stable ID/version. Outside a recording context these observations do not accumulate. The mandatory gate evaluates inside a recorded-read block and keeps that read set with the verdict. Reuse rechecks locator/existence observations before byte identities, so a retargeted locator invalidates reuse even for identical target bytes. These mechanisms are source contracts, not a fresh test result.

### Conversion, structural crossing and census

`conversion/convert.py` builds a conversion from memory files, the legacy database, code objects and pinned conversion version `1`, with the paired code commit additionally supplying the declared fallback for cards missing an anchor commit. This fallback is a specific conversion rule, not authority to add other approximations. A tree already holding `knowledge/layout.json` is a no-op. Unsupported conversion versions refuse; whole converted-tree validation occurs before results are returned for writing. A refused conversion writes nothing.

`cards.py` transforms legacy metadata/history and citation-table presentation into converted cards with one Evidence section and escaped marker-shaped text. `citations.py` resolves targets using the declared extractor/range/file rules and keeps unmatched anchor text in `Reference.note`; covered ranges add no redundant target. `code_objects.py` reads exact code-object identity rather than a worktree for conversion, enumerates abbreviated commit-prefix candidates, and distinguishes a missing blob from a Git failure: exit 1 or a non-blob returns false, other command failures raise `CodeObjectError`, and timeout propagates. A prefetched blob is answered from the local content cache, so this predicate should not be described as an unconditional fresh availability probe.

`legacy_db.py` is a read-only export boundary rather than a retained canonical writer. It exports invariant/family heads with derived IDs, preserved legacy identity and origin, revision position in predecessor chains, empty family routes and legacy-unassessed admission. Realizations retain recorded blob/locator identity and compute content from that recorded blob, preserving visible staleness; derived-ID collisions refuse by name. `inputs.py` owns input acquisition and finished-file publication.

`base.py` converts an unconverted before side at its own paired code commit and the after side's pinned version, so mechanical conversion is not attributed as semantic change. Conversion and crossing are separate routes. `crossing_sync.py` moves applicable leaf no-impact markers into `onboarding_trace.markers`, converts required sides and structurally merges. Every managed converted-memory merge uses this structural path, even when all sides already are converted; all-unconverted merge remains the ordinary non-crossing case. Version disagreement refuses. Commit validation remains the managed merge consumer's responsibility.

`crossing.py` merges Markdown by lines, sidecar references by number, realizes/proves by entry ID, and records/other JSON by fields. Mechanical anchor fields are blob, content and line numbers. Authored-versus-mechanical decisions preserve the authored side whole; both-mechanical changes choose incoming; deletion defeats a merely mechanical modification. Differing authored edits remain curator conflicts. Reference alignment moves prose markers together with their reference mapping rather than requiring manual curator renumbering. Conflict markers are explicit validator-refused JSON, not silent acceptance of one side; record conflict resolution belongs to the writer and increments beyond the higher revision. Crossing does not re-resolve anchors: later reads report staleness.

`card_authoring.py` is a distinct converted-card reference authoring route using the code working tree. Citation rows become evidence lines and resolved sidecar references; an existing trailing reference number reauthors that number, placeholders remain prose, and missing sidecars can be constructed. Removing unreferenced entries is limited to the explicitly named card. Invalid sidecars, conflicting reuse of a cited number, and adjacent merged tables involving citations produce named card refusals. Every card is prepared before the write phase, but passing cards are written even when others were refused. Markdown and sidecar are consecutive `write_text` calls; this is not a demonstrated atomic pair or batch transaction. Cards without citation tables are untouched except the named-card pruning case.

`knowledge_census/inventory.py` mechanically inventories pinned code and memory commits through Git objects. It identifies sources/artifacts and nearest governing overview routes, excluding generated caches/hidden directories; it does not read source content or author semantic claims. Unreadable baseline commits/trees refuse without an inventory. `writer.py` checks census candidate files against the existing base before publication, refuses unconverted memory and uses per-file atomic writes. Initial creation writes inventory first and baseline last as its commit point; inventory-only interrupted creation is refused by validation and can be completed by retry. This is not an all-files transaction. Bounded census measurement/reporting belongs to memory-quality owners; the earlier migration-to-canonical-store writer is retired.

`durable_evidence.py` defines `<task_root>/notes/reports` once because evidence must survive cleanup of enclosure/worktree-group directories. Single-artifact publication retains its one-plain-filename rule; directory-shaped comparison generations derive their root here instead of inventing a second durable location.

## Invariants And Boundaries

Text authority, derived indexing, validator integrity and lifecycle publication are distinct responsibilities. The index cannot author an obligation, its complete state cannot certify the whole tree, and recorded proof absence cannot become a delivery gate. Authored scope/family relationships are not inferred from folder proximity, names or symbols. A recorded absence, an unavailable observation, an unsupported locator, stale bytes and an invalid selector are separate outcomes.

Logical identity is independent of database storage location and physical serialization, while recorded path/provenance values remain semantic inputs. One pinned schema and store-owned revision seals replace the retired generation-dispatch account. Read-only handles prevent dataset repair during reads; no fallback generation or working-tree substitution is authorized by these read contracts.

Source measurement and attribution share one population and one absence predicate. Partial or unavailable observations retain their limits, and unmeasured counts are not fabricated as zeros. Snapshot/cursor mismatch cannot return a page assembled from mixed revisions. Exact recorded blob identity does not by itself establish a usable line-range locator.

Converted adoption requires validation and refuses legacy-format cards independently of accepting drift. Legacy carryover does not write converted targets. Structural crossing resolves mechanical differences under declared rules while preserving authored conflicts for the curator. Prevalidation preparation, conditional ref publication, per-file atomic publication and multi-file rollback are different guarantees and must be described at their actual scope.

Current review retains curator-owned assessments/evidence and their authority availability. Detection signals, verification observations, evidence claims and the removed authored-effects matrix remain unavailable without measured counts. Proof entries and worklist history retain their own answers; neither substitutes for a retired canonical supporting-record channel. No cross-repository authority contract is established by this overview merely because lifecycle helpers address external memory or readers refer to code objects.

## Historical And Verification Limits

The retired SQLite account remains provenance: insert-only sealed revisions; shared post-insert lineage checks evaluated before writes; family identity and revision graphs; recorded anchors with identity-plus-digest removal; exact membership pairs with both read directions and stale-caller removal; anchored realization transactions; shared endpoint checks; typed operation/table refusal context; schema fingerprinting; and lock-guarded mutation, copied candidates, publication, portable roundtrips and changeset merging. These responsibilities explain earlier intent but do not authorize reinstating their deleted writers.

Named historical limits remain explicit. The former fifteen-trigger account disclosed a `family` identity immutability gap; its old witness and exact former enforcement are not re-established by the current eight-table schema inspection. The former detection input identity included namespace/route/policy/extractor/vocabulary versions, declared inputs, per-side digest/tree/root/task/selector binding and the run ID. Its digest deliberately identified an execution as well as inputs; the run-independent-input-digest question remained open, and the module did not select which run a scope should report. Detection and observation-row codec owners are retired; the old extraction/re-export account through `evidence_records` is historical, not a present public codec door.

The former registered-scope account required exact declared datasets, exact changed-path anchors, side-specific membership and only the declared composition policy, independent of R07 retrieval/paging. It refused named unresolved inputs rather than silently constructing a partial scope, and inferred no membership from proximity. Its current owner is not re-established here; preserve it as inherited semantic intent rather than claim the retired module executes it.

The KS-L23 repair account remains historical: old-side primary-key selection for changeset deletes/updates; post-replay precommit route-cycle refusal; detection identity separation for multiple coverage items; and corrections to envelope registry, generation-wrapper and citation-schema documentation. Its append-only selectable-generation policy belongs to that retired substrate. Its pyright lesson remains a reporting limit: broad and scoped invocations were not interchangeable evidence, and claimed repairs were described as real types rather than suppressions. Historical registry sizes, schema counts and uncommitted-worktree statements describe their old bases, not this checkout.

The anchor-reuse incident remains a named historical warning: a receipt could name `other` while the stored realization referred to `resolve_budget`; the former repair used a shared stored-anchor read and refused mismatched supplied path/blob/locator before planning, while preserving matching reuse, allocation-per-creation, revision-keyed anchor identity and separate claim identity. The current former-owner reader/caller pair is not established by this proposal, so its preservation is historical intent, not a new acceptance claim.

The inherited curator candidate-source/progression account is not resolved to a present owner here. It described exact working-source capture and progression of only draft candidate code after matching predecessor receipt and logical dataset under the existing lock, while preserving strict opening, knowledge/allocation state and the original before half. Keep that named continuity intent and its receipt-to-resolution sharing as unverified historical claims; do not infer a replacement operation or whole-call-path absence from this uncertainty.

Earlier claims that the installed runtime never reached conversion/index/census before MIK-R37 describe pre-cutover timing, not present reachability. The old publication sink's `database_frozen` claim names a retired `knowledge/publication.py`; no present sink is established here from that old name. KS-L15's manifest repointing was a citation-only account, not a route behavior change. Superseded evidence-table formatting and numbered references are provenance managed separately by the parent.

Historical test passes, counts, performance figures (including the anchor memo's approximately 1.3–1.6 seconds to 0.3 seconds), golden-digest claims and delivery statements are inherited observations, not fresh acceptance. This proposal examined all supplied card prose and bounded source witnesses at the named checkout. It ran no product code or tests and makes no execution, publication or certification verdict. Old witnesses not examined or no longer present remain explicitly historical/uncertain.

## Evidence
- Retained reference account (no fresh execution or acceptance inferred): A missing object against a Git failure. [2]
- Retained reference account (no fresh execution or acceptance inferred): Entries at or under a directory, and of the files directly in it. [5]
- Retained reference account (no fresh execution or acceptance inferred): Live entry paths, links to a path, and every record of a kind. [6]
- Retained reference account (no fresh execution or acceptance inferred): The shared link query `_incoming` delegates to. [7]
- Retained reference account (no fresh execution or acceptance inferred): The store's own seal on each projected revision row. [8]
- Retained reference account (no fresh execution or acceptance inferred): The format bump that rebuilds v1 caches. [9]
- Retained reference account (no fresh execution or acceptance inferred): Every record ID of one kind, sorted; since MIK-R29 the reader's `records_of_kind` is built on it. [10]
- Retained reference account (no fresh execution or acceptance inferred): The absence refusal, naming proof claims when the leaf read asks. [13]
- Retained reference account (no fresh execution or acceptance inferred): The owner's rule: answers only, keyed by complete ids, availability never remembered, and the two residuals. [16]
- Retained reference account (no fresh execution or acceptance inferred): The memo module's tables and admission test. [17]
- Retained reference account (no fresh execution or acceptance inferred): The bound-checked line-range observation. [18]
- Retained reference account (no fresh execution or acceptance inferred): The symbol observation carrying every defining extent. [19]
- Retained reference account (no fresh execution or acceptance inferred): **The partition arithmetic and its four rules, with the one predicate behind both the bucket and the exclusive-outside label.** [20]
- Retained reference account (no fresh execution or acceptance inferred): **The shared observation vocabulary and its two construction rules.** [21]
- Retained reference account (no fresh execution or acceptance inferred): **The display seam: one observation, the carried partition, the two established omissions, and the deliberate non-replacement.** [22]
- Retained reference account (no fresh execution or acceptance inferred): **The exported root, and the shipped value it returns.** [23]
- Retained reference account (no fresh execution or acceptance inferred): The single-file publication the export deliberately does not replace. [24]
- Retained reference account (no fresh execution or acceptance inferred): **Its first consumer, which derives the whole generation layout from it.** [25]
- Retained reference account (no fresh execution or acceptance inferred): The per-file detail for the module that gained the export: the durable root and the shipped value it returns. [26]
- Retained reference account (no fresh execution or acceptance inferred): The per-file detail for the module that gained the export. [27]
- Retained reference account (no fresh execution or acceptance inferred): Current record owner marks retired classes unavailable. [28]
- Retained reference account (no fresh execution or acceptance inferred): Real authority availability and unmeasured count contract. [31]
- Retained reference account (no fresh execution or acceptance inferred): The two operations and twelve codes the merge added to the shared vocabulary. [39]
- Retained reference account (no fresh execution or acceptance inferred): **The read half's selection policy: `F0` frozen before membership expansion, the advertised-and-untraversed frontier, and the declared item order.** [41]
- Retained reference account (no fresh execution or acceptance inferred): Whole-item paging over an already-selected scope. [42]
- Retained reference account (no fresh execution or acceptance inferred): **The corrected page counts: the declared total on every page, the walk's cumulative figure, and the slice size in `len(page.items)`.** [43]
- Retained reference account (no fresh execution or acceptance inferred): The count model that refuses its own arithmetic contradiction at construction. [44]
- Retained reference account (no fresh execution or acceptance inferred): **The three genuinely different facts of a path refusal, and the corrected predicate (`*`, `?`, `[` admitted; leading `:` refused).** [45]
- Retained reference account (no fresh execution or acceptance inferred): The read's refusal vocabulary, one factory per observable failure point. [46]
- Retained reference account (no fresh execution or acceptance inferred): **The one decoder a read page and the logical digest share.** [47]
- Retained reference account (no fresh execution or acceptance inferred): The read's path lookup, which is how a path seed selects. [48]
- Retained reference account (no fresh execution or acceptance inferred): The edge lookup the directly containing family set is derived from. [49]
- Retained reference account (no fresh execution or acceptance inferred): The read's composition seam and its three boundaries (read-only handle, task-free baseline, cursor-as-binding). [50]
- Retained reference account (no fresh execution or acceptance inferred): **The nodes that measure the requirement's stopping rule, the corrected counts and the three path facts.** [51]
- Retained reference account (no fresh execution or acceptance inferred): The shared case harness registered as `contract:common-base-merge-cases`, and its evidence node. [52]
- Retained reference account (no fresh execution or acceptance inferred): The retained logical body encoder and logical digest operate with the one composed CURRENT_GENERATION; its structural guard checks the pin, and the store opener is read-only. No deleted generation registry supplies these current owners. [65]
- Retained reference account (no fresh execution or acceptance inferred): The two portable operations and the one code they added to the shared vocabulary. [68]
- Retained reference account (no fresh execution or acceptance inferred): The candidate list is the path and every ancestor, nearest first, ending with the root route `.`; `families_governing` matches routes against exactly this list. [84]
- Retained reference account (no fresh execution or acceptance inferred): A family routed at the root governs a root-level file and a deep file. [85]
- Retained reference account (no fresh execution or acceptance inferred): **Every invariant identity the namespace records, ordered by the identity's own column, with no filter and no count.** [88]
- Retained reference account (no fresh execution or acceptance inferred): **The same enumeration for the surface's other admitted subject kind.** [89]
- Retained reference account (no fresh execution or acceptance inferred): The row decoder both new reads use, so a listed identity is a decoded identity rather than a column tuple. [90]
- Retained reference account (no fresh execution or acceptance inferred): The consumer's entry half: the catalogue enumerates every recorded identity of both snapshots under the recorded namespace — no per-subject comparison runs and no subject is dropped to imply a smaller population (`ICR-R09@v1`). [91]
- Retained reference account (no fresh execution or acceptance inferred): **The status-bearing change: the raw path as the address, Git's status, the renderability and the reason an unknown is unknown.** [95]
- Retained reference account (no fresh execution or acceptance inferred): **The observation's two renderings and its two honesty rules: paths and entries cannot disagree, and an unrepresentable path implies a partial observation.** [96]
- Retained reference account (no fresh execution or acceptance inferred): **The advertised command, now the delimiter-safe interface the measurement itself reads.** [97]
- Retained reference account (no fresh execution or acceptance inferred): **The expansion detail that states a partial observation's own limit instead of only counting the paths it could carry.** [98]
- Retained reference account (no fresh execution or acceptance inferred): **The probe this route's expansion is reached through, now a one-line delegation to the review's own observation.** [99]
- Retained reference account (no fresh execution or acceptance inferred): Source-path observation cases moved with meaning preserved. [100]
- Retained reference account (no fresh execution or acceptance inferred): The package map. [101] [106]
- Retained reference account (no fresh execution or acceptance inferred): The captured-state key. [102]
- Retained reference account (no fresh execution or acceptance inferred): The build, which names every failing file. [103]
- Retained reference account (no fresh execution or acceptance inferred): Retired records are left out of the projection. [104]
- Retained reference account (no fresh execution or acceptance inferred): The cache refuses a Git working tree. [105]
- Retained reference account (no fresh execution or acceptance inferred): The pure conversion, its version pin and its validation. [107]
- Retained reference account (no fresh execution or acceptance inferred): No anchor text lost: it is kept in the note. [108]
- Retained reference account (no fresh execution or acceptance inferred): The read-only reader. [109]
- Retained reference account (no fresh execution or acceptance inferred): Rule 7 for any comparison consumer. [110]
- Retained reference account (no fresh execution or acceptance inferred): Rule 8's item rules and conflict markers. [111]
- Retained reference account (no fresh execution or acceptance inferred): Rule 8's steps. [112]
- Retained reference account (no fresh execution or acceptance inferred): The two proof lookups. [113]
- Retained reference account (no fresh execution or acceptance inferred): The card authoring's entry. [114]
- Legacy carryover apply refuses converted targets and unconditionally refuses unconverted targets; planning remains a read. [116]
- Retained reference account (no fresh execution or acceptance inferred): The index keeps each history file by path. [117]
- Retained reference account (no fresh execution or acceptance inferred): Two tables with no blank line between them are refused when either holds citations. [118]
- Retained reference account (no fresh execution or acceptance inferred): The capture copies the index with its time. [119]
- Retained reference account (no fresh execution or acceptance inferred): The governed-artifact row and the exact consumer list the L5 leaf registered in the shared catalog, which this leaf extended by two modules. [120]
- Retained reference account (no fresh execution or acceptance inferred): The registry rows this leaf added: two integration lane rows. [121]
- Retained reference account (no fresh execution or acceptance inferred): The registered support artifact the two integration lane rows land in, by its own artifact id. [122]
- Retained reference account (no fresh execution or acceptance inferred): The second registered support artifact those rows land in, by its own artifact id. [123] [125] [127]
- Retained reference account (no fresh execution or acceptance inferred): The third registered support artifact those rows land in, by its own artifact id. [124] [126] [128]
- Retained reference account (no fresh execution or acceptance inferred): The reconsideration step resolves the endpoint and asks for the approval. [129]
- Retained reference account (no fresh execution or acceptance inferred): A kept gate verdict is served only when no recorded observation changed. [130]
- Retained reference account (no fresh execution or acceptance inferred): The manifest lookup returns the highest approved version. [131]
- Retained reference account (no fresh execution or acceptance inferred): A requirement endpoint triggers only on a newer approved version. [132]
- Retained reference account (no fresh execution or acceptance inferred): The gate's warm pass becomes the refusal when a packet locator is retargeted to identical bytes. [133]
- Retained reference account (no fresh execution or acceptance inferred): The endpoint's state, code, detail, task root and key. [134]
- Retained reference account (no fresh execution or acceptance inferred): The task root, or none for a repository that is not one directory name. [135]
- Retained reference account (no fresh execution or acceptance inferred): The resolution: no root, a root outside tasks, or the owner's answer; no packet is recorded here. [136]
- Retained reference account (no fresh execution or acceptance inferred): The approval answer and the comparison with a version. [137]
- Retained reference account (no fresh execution or acceptance inferred): The manifest read records the bytes, an absent manifest or a failed read. [138]
- Retained reference account (no fresh execution or acceptance inferred): The approval lookup with its three states. [139]
- Retained reference account (no fresh execution or acceptance inferred): The latest approved version of one ID. [140]
- Retained reference account (no fresh execution or acceptance inferred): The owner the packet question is handed to. [141]
- Retained reference account (no fresh execution or acceptance inferred): The owner records the two resolutions and the packet's bytes. [142]
- Retained reference account (no fresh execution or acceptance inferred): An unreadable baseline is refused. [143]
- Retained reference account (no fresh execution or acceptance inferred): Every write is checked, then written atomically. [144]
- Retained reference account (no fresh execution or acceptance inferred): Converted first adoption preserves attributed-history precedence, lists legacy cards and refuses them without a drift waiver. [145]

- Knowledge text is authority; the retained package owns derived schema/codecs/reads rather than canonical writers or approval. [146]
- Converted baseline validates a paired immutable tree; publication reads its comparison parent after validation. [147]
- Adoption distinguishes legacy-card/validator/drift refusals and drift acceptance cannot clear the first two. [148]
- Carryover refuses converted targets and checks cutover refusal rather than acquiring a lock. [149]
- Captured bytes match a disposable captured tree; sparse-checkout omission is treated distinctly from deletion. [150]
- Parser completeness is distinct from validator integrity and history files are retained by path. [151]
- History lookup returns every matching path-bearing row and proof absence is informational. [152]
- The cache refuses a Git-worktree location and evicts by age/size around temporary-file publication. [153]
- Projection uses deterministic identities, store-owned seals and retains retired/unprojectable facts in direct index tables. [154]
- One composed v9 schema and fingerprint pin replace generation selection; current index layout is v3. [155]
- Read handles and identity enumeration retain their separate boundaries. [156]
- Selection freezes directly containing families before expansion; paging preserves total and cumulative counts. [157]
- Anchor observation retains two named availability residuals and exact-blob identity can lack a resolved range. [158]
- Attribution requires a measured denominator and licensed side inspection; no inspected sides license no absence. [159]
- Path/entry equality is conditional on supplied entries, while unrepresentable changes require partial state. [160]
- Requirement approval records exact manifest reads and distinguishes approved, not approved and unknown. [161]
- Packet owner confinement and recorded locator observations support gate memo invalidation before byte rechecks. [162]
- Converted card authoring prepares all cards, reports refusals, then writes passing Markdown and sidecar files consecutively. [163]
- Legacy export preserves recorded anchor identity; crossing keeps authored conflicts explicit and separates mechanical edits. [164]
- Census validation precedes per-file atomic writes; baseline-last creation has an explicit interrupted-creation state. [165]
- Retired supporting-record channels remain unavailable without fabricated counts or proof/worklist substitutions. [166]
- Durable task reports have one shared root, distinct from the single-file publication route. [167]
