# mcp/src/agents_remember/application/knowledge_curator_ingest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_curator_ingest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T14:20+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l43-ar`, uncommitted; base `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
| lastVerifiedCommitHash | `4ef4dddc9194930611db2b1dfbb6e02113f2226a` |
| lastVerifiedCommitDate | 2026-09-20T15:00:59+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

This is the curator's reachable ingest: the layer above `knowledge_ingest`'s write half. One
orchestrator hand-off list (revision 1's JSON entries) goes in; one admitted candidate batch and one
report come out. It owns every step between the list and the record — admit the destination, complete
each target path, read the identity that path really holds, verify the locator against those bytes,
observe each anchor against the recorded tree, author the governing routes, commit the whole list
through the closed write path, and report every entry's outcome so the run is auditable afterwards.

The module's first distinction is that three cases are never conflated. A ruling that carries no
target (`target: []`) is **skipped**, with the producer's own `disposition` and `disposition_source`
carried into the report, because there is no construct to cite and recording one would invent a claim
the producer never made. A non-empty target that does not resolve is **refused**, with the exact
reason, because the producer named a place the curator cannot verify. An entry is **committed** only
when every one of its targets resolved, verified and observed. Nothing the operation can *read* makes
it raise: unreadable identities, unresolvable paths and unverifiable locators all arrive as typed
refusals, because a traceback would break the promise that every entry's outcome is reported.

Why it matters: this is the only place where an unlanded draft's citations become recordable. A leaf
cites the code its own line is producing, so the tree a target is resolved against is the leaf's own
code work branch tip rather than the enclosure's recorded base commit, while the run's **allocated**
identities carry no task, branch, baseline or label at all, and its **derived** citation identities are
keyed on the **repository's own namespace** — the stable half — and never on that base. The split is
what lets a leaf add and modify files and still cite them, and what keeps a stored identity usable from
any task, branch or later baseline.

**The API allocates a new truth's identity; a hand-off label is never an input to it.** An invariant
and its first revision are the two identities this module *allocates*: fresh `uuid4` values, minted
here and recorded in the candidate's own allocation journal under an **idempotency key** scoped by the
enclosure's task identity, so a repeat of one creation operation resolves to the identities it already
holds while two independent tasks that both numbered an entry `R-LOCAL` mint two distinct truths. A
citation's route, anchor and claim stay *derived*, because they are facts about a place and an edge
rather than about a new truth. The label is never an input to any of them: the anchor is keyed on the
allocated revision id, and the claim on its own two endpoints. Reusing a label therefore says nothing
about whether two entries represent the same truth — continuity across a task boundary is by
**explicitly naming the stored identity**, through the entry-level `invariant_id` or the target-level
`anchor_id`. This is the developer's 2026-09-20 identity ruling implemented; `notes/DISCLOSURES.md`
D-62 in the task tree records the defect it repairs.

It refuses to be a general citation tool: no symbol extractor, no onboarding writer, no export
builder and no widening to a third root. **Publication is no longer the curator's later act.** A run
that selects an `IngestPublication` publishes *the candidate it just committed* into the destination
the caller admitted, through the shipped publication owner, so an operator never has to re-derive a
namespace, a resolution or a digest by hand to reach it. The step runs here rather than in the caller
because this is the only place holding both facts publication needs: the admitted candidate
destination the admission already built, and the candidate's **live** identity, which the batch that
just committed has changed and which therefore cannot be supplied before the run. A run that selects
none behaves exactly as it did before publication existed and reports no publication; a batch that did
not commit is never published, so a caller is never handed a dataset change it did not make; and a
destination the caller did not admit is refused rather than overwritten. Its public surface is one
entry point, the publication selection, plus the vocabulary its report is read with.

## Code Commentary

### Logic

**The entry point, and what each mode returns.** `ingest_curator_list(contract_path, entries,
selection: IngestSelection) -> IngestReport` is the whole operation. `IngestSelection` carries the
four facts one run selects — `candidate_directory`, `authorization_ref`, `dry_run`, and the
`baseline` it forks from — grouped rather than passed as four trailing arguments, because the
candidate and the baseline are the two halves of one decision: a run that can name where it writes
without being able to name what it forks is how continuity was lost in the first place. `dry_run`
is a required member with no default, so every caller states which mode it is in. The operation
refuses a blank `authorization_ref` by name before anything is read (`_require_authorization`, a
`ValueError` — the operation's own input contract, not a per-entry refusal), loads the enclosure
contract, binds the two roots (`_roots`, which requires the recorded memory worktree), derives the
resolution trees and the coordination root's top-level names once for the run, then reads and plans
the list. `dry_run=True` returns the identical report with the commit withheld; the real path builds
the authorship envelope (`write_authorship` with `actor_ref` and `authorization_ref` both set to the
one required reference, `origin_refs=("curator-handoff:revision-1",)`), admits or creates the
candidate, and calls `_run`. One required authorization reference rather than two optional ones is
deliberate: "who authorized this" and "who authored it" stay the same admitted fact.

**Admission is resume, fork or create — and a refusal is the product's own.** `_admitted_candidate`
opens an existing candidate directory (`open_knowledge_candidate`) instead of initializing over it —
the bytes there are unpublished authored work — and otherwise forks the **selected baseline**
(`clone_knowledge_candidate` under a `CandidateBaseline` whose `expected_identity` is the baseline's
own `dataset_identity`, so a baseline that moved since it was selected is caught rather than silently
cloned from), falling back to an empty `create_knowledge_candidate` only when the run selected no
baseline at all. Forking is the continuity rule, not a convenience: an empty candidate holds only
this task's new entry, so the repository's existing invariants would be absent from it and the next
task would start from nothing. The repository namespace is **read, then derived**:
`_repository_namespace` returns the namespace the baseline's own dataset already records, and
`_repository_identity` derives one under the fixed `_INGEST_NAMESPACE` only as a cold-start fallback,
keyed on `contract.repo_name` rather than on the enclosure's recorded base commit. Deriving from the
enclosure made the namespace a function of the baseline — one repository ingested at a later baseline
was handed a *different* namespace and every revision recorded at the earlier one was stranded under
a namespace nothing would look in again — while two repositories that shared a base commit were
handed the *same* one. The `CandidateResolution` is read
from the enclosure's recorded pair rather than asserted: lane `draft-candidate`, the two trees, the
recorded base commits, and `task_ref` = leaf id or task name (`_resolution`). A refused or
identity-less admission returns a report with `batch_state="not_attempted"` carrying the product's
typed refusal.

**Reading the list: the list is data, and a refusal keeps what its entry already established.**
`_read_entries` accepts the parsed list or the path of the JSON file carrying it and parses no prose; a
non-list, a non-object entry, a missing `id` and a duplicate `id` are `ValueError`s raised before
anything is written. Per entry, `_plan_entry` reads the producer-side fields once
(`_EntryFields.read`, which also reads the two fields that make an entry a *revision* of something
already held rather than a first authoring: `predecessor_revision_ids` and `invariant_id`) and either
builds a ruling plan (no target at all) or plans every target; a
target that refuses returns immediately with the places its earlier targets already completed
(`_refused_targets`) carried in the refusal, so the report's entry accounting and its target
accounting describe the same run instead of a refusal erasing its neighbour. What makes two targets
the *same place* is `_TargetPlan.target_key` — the completed path, the locator kind, and, for a
symbol, its qualified name — so two symbols in one source file are two realizations and only a
genuine repeat is refused as `duplicate_target_path` (an inline code, not a module constant). The
completed path alone was the old key, which is why the second anchor of a file could not be recorded
at all.

**Completing a path: three recorded steps, and the identity is measured rather than restated.**
`_complete_target` asks exactly three places, in order: `<code_root>/<path>` against the code
resolution tree, then `<memory_root>/onboarding/<path>`, then `<memory_root>/<path>`. Membership is
the tree's own answer (`Trees.source_candidate.members`) and the answering root travels out with the
path so the blob is read from that same tree — a memory path's blob lives in the memory tree. `_member`
then reads the working bytes' blob id (`git hash-object --no-filters`) and compares it with the blob
the tree records (`_BlobIdentity.exact`); disagreement is the `recorded_blob_mismatch` refusal saying
the bytes about to be cited are not the bytes the resolution tree holds — what an uncommitted edit to a
cited file looks like — which is what keeps the recorded identity a measurement of the file rather
than a restatement of the tree's own answer. Spelling is settled before any tree is asked
(`_spelling_refusal`): an absolute path that points inside an admitted root is refused as
`path_inside_admitted_root_spelled_absolutely`, one that points outside as
`path_outside_admitted_roots`, a `..` segment as `path_not_confined_by_spelling`, and a leading `./`
is normalised and allowed through (`_confined`).

**A path that resolves nowhere is refused under one code, with the reason that is true of it.** The
code is `target_path_unresolved` and the reason opens with one of three names decided from the
recorded trees and the path's own spelling — never from `is_file()` on a live directory, because the
enclosure's cleanup deletes task-tree files and a reason that changed with them could not be
reproduced from the record the citation was written against. `top_level_entry_file_gone` when the
first segment is a real top-level entry of one of the two admitted trees; `third_root_out_of_scope`
when the path names something under the coordination root that neither admitted tree holds; and
`dependency_source_not_ours` when it names neither. `_coordination_top_level` reads the coordination
root's directory names once per run (minus the two admitted roots) and carries them, so one entry's
reason cannot depend on what still existed when that entry happened to be read.

**The locator is verified in the same act as the path.** `_locator` refuses a null locator as
`target_locator_missing` instead of promoting it to a whole-file citation (a path and the construct
inside it are one act, and "the whole file is the place" is a claim a producer must make explicitly),
refuses an unknown kind as `unsupported_locator_kind`, and dispatches `file`, `line_range` and
`symbol`. A range earns the reason true of *this* range, one code each: `line_range_not_integer_bounds`,
`line_range_not_one_based`, `line_range_not_ordered`, and `line_range_past_last_line` measured against
the recorded member's own line count. A symbol is the producer's bare name normalised into the model's
two-part locator: the name comes from `value` or `qualified_name` (`symbol_name_missing` when absent),
the language is derived from the recorded path's extension (`symbol_language_underdetermined` when the
table does not know it), markdown is refused as `symbol_target_is_prose` and a structured data file
under the same code with its own sentence, and the name must be *defined* in the file — a mention
earns `symbol_not_a_definition`, an absence earns `construct_not_in_named_file`.

**"Defined" is decided by the shipped parser, and by exactly one implementation of the rule.**
`_symbol_locator` hands the one file the path resolved to `bound_definitions` from
`memory_quality/style/citations/extents.py`, which asks `grammars.bindings` — the same tree-sitter
machinery the citation fixer, repair and migration paths use. That function checks the last segment of
a qualified name *and* every segment before it, so a genuinely nested construct resolves while an
invented prefix cannot borrow a real method's identity, and a name that occurs only inside a docstring,
a comment or a string is bound nowhere because the parser never binds it. There is no second definition
detector here: the regex tables, the comment/literal blanking and the per-language declaration patterns
that used to live in this module (`_defines`, `_declares`, `_code_only`, `_blank`,
`_PYTHON_DEFINITION`, `_CODE_DEFINITIONS`, `_PYTHON_LITERAL`, `_SCRIPT_LITERAL`, `_CODE_LITERALS`) were
deleted, because two notions of "a definition" in one tree can drift and nothing keeps them equal.
A consequence worth knowing: a language the shipped extractor has no grammar for — `shell`, `sql`,
`.pyi` — is now refused at this boundary as `symbol_language_underdetermined` rather than accepted, so
a symbol the read rail could never re-resolve is not stored in the first place. `_occurs` anchors at
the name's *start* only, so a file holding `resolve_budget_v` does contain the `resolve_budget` a
producer wrote — which is exactly why that case is refused as "not a definition" rather than "does not
occur".

**The anchor is observed against the tree its path resolved in, and a symbol is resolved.** `_observe`
builds the exact `SourceAnchorDraft` the write path will store (a real UUID from `_observation_id`, the
confined path, `GitBlobIdentity(object_id=resolved.blob)`, the locator) and hands it to
`observe_anchor(repository_root=resolved.root, tree_id=resolved.tree_id)`. `SourceIndexError` and
`OSError` raised by the rail stop being exceptions at this point and become
`observation_<ErrorClass>` refusals, and exactly one answer passes for every locator kind, the symbol
kind included: `exact_recorded_blob`, which the rail earned by reading the recorded blob out of the
requested tree and binding the symbol inside it. Every other answer is refused as
`observation_<answer>` with the rail's detail, so a stored symbol citation is one the read path can
re-resolve rather than one it can only refuse.

**The route leg runs through the primitives, not the batch.** The closed command union's only route
member names a *family revision*, and authoring a family per entry would fabricate grouping structure
the producer never declared — the one thing the curator must not do. So `_author_routes` runs first (a
route that cannot be recorded refuses the list by name, `route_not_recorded`, attributed to every entry
that named a route, before anything is committed) inside one transaction under
`store.exclusive_candidate_lock("author_route")`; each distinct scope is asked about first
(`routes.route_for_path`) because `routes.author_route` answers an existing path by returning that
row's id without writing, so the idempotent answer can be classified as authored or reused; and a
partial author rolls back. `_attach_routes` runs *after* the batch, because the governed row is the
anchor the batch wrote and the union carries no command that sets a route on an anchor: one transaction
under `set_governing_route`, one `routes.set_governing_route` per target, with the six states
`authored`, `reused`, `attached`, `authored-not-attached`, `ungoverned` and `refused` — `ungoverned`
being a fact about a target that named no route rather than a default.

**The commit is one batch for the whole list.** `_curator_entry` turns each plan into the write
module's `CuratorEntry` (invariant id, revision id, `display_version` `v1`, the one authored
applicability string, conditions carrying the producer's kind/disposition/disposition_source/evidence,
`declares_invariant` and `predecessors` carried from the entry, and one `CuratorCitation` per target
via `_TargetPlan.citation()`), and `_commit` calls
`commit_curator_entries`, which is one `curator_batch` through the closed write path. The invariant id
is the entry's own `invariant_id` when the producer named one, and otherwise the id the run's creation
operation was **allocated** — never one derived from the entry's local id: an entry that declares
predecessors is revising an obligation the repository already holds, so it must be able to say *which*
one, and the command list then omits the `AddInvariant` those predecessors make unnecessary. Without
that distinction every changed statement was mapped to `AddInvariant` followed by
`AddInvariantRevision` and refused with `batch_stale_precondition` ("expecting the existing invariant
to be absent") — a repository could accumulate obligations and never evolve one. The batch carries only
the plans this run must write: a replayed plan contributes no command, no row and no route attachment,
and its entry is reported by `_replayed_outcome` instead. The operation is all-or-nothing: a refused
batch means nothing was committed, every planned entry is reported refused with the batch's own code
(`batch_<code>`, or `batch_refused` when there was no result), and the batch's typed `KnowledgeRefusal`
travels beside the report in `batch_refusal`. The realization role the citation carries is the
producer's own stated role or the vocabulary's unclassified member, through `_authored_role`; the
ingest no longer states a role of its own.



**The realization role is authored by the producer, not inferred from the locator (this leaf's
CYCLE-04 repair).** The ingest used to state a role it derived from the locator's spelling —
`primary-authority` for a whole file or a range, `enforcement` for a symbol — through a helper named
`_role_for`. Locator syntax cannot establish that fact: a symbol can be presentation, propagation,
support or enforcement, and so can a range, so "where to look" was being stored as "what the thing
found there means", and the inference travelled inside a valid provenance envelope into later family
review and relevance filtering as though a producer had said it. `_role_for` is gone and nothing
replaces it as a default: `_EntryFields.read` takes the entry's own `realization_role` and
`realization_rationale`, `_plan_target_inner` passes those two semantic facts straight to the target it
plans — the frozen pair that used to group them (`_Authored`) was itself removed by this leaf, once the
creation id became the third fact a target needs, because `_Authoring` now carries exactly the facts
that decide a citation's identity and a role/rationale group that no longer owns anything would be a
second spelling of them — and
`_authored_role` answers with the stated role when the shipped vocabulary knows the word and with the
vocabulary's own `UNCLASSIFIED_ROLE` when nothing was stated. The stated word is validated against
the model's one definition of the vocabulary (`stated in get_args(RealizationRole)`, then
`cast("RealizationRole", stated)`) rather than against a second copy of the list kept here, and a
word the code does not know becomes **no role at all** rather than a stored semantic claim. The
authored rationale reaches `CuratorCitation.rationale` when the producer gave one, and
`_TargetPlan.citation()`'s own sentence about where the statement is realized is the fallback rather
than the substitute. The vocabulary was not widened to make this expressible: `UNCLASSIFIED_ROLE` is
the shipped `models/knowledge/graph.py` member for an unassessed edge, because an unclassified
realization is a claim about what is known. One consequence a reader should carry: revision 1's
hand-off shape names neither `realization_role` nor `realization_rationale`, so a list written to that
shape states no role and every realization it produces is recorded `unclassified` — the honest
answer, not a defaulted one.

