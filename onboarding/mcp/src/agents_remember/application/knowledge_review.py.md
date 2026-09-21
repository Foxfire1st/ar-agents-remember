# mcp/src/agents_remember/application/knowledge_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T15:17:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l2`, uncommitted; production line `0fca5c69766aa95eebe950c19fbcdc83864ec35a` (leaf `260921-ICR-L5`'s landed cold-start work) with leaf `260921-ICR-L2`'s uncommitted review-surface work applied |
| lastVerifiedCommitHash | `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9` |
| lastVerifiedCommitDate | 2026-09-21T16:05:56+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

The Intent Reviewer's thin adapter over the shipped read, diff and view operations. It **selects
nothing**: it delegates which candidate a task context names to
`application/review_candidate_resolution.py`, calls the operations, and assembles their results into
the typed payload `models/knowledge/review.py` declares. R07's selection policy, R08's comparison
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

**Three more responsibilities were extracted in the same pass, and each one is named for what it
owns.** `application/review_source_inventory.py` measures the exact, status-bearing source-change
inventory of the bound tree pair and renders the source pane; `application/review_record_rendering.py`
renders the record collections the caller supplied into the evidence and submission values; and
`application/review_task_context.py` composes the entry that needs no selected subject. This adapter
keeps only imports and calls to them, and every name that moved is re-exported below, so no importer
had to learn a new home and no responsibility has two implementations.

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

