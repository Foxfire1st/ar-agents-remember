# mcp/src/agents_remember/application/review_task_context.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_task_context.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T21:45:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l14`, uncommitted; production line `d80a0513e928ef29a973527d09597c82c96fde87` |
| lastVerifiedCommitHash | `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` |
| lastVerifiedCommitDate | 2026-09-22T00:48:09+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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
- **The source half is the whole point.** The inventory arrives already measured from the pair the
  resolution bound — `compose_review` measures it before it decides which composition to run — and the
  pane renders it whether it is complete, partial or unavailable: the three states the model keeps
  apart.
- **Nothing here selects, ranks or concludes.** The records the caller supplied are rendered by
  `application/review_record_rendering.py`, the same renderer the subject review uses, so an
  unassessed assessment collection reads identically in both.
- **A collection it never read is reported `not_selected`, not absent.** Since `ICR-R14@v1` the
  composition states the availability of the two matrix-owned collections from its own honest
  position: it read no review matrix, so `authored_effects` is `not_selected` with a next action
  rather than omitted or reported as an owner's empty answer. "The review did not ask" and "the owner
  holds none" are different facts, and this is the one place the difference is decided.

**A knowledge half that is present but cannot be read is *stated*, not raised — and that is the
merged candidate's third state.** The pair's own preflight (`unreadable_half_refusal`, from
`application/knowledge_before_half.py`) reached this composition when leaf `260921-ICR-L5`'s landed
work met this leaf's rewrite: a damaged half is a fact about the knowledge half, and this review reads
no dataset, so refusing would trade the whole source review away for a knowledge state it never reads
— which is the failure this entry exists to remove. The state reaches the caller twice: as the pane's
own reason (a third branch of `task_context_detail`) and as a declared limitation
(`limitation:knowledge_half_unreadable`, through `unreadable_half_limitations`).

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
`_task_context_pane` builds pane 1; `source_pane(None, inventory)` builds pane 2 with the inventory as
its first required field and every attribution count stated as *not measured* with its own reason;
`evidence_pane((), records, subjects)` builds pane 3 from the caller's records with **no** matrix rows,
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

**The limitations list is the third place the absence is stated, and it is stated in the vocabulary's
own words.** `limitation:no_knowledge_subject_selected` leads, followed by
`inventory_limitations(inventory)`, so an unavailable or partial inventory is declared at the top
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