**The report is the operation's other half, and a dry run is the same report with the commit
withheld.** `IngestReport` names the contract and candidate directory, the receipt path, the lane,
both trees and where the code tree came from, the repository id, the identity-derivation sentence,
every entry id it read, the three outcome tuples, the counts, the batch state and its digests before
and after, and the batch refusal. `IngestCounts` carries fourteen counts, of which `targets_completed`
(every place whose path completed, in a committed entry *and* in a refused one) and `locators_resolved`
(the places that reached the batch with a locator verified into the model's union) are deliberately two
different measurements. `EntryOutcome`, `TargetOutcome` and `RouteOutcome` are the per-entry,
per-target and per-route renderings. A dry run returns the identical shape from `_projected`, which is
arithmetic over the plans the run already built rather than a second construction of the batch, and its
route states are projected as `authored` because a dry run never read the candidate, so claiming
`reused` would be a fact it did not measure.

**The written-row count is corrected arithmetic, not a receipt length.** `_Run.written` returns zero
for a run with no committed batch, however much its route leg did, and otherwise adds the batch's
distinct `(table, record_id)` rows — the write path reports the anchor a claim cites a second time when
the same batch wrote it (D-42), so the raw receipt length overstates rows by one per citation — to the
route leg's own rows: one `route` row per scope **this run authored** (not per scope it answered) plus
one association per governed anchor the candidate accepted. `_counts` reads every count from the
outcome it counts rather than recomputing it; the mismatch, absent and unavailable observation counters
can only be counted from committed targets, which by construction carry `exact_recorded_blob` or
`unsupported_locator`.

**The identities this operation mints split in two: a new truth is ALLOCATED, a citation is DERIVED
(this leaf's CYCLE-01 repair).** `_identity` derives only the *citation* identities — route, anchor,
claim — as a `uuid5` under the one fixed `_INGEST_NAMESPACE` over **the repository's own
`repository_id`**, which identity it is, and a discriminator that names what the identity is *about*.
An **invariant and its first revision are no longer derived at all**: `_creation` hands each new
creation operation a fresh `uuid4` pair, so the ids carry no task, no enclosure, no branch, no baseline
and no label. Keying the derivation on the enclosure's recorded code base commit — which it did two
leaves ago — made one repository's knowledge a function of the baseline it happened to be read at; then
keying it on the entry's local label made two independent tasks that both numbered an entry `R-LOCAL`
one record. Both are gone. `ingest_curator_list` still resolves the repository identity before
planning, so one value reaches every mint in the run. For a target, `_target_identities` returns the
three citation ids as one `_TargetIdentities` value, because they are one decision applied to each
identity the write path needs; its `_Authoring` argument carries the two facts that decision depends on
— whose creation this citation belongs to, and which stored anchor it reuses. The **route** stays keyed
on the entry that names the path: a route is a scope that governs a path, so N anchors in one file are N
associations with the one route row rather than N rows. The **anchor** is keyed on the **allocated
revision id**, with the locator's qualified name (`within`) as the disambiguator *inside* that
creation — so `resolve_budget` and `other` in one `pkg/module.py` are still two records, two constructs
in one file are still two anchors, and two independent tasks citing one construct now mint two anchors
instead of aliasing onto one row. The **claim** is neither a scope nor a place but the authored **edge**
from one exact revision to one exact anchor, and it is keyed on exactly those two endpoints: a claim
keyed on the label minted ONE identity for two genuinely different realizations (same claim, same role,
same rationale, different `invariant_revision_id`), which production sync then refused
`duplicate_identity` on. Keyed on the edge, the same revision citing the same anchor is the same claim
(so a repeat is an idempotent insert of one row), two revisions at one place are two claims, and one
revision citing two places is two claims.

**The retry key is a separate fact from the identity, and it is the one thing the enclosure scopes.**
`_retry_key(contract, entry_id)` joins the enclosure's own task identity — `_retry_scope`'s
`contract.leaf_id or contract.task_name`, which is the same value the candidate resolution reports as
`task_ref`, spelled once so the two cannot drift — with the entry's id inside that hand-off list. It is
an **idempotency key**: the question a retry asks, never an identity input. `_retry_scope` is what the
ruling permits enclosure identity to scope, and nothing else about the enclosure enters an identity.
`_content_digest` covers every fact the stored truth is made of — kind, statement, evidence, the
producer's disposition, and each resolved place with the locator that names the construct inside it —
so the key's content is checkable rather than assumed.

**Allocation is journalled, and the journal is what makes a repeat a replay rather than a second
truth.** `_read_allocations(paths.candidate)` reads the candidate-local
`curator-allocation-journal.json` (`_ALLOCATION_JOURNAL_NAME`) beside the shipped
`candidate-receipt.json`: an absent journal is the ordinary first-run case and reads as no records,
while a journal that is present and *cannot* be read is reported as `unreadable` and every entry that
would have to mint an identity is refused `allocation_journal_unreadable` — minting without knowing
whether this operation already holds an identity is exactly how a retry becomes a duplicate, so the
entry is refused rather than guessed at. `_creation` is the one decision point: a key the journal
already carries is this operation repeating itself and its recorded pair is handed back; a key it does
not carry is a new truth and gets fresh ids. An entry that names an existing `invariant_id` keeps the
producer's invariant and still allocates a revision, because each new revision is a new immutable record
with an identity of its own that references its predecessors. `_require_minted_content` then settles
the digest for a freshly minted pair and **refuses** `allocation_content_conflict` when a key the
journal handed back arrives with a different digest: one idempotency key names one creation operation,
and neither the stored truth nor the arriving entry is overwritten by the other. `_record_allocations`
writes **before** the batch — a run whose batch refuses has still *made* this operation's allocation,
and its retry has to resolve to it — and it writes only into the candidate admission already produced,
so it never creates the destination it names; the write is atomic and read back, and a run that
allocated nothing writes nothing, which is why a replay leaves the file alone.

**A repeat is recognised from the dataset, and reported as a replay.** The journal cannot know whether
the batch that ran after it was written committed, so `_with_replays` asks the candidate itself:
`_stored_revisions` reads every `revision_id` the candidate already holds, and any plan whose revision
is already there is marked `replayed`. `_run` then writes only the **fresh** plans — re-issuing a
replayed plan's commands would earn the batch's own insert-absence precondition, which is the right
answer to "write this again" and the wrong answer to "repeat the operation that already wrote it". An
all-replay run returns `_REPLAYED_BATCH_STATE` (`"replayed"`) with no batch at all, its routes seeded
into the ledger's `answered` side by `_replayed_routes` (so `routes_reused` tells the truth and the
written-row count stays a count of rows *this* run wrote), and each entry reported by
`_replayed_outcome` as **committed** with the identities it already holds and each route rendered
`reused`. The batch state is deliberately neither `refused` nor `changed`: nothing moved.

**A producer may name a stored anchor, exactly as it may name a stored invariant.** `_named_anchor_id`
reads a target's optional `anchor_id`: the stored `source_anchor` identity is then used verbatim and
**no anchor row is authored** — `_TargetPlan.declares_anchor` becomes false, `CuratorCitation.
declares_anchor` carries it into the write module, and `curator_entry_commands` skips
`AddSourceAnchor`, exactly as `declares_invariant` skips `AddInvariant` for a successor. Re-declaring a
stored row is refused outright by the batch, so "reuse a stored anchor" has to be expressible or it is
not expressible at all. The claim is still keyed on the pair, so citing a stored anchor from a new
revision is a new edge to a known place. A malformed value is refused per target as
`anchor_id_not_a_uuid` rather than at a schema, so the run continues to the next entry; omitting the
field authors a new anchor exactly as before.

**The report's own identity sentence says the rule the code follows, and that sentence is where the old
rule survived longest.** `IngestReport.derived_identities` is a public field a caller reads to
understand what an id means, and it described identity as `uuid5` over the enclosure's recorded code
base commit long after `_identity` had stopped following that rule — the sentence a verification round
was misled by. It now states the split: the invariant and its first revision are **allocated** by this
API, a fresh `uuid4` each, recorded in the candidate's allocation journal under an idempotency key
scoped by the enclosure's own task identity, so an independent task reusing a local hand-off label
mints a truth of its own while a repeat of one operation resolves to the identities it already holds;
a citation's route, anchor and claim are derived as `uuid5` over the fixed `_INGEST_NAMESPACE`, the
repository's own namespace identity, which identity it is, and a discriminator that names what the
citation is about. It states both halves of the negative as well: no allocated identity contains the
enclosure, the branch, the baseline or the label, and the derived half's stable component is the
repository namespace and never the recorded base commit. The module docstring carries the same split
and was rewritten with it. What makes the sentence checkable rather than aspirational is the guarded
assertion in `test_knowledge_curator_ingest_list.py`: the base commit must not appear in the field, the
field must name the repository namespace, and `_identity` is compared against the derivation itself
(`uuid5(_INGEST_NAMESPACE, repository_id|kind|discriminator|)`) rather than against a phrase.

### Conventions

- **One spelling per fact.** The three outcome words (`COMMITTED`, `REFUSED`, `SKIPPED`), the refusal
  codes, the route states, the observation answers and the three path-completion step names are module
  constants, so a reader of the report and a caller branching on it name the same words. Codes used
  once are inline strings at their use site (`duplicate_target_path`, `target_path_unresolved`,
  `route_not_recorded`, `batch_refused`).
- **Everything internal is a frozen dataclass with a leading underscore and a docstring stating the
  distinction it exists to keep.** The public surface is `__all__`'s nine names: `ingest_curator_list`
  is the operation, and the other eight are the outcome words and the report vocabulary a caller reads
  it with.
- **Refusals are values; exceptions are the operation's own input contract.** `_Refusal` before the
  batch and `EntryOutcome.refusal` strings in the report are the failure vocabulary; the raises are a
  blank authorization, a contract recording no memory worktree, a malformed or duplicated hand-off
  list, and a tree the recorded commit cannot name. Anything else that is not one of the citation
  machinery's named conditions propagates deliberately: a defect in this module is not a refusal, and
  dressing one as a refusal would be the same failure pointed the other way.
- **A new truth is allocated, a citation is derived, and the label is neither.** `_creation` allocates
  the invariant and its first revision as fresh `uuid4` values under an idempotency key scoped by the
  enclosure's own task identity; their ids are recorded in the candidate's allocation journal rather
  than computed from anything. `_identity` derives only the citation identities — route, anchor, claim —
  as `uuid5` under one fixed `_INGEST_NAMESPACE` over the repository's own `repository_id`, which
  identity it is, and a **discriminator that names what the identity is about**: the written path for a
  route, the **allocated revision id** for an anchor, and the **revision-plus-anchor pair** for a claim.
  `within` (a symbol's qualified name) is the disambiguator *inside* one creation, so a file with two
  constructs stores two of them; a range and a whole-file citation contribute no `within`, deliberately,
  so a range citation stays stable as lines move. A symbol's qualified name survives the file being
  edited above the definition, where a line number would not. The derived half's stable component is the
  repository and never the code base commit, because a namespace must not move with a baseline — see
  `_repository_namespace`, `_repository_identity` and `_identity`. Two runs of one list mint the same
  *citation* ids; a repeat of one creation operation returns the same *allocated* ids because the
  journal holds them, so a second run is a replay rather than a duplicate — see `_retry_key`, `_creation`
  and `_with_replays`.
- **The producer's vocabulary is carried, not re-derived.** `kind`, `disposition` and
  `disposition_source` travel into the report and into the revision's conditions unchanged; the ingest
  authors only the fields the list does not carry (version `v1`, applicability, the realization role)
  and says so in the report.

### Invariants And Boundaries

- **Three outcomes, never merged.** An entry appears in exactly one of `committed`, `rulings` or
  `refused`. A ruling is reported skipped with the producer's verdict carried, never committed as an
  obligation with no realization; an entry is committed only when every one of its targets resolved,
  verified and observed.
- **No readable input makes the operation raise.** Unreadable identities, unresolvable paths,
  unverifiable locators and the rail's raised boundary conditions all arrive as typed refusals in the
  report; only the operation's own input contract (and a genuine defect) raises.
- **The resolution tree moves with the line; a stored identity does not move with anything.** Citations
  resolve against the leaf's own code line — the work branch by name, else the worktree's `HEAD`, else
  the recorded base with `code_tree_source` naming the fallback — while the memory side stays the
  recorded memory base. Every report names both trees. The identities the run *allocates* carry no
  task, no enclosure, no branch, no baseline and no label, so the invariant one task recorded stays
  usable from any later task, branch or baseline; the identities it *derives* are keyed on the
  **repository's own `repository_id`**, read from the dataset the run selected and derived only as a
  cold-start fallback, and never on the enclosure's recorded code base commit, because two repositories
  sharing a base commit must not be handed the same record identity. What still separates the
  *resolution tree* from the *identity* anchor is that resolution is a fact about the line and identity
  is a fact about the repository.
- **A reused local label is not continuity; naming the stored identity is.** `R-LOCAL` is a local
  hand-off label and says nothing about whether two entries represent the same truth — two independent
  tasks numbering one entry alike are two creation operations and mint two distinct truths. Continuity
  across a task boundary is by **explicitly naming the stored identity**: an entry revising an
  obligation names `invariant_id`, and a target citing a place the dataset already records names
  `anchor_id`. Scoping the stored identity to the authoring enclosure is the opposite repair and is
  forbidden: enclosure identity scopes the **retry key** and distinguishes creation operations, and
  nothing else about it enters an identity.
- **A retry is a replay, and different content under one key is refused.** Repeating one creation
  operation resolves through its idempotency key to the identities it already holds and writes nothing;
  the same key arriving with different content is refused `allocation_content_conflict` rather than
  silently overwriting either side; a key that cannot be checked because the journal is unreadable is
  refused `allocation_journal_unreadable` rather than minted over. Neither refusal weakens the
  duplicate-identity or immutable-revision guards, which are untouched.
- **Continuity is a property of the admission, not of the caller's memory.** A run that selects a
  baseline forks it, so the candidate starts from the invariants the repository already holds; a run
  that selects none still creates an empty candidate, which is the correct behaviour for a
  repository's first task. The fork re-reads the baseline's identity first
  (`CandidateBaseline.expected_identity`), so a baseline that moved is caught rather than silently
  cloned from.
- **A reason is reproducible from the record.** Unresolved-path reasons are decided from the recorded
  trees and the path's own spelling, and the coordination root's top-level names are read once per run
  — never from the live filesystem per entry, so the same citation earns the same reason after the
  enclosure's cleanup has deleted the files it described.
- **The recorded blob identity is a measurement.** Membership is the tree's answer and the working
  bytes are hashed and compared with it; a disagreement is refused rather than recorded, so an
  uncommitted edit cannot be cited as the tree's content.
- **The route does not travel through the batch, and the report says so.** No family is invented per
  entry; the two legs are separate transactions over the candidate, and
  `routes.author_route`'s idempotence plus `routes.set_governing_route`'s one-route-per-governed-row
  constraint are what make repetition safe rather than assumed.
- **Boundary.** No symbol extractor (a symbol locator is carried and observed, and the rail answers
  `unsupported_locator` for it), no onboarding write, no export, no third root, no publication, no lane
  parameter (the `draft-candidate` lane is the only one it admits), and no candidate-directory
  convention (the caller names it and the report echoes it). In this revision no MCP tool imports the
  operation: a repository-wide search finds `ingest_curator_list` imported only by the module's own
  test population, so the caller is the curator seat rather than a tool surface.

### Todos

Two module constants are declared with their rationale and never referenced: `_RULING_SHAPE`
(`"empty_target_ruling"`, described as the one shape an empty target is reported under) and
`_NO_REFUSAL` (how a blank per-target refusal reads). Nothing in the report carries either name today —
a ruling is reported through `EntryOutcome.state` being `SKIPPED`, and a committed target's refusal is
the empty-string default on `TargetOutcome.refusal` — so the two comments document an intent the code
does not yet exercise. Everything else this module states about its own limits is a deliberate boundary
recorded above (no symbol extractor, no onboarding write, no third root, no export, publication out of
reach), not an outstanding task.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped revision: the module's own docstring and
functions, the write module whose entries it builds, the route and observation primitives it calls,
the model vocabulary it constructs, the hand-off list contract it reads, and the cases that measure
each behaviour. Three details a reader should carry: the resolution tree is the leaf's own code line,
while a **derived** citation identity is anchored to the repository's own namespace and to neither
tree and an **allocated** identity is anchored to nothing at all; the route leg is two
transactions outside the batch because the closed command union has no command that sets a route on an
anchor; and the invariant/revision pair is the only pair this module *allocates*, which is why the
rows below cite the allocation machinery separately from the derivation.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the job and of the three cases that are never conflated, beside its statement of what it refuses to be (no symbol extractor, no onboarding, no export, no third root, no publication). | "Three cases, never conflated."; "What this module does not do." | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1-80; mcp/src/agents_remember/application/knowledge_curator_ingest.py:76-80 |
| The no-exception promise, and the one boundary where the citation machinery's raised conditions become refusals instead of a traceback. | "No failure is an exception."; `_plan_target` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:41-64; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1860-1900 |
| The published surface (`__all__` plus eight report-vocabulary names), the operation itself with its required authorization and dry-run mode, and the run that authors routes, commits one batch, attaches routes and reports. | `__all__`; `ingest_curator_list`; `_run` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:163-174; mcp/src/agents_remember/application/knowledge_curator_ingest.py:999-1115; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1118-1160 |
| Admission as resume, baseline-fork or create, the stored repository namespace read before it is derived, the resolution read from the recorded pair, the enclosure helper the resolution still reads and the report's identity sentence no longer names as an identity input, and the contract and loader those facts come from. | `_admitted_candidate`; `_repository_namespace`; `_repository_identity`; `_resolution`; `_enclosure`; `WorktreeContract`; `load_contract` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1257-1299; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1302-1332; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1335-1367; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1370-1383; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1386-1393; mcp/src/agents_remember/worktrees/worktree_contract.py:234-286; mcp/src/agents_remember/worktrees/worktree_contract.py:437-468 |
| The entry fields that make an entry a revision of an obligation the repository already holds rather than a first authoring — the declared predecessors and the invariant the entry names — and the plan that carries both into the batch. | `_EntryFields`; `_Plan` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:733-785; mcp/src/agents_remember/application/knowledge_curator_ingest.py:446-478 |
| What makes two targets the same place, so that two symbols in one file are two realizations while a genuine repeat is still refused. | `target_key` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:504-515 |
| The three outcome words, and the ruling path that reports an empty-target entry as skipped with the producer's verdict carried rather than committing it. | `COMMITTED`; `REFUSED`; `SKIPPED`; `_ruling_plan` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:178-178; mcp/src/agents_remember/application/knowledge_curator_ingest.py:179-179; mcp/src/agents_remember/application/knowledge_curator_ingest.py:180-184; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1837-1857 |
| The report and count shapes a caller reads, the two measurements kept apart, and the written-row arithmetic (distinct batch rows plus authored route rows) that a dry run projects from the same plans. | `IngestReport`; `IngestCounts`; `EntryOutcome`; `TargetOutcome`; `RouteOutcome`; `_counts`; `written`; `_projected` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:403-445; mcp/src/agents_remember/application/knowledge_curator_ingest.py:379-402; mcp/src/agents_remember/application/knowledge_curator_ingest.py:365-378; mcp/src/agents_remember/application/knowledge_curator_ingest.py:339-354; mcp/src/agents_remember/application/knowledge_curator_ingest.py:355-364; mcp/src/agents_remember/application/knowledge_curator_ingest.py:3288-3326; mcp/src/agents_remember/application/knowledge_curator_ingest.py:3180-3207; mcp/src/agents_remember/application/knowledge_curator_ingest.py:3072-3097 |
| The resolution tree versus the identity anchor, the work-branch-then-HEAD-then-base line lookup, and the observation rail the anchor is handed to, with the error type whose raise that boundary converts. | `_TreeIds`; `_tree_ids`; `_code_line`; `observe_anchor`; `SourceIndexError` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:679-695; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1407-1432; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1435-1449; mcp/src/agents_remember/memory/knowledge/read_anchors.py:101-174; mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:64-65 |
| The three-step path completion, the tree-membership check, the measured working-blob identity compared with the recorded blob, and the normalisation of a leading `./`. | `_complete_target`; `_member`; `_working_identity`; `_BlobIdentity`; `_confined` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:2053-2090; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2093-2130; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2133-2163; mcp/src/agents_remember/application/knowledge_curator_ingest.py:715-732; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1961-1968 |
| The three reasons a confined path earns, the first-segment ownership test read from the trees, the third-root test against the coordination root, its once-per-run top-level read, and the lexical containment helper. | `_unresolved_reason`; `_first_segment_admitted`; `_outside_the_roots`; `_coordination_top_level`; `_within` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:2173-2213; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2216-2244; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2247-2267; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2270-2293; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2296-2310 |
| The locator gate that refuses a missing locator rather than promoting it, the four range refusals with one code each, the symbol path from bare name to two-part locator, the language and prose/structured refusals, and the extension table lookup. | `_locator`; `_range_locator`; `_symbol_locator`; `_symbol_language`; `_language_of` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:2313-2354; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2357-2401; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2404-2447; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2450-2491; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2494-2503 |
| The extension table a symbol's language name is derived from, and the extractor that decides whether a name is a *definition* — now the shipped tree-sitter one, called through `bound_definitions` rather than reimplemented here. | `_LANGUAGES`; `bound_definitions`; `grammars.parsed` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:301-316; mcp/src/agents_remember/memory_quality/style/citations/extents.py:107-131; mcp/src/agents_remember/memory_quality/style/citations/grammars.py:155-157 |
| The symbol boundary and its refusal codes: the qualified-name resolution through the shipped extractor, the locator's language derivation, and the mention-versus-absence distinction — with no second definition implementation beside it. | `_symbol_locator`; `_symbol_language`; `_occurs` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:2404-2447; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2450-2491; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2506-2516 |
| The route leg: the distinct scopes, the pre-batch authoring transaction that classifies authored versus reused, the post-batch attachment transaction, each target's route outcome, and the two primitives whose idempotence the leg depends on. | `_author_routes`; `_author_route_rows`; `_attach_routes`; `_attached_outcome`; `_distinct_routes`; `author_route`; `set_governing_route` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:2598-2626; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2651-2678; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2705-2730; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2750-2775; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2629-2637; mcp/src/agents_remember/memory/knowledge/routes.py:276-332; mcp/src/agents_remember/memory/knowledge/routes.py:436-520 |
| The write half of this module: one target plan's stored anchor and citation, whether that citation authors its anchor or reuses a stored one, the authored realization role, the entry assembly with its conditions and the revision fields it carries, the single batch commit, and the per-entry rendering of a refused batch. | `_TargetPlan`; `_TargetIdentities`; `_authored_role`; `_curator_entry`; `_commit`; `_batch_refused` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:479-540; mcp/src/agents_remember/application/knowledge_curator_ingest.py:541-555; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2950-2966; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2808-2822; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2836-2847; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2880-2908 |
| **A new truth is ALLOCATED, not derived: the retry key, the allocation journal, the content guard and the replay (this leaf's CYCLE-01 repair).** `_retry_key` joins the enclosure's own task identity (`_retry_scope`) with the entry's id to form the **idempotency key** a retry is found by, and it is explicitly not an identity input. `_creation` hands a new key a fresh `uuid4` pair, hands a recorded key back the pair it already holds, and refuses `allocation_journal_unreadable` rather than minting over an answer it cannot read; `_record_allocations` writes the journal through `_allocation_journal`/`_allocation_record` **before** the batch, into the candidate admission already produced. `_content_digest` plus `_require_minted_content` are the guard that makes one key mean one creation operation: a recorded key arriving with different content is refused `allocation_content_conflict`. `_stored_revisions` and `_with_replays` then decide replay from the **dataset** rather than from the journal, and `_replayed_routes`/`_replayed_outcome` are how a replay is reported without a second write. | `_Allocation`; `_Allocations`; `_retry_scope`; `_retry_key`; `_content_digest`; `_allocation_journal`; `_read_allocations`; `_allocation_record`; `_record_allocations`; `_creation`; `_require_minted_content`; `_stored_revisions`; `_with_replays`; `_replayed_routes`; `_replayed_outcome` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:556-594; mcp/src/agents_remember/application/knowledge_curator_ingest.py:595-609; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1471-1479; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1482-1493; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1496-1517; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1520-1523; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1526-1550; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1553-1562; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1565-1586; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1589-1628; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1631-1656; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1659-1675; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1678-1690; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2640-2648; mcp/src/agents_remember/application/knowledge_curator_ingest.py:3009-3026 |
| **The identities one target's own place mints, derived together, and each keyed on what it actually is (this leaf's CYCLE-01 repair).** `_TargetIdentities` is the frozen trio a target needs; `_target_identities` takes the repository identity, the written path, the locator and an `_Authoring` — whose creation id is the **allocated revision** — and mints them together: the route keyed on the entry that names the path, the anchor keyed on that revision with the locator's qualified name as the in-creation disambiguator, and the claim keyed on the **revision-plus-anchor edge** rather than on the label. A named `anchor_id` short-circuits the anchor to the stored identity and keeps the claim keyed on the pair, which is the explicit-reuse half. `_identity` is the one derivation, keyed on `repository.repository_id` and never on the enclosure's recorded base commit. | `_TargetIdentities`; `_target_identities`; `_Authoring`; `_identity` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:541-555; mcp/src/agents_remember/application/knowledge_curator_ingest.py:623-678; mcp/src/agents_remember/application/knowledge_curator_ingest.py:610-620; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2911-2947 |
| **The explicit-reuse input, and the one authority for the split.** `_named_anchor_id` reads a target's optional `anchor_id` and refuses a malformed one per target as `anchor_id_not_a_uuid`, so a producer citing a place the dataset already records uses that stored identity verbatim and authors no anchor row; `_report`'s `derived_identities` field is the public sentence a caller reads, and it now states both halves — allocated for a new truth, derived for a citation — and both negatives. | `_named_anchor_id`; `derived_identities`; `_identity`; `_creation` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1970-1992; mcp/src/agents_remember/application/knowledge_curator_ingest.py:3230-3280; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2911-2947; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1589-1628 |
| The anchor id the observation is handed, whose discriminator names what within the file the locator points at rather than only the kind of thing it is. | `_observation_id` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:2572-2595 |
| The write module this ingest commits through: the citation and entry drafts it builds, the per-entry command list whose order is the batch's own contract, and the all-or-nothing batch commit. | `CuratorCitation`; `CuratorEntry`; `curator_entry_commands`; `commit_curator_entries` | mcp/src/agents_remember/application/knowledge_ingest.py:67-79; mcp/src/agents_remember/application/knowledge_ingest.py:82-101; mcp/src/agents_remember/application/knowledge_ingest.py:104-130; mcp/src/agents_remember/application/knowledge_ingest.py:176-187 |
| The model vocabulary the ingest constructs: the three locator kinds it resolves into, and the stored anchor draft it hands to both the rail and the write path. | `FileLocator`; `LineRangeLocator`; `SymbolLocator`; `SourceAnchorDraft` | mcp/src/agents_remember/models/knowledge/source.py:38-41; mcp/src/agents_remember/models/knowledge/source.py:44-58; mcp/src/agents_remember/models/knowledge/source.py:60-66; mcp/src/agents_remember/models/knowledge/source.py:82-97 |
| The cases that measure the behaviours a reader is most likely to doubt: the three outcomes in one run, the ruling that is never committed, a leaf citing a file its own line created, the measured blob identity refusing a working edit, and the route recorded once per scope and attached per anchor. | "test_one_run_reports_committed_skipped_and_each_refusal_reason"; "test_a_ruling_is_never_committed_as_an_obligation_with_no_realization"; "test_a_producer_citing_a_file_its_own_leaf_created_commits_and_reads_back"; "test_the_recorded_blob_identity_is_measured_and_a_working_edit_is_a_typed_refusal"; "test_the_governing_route_is_recorded_once_per_scope_and_attached_to_each_anchor" | mcp/tests/test_knowledge_curator_ingest_list.py:417-472; mcp/tests/test_knowledge_curator_ingest_list.py:475-519; mcp/tests/test_knowledge_curator_ingest_list.py:522-575; mcp/tests/test_knowledge_curator_ingest_list.py:861-935; mcp/tests/test_knowledge_curator_ingest_list.py:1261-1317 |
| The hand-off list contract this ingest reads: the nine producer-owned fields, the rule that every entry carries all thirteen keys with curator fields null, and the required locator that makes an omission a refusal rather than a whole-file citation. | "The nine the producer supplies are"; "Every entry carries all thirteen keys"; "a target that names a path and no construct" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:27-27; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:50-50; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:85-85 |
| **The publication selection: where a committed run publishes its candidate, and that an unstated destination is not an expectation.** `IngestPublication` carries the destination path and the exact identity the caller admitted is there (`None` meaning the destination is expected to be ABSENT), and `IngestSelection.publication` is how a run selects it — the selection exists so a caller never has to re-derive the namespace, the resolution or the live identity the publication owner needs. It is also where a run names the `baseline` it forks from, which the CLI now reaches through `--baseline`. | `IngestPublication`; `IngestSelection` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:963-979; mcp/src/agents_remember/application/knowledge_curator_ingest.py:980-996 |
| **The step that reaches the shipped publication owner, and the one place a run may publish.** `_publish_candidate` reads the committed candidate's live identity with the product's own non-raising `open_knowledge_candidate` — a candidate that cannot be read arrives as a refused publication carrying that refusal — and hands it to `publish_knowledge_snapshot` under the request the caller's selection describes. | `_publish_candidate`; `publish_knowledge_snapshot`; `open_knowledge_candidate` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1175-1210; mcp/src/agents_remember/application/knowledge_snapshot.py:134-139; mcp/src/agents_remember/application/knowledge_snapshot.py:118-123 |
| **The condition publication is gated on: a batch that landed, and nothing else.** The run publishes after `_run` and only when at least one entry is in `committed` — a refused or un-attempted batch leaves `IngestReport.publication` as `None`, and `batch_state` is what says which of the two reasons applies. | `ingest_curator_list`; `IngestReport` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:999-1115; mcp/src/agents_remember/application/knowledge_curator_ingest.py:403-445 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The operation resolves every path inside the
one enclosure's two admitted roots, refuses a path under the coordination root as a third root it
cannot reach, and carries no identity beyond that enclosure; the hand-off list it reads is handed to it
as data, not fetched.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator (uncommitted change set on `ar/260915-ks-l43-ar`, code base `fb719f89`): **the identity rule this card stated is replaced by the developer's ruling, and the card now says which of the two halves is allocated and which is derived.** The pre-ruling reading — "the identities the run mints are keyed on the repository's own namespace ... so the obligation the first task recorded is the same record when the next task reads the line at a later baseline" — was true of the *citation* identities and was false of the invariant and its revision: the label was their whole distinction, so two independent tasks that both numbered an entry `R-LOCAL` and stated different truths minted ONE invariant and ONE revision, and production sync then refused `duplicate_identity` on it and offered only to discard one of two truths that were never in conflict. Under the ruling a label is a **local hand-off label** carrying no identity meaning; the **knowledge API allocates and persists** the canonical identity; continuity across a task boundary is by **explicitly naming the stored identity** (the entry-level `invariant_id`, and now the target-level `anchor_id`); and a retry rides a **separate idempotency key**. The clause was rewritten rather than annotated, and the scoping this repair is *not* is stated on the card: scoping the stored identity to the authoring enclosure is forbidden by the ruling, because it would make the invariant task-local; enclosure identity scopes the retry key and distinguishes creation operations only. **What the card now says.** A new Purpose paragraph states the allocation/derivation split; the "identities one target's own place mints" Logic bullet was rewritten into four: the split itself (invariant and first revision allocated as fresh `uuid4` under `_creation`; route, anchor and claim still derived, with the anchor keyed on the allocated revision and the claim on its own revision-plus-anchor edge); the retry key as a separate fact from any identity (`_retry_key`/`_retry_scope`); the journal, the content digest and the two new refusals (`_read_allocations`, `_record_allocations`, `_creation`, `_require_minted_content`, `allocation_content_conflict`, `allocation_journal_unreadable`); and the replay, decided from the dataset rather than from the journal (`_stored_revisions`, `_with_replays`, `_replayed_routes`, `_replayed_outcome`, the new `replayed` batch state). A fifth records the explicit anchor-reuse input (`_named_anchor_id`, `declares_anchor`, `anchor_id_not_a_uuid`). The `derived_identities` bullet was updated to the sentence the field now carries. **Conventions and Invariants.** The `Identities are derived, never random` bullet is replaced by `A new truth is allocated, a citation is derived, and the label is neither`, which names the discriminator by identity rather than listing `entry_id` as the input to all five; `The resolution tree moves with the line; the identity does not move with the baseline` became `a stored identity does not move with anything`; and two invariants were added — label reuse is not continuity and enclosure-scoped identity is forbidden, and a retry is a replay while different content under one key is refused. **Two falsified clauses were corrected with them:** the commit bullet no longer says the invariant id is "the identity derived from the entry's local id" (it is the allocated one), and the CYCLE-04 paragraph's claim that `_Authored` "keeps those two semantic facts together" is replaced, because this leaf deleted `_Authored` when `_Authoring` took over the facts that decide a citation's identity. **Citation accounting.** Every code range in the Repo-Internal References table was re-measured at its construct's own declaration extent in this candidate — this leaf added 605 lines to the module, so the whole file moved — including the ranges no checklist row named. `_identity` `:2436-2458`→`:2911-2947`; `_target_identities` `:493-513`→`:623-678`; `_observation_id` `:2108-2131`→`:2572-2595`; `_plan_target` `:1431-1473`→`:1860-1900`; `target_key` `:437-448`→`:504-515`; `_LANGUAGES` `:266-278`→`:301-316`; `_ruling_plan` `:1409-1429`→`:1837-1857`; the admission row's five ranges to `:1257-1299`/`:1302-1332`/`:1335-1367`/`:1370-1383`/`:1386-1393`; `_admitted_candidate`/`_publish_candidate`/`_curator_entry`/`_commit`/`_batch_refused`/`_counts`/`written`/`_projected` to `:1257-1299`/`:1175-1210`/`:2808-2822`/`:2836-2847`/`:2880-2908`/`:3288-3326`/`:3180-3207`/`:3072-3097`; the report-vocabulary and path-completion and unresolved-reason and locator and symbol and route-leg rows to their own declarations. Three new rows were added for the allocation machinery, the allocator/derivation authority and the explicit-reuse input. No anchor was renamed and no citation was dropped. **Stamp accounting:** `reviewedWorkingCandidate` now names this leaf's candidate `ar/260915-ks-l43-ar` on base `fb719f89`, which is the candidate this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded, because no commit contains the body as it now stands and no stamp was measured on it. No commit was made.
- 2026-09-20T12:00:25+00:00: Generated citation repair: `target_key` repointed to mcp/src/agents_remember/application/knowledge_curator_ingest.py:504-515. No content impact: mechanical anchor-range projection bound to citation source snapshot 23094be373d669ad77475ab6ebb610401913ce4b65c82d3b4cc642eb6bb44e43; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T12:00:25+00:00: Generated citation repair: `_observation_id` repointed to mcp/src/agents_remember/application/knowledge_curator_ingest.py:2572-2590. No content impact: mechanical anchor-range projection bound to citation source snapshot 23094be373d669ad77475ab6ebb610401913ce4b65c82d3b4cc642eb6bb44e43; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T07:30+02:00 — 260915-KS-L42 curator (uncommitted CYCLE-02 repair change set on `ar/260915-ks-l42-ar`, code base `74c6c693`): **the report stopped describing an identity rule the code no longer follows, and this card's own last restatement of that rule is corrected with it.** `IngestReport.derived_identities` is a public field, and it still read "uuid5 over … the enclosure's recorded code base commit … plus the written path for a target" long after `_identity` had moved to the repository's own namespace — the exact sentence a verification round was misled by. It now names the fixed `_INGEST_NAMESPACE`, the repository's namespace identity, which identity it is, the entry's own id and, for a target, what inside the written path the citation is about (a symbol's qualified name, or the locator kind where nothing finer exists), and it states the stable half as the repository namespace and never the recorded base commit. The module docstring carried the same stale clause and was corrected in the same change. Two clauses on this card were falsified by it and were rewritten rather than annotated: the Repo-Internal References preamble said "every derived identity is anchored to the recorded base commit" (it is anchored to the repository's own namespace and to neither tree), and the admission row described `_enclosure` as the helper the report's identity sentence still names (it is what `_resolution` reads, and it is no longer an identity input). A new Logic paragraph records the field, the docstring correction and the guarded assertion that makes the sentence checkable — the base commit must not appear in the field, the field must name the repository namespace, and `_identity` is compared against `uuid5(_INGEST_NAMESPACE, repository_id|kind|entry_id|)` rather than against a phrase. The outcome-word row was re-cited to the constants' own lines (`COMMITTED`/`REFUSED`/`SKIPPED` at :164-:166) and `_ruling_plan` to its own extent (:1409-1429), which this leaf's docstring edit shifted. Verification metadata is advanced to this leaf's own base `74c6c693` — a descendant of the previously recorded `f79f4db7`, so the recorded verification got closer to the working tree rather than further from it — with the uncommitted working candidate named beside it; closeout owns the committed stamp.
- 2026-09-20T05:14+02:00 — 260915-KS-L39 curator (uncommitted CYCLE-01 change set on `ar/260915-ks-l39-ar`, code base `756c47b37fa16324a836a44336655413d10fffaa`): **this card was re-read against the identity repair, and the claims that repair invalidates were rewritten rather than left standing.** `_identity` no longer derives from `_enclosure(contract)`: every id it mints is a `uuid5` over the **repository's own `repository_id`**, which identity it is and the entry's local id — with the written path discriminating a target's *route* and the locator's qualified name discriminating its *anchor* and *claim* — minted together by the new `_target_identities` into one `_TargetIdentities` value, and reached from `_Source.repository` after `ingest_curator_list` resolves the namespace before planning. That is what makes `resolve_budget` and `other` in one `pkg/module.py` two stored records instead of one `source_anchor` the batch refuses as `duplicate_identity`, and what makes one repository's obligation the same record at a later baseline. The clauses this falsified were corrected in place: the Purpose paragraph no longer says the identities stay anchored to the recorded base commit, the `Identities are derived, never random` convention now names the repository namespace and the construct-bound discriminator, the resolution-tree invariant now separates "resolution is a fact about the line" from "identity is a fact about the repository", and the admission row no longer describes the enclosure string as what the remaining identities derive from. A new Logic paragraph records why the trio is one value, and a new reference row cites `_TargetIdentities`, `_target_identities` and `_identity`. **Citation accounting:** every code range in the Repo-Internal References table was re-measured at its construct's own declaration extent in this candidate, because this leaf's insertions plus its `ruff format` pass moved the whole file — the rows the checklist named, and the ranges in those same rows whose anchors had drifted out of them. `_observation_id` is now cited at `:2108-2131`, `_plan_target` at `:1431-1473`, `_curator_entry` at `:2333-2347` and `_publish_candidate` at `:991-1026`. No anchor was renamed, no citation was dropped, and no finding text changed except where the source itself changed. **Stamp accounting:** `reviewedWorkingCandidate` now names this leaf's candidate `ar/260915-ks-l39-ar` on base `756c47b3`, which is the candidate this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded, because no commit contains the body as it now stands and no stamp was measured on it. No commit was made.
- 2026-09-20T02:28+02:00 — 260915-KS-L33 curator, post-sync repair pass (uncommitted change set on `ar/260915-ks-l33-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **re-read this card after the sync onto the moved master line, repaired the 12 citation rows the checklist named, and collapsed the two duplicated blocks the union merge left.** Two blocks were present twice, byte-identical: the "report is the operation's other half" and "written-row count" Logic bullets, and a whole second `### Conventions` section. The first copy of the Logic pair and the first Conventions section were removed; the two bullets unique to that first Conventions section ("One spelling per fact", "Everything internal is a frozen dataclass") were kept and folded into the surviving section, and the narrower `Identities are derived, never random` bullet was dropped in favour of the surviving superset that also names the construct-bound discriminator. No wording was otherwise changed. **Citation repair:** every stale range was repointed to the cited construct's own declaration extent in the candidate — the `_enclosure` row to `:1166-1173`, `_ruling_plan` to `:1372-1392`, `_projected` to `:2507-2532`, `_counts` to `:2715-2748`, `written` to `:2614-2643`, `_confined` to `:1499-1505`, `_attach_routes` to `:2193-2218`, `_attached_outcome` to `:2238-2263`, `IngestSelection` to the declaration at `:787-804` (with `IngestPublication` re-cited at its own `:770-784`), and the five admission ranges to `:1035-1079` / `:1082-1112` / `:1115-1147` / `:1150-1163` / `:1166-1173`. **Anchor rename:** the write-half row's `_role_for` anchor, which exists nowhere in the tree after this leaf's CYCLE-04 repair, was rewritten to the surviving constructs of that same narrative — `_Authored` (`:580-590`), the new `_authored_role` (`:2405-2420`) and `_TargetPlan` — with the Finding text kept unchanged because it still reads correctly as written. **Stamp accounting:** `reviewedWorkingCandidate` now names this leaf's candidate `ar/260915-ks-l33-ar`, which is the candidate this pass was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded, because no commit contains the body as it now stands and no stamp was measured on it; no anchor beyond `_role_for` was renamed, no citation was dropped, no finding text was changed, and no commit was made. **This entry folds in the earlier L33 entry that stood below it** (the 00:47 pass that first recorded the CYCLE-04 authored-role repair in this card): the ingest no longer derives a realization role from the locator — the deleted `_role_for` answered `primary-authority` for a whole file or a range and `enforcement` for a symbol, which locator syntax cannot establish, since a symbol can be presentation, propagation, support or enforcement and so can a range. `_EntryFields` gained `role` and `role_rationale`, sourced from the entry's `realization_role` and `realization_rationale`; the stated word is validated against the model's own `get_args(RealizationRole)` and cast, so an unrecognised spelling yields **no role** rather than a stored semantic claim; `_Authored` was added as the frozen pair that keeps a role and its rationale together; `_authored_role` answers with the stated role or the vocabulary's own `UNCLASSIFIED_ROLE`, and the vocabulary was not widened.
- 2026-09-20T01:28+02:00 — 260915-KS-L30 owning seat (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **the publication leg reached this operation, and the card now states it.** CYCLE-01's required direction has two halves; the earlier pass repaired the identity half, and this pass adds the second — the operation now *performs* publication rather than leaving it as a later act. `IngestPublication` (a destination path plus the exact identity the caller admitted, `None` meaning the destination is expected to be absent) is selected through `IngestSelection.publication`; after a committed batch, `_publish_candidate` reads the candidate's **live** identity — which the batch just changed, so no caller could have supplied it — with the product's own non-raising `open_knowledge_candidate`, and publishes it through the shipped `publish_knowledge_snapshot` under the request the selection describes. The Purpose paragraph's old sentence ("no publication — that is the curator's later act and is not reachable from here") stopped being true the moment this landed and is replaced by the paragraph that says what the step does, why it runs here, that a batch which did not commit is never published, and that a destination the caller did not admit is refused rather than overwritten. Three claim rows were added, for `IngestPublication`/`IngestSelection`, for `_publish_candidate`/`publish_knowledge_snapshot`, and for the `committed`-gated wiring with `IngestReport.publication`. The measured pre-repair state, the exact search results that showed the publication owner had exactly one caller in the tree (test support), and the shape of the repair are recorded in `notes/reports/2026-09-20-cycle01-publication-reachability.md`. No verification stamp was advanced and no commit hash was invented: the candidate is uncommitted and closeout owns the real code and memory commits.
- 2026-09-20T01:24+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **citation-range repair and stamp accounting against this leaf's working candidate.** The checklist named 29 `citation_anchor_absent_from_range` rows and three whose range was stale by a move (`_LANGUAGES`, `_observation_id`, `target_key`), and reopened five claims (`__all__`, `_EntryFields`/`_Plan`, `target_key`, `_TargetPlan`, `_observation_id`). All 60 code-file ranges in the Repo-Internal References table were re-measured at their declarations in the candidate; **57 were repointed to the cited construct's own declaration extent** and the three module-docstring spans (`:1-64`, `:41-46`, `:59-63`) were left because they still hold the phrases they are cited for. Of the 57, 32 are the ranges the checklist named and 25 are ranges in the same rows whose own anchor had moved out of them even though another range in that row still happened to mention it: `_plan_target` `:1281-1319`→`:1367-1405`; `ingest_curator_list`/`_run` `:700-794`/`:846-879`→`:784-891`/`:894-927`; `_admitted_candidate`/`_repository_namespace` `:926-970`/`:973-1003`→`:1012-1056`/`:1059-1089`; the six report-vocabulary ranges in the `IngestReport` row (`IngestCounts` `:343-360`→`:336-357`, `EntryOutcome` `:329-340`→`:322-333`, `TargetOutcome` `:303-316`→`:296-309`, `RouteOutcome` `:319-326`→`:312-319`, `written` `:2306-2331`→`:2572-2601`, `_projected` `:2379-2404`→`:2465-2490`); `_complete_target` `:1288-1325`→`:1517-1554`; `_unresolved_reason`/`_first_segment_admitted`/`_outside_the_roots` `:1408-1448`/`:1594-1622`/`:1625-1645`→`:1637-1677`/`:1680-1708`/`:1711-1731`; `_locator`/`_range_locator`/`_symbol_locator` `:1691-1732`/`:1735-1779`/`:1782-1825`→`:1777-1818`/`:1821-1865`/`:1868-1911`; `_symbol_locator`/`_symbol_language` in the symbol-boundary row `:1782-1825`/`:1828-1869`→`:1868-1911`/`:1914-1955`; `_author_route_rows`/`_distinct_routes` `:1877-1904`/`:2007-2015`→`:2104-2131`/`:2093-2101`; and `_TargetPlan`/`_curator_entry`/`_commit` `:399-412`/`:2175-2189`/`:2203-2214`→`:421-469`/`:2261-2275`/`:2289-2300`. Each replacement range was read at its own declaration before it was written. One cross-file range was stale for the same reason and was repointed with them: the write-module row cited `commit_curator_entries` at `knowledge_ingest.py:164-175`, which is the singular `commit_curator_entry` and its caller, and it now cites `:176-187`. Every one of the 84 (anchor, range) pairs in the table therefore has its anchor's own declaration inside its range, and no pair was left pointing at a neighbour's construct. No Finding text, anchor name, row or citation was added, removed or re-worded, and no range was deleted. The five reopened claims were re-read against the current constructs and retain their wording: `_EntryFields` still reads the fields that make an entry a revision (`predecessor_revision_ids`, `invariant_id`) and `_Plan` still carries `declares_invariant`/`predecessors` into the batch; `target_key` is still the completed path, the locator kind and a symbol's qualified name; `_TargetPlan` still carries one target's stored anchor and citation; `_observation_id` still names what within the file the locator points at; `__all__` is still the nine-name published surface. Because this body now describes a working candidate no commit contains, the stale `lastVerifiedCommitHash` and `lastVerifiedCommitDate` rows were replaced by one `reviewedWorkingCandidate` row under the reopened-claim stamp rule: **no verification stamp was advanced and no commit hash was invented**; closeout owns the real code commit.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 26 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `COMMITTED`; `REFUSED`; `_BlobIdentity`; `_TreeIds`; `__all__`; `_attach_routes`; `_attached_outcome`; `_code_line`; `_coordination_top_level`; `_counts`; `_distinct_routes`; `_first_segment_admitted`; `_language_of`; `_locator`; `_member`; `_outside_the_roots`; `_plan_target`; `_projected`; `_range_locator`; `_ruling_plan`; `_run`; `_symbol_language`; `_symbol_locator`; `_tree_ids`; `_within`; `_working_identity`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): re-verified this card against the CYCLE-01 repair and rewrote the claims that change invalidates. The entry point now takes one `IngestSelection` — candidate directory, authorization ref, a `dry_run` with no default, and the baseline it forks — instead of four trailing keyword arguments, because the candidate and the baseline are the two halves of one decision. Admission is resume, **baseline-fork** (the shipped `clone_knowledge_candidate`, under a `CandidateBaseline` whose `expected_identity` is re-read before a byte is copied, so a baseline that moved is caught) or empty-create only when the run selected no baseline at all — an empty candidate holds only this task's entry and is the continuity defect itself. The repository namespace is **read from the repository's own dataset** (`_repository_namespace`) and derived under `_INGEST_NAMESPACE` only as a cold-start fallback keyed on `repo_name`: deriving it from the enclosure's recorded base commit made one repository's namespace change with its baseline and handed two repositories that shared a base commit the same one. `_EntryFields` now reads `predecessor_revision_ids` and `invariant_id`, `_Plan` carries `declares_invariant`/`predecessors`, `_curator_entry` passes both into `CuratorEntry`, and the invariant id is the entry's named one whenever it declares predecessors — so a changed statement is a revision of the obligation the repository already holds instead of an `AddInvariant` the batch refuses as `batch_stale_precondition`. The duplicate guard is now `_TargetPlan.target_key` (completed path, locator kind, and a symbol's qualified name) and `_observation_id` carries that qualified name, so two symbols in one source file are two realizations rather than a second `duplicate_target_path`. This card's Update History was also put back in newest-first order, which the quality checklist reported. Every other claim, anchor and range was re-read against the working candidate and left as it stood; no verification stamp was advanced, because the candidate is uncommitted and closeout owns the real code and memory commits.
- 2026-09-19T18:40+02:00 — 260915-KS-L28 repair (uncommitted change set on `ar/260915-ks-l28`): re-verified this card against the repaired source, which this leaf changed for findings M1-2, INC-2, INC-3, INC-4, INC-5, INC-8 and INC-9. The symbol rows and the two prose blocks above were rewritten: this module no longer implements definition detection at all (the regex tables, the blanking pass and `_defines`/`_declares`/`_code_only`/`_blank` were deleted and both this boundary and the knowledge read rail now call `memory_quality.style.citations.extents.bound_definitions`), a non-mapping target or locator is refused rather than raising `AttributeError`, the admission and destination refusals now attribute every planned entry instead of leaving it in no outcome list, the third-root classifier resolves a name the coordination root owns at its top level as the third root, `records_written` counts route rows the leg really wrote even when the batch then refused, a dry run's route states are `projected` rather than a false `authored`, and the dead `_ROUTE_ATTACHED` constant is gone. Still verified against code revision `7e6936c0d3b87f2fa0f462c5c63d6d86441ef10b` for everything that revision already contained; the changed rows describe the working tree and must be re-stamped when this leaf lands.
- 2026-09-19T17:08+02:00 — 260915-KS-L28 curator (uncommitted change set on `ar/260915-ks-l28`): created this one-to-one card for L25's curator ingest. It records the one entry point `ingest_curator_list` with its required `authorization_ref` and dry-run mode, the three never-conflated outcomes (committed, skipped ruling, refused) with the promise that nothing readable raises, the split between the leaf's own code line used for resolution and the recorded base commit the identities stay anchored to, the three-step path completion with the working-byte blob identity measured against the recorded tree, the symbol boundary that now resolves "defined" through the shipped tree-sitter extractor instead of a second regex implementation, the four unresolved-path reasons read from the recorded trees rather than the live filesystem, the route leg run as two transactions through `author_route`/`set_governing_route` because the closed command union carries no route-on-anchor command, the report and count shapes with the corrected written-row arithmetic, and the two declared-but-unreferenced constants `_RULING_SHAPE` and `_NO_REFUSAL`. Verification metadata is the code worktree revision `7e6936c0d3b87f2fa0f462c5c63d6d86441ef10b` that contains the source this card was read against.
