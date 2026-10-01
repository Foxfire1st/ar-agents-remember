# mcp/src/agents_remember/application/review_task_context.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The **task-context review**: the source entry that needs no selected subject. A review of a *task*
asks a different question from a review of a subject — the subject review asks "what changed about
this recorded invariant", this one asks "what did this task change at all" — and its answer is the
complete source inventory of the two bound code trees plus every collected fact that does not depend
on a selection.

It exists as its own module because it is a **different composition, not a degraded one**:

- **No comparison is made, and none is faked.** No selector is resolved, no dataset is opened for
  selection and no review-matrix row is read, so a task whose knowledge half does not exist yet still
  has an openable review. The payload says so in the vocabulary's own words rather than by rendering
  an empty statement: `comparison=None`, `staleness.state="not_compared"` (there is no comparison
  binding that could be current or stale), and a knowledge pane whose `selection_state` is
  `task_context` with its reason.
- **The source half is the whole point, and the attribution is measured here.** The inventory arrives
  already measured from the pair the resolution bound — `compose_review` measures the observation
  before it decides which composition to run — and `pair_attribution` partitions that same observation
  from the pair's own two datasets, because a task review compares no dataset and therefore has no
  comparison to inherit one from. A readable half's registered mappings attribute their paths even
  when the other half is absent or unreadable, and the changes it did not attribute stay
  *undetermined* rather than becoming confirmed unregistered. The pane renders inventory and
  partition whether complete, partial, unavailable or undetermined: the states the models keep
  apart.
- **Nothing here selects, ranks or concludes.** The records the caller supplied are rendered by
  `application/review_record_rendering.py`, the same renderer the subject review uses, so an
  unassessed assessment collection reads identically in both.
- **A collection it never read is reported `not_selected`, not absent.** Since `ICR-R14@v1` the
  composition states the availability of the two matrix-owned collections from its own honest
  position: it read no review matrix, so `authored_effects` is `not_selected` with a next action
  rather than omitted or reported as an owner's empty answer. "The review did not ask" and "the owner
  holds none" are different facts, and this is the one place the difference is decided.

