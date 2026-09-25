# mcp/src/agents_remember/application/knowledge_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T06:50:00+02:00 |
| lastVerifiedCommitHash | `09329a7ee598920c519b06305b73ba8e48d72c88` |
| lastVerifiedCommitDate | 2026-09-26T00:58:43+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

The Intent Reviewer's thin adapter over the shipped read, diff and view operations. It **selects
nothing itself**: it delegates which candidate a task context names to
`application/review_candidate_resolution.py`, which retained revisions the two statement sides
render to `application/review_revision_comparison.py` (ICR-R07@v1's head-selection policy, new in
leaf `260921-ICR-L7`), calls the operations, and assembles their results into
the typed payload `models/knowledge/review.py` declares. R08's comparison
result, `Route` as the recorded scope axis and L20's review matrix are consumed exactly as their
owners publish them — no scope is computed, no frontier is widened, no reference is re-resolved and no
row is re-diffed here.

**Why the composition lives here and not in `serving/`.** `layers.toml` ranks `serving` below
`application`, so a serving module may not import the application operations this adapter composes.
The dashboard reaches it the way it reaches the launch-capsule compiler: through a port on
`ServingCollaborators` that the composition root wires in `cli/dashboard.py`. The HTTP shim therefore
does transport only.

**The candidate is resolved from canonical task context, never from a path — and now it is resolved
next door.** A caller names a repository, a master and a leaf id. The leaf's enclosure contract is
located from the recorded task root, and the two datasets the comparison is between are derived from
that contract's own recorded worktree group. The current `HEAD`, a guessed worktree path and a
browser-supplied path are all unavailable as fallbacks, because none of them is reachable from this
module's inputs. **The resolution itself lives in `application/review_candidate_resolution.py`** since
this leaf: the recorded task base commit on one side, the captured add-all candidate tree on the other,
the recheck that refuses by name when either moved, and the refusals every failure earns. This adapter
imports and re-exports that module's names, so the ingest CLI's existing import of the three review
path constants keeps resolving; there is no second resolution path here.

**A request that names no selector is answerable, and it is the task context rather than an empty
subject.** `ReviewSurfaceRequest.selector` became optional for this leaf: a request with no selector
compares no knowledge operand at all — it does not select "everything" — and the payload states that
in the vocabulary's own words instead of rendering an empty statement. The source pane still carries
the complete change inventory of the bound pair, which does not depend on knowledge availability.