**`review_namespace` reads the namespace from the candidate's own receipt, and that is the only
authority for it.** The function is the sibling module's; this adapter is the caller that threads its
answer through the whole render. A request names a *repository* (`agents-remember`); a candidate the
write plane admitted is bound to a *namespace id* derived from it
(`uuid5(namespace, "repository:<name>")`). A side opened under the requested spelling therefore refuses
against the dataset's own binding — the fixture measured `the dataset … is bound to 40d350a6-…, not to
the requested repository namespace agents-remember` — which in the live product would have failed the
review of every real candidate. So the candidate's own **receipt** (written and sealed beside the
working database by the admission that created it) is read, and `repository_id` from that receipt is the
namespace `compose_review` opens both sides and the review matrix under. A candidate with **no** receipt
beside its database is a dataset handed directly rather than admitted (a fixture, or a pair a caller
assembled from two named files): for that shape the requested repository is the available identity and
is read as it always was. A receipt that **exists but cannot be read** is refused, because standing in
the caller's word for the dataset's own record is exactly how a review comes to read a namespace nothing
admitted.

**`list_knowledge_review_entries` is the surface's entry half, and it exists because the reviewed
subject is the one input a reader cannot supply.** The subject is a recorded identity inside the
candidate, and the browser must not choose the candidate, so the task view asks the server instead of
guessing. It resolves through the *identical* operation `read_knowledge_review` uses — canonical task
context only, one contract, one derived root — so the list a caller is offered and the review it then
opens cannot disagree about which datasets are being compared. A subject is offered exactly when the
**shipped comparison** reaches it: `_recorded_identities` reads the candidate's own recorded invariant
and family identities through the store's own `list_invariants`/`list_families` (not a query written
here), each is compared through `diff_knowledge_scope` for that identity, and only the ones the
operation answers with a page are listed. `_selected_item_count` returns the page's own
`counts.items_total`, and returns `None` — dropping the subject — when the comparison refused, because
an entry that opens a refusal is worse than no entry at all. Nothing is recorded to make that true and
no ranking is applied: a candidate that records no identity the pair can compare yields an empty list,
which the caller renders as no entry rather than as an invitation to name one. **Both pair refusals are
therefore stated before any subject is compared** — the absent half first, and since leaf
`260921-ICR-L5` the unreadable half beside it (see the paragraph below) — because the per-subject
comparison runs once per recorded identity and a side no comparison can open would otherwise raise out
of the call that exists to offer a subject.

**A side that is present but cannot be read is a named refusal on both routes, and leaf
`260921-ICR-L5` added the two call sites that make it so.** `missing_dataset_half` answers *absence*;
the sibling fact — a file that is there and is not a dataset of this code — used to reach SQLite and
come back as an `apsw.NotADBError` raised from inside the comparison, so an operator got a traceback
where this surface promises a state naming the side. `unreadable_half_refusal(baseline, candidate)` (in
[`application/knowledge_before_half.py`](knowledge_before_half.py.md)) preflights both sides — the
before half through its recorded origin as well as its bytes — and returns the typed refusal or `None`.
`compose_review` states it after its own docstring and before `missing_dataset_half`, and
`list_knowledge_review_entries` states it after its absent-half check and before `_reviewable_entries`,
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

**`compose_review` measures the source inventory first and unconditionally, then splits on whether a
subject was named, and re-checks the captured endpoints last.** `review_inventory` runs before any
dataset is opened and before the selector branch, from the two tree ids the resolution bound: it is the
one half of a review that cannot depend on a knowledge selection, and measuring it only after a
comparison succeeded is how a task with no invariant — or with no datasets at all — came to lose its
source review entirely. A request with **no selector** is then answered by
`review_task_context.task_context_review`, which composes `comparison=None`,
`staleness.state="not_compared"` and a knowledge pane in the `task_context` selection state, so an
absent knowledge half stays a stated fact rather than a refused read. A request that **does** name a
selector keeps the shipped behaviour exactly: `_open_dataset_pair` refuses an absent dataset half as
`candidate_dataset_absent` naming which half is missing (and the instruction to author the candidate's
knowledge in the leaf's disposable root, or to place the dataset it forks from in the baseline half),
and reads the namespace once through `review_namespace` so one render cannot open its two sides and its
matrix under two different namespaces; `_compare` then calls the shipped comparison, and a comparison
that is not `state == "page"`, or that carries no page or no binding, becomes a `comparison_refused`
result through `_comparison_refusal`, which carries the shipped refusal's own `code`, `detail` and
`next_action` through verbatim rather than inventing a summary. `_selector_kind_or_absence` is what lets
that refusal spell a selector that is absent as `"no selector"` instead of reading `kind` through
`None`.

**The review matrix is read from the candidate through L20's operation, not recomputed.**
`read_knowledge_view` is handed the candidate database, the diff side opened by `open_diff_side` over
the same database and code root, and a `ViewRequest(view="review_matrix", record_kinds=REVIEW_MATRIX_KINDS)`.
A view that is not `state == "view"` becomes `comparison_refused` with the view's own detail appended,
so the surface never renders a pane from a partial matrix. `REVIEW_MATRIX_KINDS` is the *input* the
view is asked for — the five record kinds — rather than a selection policy of this leaf's; the view
applies its own registered traversal over them.

**The five subjects the payload states are assembled from the matrix rows and the supplied records,
and the two authored/mechanical collections never mix.** `_knowledge_pane` renders identities, both
sides' exact statements and conditions, the retained-revision groups, every field transition the
comparison reported, the authored records (`AUTHORED_EFFECT_KINDS`), the detection signals, the
assessment displays and one unresolved-author reference per authored row. The other two panes are no
longer composed here: `source_pane` (in `review_source_inventory`) renders the inventory first and then
the realization items as selected locations, the five published remaining counts, the expansion
reference and command, the attributed/unattributed changed paths, and one unresolved attribution row
per item the other side's selection did not reach; `evidence_pane` (in `review_record_rendering`)
renders the evidence links, the observations and the assessments, with `evidence_state` and
`assessment_state` computed from the collections themselves. Both are the same functions the
task-context composition calls, which is what keeps an unassessed collection reading identically in
both.

**Staleness and submission are two statements of one fact, and the payload model enforces it.**
`_staleness` returns `current` when there is no `previous_binding_digest` or it equals the comparison's
own `binding_digest`, and `stale` otherwise — retaining the previous digest as a *labelled previous
input* together with the moved axis. `submission` returns `disabled_stale` exactly when stale and
`unavailable` otherwise, and in both cases publishes `PROPOSED_ASSESSMENT_DISPOSITIONS` rather than a
control of this module's own. `KnowledgeReviewPayload`'s validator refuses the payload where the two
disagree, so "an assessment is never submitted against a comparison that has moved" is a property of
the value; its second validator holds the identity and the staleness state in agreement the other way
round, so `comparison is None` is true exactly when the state is `not_compared` and the knowledge
pane's `selection_state` says which question the payload answered.

**The inventory's own state is a declared limit of the response, not a pane detail.** `_limitations`
carries the comparison's limits and counted omissions **and** `inventory_limitations(inventory)`, so an
unavailable measurement (`limitation:source_inventory_unavailable`) and a partial one
(`limitation:source_inventory_partial`) are named at the top level beside the comparison's own
limitations — a limit a reader has to open a pane to discover is a limit the response did not state.
The task-context composition adds `limitation:no_knowledge_subject_selected` beside them.

**Five counts are published, and a count that has no meaning says so instead of reporting zero.**
`locations_remaining` and `records_present_outside_selection` are measured from the page;
`references_unresolved` is the page's own `suppressed_total`; and
`changed_paths_outside_selection` and `unattributed_changed_paths` carry `value=None` with a stated
reason when the comparison published no source expansion, because "not measured here" and "measured as
none" are different facts. `ReviewRemainingCount`'s validator refuses an unexplained absent count and
refuses a measured count that also carries a not-applicable reason.

**`review_records_for` reads the published assessment collection and treats absence as an empty
collection, not an error.** It resolves the candidate, returns `EMPTY_REVIEW_RECORDS` when the
resolution refuses or carries no contract, loads the curator-coherence authority through the shipped
`load_curator_coherence_authority`, and returns `EMPTY_REVIEW_RECORDS` for a `CuratorCoherenceError`,
`OSError` or `ValueError` rather than failing. No `current` measurement is supplied, so the extracted
`subject_states` reports every stored assessment `stale` — the shipped projection refuses to promote
an unmeasured assessment to current and this surface does not improve on that by guessing.

### Conventions

The module holds no vocabulary of its own: every value it returns is a shipped type — the review
models from `models/knowledge/review.py`, the diff models, the detection payload and the read models.
`ReviewSurfaceRequest` is imported for re-export and named in `__all__` beside
`read_knowledge_review`, `list_knowledge_review_entries`, `compose_review`, `review_records_for`,
`ReviewRecordInputs`, `EMPTY_REVIEW_RECORDS` and `REVIEW_MATRIX_KINDS`, and beside the names that are
**re-exported** from the two extracted modules — `review_candidate_resolution`'s
`resolve_review_candidate`, `ReviewCandidateResolution`, `REVIEW_CANDIDATE_RELATIVE_ROOT`,
`REVIEW_BASELINE_DIRECTORY`, `REVIEW_CANDIDATE_DIRECTORY` and (in the reference table below)
`candidate_ref`, `missing_dataset_half`, `review_namespace` and `refusal`; and
`review_record_rendering`'s `ReviewRecordInputs` and `EMPTY_REVIEW_RECORDS`, which are declared there
and imported here so the ingest CLI and the test modules that import them keep resolving.
`ReviewRecordInputs` and `ReviewCandidateResolution` are frozen dataclasses rather than pydantic
models, because they carry live paths and a loaded contract rather than a wire shape. `refused` — the
extracted record renderer's — is the single builder of a refused result **reached from this module**,
and `refusal(...)` — the resolution module's — the single builder of a refusal value, so no code path
in this module raises out of `read_knowledge_review`. The private helpers that remain are deliberately
one-purpose: `_selector_record_id` reads `kind` off the seed through `getattr` and returns `None` for
any seed kind that is not an identity, so a non-identity selector addresses no identity item rather
than a guessed one; `_entry_refused` is the entry route's single builder of a refused list — the
spelling the merged candidate carries, which the code-side sync's reapplication kept as it was (the
card's first pass had recorded the pre-sync candidate's one-word `_entryrefused`; see the history);
`_review_matrix` reads L20's view or returns the refusal it earned; `_selector_kind_or_absence` narrows
the optional selector at the one place a refusal spells it; and `_reviewable_entries` threads one
namespace through every comparison it runs.

### Invariants And Boundaries

- **The adapter selects nothing.** The comparison, the item identities, the counts, the field
  transitions and the revision groups are the shipped operations' own values; the module adds no
  ordering, no ranking, no filter and no re-diff. The entry list obeys the same rule: it offers a
  subject exactly when the shipped comparison answered for it, drops a refused one, and applies no
  ranking — so it is not a selection policy in disguise.
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
- **One responsibility, one implementation.** The inventory, the record rendering and the task-context
  composition each live in exactly one module; this adapter imports and calls them and re-exports what
  moved. Two implementations of "what did these two trees change" — the review's inventory and the
  comparison's expansion — were collapsed into one by this leaf.
- **A subject the comparison refuses is dropped, not listed with a zero.** `_selected_item_count`
  returns `None` for a refused comparison and the entry is omitted, so an entry cannot open a refusal.
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

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the adapter's own docstring and
functions, the three modules that now own resolution, the source inventory and the record rendering,
the shipped comparison and view operations it calls, the models module that declares the payload, and
the test modules that drive the whole surface. Four details a reader should carry: **the resolution is
not defined here any more** — the three `REVIEW_*` path constants, `resolve_review_candidate`,
`ReviewCandidateResolution`, `missing_dataset_half`, `review_namespace`, `refusal` and
`require_current_candidate_identity` are `application/review_candidate_resolution.py`'s and are
imported/re-exported here, which is the import path `cli/knowledge_ingest.py` still uses; **the source
half and the record rendering moved out in this leaf** — `review_inventory`, `source_pane`,
`inventory_limitations`, `tree_difference_observation` and the source pane's own `_location` are
`application/review_source_inventory.py`'s, and `refused`, `submission`, `evidence_pane`,
`subject_states`, `assessment_displays`, `signal` and `observation` are
`application/review_record_rendering.py`'s, so `__all__` is unchanged while the implementations are
not here; both halves' directory names are **published** because the ingest CLI authors into the same
root; and the candidate side resolves to **both** a code root and a tree id, from the capture, because
a recorded base commit is a precondition and the add-all candidate tree is what the anchors are
resolved against.

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter's own statement of what it selects (nothing), why the composition sits at this tier rather than in `serving/`, how the candidate is resolved from task context rather than from a path, that the endpoints are bound next door, and that three more responsibilities now live in their own modules. | `resolve_review_candidate`; `require_current_candidate_identity`; `review_source_inventory`; `review_task_context` | mcp/src/agents_remember/application/knowledge_review.py:1-41; mcp/src/agents_remember/application/knowledge_review.py:43-123; mcp/src/agents_remember/application/review_candidate_resolution.py:135-199; mcp/src/agents_remember/application/review_candidate_resolution.py:221-250 |
| **The published adapter surface: the three entry points, the two dataclasses, the request model and the record-kind constant — and, re-exported from the sibling modules, the resolution callable, the resolution value, `candidate_ref` and the three published path constants.** | `__all__` | mcp/src/agents_remember/application/knowledge_review.py:125-142 |
| The re-export itself: the import block that makes the sibling modules' names this module's public surface and keeps the ingest CLI's existing import resolving — the resolution surface and `candidate_ref` from `review_candidate_resolution`, and `EMPTY_REVIEW_RECORDS`/`ReviewRecordInputs` from `review_record_rendering`. | `resolve_review_candidate`; `REVIEW_BASELINE_DIRECTORY`; `refusal`; `candidate_ref`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/knowledge_review.py:43-123; mcp/src/agents_remember/application/review_candidate_resolution.py:328-342 |
| The record kinds the review matrix is asked for — an input to L20's view rather than a selection policy of this module's — and the authored kinds the knowledge pane separates from the mechanical signals. | `REVIEW_MATRIX_KINDS`; `AUTHORED_EFFECT_KINDS` | mcp/src/agents_remember/application/knowledge_review.py:143-153; mcp/src/agents_remember/application/knowledge_review.py:154-156 |
| The record input set, its frozen shape and its single module-level empty value — now declared in the extracted record renderer and imported here, so `review_records_for` and the ingest CLI keep resolving. | `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/review_record_rendering.py:59-77; mcp/src/agents_remember/application/knowledge_review.py:43-123 |
| **The resolution value — now the sibling module's: the two datasets, the two code roots, the two tree ids, the carried contract and the captured identity the recheck re-derives.** | `ReviewCandidateResolution` | mcp/src/agents_remember/application/review_candidate_resolution.py:102-132 |
| The one contract locator, now the sibling module's: the recorded task root, the globbed enclosures, the `repo_name`/`cleanup` skips and the leaf-id slug match. | `_leaf_contract`; `load_contract`; `slugify` | mcp/src/agents_remember/application/review_candidate_resolution.py:382-402; mcp/src/agents_remember/worktrees/worktree_contract.py:430-472; mcp/src/agents_remember/worktrees/task_resolver.py:16-27 |
| **The whole comparison operation: delegate the resolution, then compose, with a refused resolution returned as a refused result before any comparison runs.** | `read_knowledge_review`; `refused` | mcp/src/agents_remember/application/knowledge_review.py:161-189; mcp/src/agents_remember/application/review_record_rendering.py:80-85 |
| **The entry operation: the same resolution as the comparison, then one comparison per recorded identity, with a refused subject dropped instead of listed with a zero — and, since leaf `260921-ICR-L5`, with the unreadable-half refusal stated before that loop.** | `list_knowledge_review_entries`; `_reviewable_entries`; `unreadable_half_refusal` | mcp/src/agents_remember/application/knowledge_review.py:192-273; mcp/src/agents_remember/application/knowledge_review.py:276-307; mcp/src/agents_remember/application/knowledge_before_half.py:344-374 |
| **The recorded identities the entry list offers, read through the store's own two list operations rather than a query written here, and the per-subject count taken from the comparison's own page.** | `_recorded_identities`; `_selected_item_count`; `list_invariants`; `list_families` | mcp/src/agents_remember/application/knowledge_review.py:310-327; mcp/src/agents_remember/application/knowledge_review.py:330-354; mcp/src/agents_remember/memory/knowledge/store.py:181-197; mcp/src/agents_remember/memory/knowledge/store.py:199-214 |
| **The pair preflight and the pair this leaf opened out of it: the absent half named as `baseline` or `candidate`, the sibling fact beside it (a side that is present but cannot be read), and the step that runs both only when a subject was named — because a task-context review compares no dataset.** | `missing_dataset_half`; `unreadable_half_refusal`; `_open_dataset_pair` | mcp/src/agents_remember/application/review_candidate_resolution.py:279-297; mcp/src/agents_remember/application/knowledge_before_half.py:344-374; mcp/src/agents_remember/application/knowledge_review.py:449-494 |
| **The receipt-derived namespace this adapter threads through the whole render: read from the candidate's own sealed receipt, the requested repository used only when no receipt exists, and an unreadable receipt refused rather than guessed past.** | `review_namespace`; `CANDIDATE_RECEIPT_NAME` | mcp/src/agents_remember/application/review_candidate_resolution.py:300-325; mcp/src/agents_remember/models/knowledge/snapshot.py:52-72 |
| The entry route's single refusal builder, carrying the resolution's own refusal verbatim. | `_entry_refused` | mcp/src/agents_remember/application/knowledge_review.py:357-368 |
| **The composition: the inventory measured first and unconditionally, the task-context branch, the two pair refusals (absent, then unreadable), the comparison, the matrix read through the shipped view operation, the endpoint recheck immediately before the payload, and the panes with staleness, submission and the declared limits.** | `compose_review`; `require_current_candidate_identity`; `read_knowledge_view`; `ViewRequest`; `unreadable_half_refusal` | mcp/src/agents_remember/application/knowledge_review.py:371-446; mcp/src/agents_remember/application/review_candidate_resolution.py:221-250; mcp/src/agents_remember/application/knowledge_views.py:86-112; mcp/src/agents_remember/models/knowledge/view.py:1117-1160; mcp/src/agents_remember/application/knowledge_before_half.py:344-374 |
| The review matrix read as its own step, so the composition reads as measure, branch, open, compare, read, recheck, publish. | `_review_matrix` | mcp/src/agents_remember/application/knowledge_review.py:497-524 |
| The shipped comparison call over the two already-resolved sides, with the probe and the candidate's own namespace passed through and no side or selector added. | `_compare`; `diff_knowledge_scope` | mcp/src/agents_remember/application/knowledge_review.py:527-566; mcp/src/agents_remember/application/knowledge_diff.py:176-230 |
| The narrowing that lets a comparison refusal name a selector that is *absent* as `"no selector"` instead of reading `kind` through `None`, and the refusal it feeds. | `_selector_kind_or_absence`; `_comparison_refusal` | mcp/src/agents_remember/application/knowledge_review.py:569-578; mcp/src/agents_remember/application/knowledge_review.py:581-600 |
| The comparison identity carried verbatim, and the limits/omissions/side-absences **plus the inventory's own state** carried as counted facts at the top level. | `_comparison_identity`; `_limitations`; `inventory_limitations` | mcp/src/agents_remember/application/knowledge_review.py:603-619; mcp/src/agents_remember/application/knowledge_review.py:622-645; mcp/src/agents_remember/application/review_source_inventory.py:178-190 |
| **Staleness and submission as two statements of one fact, and the payload validators that refuse a payload where they disagree — including the one that ties `comparison is None` to `not_compared` and to the knowledge pane's selection state.** | `_staleness`; `submission`; `KnowledgeReviewPayload` | mcp/src/agents_remember/application/knowledge_review.py:648-663; mcp/src/agents_remember/application/review_record_rendering.py:88-115; mcp/src/agents_remember/models/knowledge/review.py:711-772 |
| The panes: identities and authored records never rendered as mechanical facts, the whole-task inventory and the five published remaining counts, and the evidence pane's two independent absence states — the last two now the extracted modules' own functions, called by both compositions. | `_knowledge_pane`; `source_pane`; `evidence_pane` | mcp/src/agents_remember/application/knowledge_review.py:666-699; mcp/src/agents_remember/application/review_source_inventory.py:540-580; mcp/src/agents_remember/application/review_record_rendering.py:118-154 |
| The per-subject assessment projection that reports an unmeasured assessment stale rather than promoting it to current — now the extracted record renderer's, so both compositions display an unassessed collection identically. | `subject_states`; `assessment_state_for` | mcp/src/agents_remember/application/review_record_rendering.py:157-176; mcp/src/agents_remember/models/lifecycles/review_assessment.py:441-479 |
| The assessment displays and the observation displayed exactly with no sufficiency field, and the detection fact with no severity — all the extracted renderer's. | `assessment_displays`; `_assessment_display`; `observation`; `signal` | mcp/src/agents_remember/application/review_record_rendering.py:179-195; mcp/src/agents_remember/application/review_record_rendering.py:198-212; mcp/src/agents_remember/application/review_record_rendering.py:215-233; mcp/src/agents_remember/application/review_record_rendering.py:236-250 |
| **The reviewed subject chosen by the selector that named it: a sibling's item is never substituted, and a subject the comparison holds on both sides is preferred.** | `_identity_item`; `_selector_record_id` | mcp/src/agents_remember/application/knowledge_review.py:702-728; mcp/src/agents_remember/application/knowledge_review.py:731-739 |
| The selected source location with its recorded role kept `None` rather than guessed, and the change state derived from the comparison's own observation — both moved with the pane they render. | `_location`; `_change_state`; `_realization_read_item` | mcp/src/agents_remember/application/review_source_inventory.py:655-678; mcp/src/agents_remember/application/review_source_inventory.py:688-694; mcp/src/agents_remember/application/review_source_inventory.py:681-685 |
| **The source half's own measurement: the delimiter-safe probe, the inventory value, its command, whether a name can be carried as text, and the byte form a name that cannot is carried by.** | `tree_difference_observation`; `review_inventory`; `inventory_command`; `is_text_path`; `byte_form` | mcp/src/agents_remember/application/review_source_inventory.py:193-235; mcp/src/agents_remember/application/review_source_inventory.py:428-454; mcp/src/agents_remember/application/review_source_inventory.py:410-425; mcp/src/agents_remember/application/review_source_inventory.py:238-260 |
| **The entry that needs no subject: `comparison=None`, `staleness.state="not_compared"`, a knowledge pane in the `task_context` selection state, and the reason it names — including an absent dataset half when there is one.** | `task_context_review`; `task_context_detail`; `_task_context_pane` | mcp/src/agents_remember/application/review_task_context.py:61-114; mcp/src/agents_remember/application/review_task_context.py:153-184; mcp/src/agents_remember/application/review_task_context.py:127-150 |
| The refusal builder the composition reaches (`refused`, the extracted renderer's), the resolution module's refusal constructor it uses, and the published assessment collection read from the curator authority's own publication with an absent authority treated as empty rather than as an error. | `refused`; `refusal`; `review_records_for`; `load_curator_coherence_authority` | mcp/src/agents_remember/application/review_record_rendering.py:80-85; mcp/src/agents_remember/application/review_candidate_resolution.py:328-342; mcp/src/agents_remember/application/knowledge_review.py:863-888; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:255-280 |
| **The case that proves the surface stores nothing: the two datasets' row counts are identical across a full render.** | `test_the_surface_stores_nothing_so_deleting_every_rendering_loses_no_canonical_information` | mcp/tests/test_knowledge_review_surface.py:460-470 |
| **The case that proves the adapter selects nothing: the comparison identity, item identities and counts are the shipped operation's own, compared value for value.** | `test_the_adapter_selects_nothing_because_the_shipped_comparison_is_the_comparison_rendered` | mcp/tests/test_knowledge_review_surface.py:473-522 |
| The case that proves the candidate is resolved from task context and never from a browser-chosen path, and the case that proves an absent dataset refuses by name. | `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`; `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one` | mcp/tests/test_knowledge_review_surface.py:751-764; mcp/tests/test_knowledge_review_surface.py:767-786 |
| The case that proves a stale comparison keeps its previous input and disables submission, and the case that proves a current one cannot be built with submission disabled for staleness. | `test_the_stale_rule_holds_in_both_directions` | mcp/tests/test_knowledge_review_surface.py:589-611 |
| **The two cases the sibling leaf `260921-ICR-L5` added for the before half: an absent side refuses by name rather than being substituted with an empty one, and a side that is present but cannot be read refuses by name instead of raising.** | `test_an_absent_baseline_half_refuses_by_name_rather_than_substituting_an_empty_one`; `test_a_before_side_that_is_present_but_unreadable_refuses_by_name` | mcp/tests/test_knowledge_review_surface.py:789-825; mcp/tests/test_knowledge_review_surface.py:828-869 |
| **The entry route's own before-half case, and the fact that it proves the damage is the cause: a damaged half is refused by name rather than raising from inside the comparison.** | `test_the_entry_route_refuses_a_damaged_before_half_instead_of_raising` | mcp/tests/test_knowledge_review_surface.py:938-976 |
| **The case that measures the delegated resolution through the real composition: the bound endpoints published in the served payload.** | `test_the_rendered_review_publishes_the_endpoints_and_reaches_the_whole_candidate`; `test_a_capture_input_that_moves_before_publication_is_refused_by_name` | mcp/tests/test_knowledge_review_source_endpoints.py:394-456; mcp/tests/test_knowledge_review_source_endpoints.py:459-483 |
| **The cases this leaf added for the task-context entry: a review with neither dataset half lists the complete source inventory and answers 200 on the real route with no selector parameters; and a knowledge-only change leaves an openable review whose inventory is a *measured* empty set while the comparison is untouched.** | `test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all`; `test_a_knowledge_only_change_leaves_an_openable_review_with_a_measured_empty_inventory` | mcp/tests/test_knowledge_review_source_endpoints.py:674-750; mcp/tests/test_knowledge_review_surface.py:1161-1210 |
| The composition root that wires this adapter into the serving port. | `review_port`; `read_knowledge_review` | mcp/src/agents_remember/cli/dashboard.py:67-111 |


## Cross-Repo References

No cross-repository behavior is implemented in this file. The adapter reads one coordination root's
task tree and one candidate's disposable datasets, and carries no identity that ranges beyond the
repository namespace the request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **the sync's memory-side conflict in this card resolved as a union: the master line's cold-start and unreadable-half facts, this leaf's three extractions and task-context entry, and both sides' history.** Every range in the reference table was re-derived against the merged 888-line adapter rather than carried from either side. **Corrected rather than merged:** `__all__` moved to `125-142` and the import block to `43-123`; `read_knowledge_review` to `161-189`; `list_knowledge_review_entries`/`_reviewable_entries` to `192-273`/`276-307`; `_recorded_identities`/`_selected_item_count` to `310-327`/`330-354`; `_entry_refused` to `357-368` — and **the name itself is corrected here**: this card's first pass recorded the pre-sync candidate's one-word `_entryrefused`, while the merged worktree carries `_entry_refused`, so the row and the Conventions paragraph now say what the code says; `compose_review` to `371-446`; `_review_matrix` to `497-524`; `_compare` to `527-566`; `_selector_kind_or_absence` to `569-578`; `_comparison_identity`/`_limitations` to `603-619`/`622-645`; `_staleness` to `648-663`; `_knowledge_pane` to `666-699`; `_identity_item`/`_selector_record_id` to `702-728`/`731-739`; `review_records_for` to `863-888`. The master side's `_entry_refused`, `_submission`, `_source_pane`, `_evidence_pane`, `_subject_states`, `_assessment_display`, `_observation`, `_location`, `_change_state` and `_refused` rows were **superseded, not duplicated**: those constructs still exist, but under their extracted names and in the modules that now own them, and the table says so. L5's `unreadable_half_refusal` facts were kept and merged into the entry-operation, pair-preflight and composition rows; L5's two new before-half cases and its entry-route case were kept with their own ranges re-derived (`789-825`, `828-869`, `938-976`). No claim was dropped and none was invented.
- 2026-09-21T15:10+02:00 — 260921-ICR-L5 curator, **two enforced rows re-read and re-cited: the sibling module's declarations added beside this adapter's import block.** The claim about the re-export and the claim about the adapter's own statement of what it selects both name constructs that live next door, so each row now cites the declaration that supports its words (`resolve_review_candidate` `review_candidate_resolution.py:130-194`, `require_current_candidate_identity` `:197-226`, `refusal` `:304-318`, `REVIEW_BASELINE_DIRECTORY` `:78-78`) rather than only the import site. Claim wording is retained: each still states what the code does at the construct it names. No verification stamp was advanced.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the adapter shrank to a delegator and gained an entry that needs no subject.** Three responsibilities left this file for modules named for what they own — `application/review_source_inventory.py` (the exact source-change inventory of the bound tree pair and the source pane), `application/review_record_rendering.py` (the record collections the caller supplied, rendered as pane values) and `application/review_task_context.py` (the task-context composition) — and `compose_review` now **measures the inventory first and unconditionally**, before any dataset is opened and before the selector branch, then splits: a request with `selector=None` is answered by `task_context_review` with `comparison=None`, `staleness.state="not_compared"` and a knowledge pane in the `task_context` selection state, while a request that names a subject keeps the shipped path through the new `_open_dataset_pair` and `_review_matrix` steps. `_limitations` now declares `inventory_limitations(inventory)` at the top level beside the comparison's own limits, and `_selector_kind_or_absence` is what lets a comparison refusal spell an absent selector instead of reading `kind` through `None` (the pyright rail's finding). Card body re-read and re-pointed: Purpose gained the task-context entry and the three extractions; Logic's `compose_review`, pane, staleness/submission and limits paragraphs were rewritten and two new paragraphs record the inventory-first order and the declared inventory limits; Conventions now names `_entry_refused`, `_open_dataset_pair`, `_review_matrix`, `_selector_kind_or_absence` and the re-exported `refused`/`submission`/`source_pane`/`evidence_pane`; Invariants gained the no-selector state and the one-responsibility-one-implementation rule. **Citation re-derivation:** every row below was re-derived against this candidate rather than carried as a delta, including ten rows whose anchors had been renamed or moved to the extracted modules (`_entry_refused`, `_submission`→`submission`, `_source_pane`→`source_pane`, `_evidence_pane`→`evidence_pane`, `_subject_states`→`subject_states`, `_assessment_display`, `_observation`, `_location`, `_change_state`, `_refused`→`refused`) and the rows whose prose named them. **Stamp accounting:** the two verification rows still name `702714fc05363cb28eacaf101ba8384475a6aa56`, the last real commit on this line, because nothing in this leaf is committed yet; the claims whose evidence this leaf's own change moved were re-read against the candidate and are recorded here as stamp-class leftovers that only closeout can stamp.
- 2026-09-21T14:30+02:00 — 260921-ICR-L5 curator, **post-sync revision: the reference table keeps L1's file attribution with every range re-derived, and the caveat below is superseded rather than merged.** The sync brought leaf `260921-ICR-L1`'s landed extraction into this candidate, so the resolution, the pair preflight, the namespace read, `ReviewCandidateResolution` and the three `REVIEW_*` constants are now cited where they live (`application/review_candidate_resolution.py`) and the adapter keeps only its delegation and composition; the two call sites this leaf added are cited where they now sit (`list_knowledge_review_entries` `:207-288`, `compose_review` `:386-496`), and every other range into this file was re-measured against the merged 1,126-line module — L1's own last pass measured a 1,113-line module, before this leaf's 13 lines landed. One upstream projection record is **retired rather than kept**: the mechanical `ReviewCandidateResolution` repair bullet, which asserted a currency for `knowledge_review.py:185-205`, a range this card no longer cites because L1 re-read that claim at the construct's new home. The caveat below was written before the sync, when the extraction was absent from this leaf's candidate; it is retained as the record of what was true then and is superseded by this entry. No verification stamp was advanced.
- 2026-09-21T14:05+02:00 — 260921-ICR-L5 curator (uncommitted change set on `ar/260921-icr-l5`, code base `f745e16659c5602252bb185a2ffccc356c2bde26`): **a present-but-unreadable before half is now a named refusal on both routes, and every citation range on this card was re-measured.** The change to the adapter is 13 lines: one import of `unreadable_half_refusal` from the new `application/knowledge_before_half.py`, and two call sites — `compose_review` states the refusal before `missing_dataset_half`, and `list_knowledge_review_entries` states it before `_reviewable_entries` — so the per-subject comparison can no longer raise `apsw.NotADBError` out of the entry route that exists to offer a subject. The two Logic paragraphs above record the fact and the boundary it respects: the readers, the four half-states and the refusal all live in the new module, and what stays here is only *where* in the two routes the answer is stated, which is the seam policy's "keep the adapter a delegator" rule rather than feature logic. **Citation accounting:** the file grew 1,281 → 1,294 lines, which moved every construct below the two call sites, and several pre-existing rows were found **materially stale** at this candidate rather than merely shifted — `resolve_review_candidate` was cited at `:182-227` (that range is `ReviewCandidateResolution`; the function is `:208-259`), `_knowledge_pane`/`_source_pane`/`_evidence_pane` at `:512-648` (they are `:802-938`), `_location` at `:1188-1211` (`:1201-1224`) and `refusal` at `:1233-1236` (`:1252-1266`) — so every row into this file was re-derived from the construct's own extent, not carried. The rows citing `mcp/tests/test_knowledge_review_surface.py` were repointed with it. This is a body change and not a metadata-only refresh. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded; no stamp was advanced or invented and no commit was made.
- 2026-09-21T14:05+02:00 — 260921-ICR-L5 curator, **caveat recorded rather than hidden:** the two `REVIEW_*` half-name constants and the entry/adapter surface this card describes are, on the master line, owned by `application/review_candidate_resolution.py` — leaf `260921-ICR-L1`'s landed extraction, which re-exports every moved name through this adapter. That module does **not** exist in this leaf's candidate: `ar/260921-icr-l5` is based on `f745e166`, while the extraction landed on the source branch afterwards as `702714fc`. This card therefore describes the adapter as it actually is in this leaf's candidate, where `resolve_review_candidate`, `missing_dataset_half` and `review_namespace` are still defined inline; the L1 extraction is explicitly **not** recorded here as this leaf's work. When this leaf's code meets the extracted module, the two call sites this leaf adds belong beside the moved preflight rather than in the adapter — that reconciliation is the orchestrator's and the later leaves' to perform, not curation's. No verification stamp was advanced.
- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, base `f745e16659c5602252bb185a2ffccc356c2bde26`): **reconciled this card against the leaf that repaired the responsibility the intake verification named, and corrected the claim it named plus the claims that depended on it.** The intake verification recorded that this card "confirms no candidate tree, absent-half refusal, assessment-only loader and unmeasured-as-stale" and that it "must be reconciled when this responsibility is repaired"; the repair is this leaf's, so the card now says what the code does. **The false claim was structural**: the card said "the candidate side supplies no root or tree id", with `candidate_code_tree_id` deliberately `None` for a live leaf's uncommitted line and `candidate_code_root` therefore `None` too. That is no longer true — the resolution binds the contract's **recorded base commit** on one side and the **captured add-all candidate tree** on the other, and supplies the worktree as the candidate root with it. Two consequences are recorded with it: a contract that records **no** base commit is now refused by name (`offending_input="baseline"`) rather than half-resolved, and the recheck of the captured target (`require_current_candidate_identity`) runs in `compose_review` immediately before the payload is built, so a capture input that moved during composition is a named refusal carrying both identities. **The resolution itself moved out**: `resolve_review_candidate`, `ReviewCandidateResolution`, `missing_dataset_half`, `review_namespace`, `refusal`, the three `REVIEW_*` path constants and `_leaf_contract` are `application/review_candidate_resolution.py`'s, re-exported here so the ingest CLI's existing import keeps resolving; the docstring, Purpose, Logic, Conventions, Invariants and reference table were all re-read and re-pointed accordingly, and the Invariants bullet that declared "a side with no exact tree is a supported state" was replaced by the bound-endpoints rule. **Citation accounting:** every range this card cites into `knowledge_review.py` was re-derived from the construct's own extent in this candidate (the module went 1281 → 1113 lines when the resolution left), each disposition row that had cited a construct now living in the sibling module was split so the anchor and its real file agree, and the two ranges that had run past the end of the file (`:1188-1211`, `:1221-1227`, `:1233-1236`, `:1256-1281` in the old numbering) are gone rather than widened to nothing. Two rows now also cite the cases this leaf added for the delegated resolution (`mcp/tests/test_knowledge_review_source_endpoints.py:370-428`, `:434-458`). **Stamp accounting:** the `reviewedWorkingCandidate` row names this leaf's candidate; the commit fields are left as the last real verification wrote them, because the change is uncommitted and closeout owns that stamp. **One generated history record was retired in this pass:** the mechanical repair bullet for `ReviewCandidateResolution` (which repointed it to `knowledge_review.py:184-204`) is removed, because this curator re-read that claim against the construct's new home in `review_candidate_resolution.py` and derived the range by hand — leaving the generated record would keep asserting a currency for a range no longer cited. No other history entry was touched.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewCandidateResolution` repointed to mcp/src/agents_remember/application/knowledge_review.py:185-205. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `REVIEW_MATRIX_KINDS`; `AUTHORED_EFFECT_KINDS` repointed to mcp/src/agents_remember/application/knowledge_review.py:143-149; mcp/src/agents_remember/application/knowledge_review.py:154-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` repointed to mcp/src/agents_remember/application/knowledge_review.py:163-176; mcp/src/agents_remember/application/knowledge_review.py:181-181. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `read_knowledge_review` repointed to mcp/src/agents_remember/application/knowledge_review.py:333-361. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): the adapter gained the surface's **entry half** and the two connections that make a live leaf's candidate pair actually exist. This card now records: (1) `list_knowledge_review_entries` and its helpers — the subjects the resolved pair can be compared on, resolved through the *identical* operation the comparison uses, offered only when the shipped `diff_knowledge_scope` answered for that identity, and **dropped** rather than listed with a zero when it refused; (2) the two **published** directory constants `REVIEW_BASELINE_DIRECTORY`/`REVIEW_CANDIDATE_DIRECTORY`, exported because the ingest CLI derives the candidate directory it authors into from the same names, which is what makes "the candidate the leaf authored" and "the candidate the review resolved" one directory instead of two conventions; (3) `missing_dataset_half`, the pair preflight that turns an absent half into the existing `candidate_dataset_absent` refusal **naming which half** is missing, where before an absent baseline raised `CantOpenError` from inside side construction; (4) `review_namespace`, which reads the namespace from the candidate's own sealed **receipt**, because the dataset is bound to a namespace id and a side opened under the requested repository spelling refuses against its own binding — measured in the leaf's fixture as `bound to 40d350a6-…, not to the requested repository namespace agents-remember`, a failure every live review of a real candidate would have hit; and (5) that the candidate side now resolves to both a code root and a tree id **or to neither**, since a live leaf's uncommitted line has no tree id and supplying the root anyway made every comparison raise instead of reporting the source expansion it could not make. The `reviewedWorkingCandidate` row was repointed at this leaf's candidate; no verification stamp was advanced, because no commit contains this body.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **re-read this claim against the construct its mechanically projected range now covers, and retired that projection record after the read.** The claim is **"The published adapter surface: the three entry points, the two dataclasses, the three published constants and the re-exported request model."** against `__all__` at `mcp/src/agents_remember/application/knowledge_review.py:110-124`: the anchor resolves at line 110 and the range holds the whole list, which now names `list_knowledge_review_entries` beside `read_knowledge_review` and `review_request_from_query`, `ReviewCandidateResolution` and `ReviewRecordInputs`, `REVIEW_BASELINE_DIRECTORY` and `REVIEW_CANDIDATE_DIRECTORY` beside `REVIEW_CANDIDATE_RELATIVE_ROOT`, plus `ReviewSurfaceRequest` and `REVIEW_MATRIX_KINDS` — three entry points, two dataclasses, three constants, one re-exported request model, so the wording holds unchanged. The generated repair bullet for this range was **retired** because that projection resolves an exact NAME rather than the claim's subject, so leaving it would keep asserting a currency it cannot support. No other bullet or row was deleted and no verification stamp was advanced.
- 2026-09-20T01:25+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared the last two citation rows of this card — two dead anchors and one reopened claim, which are the same row.** The stale-rule row named two cases that exist nowhere in the tree; the source records that they are one case now — `test_the_stale_rule_holds_in_both_directions` (569) states in its own docstring "One rule, two directions, and they were two cases until they were merged", and both behaviours the Finding names (the stale state keeping its previous reference with submission disabled, and a payload claiming a current comparison while disabling submission being unconstructible) are asserted in that one case. The Anchor cell therefore names that surviving case, and both cited ranges were retained unchanged because each already holds it: `:569-590` is the merged case's own declaration span and `:569-598` the wider range the row carried. The Finding text is unchanged, the row is not deleted and no citation was dropped. Because the row's evidence changed after verification and the claim is now current against this candidate, the claim was re-read and **retained as written**: the two behaviours are still exactly what it describes. **Stamp accounting:** the stale `lastVerifiedCommitHash`/`lastVerifiedCommitDate` rows (and the L22-era `reviewedWorkingCandidate` row beside them) were replaced by ONE `reviewedWorkingCandidate` row naming this candidate, because no commit contains the body as it now stands and no stamp was measured on it. No other range, anchor or claim wording was changed anywhere in this document.
- 2026-09-20T00:55+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): hand-read the two enforced rows this card carried. One is cleared (`test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`): its second range `750-771` was replaced with the exact extent of `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one` (`745-764`), which the claim's second half names. The other is LEFT and reported: `test_a_stale_comparison_keeps_the_previous_input_and_disables_submission` and `test_a_current_comparison_cannot_be_built_with_submission_disabled_for_staleness` exist nowhere in the tree — the docstring of `test_the_stale_rule_holds_in_both_directions` (`569-590`) records that the two cases were merged into it, and both behaviours the claim names are still asserted there, so the source is not wrong but the claim's two anchors are. Only a curator re-reading the claim can re-point it at the merged case, so the row is untouched. No other range in either row was touched, no claim was re-worded, no anchor or range was dropped to silence a finding, and no verification stamp was advanced. No commits.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 1 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:38+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): **re-read each claim below against the construct its range now covers, corrected the wording where the construct had moved, re-derived every range from the construct's real extent in the file the claim cites, and only then left the card's stamp to closeout.** No `Generated citation repair` bullet is written: these are curator edits, not a mechanical projection. `knowledge_review.py.md:208` — re-read: the two cases the claim names were merged into one, and its own docstring says so ('One rule, two directions, and they were two cases until they were merged'). The rule is unchanged, so the claim's SUBJECT survives; only the anchor and range are wrong.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `knowledge_review.py.md:207` (`test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`, `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one`).
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's application adapter. It records the four things a reader of this route needs: the adapter **selects nothing** and composes only R08's `diff_knowledge_scope` and L20's `read_knowledge_view(review_matrix)`; the composition sits at the application tier because `layers.toml` ranks `serving` below `application`, so the HTTP shim reaches it through a port the composition root wires; the candidate is resolved from canonical task context and never from a caller-supplied path; and every absence is a named state or a typed refusal rather than a favourable default. It also records the two published facts the panes are built on — the five remaining counts, where an unmeasurable quantity states its reason instead of reporting a zero, and the stale/submission coupling the payload model enforces structurally. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.