**A knowledge half that is present but cannot be read is *stated*, not raised — and a candidate
receipt that exists and does not validate is stated three times.** The pair's own preflight
(`unreadable_half_refusal`, from `application/knowledge_before_half.py`) reached this composition
when leaf `260921-ICR-L5`'s landed work met this leaf's rewrite; this leaf adds the receipt question
(`candidate_receipt_refusal`, from the shared refusal owner in
`application/review_candidate_resolution.py`), asked once before the pair read and once more after
it — so a record that read as valid at the preflight and broke before the sides were bound reaches
the pane and the declared limitations instead of stopping at the partition's side entries, and a
second read of the same bytes is still guarded, so a receipt that moves between the two reads is a
stated state rather than an escaping error. A damaged or unreadable half is a fact about the
knowledge half, and this review reads no dataset for selection, so refusing would trade the whole
source review away for a knowledge state it never selects from — which is the failure this entry
exists to remove. The state reaches the caller in three places: as the pane's own reason (a third
branch of `task_context_detail`, now carrying the actionable instruction too) and as declared
limitations (`limitation:knowledge_half_unreadable`, through `unreadable_half_limitations`, plus the
partition's own `attribution_limitations`).

**Why this is the entry R02 required.** The surface used to require a subject, so a task that records
no invariant — or whose datasets do not exist yet — lost its source review entirely, which is exactly
the non-conforming example the packet names. Making the task context answerable is what turns the
review from "a review of a selected subject" into "a review of the task, refined by a subject".

## Code Commentary

### Logic

**`task_context_review` re-derives the captured candidate immediately before it builds the payload,
then composes three values and one statement.** The recheck is `require_current_candidate_identity`,
called at the same moment the subject composition calls it (after the reads, immediately before
publication), so a capture input that moved while the inventory was being measured is a named refusal
rather than an inventory attributed to a candidate the leaf no longer holds. It is deliberately the
**same** operation, not a second copy: a task-context review and a subject review must not disagree
about when a candidate stopped being current.

**`unreadable_half_limitations` is the one new public function, and it exists because a limit a
reader has to open a pane to discover is a limit the response did not state.** It returns
`("limitation:knowledge_half_unreadable",)` when the pair's preflight reported an unreadable half and
the empty tuple otherwise, and `task_context_review` splices it between
`limitation:no_knowledge_subject_selected` and `inventory_limitations(inventory)` — so one response
declares all three facts about itself in the vocabulary the rest of the surface uses.

**The payload it returns is one composition of values that are all already owned elsewhere.**
`candidate_ref` (from `review_candidate_resolution`) names the reviewed candidate from the
resolution's own leaf id; `comparison=None` states that no knowledge operand was compared;
`_task_context_pane` builds pane 1; `source_pane(None, inventory, attribution)` builds pane 2 with
the inventory as its first required field and the pair's own measured partition beside it — never a
recomputed one, because this route has no comparison to inherit from; `evidence_pane((), records,
subjects)` builds pane 3 from the caller's records with **no** matrix rows,
because this composition reads no matrix it cannot select for; and the staleness value is
`not_compared` with a statement that says the Source pane carries the complete inventory of the bound
pair. `submission` is `submission(stale=False)` — nothing about a task-context review is stale, because
nothing was compared.

**The one added call is `with_selection_channels(records, (), selected=False)`, and it exists because a
review that did not ask may not report an owner's absence.** It runs first, before the subject states
are projected, and adds the two matrix-owned collections' availability to the bundle: with no matrix
read they are `not_selected`, with no count and a next action, instead of appearing as empty
collections the composition never asked about. The same call in the subject composition passes the rows
the view returned, so one function states both compositions' positions from the same vocabulary.

**The limitations list is where every absence is stated, in the vocabulary's own words.**
`limitation:no_knowledge_subject_selected` leads, followed by the unreadable-half declaration,
`attribution_limitations(attribution)` and `inventory_limitations(inventory)`, so an unavailable or
partial inventory and an undetermined attribution are declared at the top
level of the same response rather than only inside the pane.

**`_task_context_pane` renders pane 1 with two `unresolved` sides rather than two empty ones.** An
empty statement is a statement *about a snapshot*, and this pane made none: each side carries
`state="unresolved"` with the detail `task_context_detail` returns. The signals and assessment
displays the caller supplied are rendered exactly as the subject path renders them — which assessment
belongs to which subject is the applicability projection's own contract, and this composition grows no
second rule for it.

**`task_context_detail` names which dataset half answers for the absence, in the order that decides
it.** Three states: a half whose bytes are there and **cannot be read** (the pair's preflight, stated
here because this review raises nothing for it — the refusal's own `detail` is quoted rather than
summarised); a half that is **absent** (named with the database's own name, "the resolved candidate
dataset is absent (`<name>`)"); and a pair that is present and simply **was not selected over**. All
three still point at the Source pane, because the inventory **does not depend on knowledge
availability** — absent or damaged knowledge is a fact this review states, not a reason it cannot be
opened. The last state is deliberately not a degraded first: it is what a review of the task alone is.

### Conventions

`__all__` publishes two names, `task_context_review` and `pair_attribution`, because the pair
measurement is the route's own and another composition must not re-derive it; `unreadable_half_limitations` is public and called by that composition (the merge that
brought L5's unreadable-half fact into this module added it here rather than in the pair's own module,
because the *declaration* is this response's), and `_task_context_pane` and `task_context_detail` are
public-in-file helpers whose leading underscore marks the two the composition itself calls. Every value it returns is a shipped type from
`models/knowledge/review.py`; the module declares no model and imports no store. It opens each
knowledge half read-only when it is there (`_pair_side`, one dataset-identity read plus one SELECT
per measured path per readable half) and carries an unreadable one as an unavailable side — the one
extra read cost this route pays for its own attribution, with no latency claim made or measured.
It reaches the resolution, the record renderer and the source inventory through their public functions
only, and it writes nothing.

### Invariants And Boundaries

- **No subject is selected, and no comparison is faked.** `comparison` is `None`, `staleness.state` is
  `not_compared`, and the knowledge pane's `selection_state` is `task_context` with a reason — three
  spellings of one fact that `KnowledgeReviewPayload`'s validators hold in agreement.
- **No dataset is opened for selection and no matrix is read.** This composition never selects,
  so an absent or unreadable knowledge half cannot refuse a task-context review; the refusal still
  exists on the **subject** path, where a named subject that cannot be compared is a different fact.
  Each half is opened **read-only** when it is there for the attribution measurement alone
  (`_pair_side`), and a half that is not becomes an unavailable side — no negative conclusion is
  drawn from its silence.
- **An unreadable knowledge half is stated, never raised.** `unreadable_half_refusal` is consulted,
  and its answer becomes the pane's reason and a declared limitation; this composition refuses nothing
  on the knowledge half's account, because it reads no dataset and refusing would remove the source
  review with it.
- **The inventory is present in all three of its states.** Complete, partial or unavailable, the Source
  pane carries it and the response declares its limit at the top level.
- **The candidate is re-checked immediately before publication**, by the same operation the subject
  composition calls, so a capture input that moved is a named refusal in both.
- **The records are the caller's and are rendered, not selected.** The task-context composition reads
  no review matrix, so `authored_effects` and `evidence_links` are empty here — and since
  `ICR-R14@v1` the matrix-owned collection says *why* it is empty (`not_selected`, no count, a next
  action) instead of leaving the reader to guess between "not read" and "read and empty". The
  caller's observations, signals, claims and assessments still render, because those collections do
  not depend on a selection at all: the claims collection is the candidate's own and arrives with its
  links unselected, not unsupplied.
- **The selection channels are added before the subject states are projected**, so the payload the
  validators check and the payload the channels describe are built from the same bundle.
- **Rank.** The composition lives at the application tier beside the adapter that calls it, because
  `serving` may not import these operations and the HTTP shim does transport only.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: this module's own docstring and three
functions, the models that hold the three spellings of "nothing was compared", the two modules it
composes with, the adapter that decides when to call it, and the cases that measure it through the
real route. Three details a reader should carry: the composition is reached only when
`ReviewSurfaceRequest.selector` is `None`; the inventory it renders is measured by
`review_source_inventory` **before** the adapter branches, while the attribution it renders is
measured here from the pair's own halves (`pair_attribution`); and
an absent dataset half changes the *reason* it states, never its ability to answer.

- The module's own statement of what a task-context review asks, the three things it does not do, and why it is a different composition rather than a degraded one. [1]
- The module's two published names: the composition and its pair measurement. [2]
- **The pair preflight this composition consults and never raises for: a half that is present and cannot be read is a named state, the receipt question asked twice, and the declaration each earns is this response's own.** [3]
- **The composition: the candidate re-derived immediately before the payload, the selection channels added first, the receipt asked before and after the pair read, the carried reference, `comparison=None`, the three panes, the `not_compared` staleness statement and the five declared limitations.** [4]
- **The selection-channel call that makes "this review did not ask" a stated fact rather than an empty collection, and the function that states both compositions' positions from one vocabulary.** [5]
- **The pair's own attribution: each half opened read-only when it is there, a side that cannot be bound carried as unavailable, and only the side that cannot be bound marked so.** [6]
- **Pane 1 for a review that compared nothing: two `unresolved` sides rather than two empty ones, the caller's records rendered as the subject path renders them, and the two selection-state fields.** [7]
- **The reason the payload states, in its three ordered states — an unreadable half, an absent half, and a pair that was simply not selected over — and the sentence that says the inventory does not depend on knowledge availability, with the next action to act on it.** [8]
- **The validators that hold the three spellings of "nothing was compared" in agreement, so the composition cannot publish a payload that disagrees with itself.** [9]
- **The branch that reaches this composition: the observation made once, the inventory rendered from it, then the selector branch.** [10]
- The boundary that produces a selector-less request at all: the transport admitting "both parameters omitted" as the task context. [11]
- The browser entry that offers the task-context target for every live leaf. [12]
- **The case that measures this composition through the real route: neither dataset half present, the payload's three states, the inventory equal to an independent Git observation, and the real HTTP route answering 200 with no selector parameters.** [13]
- **The case that measures the selection channel itself: the same fixture read through the task-context entry reports the matrix-owned collection `not_selected` while the candidate-owned collections stay supplied.** [14]
- The dashboard case that measures the same entry from the browser side: the server offers no subject and the target is still `review: {}`. [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It composes values from one candidate's
resolution, inventory and supplied records and carries no identity that ranges beyond the repository
namespace the request names.

No meaningful cross-repo references found.

## 260921-ICR-L10 The Task-Context Composition Calls The Extracted Branch

`260921-ICR-L10` (`ICR-R10@v1`) leaves this composition's behavior unchanged and moves one
construction out of it: the selection channels' "no matrix was read" branch is now
`without_selected_matrix` in `review_evidence_records.py`, called here, so there is one implementation
of that statement rather than two. A paged request that names no subject is still answered as the task
context with neither a page nor a page refusal, because that review compares no operand and reads no
matrix at all — there is no bounded collection to page.

## 260921-ICR-L26 A Review That Selected No Subject Labels Every Record As The Candidate's

`260921-ICR-L26` (`ICR-R26@v1`) gives the task-context composition the same attribution vocabulary,
with the one label that is true when nothing was compared: `task_context_applicability(records)` labels
**every** supplied record `candidate` — the candidate's own input, with its recorded subject beside it —
and the pane gained the labelled collections and the six-way counts. **376 → 390 lines.**

**Why `candidate` and not `unresolved`.** There is no selected subject and no comparison generation, so
a record that names a subject is not naming *the* subject, and reporting its binding unresolved would
claim a question was asked and could not be answered. `candidate` is the label that neither claims the
record applies to a subject nor reports a failure that did not happen; `task_context_applicability`'s
own docstring states it, and the summary counts make the whole supplied population visible beside a
pane that displays none of the two matrix-owned collections.

**The two panes still render one population.** `_task_context_pane` filters its signals and its
assessment displays through the projection exactly as the subject composition does — the projection is
the same `ReviewApplicabilityProjection` port — and it carries `context` and `applicability` onto the
pane, which is empty for a task context because no selection reaches any other identity.

## 260921-ICR-L12 A Reopened Review States Its Record's Own Intent Absence

`260921-ICR-L12` (`ICR-R12@v1`) gives the task-context composition the vocabulary a **reopened**
review needs, in two places:

- `task_context_review` adds `closed_leaf_limitations(resolved)` to the limitations it states, so the
  response says which record answered, which generation it was and what that record holds about each
  intent half. A live candidate contributes no token and this composition's live behaviour is
  unchanged.
- `task_context_detail` now answers a reopened review **first**, through
  `closed_leaf_intent_detail(resolved)`, before its three live states. The reason is the one fact this
  leaf exists to keep straight: an intent generation the leaf never recorded is a typed absence about
  the repository's history, and one that was recorded and no longer resolves is unavailable content.
  Reported as each other, either sentence is false — the first would read as content that was expected
  and lost, the second as an absence that was never anyone's failure. The sentence the owner produces
  decides which leads, and the composition only carries it.

The composition still measures nothing about knowledge itself: the two extra calls are pure reads of a
value the resolution already carries, and the live path through this module is byte-identical.

## 260921-ICR-L31 A Review That Selected No Subject States Its Family Absence In The One Vocabulary

**This entry now answers the family question with the one state that claims nothing
(`ICR-R31@v1`).** The payload's ``family_context`` field is required, so a task-context review — which
composes no comparison and selects no subject — supplies a stated context whose state is
``no_subject_selected`` and whose sentence says that no recorded family, guarantee or member roster was
resolved, and that the Source pane carries the complete inventory of the bound source pair
independently of any family membership. The distinction the state keeps is the point: the recorded
families of a subject nobody named are not an unread scope, not an unavailable one and not a measured
zero, and collapsing them into ``no_family_recorded`` would report a measurement this entry never took.

**What did not change:** the candidate re-derivation and its receipt, the selection channels, the
three panes, the ``not_compared`` staleness statement and the five declared limitations are exactly as
they were. The new field is the only addition, and it is additive to the payload rather than a change
to what this entry reads.

**Citation accounting:** one row was re-anchored to the ``submission`` call site this row describes
(the composition's own tail, not the import of the same name) after this leaf's additions moved it. No
claim cell was re-worded and no stamp was advanced beyond the honest basis below.