**Seven responsibilities now live in their own modules, and the docstring's own count is one behind
its list.** `ICR-R17@v1` advanced the docstring's heading from "Five more responsibilities" to "Six
more responsibilities" when `application/review_comparison_staleness.py` joined the list — the module
that carries the comparison's own declared identity and the staleness that identity earns against the
previous binding a refresh read supplies. A reader should carry the arithmetic rather than the heading:
that paragraph named **six** modules under a heading of "Five" before this leaf, and it now names
**seven** under a heading of "Six", so the count has been one behind its own list throughout and this
leaf's addition is the seventh name — the heading moved by one, the list by one, and neither closed the
gap. The seven are `application/review_source_inventory.py` (the exact, status-bearing source-change
inventory of the bound tree pair, and the source pane), `application/review_record_rendering.py` (the
record collections the caller supplied, rendered into the evidence and submission values),
`application/review_statement_sides.py` (one comparison item's recorded content projected into the
pane's statement sides and mechanical field rows, where ICR-R06's one-sided contract lives),
`application/review_revision_comparison.py` (which retained revisions those sides render — the before
head and the after head from the snapshots' own authored successor relationships, with explicit
ambiguity when no unique head exists, which is ICR-R07's explicit revision comparison),
`application/review_subject_catalogue.py` (the entry's labelled subject catalogue from both snapshots'
own identity tables, with totals and per-row presence and **no subject compared to earn its row**;
ICR-R09), `application/review_task_context.py` (the entry that needs no selected subject) and
`application/review_comparison_staleness.py` (the comparison's declared identity and the staleness it
earns against a carried previous binding; ICR-R17). This adapter keeps only imports and calls to them,
and every name an importer referenced is re-exported below — the statement-side helpers are the **one**
move that leaves no alias, because they were private to this adapter and no module under `mcp/`
imported them; the head-selection rule likewise leaves no alias, because the both-sides preference it
replaces was private to this adapter; the entry enumeration leaves none either, because the per-subject
compare-to-earn-a-row helpers were private to this adapter and the catalogue **replaces their mechanism
rather than moving it**; and this leaf's two helpers leave none for that identical reason, which is
recorded below — so no importer had to learn a new home and no responsibility has two implementations.

**Every absence is a state.** An unresolvable author, a missing operand, an absent assessment
collection and a comparison the shipped operation refused each produce a named field or a typed
refusal — never a blank a reader could take for a measured zero, and never a favourable default.

## Code Commentary

### Logic

**Resolution is delegated, and this module no longer defines it.** `resolve_review_candidate`,
`ReviewCandidateResolution`, `missing_dataset_half`, `review_namespace`, `refusal`, the three
`REVIEW_*` path constants and the pre-publication recheck are all
`application/review_candidate_resolution.py`'s; this adapter imports them and re-exports them in
`__all__`, which is what keeps the ingest CLI's existing
`from agents_remember.application.knowledge_review import (REVIEW_BASELINE_DIRECTORY, …)` resolving
without a second definition. What the delegation leaves here is the *call*: `read_knowledge_review` and
`list_knowledge_review_entries` resolve through that module and return a refused result immediately when
it refuses. The resolution's own rules — the three selectors screened as single path segments, the
contract located from the recorded task root, the recorded base commit as a precondition, the capture of
the add-all candidate tree, the two datasets under one disposable root, and the receipt-derived
namespace — are documented on that module's card.

**What this adapter still owns about the endpoints is where they are re-checked.** `compose_review`
calls `require_current_candidate_identity` **after** the comparison and the review-matrix read and
immediately before the payload is built, and returns the named refusal when a capture input moved while
the review was being composed. The recheck is deliberately not part of resolution: a capture that was
current when it was taken can be stale by the time a payload would be returned, and publishing that
payload would bind a generation to a candidate the leaf no longer has under a label that says it is the
candidate's own comparison.

**`missing_dataset_half` is the pair preflight, and it is what keeps an absent half a named state
rather than a storage exception.** It is the sibling module's function and its mechanism is documented
there; what matters here is that both of this adapter's callers run it before they compare —
`read_knowledge_review` (through `compose_review`) and `list_knowledge_review_entries`. A comparison is
*between* two datasets, so an absent half is not a smaller comparison: the refusal says **which** half
is missing, because "author a candidate" and "place the dataset this candidate forks from" are
different next actions a reader cannot choose between from the words "the datasets are absent". Without
it, an absent baseline made the side construction throw `CantOpenError` before the shipped operation
could return its typed `selected_input_unavailable`.

**`review_namespace` reads the namespace from the record standing beside the bytes, and that is the
only authority for it.** The function is the sibling module's; this adapter is the caller that threads
its answer through the whole render. A request names a *repository* (`agents-remember`); a dataset the
write plane placed is bound to a *namespace id* derived from it
(`uuid5(namespace, "repository:<name>")`). A side opened under the requested spelling therefore refuses
against the dataset's own binding — the fixture measured `the dataset … is bound to 40d350a6-…, not to
the requested repository namespace agents-remember` — which in the live product would have failed the
review of every real candidate. So the dataset's own **record** is read, and `repository_id` from that
record is the namespace `compose_review` opens both sides and the review matrix under.

**Two records answer, because the two halves are placed by two different acts.** `260921-ICR-L34`
corrected this: the read consulted `candidate-receipt.json` **alone**, which a *candidate* half has —
an admission wrote and sealed it — and a **before** half placed by a run handed a published
`--baseline` never does, because a published dataset is not an admitted candidate. That half carries
`baseline-generation.json` instead, written by `knowledge_baseline_generation`, and that record names
the namespace its captured bytes belong to. The rule now reads the receipt when there is one,
otherwise the before half's own generation record, and falls back to the requested repository only
when **neither** exists — the shape a caller-assembled pair has. The consequence was a product defect:
before the correction the before half of every continuity run was opened under the requested
repository while its bytes were bound to a namespace id, the storage owner refused the mismatch, and
the freeze answered `candidate_dataset_absent` — so **no leaf on the ordinary `knowledge-ingest
--baseline` route could record its comparison**. A dataset with **neither** record beside it keeps the
requested identity, and a record that **exists but cannot be read** is refused, because standing in the
caller's word for the dataset's own record is exactly how a review comes to read a namespace nothing
admitted.

**`list_knowledge_review_entries` is the surface's entry half, and it exists because the reviewed
subject is the one input a reader cannot supply.** The subject is a recorded identity inside the
comparison's before/after pair, and the browser must not choose the candidate, so the task view asks
the server instead of guessing. It resolves through the *identical* operation `read_knowledge_review`
uses — canonical task context only, one contract, one derived root — so the list a caller is offered
and the review it then opens cannot disagree about which datasets are being compared. **The catalogue
is enumerated, not compared:** since this leaf (`260921-ICR-L9`, `ICR-R09@v1`) the entry half
delegates to `application/review_subject_catalogue.py`'s `read_subject_catalogue(resolved)` — every
invariant and family identity the pair's before/after snapshots record is listed with its label, its
per-row `presence` and the labelled totals, and **no subject is compared to earn its row**. The old
per-subject mechanism (a subject offered exactly when the shipped comparison answered for it, each
compared through `diff_knowledge_scope`, a refused one dropped by `_selected_item_count` returning
`None`) is **deleted, not moved** — it was the verified F06 defect this packet owns, "the API returns
multiple entries but only the first is reachable" in its entry-half shape, and it silently dropped a
retired (before-only) subject entirely. What one subject's review renders stays the comparison's own
answer when that subject alone is opened. The adapter fills the totals itself — `total_subjects`
counts the rows, split once into `invariant_total`/`family_total` — and a candidate that records no
identity yields an empty list, which the caller renders as no entry beside the source inventory
rather than as an invitation to name one. **Both pair refusals are therefore stated before any
subject is listed** — the absent half first, and since leaf `260921-ICR-L5` the unreadable half
beside it (see the paragraph below) — because the catalogue read opens both snapshots and a side no
catalogue can open would otherwise raise out of the call that exists to offer a subject.

**A side that is present but cannot be read is a named refusal on both routes, and leaf
`260921-ICR-L5` added the two call sites that make it so.** `missing_dataset_half` answers *absence*;
the sibling fact — a file that is there and is not a dataset of this code — used to reach SQLite and
come back as an `apsw.NotADBError` raised from inside the comparison, so an operator got a traceback
where this surface promises a state naming the side. `unreadable_half_refusal(baseline, candidate)` (in
[`application/knowledge_before_half.py`](knowledge_before_half.py.md)) preflights both sides — the
before half through its recorded origin as well as its bytes — and returns the typed refusal or `None`.
`compose_review` states it after its own docstring and before `missing_dataset_half`, and
`list_knowledge_review_entries` states it after its absent-half check and before the catalogue read,
so both routes answer the same way and "the before side is unreadable" stays a different state from
"the before side is absent". The refusal reuses the shipped `candidate_dataset_absent` code rather than
widening a shared refusal vocabulary the transport and the renderer both read; the state travels in the
detail and the offending input. The change to this adapter is exactly one import and those two call
sites — 13 lines — and it is a deliberate contract with the seam policy's "keep the adapter a
delegator" rule, not new feature logic: the readers, the states and the refusal all live in the new
module, and what stays here is only *where* in the two routes the answer is stated.

**`read_knowledge_review` is the whole public comparison operation and it resolves before it
composes.** It calls the sibling module's `resolve_review_candidate`, returns `_refused(...)`
immediately when that yields a `ReviewRefusal`, and otherwise delegates to `compose_review`. The
`contract` is carried on the resolution so a caller that also needs the recorded task facts reads them
from the same resolution rather than resolving twice.

**`compose_review` measures the source observation once and hands it to both renderings, then
splits on whether a subject was named, and re-checks the captured endpoints last.** The two tree
sides are built and the observation is made before any dataset is opened and before the selector
branch, from the two tree ids the resolution bound: it is the one half of a review that cannot
depend on a knowledge selection, and measuring it only after a comparison succeeded is how a task
with no invariant — or with no datasets at all — came to lose its source review entirely.
`review_inventory` renders that same observation (the `observed` input, not a second measurement),
and the task-context branch hands it to `pair_attribution` as the partition's denominator. A request
with **no selector** is then answered by `review_task_context.task_context_review`, which composes
`comparison=None`, `staleness.state="not_compared"` and a knowledge pane in the `task_context`
selection state, so an absent knowledge half stays a stated fact rather than a refused read. A
request that **does** name a selector keeps the shipped behaviour exactly, with one narrowing:
`_open_dataset_pair` refuses an absent dataset half and an unreadable candidate receipt through the
shared refusal owner (`unreadable_candidate_refusal` in `review_candidate_resolution.py`, the only
place the code, detail, next action and offending input exist), and reads the namespace once through
`review_namespace` so one render cannot open its two sides and its matrix under two different
namespaces; `_compare` then calls the shipped comparison, and a comparison
that is not `state == "page"`, or that carries no page or no binding, becomes a `comparison_refused`
result through `_comparison_refusal`, which carries the shipped refusal's own `code`, `detail` and
`next_action` through verbatim rather than inventing a summary. `_selector_kind_or_absence` is what lets
that refusal spell a selector that is absent as `"no selector"` instead of reading `kind` through
`None`. The subject route's pane attribution is the comparison's own partition, carried verbatim by
`_comparison_attribution` — never recomputed here, because a second measurement could only disagree
with the one the payload's expansion already publishes.

**The reviewed identity's explicit revision selection is computed once in `compose_review`, from the
comparison's own union items and the two snapshots' own authored edges, and the pane renders it.**
`select_subject_revisions(page.items, request.selector, repository_id=comparison.repository_id,
before_database=resolved.baseline_database, after_database=resolved.candidate_database)` is the one
call, placed after the staleness measurement and before the payload is built, and `_knowledge_pane`
receives its answer (`selected`) instead of the selector — the adapter resolves, calls and
assembles, and the head rule lives in its own module. A selector that names no identity selects no
revision, exactly as the both-sides preference this replaces did.

**The review matrix is read from the candidate through L20's operation, not recomputed.**
`read_knowledge_view` is handed the candidate database, the diff side opened by `open_diff_side` over
the same database and code root, and a `ViewRequest(view="review_matrix", record_kinds=REVIEW_MATRIX_KINDS)`.
A view that is not `state == "view"` becomes `comparison_refused` with the view's own detail appended,
so the surface never renders a pane from a partial matrix. `REVIEW_MATRIX_KINDS` is the *input* the
view is asked for — the five record kinds — rather than a selection policy of this leaf's; the view
applies its own registered traversal over them.

**The matrix's own answer is what states the two matrix-owned collections' availability, and the
composition reports it rather than deriving it.** Immediately after the rows are in hand,
`compose_review` calls `review_evidence_records.with_selection_channels(records, rows, selected=True,
rows_remaining=_rows_remaining(matrix))`, which adds the `authored_effects` channel from the rows the
view returned and carries the view's **own** declared bound: `_rows_remaining` reads
`payload.counts.rows_remaining` off the served view, so a review that rendered a bounded page reports
the bound instead of presenting the page it read as the whole selection. The task-context branch of the
same composition calls the identical function with `selected=False` — a review that read no matrix did
not ask, and "did not ask" is a different fact from an owner answering that it holds none.

**The five subjects the payload states are assembled from the matrix rows and the supplied records,
and the two authored/mechanical collections never mix.** `_knowledge_pane` renders identities, both
sides' exact statements and conditions, the retained-revision groups, every field transition the
comparison reported, the authored records (`AUTHORED_EFFECT_KINDS`), the detection signals, the
assessment displays and one unresolved-author reference per authored row. The other two panes are no
longer composed here: `source_pane` (in `review_source_inventory`) renders the inventory first and
then the measured attribution partition — the selected locations, the six published remaining
counts, the expansion reference and command, and the three bucket lists read from the partition
value — with `evidence_pane` (in `review_record_rendering`)
renders the evidence links, the observations and the assessments, with `evidence_state` and
`assessment_state` computed from the collections themselves. Both are the same functions the
task-context composition calls, which is what keeps an unassessed collection reading identically in
both.

**Pane 1's statement sides and field roster are delegated too, and the one wire-visible behavior this
leaf changed lives in that delegation.** `_knowledge_pane` calls
`application/review_statement_sides.py`'s `side_content` for both sides, `side_conditions` for both
condition tuples and `field_changes(items)` for the roster — the same four names under their new,
public spellings, with the module's own `read_side` replacing the adapter's private one. The
behavioral delta is inside `field_changes`' value reader: a **changed structured field** used to be
reported as `None` on both sides (`_field_text` returned `None` for any `dict`), which states an
absence the snapshot does not hold — and on a field the comparison reports as *changed*, two of them
at once. Each side now carries `structured_value_text` of the value that side really holds, and
`None` stays reserved for the two real absences (no record at all; no value recorded for that field).
The statement-side contract therefore has one implementation, in a module named for it, and this
adapter keeps only *that* it asks for the sides and *where* it puts them.

**Pane 1's two operands are the reviewed identity's selected revisions, and the deleted
prefer-both-sides rule is what this leaf removed to make that true.** `_knowledge_pane` no longer
takes the selector and no longer prefers the item present on both sides (`_identity_item` and
`_selector_record_id` are deleted, not moved: they were private to this adapter and no module under
`mcp/` imported them). It takes the head selection, renders the selected head items' sides through
`_selected_statements` — a compared or one-sided selection renders the heads' own recorded sides, so
a known-empty side stays the absent state ICR-R06 already gives it — and an ambiguous or unresolved
selection renders no head's text as the subject's operand: both sides carry the explicit statement
that says why no pair was chosen, with empty conditions, while the recorded selection beside them
(`revision_selection` on the pane) still lists every head and every retained revision. The
wire-visible change is therefore twofold: a unique chain now compares the before head to the after
head instead of the retained predecessor, and a branched identity renders an explicit ambiguity
instead of a silently chosen pair.

**Staleness and submission are two statements of one fact, and in this leaf the rule itself moved out while the coupling stayed here.** `comparison_identity` and `review_staleness` are
[`application/review_comparison_staleness.py`](review_comparison_staleness.py.md)'s, and the two private
helpers that used to hold them in this adapter (`_comparison_identity`, `_staleness`) are **deleted, not
annotated**: nothing under `mcp/` imported them, so the extraction leaves no alias and `__all__` is
unchanged. What stays here is the call and the reading. `compose_review` computes the identity once
with `comparison_identity(comparison)` immediately after the comparison and the review-matrix answer,
calls `review_staleness(identity, request.previous_binding_digest)`, reads `staleness.state == "stale"`
for the submission state **and** publishes that same `staleness` value on the payload — one
measurement, so "an assessment is never submitted against a comparison that has moved" cannot be true
of one field and false of the other. The previous identity is no longer a keyword beside the request
either: `read_knowledge_review` and `compose_review` lost their `previous_binding_digest` parameter and
read it from `ReviewSurfaceRequest.previous_binding_digest`, which is one spelling of what was asked.
`submission` returns `disabled_stale` exactly when stale and `unavailable` otherwise, and in both cases
publishes `PROPOSED_ASSESSMENT_DISPOSITIONS` rather than a control of this module's own.
`KnowledgeReviewPayload`'s validator refuses the payload where the two disagree, so "an assessment is
never submitted against a comparison that has moved" is a property of the value; its second validator
holds the identity and the staleness state in agreement the other way round, so `comparison is None` is
true exactly when the state is `not_compared` and the knowledge pane's `selection_state` says which
question the payload answered.

**The inventory's own state is a declared limit of the response, not a pane detail.** `_limitations`
carries the comparison's limits and counted omissions **and** `inventory_limitations(inventory)`, so an
unavailable measurement (`limitation:source_inventory_unavailable`) and a partial one
(`limitation:source_inventory_partial`) are named at the top level beside the comparison's own
limitations — a limit a reader has to open a pane to discover is a limit the response did not state.
The task-context composition adds `limitation:no_knowledge_subject_selected` beside them.

**Six counts are published, and a count that has no meaning says so instead of reporting zero.**
`locations_remaining` and `records_present_outside_selection` are measured from the page;
`references_unresolved` is the page's own `suppressed_total`; and
`changed_paths_outside_selection`, `unattributed_changed_paths` and
`unknown_attribution_changed_paths` carry `value=None` with a stated
reason when the comparison published no source expansion, because "not measured here" and "measured as
none" are different facts. `ReviewRemainingCount`'s validator refuses an unexplained absent count and
refuses a measured count that also carries a not-applicable reason.

**`review_records_for` left this module for the record owner, and the name here is a re-export**
(`ICR-R14@v1`). The resolver used to read the published assessment collection and collapse an absent
authority and an unreadable one into `EMPTY_REVIEW_RECORDS`; both of those are now *states* on the
bundle, and the whole collection resolution lives in
[`application/review_evidence_records.py`](review_evidence_records.py.md). The adapter keeps the name in
`__all__` and imports it from the owner (the import block at the top of the file is the re-export), so
`cli/dashboard.py` and the test modules that import `review_records_for` from here keep resolving
without a new home to learn — the same convention this module already follows for
`resolve_review_candidate`, `candidate_ref` and `ReviewRecordInputs`. `AUTHORED_EFFECT_KINDS` moved
with it for the same reason and is imported back here: the kinds a channel counts and the kinds
`_knowledge_pane` renders are one declaration, so they cannot drift.

### Conventions

The module holds no vocabulary of its own: every value it returns is a shipped type — the review
models from `models/knowledge/review.py`, the diff models, the detection payload and the read models.
`ReviewSurfaceRequest` is imported for re-export and named in `__all__` beside
`read_knowledge_review`, `list_knowledge_review_entries`, `compose_review`, `review_records_for`,
`ReviewRecordInputs`, `EMPTY_REVIEW_RECORDS` and `REVIEW_MATRIX_KINDS`, and beside the names that are
**re-exported** from the extracted modules — since `ICR-R14@v1`, the record owner's `review_records_for`
and the `AUTHORED_EFFECT_KINDS` that owner now declares (imported here for `_knowledge_pane` and for
that re-export) — `review_candidate_resolution`'s
`resolve_review_candidate`, `ReviewCandidateResolution`, `REVIEW_CANDIDATE_RELATIVE_ROOT`,
`REVIEW_BASELINE_DIRECTORY`, `REVIEW_CANDIDATE_DIRECTORY` and (in the reference table below)
`candidate_ref`, `missing_dataset_half`, `review_namespace` and `refusal`; and
`review_record_rendering`'s `ReviewRecordInputs` and `EMPTY_REVIEW_RECORDS`, which are declared there
and imported here so the ingest CLI and the test modules that import them keep resolving.
**`review_statement_sides`' five names are the deliberate exception**: `side_content`,
`side_conditions`, `field_changes`, `field_text` and `read_side` are imported for use and **not**
re-exported under their former private spellings (`_side_content`, `_conditions`, `_field_changes`,
`_field_text`, `_read_side`), because no module under `mcp/` imported those names — so there is no
importer to keep resolving and no alias to justify. `__all__` is therefore unchanged by this
extraction: the statement-side helpers were always private to this adapter.
`ReviewRecordInputs` and `ReviewCandidateResolution` are frozen dataclasses rather than pydantic
models, because they carry live paths and a loaded contract rather than a wire shape. `refused` — the
extracted record renderer's — is the single builder of a refused result **reached from this module**,
and `refusal(...)` — the resolution module's — the single builder of a refusal value, so no code path
in this module raises out of `read_knowledge_review`. The private helpers that remain are deliberately
one-purpose: `_selected_statements` renders one head selection's two statement sides and their
conditions (the heads' own recorded sides, or the explicit ambiguity on both sides with empty
conditions); `_selector_kind_or_absence` narrows
the optional selector at the one place a refusal spells it; `_entry_refused` is the entry route's single builder
of a refused list — the
spelling the merged candidate carries, which the code-side sync's reapplication kept as it was (the
card's first pass had recorded the pre-sync candidate's one-word `_entryrefused`; see the history);
`_review_matrix` reads L20's view or returns the refusal it earned; and the head-selection import
(`select_subject_revisions`, `SubjectRevisionSelection`) is deliberately **not** re-exported: the
both-sides preference it replaces was private to this adapter, so there is no importer to keep
resolving and no alias to justify — the same rule the statement-side move followed. The catalogue
import (`read_subject_catalogue`, `ICR-R09@v1`) follows the same rule: it is imported **for use**, not
re-exported, because the per-subject helpers it replaced (`_reviewable_entries`,
`_recorded_identities`, `_selected_item_count`) were private to this adapter — there is no importer to
keep resolving, and `__all__` is unchanged by the extraction.

### Invariants And Boundaries

- **The adapter applies no rule of its own.** The comparison, the item identities, the counts, the field
  transitions and the revision groups are the shipped operations' own values; the module adds no
  ordering, no ranking, no filter and no re-diff — and the head selection is the policy module's,
  computed once in `compose_review` from the comparison's own union items and the snapshots' own
  authored edges. The entry list obeys the same rule since `ICR-R09@v1`: it offers exactly the union
  of the two snapshots' own recorded identities — no comparison runs to earn a row, no row is dropped
  for being unselectable, and no ranking is applied — so it is not a selection policy in disguise.
- **No path is accepted from a caller.** The candidate dataset is derived from the located enclosure
  contract's recorded worktree group; `HEAD`, a guessed worktree and a browser-supplied path are all
  unreachable from the module's inputs. The entry route's inputs are the task context and nothing else.
- **The two directory names are published, not private.** `REVIEW_BASELINE_DIRECTORY` and
  `REVIEW_CANDIDATE_DIRECTORY` are the one spelling two owners read — this adapter resolving the pair
  and the ingest CLI authoring into it — so the write side and the read side cannot drift apart.
- **An absent dataset half is a named state, never an exception.** `missing_dataset_half` runs before
  any comparison and the refusal names which half is missing.
- **The namespace is the dataset's own, read from its receipt.** Both sides of a comparison and the
  review matrix are opened under the candidate's recorded namespace; the requested repository name is
  used only when no receipt exists, and a receipt that exists but cannot be read is refused rather than
  guessed past.
- **A side with no exact tree is no longer a supported state of a review.** The endpoints are bound by
  `review_candidate_resolution`: the baseline is the contract's recorded base commit and the candidate
  is the captured add-all tree, and a contract that records no base commit is refused by name rather
  than resolved with an absent tree. The `| None` field types survive only for a resolution assembled
  by hand (a caller comparing two named files), which has no contract and no capture to bind.
- **A moved capture input is refused before the payload is built.** `compose_review` calls
  `require_current_candidate_identity` after the comparison and the matrix read, and
  `task_context_review` calls it after the inventory is measured; a moved input returns the named
  refusal carrying the two identities it compared — never a stale publication.
- **No selector is a state, not an empty subject.** A request whose `selector` is `None` compares no
  knowledge operand: the payload carries `comparison=None`, `staleness.state="not_compared"` and a
  knowledge pane whose `selection_state` is `task_context` with its reason, and the source pane still
  carries the complete inventory. The task-context path never opens a dataset, never reads the review
  matrix and never reaches a comparison refusal.
- **One responsibility, one implementation.** The inventory, the record rendering, the statement-side
  projection and the task-context composition each live in exactly one module; this adapter imports
  and calls them and re-exports what moved. Two implementations of "what did these two trees change"
  — the review's inventory and the comparison's expansion — were collapsed into one by this leaf.
- **A field row's `None` means absence, and the comparison's roster is the roster.** The statement-side
  module owns both rules; this adapter neither widens the roster nor reconstructs a structured value
  as a `None` of its own, and a changed structured field is served as each side's own projection.
- **A subject the comparison refuses is still listed, and its reason is carried by the review it
  opens.** The catalogue never drops a recorded identity to imply a smaller complete population; a
  recorded but unselectable subject opens to the comparison's own typed refusal, which names the
  subject and its reason, while the other subjects and the task-context source review stay
  accessible. (Until this leaf the opposite rule held — `_selected_item_count` returned `None` for a
  refused comparison and the entry was omitted — and that rule was the F06 defect this packet owns.)
- **Unassessed is the absence of a value.** No `current` measurement means every stored assessment is
  displayed `stale`; a candidate with no published assessment displays `unassessed` rather than a
  clearance.
- **An unresolved reference is displayed, never dropped and never made anonymous.** `_unresolved_author`
  names the record and states that the matrix publishes no author; the evidence pane names the coverage
  the matrix does not publish; the source pane names every item held by only one snapshot.
- **The module defines no record kind and stores nothing.** It opens the candidate read-only through
  the shipped operations and writes no file; `REVIEW_CANDIDATE_RELATIVE_ROOT` is a location it *reads*.
- **Rank is the reason for the ports.** `serving/review.py` takes `read_knowledge_review` and
  `list_knowledge_review_entries` as ports supplied by the composition root, because a serving module
  may not import them.

### Todos

None recorded. The one leftover this card previously recorded — the dead `_IDENTITY_ITEM_KINDS`
constant (`knowledge_review.py:172` at the L7 candidate) — no longer exists anywhere under `mcp/src`
at this leaf's base `f141d164` or in this candidate (measured by grep), so the recorded leftover is
retired rather than carried.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the adapter's own docstring and
functions, the four modules that now own resolution, the source inventory, the record rendering and
the statement-side projection, the shipped comparison and view operations it calls, the models module
that declares the payload, and the test modules that drive the whole surface. Five details a reader
should carry: **the resolution is not defined here any more** — the three `REVIEW_*` path constants,
`resolve_review_candidate`, `ReviewCandidateResolution`, `missing_dataset_half`, `review_namespace`,
`refusal` and `require_current_candidate_identity` are
`application/review_candidate_resolution.py`'s and are imported/re-exported here, which is the import
path `cli/knowledge_ingest.py` still uses; **the source half and the record rendering moved out in
this leaf's predecessor** — `review_inventory`, `source_pane`, `inventory_limitations`,
`tree_difference_observation` and the source pane's own `_location` are
`application/review_source_inventory.py`'s, and `refused`, `submission`, `evidence_pane`,
`subject_states`, `assessment_displays`, `signal` and `observation` are
`application/review_record_rendering.py`'s, so `__all__` is unchanged while the implementations are
not here; **the statement sides and the field roster moved out in this leaf** — `side_content`,
`side_conditions`, `read_side`, `field_changes` and `field_text` are
`application/review_statement_sides.py`'s, they are the one move that leaves no alias, and the
wire-visible change that came with them is that a changed structured field is served as each side's
own projection instead of `None`; both halves' directory names are **published** because the ingest
CLI authors into the same root; and the candidate side resolves to **both** a code root and a tree id,
from the capture, because a recorded base commit is a precondition and the add-all candidate tree is
what the anchors are resolved against.

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter's own statement of what it selects (nothing), why the composition sits at this tier rather than in `serving/`, how the candidate is resolved from task context rather than from a path, that the endpoints are bound next door, and that **six** more responsibilities now live in their own modules — the last three the statement-side projection (ICR-R06), the head-selection policy (ICR-R07) and the subject catalogue (ICR-R09), each the one move (or replacement) that leaves no alias. | `resolve_review_candidate`; `require_current_candidate_identity`; `review_source_inventory`; `review_statement_sides`; `review_revision_comparison`; `review_subject_catalogue`; `review_task_context` | mcp/src/agents_remember/application/knowledge_review.py:1-56; mcp/src/agents_remember/application/knowledge_review.py:65-139; mcp/src/agents_remember/application/review_candidate_resolution.py:138-202; mcp/src/agents_remember/application/review_candidate_resolution.py:224-254 |
| **The published adapter surface: the three entry points, the two dataclasses, the request model and the record-kind constant — and, re-exported from the sibling modules, the resolution callable, the resolution value, `candidate_ref` and the three published path constants.** | `__all__` |mcp/src/agents_remember/application/knowledge_review.py:176-199|
| The re-export itself: the import block that makes the sibling modules' names this module's public surface and keeps the ingest CLI's existing import resolving — the resolution surface and `candidate_ref` from `review_candidate_resolution`, and `EMPTY_REVIEW_RECORDS`/`ReviewRecordInputs` from `review_record_rendering`. | `resolve_review_candidate`; `REVIEW_BASELINE_DIRECTORY`; `refusal`; `candidate_ref`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/knowledge_review.py:65-139; mcp/src/agents_remember/application/review_candidate_resolution.py:138-202; mcp/src/agents_remember/application/review_candidate_resolution.py:86-86; mcp/src/agents_remember/application/review_candidate_resolution.py:374-388; mcp/src/agents_remember/application/review_candidate_resolution.py:205-221 |
| The record kinds the review matrix is asked for — an input to L20's view rather than a selection policy of this module's — and the authored kinds the knowledge pane separates from the mechanical signals, which the record owner now **declares** and this module imports back so the counted collection and the rendered one cannot drift. | `REVIEW_MATRIX_KINDS`; `AUTHORED_EFFECT_KINDS` | mcp/src/agents_remember/application/knowledge_review.py:211-219; mcp/src/agents_remember/application/review_evidence_records.py:132-134 |
| The record input set, its frozen shape and its single module-level empty value — now declared in the extracted record renderer and imported here, so `review_records_for` and the ingest CLI keep resolving. | `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/review_record_rendering.py:85-111; mcp/src/agents_remember/application/knowledge_review.py:65-139 |
| **The resolution value — now the sibling module's: the two datasets, the two code roots, the two tree ids, the carried contract and the captured identity the recheck re-derives, and the record a closed leaf's review was reopened from.** | `ReviewCandidateResolution` | mcp/src/agents_remember/application/review_candidate_resolution.py:120-157 |
| The one contract locator, now the sibling module's: the recorded task root, the globbed enclosures, the `repo_name`/`cleanup` skips and the leaf-id slug match. | `recorded_leaf_contract`; `load_contract`; `slugify` | mcp/src/agents_remember/application/review_candidate_resolution.py:473-500; mcp/src/agents_remember/worktrees/worktree_contract.py:437-467; mcp/src/agents_remember/worktrees/task_resolver.py:16-27 |
| **The whole comparison operation: delegate the resolution, then compose, with a refused resolution returned as a refused result before any comparison runs.** | `read_knowledge_review`; `refused` | mcp/src/agents_remember/application/knowledge_review.py:220-249; mcp/src/agents_remember/application/review_record_rendering.py:186-193 |
| **The entry operation: the same resolution as the comparison, then the catalogue read — every recorded identity of both snapshots listed with presence and totals, no subject compared to earn its row — with the unreadable-receipt preflight stated before that read. The enumeration itself is `review_subject_catalogue`'s, and the per-subject compare-to-earn-a-row helpers this module used to own are deleted.** | `list_knowledge_review_entries`; `read_subject_catalogue`; `unreadable_half_refusal`; `candidate_receipt_refusal` |mcp/src/agents_remember/application/knowledge_review.py:238-307; mcp/src/agents_remember/application/review_subject_catalogue.py:47-69; mcp/src/agents_remember/application/knowledge_before_half.py:347-377; mcp/src/agents_remember/application/review_candidate_resolution.py:403-416|
| **The catalogue's own population read, which the entry operation delegates to: both snapshots' identities through the store's own two list operations, and the globally kind-grouped union with per-row presence.** | `_side_identities`; `_union`; `list_invariants`; `list_families` | mcp/src/agents_remember/application/review_subject_catalogue.py:72-87; mcp/src/agents_remember/application/review_subject_catalogue.py:90-112; mcp/src/agents_remember/memory/knowledge/store.py:181-197; mcp/src/agents_remember/memory/knowledge/store.py:199-214 |
| **The pair preflight and the pair this leaf opened out of it: the absent half named as `baseline` or `candidate`, the sibling fact beside it (a side that is present but cannot be read), the unreadable receipt refused through the shared owner, and the step that runs both only when a subject was named — because a task-context review compares no dataset.** | `missing_dataset_half`; `unreadable_half_refusal`; `unreadable_candidate_refusal`; `_open_dataset_pair` | mcp/src/agents_remember/application/review_candidate_resolution.py:330-348; mcp/src/agents_remember/application/knowledge_before_half.py:347-377; mcp/src/agents_remember/application/knowledge_review.py:713-785; mcp/src/agents_remember/application/review_candidate_resolution.py:402-417 |
| **The record-beside-the-bytes namespace this adapter threads through the whole render: the candidate's own sealed receipt when there is one, otherwise the before half's own `baseline-generation.json`, the requested repository used only when neither record exists, and an unreadable record refused rather than guessed past.** | `review_namespace`; `CANDIDATE_RECEIPT_NAME`; `read_baseline_generation` |mcp/src/agents_remember/application/review_candidate_resolution.py:351-399; mcp/src/agents_remember/models/knowledge/snapshot.py:53-53; mcp/src/agents_remember/application/knowledge_baseline_generation.py:285-316|
| The entry route's single refusal builder, carrying the resolution's own refusal verbatim. | `_entry_refused` | mcp/src/agents_remember/application/knowledge_review.py:282-294 |
| **The composition: the observation made once and handed to both renderings, the task-context branch, the three pair refusals (absent, unreadable receipt, unreadable dataset), the comparison, the matrix read through the shipped view operation with its selection channels stated, the endpoint recheck immediately before the payload, and the panes with staleness, submission and the declared limits.** | `compose_review`; `require_current_candidate_identity`; `read_knowledge_view`; `ViewRequest`; `unreadable_half_refusal`; `candidate_receipt_refusal`; `with_selection_channels`; `_matrix_rows_remaining` | mcp/src/agents_remember/application/knowledge_review.py:353-541; mcp/src/agents_remember/application/review_candidate_resolution.py:272-301; mcp/src/agents_remember/application/knowledge_views.py:86-112; mcp/src/agents_remember/models/knowledge/view.py:1117-1148; mcp/src/agents_remember/application/knowledge_before_half.py:347-377; mcp/src/agents_remember/application/review_candidate_resolution.py:420-433; mcp/src/agents_remember/application/review_evidence_records.py:264-289; mcp/src/agents_remember/application/knowledge_review.py:612-625 |
| **The recorded before/after relationship union traversed from the comparison's own page items and threaded into the source pane (`ICR-R08@v1`): one call, and the adapter adds no traversal logic of its own.** | `relationship_movements`; `RelationshipSources`; `source_pane` | mcp/src/agents_remember/application/review_relationship_movement.py:142-177; mcp/src/agents_remember/application/review_relationship_movement.py:123-139; mcp/src/agents_remember/application/review_source_inventory.py:560-613 |
| **The comparison's own partition carried verbatim — never recomputed, because a second measurement could only disagree.** | `_comparison_attribution` |mcp/src/agents_remember/application/knowledge_review.py:562-586|
| The review matrix read as its own step, so the composition reads as measure, branch, open, compare, read, recheck, publish. | `_review_matrix` |mcp/src/agents_remember/application/knowledge_review.py:750-822|
| The shipped comparison call over the two already-resolved sides, with the probe and the candidate's own namespace passed through and no side or selector added. | `_compare`; `diff_knowledge_scope` |mcp/src/agents_remember/application/knowledge_review.py:544-559; mcp/src/agents_remember/application/knowledge_diff.py:184-238|
| The narrowing that lets a comparison refusal name a selector that is *absent* as `"no selector"` instead of reading `kind` through `None`, and the refusal it feeds. | `_selector_kind_or_absence`; `_comparison_refusal` | mcp/src/agents_remember/application/knowledge_review.py:942-951; mcp/src/agents_remember/application/knowledge_review.py:954-973 |
| **The comparison identity carried verbatim — now owned by [`application/review_comparison_staleness.py`](review_comparison_staleness.py.md): this leaf moved the identity helper out of this adapter and **deleted** its private `_comparison_identity` rather than keeping it as an alias, because nothing under `mcp/` imported it.** | `comparison_identity` | mcp/src/agents_remember/application/review_comparison_staleness.py:51-73 |
| The comparison's declared limits, omissions and side-absences **plus the inventory's own state**, carried as counted facts at the top level. | `_limitations`; `inventory_limitations` | mcp/src/agents_remember/application/knowledge_review.py:905-928; mcp/src/agents_remember/application/review_source_inventory.py:179-191 |
| **The staleness rule — now owned by the sibling module: agreement, or an absent previous binding, is `current`; disagreement is `stale` with the carried identity retained as the labelled previous input and the moved axis named. This leaf deleted the private `_staleness` rather than keeping it as an alias.** | `review_staleness` | mcp/src/agents_remember/application/review_comparison_staleness.py:76-97 |
| **Submission as the other statement of the same fact, and the payload validators that refuse a payload where the two disagree — including the one that ties `comparison is None` to `not_compared` and to the knowledge pane's selection state.** | `submission`; `KnowledgeReviewPayload`; `_require_the_submission_state_to_follow_staleness`; `_require_the_identity_and_staleness_to_agree` | mcp/src/agents_remember/application/review_record_rendering.py:183-210; mcp/src/agents_remember/models/knowledge/review.py:1030-1126 |
| The panes: identities and authored records never rendered as mechanical facts, the whole-task inventory, the six published remaining counts and the measured partition, and the evidence pane's two independent absence states — the last two now the extracted modules' own functions, called by both compositions. | `_knowledge_pane`; `source_pane`; `evidence_pane` | mcp/src/agents_remember/application/knowledge_review.py:926-1002; mcp/src/agents_remember/application/review_source_inventory.py:560-613; mcp/src/agents_remember/application/review_record_rendering.py:213-252 |
| **Pane 1's delegation, and the one wire-visible change this leaf made: the import of the statement-side module and the four calls inside `_knowledge_pane` that replaced the adapter's private `_side_content`/`_conditions`/`_field_changes`, where a changed structured field is now served as each side's own projection instead of `None`.** | `side_content`; `side_conditions`; `field_changes`; `_knowledge_pane` | mcp/src/agents_remember/application/knowledge_review.py:926-1002; mcp/src/agents_remember/application/review_statement_sides.py:86-117; mcp/src/agents_remember/application/review_statement_sides.py:120-124; mcp/src/agents_remember/application/review_statement_sides.py:135-155 |
| **The cases that measure this adapter's one-sided output through the real composition: an addition, a removal, a one-sided field row, and a structured value served as its own projection on both sides.** | `test_an_added_statement_renders_its_after_text_beside_a_named_absent_before`; `test_a_removed_statement_renders_its_before_text_beside_a_named_absent_after`; `test_a_structured_field_value_is_rendered_as_its_own_text_and_never_as_an_absence` | mcp/tests/test_knowledge_review_one_sided_statements.py:249-269; mcp/tests/test_knowledge_review_one_sided_statements.py:272-285; mcp/tests/test_knowledge_review_one_sided_statements.py:320-350 |
| The per-subject assessment projection that reports an unmeasured assessment stale rather than promoting it to current — now the extracted record renderer's, so both compositions display an unassessed collection identically. | `subject_states`; `assessment_state_for` |mcp/src/agents_remember/application/review_record_rendering.py:255-274; mcp/src/agents_remember/models/lifecycles/review_assessment.py:542-594|
| The assessment displays and the observation displayed exactly with no sufficiency field, and the detection fact with no severity — all the extracted renderer's. | `assessment_displays`; `_assessment_display`; `observation`; `signal` | mcp/src/agents_remember/application/review_record_rendering.py:277-302; mcp/src/agents_remember/application/review_record_rendering.py:305-322; mcp/src/agents_remember/application/review_record_rendering.py:431-453; mcp/src/agents_remember/application/review_record_rendering.py:456-473 |
| **The deleted prefer-both-sides rule and what replaced it: `_identity_item` and `_selector_record_id` are gone, and the pane renders the head selection instead.** The old rule preferred the item present on both sides — the retained predecessor both snapshots happen to hold — and used a one-sided item only for additions/removals. `ICR-R07@v1` deletes that preference: `compose_review` computes the before/after head pair from authored successor edges and `_knowledge_pane` renders it through `_selected_statements`, with ambiguity or unresolved lineage rendered as an explicit non-pair. | `_selected_statements`; `select_subject_revisions`; `revision_selection` | mcp/src/agents_remember/application/knowledge_review.py:117-1004; mcp/src/agents_remember/application/knowledge_review.py:1057-1080; mcp/src/agents_remember/application/knowledge_review.py:1002-1054; mcp/src/agents_remember/application/knowledge_review.py:100-100; mcp/src/agents_remember/application/knowledge_review.py:371-371 |
| The selected source location, now rendered by the recorded-relationship display owner from the movement side (`ICR-R08@v1`), with the recorded role kept `None` rather than guessed and the counterpart address named only when the other side records exactly one. | `_location`; `_counterpart_path`; `_baseline_only` | mcp/src/agents_remember/application/review_relationship_display.py:791-821; mcp/src/agents_remember/application/review_relationship_display.py:835-848; mcp/src/agents_remember/application/review_relationship_display.py:824-832 |
| The comparison's own statement about one claim's source observation, carried verbatim by the recorded-relationship owner (the moved `_change_state`), and the realization payload the recorded side is read from — the deleted `_realization_read_item` was that payload selection, now `side_payload`/`read_snapshot_relationships` in the same owner. | `recorded_change_state`; `side_payload`; `read_snapshot_relationships` | mcp/src/agents_remember/application/review_recorded_relationships.py:593-603; mcp/src/agents_remember/application/review_recorded_relationships.py:452-455; mcp/src/agents_remember/application/review_recorded_relationships.py:458-475 |
| **The source half's own measurement: the delimiter-safe probe, the inventory value, its command, whether a name can be carried as text, and the byte form a name that cannot is carried by.** | `tree_difference_observation`; `review_inventory`; `inventory_command`; `is_text_path`; `byte_form` | mcp/src/agents_remember/application/review_source_inventory.py:194-236; mcp/src/agents_remember/application/review_source_inventory.py:429-469; mcp/src/agents_remember/application/review_source_inventory.py:411-426; mcp/src/agents_remember/application/review_source_inventory.py:239-249; mcp/src/agents_remember/application/review_source_inventory.py:252-261 |
| **The entry that needs no subject: `comparison=None`, `staleness.state="not_compared"`, a knowledge pane in the `task_context` selection state, the measured pair attribution, and the reason it names — including an absent or unreadable dataset half when there is one.** | `task_context_review`; `task_context_detail`; `_task_context_pane`; `pair_attribution` | mcp/src/agents_remember/application/review_task_context.py:84-158; mcp/src/agents_remember/application/review_task_context.py:196-228; mcp/src/agents_remember/application/review_task_context.py:170-193; mcp/src/agents_remember/application/review_task_context.py:231-289 |
| The refusal builder the composition reaches (`refused`, the extracted renderer's), the resolution module's refusal constructor it uses, and the **re-exported** record resolver the production port calls — whose owner is now the record module, and whose old assessment-only body is gone rather than kept beside it. | `refused`; `refusal`; `review_records_for` | mcp/src/agents_remember/application/review_record_rendering.py:186-191; mcp/src/agents_remember/application/review_candidate_resolution.py:374-390; mcp/src/agents_remember/application/knowledge_review.py:90-95; mcp/src/agents_remember/application/review_evidence_records.py:171-196 |
| **The case that proves the surface stores nothing: the two datasets' row counts are identical across a full render.** | `test_the_surface_stores_nothing_so_deleting_every_rendering_loses_no_canonical_information` | mcp/tests/test_knowledge_review_surface.py:496-508 |
| **The case that proves the adapter selects nothing: the comparison identity, item identities and counts are the shipped operation's own, compared value for value.** | `test_the_adapter_selects_nothing_because_the_shipped_comparison_is_the_comparison_rendered` | mcp/tests/test_knowledge_review_surface.py:509-560 |
| The case that proves the candidate is resolved from task context and never from a browser-chosen path, and the case that proves an absent dataset refuses by name. | `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`; `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one` | mcp/tests/test_knowledge_review_surface.py:870-883; mcp/tests/test_knowledge_review_surface.py:886-905 |
| The case that proves a stale comparison keeps its previous input and disables submission, and the case that proves a current one cannot be built with submission disabled for staleness. | `test_the_stale_rule_holds_in_both_directions` | mcp/tests/test_knowledge_review_surface.py:625-649 |
| **The two cases the sibling leaf `260921-ICR-L5` added for the before half: an absent side refuses by name rather than being substituted with an empty one, and a side that is present but cannot be read refuses by name instead of raising.** | `test_an_absent_baseline_half_refuses_by_name_rather_than_substituting_an_empty_one`; `test_a_before_side_that_is_present_but_unreadable_refuses_by_name` | mcp/tests/test_knowledge_review_surface.py:908-944; mcp/tests/test_knowledge_review_surface.py:947-985 |
| **The entry route's own before-half case, and the fact that it proves the damage is the cause: a damaged half is refused by name rather than raising from inside the comparison.** | `test_the_entry_route_refuses_a_damaged_before_half_instead_of_raising` | mcp/tests/test_knowledge_review_surface.py:1057-1097 |
| **The case that measures the delegated resolution through the real composition: the bound endpoints published in the served payload.** | `test_the_rendered_review_publishes_the_endpoints_and_reaches_the_whole_candidate`; `test_a_capture_input_that_moves_before_publication_is_refused_by_name` |mcp/tests/test_knowledge_review_source_endpoints.py:481-540; mcp/tests/test_knowledge_review_source_endpoints.py:546-570|
| **The cases this leaf added for the task-context entry: a review with neither dataset half lists the complete source inventory and answers 200 on the real route with no selector parameters; and a knowledge-only change leaves an openable review whose inventory is a *measured* empty set while the comparison is untouched.** | `test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all`; `test_a_knowledge_only_change_leaves_an_openable_review_with_a_measured_empty_inventory` | mcp/tests/test_knowledge_review_source_endpoints.py:842-918; mcp/tests/test_knowledge_review_surface.py:1359-1434 |
| The composition root that wires this adapter into the serving port. | `review_port`; `read_knowledge_review` | mcp/src/agents_remember/cli/dashboard.py:67-111 |
| **The composition measures what this leaf's own managed syncs recorded against the published generation and folds that measurement into the staleness it publishes (`ICR-R22@v1`): a measured movement outranks the reader's carried previous identity, so a review whose inputs a sync moved can never read `current`, and the payload carries the same measurement beside it.** | `review_sync_movement`; `review_staleness_with_sync_movement`; `sync_movement` | mcp/src/agents_remember/application/review_sync_movement.py:357-382; mcp/src/agents_remember/application/review_sync_movement.py:309-334; mcp/src/agents_remember/application/review_sync_movement.py:89-107 |


## Cross-Repo References

No cross-repository behavior is implemented in this file. The adapter reads one coordination root's
task tree and one candidate's disposable datasets, and carries no identity that ranges beyond the
repository namespace the request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all`; `test_a_knowledge_only_change_leaves_an_openable_review_with_a_measured_empty_inventory` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:842-918; mcp/tests/test_knowledge_review_surface.py:1359-1434. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 curator (uncommitted change set; leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta): **cleared the nine enforced `citation_anchor_absent_from_range` rows this card carried, by re-pointing each cited range to the declaration the tree now holds — range digits only, no claim or anchor wording touched.** Citation accounting, row by row: the authored-kinds row (`:471`) cited `review_evidence_records.py:120-122` for `AUTHORED_EFFECT_KINDS`, which the owner declares at `:132-134` — repointed. The refusal-builder row (`:475`) cited `review_record_rendering.py:175-180` for `refused`, declared at `:186-191` — repointed. The per-subject projection row (`:494`) cited `review_assessment.py:441-479` for `assessment_state_for`, declared at `:542-594` — repointed. The refusal/re-export row (`:501`) cited `review_record_rendering.py:175-180` for `refused` (repointed to `:186-191`), `knowledge_review.py:74-79` for the re-exported `review_records_for` — the re-export import is the block at `:90-95`, which is what the cell cites now — and `review_evidence_records.py:174-215` for the owner's entry point, written to that function's own extent `:171-196`. The two task-context/candidate rows cited surface-test ranges the merged file has left behind: `test_knowledge_review_surface.py:803-822` → `:870-883` and `:786-799` → `:886-905` (`:504`), and `:864-902` → `:908-944` and `:824-860` → `:947-985` (`:506`), each range now covering the case it names. Every other range on the card is unchanged and no range was dropped to silence a row. **Recorded rather than repaired:** the authored-kinds row's first range, `knowledge_review.py:190-196`, no longer holds `REVIEW_MATRIX_KINDS` either — that construct is declared at `:199-205` and the checklist reports that anchor as **stale by a move** in its own report-only bucket, which is the mechanical projection's rewrite rather than curator work, so it was left alone. No verification stamp was advanced: the candidate is uncommitted — the honest basis is the leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta — so no commit contains the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`, confirmed from the enclosure contract): **the composition traverses the recorded relationship union (757 → 778 lines).** `compose_review` gained one import (`relationship_movements`, `RelationshipSources` from `application/review_relationship_movement.py`) and **one call** placed where the page items and the resolved dataset halves are both in scope, and `source_pane` is now handed the traversed relationships — the adapter adds no traversal, pairing or display logic. The address view and the two-sided movement are the new modules' (`ICR-R08@v1`); this adapter's own rows for `compose_review` (`:300-412`) and the pane call were re-derived from the candidate. **Split-and-repoint:** the row that cited `_location`, `_change_state` and `_realization_read_item` **in `review_source_inventory.py`** was split per construct, because two of the three moved (`_location` to `application/review_relationship_display.py`, the change state to `recorded_change_state` in `application/review_recorded_relationships.py`) and the third was deleted with the payload selection it performed (now `side_payload`/`read_snapshot_relationships`); citing the old file would have been a false claim about where the display is built, not a stale range. **Metadata removal:** this card's seven candidate-reading metadata rows were removed under the developer's 2026-09-22 rule, and every history sentence that pointed at such a row was corrected in the same pass so the document no longer claims the row exists. No verification stamp was advanced: the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-22T14:50:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **the entry half's enumeration moved to `review_subject_catalogue.py` and the per-subject compare-to-earn-a-row mechanism is deleted (841 → 757 lines; `ICR-R09@v1`).** Purpose now names **six** extracted responsibilities (the subject catalogue beside the statement-side projection and the head-selection policy; the catalogue *replaces* the private helpers' mechanism rather than moving it, so no alias is left and `__all__` is unchanged). The entry-half Logic paragraph was **rewritten, not annotated**: the old account ("a subject is offered exactly when the shipped comparison reaches it … `_selected_item_count` returns `None` — dropping the subject") described the mechanism the packet deletes (the verified F06 defect), so it now states the catalogue contract — the union of both snapshots' own identity tables, per-row presence, labelled totals, no comparison run to earn a row, no silent drops. Two Invariants bullets were replaced for the same reason: "the entry list offers a subject exactly when the shipped comparison answered for it, drops a refused one" and "a subject the comparison refuses is dropped, not listed with a zero" are both false at this candidate; the catalogue lists every recorded identity with its presence and the review an entry opens carries the refusal. The Todos paragraph recording the dead `_IDENTITY_ITEM_KINDS` constant is **retired**: the constant exists neither at the base commit `f141d164` nor in the candidate (measured by grep over `mcp/src`), so the recorded leftover was already resolved on the landed line. **Citation accounting:** every range into this file re-derived from its construct's own extent against the 757-line candidate — docstring `1-56`, import block `65-139`, `__all__` `141-157`, `REVIEW_MATRIX_KINDS` `159-166`, `read_knowledge_review` `168-197`, `list_knowledge_review_entries` `199-280`, `_entry_refused` `282-294`, `compose_review` `296-392`, `with_selection_channels` call `348-349`, `_comparison_attribution` `394-405`, `_open_dataset_pair` `407-442`, `_review_matrix` `444-474`, `_compare` `489-529`, `_selector_kind_or_absence` `531-541`, `_comparison_refusal` `543-563`, `_comparison_identity` `565-582`, `_limitations` `584-608`, `_staleness` `610-626`, `_knowledge_pane` `628-674`, `_selected_statements` `676-700`, head-selection import `94-96`, statement-side import `105-108`, `revision_selection` `659` — and the two rows that cited the deleted helpers (`_reviewable_entries`, `_recorded_identities`, `_selected_item_count`) are **replaced, not annotated**: the entry-operation row now cites the catalogue delegation (`read_subject_catalogue` at its own module), and the recorded-identities row now cites the catalogue owner's `_side_identities`/`_union` beside the same store list operations. A new row cites the catalogue owner's contract (`review_subject_catalogue.py:1-22`). **Stamp accounting:** the verification pair names this leaf's base — the last real commit the reading was taken against — because the catalogue and the deletion exist only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T11:39:00+02:00 — 260921-ICR-L13 curator, **L7-aftershock citation repairs: six rows re-cited to the landed adapter declarations.** L7’s pass cited its uncommitted candidate’s positions; the landed file moved them (`_comparison_identity` `:649-667`, `_limitations` `:668-693`, `_knowledge_pane` `:712-759`, `_selected_statements` `:760-785`, `select_subject_revisions` import `:90-93`, `revision_selection` `:743`, `compose_review` `:380-477`, `_rows_remaining` `:560-575`, `list_knowledge_review_entries` `:204-284`, `_reviewable_entries` `:285-318`). Each claim re-read against its declaration with wording retained. Follow-up in the same pass: `_selected_item_count` `:341-367` → `:339-367` (the declaration line sat two lines above the cited range). No verification stamp was advanced.
- 2026-09-22T10:40:00+02:00 — 260921-ICR-L7 curator (uncommitted change set on `ar/260921-icr-l7`, base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **the adapter renders the head selection and the prefer-both-sides rule is deleted (825 → 843 lines).** Purpose now names the five extracted responsibilities (the head-selection policy beside the statement-side projection, each leaving no alias) and the head rule the adapter calls; Logic gained the one-call composition paragraph and the deleted-rule pane paragraph (`_knowledge_pane` takes the selection, `_selected_statements` renders heads or the explicit non-pair); Conventions names `_selected_statements` and the deliberately un-re-exported selection import; Invariants says the adapter applies no rule of its own. The old `_identity_item`/`_selector_record_id` row is **replaced, not annotated**, with the deletion record (the both-sides preference falsified by the packet), because "a subject held on both sides is preferred" is exactly what this leaf removes. **Recorded rather than repaired:** `_IDENTITY_ITEM_KINDS` (`knowledge_review.py:172`) is defined but now referenced nowhere — the deleted helper was its only reader — dead, not wrong, and the code owner's one-line cleanup. **Citation accounting:** every range into this file re-derived from its construct's own extent against the 843-line adapter — docstring `1-52`, import block `54-144`, `__all__` `146-160`, `REVIEW_MATRIX_KINDS` `164-170`, `read_knowledge_review` `175-205`, `list_knowledge_review_entries` `206-286`, `_reviewable_entries` `287-320`, `_recorded_identities` `321-340`, `_selected_item_count` `341-367`, `_entry_refused` `368-381`, `compose_review` `382-479`, `_comparison_attribution` `480-492`, `_open_dataset_pair` `493-529`, `_review_matrix` `530-561`, `_rows_remaining` `562-574`, `_compare` `575-616`, `_selector_kind_or_absence` `617-628`, `_comparison_refusal` `629-650`, `_comparison_identity` `651-669`, `_limitations` `670-695`, `_staleness` `696-713`, `_knowledge_pane` `714-761`, `_selected_statements` `762-787` (added row), and the surface-test rows to their merged extents. The `review_records_for` re-export row now cites the import at `74-79`. Header names this leaf's candidate row. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the leaf's base — the last real commit the reading was taken against — because every construct this pass touched exists only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T09:15:00+02:00 — 260921-ICR-L4 curator (sync-merge resolution of the parked candidate against the landed line, merged base code `d21bc8a6` / memory `75bb4d65`): **additive union with landed `260921-ICR-L14`.** Both sides' reference rows are kept with every range re-derived against the merged 825-line adapter: L14's record-resolver extraction (`review_records_for`/`AUTHORED_EFFECT_KINDS` owned by `review_evidence_records.py`, `with_selection_channels` + `_rows_remaining` in the composition) beside this leaf's attribution wiring (hoisted observation, `_comparison_attribution`, receipt preflight, shared refusal owner). Both history sets kept newest-first. Header names the merged base on this leaf's candidate row; stamp stays the landed `8ff80ce0`. No verification stamp was advanced.
- 2026-09-22T08:30:00+02:00 — 260921-ICR-L4 curator (uncommitted change set on `ar/260921-icr-l4`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the adapter stays a delegator and gains the attribution wiring (831 → 837 lines).** `compose_review` builds the two tree sides and makes the source observation once, hands it to `review_inventory` as `observed` and to the task-context branch as the partition's denominator; the subject route's pane attribution is the comparison's own partition carried verbatim by the new `_comparison_attribution` (one observation hoisted, one call changed, one narrowing helper); the entry route states the unreadable-receipt preflight beside the unreadable-half refusal, and both routes plus the pair read refuse an unreadable candidate through the shared owner (`unreadable_candidate_refusal`/`candidate_receipt_refusal` in `review_candidate_resolution.py` — the only place the code, detail, next action and offending input exist). Every reference row into this file and the pane/count rows were re-derived against this candidate. **Stamp accounting:** the verification pair stays L18's; this leaf's claims were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T22:15:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **the private record resolver left this adapter for the record owner, and the composition gained the step that states the matrix-owned collection's availability.** `review_records_for` — whose body read the published assessment collection and returned `EMPTY_REVIEW_RECORDS` for an absent *or* unreadable authority — is gone from this module; `ICR-R14@v1`'s owner is `application/review_evidence_records.py`, and the name survives here as a **re-export** in the import block and `__all__`, which is this module's existing convention for `resolve_review_candidate`, `candidate_ref` and `ReviewRecordInputs`. The Logic paragraph that described the old body was **replaced, not annotated**, because "absent authority and unreadable authority are both an empty collection" is exactly the collapse the leaf removes. `AUTHORED_EFFECT_KINDS` moved to the same owner and is imported back, so the kinds a channel counts and the kinds `_knowledge_pane` renders remain one declaration; the Conventions section now says so instead of listing the constant as this module's own. `compose_review` gained one call — `with_selection_channels(records, rows, selected=True, rows_remaining=_rows_remaining(matrix))` — and a new Logic paragraph records it and the new `_rows_remaining`, which reads the view's own `rows_remaining` count so a bounded page is reported as bounded; the task-context branch calls the same function with `selected=False`. The adapter is **831 → 819 lines**, and the file-size rail's relief is the reason the resolver moved out rather than growing here. **Citation accounting:** this leaf's removal shifted every construct below `:126`, and every range in the reference table was re-derived from its construct's own extent — docstring `1-47`, `__all__` `131-145`, `REVIEW_MATRIX_KINDS` `149-153`, `read_knowledge_review` `161-189`, `list_knowledge_review_entries` `192-273`, `_reviewable_entries` `276-307`, `_recorded_identities` `310-327`, `_selected_item_count` `330-354`, `_entry_refused` `357-368`, `compose_review` `371-453`, `_open_dataset_pair` `456-500`, `_review_matrix` `504-534`, `_compare` `548-587`, `_selector_kind_or_absence` `591-600`, `_comparison_refusal` `603-622`, `_comparison_identity` `625-641`, `_limitations` `644-667`, `_staleness` `670-685`, `_knowledge_pane` `688-720`, `_identity_item` `723-749`, `_selector_record_id` `752-760`, and the sibling-module rows to theirs. The row that named `review_records_for` at `806-831` was **repointed** to the re-export line and the owner's own entry point; the `AUTHORED_EFFECT_KINDS` row was repointed to the declaration's new home; two rows were **added** for the selection-channel step and the re-export block. Nothing was dropped. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` now name the **production line this reading was against** — `d80a0513e928ef29a973527d09597c82c96fde87`, the master line's current tip and this leaf's base — replacing the previous pair rather than leaving a stamp no reading in this pass measured; the candidate is uncommitted, so no commit contains the content a stamp would claim to have verified, and the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `_entry_refused` repointed to mcp/src/agents_remember/application/knowledge_review.py:357-368. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T18:20:00+02:00 — 260921-ICR-L6 curator (uncommitted change set on `ar/260921-icr-l6`, merged base `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **the statement-side responsibility left this file for `application/review_statement_sides.py`, and this entry was revised at the sync so the card states the merged line rather than either side of it.** The adapter is 888 → **831 lines** on both sides of the merge, because leaf `260921-ICR-L18` changed the ingest CLI and the catalogue and not this file; the only structural change is one import block (`84-88`) and the four calls inside `_knowledge_pane` (`672-705`) where `_side_content`, `_conditions`, `_read_side`, `_field_changes` and `_field_text` used to be defined and called, and no feature logic was added. **The behavior delta is in the field-value reader:** the base `_field_text` returned `None` for any `dict`, so a *changed* structured field (`provenance`) was served as `None` on both sides — an absence the snapshot does not hold, stated twice — while each side now carries `structured_value_text` of the value that side really holds; `None` stays reserved for a side with no record and a record with no value for that field. **Citation re-derivation:** every range into this file was re-measured against the 831-line merged adapter rather than carried from the pre-extraction card — docstring `1-47`, import block `49-129`, `__all__` `131-145`, `REVIEW_MATRIX_KINDS` `149-158`, `AUTHORED_EFFECT_KINDS` `160-162`, `read_knowledge_review` `167-195`, `list_knowledge_review_entries` `198-279`, `_reviewable_entries` `282-313`, `_recorded_identities` `316-333`, `_selected_item_count` `336-360`, `_entry_refused` `363-374`, `compose_review` `377-452`, `_open_dataset_pair` `455-500`, `_review_matrix` `503-530`, `_compare` `533-572`, `_selector_kind_or_absence` `575-584`, `_comparison_refusal` `587-606`, `_comparison_identity` `609-625`, `_limitations` `628-651`, `_staleness` `654-669`, `_knowledge_pane` `672-705`, `_identity_item` `708-734`, `_selector_record_id` `737-745`, `review_records_for` `806-831`. Two rows were **added** (the delegation and the new case module) and none was dropped. **`__all__` is unchanged and that is a fact, not an omission:** `review_statement_sides`' five names are the one move that leaves no alias, because no module under `mcp/` imported the adapter's private spellings, and the Conventions section says so. Cardinality wording was corrected where the file's own docstring now says "Four more responsibilities". The sibling-module ranges kept from L18's line were re-derived too: `unreadable_half_refusal` is `knowledge_before_half.py:347-377` on the merged tree, not `344-374`. **Sync accounting:** the card's `15 / 65` statements were already false before this leaf and the merged catalogue measures **16 / 66**. **Stamp accounting:** the verification pair is L18's `71a4433e` / `2026-09-21T16:29:06+02:00`, which this leaf neither advances nor regresses — nothing in this leaf is committed, so the claims whose evidence this leaf moved are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **the sync's memory-side conflict in this card resolved as a union: the master line's cold-start and unreadable-half facts, this leaf's three extractions and task-context entry, and both sides' history.** Every range in the reference table was re-derived against the merged 888-line adapter rather than carried from either side. **Corrected rather than merged:** `__all__` moved to `125-142` and the import block to `43-123`; `read_knowledge_review` to `161-189`; `list_knowledge_review_entries`/`_reviewable_entries` to `192-273`/`276-307`; `_recorded_identities`/`_selected_item_count` to `310-327`/`330-354`; `_entry_refused` to `357-368` — and **the name itself is corrected here**: this card's first pass recorded the pre-sync candidate's one-word `_entryrefused`, while the merged worktree carries `_entry_refused`, so the row and the Conventions paragraph now say what the code says; `compose_review` to `371-446`; `_review_matrix` to `497-524`; `_compare` to `527-566`; `_selector_kind_or_absence` to `569-578`; `_comparison_identity`/`_limitations` to `603-619`/`622-645`; `_staleness` to `648-663`; `_knowledge_pane` to `666-699`; `_identity_item`/`_selector_record_id` to `702-728`/`731-739`; `review_records_for` to `863-888`. The master side's `_entry_refused`, `_submission`, `_source_pane`, `_evidence_pane`, `_subject_states`, `_assessment_display`, `_observation`, `_location`, `_change_state` and `_refused` rows were **superseded, not duplicated**: those constructs still exist, but under their extracted names and in the modules that now own them, and the table says so. L5's `unreadable_half_refusal` facts were kept and merged into the entry-operation, pair-preflight and composition rows; L5's two new before-half cases and its entry-route case were kept with their own ranges re-derived (`789-825`, `828-869`, `938-976`). No claim was dropped and none was invented.
- 2026-09-21T15:10+02:00 — 260921-ICR-L5 curator, **two enforced rows re-read and re-cited: the sibling module's declarations added beside this adapter's import block.** The claim about the re-export and the claim about the adapter's own statement of what it selects both name constructs that live next door, so each row now cites the declaration that supports its words (`resolve_review_candidate` `review_candidate_resolution.py:130-194`, `require_current_candidate_identity` `:197-226`, `refusal` `:304-318`, `REVIEW_BASELINE_DIRECTORY` `:78-78`) rather than only the import site. Claim wording is retained: each still states what the code does at the construct it names. No verification stamp was advanced.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the adapter shrank to a delegator and gained an entry that needs no subject.** Three responsibilities left this file for modules named for what they own — `application/review_source_inventory.py` (the exact source-change inventory of the bound tree pair and the source pane), `application/review_record_rendering.py` (the record collections the caller supplied, rendered as pane values) and `application/review_task_context.py` (the task-context composition) — and `compose_review` now **measures the inventory first and unconditionally**, before any dataset is opened and before the selector branch, then splits: a request with `selector=None` is answered by `task_context_review` with `comparison=None`, `staleness.state="not_compared"` and a knowledge pane in the `task_context` selection state, while a request that names a subject keeps the shipped path through the new `_open_dataset_pair` and `_review_matrix` steps. `_limitations` now declares `inventory_limitations(inventory)` at the top level beside the comparison's own limits, and `_selector_kind_or_absence` is what lets a comparison refusal spell an absent selector instead of reading `kind` through `None` (the pyright rail's finding). Card body re-read and re-pointed: Purpose gained the task-context entry and the three extractions; Logic's `compose_review`, pane, staleness/submission and limits paragraphs were rewritten and two new paragraphs record the inventory-first order and the declared inventory limits; Conventions now names `_entry_refused`, `_open_dataset_pair`, `_review_matrix`, `_selector_kind_or_absence` and the re-exported `refused`/`submission`/`source_pane`/`evidence_pane`; Invariants gained the no-selector state and the one-responsibility-one-implementation rule. **Citation re-derivation:** every row below was re-derived against this candidate rather than carried as a delta, including ten rows whose anchors had been renamed or moved to the extracted modules (`_entry_refused`, `_submission`→`submission`, `_source_pane`→`source_pane`, `_evidence_pane`→`evidence_pane`, `_subject_states`→`subject_states`, `_assessment_display`, `_observation`, `_location`, `_change_state`, `_refused`→`refused`) and the rows whose prose named them. **Stamp accounting:** the two verification rows still name `702714fc05363cb28eacaf101ba8384475a6aa56`, the last real commit on this line, because nothing in this leaf is committed yet; the claims whose evidence this leaf's own change moved were re-read against the candidate and are recorded here as stamp-class leftovers that only closeout can stamp.
- 2026-09-21T14:30+02:00 — 260921-ICR-L5 curator, **post-sync revision: the reference table keeps L1's file attribution with every range re-derived, and the caveat below is superseded rather than merged.** The sync brought leaf `260921-ICR-L1`'s landed extraction into this candidate, so the resolution, the pair preflight, the namespace read, `ReviewCandidateResolution` and the three `REVIEW_*` constants are now cited where they live (`application/review_candidate_resolution.py`) and the adapter keeps only its delegation and composition; the two call sites this leaf added are cited where they now sit (`list_knowledge_review_entries` `:207-288`, `compose_review` `:386-496`), and every other range into this file was re-measured against the merged 1,126-line module — L1's own last pass measured a 1,113-line module, before this leaf's 13 lines landed. One upstream projection record is **retired rather than kept**: the mechanical `ReviewCandidateResolution` repair bullet, which asserted a currency for `knowledge_review.py:185-205`, a range this card no longer cites because L1 re-read that claim at the construct's new home. The caveat below was written before the sync, when the extraction was absent from this leaf's candidate; it is retained as the record of what was true then and is superseded by this entry. No verification stamp was advanced.
- 2026-09-21T14:05+02:00 — 260921-ICR-L5 curator (uncommitted change set on `ar/260921-icr-l5`, code base `f745e16659c5602252bb185a2ffccc356c2bde26`): **a present-but-unreadable before half is now a named refusal on both routes, and every citation range on this card was re-measured.** The change to the adapter is 13 lines: one import of `unreadable_half_refusal` from the new `application/knowledge_before_half.py`, and two call sites — `compose_review` states the refusal before `missing_dataset_half`, and `list_knowledge_review_entries` states it before `_reviewable_entries` — so the per-subject comparison can no longer raise `apsw.NotADBError` out of the entry route that exists to offer a subject. The two Logic paragraphs above record the fact and the boundary it respects: the readers, the four half-states and the refusal all live in the new module, and what stays here is only *where* in the two routes the answer is stated, which is the seam policy's "keep the adapter a delegator" rule rather than feature logic. **Citation accounting:** the file grew 1,281 → 1,294 lines, which moved every construct below the two call sites, and several pre-existing rows were found **materially stale** at this candidate rather than merely shifted — `resolve_review_candidate` was cited at `:182-227` (that range is `ReviewCandidateResolution`; the function is `:208-259`), `_knowledge_pane`/`_source_pane`/`_evidence_pane` at `:512-648` (they are `:802-938`), `_location` at `:1188-1211` (`:1201-1224`) and `refusal` at `:1233-1236` (`:1252-1266`) — so every row into this file was re-derived from the construct's own extent, not carried. The rows citing `mcp/tests/test_knowledge_review_surface.py` were repointed with it. This is a body change and not a metadata-only refresh. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded; no stamp was advanced or invented and no commit was made.
- 2026-09-21T14:05+02:00 — 260921-ICR-L5 curator, **caveat recorded rather than hidden:** the two `REVIEW_*` half-name constants and the entry/adapter surface this card describes are, on the master line, owned by `application/review_candidate_resolution.py` — leaf `260921-ICR-L1`'s landed extraction, which re-exports every moved name through this adapter. That module does **not** exist in this leaf's candidate: `ar/260921-icr-l5` is based on `f745e166`, while the extraction landed on the source branch afterwards as `702714fc`. This card therefore describes the adapter as it actually is in this leaf's candidate, where `resolve_review_candidate`, `missing_dataset_half` and `review_namespace` are still defined inline; the L1 extraction is explicitly **not** recorded here as this leaf's work. When this leaf's code meets the extracted module, the two call sites this leaf adds belong beside the moved preflight rather than in the adapter — that reconciliation is the orchestrator's and the later leaves' to perform, not curation's. No verification stamp was advanced.
- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, base `f745e16659c5602252bb185a2ffccc356c2bde26`): **reconciled this card against the leaf that repaired the responsibility the intake verification named, and corrected the claim it named plus the claims that depended on it.** The intake verification recorded that this card "confirms no candidate tree, absent-half refusal, assessment-only loader and unmeasured-as-stale" and that it "must be reconciled when this responsibility is repaired"; the repair is this leaf's, so the card now says what the code does. **The false claim was structural**: the card said "the candidate side supplies no root or tree id", with `candidate_code_tree_id` deliberately `None` for a live leaf's uncommitted line and `candidate_code_root` therefore `None` too. That is no longer true — the resolution binds the contract's **recorded base commit** on one side and the **captured add-all candidate tree** on the other, and supplies the worktree as the candidate root with it. Two consequences are recorded with it: a contract that records **no** base commit is now refused by name (`offending_input="baseline"`) rather than half-resolved, and the recheck of the captured target (`require_current_candidate_identity`) runs in `compose_review` immediately before the payload is built, so a capture input that moved during composition is a named refusal carrying both identities. **The resolution itself moved out**: `resolve_review_candidate`, `ReviewCandidateResolution`, `missing_dataset_half`, `review_namespace`, `refusal`, the three `REVIEW_*` path constants and `_leaf_contract` are `application/review_candidate_resolution.py`'s, re-exported here so the ingest CLI's existing import keeps resolving; the docstring, Purpose, Logic, Conventions, Invariants and reference table were all re-read and re-pointed accordingly, and the Invariants bullet that declared "a side with no exact tree is a supported state" was replaced by the bound-endpoints rule. **Citation accounting:** every range this card cites into `knowledge_review.py` was re-derived from the construct's own extent in this candidate (the module went 1281 → 1113 lines when the resolution left), each disposition row that had cited a construct now living in the sibling module was split so the anchor and its real file agree, and the two ranges that had run past the end of the file (`:1188-1211`, `:1221-1227`, `:1233-1236`, `:1256-1281` in the old numbering) are gone rather than widened to nothing. Two rows now also cite the cases this leaf added for the delegated resolution (`mcp/tests/test_knowledge_review_source_endpoints.py:370-428`, `:434-458`). **Stamp accounting:** this entry names this leaf's candidate as the reading's basis; the commit fields are left as the last real verification wrote them, because the change is uncommitted and closeout owns that stamp. **One generated history record was retired in this pass:** the mechanical repair bullet for `ReviewCandidateResolution` (which repointed it to `knowledge_review.py:184-204`) is removed, because this curator re-read that claim against the construct's new home in `review_candidate_resolution.py` and derived the range by hand — leaving the generated record would keep asserting a currency for a range no longer cited. No other history entry was touched.
- 2026-09-20T11:53:49+00:00 — retired by the 260921-ICR-L12 curator: this mechanical bullet bound `ReviewCandidateResolution` to mcp/src/agents_remember/application/knowledge_review.py:185-205, which is a mention of the imported name rather than the value's declaration. The claim at `:456` was re-read and re-cited to the declaration itself, mcp/src/agents_remember/application/review_candidate_resolution.py:120-157, and its wording now also states the one field this leaf's change added to the value (the record a closed leaf's review was reopened from). A projection is not evidence that a claim still holds, so the review — recorded in this document's ICR-L12 entry — is what disposes of it; no verification stamp was advanced because the candidate is uncommitted.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `REVIEW_MATRIX_KINDS`; `AUTHORED_EFFECT_KINDS` repointed to mcp/src/agents_remember/application/knowledge_review.py:143-149; mcp/src/agents_remember/application/knowledge_review.py:154-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` repointed to mcp/src/agents_remember/application/knowledge_review.py:163-176; mcp/src/agents_remember/application/knowledge_review.py:181-181. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `read_knowledge_review` repointed to mcp/src/agents_remember/application/knowledge_review.py:333-361. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): the adapter gained the surface's **entry half** and the two connections that make a live leaf's candidate pair actually exist. This card now records: (1) `list_knowledge_review_entries` and its helpers — the subjects the resolved pair can be compared on, resolved through the *identical* operation the comparison uses, offered only when the shipped `diff_knowledge_scope` answered for that identity, and **dropped** rather than listed with a zero when it refused; (2) the two **published** directory constants `REVIEW_BASELINE_DIRECTORY`/`REVIEW_CANDIDATE_DIRECTORY`, exported because the ingest CLI derives the candidate directory it authors into from the same names, which is what makes "the candidate the leaf authored" and "the candidate the review resolved" one directory instead of two conventions; (3) `missing_dataset_half`, the pair preflight that turns an absent half into the existing `candidate_dataset_absent` refusal **naming which half** is missing, where before an absent baseline raised `CantOpenError` from inside side construction; (4) `review_namespace`, which reads the namespace from the candidate's own sealed **receipt**, because the dataset is bound to a namespace id and a side opened under the requested repository spelling refuses against its own binding — measured in the leaf's fixture as `bound to 40d350a6-…, not to the requested repository namespace agents-remember`, a failure every live review of a real candidate would have hit; and (5) that the candidate side now resolves to both a code root and a tree id **or to neither**, since a live leaf's uncommitted line has no tree id and supplying the root anyway made every comparison raise instead of reporting the source expansion it could not make. The candidate this reading was taken against was recorded in that entry's own words (the metadata row that carried it was removed on 2026-09-22 as not a real field); no verification stamp was advanced, because no commit contains this body.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **re-read this claim against the construct its mechanically projected range now covers, and retired that projection record after the read.** The claim is **"The published adapter surface: the three entry points, the two dataclasses, the three published constants and the re-exported request model."** against `__all__` at `mcp/src/agents_remember/application/knowledge_review.py:110-124`: the anchor resolves at line 110 and the range holds the whole list, which now names `list_knowledge_review_entries` beside `read_knowledge_review` and `review_request_from_query`, `ReviewCandidateResolution` and `ReviewRecordInputs`, `REVIEW_BASELINE_DIRECTORY` and `REVIEW_CANDIDATE_DIRECTORY` beside `REVIEW_CANDIDATE_RELATIVE_ROOT`, plus `ReviewSurfaceRequest` and `REVIEW_MATRIX_KINDS` — three entry points, two dataclasses, three constants, one re-exported request model, so the wording holds unchanged. The generated repair bullet for this range was **retired** because that projection resolves an exact NAME rather than the claim's subject, so leaving it would keep asserting a currency it cannot support. No other bullet or row was deleted and no verification stamp was advanced.
- 2026-09-20T01:25+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared the last two citation rows of this card — two dead anchors and one reopened claim, which are the same row.** The stale-rule row named two cases that exist nowhere in the tree; the source records that they are one case now — `test_the_stale_rule_holds_in_both_directions` (569) states in its own docstring "One rule, two directions, and they were two cases until they were merged", and both behaviours the Finding names (the stale state keeping its previous reference with submission disabled, and a payload claiming a current comparison while disabling submission being unconstructible) are asserted in that one case. The Anchor cell therefore names that surviving case, and both cited ranges were retained unchanged because each already holds it: `:569-590` is the merged case's own declaration span and `:569-598` the wider range the row carried. The Finding text is unchanged, the row is not deleted and no citation was dropped. Because the row's evidence changed after verification and the claim is now current against this candidate, the claim was re-read and **retained as written**: the two behaviours are still exactly what it describes. **Stamp accounting:** the stale `lastVerifiedCommitHash`/`lastVerifiedCommitDate` rows (and the L22-era candidate-reading row beside them) were replaced by the candidate reading recorded in this entry, because no commit contains the body as it now stands and no stamp was measured on it. No other range, anchor or claim wording was changed anywhere in this document.
- 2026-09-20T00:55+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): hand-read the two enforced rows this card carried. One is cleared (`test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`): its second range `750-771` was replaced with the exact extent of `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one` (`745-764`), which the claim's second half names. The other is LEFT and reported: `test_a_stale_comparison_keeps_the_previous_input_and_disables_submission` and `test_a_current_comparison_cannot_be_built_with_submission_disabled_for_staleness` exist nowhere in the tree — the docstring of `test_the_stale_rule_holds_in_both_directions` (`569-590`) records that the two cases were merged into it, and both behaviours the claim names are still asserted there, so the source is not wrong but the claim's two anchors are. Only a curator re-reading the claim can re-point it at the merged case, so the row is untouched. No other range in either row was touched, no claim was re-worded, no anchor or range was dropped to silence a finding, and no verification stamp was advanced. No commits.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 1 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:38+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): **re-read each claim below against the construct its range now covers, corrected the wording where the construct had moved, re-derived every range from the construct's real extent in the file the claim cites, and only then left the card's stamp to closeout.** No `Generated citation repair` bullet is written: these are curator edits, not a mechanical projection. `knowledge_review.py.md:208` — re-read: the two cases the claim names were merged into one, and its own docstring says so ('One rule, two directions, and they were two cases until they were merged'). The rule is unchanged, so the claim's SUBJECT survives; only the anchor and range are wrong.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `knowledge_review.py.md:207` (`test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`, `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one`).
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's application adapter. It records the four things a reader of this route needs: the adapter **selects nothing** and composes only R08's `diff_knowledge_scope` and L20's `read_knowledge_view(review_matrix)`; the composition sits at the application tier because `layers.toml` ranks `serving` below `application`, so the HTTP shim reaches it through a port the composition root wires; the candidate is resolved from canonical task context and never from a caller-supplied path; and every absence is a named state or a typed refusal rather than a favourable default. It also records the two published facts the panes are built on — the five remaining counts, where an unmeasurable quantity states its reason instead of reporting a zero, and the stale/submission coupling the payload model enforces structurally. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The candidate this reading was taken against is named in the entry itself, and closeout owns the stamp once the code commit exists.

## 260921-ICR-L10 The Adapter Offers A Cursor To The Collection It Names

`260921-ICR-L10` (`ICR-R10@v1`) carries a request's cursor to the collection that names it. The
adapter still delegates the page arithmetic to `review_pagination.py`; what it gained is the wiring: the
request's `page_of`/`continuation`/`page_size` are offered to that collection's own owner, the comparison
and the matrix are read at that position, and the one page the request named is published beside the
panes — with the refusal it earned when a requested page could not be served.

Two renames came with it, and a reader should read them as renames rather than new behavior:
`_rows_remaining` is now `_matrix_rows_remaining` (it takes the matrix's own selection rather than a bare
view result), and the task-context branch of the selection channels is now the extracted
`without_selected_matrix`. A refused cursor leaves the payload with no page and the matrix channels
`unavailable`, never a measured zero: a refused read has no counts, and a page of invented zeros would be
a lie about a read that did not happen.

## Update History
- 2026-09-23T00:30:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; production line at this leaf's base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **the adapter offers a cursor to the collection it names.** The page wiring is new (the request's
cursor goes to the owner that minted it, the page is published beside the panes, and a refused page
carries its refusal instead of a zero); `_rows_remaining` became `_matrix_rows_remaining` and the
task-context branch became the extracted `without_selected_matrix`, both renames rather than new
behavior. Every row on this card that cited this adapter by line was re-derived against this candidate,
because this leaf moved them. No verification stamp was advanced: nothing in this leaf is committed, so the commit/closeout stamp remains closeout's.
## 260921-ICR-L26 The Adapter Classifies Before It Renders, And The Two Row Renderers Move Out

`260921-ICR-L26` (`ICR-R26@v1`) adds **one** thing to this adapter and removes two helpers from it:
`compose_review` now calls `review_applicability(...)` **once**, before either pane renders anything,
and hands the panes what that projection kept. The call is a `ComparisonFacts` value the adapter
already holds — the comparison's union items, ICR-R07's revision selection, ICR-R11's published
identity and ICR-R08's recorded relationship union — and the projection is the attribution half of the
review, so the adapter stays a delegator: **1034 → 1036 lines** while a whole classification stage
arrives beside it.

**What changed shape.** `_knowledge_pane` no longer takes the request's selection as an argument: it
reads `applicability.revision_selection` from the projection, so the statements are rendered from the
same selection the classification was made against rather than from a second spelling of "which
revisions were selected". Both panes are built from `applicability.displayed_rows(rows)`, the two
per-record renderers moved to `application/review_record_rendering.py` as `authored_effects` and
`unresolved_authors`, and `_authored_effect`/`_unresolved_author` are deleted here — the adapter's
private copies are exactly what the extracted renderer exists to prevent.

**What a later reader must not undo.** The classification runs **before** the panes and on the
**selection**, never on the page: a row whose recorded references named another subject's identity is
not in `displayed_rows`, and a row whose references resolved to nothing is (as `unresolved`), because
dropping it would report an unresolvable binding as an absence of records. The one call site is also
the one place the ordering is guaranteed.

## Update History
- 2026-09-23T02:40:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): **the adapter classifies once, before either pane, and loses its two row renderers (1034 → 1036 lines; `ICR-R26@v1`).** The Logic section was extended with the call, the `displayed_rows` hand-off to both panes and the `revision_selection` the pane now reads from the projection; the two deleted private helpers are recorded as moved to the record renderer. **Citation accounting:** the rows this leaf's insertions moved were re-derived from each construct's own extent in the 1036-line candidate — `_knowledge_pane` `628-674`/`649-694` → `926-978`, `evidence_pane`'s renderer range `152-176` → `213-252`, `source_pane` `556-619` → `560-613`, and the extracted renderers' four ranges (`200-218`, `219-235`, `276-296`, `297-311`) → their real extents (`277-302`, `305-322`, `431-453`, `456-473`). Wording was retained where the claim still states what the code does. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header already names this leaf's base as the production line the reading was taken against, and the governed closeout owns the real stamp.
## 260921-ICR-L12 The Adapter Delegates The Closed Leaf And Reports Its Two Kinds Of Absence In Two Voices

`260921-ICR-L12` (`ICR-R12@v1`) changes this adapter in three delegating places and one
extraction, and adds no resolution logic of its own:

- **both resolutions name the record the request asked for.** `read_knowledge_review` and
  `review_records_for`'s caller pass `recorded=request.history == "recorded"`, so a review of a leaf's
  recorded comparison is composed — and handed the records — from the same recorded pair rather than
  from whatever the leaf holds now.
- **the pair's own refusals come first and are one answer.** `list_knowledge_review_entries` now asks
  `closed_leaf_dataset_refusal(resolved)` **or** `_absent_pair_refusal(resolved)`: a closed leaf's
  record answers in its own words — an intent generation this leaf never recorded is a fact about the
  repository's history, and reporting it as "the resolved half is absent" would read as content that
  was expected and lost — while a live pair with an absent half earns the shipped sentence, which is
  why that sentence moved into `_absent_pair_refusal` unchanged. Both are stated before any subject is
  listed, so the catalogue can never answer for a pair nothing could open.
- **the subject composition asks the same question before the shipped preflight.** `compose_review`
  returns `closed_leaf_dataset_refusal(resolved)` when it is not `None`, so a declared absence and
  unavailable content are two different refusals rather than one; a live candidate, and a closed leaf
  whose recorded halves both resolve, fall through unchanged.
- **the response declares which record it read.** The payload's `limitations` gains
  `closed_leaf_limitations(resolved)` beside the comparison's own limits; a live candidate contributes
  no token, so a live response is byte-identical to the one it always was.

**The adapter grew 1036 → 1077 lines and every added line delegates.** The inline "absent half"
refusal was replaced by the `_absent_pair_refusal` extraction (−21/+7), three delegating calls and one
`recorded=` keyword were added, and no R12 feature logic lives here. The module remains the composition
root's one review port, and the closed-leaf owner is reached only through it.

## Update History
- 2026-09-23T04:45:00+02:00 — 260921-ICR-L12 curator, **review of a mechanically projected range (the check's own disposition request)**: the projection bullet above was retired after the claim it names was re-read against the construct its own words describe, and re-cited to that construct's declaration rather than to the mention the projection had bound. Answering the check's two questions: (1) the construct the new range covers does support the claim's wording; (2) the old range arrived by mechanical anchor-range projection, which is exactly why it is not evidence that the claim holds — the review, not the projection, is what disposes of it. The bullet is retired rather than left standing because a projection that has been superseded by a curator's re-citation would otherwise keep asking the same question forever.
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **the adapter delegates the closed leaf and states its own absences in two voices (ICR-R12@v1).**
Both resolutions now carry `recorded=request.history == "recorded"`; the entry route asks the
closed-leaf refusal before the shipped one and the extraction left the live sentence unchanged; the
subject composition states a declared absence and unavailable content as two different refusals; and the
payload declares which record it read. 1036 → 1077 lines, delegation only. **Citation accounting:**
every row into this module was re-derived against the candidate. **Stamp accounting:** no verification
stamp was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.

## 260921-ICR-L17 The Adapter Reads The Previous Identity From The Request And Loses Its Two Staleness Helpers

`260921-ICR-L17` (`ICR-R17@v1`) leaves this adapter a delegator and takes two private helpers out of it.
The comparison's declared identity and the staleness it earns moved to
[`application/review_comparison_staleness.py`](review_comparison_staleness.py.md) — a purpose-named
adjacent owner — and the adapter **1077 → 1041 lines**.

**What is deleted here rather than annotated.** `_comparison_identity` and `_staleness` are gone from
this file. They were private to it and nothing under `mcp/` imported them, so the extraction leaves **no
alias and no re-export**: `__all__` is unchanged, and no importer had to learn a new home. Their bodies
are the sibling module's `comparison_identity` and `review_staleness` verbatim (the moved sentence
`"Candidate changed — open a new comparison"` and the moved axis `("comparison-binding",)` are worded
there now), so there is exactly one implementation of each rule.

**What the composition reads instead.** `compose_review` calls `comparison_identity(comparison)` and
then `review_staleness(identity, request.previous_binding_digest)`, and reads
`staleness.state == "stale"` for the submission state **and** publishes that same `staleness` value on
the payload — one measurement, so "an assessment is never submitted against a comparison that has moved"
cannot be true of one field and false of the other. The comment above the two calls says exactly that.

**The previous identity travels on the request, not beside it.** Both `read_knowledge_review` and
`compose_review` lost their `previous_binding_digest` keyword; the value is read from
`ReviewSurfaceRequest.previous_binding_digest`, which the route shape-admits and the client's refresh
control supplies. `read_knowledge_review`'s docstring records both facts — that the field is the identity
a reader was looking at carried on the read that replaces it, and that it travels on the request because
there is one spelling of what was asked.

**The docstring's responsibility count was advanced, and it is still one behind its list.** The
paragraph that names the extracted owners moved from "Five more responsibilities" to "Six more
responsibilities" when the new module joined it. It names **seven** modules under that heading, because
it already named six under a heading of "Five" before this leaf; the Purpose section above records the
arithmetic rather than repeating the heading.

**What a later reader must not undo.** The identity is **carried, never recomputed**: the helper reads the
comparison operation's own `binding`/`binding_digest`/`selector_digest` and copies them, and a second
spelling of that digest is how two readers come to compare two different generations. And the previous
identity selects nothing — it reaches no dataset path, no candidate resolution and no comparison input.

## Update History
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **the comparison's identity and its staleness rule moved out of this adapter and the previous identity moved onto the request (1077 → 1041 lines; `ICR-R17@v1`).** `_comparison_identity` and `_staleness` are **deleted, not annotated**: both were private to this adapter and nothing under `mcp/` imported them, so the extraction leaves no alias, `__all__` is unchanged, and the two rows that cited them were **replaced, not amended**. The staleness Logic paragraph was **rewritten** for the same reason: its old text was a description of a function that no longer exists here ("`_staleness` returns `current` when there is no `previous_binding_digest`…"), so it now states the two calls `compose_review` makes, the one measurement both the published state and the submission state read from, and the fact that the previous identity is no longer a keyword beside the request but a field on it. The Purpose paragraph that counted the extracted responsibilities was corrected: the docstring's heading advanced "Five more responsibilities" → "Six more responsibilities" while the paragraph names **seven** modules, because it already named six under a heading of "Five" before this leaf — recorded as the arithmetic it is rather than repeated as a count. **Citation accounting:** the two rows this leaf's deletion falsified were split and re-cited from each construct's own declaration on the candidate — the identity and the staleness rule to the sibling module (`comparison_identity` `:51-73`, `review_staleness` `:76-97`), `_limitations` to `:905-928`, `submission` to `review_record_rendering.py:183-210`, and the payload validators to `models/knowledge/review.py:1030-1126`. **Stamp accounting:** the verification pair names this leaf's base — the last real commit the reading was taken against — because the extraction and the deletion exist only in this leaf's uncommitted working tree; closeout owns the stamp once the code commit exists.

## 260921-ICR-L22 The Composition Measures The Sync's Rebinding And Folds It Into Staleness

`260921-ICR-L22` (`ICR-R22@v1`) leaves this adapter a delegator and gives it **one measurement and one
fold**, made in the same place the staleness it already published is decided. `compose_review`
(`:357-555`) now calls `review_sync_movement(resolved)` (`:475`) — what this leaf's own managed syncs
recorded against the comparison generation it published — and hands that value, beside the staleness
R17 already computes from the reader's carried identity, to
`review_staleness_with_sync_movement(review_staleness(identity, request.previous_binding_digest),
sync_movement)` (`:476-478`). The payload publishes the same measurement as `sync_movement` (`:537`).

**A measured movement outranks the reader's carried previous binding, and that ordering is the change.**
`previous_binding_digest` says what the reader was looking at when the read replaced that display; a
sync's own record says what happened to the reviewed inputs. The stronger fact wins, so a review whose
inputs a managed sync moved can never read as `current` — the packet's own non-conforming example — and
submission follows without a second rule, because the payload's constructor refuses a `stale`
comparison offered for submission. Both fields still read the one `staleness` value
(`stale = staleness.state == "stale"`, `:479`), so "an assessment is never submitted against a
comparison that has moved" remains one fact rather than two spellings of it.

**The measurement is the owner's, not this adapter's.** `review_sync_movement` and the fold
`review_staleness_with_sync_movement` are `application/review_sync_movement.py`'s (`:87-105`,
`:309-334`); this file contributes the one call site, placed where the comparison identity and the
resolved pair are both in scope, and the comment above it (`:470-474`) states why an unmeasured read is
carried as a fact rather than collapsed into a measured agreement. `None` means no measurement is
recorded — no enclosure contract to resolve a generation under, no published generation, no rebinding
recorded against it, a rebinding that does not describe it, or a read error along the way — and a live
review read never fails because a *measurement* was unavailable. The payload field is additive
(`models/knowledge/review.py:1022-1026`), so a read that measured nothing is the response it always was.

## Update History
- 2026-09-23T20:30:00+02:00 — 260921-ICR-L23 curator (memory worktree only; no code changed, no commits; leaf base `473ad8242bb4c22bdabed5d5253767350381eb3e` plus the working-tree delta): **the adapter now delegates and folds a second movement reading, and three reference rows in this card were re-anchored to the candidate's own bytes.** `compose_review` measures the raw-Git identity boundary beside the managed-sync one — `external_git_movement(resolved)` at `:491` feeding the new `review_staleness_with_external_movement` at `:492-496` — and publishes the measurement on the payload at `:556`; the module docstring states why the two movement readings are delegated the same way (`:46-52`). The three repaired rows are the ones whose anchors had moved under this leaf's own insertion at `:491` and the earlier refusal-vocabulary growth: `_selector_kind_or_absence` now cites its own construct (`:903-912`), `_comparison_refusal` its own (`:915-934`), and `review_sync_movement` the call site in the composition (`:483`). No claim was re-worded and no row was dropped to silence a finding. **No verification stamp was advanced**: the candidate is uncommitted, so no commit holds the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee):` **the composition measures the managed sync's rebinding and folds it into the staleness it publishes (`ICR-R22@v1`).** `compose_review` gained `review_sync_movement(resolved)` (`:475`) and `review_staleness_with_sync_movement(review_staleness(identity, request.previous_binding_digest), sync_movement)` (`:476-478`), and the payload gained `sync_movement=sync_movement` (`:537`) — one measurement, so a review whose inputs a managed sync moved can never read as `current`, and submission follows through the payload's existing stale/submission coupling rather than through a second rule. The body gained one section recording that ordering and the unmeasured-`None` fact beside it, and the reference table gained one row. **Citation accounting:** one row was **added** for this leaf's construct (`knowledge_review.py:475-478`, `application/review_sync_movement.py:87-105` and `:309-334`); no existing row, anchor or range on this card was moved, re-pointed, re-worded or dropped, because the curator's citation pass owns that work row by row. **Stamp accounting:** the header's verification pair is left exactly as recorded — `e605822eb3bf83bf63a45963c5f51d5fc28859ee`, this leaf's recorded base — and it is not advanced, because every construct cited in this entry exists only in this leaf's uncommitted working tree; the governed closeout owns the real stamp.

## 260921-ICR-L31 The Composition Answers Which Recorded Families The Selection Belongs To

**This composition now composes the comparison-bound family context once, after the relationship union
its member contexts reference (`ICR-R31@v1`).** ``compose_review`` gained one call — it builds a
``FamilyContextSources`` from the values the resolution already produced (the two databases, the
namespace, the two code roots, their code tree ids, the reviewed selector, the movement union and the
request's own page size) and passes the request's cursor only when the request named the
``family_members`` collection. The result travels on the payload as the required ``family_context``
field, so a review that read its recorded scope and holds no family states ``no_family_recorded``
rather than leaving an absent field to be read as one.

Two seams moved with it. The adapter's own ``_collection_page`` now answers ``None`` for the family
roster collection, because that page is the projection's own rather than one of the two owners this
function pages; and the published page/refusal for that collection is taken from the composition's
outcome, with the collection's own refusal standing in when a request named the collection without a
cursor — the collection is a *set* of per-family roster walks, so naming it addresses no single one.

**What this composition still does not do:** it selects no subject, widens no retrieval or policy
scope, restates none of the read owner's counts or cursors, and concludes nothing about a guarantee.
The family context is composed from the shipped read operation and the family/membership owners, and
its one bounded collection is continued with the read owner's own cursor.

**Citation accounting:** three rows of this card were re-anchored to the declarations they name after
this leaf's own additions moved them — the moved construct is cited at its own new extent, and no
claim cell was re-worded. No verification stamp was advanced beyond the honest basis below.

## Update History
- 2026-09-23T22:20:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): the composition now calls ``review_family_context`` once and carries its value on the payload as ``family_context`` (`ICR-R31@v1`); ``_collection_page`` no longer pages the family roster collection, and that collection's page or refusal comes from the projection's own outcome. Body updated with the real section above; no stamp advanced beyond the leaf's base plus the working-tree delta, because no commit contains what a stamp would otherwise claim to have verified.
