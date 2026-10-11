# mcp/src/agents_remember/application/knowledge_review.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The review adapter assembles the shipped source, knowledge and owner-record operations over one canonical task resolution. It selects no semantic frontier, authors no verdict and stores no composed answer.

## Shared resolution at the dashboard operation

`read_complete_knowledge_review` is the complete dashboard operation: resolve the candidate once, collect owner records through `review_records_of`, and compose over that same resolution. The existing publication currentness check still recaptures both live worktrees and refuses a moved candidate. Record-only and older composition entry points keep their owned operations; they do not become another capture implementation. No composed review answer is stored on the server.

## Code Commentary

### Logic

`read_complete_knowledge_review` resolves once, collects records over that same pair and composes the response. `review_candidate_resolution` binds converted knowledge as the exact baseline/candidate code and memory trees, captures live inputs through their existing owners and rechecks those inputs before publication. The adapter no longer reexports canonical baseline/candidate dataset path constants for retired ingest.

A request with no knowledge selector is a task-context review: it compares no knowledge operand and still returns the exact source inventory and named availability. A selected subject delegates head selection, relationship union, family context and derived-index views to their existing owners. Canonical datasets are retired; unconverted knowledge is `legacy-unavailable` while recorded source identities remain readable.

### Invariants And Boundaries

No guessed worktree, browser path, current HEAD or current knowledge replaces a recorded endpoint. Source review survives unavailable knowledge. Retired record classes remain unavailable without invented zero counts. Currentness and applicability are measured separately from authored dispositions. This adapter restores no canonical placement, publication or fallback route.

### Todos

None recorded.

### Logic

**Resolution is delegated, and this module no longer defines it.** What the delegation leaves here is the *call*: `read_knowledge_review` and
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
catalogue can open would otherwise raise out of the call that exists to offer a subject. Since
`260921-ICR-L47` those refusals are one call, `pair_preflight_refusal(resolved)` from
[`review_pair_preflight.py`](review_pair_preflight.py.md), in the same order; the changed-intent
summary shares it, so the task entry cannot count a pair its catalogue refuses.

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

**The records bundle arrives already marked, and the composition renders it as it arrives.** `compose_review` takes the `ReviewRecordInputs` bundle as a parameter (defaulting to `EMPTY_REVIEW_RECORDS`); subject states come from `subject_states(records)` and the pane's signals from `records.signals`. No selection helper builds channels here — `with_selection_channels`, `MatrixSelection` and `_matrix_rows_remaining` left with the review matrix (MIK-R74 rule 1) — and the authored-effects channel arrives unavailable with its removal as the reason rather than being counted from view rows. A review that rendered a bounded page reports the served view's own bound instead of presenting the page it read as the whole selection.

**The five subjects the payload states are assembled from the comparison and the supplied records.** `_knowledge_pane` renders identities, both
sides' exact statements and conditions, the retained-revision groups, every field transition the
comparison reported, the detection signals, the
assessment displays and no authored rows or unresolved-author references (the matrix renderers are gone with the matrix). The other two panes are no
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

**`review_records_for` left this module for the record owner, and the name here is a re-export**
(`ICR-R14@v1`). The resolver used to read the published assessment collection and collapse an absent
authority and an unreadable one into `EMPTY_REVIEW_RECORDS`; both of those are now *states* on the
bundle, and the whole collection resolution lives in
[`application/review_evidence_records.py`](review_evidence_records.py.md). No channel-counting kinds are declared or re-exported here: the authored-effects channel is unavailable with its removal as the reason, and what `_knowledge_pane` renders for signals comes from `records.signals`.

**The family context carries change-kind facts on a tree comparison (MIK-L33, MIK-R33).** `compose_review` publishes
`family_context=with_change_kinds(family.context, resolved.trees)`: for a tree comparison every family entry comes back
carrying `change_kinds`, the facts of the member occurrences this page returned, computed by
`application/review_change_kinds.py` over MIK-L32's lane (one `open_tree_lane` per read); a dataset review
(`resolved.trees` is `None`) gets its context back exactly as composed, and the served body omits the null field
(`exclude_none`). The dataset guard lives in `with_change_kinds` rather than here, which kept `compose_review`'s
complexity at C (the worker's radon note). The adapter adds no fact of its own. The file is 1,078 lines (1,075 on
MIK-L33's base).

### Conventions

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
  the shipped operations and writes no file
- **Rank is the reason for the ports.** `serving/review.py` takes `read_knowledge_review` and
  `list_knowledge_review_entries` as ports supplied by the composition root, because a serving module
  may not import them.

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
- The panes: identities never rendered as mechanical facts and no authored rows at all, the whole-task inventory, the six published remaining counts and the measured partition, and the evidence pane's two independent absence states — the last two now the extracted modules' own functions, called by both compositions. [24]
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

### Repo-Internal References

- The dashboard operation shares one resolution with records and composition. [47]
## 260921-ICR-L10 The Adapter Offers A Cursor To The Collection It Names

`260921-ICR-L10` (`ICR-R10@v1`) carries a request's cursor to the collection that names it. The
adapter still delegates the page arithmetic to `review_pagination.py`; what it gained is the wiring: the
request's `page_of`/`continuation`/`page_size` are offered to that collection's own owner, the comparison
and the matrix are read at that position, and the one page the request named is published beside the
panes — with the refusal it earned when a requested page could not be served.

Two renames came with the matrix retirement, and a reader should read the retired names as gone rather than new behavior:
the task-context branch builds no selection channels anymore, and a refused cursor leaves the payload with no page and the removed collection earning `comparison_page_unreadable`, never a measured zero: a refused read has no counts, and a page of invented zeros would be
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
