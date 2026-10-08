# mcp/src/agents_remember/application/knowledge_review.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The review adapter assembles the shipped source, knowledge and owner-record operations over one canonical task resolution. It selects no semantic frontier, authors no verdict and stores no composed answer.

## Code Commentary

### Logic

`read_complete_knowledge_review` resolves once, collects records over that same pair and composes the response. `review_candidate_resolution` binds converted knowledge as the exact baseline/candidate code and memory trees, captures live inputs through their existing owners and rechecks those inputs before publication. The adapter no longer reexports canonical baseline/candidate dataset path constants for retired ingest.

A request with no knowledge selector is a task-context review: it compares no knowledge operand and still returns the exact source inventory and named availability. A selected subject delegates head selection, relationship union, family context and derived-index views to their existing owners. Canonical datasets are retired; unconverted knowledge is `legacy-unavailable` while recorded source identities remain readable.

### Invariants And Boundaries

No guessed worktree, browser path, current HEAD or current knowledge replaces a recorded endpoint. Source review survives unavailable knowledge. Retired record classes remain unavailable without invented zero counts. Currentness and applicability are measured separately from authored dispositions. This adapter restores no canonical placement, publication or fallback route.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

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

- The adapter's own statement of what it selects (nothing), why the composition sits at this tier rather than in `serving/`, how the candidate is resolved from task context rather than from a path, that the endpoints are bound next door, and that **six** more responsibilities now live in their own modules — the last three the statement-side projection (ICR-R06), the head-selection policy (ICR-R07) and the subject catalogue (ICR-R09), each the one move (or replacement) that leaves no alias. [1]
- The public adapter surface includes the complete dashboard review operation alongside the existing review/catalogue/summary entry points, models and re-exported owner types. [2]

- The current resolver binds converted code/memory trees and index namespace; canonical path-constant reexports are retired. [3]

- The record kinds the review matrix is asked for — an input to L20's view rather than a selection policy of this module's — and the authored kinds the knowledge pane separates from the mechanical signals, which the record owner now **declares** and this module imports back so the counted collection and the rendered one cannot drift. [4]
- The record input set, its frozen shape and its single module-level empty value — now declared in the extracted record renderer and imported here, so `review_records_for` and the ingest CLI keep resolving. [5]
- **The resolution value — now the sibling module's: the two datasets, the two code roots, the two tree ids, the carried contract and the captured identity the recheck re-derives, and the record a closed leaf's review was reopened from.** [6]
- The one contract locator, now the sibling module's: the recorded task root, the globbed enclosures, the `repo_name`/`cleanup` skips and the leaf-id slug match. [7]
- **The whole comparison operation: delegate the resolution, then compose, with a refused resolution returned as a refused result before any comparison runs.** [8]
- **The entry operation: the same resolution as the comparison, then the pair's refusals through the shared `pair_preflight_refusal` (closed-leaf record, absent half, unreadable half, unreadable receipt — the rule the changed-intent summary also uses, since `260921-ICR-L47`), then the catalogue read — every recorded identity of both snapshots listed with presence and totals, no subject compared to earn its row. The enumeration itself is `review_subject_catalogue`'s, and the per-subject compare-to-earn-a-row helpers this module used to own are deleted.** [9]
- **The catalogue's own population read, which the entry operation delegates to: both snapshots' identities through the store's own two list operations, and the globally kind-grouped union with per-row presence.** [10]
- **The pair preflight and the pair this leaf opened out of it: the absent half named as `baseline` or `candidate`, the sibling fact beside it (a side that is present but cannot be read), the unreadable receipt refused through the shared owner, and the step that runs both only when a subject was named — because a task-context review compares no dataset.** [11]

