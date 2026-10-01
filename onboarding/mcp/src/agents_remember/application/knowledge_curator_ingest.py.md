# mcp/src/agents_remember/application/knowledge_curator_ingest.py

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
admission's own `scope`, so a repeat of one creation operation resolves to the identities it already
holds while two independent tasks that both numbered an entry `R-LOCAL` mint two distinct truths. A
citation's route, anchor and claim stay *derived*, because they are facts about a place and an edge
rather than about a new truth. The label is never an input to any of them: the anchor is keyed on the
allocated revision id, and the claim on its own two endpoints. Reusing a label therefore says nothing
about whether two entries represent the same truth — continuity across a task boundary is by
**explicitly naming the stored identity**, through the entry-level `invariant_id` or the target-level
`anchor_id`. This is the developer's 2026-09-20 identity ruling implemented; `notes/DISCLOSURES.md`
D-62 in the task tree records the defect it repairs.

It uses the existing citation locator and definition owners for file, range and symbol targets; it is not an onboarding writer or export builder and admits no third root. **Publication is no longer the curator's later act.** A run
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

For a real leaf admission, source resolution now uses curator_candidate_source and the shared future-code capture, including eligible working and new files. Existing draft candidate code bindings progress only through the predecessor-bound candidate owner; ordinary open remains strict. Source currentness is rechecked before the knowledge batch and before publication. Memory resolution retains the admitted memory base, and no before half or immutable invariant revision is rebased by code progression.

An invariant entry now requires curator-authored scope before allocation and target planning. _curator_entry carries applicability, conditions and exclusions through CuratorScope into the existing invariant revision; _content_digest binds this scope to retry identity. Missing or malformed scope returns unfilled_curation_scope per entry, including preview. An allocated entry with changed scope requires a new successor entry and real predecessor IDs; historical revisions are not rewritten.

