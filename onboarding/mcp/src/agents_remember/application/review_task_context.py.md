# mcp/src/agents_remember/application/review_task_context.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_task_context.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T02:40+02:00 |
| lastVerifiedCommitHash | `870701b43039cd205a8c98e418382729510c3de3` |
| lastVerifiedCommitDate | 2026-09-23T03:12:21+02:00|
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
`review_source_inventory` **before** the adapter branches, while the attribution it renders is
measured here from the pair's own halves (`pair_attribution`); and
an absent dataset half changes the *reason* it states, never its ability to answer.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what a task-context review asks, the three things it does not do, and why it is a different composition rather than a degraded one. | `not_compared`; `task_context` | mcp/src/agents_remember/application/review_task_context.py:1-23 |
| The module's two published names: the composition and its pair measurement. | `__all__` | mcp/src/agents_remember/application/review_task_context.py:81-81 |
| **The pair preflight this composition consults and never raises for: a half that is present and cannot be read is a named state, the receipt question asked twice, and the declaration each earns is this response's own.** | `unreadable_half_refusal`; `unreadable_half_limitations`; `candidate_receipt_refusal` | mcp/src/agents_remember/application/knowledge_before_half.py:347-377; mcp/src/agents_remember/application/review_task_context.py:160-167; mcp/src/agents_remember/application/review_candidate_resolution.py:358-372 |
| **The composition: the candidate re-derived immediately before the payload, the selection channels added first, the receipt asked before and after the pair read, the carried reference, `comparison=None`, the three panes, the `not_compared` staleness statement and the five declared limitations.** | `task_context_review`; `with_selection_channels`; `candidate_ref`; `require_current_candidate_identity`; `unreadable_half_refusal`; `unreadable_half_limitations`; `source_pane`; `evidence_pane`; `submission`; `attribution_limitations` | mcp/src/agents_remember/application/review_task_context.py:84-158; mcp/src/agents_remember/application/review_task_context.py:160-167; mcp/src/agents_remember/application/review_candidate_resolution.py:205-221; mcp/src/agents_remember/application/review_candidate_resolution.py:224-254; mcp/src/agents_remember/application/review_evidence_records.py:256-281; mcp/src/agents_remember/application/review_source_inventory.py:556-619; mcp/src/agents_remember/application/review_record_rendering.py:152-176; mcp/src/agents_remember/application/review_record_rendering.py:122-150; mcp/src/agents_remember/application/review_source_inventory.py:741-763 |
| **The selection-channel call that makes "this review did not ask" a stated fact rather than an empty collection, and the function that states both compositions' positions from one vocabulary.** | `with_selection_channels`; `_not_selected` | mcp/src/agents_remember/application/review_evidence_records.py:257-798; mcp/src/agents_remember/application/review_evidence_records.py:229-229 |
| **The pair's own attribution: each half opened read-only when it is there, a side that cannot be bound carried as unavailable, and only the side that cannot be bound marked so.** | `pair_attribution`; `_pair_without_namespace`; `_side_from_own_bytes`; `_pair_side` | mcp/src/agents_remember/application/review_task_context.py:231-289; mcp/src/agents_remember/application/review_task_context.py:291-320; mcp/src/agents_remember/application/review_task_context.py:322-349; mcp/src/agents_remember/application/review_task_context.py:351-376 |
| **Pane 1 for a review that compared nothing: two `unresolved` sides rather than two empty ones, the caller's records rendered as the subject path renders them, and the two selection-state fields.** | `_task_context_pane`; `ReviewSideContent`; `ReviewKnowledgePane` | mcp/src/agents_remember/application/review_task_context.py:170-193; mcp/src/agents_remember/models/knowledge/review.py:148-174; mcp/src/agents_remember/models/knowledge/review.py:461-516 |
| **The reason the payload states, in its three ordered states — an unreadable half, an absent half, and a pair that was simply not selected over — and the sentence that says the inventory does not depend on knowledge availability, with the next action to act on it.** | `task_context_detail`; `missing_dataset_half`; `unreadable_half_refusal` | mcp/src/agents_remember/application/review_task_context.py:196-228; mcp/src/agents_remember/application/knowledge_before_half.py:347-377; mcp/src/agents_remember/application/review_candidate_resolution.py:282-300 |
| **The validators that hold the three spellings of "nothing was compared" in agreement, so the composition cannot publish a payload that disagrees with itself.** | `_require_the_identity_and_staleness_to_agree`; `_require_the_selection_state_to_state_itself`; `KnowledgeReviewPayload`; `ReviewStaleness` | mcp/src/agents_remember/models/knowledge/review.py:736-1092; mcp/src/agents_remember/models/knowledge/review.py:705-705; mcp/src/agents_remember/models/knowledge/review.py:924-924; mcp/src/agents_remember/models/knowledge/review.py:1040-1040 |
| **The branch that reaches this composition: the observation made once, the inventory rendered from it, then the selector branch.** | `compose_review`; `review_inventory` | mcp/src/agents_remember/application/knowledge_review.py:300-412; mcp/src/agents_remember/application/review_source_inventory.py:429-469 |
| The boundary that produces a selector-less request at all: the transport admitting "both parameters omitted" as the task context. | `review_request_from_query` | mcp/src/agents_remember/serving/review.py:260-260 |
| The browser entry that offers the task-context target for every live leaf. | `useReviewCatalogue`; `DocChangeSetBar` | dashboard/src/panels/detail-panel/changeSetBar.tsx:122-187; dashboard/src/panels/detail-panel/changeSetBar.tsx:360-395 |
| **The case that measures this composition through the real route: neither dataset half present, the payload's three states, the inventory equal to an independent Git observation, and the real HTTP route answering 200 with no selector parameters.** | `test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all`; `build_endpoint_fixture`; `task_request` | mcp/tests/test_knowledge_review_source_endpoints.py:750-826; mcp/tests/test_knowledge_review_source_endpoints.py:215-248; mcp/tests/test_knowledge_review_source_endpoints.py:149-167 |
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
- 2026-09-22T09:20:00+02:00 — 260921-ICR-L4 curator (gate repair pass on the merged line): **validators row re-cited** (`_require_the_identity_and_staleness_to_agree` at `:793-810` beside the payload value). Wording unchanged; no stamp advanced.
- 2026-09-22T09:15:00+02:00 — 260921-ICR-L4 curator (sync-merge resolution of the parked candidate against the landed line, merged base code `d21bc8a6` / memory `75bb4d65`): **additive union with landed `260921-ICR-L14`.** Both sides' history kept newest-first; L14's selection-channel call and rows beside this leaf's pair-attribution measurement, with every range re-derived against the merged 376-line module (`task_context_review` `84-158`, the four pair helpers `231-376`; `models/knowledge/review.py` at its merged 873-line extents). Header names the merged base on this leaf's candidate row. No verification stamp was advanced.
- 2026-09-22T08:30:00+02:00 — 260921-ICR-L4 curator (uncommitted change set on `ar/260921-icr-l4`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the task-context route measures its own pair attribution (184 → 372 lines).** `task_context_review` takes the already-made `observed`, asks the receipt question before and after the pair read, and composes `source_pane(None, inventory, attribution)` with the partition beside the inventory; `pair_attribution` opens each half read-only when it is there and carries an unreadable one as an unavailable side — with the F-V3-1 correction that only the side that cannot be bound is unavailable (the before half binds from the namespace its own bytes disclose, the candidate half carries the refusal); the unreadable state reaches the pane, the top-level limitations and the partition's side entries, and the pane detail carries the next action. New `pair_attribution`, `_pair_without_namespace`, `_side_from_own_bytes`, `_pair_side`; `__all__` is two names. Every reference row was re-derived against this candidate. **Stamp accounting:** old verification rows name the last real commit; this leaf's claims were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T21:45:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **this composition now states the availability of the collections it never read, so the card's "`authored_effects` and `evidence_links` are empty here" needed the reason beside it.** `ICR-R14@v1` added one call — `with_selection_channels(records, (), selected=False)` — placed **before** the subject states are projected, and it reports the two matrix-owned collections `not_selected` with no count and a next action: a review that read no matrix did not ask, and "did not ask" is a different fact from an owner answering that it holds none. The Purpose gained the paragraph that states the distinction, the Logic gained the call and where it sits relative to the payload, and the invariant that used to leave the emptiness unexplained now says *why* it is empty and notes that the candidate-owned collections (claims included) arrive independently of any selection — with their links simply unselected. **Citation accounting:** every range into this 188-line file was re-derived at its own declaration extent (`__all__` `61`, `task_context_review` `64-118`, `unreadable_half_limitations` `121-128`, `_task_context_pane` `131-154`, `task_context_detail` `157-188`), and the `models/knowledge/review.py` references moved with that file (836→851): `ReviewSideContent` `128-153`→`136-163`, `ReviewKnowledgePane` `439-488`→`447-503`, `ReviewStaleness` `666-691`→`681-708`, `KnowledgeReviewPayload` `711-772`→`726-789`; the R01 enclosure case moved to `733-810` and `build_endpoint_fixture` to `198-231`; and the two rendering rows were repointed to their constructs' new extents. One row was **added** for the selection-channel call and the `_not_selected` builder it reaches, and one for the case that measures it through the task-context entry; nothing was dropped. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` now name the **production line this reading was against** — `d80a0513e928ef29a973527d09597c82c96fde87`, the master line's current tip and this leaf's base — replacing the previous pair rather than leaving a stamp no reading in this pass measured; the candidate is uncommitted, so no commit contains the content a stamp would claim to have verified, and the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates.
- 2026-09-21T16:10+02:00 — orchestrating session, pre-closeout metadata repair on `ar/260921-icr-l2`: the governed closeout refused the memory leg because this card for a module that exists only in this leaf's uncommitted candidate carried no verification stamp in its header metadata (`external-memory closeout requires onboarding verification metadata before memory commit`). The two fields were added naming the **production line this card was read against** — `c755cec6…`, the master line after this leaf's resolved syncs brought in the ICR-L5 and ICR-L19 landings, at that closeout's recorded time `2026-09-21T15:29:12+02:00` — and the candidate row was left as it was. This states what the reading was against, not that the module exists in that commit; the closeout's own metadata refresh re-stamps the card against the code commit this transaction creates. No range, claim or anchor was changed by this repair.
- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **the sync brought leaf `260921-ICR-L5`'s unreadable-half fact into this composition, and the card now records it.** The code-side resolution kept L5's refusal *inside* this module rather than beside it: `unreadable_half_refusal` is imported from `application/knowledge_before_half.py`, `task_context_review` reads it from the resolved pair's two databases, threads it into the pane and states it as `limitation:knowledge_half_unreadable` through the new `unreadable_half_limitations`; and `task_context_detail` gained a **third ordered state** (an unreadable half, then an absent half, then a pair simply not selected over). The card's Purpose, Logic, Conventions and Invariants were extended with that state — the claim that this composition has two states was **corrected, not merged**, because a second wording would have described a module that no longer exists — and every range was re-derived against the merged 184-line file (`__all__` `58`, the composition `61-114`, `unreadable_half_limitations` `117-124`, the pane `127-150`, the detail `153-184`). The module-statement row and the preflight row were added for the same reason. No verification stamp is carried by this card and none was invented: every construct it cites exists only in this candidate and the governed closeout owns the stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): created this one-to-one card for the module this leaf introduced as the review surface's **task-context entry**. The card records why the composition exists rather than only what it returns: a review of a task asks a different question from a review of a subject, and the surface used to require a subject, so a task with no recorded invariant — or with no datasets yet — lost its source review entirely. It records the three spellings of "nothing was compared" that the payload's validators hold in agreement (`comparison=None`, `staleness.state="not_compared"`, `knowledge.selection_state="task_context"` with its reason), the fact that the inventory is measured by `review_source_inventory` **before** the adapter branches so this module measures nothing, the candidate recheck it shares with the subject composition (a moved capture input is a named refusal in both), and the one thing an absent dataset half changes here — the reason the payload states, never whether it can answer. **Stamp accounting:** this card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**, because every construct it cites exists only in this leaf's uncommitted candidate and no real commit contains the content a stamp would claim to have verified; what was actually read is this leaf's uncommitted working tree, and closeout owns the real stamp once the code commit exists.

## 260921-ICR-L10 The Task-Context Composition Calls The Extracted Branch

`260921-ICR-L10` (`ICR-R10@v1`) leaves this composition's behavior unchanged and moves one
construction out of it: the selection channels' "no matrix was read" branch is now
`without_selected_matrix` in `review_evidence_records.py`, called here, so there is one implementation
of that statement rather than two. A paged request that names no subject is still answered as the task
context with neither a page nor a page refusal, because that review compares no operand and reads no
matrix at all — there is no bounded collection to page.

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-23T00:30:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; production line at this leaf's base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **the task-context composition calls the extracted `without_selected_matrix`.** No behavior
changed: the construction moved beside `with_selection_channels` so one module owns the statement. The
unnamed-collection boundary is unchanged and stated: a paged request with no subject is the task context,
with neither a page nor a refusal. Rows on this card that cited `review_task_context.py` or
`serving/review.py` by line were re-derived against this candidate. No verification stamp was advanced: nothing in this leaf is committed, so the commit/closeout stamp remains closeout's.
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

## Update History
- 2026-09-23T02:40:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): **the task-context review labels every supplied record as the candidate's own input (376 → 390 lines; `ICR-R26@v1`).** The card records why `candidate` is the true label when nothing was compared, and that the pane consumes the same projection port as the subject composition. **Citation accounting:** this leaf's insertions moved nothing this card cites by an enforced range — the measured baseline check reports **zero** enforced findings for this card — so only the leaf's own section and this entry were added, and no range was rewritten to fit. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header already names this leaf's base, and the governed closeout owns the real stamp.