- **The record-beside-the-bytes namespace this adapter threads through the whole render: the candidate's own sealed receipt when there is one, otherwise the before half's own `baseline-generation.json`, the requested repository used only when neither record exists, and an unreadable record refused rather than guessed past.** [12]
- The entry route's single refusal builder, carrying the resolution's own refusal verbatim. [13]
- **The composition: the observation made once and handed to both renderings, the task-context branch, the three pair refusals (absent, unreadable receipt, unreadable dataset), the comparison, the matrix read through the shipped view operation with its selection channels stated, the endpoint recheck immediately before the payload, and the panes with staleness, submission and the declared limits.** [14]
- **The recorded before/after relationship union traversed from the comparison's own page items and threaded into the source pane (`ICR-R08@v1`): one call, and the adapter adds no traversal logic of its own.** [15]
- **The comparison's own partition carried verbatim — never recomputed, because a second measurement could only disagree.** [16]
- The review matrix read as its own step, so the composition reads as measure, branch, open, compare, read, recheck, publish. [17]
- The shipped comparison call over the two already-resolved sides, with the probe and the candidate's own namespace passed through and no side or selector added. [18]
- The narrowing that lets a comparison refusal name a selector that is *absent* as `"no selector"` instead of reading `kind` through `None`, and the refusal it feeds. [19]
- **The comparison identity carried verbatim — now owned by [`application/review_comparison_staleness.py`](review_comparison_staleness.py.md): this leaf moved the identity helper out of this adapter and **deleted** its private `_comparison_identity` rather than keeping it as an alias, because nothing under `mcp/` imported it.** [20]
- The comparison's declared limits, omissions and side-absences **plus the inventory's own state**, carried as counted facts at the top level. [21]
- **The staleness rule — now owned by the sibling module: agreement, or an absent previous binding, is `current`; disagreement is `stale` with the carried identity retained as the labelled previous input and the moved axis named. This leaf deleted the private `_staleness` rather than keeping it as an alias.** [22]
- **Submission as the other statement of the same fact, and the payload validators that refuse a payload where the two disagree — including the one that ties `comparison is None` to `not_compared` and to the knowledge pane's selection state.** [23]
- The panes: identities and authored records never rendered as mechanical facts, the whole-task inventory, the six published remaining counts and the measured partition, and the evidence pane's two independent absence states — the last two now the extracted modules' own functions, called by both compositions. [24]
- **Pane 1's delegation, and the one wire-visible change this leaf made: the import of the statement-side module and the four calls inside `_knowledge_pane` that replaced the adapter's private `_side_content`/`_conditions`/`_field_changes`, where a changed structured field is now served as each side's own projection instead of `None`.** [25]
- **The cases that measure this adapter's one-sided output through the real composition: an addition, a removal, a one-sided field row, and a structured value served as its own projection on both sides.** [26]
- The per-subject assessment projection that reports an unmeasured assessment as not measured and a subject without an authored assessment as unassessed — now the extracted record renderer's, so both compositions display an unassessed collection identically. [27]
- The assessment displays and the observation displayed exactly with no sufficiency field, and the detection fact with no severity — all the extracted renderer's. [28]
- **The deleted prefer-both-sides rule and what replaced it: `_identity_item` and `_selector_record_id` are gone, and the pane renders the head selection instead.** The old rule preferred the item present on both sides — the retained predecessor both snapshots happen to hold — and used a one-sided item only for additions/removals. `ICR-R07@v1` deletes that preference: `compose_review` computes the before/after head pair from authored successor edges and `_knowledge_pane` renders it through `_selected_statements`, with ambiguity or unresolved lineage rendered as an explicit non-pair. [29]
- The selected source location, now rendered by the recorded-relationship display owner from the movement side (`ICR-R08@v1`), with the recorded role kept `None` rather than guessed and the counterpart address named only when the other side records exactly one. [30]
- The comparison's own statement about one claim's source observation, carried verbatim by the recorded-relationship owner (the moved `_change_state`), and the realization payload the recorded side is read from — the deleted `_realization_read_item` was that payload selection, now `side_payload`/`read_snapshot_relationships` in the same owner. [31]
- **The source half's own measurement: the delimiter-safe probe, the inventory value, its command, whether a name can be carried as text, and the byte form a name that cannot is carried by.** [32]
- **The entry that needs no subject: `comparison=None`, `staleness.state="not_compared"`, a knowledge pane in the `task_context` selection state, the measured pair attribution, and the reason it names — including an absent or unreadable dataset half when there is one.** [33]
- The refusal builder the composition reaches (`refused`, the extracted renderer's), the resolution module's refusal constructor it uses, and the **re-exported** record resolver the production port calls — whose owner is now the record module, and whose old assessment-only body is gone rather than kept beside it. [34]
- **The case that proves the surface stores nothing: the two datasets' row counts are identical across a full render.** [35]
- **The case that proves the adapter selects nothing: the comparison identity, item identities and counts are the shipped operation's own, compared value for value.** [36]
- The case that proves the candidate is resolved from task context and never from a browser-chosen path, and the case that proves an absent dataset refuses by name. [37]
- The case that proves a stale comparison keeps its previous input and disables submission, and the case that proves a current one cannot be built with submission disabled for staleness. [38]
- **The two cases the sibling leaf `260921-ICR-L5` added for the before half: an absent side refuses by name rather than being substituted with an empty one, and a side that is present but cannot be read refuses by name instead of raising.** [39]
- **The entry route's own before-half case, and the fact that it proves the damage is the cause: a damaged half is refused by name rather than raising from inside the comparison.** [40]
- **The case that measures the delegated resolution through the real composition: the bound endpoints published in the served payload.** [41]
- **The cases this leaf added for the task-context entry: a review with neither dataset half lists the complete source inventory and answers 200 on the real route with no selector parameters; and a knowledge-only change leaves an openable review whose inventory is a *measured* empty set while the comparison is untouched.** [42]
- The composition root that wires this adapter into the serving port. [43]
- **The composition measures what this leaf's own managed syncs recorded against the published generation and folds that measurement into the staleness it publishes (`ICR-R22@v1`): a measured movement outranks the reader's carried previous identity, so a review whose inputs a sync moved can never read `current`, and the payload carries the same measurement beside it.** [44]
- A tree comparison's family context carries the change facts of the returned members; a dataset review's is published as composed (MIK-L33). [45]
- The facts' owner. [46]


### Cross-Repo References

No cross-repository behavior is implemented in this file. The adapter reads one coordination root's
task tree and one candidate's disposable datasets, and carries no identity that ranges beyond the
repository namespace the request names.

No meaningful cross-repo references found.

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
  listed, so the catalogue can never answer for a pair nothing could open. *(Since `260921-ICR-L47` the
  whole ordered preflight — including this private helper, now public as `absent_pair_refusal` — lives
  in `application/review_pair_preflight.py`; see the section below.)*
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

## 260921-ICR-L47 The Entry's Pair Refusals Become One Shared Preflight

`260921-ICR-L47` (`ICR-R24@v3`) gives the task entry a changed-intent summary
([`review_intent_summary.py`](review_intent_summary.py.md)) that must refuse a pair exactly when the
catalogue does. This adapter therefore **delegates** its entry-route pair refusals to
[`review_pair_preflight.pair_preflight_refusal`](review_pair_preflight.py.md) — closed-leaf record
absence, an absent half, an unreadable half, then an unreadable candidate receipt, in that order —
and the private `_absent_pair_refusal` moved there unchanged as `absent_pair_refusal`. The order and
every refusal's wording are unchanged; the module shrank 1112 → 1075 lines and gained no feature logic.
The summary itself is a separate port wired by the composition root; it does not pass through this
adapter.