**The entry point, and what each mode returns.** `ingest_curator_list(admission, entries,
selection: IngestSelection) -> IngestReport` is the whole operation. Its first parameter is a
**`KnowledgeWriteAdmission`** — the facts the operation reads — and it is coerced once at the door by
`as_write_admission`, so a caller may hand it an admission the bootstrap resolver built, a
`WorktreeContract`, or a contract path. `load_contract` is **gone from this module** (`ICR-R29@v1`):
the operation no longer knows what an enclosure is, which is what lets a repository with no task be
written by the *same* operation instead of by a second write path. `IngestSelection` carries the
facts one run selects — `candidate_directory`, `authorization_ref`, `dry_run`, the `baseline` it forks
from, and the `publication` it may make — grouped rather than passed as trailing arguments, because the
candidate and the baseline are the two halves of one decision: a run that can name where it writes
without being able to name what it forks is how continuity was lost in the first place. `dry_run`
is a required member with no default, so every caller states which mode it is in. The operation
refuses a blank `authorization_ref` by name before anything is read (`_require_authorization`, a
`ValueError` — the operation's own input contract, not a per-entry refusal), binds the two roots
(`_roots`, which requires the admitted memory worktree), derives the
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
keyed on `admission.repository_name` rather than on the admitted base commit. Deriving from the
admission made the namespace a function of the baseline — one repository ingested at a later baseline
was handed a *different* namespace and every revision recorded at the earlier one was stranded under
a namespace nothing would look in again — while two repositories that shared a base commit were
handed the *same* one. The `CandidateResolution` is read
from the admission's recorded pair rather than asserted: lane `draft-candidate`, the two trees, the
recorded base commits, and `task_ref` = the admission's own `scope` (`_resolution`). A refused or
identity-less admission returns a report with `batch_state="not_attempted"` carrying the product's
typed refusal.

**A baseline the caller selected is read on every run, resume included, and that is leaf
`260921-ICR-L5`'s repair to this admission.** `_admitted_candidate` used to decide in the order
"existing candidate → clone → create", so a resume (an existing candidate) never looked at
`baseline` at all — and the ingest CLI then went on to fill the review's before half from the bytes it
had captured at the top of the run, replacing an identified first generation with a corrupt file and
reporting it *placed*. The read now happens **first**, through `_selected_baseline`, and both ways a
selected input can be unavailable are answered before anything else is decided: `read_dataset_identity`
(the before half's own value-or-reason reader) returns the identity or the reason, and a reason becomes
the shipped `selected_input_unavailable` refusal naming the path and the reason. "Not a file" and "a
file that is not a dataset of this code" therefore reach the caller as one typed input refusal rather
than as an escaping storage error, and neither is ever read as "no baseline selected" — which is the
other reading of an unreadable fork point, and the one under which a missing historical dataset comes
to be silently replaced by a newly empty one. What stays here is the refusal *this* operation answers a
selected input with, because that is the admission's voice and not the reader's; the reader itself
lives in `application/knowledge_before_half.py` with the half's other dataset reads, and the clone's own
precondition still runs independently (a clone whose named file is not there is refused by the storage
owner).

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
the bytes about to be cited are not the bytes the resolution tree holds — what source movement after capture looks like — which is what keeps the recorded identity a measurement of the file rather
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
travels beside the report in `batch_refusal`. The realization role and rationale the citation
carries are the ones resolved for that target by `curator_realization_authoring.EntryRealization`
(the target's own `role` / `rationale` first, then the entry's explicit default); the ingest states
neither a role nor a rationale of its own.



**The realization role is authored by the producer, not inferred from the locator (this leaf's
CYCLE-04 repair).** The ingest used to state a role it derived from the locator's spelling —
`primary-authority` for a whole file or a range, `enforcement` for a symbol — through a helper named
`_role_for`. Locator syntax cannot establish that fact: a symbol can be presentation, propagation,
support or enforcement, and so can a range, so "where to look" was being stored as "what the thing
found there means", and the inference travelled inside a valid provenance envelope into later family
review and relevance filtering as though a producer had said it. `_role_for` is gone and nothing
replaces it as a default. Since leaf `260921-ICR-L45` the role/rationale pair is owned by
`curator_realization_authoring.py`: `_EntryFields.read` keeps one `EntryRealization` read from the
entry's `realization_role` / `realization_rationale` (the explicit entry-level default), and
`_plan_target_inner` binds each planned target to `EntryRealization.for_target(target)`, which takes
the target's own `role` / `rationale` first and the entry default only for what the target leaves
unstated; the two halves resolve independently. When neither level states a role the claim is the
vocabulary's own `UNCLASSIFIED_ROLE`. The vocabulary is still validated against the model's one
definition (`get_args(RealizationRole)`), never a second copy kept here. (The frozen pair that once
grouped role and rationale, `_Authored`, was removed by an earlier leaf once the creation id became the
third fact a target needs; `_Authoring` carries only the facts that decide a citation's identity.)
The vocabulary was not widened: `UNCLASSIFIED_ROLE` is the shipped `models/knowledge/graph.py` member
for an unassessed edge.

**No rationale is generated, and an unexplained realization is refused at admission (leaf
`260921-ICR-L45`, developer ruling "require rationale", superseding the fallback this card used to
describe).** `_TargetPlan.citation()` hands the resolved rationale to `CuratorCitation` unchanged; the
old fallback sentence "The statement is realized at <path>." is gone, and nothing replaces it. The
stored claim cannot hold an absent rationale (the model and the table require non-blank text), so
`_resolve_creation` asks `realization_refusal` **after the scope check and before `_creation` mints any
identity**, and a failing entry is refused by name while its sibling entries still commit. The named
refusals are `realization_value_not_text` (a non-string `rationale`, `role`, `governing_route`,
`realization_rationale`, `realization_role` or `authority.governing_route` — never `str()`-rendered),
`realization_role_unknown` (a role outside the shipped vocabulary, the word `absent` included — the old
"unknown word becomes no role" reading no longer applies to an admitted entry),
`realization_governing_route_absent_literal` (the word `absent` in any case once trimmed, at a target or
at `authority.governing_route`; omit the key when no route governs), `realization_rationale_absent`
(a target with no rationale at either level; blank counts as absent) and
`realization_rationale_too_long` (over `PROSE_MAX_LENGTH`). **The checks apply only to an entry that
would write new realizations:** when the entry's retry key already holds a recorded allocation whose
revision the candidate stores (`_Allocations.committed`, filled in `ingest_curator_list` from
`curator_stored_revisions.committed_revisions`), the entry is not admitted again, so its exact retry
replays and can publish exactly as at base — including operations committed before targets carried a
rationale — while changed content under that key still reaches `_require_minted_content` and is
refused `allocation_content_conflict`. A recorded-but-uncommitted allocation (a crash between the
journal write and the batch) is **not** exempt. The `str(route_path)` spelling in
`_plan_target_inner` is deliberately kept: after this change only a committed operation's exact retry
reaches it with a non-string value, and its base content digest used that spelling. Stored claims
holding the old generated sentence are never re-read or rewritten; replacing them needs authored
successor entries.

**The report is the operation's other half, and a dry run is the same report with the commit
withheld.** `IngestReport` names the **admission source** (`admission_source`, the document this run
was admitted under — a leaf enclosure contract or a settings document), the candidate directory, the
receipt path, the lane, both trees and where the code tree came from, the repository id, the
identity-derivation sentence, every entry id it read, the three outcome tuples, the counts, the batch
state and its digests before and after, and the batch refusal. It also carries the run's **retained
identity-bound progress**: `allocation_journal` is the candidate's own journal path and
`held_operations` is the per-entry `HeldOperation` list, derived by `_held_operations` from that
journal — **never from the plan** — so a caller can see which identities the operation already holds
without re-reading the candidate itself. `IngestCounts` carries fourteen counts, of which
`targets_completed`
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
`_content_digest` covers the **semantic write intent** this operation is minting an identity for —
kind, statement, evidence, the producer's disposition *and the source it rules from*, the named
invariant when the entry revises one, the predecessor edges it declares, the authored realization
role and its rationale, and each resolved place with the locator that names the construct inside it —
so the key's content is checkable rather than assumed. Since leaf `260921-ICR-L45` each target record
also carries the `role` / `rationale` that target **stated for itself** (`TargetRealization.stated`),
and only when it stated them: a target that inherits everything digests exactly as before, so
allocation journals written before per-target rationale still replay, while a reworded per-target
rationale under a minted key is changed content (`allocation_content_conflict`). The entry-level
`realization_rationale` keeps its verbatim spelling in the digest for the same reason.

> **Correction, leaf `260915-KS-L47`.** This paragraph previously read *"covers every fact the stored
> truth is made of — kind, statement, evidence, the producer's disposition, and each resolved place
> with the locator that names the construct inside it"*. That universal was false and the code
> refuted it: `_EntryFields` carries eleven fields the write path consumes, and `disposition_source`,
> `predecessors`, `named_invariant_id`, `realization_role` and `realization_rationale` were absent
> from the digest. A request changing any of them under a held retry key was reported
> `replayed`/committed against an unchanged database, and in the disposition-source case the success
> report echoed the new ruling text while the stored revision kept the old one. The universal is
> withdrawn rather than reworded: the digest covers the semantic intent, and it deliberately excludes
> `entry_id` (the retry key's own scoping half) and `declares_invariant` (derived as
> `not predecessors`, so it carries no fact its own source field does not). See the ruling at
> `requirements/KS-R01-v1-immutable-knowledge-identity.md:116-117`.

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
`curator_stored_revisions.stored_revisions` (moved out of this module by leaf `260921-ICR-L45`, which
also uses the same reader to decide admission) reads every `revision_id` the candidate already holds, and any plan whose revision
is already there is marked `replayed`. `_run` then writes only the **fresh** plans — re-issuing a
replayed plan's commands would earn the batch's own insert-absence precondition, which is the right
answer to "write this again" and the wrong answer to "repeat the operation that already wrote it". An
all-replay run returns `_REPLAYED_BATCH_STATE` (`"replayed"`) with no batch at all, its route facts
read from the candidate rather than from the arriving request: `_stored_route_outcomes` reads every
replayed plan's stored association once, over a read-only connection, taking the path itself back
from the route's own row with `routes.route_path_for_id`, and `_ledger_scopes` seeds the ledger's
`answered` side from those stored outcomes, while each entry is reported by `_replayed_outcome` as
**committed** with the identities it already holds and each route rendered
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
- **The resolution tree moves with the line; a stored identity does not move with anything.** Leaf citations resolve against the exact future-code candidate captured from the admitted worktree, including eligible uncommitted and new files. Taskless admission retains its existing resolution owner. The memory side stays the recorded memory base. Every report names both trees. The identities the run *allocates* carry no
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
  post-capture source edit cannot be cited as the captured tree's content.
- **The route does not travel through the batch, and the report says so.** No family is invented per
  entry; the two legs are separate transactions over the candidate, and
  `routes.author_route`'s idempotence plus `routes.set_governing_route`'s one-route-per-governed-row
  constraint are what make repetition safe rather than assumed.
- **Boundary.** The installed leaf and taskless CLIs drive the admitted batch writer. File, range and supported symbol locators are resolved against their exact source; unsupported locators refuse by name. The mounted knowledge_change surface remains non-writing. No onboarding write, export, third root or caller-selected write lane is admitted. Explicit publication uses the existing publication owner and declared destination.

### Todos

Two module constants are declared with their rationale and never referenced: `_RULING_SHAPE`
(`"empty_target_ruling"`, described as the one shape an empty target is reported under) and
`_NO_REFUSAL` (how a blank per-target refusal reads). Nothing in the report carries either name today —
a ruling is reported through `EntryOutcome.state` being `SKIPPED`, and a committed target's refusal is
the empty-string default on `TargetOutcome.refusal` — so the two comments document an intent the code
does not yet exercise. Everything else this module states about its own limits is a deliberate boundary
recorded above (no onboarding write, no third root, no export or new write lane), not an outstanding task.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped revision: the module's own docstring and
functions, the write module whose entries it builds, the route and observation primitives it calls,
the model vocabulary it constructs, the hand-off list contract it reads, and the cases that measure
each behaviour. Three details a reader should carry: the resolution tree is the leaf's own code line,
while a **derived** citation identity is anchored to the repository's own namespace and to neither
tree and an **allocated** identity is anchored to nothing at all; the route leg is two
transactions outside the batch because the closed command union has no command that sets a route on an
anchor; and the invariant/revision pair is the only pair this module *allocates*, which is why the
rows below cite the allocation machinery separately from the derivation.

- The module's own statement of the job and of the three cases that are never conflated, beside its statement of what it refuses to be (no onboarding writer, no export builder, no third root or independent publication authority). [1]
- The no-exception promise, and the one boundary where the citation machinery's raised conditions become refusals instead of a traceback. [2]
- The published surface (`__all__` plus eight report-vocabulary names), the operation itself with its required authorization and dry-run mode, and the run that authors routes, commits one batch, attaches routes and reports. [3]
- **Admission as resume, baseline-fork or create, the stored repository namespace read before it is derived, the resolution read from the admission's recorded facts, and the admission vocabulary that replaced the enclosure document this module used to load (`ICR-R29@v1`).** [4]
- **The report's retained identity-bound progress: the journal path, the per-entry held operations, and the helper that derives them from the candidate's journal rather than from the plan (`ICR-R29@v1`).** [5]
- **A selected baseline is read on every run, resume included, before anything else is decided — leaf `260921-ICR-L5`'s repair.** `_selected_baseline` answers with the baseline the selected path names or with the shipped `selected_input_unavailable` refusal that names the path and the reason, and `_admitted_candidate` states it first so an unreadable fork point is never taken as "no baseline selected" and never escapes as a storage error. The value-or-reason reader itself is the before half's, not this module's. [6]
- The entry fields that make an entry a revision of an obligation the repository already holds rather than a first authoring — the declared predecessors and the invariant the entry names — and the plan that carries both into the batch. [7]
- What makes two targets the same place, so that two symbols in one file are two realizations while a genuine repeat is still refused. [8]
- The three outcome words, and the ruling path that reports an empty-target entry as skipped with the producer's verdict carried rather than committing it. [9]
- The report/outcome models and shared counters expose projected versus written rows and the per-entry result. [10]
- The resolution tree versus the identity anchor, the work-branch-then-HEAD-then-base line lookup, and the observation rail the anchor is handed to, with the error type whose raise that boundary converts. [11]
- The three-step path completion, the tree-membership check, the measured working-blob identity compared with the recorded blob, and the normalisation of a leading `./`. [12]
- The three reasons a confined path earns, the first-segment ownership test read from the trees, the third-root test against the coordination root, its once-per-run top-level read, and the lexical containment helper. [13]
- The locator gate that refuses a missing locator rather than promoting it, the four range refusals with one code each, the symbol path from bare name to two-part locator, the language and prose/structured refusals, and the extension table lookup. [14]
- The extension table a symbol's language name is derived from, and the extractor that decides whether a name is a *definition* — now the shipped tree-sitter one, called through `bound_definitions` rather than reimplemented here. [15]
- The symbol boundary and its refusal codes: the qualified-name resolution through the shipped extractor, the locator's language derivation, and the mention-versus-absence distinction — with no second definition implementation beside it. [16]
- The route leg: the distinct scopes, the pre-batch authoring transaction that classifies authored versus reused, the post-batch attachment transaction, each target's route outcome, and the two primitives whose idempotence the leg depends on. [17]
- The write half of this module: one target plan's stored anchor and citation, the realization role and rationale resolved for that target (no generated fallback), the entry assembly with its conditions, the single batch commit, and the per-entry rendering of a refused batch. [18]
- The write half of this module: one target plan's stored anchor and citation, whether that citation authors its anchor or reuses a stored one, the realization role and rationale resolved for that target, the entry assembly with its conditions and the revision fields it carries, the single batch commit, and the per-entry rendering of a refused batch. [19]
- **A new truth is ALLOCATED, not derived: the retry key, the allocation journal, the content guard and the replay (this leaf's CYCLE-01 repair).** `_retry_key` joins the enclosure's own task identity (`_retry_scope`) with the entry's id to form the **idempotency key** a retry is found by, and it is explicitly not an identity input. `_creation` hands a new key a fresh `uuid4` pair, hands a recorded key back the pair it already holds, and refuses `allocation_journal_unreadable` rather than minting over an answer it cannot read; `_record_allocations` writes the journal through `_allocation_journal`/`_allocation_record` **before** the batch, into the candidate admission already produced. `_content_digest` plus `_require_minted_content` are the guard that makes one key mean one creation operation: a recorded key arriving with different content is refused `allocation_content_conflict`. `stored_revisions` (now in `curator_stored_revisions.py`) and `_with_replays` then decide replay from the **dataset** rather than from the journal, and `_stored_route_outcomes`/`_replayed_outcome` are how a replay is reported without a second write. [20]
- **The identities one target's own place mints, derived together, and each keyed on what it actually is (this leaf's CYCLE-01 repair).** `_TargetIdentities` is the frozen trio a target needs; `_target_identities` takes the repository identity, the written path, the locator and an `_Authoring` — whose creation id is the **allocated revision** — and mints them together: the route keyed on the entry that names the path, the anchor keyed on that revision with the locator's qualified name as the in-creation disambiguator, and the claim keyed on the **revision-plus-anchor edge** rather than on the label. A named `anchor_id` short-circuits the anchor to the stored identity and keeps the claim keyed on the pair, which is the explicit-reuse half. `_identity` is the one derivation, keyed on `repository.repository_id` and never on the enclosure's recorded base commit. [21]
- **The explicit-reuse input, and the one authority for the split.** `_named_anchor_id` reads a target's optional `anchor_id` and refuses a malformed one per target as `anchor_id_not_a_uuid`, so a producer citing a place the dataset already records uses that stored identity verbatim and authors no anchor row; `_report`'s `derived_identities` field is the public sentence a caller reads, and it now states both halves — allocated for a new truth, derived for a citation — and both negatives. [22]
- The anchor id the observation is handed, whose discriminator names what within the file the locator points at rather than only the kind of thing it is. [23]
- The write module this ingest commits through: the citation and entry drafts it builds, the per-entry command list whose order is the batch's own contract, and the all-or-nothing batch commit. [24]
- The model vocabulary the ingest constructs: the three locator kinds it resolves into, and the stored anchor draft it hands to both the rail and the write path. [25]
- The cases cover mixed outcomes, targetless rulings, new leaf source, exact captured working blobs and reused route associations. [26]
- The hand-off list contract this ingest reads: the nine producer-owned fields, the rule that every entry carries all thirteen keys with curator fields null, and the required locator that makes an omission a refusal rather than a whole-file citation. [27]
- **The publication selection: where a committed run publishes its candidate, and that an unstated destination is not an expectation.** `IngestPublication` carries the destination path and the exact identity the caller admitted is there (`None` meaning the destination is expected to be ABSENT), and `IngestSelection.publication` is how a run selects it — the selection exists so a caller never has to re-derive the namespace, the resolution or the live identity the publication owner needs. It is also where a run names the `baseline` it forks from, which the CLI now reaches through `--baseline`. [28]
- **The step that reaches the shipped publication owner, and the one place a run may publish.** `_publish_candidate` reads the committed candidate's live identity with the product's own non-raising `open_knowledge_candidate` — a candidate that cannot be read arrives as a refused publication carrying that refusal — and hands it to `publish_knowledge_snapshot` under the request the caller's selection describes. [29]
- **The condition publication is gated on: a batch that landed, and nothing else.** The run publishes after `_run` and only when at least one entry is in `committed` — a refused or un-attempted batch leaves `IngestReport.publication` as `None`, and `batch_state` is what says which of the two reasons applies. [30]

| `_curator_entry` owns the behavior described above. | `_curator_entry` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:3420-3441 |
| `_resolve_creation` owns the behavior described above, and since leaf `260921-ICR-L45` it asks the realization admission checks after the scope check and before `_creation` mints, skipping them only for an entry whose recorded allocation the candidate already stores. | `_resolve_creation`; `realization_refusal`; `committed_revisions` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:2221-2254; mcp/src/agents_remember/application/curator_realization_authoring.py:249-280; mcp/src/agents_remember/application/curator_stored_revisions.py:35-41 |
| `_content_digest` owns the behavior described above. | `_content_digest` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1856-1908 |
| The per-target realization cases (leaf `260921-ICR-L45`): distinct rationale per target, entry-level default inheritance, the absent-rationale refusal with nothing generated, exact replay versus changed rationale, and the committed-versus-recorded allocation distinction for the admission exemption. | `test_each_target_of_one_entry_stores_its_own_authored_rationale_and_role`; `test_a_target_with_no_rationale_refuses_its_entry_by_name_and_nothing_is_generated`; `test_an_exact_replay_of_per_target_rationale_is_idempotent_and_a_changed_one_is_refused`; `test_a_recorded_but_uncommitted_allocation_without_rationale_is_still_refused` | mcp/tests/test_curator_realization_authoring.py:121-150; mcp/tests/test_curator_realization_authoring.py:182-215; mcp/tests/test_curator_realization_authoring.py:218-251; mcp/tests/test_curator_realization_authoring.py:400-432 |

### Cross-Repo References

No cross-repository behavior is implemented in this file. The operation resolves every path inside the
one enclosure's two admitted roots, refuses a path under the coordination root as a third root it
cannot reach, and carries no identity beyond that enclosure; the hand-off list it reads is handed to it
as data, not fetched.

No meaningful cross-repo references found.

## 260921-ICR-L29 The Operation Is Bound To An Admission, Not To A Document

`ICR-R29@v1` (knowledge bootstrap initialization publication and recovery) changes this module's **front
door**, not its behaviour. The operation used to resolve every tree, identity, retry scope and root it
uses from a `WorktreeContract` — a leaf enclosure contract — so the operation's own input shape said
that a repository's knowledge can only be written by a task that already has a worktree. A repository's
*first* knowledge has no task, no leaf and no enclosure: the bootstrap handover refuses minting one to
satisfy the shape, and a second write path is the parallel-store defect the preservation boundaries
name.

So the operation is bound to `KnowledgeWriteAdmission` instead: exactly the facts it reads — the retry
`scope`, the repository name, the coordination root, the two roots, the two exact base commits, the code
work branch, and the `source_ref` document the admission was read from. `as_write_admission` is the one
coercion at the door, and a value that is already an admission is passed through **untouched**, because
its provenance is the fact being carried and re-deriving it would replace a real authority with a guess.

**What did not change is the point.** The candidate, the namespace, the identity allocation, the first
generation, the batch, the snapshot and the publication are the same shipped owners with the same
rules; the two admissions are two producers of one value, not two paths. `enclosure_admission` adapts an
existing contract and `admit_bootstrap_context` resolves the repository-bootstrap one from the settings
document and the ordinary read route, and both reach this function.

**The report gained the progress a resume needs.** `allocation_journal` names the candidate's own
allocation journal and `held_operations` is the per-entry `HeldOperation` tuple, derived by
`_held_operations` from **that journal** rather than from the plan — so a caller (and the bootstrap's
retained progress record) can see which identities the operation already holds without re-reading the
candidate. `admission_source` replaced `contract_path`/`contractPath` in the report and in the JSON
payload, because the document a run is admitted under is a settings document for a bootstrap and
calling it "the contract" was false about it.