`__all__` publishes exactly one name, `task_context_review`, because one composition is the module's
whole surface; `unreadable_half_limitations` is public and called by that composition (the merge that
brought L5's unreadable-half fact into this module added it here rather than in the pair's own module,
because the *declaration* is this response's), and `_task_context_pane` and `task_context_detail` are
public-in-file helpers whose leading underscore marks the two the composition itself calls. Every value it returns is a shipped type from
`models/knowledge/review.py`; the module declares no model, imports no store and opens nothing. It
reaches the resolution, the record renderer and the source inventory through their public functions
only, and it writes nothing.

### Invariants And Boundaries

- **No subject is selected, and no comparison is faked.** `comparison` is `None`, `staleness.state` is
  `not_compared`, and the knowledge pane's `selection_state` is `task_context` with a reason — three
  spellings of one fact that `KnowledgeReviewPayload`'s validators hold in agreement.
- **No dataset is opened and no matrix is read.** This composition never touches storage, so an absent
  or unreadable knowledge half cannot refuse a task-context review; the refusal still exists on the
  **subject** path, where a named subject that cannot be compared is a different fact.
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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: this module's own docstring and three
functions, the models that hold the three spellings of "nothing was compared", the two modules it
composes with, the adapter that decides when to call it, and the cases that measure it through the
real route. Three details a reader should carry: the composition is reached only when
`ReviewSurfaceRequest.selector` is `None`; the inventory it renders is measured by
`review_source_inventory` **before** the adapter branches, so this module never measures anything; and
an absent dataset half changes the *reason* it states, never its ability to answer.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what a task-context review asks, the three things it does not do, and why it is a different composition rather than a degraded one. | `not_compared`; `task_context` | mcp/src/agents_remember/application/review_task_context.py:1-22 |
| The module's one published name. | `__all__` | mcp/src/agents_remember/application/review_task_context.py:61-61 |
| **The pair preflight this composition consults and never raises for: a half that is present and cannot be read is a named state, and the declaration it earns is this response's own.** | `unreadable_half_refusal`; `unreadable_half_limitations` | mcp/src/agents_remember/application/knowledge_before_half.py:347-377; mcp/src/agents_remember/application/review_task_context.py:121-128 |
| **The composition: the candidate re-derived immediately before the payload, the selection channels added first, the pair's unreadable-half answer read and stated, the carried reference, `comparison=None`, the three panes, the `not_compared` staleness statement and the three declared limitations.** | `task_context_review`; `with_selection_channels`; `candidate_ref`; `require_current_candidate_identity`; `unreadable_half_refusal`; `unreadable_half_limitations`; `source_pane`; `evidence_pane`; `submission` | mcp/src/agents_remember/application/review_task_context.py:64-118; mcp/src/agents_remember/application/review_candidate_resolution.py:202-218; mcp/src/agents_remember/application/review_candidate_resolution.py:221-250; mcp/src/agents_remember/application/review_source_inventory.py:540-580; mcp/src/agents_remember/application/review_record_rendering.py:152-176; mcp/src/agents_remember/application/review_record_rendering.py:122-149 |
| **The selection-channel call that makes "this review did not ask" a stated fact rather than an empty collection, and the function that states both compositions' positions from one vocabulary.** | `with_selection_channels`; `_not_selected` | mcp/src/agents_remember/application/review_evidence_records.py:217-238; mcp/src/agents_remember/application/review_evidence_records.py:704-717 |
| **Pane 1 for a review that compared nothing: two `unresolved` sides rather than two empty ones, the caller's records rendered as the subject path renders them, and the two selection-state fields.** | `_task_context_pane`; `ReviewSideContent`; `ReviewKnowledgePane` | mcp/src/agents_remember/application/review_task_context.py:131-154; mcp/src/agents_remember/models/knowledge/review.py:136-163; mcp/src/agents_remember/models/knowledge/review.py:447-503 |
| **The reason the payload states, in its three ordered states — an unreadable half, an absent half, and a pair that was simply not selected over — and the sentence that says the inventory does not depend on knowledge availability.** | `task_context_detail`; `missing_dataset_half`; `unreadable_half_refusal` | mcp/src/agents_remember/application/review_task_context.py:157-188; mcp/src/agents_remember/application/knowledge_before_half.py:347-377; mcp/src/agents_remember/application/review_candidate_resolution.py:279-297 |
| **The validators that hold the three spellings of "nothing was compared" in agreement, so the composition cannot publish a payload that disagrees with itself.** | `_require_the_identity_and_staleness_to_agree`; `_require_the_selection_state_to_state_itself`; `KnowledgeReviewPayload`; `ReviewStaleness` | mcp/src/agents_remember/models/knowledge/review.py:726-789; mcp/src/agents_remember/models/knowledge/review.py:447-503; mcp/src/agents_remember/models/knowledge/review.py:681-708 |
| **The branch that reaches this composition: the inventory measured first and unconditionally, then the selector branch.** | `compose_review`; `review_inventory` | mcp/src/agents_remember/application/knowledge_review.py:371-453; mcp/src/agents_remember/application/review_source_inventory.py:428-454 |
| The boundary that produces a selector-less request at all: the transport admitting "both parameters omitted" as the task context. | `review_request_from_query` | mcp/src/agents_remember/serving/review.py:83-122 |
| The browser entry that offers the task-context target for every live leaf. | `useReviewSubject`; `DocChangeSetBar` | dashboard/src/panels/detail-panel/changeSetBar.tsx:71-97; dashboard/src/panels/detail-panel/changeSetBar.tsx:98-170 |
| **The case that measures this composition through the real route: neither dataset half present, the payload's three states, the inventory equal to an independent Git observation, and the real HTTP route answering 200 with no selector parameters.** | `test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all`; `build_endpoint_fixture`; `task_request` | mcp/tests/test_knowledge_review_source_endpoints.py:733-810; mcp/tests/test_knowledge_review_source_endpoints.py:198-231; mcp/tests/test_knowledge_review_source_endpoints.py:132-146 |
| **The case that measures the selection channel itself: the same fixture read through the task-context entry reports the matrix-owned collection `not_selected` while the candidate-owned collections stay supplied.** | `test_a_task_context_review_reports_the_matrix_collection_as_not_selected` | mcp/tests/test_knowledge_review_evidence_channels.py:655-677 |
| The dashboard case that measures the same entry from the browser side: the server offers no subject and the target is still `review: {}`. | `stubCounters` | dashboard/src/panels/detail-panel/test-utils.tsx:428-457; dashboard/src/panels/detail-panel/changeSetBar.test.tsx:170-195 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It composes values from one candidate's
resolution, inventory and supplied records and carries no identity that ranges beyond the repository
namespace the request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T21:45:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **this composition now states the availability of the collections it never read, so the card's "`authored_effects` and `evidence_links` are empty here" needed the reason beside it.** `ICR-R14@v1` added one call — `with_selection_channels(records, (), selected=False)` — placed **before** the subject states are projected, and it reports the two matrix-owned collections `not_selected` with no count and a next action: a review that read no matrix did not ask, and "did not ask" is a different fact from an owner answering that it holds none. The Purpose gained the paragraph that states the distinction, the Logic gained the call and where it sits relative to the payload, and the invariant that used to leave the emptiness unexplained now says *why* it is empty and notes that the candidate-owned collections (claims included) arrive independently of any selection — with their links simply unselected. **Citation accounting:** every range into this 188-line file was re-derived at its own declaration extent (`__all__` `61`, `task_context_review` `64-118`, `unreadable_half_limitations` `121-128`, `_task_context_pane` `131-154`, `task_context_detail` `157-188`), and the `models/knowledge/review.py` references moved with that file (836→851): `ReviewSideContent` `128-153`→`136-163`, `ReviewKnowledgePane` `439-488`→`447-503`, `ReviewStaleness` `666-691`→`681-708`, `KnowledgeReviewPayload` `711-772`→`726-789`; the R01 enclosure case moved to `733-810` and `build_endpoint_fixture` to `198-231`; and the two rendering rows were repointed to their constructs' new extents. One row was **added** for the selection-channel call and the `_not_selected` builder it reaches, and one for the case that measures it through the task-context entry; nothing was dropped. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` now name the **production line this reading was against** — `d80a0513e928ef29a973527d09597c82c96fde87`, the master line's current tip and this leaf's base — replacing the previous pair rather than leaving a stamp no reading in this pass measured; the candidate is uncommitted, so no commit contains the content a stamp would claim to have verified, and the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates.
- 2026-09-21T16:10+02:00 — orchestrating session, pre-closeout metadata repair on `ar/260921-icr-l2`: the governed closeout refused the memory leg because this card for a module that exists only in this leaf's uncommitted candidate carried no verification stamp in its header metadata (`external-memory closeout requires onboarding verification metadata before memory commit`). The two fields were added naming the **production line this card was read against** — `c755cec6…`, the master line after this leaf's resolved syncs brought in the ICR-L5 and ICR-L19 landings, at that closeout's recorded time `2026-09-21T15:29:12+02:00` — and the candidate row was left as it was. This states what the reading was against, not that the module exists in that commit; the closeout's own metadata refresh re-stamps the card against the code commit this transaction creates. No range, claim or anchor was changed by this repair.
- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **the sync brought leaf `260921-ICR-L5`'s unreadable-half fact into this composition, and the card now records it.** The code-side resolution kept L5's refusal *inside* this module rather than beside it: `unreadable_half_refusal` is imported from `application/knowledge_before_half.py`, `task_context_review` reads it from the resolved pair's two databases, threads it into the pane and states it as `limitation:knowledge_half_unreadable` through the new `unreadable_half_limitations`; and `task_context_detail` gained a **third ordered state** (an unreadable half, then an absent half, then a pair simply not selected over). The card's Purpose, Logic, Conventions and Invariants were extended with that state — the claim that this composition has two states was **corrected, not merged**, because a second wording would have described a module that no longer exists — and every range was re-derived against the merged 184-line file (`__all__` `58`, the composition `61-114`, `unreadable_half_limitations` `117-124`, the pane `127-150`, the detail `153-184`). The module-statement row and the preflight row were added for the same reason. No verification stamp is carried by this card and none was invented: every construct it cites exists only in this candidate and the governed closeout owns the stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): created this one-to-one card for the module this leaf introduced as the review surface's **task-context entry**. The card records why the composition exists rather than only what it returns: a review of a task asks a different question from a review of a subject, and the surface used to require a subject, so a task with no recorded invariant — or with no datasets yet — lost its source review entirely. It records the three spellings of "nothing was compared" that the payload's validators hold in agreement (`comparison=None`, `staleness.state="not_compared"`, `knowledge.selection_state="task_context"` with its reason), the fact that the inventory is measured by `review_source_inventory` **before** the adapter branches so this module measures nothing, the candidate recheck it shares with the subject composition (a moved capture input is a named refusal in both), and the one thing an absent dataset half changes here — the reason the payload states, never whether it can answer. **Stamp accounting:** this card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**, because every construct it cites exists only in this leaf's uncommitted candidate and no real commit contains the content a stamp would claim to have verified; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the real stamp once the code commit exists.