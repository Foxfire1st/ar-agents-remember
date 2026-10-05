# mcp/src/agents_remember/models/ - Response Contract Models Overview

## Native identity and requested launch options

role_agents/role_launcher describe native start/message and launcher wire contracts. TaskDocumentRef and TaskScopedReaderContext retain repository/path identity separately from provider actor/workspace IDs. Dynamic model/effort/tier validation respects explicit overrides. Immutable sessionOptions records requested native creation values; agent.serviceTier is observed only when the host reports it. The declared schema alone certifies no launch, acceptance or publication.

- Current imported source owns this scoped route boundary. [275]
- Current imported source owns this scoped route boundary. [276]
- Current imported source owns this scoped route boundary. [277]
- Current imported source owns this scoped route boundary. [278]

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/models/`          |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

| lastUpdated | 2026-09-21T23:45+02:00 |
- **The union that gained this leaf's member, with the new code inserted between the comparison refusal and the adapter refusal.** [1]
- **The refusal record the new code travels in, and the result that carries it as one of exactly two outcomes.** [2]
- The surface version that stays `/1`, with the reasoning recorded beside the constant. [3]
- **The availability vocabulary, its five states and the validator that refuses a favourable default.** [4]
- **The field the evidence pane gained, and the re-export that keeps the vocabulary reachable through the payload module.** [5]
- **The owner that resolves every channel, so the vocabulary has a producer and not only a shape.** [6]
- The cases that measure the vocabulary's refusals and its presence in the served wire schema. [7]

## 260928-MIK-L37 A Reopened Leaf's History Attempt, And The `database_frozen` Refusal Code

`260928-MIK-L37` (MIK-R37). Three models changed:

- **[`knowledge_files/history.py`](knowledge_files/history.py.md).** `ar-history/v1` gains an optional `attempt`
  (>= 2, a leaf only). A leaf reopened after its closeout keeps its closed file frozen and writes
  `<leaf-id>-attempt-<n>.json`. `writable_attempt` names the attempt a write or closeout goes to, and
  `merged_leaf_history` reads all of a leaf's files as one history: a later row about a subject supersedes the
  earlier one. A first file carries no `attempt`, so every existing file keeps its bytes. The same module holds
  the rules for the governing row of a record a leaf changed (`changed_record_row_violation`,
  `changed_family_row_violation`, `keeps_change_visible`), and `invariant_revision_violation` accepts a `changed`
  row at an unchanged revision only as a restatement of the leaf's earlier `changed` row (INV-XN0FG8).
- **[`knowledge_files/documents.py`](knowledge_files/documents.py.md).** `history_path(owner, attempt)` and its
  inverse `owner_history_attempt(path, owner)`.
- **[`knowledge/result.py`](knowledge/result.py.md).** `database_frozen` joins the refusal codes: a database write
  or publication into a converted memory tree (MIK-R37 rule 3).

- All of an owner's history files read as one. [272]
- The attempt-qualified history path. [273]

- Why a row cannot govern an invariant whose revision the leaf changed. [274]


## 260921-ICR-L44 Two Pure Extractions, And The Anchor Observation Gains A Structured Region

Two value vocabularies moved into their own modules, each re-exported unchanged by the module it left so
every existing import keeps working: the anchor-observation vocabulary (`AnchorResolutionState`,
`ANCHOR_RESOLUTIONS`, `AnchorResolution`) now lives in `models/knowledge/read_anchor.py` (re-exported by
`read.py`), and the family member-source reference (`ReviewFamilyMemberSource`,
`ReviewSourceLocatorState`, `source_locator_state`) in `models/knowledge/review_family_source.py`
(re-exported by `review_family_context.py`). Both moves kept their source modules under the 600-line
pressure line. Two additive wire changes rode with them: `AnchorResolution.resolved_ranges` — structured
one-based line ranges, allowed only on `exact_recorded_blob` — appears on **every** anchor observation
(knowledge read pages, diff observations, the family roster), and the member source gained `locator`,
`resolved_ranges` and a required `locator_state`, with `role`/`rationale` required. The locator state is
decided by one function shared by the producer and the validator, so a region can never be stated on
bytes the side did not find.

- The anchor observation and its region validator. [8]
- The member-source reference and its one locator-state rule. [9]

## 260921-ICR-L15 Measured assessment currentness

**Route meaning changed: an assessment's currentness is now a fact a measurement established, not a
label derived from whether a mapping was supplied.** Three modules of this route are touched: two change
their vocabulary, and the third changes only a docstring.

`models/lifecycles/review_assessment.py` (502 → 620 lines) declares the per-record state as the
four-member `AssessmentBindingStatus` — `not-measured`, `current`, `stale`, `unavailable` — published
once as `ASSESSMENT_BINDING_STATUSES` and reused as `CURRENTNESS_STATES`, and
`AssessmentEntry.currentness` carries it. `SubjectAssessmentStatus` gained `not-measured` and
`unavailable` beside `none-recorded`, which stays the *unassessed* subject's own state rather than a
fourth disposition. `SubjectAssessmentState` gained `notMeasuredCount` and `unavailableCount` plus the
validator (`_counts_describe_the_records_that_exist`, `_require_the_counts_to_partition_the_records`,
`_status_of_records`) that derives the currentness counts from the entries and refuses a status its own
records contradict, and `assessment_state_for(assessments, *, statuses=None)` reports `not-measured`
for an assessment nobody measured — there is no argument that means "assume current" and none that
means "assume stale". The subject status follows the precedence `stale` → `unavailable` → `unresolved`
→ `not-measured` → `current`.

`models/lifecycles/review_assessment_binding.py` (276 → 497 lines) gained
`AssessmentCurrentnessMeasurement` (`state` ∈ `measured`/`not-measured`/`unavailable`, the `values` a
world was read to hold, a `detail`, and the `unmeasured` identities with their own reason) and the whole
rule in `measured_binding_status`: a failed measurement is `unavailable`; a measured disagreement is
`stale`, decided by the shipped `disputed_dependencies` comparison; a completed measurement that
covered every declared identity and disagreed nowhere is `current`; and everything else — including an
empty measurement — is `not-measured`. `measured_binding_statuses`, `supplied_measurement_statuses`,
`subject_state` and `unmeasured_identities` carry it to the shapes the composition and the projection
use. `assessment_currentness`, `disputed_dependencies` and the `require_current_*` refusals are
**unchanged**: the comparison stays the one equality authority.

`models/knowledge/review.py` is a **docstring-only** change (1198 lines before and after):
`ReviewAssessmentDisplay.binding_state` is now documented as the measured status carried verbatim, in
the four states named above. `models/knowledge/review_records.py` is unchanged by this leaf, so nothing
on the record-availability vocabulary moves.

Three facts a reader of this route should carry:

- **Presence of a mapping is never the decision.** An empty measurement is measured and covers nothing,
  which is a different fact from a measurement that failed.
- **An unmeasured binding is neither current nor stale.** Reporting it as either would publish a fact
  the store never held.
- **The summary cannot disagree with its records.** The counts partition the entries and the status is
  re-derived from them, so a `current` subject holding an entry nothing measured is unrepresentable.

## 260921-ICR-L21 The Final-Output Vocabulary: One Record, Three Verdicts, And A Validator That Re-Derives Them

`260921-ICR-L21` (`ICR-R21@v1`) declares the final-output receipt in a **new sibling module**,
`models/knowledge/review_final_output_receipt.py`, beside the other review vocabularies and next to the
record it belongs to (`review.py`). It is the **vocabulary alone** — the operation that selects a
generation, publishes the receipt and reads it back is
`application/review_final_output_receipt.py` — so a consumer can hold and validate a receipt without
importing the operation that produced it.

The vocabulary's shape is the requirement's own rule made unconstructible-if-false:

- **`FinalOutputReceipt` is a set of owner-produced identities and no authored prose** — the generation's
  seal and manifest digest, the reviewed baseline and candidate code trees, the delivered code
  commit/tree, the delivered memory-content commit/tree (absent together exactly when
  `memory_output_state` says so), the published knowledge identity read through the ordinary read route,
  and the two match verdicts. The one sentence it publishes, `statement`, is derived from those fields.
- **The verdict has three values, and the third exists because two would state something false.**
  `bound` is the only value that claims coverage and it requires a measured match on every channel the
  generation actually **selected**; an unmeasured knowledge channel is `unmeasured`, not matched; a
  mismatch is `moved`. Likewise `MatchState`'s `not-comparable` is not a softer
  `differs-from-reviewed-input`, and `PublishedKnowledgeState` keeps `unusable` apart from
  `not-recorded`.
- **The validator re-derives every verdict from the record's own fields and refuses a record whose
  verdicts do not follow** — detectable without the store, which is what stops a forged `bound` from
  surviving a read-back.
- **One rule, one expression.** `final_output_verdict` is the single statement of the verdict rule and
  the writer calls it, so no second copy can drift from the validator.

## 260921-ICR-L8 The Movement Vocabulary Enters The Review Wire

`260921-ICR-L8` (`ICR-R08@v1`) declares the recorded-relationship vocabulary in a **new sibling module**,
`models/knowledge/review_relationships.py` (372 L), beside the other payload vocabularies — the movement,
its sides and states, the authored lineage, the gaps with their codes, the recorded pairing bases and the
labelled rename inference — and re-exports it from `models/knowledge/review.py`, whose `__all__` names
stay where a reader looks for them. The vocabulary is an **enforcement** of the packet rather than a
container: a movement carries both sides or the transition that says why not; a paired movement must
name the recorded relation it paired on; a gap must name a displayed side; a movement that could not
establish its identity must say so with an `identity_not_recorded` gap; and a rename inference's basis
can only be Git's own detection, with a measured pairing, a measured non-pairing and an unmeasured
inference kept apart.

Two additive field changes reach the review wire, both with defaults so an existing dashboard fixture
still validates: `ReviewSourceLocation` gains the preserved `invariant_id`, the `recorded_side`, the
movement's `transition`, the `counterpart_path` (named only when the other side records exactly one
address) and the whole `movement`; `ReviewSourcePane` gains the `relationships` collection, which exists
because a membership and a route association have no source address at all and because a movement whose
two sides are one row at one address is still one association rather than two locations. The dashboard's
TypeScript mirror (`dashboard/src/data/review.ts`) does **not** carry the new fields yet — mounting the
collection in the pane is `ICR-R24`'s — so this route records the wire, not a rendered page.

- **The vocabulary module's own statement of the five rules its shape enforces, and the movement with its four validators.** [10]
- The closed unions: the kinds, the side states, the transitions, the lineage kinds, the gap codes and the recorded pairing bases. [11]
- **The unresolved fact as a value, and the side whose validator refuses a recorded state without a relationship identity.** [12]
- **The labelled rename inference, whose validator ties a pairing to its state and refuses a similarity word on an unmeasured one.** [13]
- **The pane row that now carries the association beside its address, and the pane that carries the whole collection.** [14]
- The display owner that fills the vocabulary, and the traversal that builds the movements. [15]

## 260921-ICR-L9 The Catalogue's Presence And Totals Enter The Wire, And The Per-Subject Count Leaves It

**Route meaning changed: the entry half's vocabulary now describes a population, not a per-subject
comparison.** `ReviewEntry.presence` — the new three-member `ReviewSubjectPresence` union
`before_only`/`after_only`/`both` — **replaces** `selected_item_count` (893 → 936 lines). The deleted
field was the wire carrier of the per-subject compare-to-earn-a-row mechanism `ICR-R09@v1` removes;
an entry that carried a comparison count would oblige the catalogue read to compare every subject
before answering, which the packet forbids. `ReviewEntryListResult` gains the labelled totals
(`total_subjects`/`invariant_total`/`family_total`) with the `_require_the_totals_to_describe_the_catalogue`
validator: the total must sum its two kind totals, a refused read carries zero totals, and the total
is `>=` the page beside it — the rule R10's paging depends on. The one-direction rule is unchanged in
substance and now totalled: a refused entry read still offers **no** entry, an empty `entries` on an
`entries` state is still a pair that records no subject with the task-context source review reachable
beside it.

- **The presence union on the vocabulary, beside the subject-kind union it parallels.** [16]
- **The entry value with `presence`, and the entry list with the totals and their agreement validator.** [17]
- The catalogue owner that fills these values, and the adapter that delegates to it. [18]

## 260921-ICR-L7 The Review Wire Carries The Explicit Revision Selection, Declared Next Door

**Route meaning changed: pane 1's two statements are the selected revisions, and the selection is a
recorded value with its own validators.** `models/knowledge/revision_selection.py` (new, 150 lines)
declares `ReviewRevisionSelection`: the `compared` head pair, the `added`/`removed` one-sided head,
or the explicit `ambiguous`/`unresolved` non-pair — always with every head and every retained
revision listed, and with the human-readable `statement` beside the ids. Three validators make a
misreading unconstructible: the state carries its own state's ids and no other's, the pair is drawn
from the recorded heads, and the heads from the retained. There is no timestamp, no similarity, no
rank and no "latest" anywhere in the value. `models/knowledge/review.py` (873 → 893 lines) carries
it on the pane as the optional `revision_selection` — absent exactly when no subject was compared —
with the one-direction validator that refuses a recorded selection beside a task-context pane. The
value lives outside the vocabulary file so that file stays under the soft rail, and the selection
policy that computes it lives on the application route, not here.

- **The new value module: the five-state union and the model with its own statement.** [19]
- **The three validators that make a misreading unconstructible.** [20]
- **The pane field that carries the value, with its one-direction validator.** [21]
- **The policy that computes the value from authored heads.** [22]

## 260928-MIK-L04 A Family Route May Be The Repository Root, `.`

**Route impact (MIK-R04@v2, ruling Q3).** [`knowledge_files/sidecars.py`](knowledge_files/sidecars.py.md)
exposes `RoutePath`, the route sidecar's own route-directory spelling (a repository-relative path, or `.` for
the root route), and [`knowledge_files/records.py`](knowledge_files/records.py.md) types
`FamilyRecord.routes` with it. A family routes at `.` only when it genuinely has no narrower home. Every
other path field keeps `RepositoryPath`, so `""`, `"./"`, `"./mcp"`, `".."`, `"/"` and `"mcp/"` are still
refused everywhere.

- The shared route-directory type. [23]
- The family record's routes use it. [24]

## 260928-MIK-L20 The Census File Formats

**Route impact (MIK-R20@v2).** [`knowledge_files/census.py`](knowledge_files/census.py.md) declares the four
`ar-census-*/v1` schemas (baseline, inventory, claims, route status), the injective `route_slug` (the root
route `.` is `@root`), `mint_claim_id` (`CLM-` plus six Crockford characters) and `governing_status`, the
"latest status entry across every census" rule, at this rank so every layer can apply it.
[`knowledge_files/documents.py`](knowledge_files/documents.py.md) registers the four schemas in
`SCHEMA_MODELS` and `CensusDocument` in `KnowledgeDocument`. The models check shape only; append-only and
pinning are the validator's census rules. The legacy `knowledge/census.py` vocabulary is kept for the claim
kinds and applicability and stays until MIK-R26 (leaf L26).

- The four census schemas registered for dispatch. [25]
- The latest status entry across every census governs. [26]

## 260928-MIK-L12 The One Definition Of An Anchor's `content`

**Route impact (MIK-R12@v2, architect ruling 5).** [`knowledge_files/anchor_content.py`](knowledge_files/anchor_content.py.md)
fixes which bytes an anchor's `content` hashes: a line range is its lines (one-based, inclusive), each with its
own terminator exactly as the blob holds it, split on `\n` only and never decoded; a file anchor is the whole
blob; `content` is `sha256:<hex>` of those bytes. The curator writer records `content` through it, and L24's
converter and every later leaf (MIK-R03, R08) must compute it here too; the Doc14/L21 fixture hashes are
illustrative. It is not re-exported from `knowledge_files/__init__.py`.

- The range's bytes. [27]
- The content identity. [28]


## 260928-MIK-L24 The `onboarding_trace` Row Kind, And The Read Tool's Format Fields

**Route impact (MIK-R24@v1 rules 5, 8 and 9).**

- [`knowledge_files/history.py`](knowledge_files/history.py.md) registers a third row kind,
  `onboarding_trace` (`OnboardingTraceRow`, owner MIK-R30). Its subject is `onboarding:<path>` or
  `onboarding:<route>/overview`, with the single disposition `no_impact`. MIK-R24 rule 8 step 1 is its first
  writer: a crossing sync moves an open leaf's Update History no-impact markers into its history file as
  these rows. **By architect ruling N1 the moved lines go in the structured list field `markers`** (one
  `Text` per marker line, a longer line split deterministically), and `reason` is a short fixed summary. The
  minimal registration is accepted; the kind's semantics stay MIK-R30's (L30), which inherits `markers`.
- [`read_files.py`](read_files.py.md): `FileRead` admits three optional fields, `format` (`text/v2` or
  `legacy-format`), `sidecar` and `references`. `application/read_files_format.py` fills them.

- The onboarding-trace row and its `markers` list. [29]
- The file result's format fields. [30]

## 260928-MIK-L28 The Read Response Carries Optional Proofs

**Route impact (MIK-R28@v1 rule 4).** [`tools/knowledge_responses.py`](tools/knowledge_responses.py.md)
gains one optional, response-side field: `proofs` on `KnowledgeReadResponse`, each
`{id, invariant, path, anchor, facet, sidecar}`, present only for an `invariant` or `family` read from a
converted memory tree. **The additive optional field is accepted (architect ruling, 2026-09-29).** It
defaults to `None` and is absent from the wire for a database read, so no existing response changes. The
module docstring states that a proof says what its test demonstrates, never that the test passed or that
the invariant holds. No input model changed.

- The optional field (beside the later `currentness`, `families` and, since MIK-R05, `routeChain`) and the docstring boundary. [31]

## 260928-MIK-L02 The Shared Continuation Token, And The Read Response's Page

**Route impact (MIK-R02@v2).** Three model modules change:

- [`knowledge/continuation.py`](knowledge/continuation.py.md) (new, carded, governed by this overview):
  `KnowledgeContinuation`, the one `knowledge-continuation/v2` token (`kc2.` prefix; short aliases,
  compressed canonical JSON). It binds the memory tree, the response and resuming view, the seed (with a view
  walk's effective ordering), the selection policy and version, the manifest digest, the position, the
  threshold, the code tree page 1 resolved at, and at most 64 queued seeds. It carries no local path
  (architect rulings 19:56:40 Q5 and Q6; 20:40:40 F2; the tree ID binding accepted at 21:32:34; the 64-seed
  edge carried to L01, which resolved it as the named refusal `seed_queue_exceeded`).
- [`tools/knowledge_responses.py`](tools/knowledge_responses.py.md): `KnowledgeReadResponse.state` gains
  `"page"`, and the model gains the optional `page` and `threshold` fields, both absent for a database.
- [`knowledge/projection_manifest.py`](knowledge/projection_manifest.py.md): the projection refusal closure
  gains `oversized_row`, additively.

- The one continuation token and what it binds. [32]
- The read response's page state and fields, re-read when MIK-R05 added `routeChain`. [33]
- The projection refusal code for a row too large for one artifact. [34]

## 260928-MIK-L08 The Integrity And Sync Responses Carry The Worklist

**Route impact (MIK-R08@v2 rules 7 and 8).** Two response models gain optional fields, both absent from the
wire when unset:

- [`tools/knowledge_responses.py`](tools/knowledge_responses.py.md): `KnowledgeIntegrityCheckResponse`'s
  `repositoryId` becomes optional, and `worklistState` and `worklist` are present only when the caller
  named a leaf's `contractPath`.
- [`worktree.py`](worktree.py.md): `WorktreeSyncResponse` gains `knowledgeWorklist`, the summary a completed
  managed sync attaches when a worklist applies.

For every unconverted leaf (every production leaf before MIK-R37) and every dataset-only call, the
responses are unchanged. No input model changed.

- The integrity response's optional fields. [35]
- The sync response's worklist summary. [36]

## 260928-MIK-L03 The Read Response Carries Optional Currentness

**Route impact (MIK-R03@v2).** [`tools/knowledge_responses.py`](tools/knowledge_responses.py.md):
`KnowledgeReadResponse` gains `currentness: dict[str, Any] | None = None`, absent for a database read. The
module docstring is its description: the counts cover every invariant the answer carries, named or in full,
plus every family member (review N5, 2026-09-29T19:13:41); with no `codeTreeId` every realized invariant is
`unverifiable` and `HEAD` is never substituted (18:42:37 ruling 2); a failure is `unverifiableReason` and
never refuses the read (N2). No input model changed.

- The optional field and its docstring paragraph. [37]

## 260928-MIK-L30 What The `onboarding_trace` Row Means

`knowledge_files/history.py` changes only in `OnboardingTraceRow`'s docstring: MIK-R30 now gives the kind its
semantics. On a converted tree a row with disposition `no_impact` satisfies the onboarding gate's item for a
changed source file's card or nearest governing route overview that has no counted change; `no_impact` is
the only disposition; the curator writes it through the writer's `history` section, and MIK-R24's crossing
sync also writes it when it moves an open leaf's markers. The root route's subject is `onboarding:overview`
(architect ruling 2026-09-29T18:49:50 (3)). The model, its fields and its registration are L24's, unchanged.

- The row kind's docstring with MIK-R30's meaning. [38]

## 260928-MIK-L11 The Planned-Effect Forms And The Planned Row

MIK-R11 adds one pure module and one row kind to `knowledge_files/`:

- [`planned.py`](knowledge_files/planned.py.md) is the one spelling of the planned-effect forms: the declared
  subject (`invariant:<INV-ID>`, `family:<FAM-ID>` or `new:<hand-off label>`), the planned subject key
  `planned:<declared subject>#<effect>` (built from the declaration, never from its list position), the
  `requirementRef` form `<stable ID>@v<n>` (ruling Q5, 2026-09-29T21:56:18+02:00), the three dispositions and
  the ref each takes, and `planned_item_open`, the stored-item predicate for the closeout gate (MIK-R09),
  which agrees with the worklist's `satisfiedBy`. The task plane, the history model, the worklist and the
  writer all import these forms from here; the task plane imports them without reading knowledge.
- [`history.py`](knowledge_files/history.py.md) gains `PlannedRef` and `PlannedEffectRow`, the fourth
  registered row kind (`planned`, owned by MIK-R11): a planned row answers a `planned_untouched` item with
  `realized_elsewhere`, `deferred` or `dropped` and a `ref` naming exactly one thing of the kind its
  disposition takes. The model checks shape; the writer checks that the ref resolves.
- The effect vocabulary is unchanged (the planned key's effect alternation is the admitted labels).
- Nothing in the installed runtime reads history files or the declaration before MIK-R37, and no real task
  document may carry the declaration before that install (ruling Q2).

- The planned forms, the key and the gate predicate. [39]
- The planned row and its disposition-bound ref. [40]
- The registry with the fourth kind (MIK-R10 later adds a fifth). [41]

## 260928-MIK-L27 The Admission Criteria's Meanings

MIK-R27 changes no model here: the `admission` shape and each kind's criterion vocabulary stay MIK-R21
rule 4's. [`shapes.py`](knowledge_files/shapes.py.md)'s admission docstrings now give each criterion's
meaning: `spans_locations` (realized in more than one file), `guarded_by_test` (at least one proof entry),
`family_guarantee`, `prevents_costly_mistake` (the justification names the costly error), `joint_guarantee`,
`real_alternatives` and `constrains_future_work`. The first two are the only ones checked mechanically, by
the knowledge validator's `rules_admission.py` for a new record; the reviewer judges the rest (OM-4, entered
by requirement, ruling 2026-09-29T22:11:24 Q3). An export is recognised by its `origin.legacyId` deriving its
ID through `knowledge_files/ids.py`'s `derived_record_id` (ruling 23:04:57 F2), so a record carrying a
`legacyId` that does not derive its ID is judged as new.

- The invariant criteria's meanings, and which two the validator checks. [42]
- The derivation that identifies an export. [43]

## 260928-MIK-L01 The `leaf` Response Kind, The Public Queue Cap, And The Optional `families`

**Route impact (MIK-R01@v2).** Two model modules change, additively:

- [`knowledge/continuation.py`](knowledge/continuation.py.md): `PagedResponse` gains `"leaf"`, the response
  kind of the family-complete leaf read of a seed path, which resumes on the `source_context` view. The queue
  cap is public as `MAX_QUEUED_SEEDS` (64), because `knowledge_paging/block_pages.py` refuses a longer tail by
  name, `seed_queue_exceeded`, instead of minting it (the L02 R2-1 edge; ruling 2026-09-29 23:21:57). The token
  still carries no local path (carried 21:17:07).
- [`tools/knowledge_responses.py`](tools/knowledge_responses.py.md): a docstring paragraph names the leaf read
  (a `source_context` read of a path is `state: "page"` whose `payload.rows` are the leaf rows), and the model
  gains the optional `families` field, the `invariant` view's containing families by ID and title (rule 7).
  Both are absent for a database.

- The response kinds a token pages, and the public queue cap. [44]
- The optional `families` field on the read response, followed since MIK-R05 by `routeChain`. [45]

## 260928-MIK-L13 The Decision Content Rules And Their Derived Reads

**Route impact (MIK-R13@v2), one new module.** [`knowledge_files/decisions.py`](knowledge_files/decisions.py.md)
holds MIK-R13's content rules for `records.DecisionRecord` as pure functions over one record, so the validator
(`memory_quality/knowledge_validator/rules_decisions.py`) and every reader apply one reading: at least two
alternatives and exactly one chosen, `reconsider_when` on every rejected or deferred alternative (the prose is never
evaluated), and `reconsider_on` indexes that name an existing rejected or deferred alternative in the authored
order. It also derives what is never stored: `superseded_by` and `derived_status` (a decision is `superseded` when a
later decision's `supersedes` names it; `DecisionStatus` cannot spell it), `governs_links` and `reconsider_links`
(MIK-R14's subject `reconsider:<DEC-ID>#<i>`). The reads are for L29 (packet rule 6, ruling 2026-09-30T01:45:56
Q4) and L14 (Q6: index stability when alternatives are reordered; L14 met it, see its section below). The record
shape is unchanged.
[`knowledge_files/records.py`](knowledge_files/records.py.md)'s card now points to the module.

- At least two alternatives, exactly one chosen. [46]
- Superseded is derived from later decisions' `supersedes`. [47]
- The reconsider links and MIK-R14's subject. [48]

## 260928-MIK-L25 The Review Comparison As Four Git Trees, And The Tree View's Answer

**Route meaning extended (MIK-R25).** One new model module, [`knowledge/review_trees.py`](knowledge/review_trees.py.md)
(carded, governed here, following the `knowledge/` precedent of no sub-route overview):

- `ReviewTreeComparisonRecord` (`ar-review-tree-comparison/v1`): task id (the task directory name), leaf id,
  number, the four `ReviewTreeSide`s (a committed side names its commit; an uncommitted one names its pinning ref
  under `REVIEW_REF_NAMESPACE`, `refs/ar/review`) and the optional `ReviewConvertedBase`. `same_trees` compares task,
  leaf, the four trees and the converted base, so a record written under another naming is never reused (ruling
  2026-09-30T02:32:42 (a)).
- `ReviewTreeSideState`: `available`, `unavailable-history` (named, never substituted) or `legacy-unavailable`.
  `ReviewKnowledgeSide` carries the index state and problems; `ReviewCodeSide` (review F4) the reopened code trees.
- `ReviewTreesResult`: `trees`, `not-converted` or `refused`, with the knowledge diff groups
  (`ReviewKnowledgeTreeDiff`), per-side currentness and `ReviewWorklistView`. Its mixed key casing is carried to L31
  (review F9).

No database path is part of either shape.

- The ref namespace and the durable record. [49]
- The tree view's answer. [50]

## 260928-MIK-L10 The Unexplained-Change Subjects And The No-Invariant Row

MIK-R10 adds one pure module and one row kind to `knowledge_files/`:

- [`unexplained.py`](knowledge_files/unexplained.py.md) is the one spelling of the unexplained-change subjects:
  `hunk:<path>@<base lines>..<candidate lines>` (each side the `sha256` of the hunk's changed lines, or `absent`),
  `file:<path>@<C-side object>`, the item ID of a hunk subject (a function of the subject alone, so an edit
  elsewhere never reopens an answered item), the `no_invariant` row subjects (`hunk:<item id>` or the file
  subject), and the predicate `unexplained_satisfied_by` / `unexplained_item_open`. A **covered** item is
  answered only by its `no_invariant` row; an **uncovered** item only by the file's onboarding trace (a counted
  card change or the `onboarding:<path>` row), never by a `no_invariant` row (ruling 2026-09-30T03:24:28 N2). The
  worklist computes `satisfiedBy` with the same function the closeout gate (MIK-R09, L09) applies, so they agree.
- [`history.py`](knowledge_files/history.py.md) gains `UnexplainedChangeRow`, the fifth registered row kind
  (`unexplained`, owned by MIK-R10): `no_invariant` is its only disposition, with a non-blank `reason`, and it
  adds nothing to the common row fields. Attach and author are not rows: an entry over the change links it
  (ruling 01:56:39 Q1), and a delete-only hunk, which no new entry can link, admits only this row.
- Nothing in the installed runtime reads history files before MIK-R37, so unconverted memory is unchanged.

- The subjects, the row subject and the gate predicate. [51]
- The no_invariant row. [52]
- The registry with the fifth kind. [53]

## 260928-MIK-L05 The Read Response's Optional `routeChain`

MIK-R05 adds one optional, response-side field and one docstring paragraph to
[`tools/knowledge_responses.py`](tools/knowledge_responses.py.md):

- `KnowledgeReadResponse.routeChain` (`dict[str, Any] | None = None`) is set on a `registration_absent` refusal of
  a path read from a converted tree: the mechanical chain (`directory`, `links`, `derivation`, `state`,
  `families`) stating `no_governing_family`. A page carries the same block inside `payload`.
- The docstring paragraph "Route-chain families (MIK-R05)" names the `chain_family` rows in `payload.rows`,
  `payload.routeChain`, and the family seed (`source_context` naming `familyRevisionId` and no path; ruling Q1,
  2026-09-30 03:32:18).
- The continuation model is unchanged: a family seed is a `leaf` token whose seed is `{"kind": "family", "id"}`,
  and the policy it binds is now `family-complete-leaf/v2` (ruling Q4), so a v1 token is refused.
- A database read never sets the field, so the installed runtime's responses are unchanged.

- The optional field. [54]
- The docstring paragraph. [55]

## 260928-MIK-L31 One Entry Located On Both Code Sides, For The Focused Cards

**Route meaning extended (MIK-R31).** One new model module,
[`knowledge/review_tree_entries.py`](knowledge/review_tree_entries.py.md) (carded, governed here, following the
`knowledge/` precedent of no sub-route overview), and one field on
[`knowledge/review_trees.py`](knowledge/review_trees.py.md):

- `ReviewTreeEntry`: one realization or proof entry of K_B or K_C (`id`, `kind`, the text `invariant`, the
  `invariant_key` the landed review payload addresses the invariant by, `before`, `after`, `change`).
- `ReviewTreeEntrySide`: whether that side's memory tree records the entry (`recorded`, `None` when it could not be
  read), the range state (`resolved`, `unresolved` with a reason, `absent`, `unavailable` with a reason — `absent`
  and `unavailable` never merged), the range and its content identity, the excerpt from the exact blob bounded by
  `EXCERPT_MAX_LINES` (400) and `EXCERPT_MAX_CHARACTERS` (48,000), the side's own authored `role`/`rationale` or
  `facet`, and its MIK-R03 `currentness`.
- `ReviewEntryChange`: `changed`, `unchanged` (the excerpt carried once, on the after side) or `undetermined` (never
  counted by guess).
- `ReviewTreesResult.entries`, empty on the leaf-wide view and filled only by the on-demand cards read (ruling
  2026-09-30T05:36:19 Q2). The wire is snake_case throughout (MIK-L25 review F9, settled by L31).

- The range and change states and the excerpt bounds. [56]
- One entry on one side, and on both sides. [57]
- The tree view's field for the entries. [58]

## 260928-MIK-L32 The Unexplained-Changes Lane's Vocabulary And Its Reconciliation Validators

**Route meaning extended (MIK-R32).** One new model module, [`knowledge/review_lane.py`](knowledge/review_lane.py.md)
(carded, governed here, following the `knowledge/` precedent of no sub-route overview), and new optional fields on two
existing results:

- `review_lane.py` fixes the lane's three shapes: `ReviewLaneSummary` (the entry's count, file buckets only),
  `ReviewUnexplainedLane` (the two destinations, the bucket totals, `unmeasured` and every measured path's bucket,
  `paths`, ruling 2026-09-30T12:19:20 Q1) and `ReviewFileClassification` (the per-file response: both sides with every
  entry's range or `LaneRangeReason`, each hunk with its class, links with invariant revisions, their keys and family
  occurrences with `LaneMembershipState`, and the unknown reasons per side). Its validators make an answer reconcile:
  an entry supplies a range or names why not; a hunk is linked exactly when it has links and unknown exactly when it
  has reasons; the classes sum to the hunks; a destination lists exactly its bucket and attributed files; the three
  buckets sum to the changed total; and an unmeasured value (`partial`, `unavailable`) carries no totals, so it can
  never read as zero.
- [`knowledge/review_trees.py`](knowledge/review_trees.py.md): `ReviewTreesResult.lane` and `file_classification`,
  filled only by a lane or file read.
- [`knowledge/review_intent_summary.py`](knowledge/review_intent_summary.py.md): `ReviewIntentSummaryResult.attribution`,
  the lane's count for a tree comparison, outside the one-outcome validator (ruling Q6) and absent for a dataset
  comparison (the served body omits `None`).

The caps are the knowledge base's own (`REFERENCE_MAX_LENGTH`, `PROSE_MAX_LENGTH`, `PATH_MAX_LENGTH`); the application
clips reasons and a refusal's input so a validated request never trips one (review R1 F2 and F4, ruling 13:07:38).

- The lane's literals: buckets, hunk classes, range reasons, membership states, gate linkage. [59]
- The lane reconciles; an unmeasured value carries no totals. [60]
- The tree view's two new fields, and the summary's. [61]

## 260928-MIK-L33 The Change-Kind Vocabulary Rides On The Family Context

MIK-R33's facts have their own wire module, [`knowledge/review_change_kinds.py`](knowledge/review_change_kinds.py.md):
the literals (`ChangeKind`, `ChangeFact`, `ChangeMark`, `GuaranteeChange`), the precedence, `primary_change` and
`change_marks` (the unconditional `unknown` for an unresolved range, review R1 F4), `ReviewMemberChange` (built by
`of`; validators re-derive `primary` and `marks`, and require `unknown_reasons` exactly when the change kind is not
fully known and `membership_reasons` exactly when the membership is unknown) and `ReviewFamilyChanges`.
[`knowledge/review_family_context.py`](knowledge/review_family_context.py.md)'s `ReviewFamilyContextEntry` gains the
optional `change_kinds` and a validator requiring facts for exactly the returned member occurrences.

- The facts derive the primary and the marks. [62]
- The entry's facts describe exactly its returned members. [63]

## 260928-MIK-L14 The Reconsideration Subject, Its Triggers, And The Sixth Row Kind

**Route impact (MIK-R14@v2), one new module and one row kind.** [`knowledge_files/reconsideration.py`](knowledge_files/reconsideration.py.md)
(new, carded, governed here) is the one spelling of MIK-R14's names, so the worklist registrant, the history-row
model, the writer and the closeout gate cannot drift apart: the kind `reconsideration_candidate`; the subject
`reconsider:<DEC-ID>#<alternative index>` (`RECONSIDER_SUBJECT_PATTERN`, the same spelling as L13's
`ReconsiderLink.subject`), spelled and parsed; the two dispositions `still_rejected` and `raise`; the history-row
dispositions that count as a change (`changed`, `moved`, `deleted`, `rerouted`, `retired`); the five triggers
(`TRIGGERS`, with `anchor_stale` from review F3) and the three a `still_rejected` answer refreshes
(`REFRESHED_TRIGGERS`, rulings Q2/Q3, F1); `question_key`, the prefix that makes a `raise` question appear once per
subject and leaf (Q7); `link_target_key`, the one spelling of a link target the writer compares before a refresh
(review N1); and `reconsideration_item_open`, the gate's predicate, which the worklist's `satisfiedBy` applies too.
[`knowledge_files/history.py`](knowledge_files/history.py.md) gains `ReconsiderationRow`, the sixth registered row
kind (`reconsideration`, owner MIK-R14), with the common fields only; the registry is compared as a set in the tests
because leaves register in landing order (review F9). The module docstring names MIK-R14 and leaves MIK-R06 for
later. L13's `decisions.py` reads (`reconsider_links`, `superseded_by`, `derived_status`) are what the worklist
evaluates; its Q6 carry (index stability) is met by the validator rule `R14.1-linked-alternative-order` in
`memory_quality`. Nothing reads these names on an unconverted leaf.

- The subject pattern, the triggers and the refreshed triggers. [64]
- The one spelling of a link target, and the gate's predicate. [65]
- The sixth row kind. [66]

## 260921-ICR-L3 The Review Refusal Vocabulary Gains The Source-Content Code
This route's impact is **one member of one closed union**, and the reason it is worth naming is that a
closed vocabulary a client reads is a contract change even when the addition is strictly additive.
`models/knowledge/review.py`'s `ReviewRefusalCode` — the closed union a `ReviewRefusal` carries as its
`code` — gained `source_content_unresolved`, inserted between `comparison_refused` and
`review_adapter_unavailable`. It is the answer the new **entry-content** route gives when the generation
a listing published no longer resolves to the two code objects that listing bound: there are no bytes to
serve for that entry, and that is a different fact from "this process cannot read the entry" (an
unwired port) and from "this entry has no content" (an empty rendering). The union is the module's own
statement of which refusals exist, declared once here so the transport's admission path and the
browser's rendering of a refusal cannot come to disagree about the vocabulary.
**It is additive in the strict sense, and that is a fact about the transport rather than a promise.**
The union is a vocabulary, not control flow: a code the transport does not recognise already answers
`400`, so a client written against the previous six keeps working and an unknown code is refused rather
than quietly mapped onto an existing answer. `KNOWLEDGE_REVIEW_SURFACE_VERSION` therefore stays
`knowledge-review-surface/1`, exactly as it did for the R02 inventory and the L45 entry half.
## 260921-ICR-L14 The Record-Availability Vocabulary Gets Its Own Module, And The Evidence Pane Carries It
`ICR-R14@v1` adds one module to this route and one field to an existing model.
[`models/knowledge/review_records.py`](knowledge/review_records.py.md) declares the vocabulary a
review's record composition reports: `ReviewRecordClassName` (the six collections, named by record
class rather than by pane, because availability is a fact about the owner and one fact must serve
whichever pane renders the records), `ReviewRecordChannelState` (the five states — `recorded`,
`none_recorded`, `unavailable`, `not_measured`, `not_selected`) and `ReviewRecordChannel`, whose
validator makes "a count nobody measured" unrepresentable: a counted state must carry its count, an
uncounted state may not carry one, `recorded` requires at least one record, `none_recorded` requires
exactly zero, and every non-answer must state what would produce one.
**The extraction is also a rail repair.** The vocabulary used to live in
[`models/knowledge/review.py`](knowledge/review.py.md), which had crossed the 900-line soft rail at 940;
it is 851 now and the three names are **re-exported** from it, so no importer had to learn a new home.
`ReviewEvidencePane.channels` is the one field this leaf added there — the composition's own supply,
carried **whole** (a class that was not read or could not be read appears with that state instead of
being absent from the list) and deliberately not derived from the collection lengths, because an empty
tuple has three possible meanings and the pane must render all three without claiming which one it is.

## 260915-KS-L41 The Reader Port Gains A Membership Method, And The Integrity Response Binds Its Run

Two models on this route changed, and both are contract changes rather than behaviour changes.
`models/knowledge/view.py`'s `KnowledgeViewReader` protocol now declares **five** methods rather than
four: `snapshot()`, `registered_counts()`, `rows(record_kind)`, `family_member_rows()` and
`anchor_state(locator)`. `family_member_rows()` exists because a generic read cannot answer its question —
family membership is a recorded generation-1 entity with its own table and is **not** duplicated into the
`knowledge_record`/`record_revision` envelope `rows(record_kind)` reads, so asking that method for the
kind `family_member` returned no rows on a dataset that holds them, and a family view then reported a
joint guarantee, no members, no implementation locations and a complete answer. Declaring the method is
what makes the read a typed call rather than a string a caller can spell into an empty answer, and a
reader that cannot satisfy it fails the protocol instead of returning empty.

`models/tools/knowledge_responses.py`'s `KnowledgeIntegrityCheckResponse` gained the five fields that
bind its conditions to the run they were measured over: `selectedRunId` and `inputDigest` (each
`str | None`, defaulting to `None`), `inputIdentities` and `matchingRunIds` (each a list of objects,
defaulting to empty), and `exactInputSelector` (an optional object). `matchingRunIds` carries every run
the requested scope holds, the selected one included, and `exactInputSelector` echoes the caller's own
`runId`/`inputDigest` or `None` — an explicit "the caller named no exact input" rather than a silent
absence. `compatible: None` is unchanged and still by design: this route adds a binding, not a verdict.
The response model still declares no `payload` field, so there is nowhere for a rendered view to arrive.

## IAS Contract-Scoped Activation And Sync Vocabulary

The activation vocabulary lives under `models/structural/atomic_series_activation.py` and is keyed by
the canonical series contract, not by a protected source pair. It separates selectable state
(`reconciling|active`) from observed state (`vacant|unreadable|reconciling|active`) and binds the
selected master plus canonical contract path to `contractFingerprint` — the SHA-256 of the canonical
resolved contract path. Each activation record is `schemaVersion "2.0"`; the former
`AtomicSeriesSourceRef` / `AtomicSeriesSourcePair` models and the `sourcePairFingerprint` field they
fed are gone, because two atomic masters commanded by one sprint derive the same protected source pair
and must nonetheless hold independent selection. This is disposable selection, not task truth, queue
membership, or lifecycle evidence.

Sync models project the stable enclosure-root journal without requiring task-document parsing.
Public status distinguishes a retained resolution, automatic resume, cancellation, terminal
completion, malformed/identity-invalid evidence, and bounded quarantine. Exact Git refs, admitted
heads, and per-side progress remain strict durable state; the response exposes only what an agent
needs to continue, cancel, or repair. Exact field membership is reconciled to the frozen candidate;
verification metadata remains closeout-owned until the new code commit exists.

CCR-R25 extends the public worktree wire vocabulary with optional
`AtomicSeriesActivationFact` and `AtomicSeriesAdmission` fields; the contract-scoped re-key makes them
per-contract. Status carries the addressed contract's activation address, `contractFingerprint`,
observed state, and record/error evidence. Admission responses explain the addressed contract's own
corrective state, the nested activation snapshot, expected/observed evidence, retry precondition, and
a contract-bound read-only status action. They no longer carry a `classification`, a `sourcePair*`
field or a `blocking` blocker — with them went the `AtomicSeriesAdmissionBlocking` model — because a
foreign live master is never this contract's wait, blocker, or retry precondition. These models
validate the projection shape only; selector mutation and recovery remain owned by the activation and
lifecycle domains.

## Current Structural Wire Vocabulary

MCAR-L02 adds the strict curator-coherence lifecycle family under
`models/lifecycles/curator_coherence.py`. It keeps the semantic requirement revision, worker
delivery attempt, exact source candidates, agent-owned judgments, immutable record generation,
stable live authority, optional attempt snapshot, and public request/response as separate typed
identities. The request exposes one closed `status|prepare|publish|validate` action vocabulary.
What `publish` requires is now **one declaration**: the nine publication members live in
`PUBLICATION_MEMBERS` beside the request model, and the validator, the `publish` refusal and the
`prepare` text all read it, so a member appended there is checked, named and stated with no second
edit. A `publish` refusal names every missing member by its request field name, a
`status`/`prepare`/`validate` refusal names the publication-only field it received, and the
`prepare` response states the complete input set — including the two members it does not derive
(`semantic_requirement_revision`, `delivery_attempt`), which stay the caller's own delivery
identities. Record validation requires unique exact coverage of the structured source-candidate set
rather than accepting partial or extra judgments.

`TaskDocumentRef` is the shared repository-qualified work identity. `models/structural/agent.py` and
`models/structural/gates.py` define the agent-facing request/response families without runtime
address fields; internal gate correlation models are isolated behind that public boundary. The
former flat gate model has moved, with its semantic history preserved in the successor card.
`TaskDocumentRef` is a frozen value object whose explicit hash uses repository plus path; task
altitude remains topology-owned rather than becoming a third identity field.

`models/task_document.py` also owns the closed `MasterExecutionNature` wire vocabulary:
`organizational|atomic`. Persisted task-document schema, observer projection, generated dashboard
schema, and TypeScript all import or derive from that one enum rather than maintaining parallel
strings.

`lifecycles/operation.py` adds strict closeout/integration input snapshots, an internal durable
record, and a deliberately smaller public projection. The record carries private fingerprint,
candidate tree, PID, approval claim, and recovery details; the projection exposes only the task,
kind, state, phase, heartbeat, current command, result/failure, and guidance required by agents
and the dashboard. `models/worktree.py` embeds that projection without publishing operation IDs.

## Shared Serving-Build Wire Identity

ARSPAWN-L4 owns `ServingBuildPayload` in `models/core.py` so dashboard served state and MCP
`server_info` cannot maintain parallel candidate-identity shapes. Co-location avoids adding a 26th
flat model module while keeping one strict wire authority. Required version and boot time
are supplemented by optional content digest, interpreter, package root, checkout commit, dashboard
fingerprint, and proven-dirty evidence. Absence stays honest unknown; package version alone is not
treated as exact candidate identity.

## Shared Certification Wire Ownership

[The certification wire route](certification/overview.md) owns shared frozen primitives, canonical corrective dispositions and exact stored-object references. Domain certification and lifecycle models import these concrete values; wire validity does not establish observed authority, execute a gate or select a journal record. Registry/plan compilers and the existing certificate store remain the semantic and storage owners. This extraction changes retrieval ownership while preserving the moved constraints.

## Purpose

`models/` owns the Pydantic response contracts for Agents Remember MCP payload
builders. It turns the public tool surface and internal builders
from loose dictionaries into named, inspectable models that can be validated at
runtime and tested by schema. Model homes follow tool domains: `TaskReopenResponse`
(cit:([`TaskReopenResponse`], mcp/src/agents_remember/models/task_doc.py:223-226)) lives in `task_doc.py` while keeping the `WorktreeCommandResponse` shape, since
the task_reopen payload carries the enclosure contract state.

## Hot Path Summary

The imported native Paseo role route retains canonical task/workspace identity, exact launch/replay and independent model/effort/tier validation alongside the existing converted MIK memory and publication owners.

Closeout and landing models expose code/memory outputs; `DirectLandingResponse.ledgerCache` is an informational cache-refresh result. The lifecycle models distinguish actual Git heads from filtered memory content and retain no ledger commit alias.

## 260915-CAPS-L2 Role-Capsule Contract And Compiler

`mcp/src/agents_remember/models/role_capsules/` is a **new sub-route** on this route: the master's
frozen role-capsule DTO surface plus the pure logic that compiles it. It is the first thing on this
route whose entire contract is about *what an agent seat is given*, so its reading order is worth
stating once.

The package reads in six steps, and each step is one module: `vocabulary.py` declares the frozen
ten roles/nine operations and the four composition roots; `manifest.py` parses the canonical
authored `composition-manifest.json` into typed entries **without touching the filesystem**;
`selection.py` turns an admitted binding into a scope by exact membership (no scoring, no
nearest-match, no fallback operation); `source_set.py` proves the admitted files agree with the
locked plan **in both directions**; `resolution.py` reduces each identity to exactly one block,
collapsing byte-identical duplicates and stopping on an equal-authority contradiction;
`tools.py` narrows requested tool identities against the admitted policy snapshot; and
`compiler.py` seals the result with the semantic digest and the diagnostic manifest.

`models/memory_content_excludes.py` is the route's second 260915-CAPS-L13 addition and is a
different kind of module: not a capsule DTO but the **shared memory-content exclusion policy** —
`memory.md` (the computed ledger cache) and `bootstrap/` (transient scaffolding) declared once for
all four seams that create a memory-content commit. It lives in `models` because that is the lowest
layer every producing seam can read.

Three separations are load-bearing and easy to collapse by accident:

1. **admitted input / content output / diagnostic output** — the DTOs in `types.py` keep these
   structurally apart, which is why `types.py` was split at 704 lines and the diagnostic
   projection extracted into `diagnostics.py` (541 + 217 after the A3 repairs). **Nothing in `diagnostics.py` may ever
   feed `semantic_digest`**; timestamps, unselected sources, conflict rows and refusal text are
   deliberately outside the capsule's identity.
2. **a request is not a grant** — tool requests are narrowed against `CapsuleToolPolicy`; nothing in
   this package can add a capability the policy did not already permit. **The skill channel is a
   different shape and must not be described with this one:** `compiler.skill_references` builds one
   content-addressed `CapsuleSkillReference` per declared skill (`identity`/`origin`/`uri`/`revision`)
   and consults **no** policy — a skill reference is a pointer to separately delivered content, so it
   is *carried*, and the only thing that can invalidate it is a skill root file that was not admitted.
3. **declared vocabulary over the manifest** — the role/operation registry is declared in code and
   handed to the parser, so a manifest edit fails compilation instead of minting a new role.

The semantic digest is a `\t`-separated canonical document over the seat, operation, repository,
work branch, task reference and document digest, requirement identities, the specializations
**actually composed**, one line per composed block with its revision, one line per requested tool id
in sorted order, one `skill` line per carried reference, and the task context when supplied. Order is
part of identity, not presentation over it. Ten shipped roles compile from disk twice to one digest
each and to ten different digests, so the digest is neither a constant nor order-insensitive.

`layers.toml` places this package in `models` (rank 2) precisely because it holds only
dependency-free value types, canonical source parsing, and selection logic. The contract's declared
target is not yet met tree-wide — the tree reports 16 pre-existing violations, **none** naming a
role-capsule module — so do not present the layer contract as currently satisfied.

## Detailed Route Context

The model layer now carries closed lifecycle generation, legal-control, enclosure, door, successor, termination, direct-landing, and bounded legacy vocabularies while keeping scheduling projection separate.

The closeout input, source, and projection vocabulary now lives under `models/closeout/`. This is a
one-to-one package move of the existing typed contracts, not a compatibility namespace: input owns
accepted plan shape, source owns exact candidate provenance, and projection owns disposable
scheduling facts while journal models retain lifecycle evidence.

`models/closeout/input.py` no longer owns the rendering of the memory-content commit message.
Since 260913-LCA-L4 the one writer is `kernel.memory_attribution.render_memory_content_message`
(kernel/memory_attribution.py:72-97), and `EffectiveCloseoutInput.memory_content_message(code_commit)`
(input.py:148-166) is the closeout-shaped way in to it: the closeout's own message verbatim plus
exactly one final-paragraph `Code-Commit: <sha>` trailer naming the code commit that same closeout
landed. Both closeout routes still render through that wrapper — worktree closeout and the
branch-addressed direct landing — while the prepared memory-content leg, carryover, baseline adoption
and backfill call the kernel renderer directly, so the attribution has a single definition in kernel.
There is no current ledger-only producer: the cache is rebuilt without a commit. Historical commits without attribution contribute no computed mapping.

ACPUI-L2 adds `launch-selection-invalid` to the strict terminal spawn response for an incomplete
role-configured native selection. Existing `resolvedModel`/`resolvedEffort` fields continue to
carry settings provenance, while `sessionCommands` is now explicitly user-authored launch
configuration rather than a normalized model/effort vehicle. Dynamic catalog and process failures
remain hosted control evidence and do not inflate the pre-spawn status enum.

HFX2-L17 adds binding identity to terminal responses: attach can return `role-required` and carries
`seatRole`/`previousSeatRole`; spawn carries `seatRole`. The legacy `role` field still means
transport (`chat` or `terminal`) and is not orchestration identity.

HFX2-L15 extends the terminal spawn response with `replacementForLeaf`, resolved model/effort, and
bound session-log entry/path provenance. Delivery booleans are evidence-specific: context is true
only for the id-bearing user record, and commands require command plus non-error stdout evidence.

Start with `tools/tool_registry.py`: `TOOL_RESPONSE_MODELS` maps every modeled builder
to one response model, while `PUBLIC_TOOL_RESPONSE_MODELS` filters out retained
compatibility builders so it matches `mcp.tools.PUBLIC_TOOLS`. Both are typed
`dict[str, type[ResponseEnvelope]]` (260731-EFA-L4), not `type[BaseModel]`.
`tools/public_roster.py` (260831-LOCR-L32) is the route's zero-import leaf holding the single
definition of the advertised tuple `PUBLIC_TOOLS` (63 ordered names since 260831-LOCR-L37 added
`worktree_pause`; L22-L86); `mcp/tools/base.py`
re-exports the identical object. It lives here because a `models` response model now reads it —
`models/worktree.py` enforces the worktree surface's next-move vocabulary against it — and
`models → mcp` would be a `layers.toml` violation.
`base.py` defines strict response envelopes, intentionally
flexible detail envelopes, token metadata fields, and the strict `NextStep`
lifecycle-hint model carried by an optional `nextStep` field on BOTH envelope
bases (`ResponseModel` and `FlexibleResponseEnvelope`), so every modeled tool
response can surface the computed next move; 260731-EFA-L4 declares the
`supervisorBanner: str | None` stale-supervisor field beside it on both bases and
names their union `ResponseEnvelope`. Domain modules then own
contract slices: `context_packet.py` for compact `ContextPacketV2`,
`providers.py` for provider summaries and diagnostics, `worktree.py` for
worktree context/status responses including `enclosurePath`, `leafId`, and `kind`, `memory.py` for memory/onboarding tools,
`runtime.py` for runtime and resolver tools, `benchmarks.py` for Codex
benchmark tools, `lifecycles/responses.py` for the `lifecycle_*` signal responses
(with `LifecycleStartResponse` also carrying an optional `frontHalfRundown`
front-half roadmap, and the task-28 `LifecycleTurnEndNotificationResponse`
adding a `summary` for the public NOTIFY-AND-CONTINUE turn-end tool),
`task_doc.py` for the `task_doc` authoring response including the optional Task 21 `masterSync`
leaf-to-master result, `gates.py` for
`LifecycleGateResponse`, the public gate decide/list responses, and retained
compatibility gate responses (L4 adds delegated-decision `decidingRole` and
`evidenceRefs` to the decide response), `operator_inbox.py` for the
three `operator_inbox_*` external-chat response contracts (task 10),
`orchestration.py` for the strict `orchestration_nudge_manager` response,
`lifecycles/finalize.py` for the strict terminal task-finalizer response, `terminal.py` for the strict
`attach_terminal_session_to_leaf` hosted-chat/terminal reassignment response AND the L2
`spawn_agent_session` dispatch response (`SpawnAgentSessionResponse` — spawned-by provenance +
context-delivery outcome (since 260707-HFX-L3 incl. the failure-evidence `deliveryCapture` field) + the server-arbitrated `leaf-taken`/pre-spawn refusal statuses; since HFX-L4 the attach/spawn models also accept
`leaf-ref-not-found` / `leaf-ref-ambiguous` refusals with the original `leafKey` and optional detail; since
260703-L16 also the `effort-invalid`/`model-invalid`/`level-invalid` refusals, the free-form spawn
provenance `launchArgs`/`promptKeywords`/`sessionCommands` + `sessionCommandsDelivered`, and the
level provenance `spawnLevel`/`spawnLevelSource`; HFX2-L10 adds the
`spend-override-unsupported` refusal for legacy caller spend fields and maintained harness-native
spend env keys; since 260821-ARSPAWN-L1 also the caller-kind provenance `spawnedByKind`
(`plane|ambient|unattributed`) mirroring the catalog row — the provenance the public `dispatch_agent`
sets by caller kind), and
`tokens.py` for response token accounting. **260707-HFX-L8** adds two more strict models to
`terminal.py`: `SessionRetireResponse` (`retired`/`already-retired`/`unknown-session`/
`unknown-actor`/`retire-refused` statuses, retirement provenance fields, `detail` naming the exact
authority-policy clause on refusal) and `SessionRenameResponse` (`renamed`/`unknown-session`,
`label`/`spawnedLabel` — identity text only, no `spawn_role` field on this response since a rename
never changes it). `lifecycles/finalize.py`'s `LifecycleFinalizeTaskResponse` carries additive
`autoLandedSeats: list[str]` field for the master→super finalize edge's landed archive hook.

## Route Model

- Owned compact contracts should inherit from `StrictResponseModel` or
  `ToolResponse` so unknown fields are rejected.
- Native/detail surfaces that intentionally pass through provider or service
  payloads should inherit from `FlexibleResponseModel` or `FlexibleToolResponse`.
- The strict `NextStep` model (task 27) mirrors the worktree guidance dict shape
  (`summary` plus optional `nextOperation`/`nextTool`/`nextArgs`/`nextRequiredArgs`),
  so an operational hint and a gate-raise share one vocabulary (a gate junction
  is just `nextTool="lifecycle_gate"`). Both envelope bases
  ([base.py](agents-remember/mcp/src/agents_remember/models/base.py)) declare an
  optional `nextStep: NextStep | None` field, populated for in-lifecycle calls at
  the [mcp/tools/base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py)`::_tool_payload`
  choke point and excluded when None, so lifecycle-less calls stay unchanged.
- Both envelope bases also declare `supervisorBanner: str | None` (260731-EFA-L4), set at
  the same choke point. It had been written by the choke point since 260707-HFX2-L2 R5 but
  declared on no model, which is the specific hole: `ResponseModel` is `extra="forbid"`, so
  a response carrying a stale-supervisor banner failed its OWN `model_validate`, and
  `FlexibleResponseEnvelope`'s `extra="allow"` accepted it undeclared — tolerated drift is
  for the PROVIDER's fields, not this package's. `ResponseEnvelope` is the
  `ResponseModel | FlexibleResponseEnvelope` alias naming the two families; the split between
  them is about `extra`, not about the header, and both carry the same
  `ok`/`tokens`/`nextStep`/`supervisorBanner` fields.
- `ContextPacketV2` keeps startup context compact and points detailed provider
  troubleshooting to `provider_diagnostics`.
- Token metadata fields exist on every modeled response; the final S6 wiring
  fills them from the serialized JSON payload.

## Invariants And Boundaries

- Every public MCP tool must have exactly one declared response model in
  `PUBLIC_TOOL_RESPONSE_MODELS`; every retained compatibility builder that still
  returns through `_tool_payload` must have one in `TOOL_RESPONSE_MODELS`.
- **The advertised tuple, the live FastMCP registration, and this registry are three separately
  declared artifacts** (260831-LOCR-L29). `finalize_tool_response` indexes
  `TOOL_RESPONSE_MODELS` by tool name, so an advertised name with no registry row raises instead of
  returning a payload. Compare all three from a live probe server —
  `mcp/tests/test_tools.py::PublicSurfaceInventoryTests` is that executor. Do not treat the
  `server_info` payload as surface authority: it reports `mcp.tools.PUBLIC_TOOLS` itself, so
  comparing it to the tuple is self-referential.
- Do not rely on Pydantic to silently coerce nested raw dictionaries for owned
  contract objects. Construct nested models explicitly, or call
  `NestedModel.model_validate(...)` only at a narrow raw-adapter boundary.
- Keep `context_packet` free of `rawStatus` and duplicate top-level
  `pathRules`; detailed provider state belongs in `provider_diagnostics`.
- Nullable response fields that can be omitted after `exclude_none=True` must
  declare optional defaults (`= None`); otherwise a later public payload
  validation pass treats the missing key as a required-field error.
- Flexible models are for intentionally raw/detail payloads, not a shortcut for
  avoiding a stable public contract.
- **A wire vocabulary is IMPORTED from whoever produces it; it is never retyped on this
  route** (260731-EFA-L4). A hand-copied `Literal` beside a producer's own is a set that can
  only be compared against the producer when a real payload carries the new member — which
  happens as a `ValidationError` raised inside an `@server.tool()` handler that has no
  `except` for one. Nested `Literal` aliases flatten under PEP 586, so folding a producer's
  alias into a longer list (`Literal["attached", ..., LeafRefStatus]`) publishes exactly the
  same enum it did when the members were spelled out. Where the producing module cannot be
  imported without a cycle, the vocabulary is declared HERE and the producer imports it (see
  `terminal.py` below) — one declaration is the invariant; a particular module owning it is
  not.
- **Nothing on this route declares a status a producer cannot emit, or omits one it can.**
  The historical wire-vocabulary suite measured produced-vs-declared in both
  directions and is the suite to extend when a new status appears.
- **Nothing on this route may reach the network while the package is importing.**
  `tokens.py` builds `DEFAULT_TOKEN_COUNTER = TiktokenTokenCounter()` at module
  scope, and `mcp/tools/base.py` imports `finalize_payload_tokens` from it — so
  that construction runs on the server's startup path, and anything it touches
  runs there too. Adding a second `tiktoken` encoding therefore means
  vendoring its vocabulary too — `vendored_vocabulary_cache` raises
  `TokenizerVocabularyError` (`errors.py`) for any name other than
  `VENDORED_ENCODING_NAME` rather than letting `tiktoken` download it.
- **A vendored vocabulary is verified by this route before `tiktoken` is pointed at
  it, never afterwards.** `_verify_vendored_vocabulary` hashes the file against
  `VENDORED_VOCABULARY_SHA256` and raises for absent, unshipped, *or byte-wrong*;
  only then does `vendored_vocabulary_cache` set `TIKTOKEN_CACHE_DIR`, and only to
  the verified file's own parent directory. Delegating the check to `tiktoken` is not
  equivalent and must not be "simplified" back: `tiktoken.load.read_file_cached`
  checks the same digest but answers a mismatch by deleting the file and downloading
  a replacement over it — inside an installed package that is a startup fetch plus a
  rewrite of the installed tree, or a `PermissionError` on a read-only install.
- Tools whose bulk moved to `temp/tool-reports/` (2.5.1: runtime install,
  provider diagnostics/watchers; 2.5.2: carryover plan/apply) document the
  compact wire fields as optional declared fields on their flexible models —
  `reportPath` everywhere, plus the per-tool digests (rebind `phases`,
  carryover `decisions`/`carriedPaths`) — so the compact shape is discoverable
  from the model even though the envelope stays flexible.

L14: the task-doc node model exposes the optional `orchestrates` list and the sessions wire model carries the optional `spawnRole` — both additive, absent on old payloads.

## Evidence

### Repo-Internal References

- Public MCP payload builders validate through the response model registry. [67]
- The advertised public roster's single definition, in this route's zero-import `tools/` leaf; the adapter re-exports the identical object. [68]
- The response model that reads the roster to enforce the worktree surface's next move against `PUBLIC_TOOLS`. [69]
- The registry maps every modeled builder and the advertised public subset to response models. [70]
- Contract tests prove public tool coverage and schema generation. [71]
- The record-landing envelope is declared on this route. [72]
- The checkpoint-landing envelope is declared on this route. [73]
- The checkpoint registry row sits between the integrate and record-landing rows; the record-landing row follows it. [74]
- Curator coherence keeps semantic revision, attempt, immutable record, stable authority, snapshot, and action request identities separate and exact. [75]
- Operator inbox response models cover post, poll, consume, and hosted-delivery metadata. [76]
- Contract tests prove public tool coverage and schema generation. [77]
- Orchestration response models cover the public manager-nudge helper. [78]
- Lifecycle finalizer response model covers the terminal task finalization payload. [79]
- Terminal response models cover trusted task-seat assignment and internal hosted-session spawn. [80]
- The next-step engine that fills `nextStep` from the active lifecycle. [81]
- The wire-test module documents the 165-of-213 `context_packet` baseline. [82]
- The worktree model declares the contract-cell vocabulary aliases (moved from worktrees by 260731-EFA-L9) with `MemoryMode` imported from kernel. [83]
- The worktree model declares the phase/next-operation/next-tool vocabulary (moved from guidance by L9). [84]
- Guidance consumes the phase/next-operation/next-tool aliases declared by the wire model through one grouped import. [85]
- The drift-status vocabulary and `DriftSummaryPacket` that `drift.py` and `memory.py` import. [86]

Current working-candidate evidence for this route:

- Direct landing returns cache observations separately from commits. [87]
- Public message transport names only code and memory. [88]
- None [89]

### 260821-ARSPAWN-L2 Stable Structural Evidence

`TerminalCatalogEntry.dispatch_brief_entry_id` is private durable reconciliation evidence, not a
structural address. It may be serialized for control-plane recovery and dashboard diagnostics.
The receipt survives promotion of a staged heir into the same document-and-role seat, but clears
when document or role changes. Promotion also clears the replacement reference so one row cannot
remain in both seat generations.

`StructuralOutcome` projects operation, status, canonical task document, role, detail, and
delivery state while deliberately excluding runtime occupant identity.

## 260712-TRH-L4 Route Impact

Models now distinguish spawned-unbriefed, harness-ready, and briefed and carry the readiness/dispatch statuses, exact-session proof fields, dispatch kind, and separated supervisor state surface.

### 260713-PHA-L5 Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## 260731-EFA-L3 Route Impact — `tokens.py` Counts Offline

The token counter no longer downloads its vocabulary. `TiktokenTokenCounter.__post_init__` used to
call `tiktoken.get_encoding("o200k_base")` bare, which on a cold cache fetched
`o200k_base.tiktoken` from `openaipublic.blob.core.windows.net` — and because
`DEFAULT_TOKEN_COUNTER = TiktokenTokenCounter()` is built at module scope on the import path of
every MCP tool, that HTTPS round trip happened *while the server was starting*. A fresh container,
an offline machine or a hermetic CI job could not start the server at all.

The vocabulary now ships inside the package at
`agents_remember/package_data/tiktoken/fb374d419588a4632f3f557e76b4b70aebbca790`. That file name is
not decoration: `tiktoken.load.read_file_cached` keys its cache on `sha1(url)`, so it is the only
name a cache hit can have, and `vendored_vocabulary_path()` recomputes it from
`VENDORED_VOCABULARY_URL` rather than hard-coding the digest — the shipped file and the download it
replaces stay provably the same thing. `__post_init__` now loads inside
`vendored_vocabulary_cache(self.encodingName)`, which points `TIKTOKEN_CACHE_DIR` at the vendored
directory for the duration of that one load, under `_CACHE_DIR_LOCK`, and restores
the operator's previous value afterwards. Scoped rather than exported, because the vendored
directory sits inside an installed (usually read-only) package and any *other* encoding loaded later
in the process would try to write its download there. The operator's own `TIKTOKEN_CACHE_DIR` is
deliberately overridden rather than honoured — theirs may be cold, and honouring a cold one is
exactly the download this exists to remove.

**The route verifies the vocabulary itself, before tiktoken is told where to look.**
`vendored_vocabulary_cache` calls the private `_verify_vendored_vocabulary(encoding_name)` as its
first statement — ahead of the lock and ahead of any environment mutation — and that helper raises
`TokenizerVocabularyError` in three cases: an encoding this package does not ship, an absent file,
and a file whose SHA-256 does not equal `VENDORED_VOCABULARY_SHA256`. It then hands back the
verified path, and only *that file's own parent directory* is ever exported, so tiktoken cannot be
pointed at a directory whose contents were not checked.

Leaving the digest to tiktoken is not the same thing, and the difference is the whole point.
tiktoken checks the same SHA-256, but it does **not** fail closed on a mismatch:
`tiktoken.load.read_file_cached` deletes the offending cached file and downloads a replacement over
it. Pointed at this package's directory, that turns a corrupt vendored copy into a silent network
fetch on the server's startup path *and* a rewrite of the installed tree — or, on the read-only
install this module is written for, into a `PermissionError` from the write-back instead of the
designed refusal. Checking first is what makes corruption behave like absence. `VENDORED_VOCABULARY_SHA256`
is restated here rather than imported, and that is not a second source of truth:
`mcp/tests/test_cold_start.py` re-derives it from the installed tiktoken, so a release that changes
what tiktoken asks for fails there. Hashing costs one full read of 3.6 MB per counter construction,
which in the server is once per process.

`_CACHE_DIR_LOCK` is a `threading.RLock`, not a `Lock`, because the guarded region spans the `yield`
in an exported context manager. The obvious use of one —
`with vendored_vocabulary_cache(name): TiktokenTokenCounter()` — has the counter's own load re-enter
the manager on the same thread, which on a non-reentrant lock is a permanent hang with no timeout
and no traceback rather than a wrong answer. The lock's honest scope is "the counters this package
builds": `TIKTOKEN_CACHE_DIR` is process-global and belongs to tiktoken, so a thread that reads or
writes it without coming through here can still observe or clobber the override, and nothing at this
layer can prevent that.

Nothing about the response contract changed: the shipped bytes are the download's bytes, so counts
are the same numbers and `name` still reports
`tiktoken:o200k_base`. There is deliberately no approximate fallback — a fallback would make a
reported count depend on whether the machine that produced it had egress, silently mixing exact and
estimated values inside one dashboard aggregate. A vendored file that is missing **or present with
the wrong bytes** raises `TokenizerVocabularyError` instead, naming both the expected and the found
digest, so a build that failed to ship it — or a `core.autocrlf=true` checkout that rewrote its line
endings — says so at startup rather than working only where the network happens to be reachable.

## 260731-EFA-L4 Route Impact — Vocabularies Come From Their Producers

Every change here has the same shape: a `Literal` this route had typed out by hand, standing
beside the module that actually produces those values, replaced by an import of the producer's
own alias. The failure mode being removed is a **set difference**, and it lands as a
`ValidationError` raised inside an MCP tool handler with no `except` for one.

**`worktree.py` — six copies, six drifts, 165 of 213 contracts.** `WorktreeSummary`'s
vocabularies were all local `Literal`s. They now come from
`worktrees.worktree_contract` (`WorkflowKind`, `MemoryMode`, `HumanReviewStatus`,
`IntegrationStatus`, `CleanupStatus`, and `CloseoutStatus` aliased to the published wire name
`LifecycleStatus`) and `worktrees.modules.guidance` (`WorktreePhase`, `NextOperation`,
`NextTool`). Only `WorktreeState` stays local — it is produced entirely inside
`application.worktree_status`, which constructs the model directly, so the checker already sees a single
writer. What the copies had missed is checkable against the producers: the local
`WorkflowKind` was `Literal["chat", "light", "light-task"]` while the contract's is
`Literal["chat-task", "light-task"]` — the copy did not contain the kind `worktree_start`'s own
docstring advertises and had two members the contract cannot write; local `CleanupStatus` lacked
`reopened`; local `WorktreePhase` lacked `carryover-pending` and `abandoned`; local
`NextOperation` lacked `request_carryover_decision`; local `NextTool` lacked
`memory_carryover_apply`. Measured effect, recorded in
`test_wire_vocabulary_exhaustiveness.py`'s docstring: 165 of the 213 `series-contract.md` files
on disk (77.5%) made `context_packet` raise, across seven independent gaps. Two additive
optional fields join the summary: `nextRequiredArgs` gains a documented absent-means-nothing-
required reading (the producer writes the key only when there is a required argument, and the
projection reports what the producer said rather than substituting `[]`), and
`unknownContractCells: list[str] | None` reports `"<field>=<raw token> read as <fallback>"` for
any contract cell outside its declared vocabulary — the file still projects as `active` with
substituted values, and heals the next time a lifecycle tool writes it.

**`context_packet.py` — three retyped vocabularies.** `RepoSummary.state` takes
`kernel.git_facts.RepoState` and `BranchFreshness.state` takes
`kernel.git_freshness.FreshnessState`, both of which are assembled here through
`model_validate` of an untyped dict, so a copy would be measured against the producer only
when a real degrade path fired. `MemorySummary.mode` moves from `Literal["internal",
"external"]` to `worktrees.worktree_contract.MemoryMode`, which has always included
`disabled` — `WorktreeSummary` in the SAME response already declared it, so one packet could
pass `memoryMode="disabled"` and fail `memory.mode` on the same value.

**`drift.py` / `memory.py` — one vocabulary, three declarations, two of them short.**
`DriftStatus` now lives once, in
`memory_quality/integrity/onboarding_drift_check/models.py` beside `run_drift_summary` which
produces it, and both wire models import it. `models.drift.DriftStatus` had been
`Literal["notChecked", "checked"]` and `DriftSummary` declared no `error` field, while
`run_drift_summary` returns `{"status": "error", "error": ...}` whenever the onboarding root is
missing — so `include_drift=true` against a repo without onboarding raised out of the tool on
the status *and* the key, i.e. the diagnostic crashed on exactly the call meant to explain the
problem. `DriftSummary` gains `error: str | None`. `models.memory.DriftCheckStatus` was the
third copy (correct, but a third place for the next member not to arrive) and is gone.

**`read_files.py` — the alias moved to the decider.** `FileReadStatus` is declared in
`application/read_files.py`, where `_resolve_onboarding` decides it and now returns it as its
annotated type, and this model imports it. Note the direction: this is a `models/` →
`application/` import, the reverse of the usual layering, chosen because the deciding function
is the single writer and it puts the value into an untyped payload dict. It creates no cycle —
`application/read_files.py` does not import `models.read_files`.

**`terminal.py` — folded members and runtime halves.** `LeafAssignmentStatus` and
`SpawnAgentSessionStatus` fold in `worktrees.leaf_refs.LeafRefStatus` (the pair
`leaf-ref-not-found`/`leaf-ref-ambiguous`) instead of respelling it; `Literal` flattening means
the published enums are unchanged (`get_args(LeafAssignmentStatus)` is still the same six
members). The three terminal vocabularies stay declared HERE rather than beside the payload
builders that write them, and the module says why: `mcp.tools.base` → `models.tools.tool_registry` →
`models.terminal` is an existing import edge, so a `models.terminal` → `mcp.tools.terminal`
import would close a cycle. The invariant is one declaration, not a particular owner —
`mcp.tools.terminal` imports these aliases and annotates its status seams with them.
`VALID_SPAWN_AGENT_SESSION_STATUSES`, `VALID_SESSION_RETIRE_STATUSES` and
`VALID_SESSION_RENAME_STATUSES` are `frozenset(get_args(...))` of their aliases — the runtime
half derived from the type rather than typed beside it.

**`tools/tool_registry.py` — the loose type that made the token count wrong.** Both registries are
`dict[str, type[ResponseEnvelope]]`. Under the previous `dict[str, type[BaseModel]]`,
`TOOL_RESPONSE_MODELS[tool].model_validate(payload)` was typed as a bare `BaseModel`, on which
`nextStep` and `supervisorBanner` are not attributes a checker knows — so the choke point had
no type-clean way to set them on the validated response, and wrote them into the dict AFTER
`model_dump` and AFTER `finalize_payload_tokens`. Two consequences, both silent: the served
response carried bytes the advertised `tokens` did not count, and `supervisorBanner` was a key
on an object whose model did not declare it. Naming the union is what let the choke point be
reordered (see the `mcp/tools/` overview). Verified: all 62 registered models are
`ResponseModel` or `FlexibleResponseEnvelope` subclasses and all 62 declare both fields, so the
narrower type is true of the whole registry today.

## 260731-EFA-L9 Route Impact — Conversation Wire Models Join This Route

The route now owns more than MCP response contracts. 260731-EFA-L9 moved the stable
conversation/evidence/control-wire grammar out of `serving/` into the new
`models/conversations/` child route (16 responsibility-owned modules + curated `__init__.py`
export surface), moved the terminal-catalog row vocabulary into `models/terminal_catalog.py`,
and added the task-document wire vocabulary in `models/task_document.py`. The route model is
unchanged in kind — strict owned contracts, curated exports — but the wire surface it governs is
now shared by serving projectors/control and the response-model registry. `models/__init__.py`
re-exports the curated conversation surface (R6); no forwarding shims exist at the old serving
paths.

## L23 Source-Lineage Contract

The model layer now owns closed lineage relation, side, edge-state, aggregate
state, recovery, and terminal refusal vocabularies. Worktree, terminal, observer,
and dashboard consumers import or mirror this strict shape instead of accepting
free strings or agent-supplied identity.

## 260815-DAG-L3 Queue Models

`models/closeout_queue.py` adds the strict action-specific request, categorical scheduling grade,
exact evidence facts, candidate state machine, atomic blocker, bounded canonical queue state, and
ready/waiting/blocked/in-flight response projection. Every persisted/public text and collection is
bounded, impossible state/owner/commit combinations fail validation, external memory requires exact
evidence while internal/disabled use a typed not-applicable state, and only a one-way lifecycle
owner fingerprint reaches durable state. Since 260815-DAG-L13 `LANE_OCCUPYING_STATES` narrows the
landing lane to selected/closeout-in-flight/integration-in-flight candidates (a certified candidate
no longer occupies it), and the response carries the scheduling readout fields (`mode`,
`registers`, `laneOwner`, `legalNextOperations`, `acquisitionFacts`). Shared `TaskDocumentRef` values enforce their repository
and path bounds after canonical normalization, avoiding JSON Schema constraints that the generated
TypeScript projection could not express truthfully.

## 260815-DAG-L4 L4 Durable Authority Models

Worktree, closeout-queue, and task projections now distinguish organizational direct-super lineage from atomic series lineage and carry exact configured repository, ref, candidate, recovery, and conflict-transaction facts required by the mutation plane.

## 260815-DAG-L15 Route Impact

`MemoryQualityCheckResponse` gained the optional async `status`/`runId` run envelope (L15-R7); the synchronous response shape is unchanged.

## 260815-DAG Master Full-Gate Repair Route Impact

`models/closeout_queue.py` moved to the new `models/queue/` sub-route; `models/task_doc.py` `TaskDocResponse` gained the special-op wire fields (the strict-envelope rejection fix).

## 260821-CLIVE-L1 Closeout Vocabulary

`closeout_input.py` adds the raw-message, resolved-plan, enabled/not-applicable leg, structured-refusal, and effective-input vocabulary shared by both closeout routes. Public worktree and direct-landing responses expose that vocabulary. Lifecycle operation records use only the normalized form; no generated subject, blank sentinel, or fallback input remains below validation.

## 260821-CLIVE-L2 Historical Intermediate Architecture

Models validate immutable identity and contradictory evidence but perform no I/O or recovery.
`models.lifecycles` owns the canonical root-journal vocabulary. The transitional L2
selected/in-flight/certified queue schema was removed by L3; `models.queue` now exposes only the
disposable waiting-door projection request/response contract, while
`models.closeout_projection` owns its strict projection vocabulary.

Registered tool request/response contracts now live under `models/tools/`; the move removes the former flat paths without changing the registry's ownership or creating compatibility exports.

### Reconciled Source Evidence

- Strict lifecycle operation record/projection. [90]
- Queue candidate projection. [91]

## 260821-DAGQC-L2 Closed Quality And Landing Models

The route adds strict discriminated memory-quality request DTOs and the shared
`QualityGateResult`/memory-policy models. Closeout and integration no longer expose open quality
mappings, and stable versus immutable result paths remain distinct. Direct landing keeps exactly
three top-level outcomes; journal lifecycle evidence is nested.

## 260824-PDLS — Python Test Evidence Model

`test_evidence.py` adds a closed diagnostic/certifying altitude and consumer vocabulary.
Diagnostic evidence carries exact nodes, exit code, and a structural candidate binding;
certifying evidence has no public constructor and is minted only from a verified immutable Dagger
generation. Coverage, quality, retry, route review, lifecycle, closeout, and integration require
the certifying type, keeping acceptance impossible to express as a generic payload flag.

## 260824-PDLS Final Model Reconciliation

The evidence models close authority, lifetime, cadence, and result vocabularies for diagnostic and
certifying lanes, while lifecycle models retain strict journal-owned mutation proof. Projection
invalidation removes the impossible `not-created` outcome, and validator decomposition preserves
one typed public contract instead of distributing failure-family knowledge across callers.

## MCAR-L03 Pair Identity Models

`memory_candidate.py` owns the frozen exact-pair schema. Memory-quality, curator-coherence, and
closeout response models reference that schema rather than copying its fields. Semantic
requirement versions, delivery attempts, candidate trees, and pair identity remain separate
contracts.

## Status-Change Wait Response

`models/worktree.py` still owns `WorktreeStatusWaitResponse`, but `models/tools/tool_registry.py`
no longer registers it: the `worktree_status_wait` tool was removed from the public surface, so the
response class is currently unregistered and unreferenced anywhere in the tree. It carries a typed
outcome, optional successor generation and meaningful revision, elapsed/timeout observations, and
the coherent lifecycle projection. It introduces no public worker PID or private operation key.

- The read-only wait response exposes outcomes and cursors without private worker authority. [92]
- Public response registration no longer carries the dedicated wait response: `worktree_status_wait` is absent from `TOOL_RESPONSE_MODELS`, so `WorktreeStatusWaitResponse` stays defined in `models/worktree.py` with no registered tool. [93]

## Integrated IAS Recovery Contract

The changed lifecycle preparation model retains original command ownership and append-only terminal observations through focused validation helpers. Runtime composition and physical Git proof remain outside models. The retained `test_wire_vocabulary_exhaustiveness.py` is now support code without collected test functions; its historical census and deleted cases must not be read as current exhaustive protection.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.

## 260831-LOCR-L30 Checkpoint-Landing Wire Model

`models/worktree.py` gains `WorktreeCheckpointLandingResponse` (operation literal
`worktree_checkpoint_landing`, carrying `integrationStrategy`, `integratedCodeCommit`,
`integratedMemoryContentCommit`), `IntegrationStatus` gains the
`checkpointed` member, and `models/tools/tool_registry.py` registers the new envelope between
`worktree_integrate` and `worktree_record_landing`.

This is the same invariant the L29 section below states, satisfied a second time — and the second
landing envelope is why the registry cannot be checked as a set alone. The two tools sit adjacent in
the registry and their payloads differ only in the operation literal, so a swap between them would
still validate as a set. `mcp/tests/test_tools.py::PublicSurfaceInventoryTests` drives one
`finalize_tool_response` call per name for that reason.

**260831-LOCR-L34** adds `worktree_checkpoint_landing` to the `NextTool` vocabulary
cit:([`NextTool`], mcp/src/agents_remember/models/worktree.py:65-87) — the checkpoint's preview and its
`integration-ref-race` refusal both emit it, and it is a registered public tool — while deliberately
leaving `NextOperation` unchanged, because pausing a master is the existing
`request_integration_decision` intent rather than a lifecycle phase. The reasoning and the
reviewed-and-not-changed row live on the `models/worktree.py` card; the preview/apply parity invariant
that produced the repair is inventoried on the `worktrees/overview.md` route.

## 260831-LOCR-L29 Public-Surface Repair

`models/worktree.py` gains `WorktreeRecordLandingResponse` (operation literal
`worktree_record_landing`, carrying `integrationStrategy`, `landedCodeCommit`, and
`landingTargets`), and `models/tools/tool_registry.py` registers it immediately after
`worktree_integrate`. This route overview also governs `models/tools/`, which has no nested
overview of its own.

The route already stated the invariant — every advertised MCP tool has exactly one declared
response model — and this is the route where it can be violated invisibly. `finalize_tool_response`
indexes `TOOL_RESPONSE_MODELS` by tool name, so a tool that `mcp/registration/closeout.py` registers
is published by FastMCP while the missing row makes its own response lookup raise. The tool was
advertised and unable to return a payload, and the suite stayed green: `server_info` reports
`PUBLIC_TOOLS` itself, so the only comparison available was self-referential.

The matching census row landed in `mcp/tools/base.py` (61 advertised names at that leaf — 62 since
260831-LOCR-L30 — with `worktree_record_landing` immediately after `worktree_integrate`), and the
invariant now has an executor in
`mcp/tests/test_tools.py::PublicSurfaceInventoryTests`, which compares the live registration order
to that tuple and drives one `finalize_tool_response` call for the repaired name.

## 260831-LOCR-L32 The Public Roster Joins This Route, And The Worktree Next Move Is Enforced

This route's `tools/` leaf gained `public_roster.py` — a zero-import module whose whole body is the
`PUBLIC_TOOLS` literal
cit:([`PUBLIC_TOOLS`], mcp/src/agents_remember/models/tools/public_roster.py:22-97) — **62 names at this
leaf, 63 from 260831-LOCR-L37, and 66 since 260915-CAPS-L4**. It is the tuple's **single definition**; `mcp/tools/base.py`
now re-exports that identical object instead of declaring its own, so
`agents_remember.mcp.tools.PUBLIC_TOOLS`, `PUBLIC_TOOL_RESPONSE_MODELS`, the live registration order,
and the `public_surface` pin all still name the same tuple with no consumer change.

The roster lives here because a model needs to read it. `models/worktree.py::WorktreeCommandResponse`
now declares `nextAction` / `nextTool` / `nextArgs`
cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-400) and refuses a `nextTool` outside
  cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-400) and refuses a `nextTool` outside
`PUBLIC_TOOLS` through `_require_registered_public_next_tool`
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442). Before this leaf the
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442). Before this leaf the
cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-400) and refuses a `nextTool` outside
envelope inherited `extra="allow"` and declared none of those keys, so
`application/worktree_status.py::_project_terminal_contract_status`'s write crossed the wire verbatim
and unchecked — `worktree_abandon` reached the wire as a `nextTool` without ever being a `NextTool`
member. `models → mcp` would be a `layers.toml` violation (models = 2, mcp = 22), a function-local
import trips `ruff PLC0415`, and module-level imports in either direction are circular — so the tuple's
move into this route is the precondition of the fix, not a companion cleanup. The layering checker
returned to its exact baseline of 16 violations with no `models → mcp` edge and no new cycle.

**The invariant is per surface.** The worktree surface's next move must name a registered *public*
tool; the `task_doc` surface may name the registered-but-non-public `session_retire`
(`TaskDocResponse` is not a `WorktreeCommandResponse`). Do not widen `PUBLIC_TOOLS` to cover it.

## 260831-LOCR-L36 The Activation Vocabulary Becomes Contract-Scoped

The atomic-series activation record was re-keyed from the protected source pair to the canonical
series contract, and this route's wire models moved with it. Two atomic masters commanded by one
sprint derive the *same* protected pair (same code repository/branch and memory repository/branch;
only the work branches differ), so a one-record-per-pair store made the second master's selection
replace the first. `models/structural/atomic_series_activation.py` is now 45 lines and declares only
`AtomicSeriesActivationRecord` (16) and `AtomicSeriesActivationArchiveEvidence` (30), both
`schemaVersion "2.0"` with `contractFingerprint`.

On the worktree wire vocabulary (`models/worktree.py`, 514 lines):

- `AtomicSeriesActivationFact.contractFingerprint` replaces `sourcePairFingerprint`, so status
  evidence names the contract whose record was read.
- `AtomicSeriesAdmissionActivation.contractFingerprint` replaces `sourcePairFingerprint`.
- `AtomicSeriesAdmission` lost `classification`, `sourcePair`, `sourcePairFingerprint` and `blocking`,
  and gained `contractFingerprint`. The `AtomicSeriesAdmissionBlocking` model was deleted, so a
  foreign live master is no longer expressible as this contract's blocker or retry precondition.
- No model on this route declares `AtomicSeriesSourceRef` / `AtomicSeriesSourcePair`.

The wait vocabulary narrowed with it: the activation domain now returns only
`atomic-series-reconciling`, so a vacant record and another master's active selection are never
waiting reasons. Real wave dependencies still gate through the sprint execution graph's own
`predecessor-incomplete:` reasons, and everything under `worktrees/integration/**` is untouched by
this change.

## 260915-KS-L1 Knowledge Vocabulary

## 260915-CAPS-L4 The Capsule And Skill-Resource Wire Contracts

This route gained one sub-route of nine modules, `models/knowledge/`, and no authority. It is the shared
vocabulary of the experimental knowledge substrate: repository namespace identity, invariant identity and the
immutable revision aggregate, the sealed-payload digest, the provenance envelope, the source identity and locator
union, the typed operation/refusal/result contract, and the schema identity.
This route gained two modules that own the AR MCP surface's wire vocabulary for the capsule operation
and the SEP-2640 skills transport. Both are value modules: dataclasses or strict response models plus
their rendering, with no behavior that decides a selection, a permission or a trust level.

Three ownership rules are the reason it lives here rather than in the store that writes it:
- `role_capsule_resources.py` — the three strict response envelopes (`role_capsule_compile`,
  `skill_catalog_list`, `skill_catalog_read`) and their nested payloads, plus the bridge-name and
  `server-supplied-data` trust constants. The capsule envelope carries **both** shapes: `ok` false plus
  a typed `refusalStatus` is a refusal, not an error type, and the identity/provenance fields are
  optional precisely because a refusal legitimately carries only what was established before it
  refused.
- `skill_resources.py` — the discovery registry (`SkillResourceEntry`, `SkillResourceFile`,
  `SkillResourceCatalog`, `UnreadableSkill`), the **SEP-2640 entry shape**
  (`{uri, frontmatter, resources:[{uri,digest,size}]}`), this server's own Agent Skills discovery index,
  and the `_meta` provenance block. Identity is `origin` + name, which is what keeps two servers serving
  a same-named skill distinct. `entry_documents()` is the **enumeration surface** the `skills/list`
  method returns; `discovery_metadata()` is what this server's own listing tools hand out; neither can
  reach a file body.

- **Literal vocabularies are defined where they decide.** `KnowledgeState` (`proposed`/`accepted`),
  `KnowledgeOperation`, `KnowledgeRefusalCode`, `REVISION_PAYLOAD_VERSION` and `KNOWLEDGE_SCHEMA_NAME` are declared
  in their owning model and imported by the decider — never declared by the decider and re-exported downward.
- **Values, not rows.** `KnowledgeModel` is frozen with `extra="forbid"`, which makes the process-local value
  immutable; refusing an update to a stored revision is a storage rule enforced by schema triggers and the
  operation's preconditions, not by model immutability.
- **Identity is not a label.** Display version and display label are separated from immutable identity, so two
  successors of one revision may both display `v2` and both stay addressable. `RevisionDraft` deliberately has no
  `payload_digest` field: the store recomputes the seal rather than accepting it.
Two vocabulary facts that belong at route level, because they are the route's own
"defined here, imported by whoever decides it" rule applied to a security property:

`Authorship` and the `SourceLocator` union are declared **shared**: they are the vocabulary the selective
read/diff contributor (KS-R07/KS-R08) is expected to consume, and the locator union is discriminated on `kind` so
that consumer needs no second locator vocabulary. That consumer does not exist yet; nothing here claims it does.
The blob identity is a Git object identity, not a copy of the bytes — there is no second content store.
- **`contentTrust` is a stated constant, not an inferred or settable field**, and
  **`declaredAllowedTools` is an observation, never a grant** — a host MUST NOT honor mechanisms
  declared in skill content, and no field on these models is a channel through which it could. The
  leaf's mutation probe removes the related guarantee on the admitted-policy side (`M2`) and its named
  case fails.
- **`requestedTools` and `grantedTools` are separate fields on the capsule envelope.** The compiler
  narrows every request against the admitted policy snapshot; keeping both on the wire is what makes
  that narrowing auditable rather than invisible.

Validation vocabulary matters as much as shape: `normalized_uuid` refuses a non-canonical identifier spelling
instead of rewriting it, `Authorship` requires a normalized-UTC `recorded_at`, and `SourceAnchor` refuses an
absolute, backslash, UNC or parent-escaping path so a stored record never carries one.
A third fact, added by the post-rejection repairs and worth carrying here because it is a wire-shape
decision rather than a reader's choice: **the entry's `frontmatter` is the verbatim `SKILL.md`
frontmatter, not a two-field summary.** SEP-2640 §Enumeration requires *"every field the author wrote,
not a curated subset"*, so `SkillResourceEntry.frontmatter` carries the whole YAML map the reader
produced, and `license`, `metadata` and future specification fields pass through unchanged. A nested
skill is published flat: an ordinary entry whose `uri` merely shares a path prefix with its parent's.

Both modules import nothing from `mcp` — the same `models` rank constraint this route's
`tools/public_roster.py` records. The protocol methods that consume these values live on the `mcp`
route (`registration/skills_extension.py`), which is the correct direction for this rank.

- The served knowledge vocabulary as an explicit re-export list — re-cited against the working tree, which the graph half extended. [94]
- The frozen base and the refusal to rewrite a non-canonical identifier. [95]
- The invariant identity and revision aggregate, including the display-label-versus-identity separation. [96]
- The sealed payload, with the predecessor set inside the digest and the digest field excluded. [97]
- The provenance envelope and its normalized-UTC requirement. [98]
- The shared source identity, locator union and the relative-POSIX-path rule — now split into the draft and the stored anchor, with a real `UUID` identity. [99]
- The typed operation, refusal-code and result contract — re-cited against the working tree, which the graph, candidate-change, snapshot, merge, authored-judgment and detection halves have each extended since. [100]
- The invariant-creation result whose `operation` field names the operation that produced it. [101]
- The storage owner that writes this vocabulary. [102]
The later requirement packets the shared envelope and locator are declared for: requirement packets `KS-R07` and `KS-R08`, which live in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address them.
- The capsule envelope keeps one shape for success and refusal, with the seat facts it established. [103]
- The requested-versus-granted split that makes the compiler's narrowing auditable. [104]
- Identity is origin plus name, and a listing cannot reach a body. [105]
- The trust statement is a constant and a declared tool set is observed, never applied. [106]
- The three registry rows that make the new names returnable. [107]

## 260915-KS-L2 The Graph Vocabulary, And The Repaired Anchor Identity

## 260915-CAPS-L7 The Eve Capsule Carrier Format

This route's knowledge sub-route grew from nine modules to eleven and the vocabulary it serves now covers the
**graph**: `family.py` carries family identity and the immutable family revision, and `graph.py` carries the two
relations and the read models both directions answer with. Four of the nine L1 modules changed, three of them
substantively.
This route gained `eve_capsule_carrier.py`, which owns the **format** of the one value AR hands a pinned
eve runtime before it executes. The launch environment can carry a reference and a digest but not the
compiled instructions, so the content travels as a file whose bytes that digest addresses.

The three graph-vocabulary rules, each the model-level half of a storage contract:
It owns the format and nothing else — it parses bytes it is handed and computes digests over them, with
**no filesystem import by design**. Reading the file, writing it and deciding whether a launch may
proceed belong to the tiers that own those surfaces, and that separation is what lets one shape serve
the compiler side (`application`) and the launch side (`serving`) with neither importing the other.

- **A guarantee is the family's own text.** `FamilyRevisionDraft` carries the joint guarantee and never composes
  it from its members, and its `payload_digest` seals the whole aggregate including the sorted predecessor set, so
  a changed guarantee is a separately identified successor.
- **A draft carries no seal, and the anchor draft carries no provenance.** `FamilyMemberDraft`,
  `RealizationClaimDraft` and `FamilyRevisionDraft` have no row digest, and `SourceAnchorDraft` has no
  `provenance` field; the store computes the first and the admitted application attaches the second.
- **A role is an authored claim.** `RealizationRole` is a closed vocabulary with an explicit `unclassified`
  member, so a missing role is representable as "not classified" rather than silently defaulted to a real one,
  and no reader infers a role or a rationale from the source.
Four properties are enforced here rather than trusted, all at parse time:

**The repaired anchor identity is a correction to the L1 vocabulary, not a new feature.** `SourceAnchor.anchor_id`
was declared `anchor_id: UUID = Field(pattern=UUID_PATTERN)`, and Pydantic refuses to apply a string `pattern`
constraint to its UUID schema, so **every** anchor construction raised
`TypeError: Unable to apply constraint 'pattern' … for schema of type 'uuid'` — the class was unconstructible, and
it stayed latent because no L1 test constructed one. The field is now a plain `UUID` and the canonical stored text
is derived at the storage boundary (`records.anchor_row` writes `str(anchor.anchor_id)`), exactly as it is for an
authorship operation identity. The same change split `SourceAnchor` into the draft (what the author decided) and
the stored record (the draft plus the provenance envelope), which is what keeps provenance out of a caller's hands.
The lesson a future reader should take is narrow and reusable: on an identifier field, a `pattern`-constrained
string and a parsed `UUID` are not interchangeable spellings — one of them is unconstructible.
- **Self-describing identity** — `EveCapsuleIdentity` names the seat it belongs to, so a carrier left
  over from another seat is refused by `require_identity` instead of applied.
- **The digest is over the exact bytes on disk**, so a carrier edited after it was written is refused.
- **Every consumer-needed field is required**, so a truncated or hand-written carrier fails naming the
  missing field rather than contributing an empty instruction block; the three parallel instruction
  lists must correspond one to one.
- **The workspace scope and the workspace root are forced equal** (`_require_workspace_confinement`),
  so the runtime cannot read and execute in one directory while its write rule admits another.

The `models/` route's own statement that `REVISION_PAYLOAD_VERSION` is the payload version is now one of two:
`FAMILY_REVISION_PAYLOAD_VERSION` exists because the family payload seals a different field set, so a digest can
never be mistaken for the other object's identity.
This module is also the single home of the four environment names and of the two instruction
**channels**. The channel choice is load-bearing rather than stylistic: the trusted instructions go in
the **system** role, which eve keeps outside conversation history and includes on every model call — so
they survive turn boundaries, compaction and clear — while task facts go in the **user** role, because
they are content rather than authority and compaction may legitimately summarize them.

- The family identity, the immutable revision aggregate and its self-consistency rules. [108]
- The two relation shapes, the closed authored role vocabulary and the four read models. [109]
- The draft/stored split and the repaired `UUID` identifier field. [110]
- The two payload versions and the family payload's sealed field set. [111]
- The shared accepted/proposed rule both revision aggregates apply at construction. [112]
- The extended served surface, including the graph names. [113]
- The eight graph operations and the anchor-endpoint union the request vocabulary gained. [114]
- The eight graph operations and the anchor-endpoint union the request vocabulary gained. [115]
- The storage owners that write this vocabulary: the graph modules, plus the store for the invariant half. [116]
The requirement this graph vocabulary belongs to: requirement packet `KS-R02@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.
- The carrier format added to this route: schema, value types and the on-disk byte contract. [117]
- The two channels and why the distinction is load-bearing. [118]
- The parse-time confinement invariant and the wrong-seat refusal. [119]
- The four environment names declared beside the format so writer and reader cannot drift. [120]
- The producer that builds this value and the two consumers that verify it, none of them in this route. [121]

## 260915-KS-L3 The Candidate-Change Vocabulary

## 260915-CAPS-L11 One Refusal Shape For One Class Of Source Defect

This route's knowledge sub-route grew from eleven modules to twelve, and the vocabulary it serves now covers the
**write boundary** rather than only the stored shapes. `candidate.py` is the whole vocabulary of the one
candidate-change operation: the resolved context, the expected-record model, the closed command union, the batch
and its factual receipt. Three of its rules are the model-level half of a storage contract:
`sources.py` on this route now refuses an **emptied** admitted source the same way it already refused
a non-UTF-8 one: a typed `CapsuleSourceError` carrying `status="source-empty"`, a detail naming the
source path, and a next action — rather than a bare `ValueError` escaping `CapsuleSource.text`.

- **A resolved context is compared, never trusted.** `KnowledgeContext` carries what the admitted runtime
  resolved, and `context_digest` seals every field but itself; `CandidateResolution` deliberately has **no**
  dataset-identity field, so an application cannot pass a remembered digest — it can only read one. The model
  validator refuses an unsealed context at construction, and the operation re-derives the digest inside its
  transaction, which is the only defence against a `model_copy`-built batch that bypasses the validator.
- **The union is the reach.** `ProposedCommand` is eighteen frozen members discriminated on `kind` with
  `extra="forbid"`: there is no promotion member, no approval member, no arbitrary-SQL member and no free-form
  field, so "this operation never accepts knowledge" and "a payload cannot confer authority" are properties of
  the vocabulary rather than rules the operation remembers to apply. Command payloads carry **no** `Authorship`:
  the admitted envelope is attached by the store, and a draft that arrived with its own is re-stamped.
- **Expected state, never assumed state.** `ExpectedRecord` is `present` with a digest or `absent` without one,
  and there is deliberately no third mode — "I did not say" is not an expectation. `ChangeBatch` refuses two
  expectations for one record.
**Why the shape matters rather than the message.** `compile_admitted_capsule` catches only
`CapsuleCompilationError`, so an untyped raise from the value layer surfaced to an operator as a
traceback instead of the named refusal the compiler's own boundary promises. One class of defect now
has one refusal shape at one boundary.

The receipt is part of the contract too: `RecordIdentity.state` is exactly `written | removed`, a removal carries
the digest the row had, a command whose effect was already stored contributes no entry, and
`MutationResult._require_consistent_receipt` refuses a refusal that changed anything, a non-refused result with a
refusal, a `no_change` result with entries, a `changed` result with an empty entry list, or a `changed` result
whose two identities are equal.

`models/knowledge/result.py` grew the two label-edit request/result pairs and the two candidate-boundary codes
(`target_not_candidate`, `promotion_not_supported`), while the `task-candidate` lane deliberately reuses
`unauthorized_scope`. **The refusal code `no_change` remains declared with no producer** — the reachable
vocabulary is the *result state*, and a consumer must not branch on the code.

- The lane vocabulary, including the read-only `baseline` member that exists so it can be refused by name. [122]
- The resolved context and its two consistency validators. [123]
- The module-level digest the validator calls and the operation re-derives. [124]
- The expectation model and its present-with-digest / absent-without-digest rule. [125]
- **The closed union with no promotion, approval or SQL member — twenty-two members after this leaf's four composition command kinds joined the eighteen**, and the members are the operation's entire reach. [126]
- The alias a batch's commands travel under, and the construct that makes the union's membership checkable in one place. [127]
- The resolution shape that deliberately omits the dataset identity. [128]
- The batch and the receipt consistency validator the operation's results must satisfy. [129]
- The lane vocabulary, including the read-only `baseline` member that exists so it can be refused by name. [130]
- The resolved context and its two consistency validators. [131]
- The module-level digest the validator calls and the operation re-derives. [132]
- The expectation model and its present-with-digest / absent-without-digest rule. [133]
- The closed union with no promotion, approval or SQL member; the twenty-two kinds are the operation's entire reach. [134]
- The resolution shape that deliberately omits the dataset identity. [135]
- The resolution shape that deliberately omits the dataset identity. [136]
- The batch and the receipt consistency validator the operation's results must satisfy. [137]
- The two candidate-boundary codes and the three operations that leaf added to the served vocabulary. [138]
- The served operation union the candidate-boundary leaf joined. [139]
- The invariant-label result that leaf added to the served vocabulary. [140]
- The operation that consumes this vocabulary. [141]
- The composition seam that resolves a context from a live candidate and seals it. [142]
- The seam entry point that applies a batch under the admitted provenance. [143]
- The lane rules the batch operation applies before it takes the lock. [144]

## 260915-KS-L4 The Snapshot Vocabulary

The knowledge sub-route grew a thirteenth module, `models/knowledge/snapshot.py`, and the vocabulary it adds is a
**local working object's** vocabulary rather than a stored shape's: one candidate directory, its sealed receipt,
one closed snapshot stage, one publication request/result, the publication-state measurement a read gates on, and
the closed disposal union. `models/knowledge/result.py` grew six operations and seven refusal codes in the same
change, and the facade re-exports all of it.

Three model-level rules carry the contract, and each is the reason a field is missing rather than present:

- **The receipt carries no dataset digest.** `CandidateReceipt` records namespace, lane, the exact code and memory
  inputs, the schema generation and the candidate reference, and seals every one of them with `receipt_digest` —
  but the *dataset's* logical identity is deliberately absent, because a caller that could state it could hand-write
  the identity its publication would later be compared against. The identity is read from the database or it does
  not exist, and `build_candidate_receipt` derives rather than accepts.
- **Every result is closed, and `state` is the only branch.** `CandidateResult`, `SnapshotPublicationResult`,
  `PublicationState` and `CandidateDisposalResult` each refuse an inconsistent combination at construction: a
  refusal carries its refusal and reports nothing it did not establish, a non-refusal names what it reached, and a
  refused publication reports **no** destination identity at all. `PreparedKnowledgeSnapshot` carries both the
  logical identity and the physical `file_digest` because publication decides two different questions — "is this
  the same knowledge?" and "is this the file I froze?".
- **The disposal union has exactly two members, and its authorization is carried, not examined.**
  `CandidateDisposition` is `DiscardCandidate | PublishedCandidate` discriminated on `kind`; there is no "it looked
  disposable" mode. `DiscardCandidate.authorization_ref` is stored because the caller owns the approval chain,
  while this layer decides only permissibility (whether the named identity is the one the candidate holds now, and
  therefore whether discarding abandons work no retained publication covers).

The refusal vocabulary's own rule is unchanged by the addition and worth restating where the codes are declared:
`no_change` remains a **result state** in two vocabularies (the batch's `MutationResult` and the publication's
`SnapshotPublicationResult`) and a refusal code with no producer, and `snapshot_incomplete` /
`publication_durability_unconfirmed` exist because "the private stage did not complete" and "the replacement
completed but cannot be confirmed" need different remedies.

- **The snapshot vocabulary's own module: layout, receipt, stage, publication and disposal.** [145]
- The two derived paths that keep write and publication on one file. [146]
- The typed admitted handle that confers no authority by itself. [147]
- The baseline that requires the identity the caller admitted for it. [148]
- The receipt's sealing helper and the one derived constructor. [149]
- The destination request whose "expected absent" mode is the only way to overwrite. [150]
- The measurement that reports two identities and guesses nothing. [151]
- The carried-not-examined authorization reference and the verdict. [152]
- **The operation and refusal vocabulary this leaf extended.** [153]
- The facade that re-exports the whole snapshot surface as the served vocabulary. [154]
- The lifecycle and publication operations that produce these values. [155]
- The second composition seam that admits these values and returns them unchanged. [156]
- The node that proves the publication outcome is a measurement rather than a claim. [157]

## 260915-KS-L5 The Merge Vocabulary

The knowledge sub-route grew a fourteenth module, `models/knowledge/merge.py`, and it declares the **structural**
half of the substrate's vocabulary: three datasets that already exist, two base claims, the coverage facts of a
delta, one conflict record and one outcome. The absence the whole module is built around is stated in its own
docstring rather than left to a consumer's inference: **nothing here can carry a judgement about whether the
merged knowledge is correct** — there is no compatibility, acceptance, approval or "harmless" field, and the one
non-refusal state is named `structurally_merged` because that is the entire claim.

Three splits are load-bearing, and each is a place a weaker model would have permitted a guess:

- **An explicit input versus a resolved one.** `MergeInput` names a dataset *and* the exact logical identity the
  caller admitted for it. A caller cannot hand over a path and let the operation decide which dataset it meant;
  the identity is re-read and compared before any byte is copied. The `reference` field is the caller's own
  durable anchor and is carried as a fact — this layer does not read Git objects to decide what a dataset is.
- **A base claim versus a base fact.** The claim is a closed union of `SuppliedGitBase` (the caller resolved it)
  and `ResolvedGitBase` (the caller claims one commit is the *unique* common base and asks for the evidence).
  There is no third member, so "the operation may pick one" is not expressible. `MergeBaseResolution` records
  which of the two applied, so a reader can tell "the history had one common base" from "the caller said which
  commit it was" without re-deriving it from the claim.
- **A measurement versus a verdict.** `MergeCoverage` reports which tables the changeset touched, which the
  replay proved covered, and how many operations of each kind were materialised; `MergeOutcome` reports the
  identities it observed. Neither can express an opinion about the data.

Two model-level rules a consumer must not flatten, because each is enforced at construction:

- **A table that changed but carried no operation is representable, and it is not silent.** `TableCoverage`
  separates `table_changed` (read from the two datasets) from `operations` (counted from the changeset) — the
  exact pair whose disagreement *is* the silent-omission class — and `MergeCoverage` covers every canonical
  table, so "examined and had nothing to carry" cannot be confused with "never attached".
- **A conflict record states only what the engine supplied.** `MergeConflict` has two shapes:
  `engine_attributed`, where the callback held the operation and the record carries its table, kind and the exact
  row key (read from the operation's **old** values, because a changeset omits a key column an `UPDATE` did not
  change), and `engine_reported_without_row`, where a foreign-key conflict gave the callback no change at all, so
  the row fields are absent and `detail` says so. No violation count is reported for that shape: the pinned
  binding raises `ConstraintError` with no count, so a number there would be the operation's own inference.

`models/knowledge/result.py` grew the two operations (`resolve_merge_base`, `merge_knowledge_datasets`) and
twelve refusal codes in the same change — one per observable failure point, so the twelve different next actions
stay distinguishable. `duplicate_identity` and `delete_reference_conflict` are the two whose meaning a reader must
read from the merge's cards rather than from the code name: the first fires even on byte-identical payloads, and
the second names no row.

- **The merge vocabulary's own module: the explicit input, the closed base claim, coverage, conflict and outcome.** [158]
- The one non-refusal state name, which is the entire claim the operation makes. [159]
- **The precondition the row-less conflict offer reads, the field that carries it, and the function that no longer infers the offer from the code.** [160]
- The request that carries the proven resolution, the paths it deliberately keeps out of the resolution, and the optional destination. [161]
- The base-resolution request and the resolution that records which claim applied. [162]
- The per-table coverage fact that separates "changed" from "carried an operation". [163]
- **The operation and refusal vocabulary this leaf extended.** [164]
- The merge operation that consumes this vocabulary. [165]
- The base resolution that produces the value this vocabulary consumes. [166]
- The third composition seam that takes these values and returns them unchanged. [167]
- The node that asserts the published outcome carries no verdict field and reports the coverage record. [168]
- The boundary node that holds the conflict record to the engine's own row identity. [169]

## 260915-KS-L6 The Portable Vocabulary, And The Boundary It Draws Around External Input

The knowledge sub-route gained its **fifteenth module**, `models/knowledge/portable.py`, and
`models/knowledge/result.py` gained two operation names and one refusal code. The portable vocabulary is the
wire shape of the artifact contract, and three splits carry it — each exists because collapsing it would make a
statement the code cannot support:

- **A request versus an admitted identity.** `ExportRequest.expected_identity` is **required**, because an export
  is addressed at a dataset rather than at whatever a path currently holds; storage re-reads it before encoding.
- **A validated artifact versus a published dataset.** `PortableValidation` reports what was *checked* — with
  `row_counts` over every canonical table **including the empty ones**, because "present and empty" is the fact
  that separates a complete export from one that dropped a collection — while `ImportResult` reports what now
  *exists*. Neither can carry a verdict and neither can grant acceptance: a row whose `state_at_origin` says
  `accepted` crosses as that stored value and nothing more.
- **A staging fact versus a destination fact.** An import can validate perfectly and still not publish, so
  `ImportResult.verified_identity` is carried **independently of `state`**, and the model refuses to construct
  unless the verified identity and the destination's identity agree on the logical digest.

`ImportRequest.expected_destination` is a **closed two-mode choice** in effect — the exact identity the caller
observed, or `None` for "expected to be absent" — and there is no third mode: an occupied destination nobody
admitted is `destination_occupied` rather than replaced, and a named-but-absent destination is `destination_stale`
rather than a silent fresh install. `expected_repository_id` is optional and only narrows.

**The one vocabulary addition is the narrowest member of the whole refusal union.** `invalid_export` exists
because the portable artifact is the only input on any of these paths that can be **malformed as a document** —
an unknown envelope field, a missing manifest key, a repeated JSON key, a row whose fields are not the declared
columns in declared order, a value the declared type cannot hold, or a text that is not the canonical rendering of
the document it holds — which is this route's own recorded rule ("a code is a vocabulary decision, not a
raise-site convenience") at its sharpest. `unsupported_schema`, `duplicate_identity`, `invalid_reference` and
`destination_occupied` are shared with the paths where the failure is the same fact. The two operations are
separate for the same reason the merge pair is: an export answers "what is this dataset, logically" and an import
answers "may this artifact become a dataset here".

**One convention is worth stating here because it is a deliberate non-change:** `models/knowledge/__init__.py`
does **not** re-export the portable (or merge) vocabulary, so a consumer reaches it as
`agents_remember.models.knowledge.portable` — the shape the merge vocabulary already follows.

- The portable sub-route module, its three splits and its deliberately absent verdict. [170]
- The one code and the two operations this leaf added to the shared vocabulary. [171]
- The five factories that produce the portable boundary's codes. [172]
- The encoder and reader this vocabulary describes. [173]
- The nodes that hold the round trip and the no-promotion rule to this vocabulary. [174]

## 260915-KS-L7 The Recorded-Scope Read Vocabulary

The knowledge sub-route gained its **sixteenth module**, `models/knowledge/read.py`, and three existing modules
changed: `result.py` gained one operation and six refusal codes, `base.py` gained the shared path rule
`require_plain_git_path`, and `source.py`'s anchor validator now delegates its Git-pathspec half to it. The
selective read's vocabulary holds no SQL, no Git call and no authority decision — it declares what a caller may
ask for and what a caller is told.

**Four splits are load-bearing, and each is a place a future edit could silently undo a guarantee:**

- **Seed versus selection.** The seed is a **closed discriminated union** of five kinds — `path`, `invariant`,
  `invariant_revision`, `family`, `family_revision`, one per row of the requirement's table — and it carries **no
  filter, no sort, no revision preference and no display version**, because none of those may select a record.
  The only thing that narrows a selection is an exact identity the caller named.
- **Selection versus page.** The three `primary_items_*` fields describe **one walk**: the declared selection
  total, the cumulative returned, what remains. All three travel on every page, so a one-item page cannot be read
  as a one-item scope **at any position** — not only at its first page — and `KnowledgeReadCounts` refuses its own
  arithmetic contradiction at construction.
- **Provenance versus verdict.** Every statement, role, rationale and lifecycle crosses as the authored text it
  is stored as, and **the response has no field that could hold a current-truth marker, a severity or a
  ranking**. That absence is how the requirement's *Forbidden Overreach* is enforced structurally rather than by
  discipline, and it is the property this route's "a wire vocabulary is imported from its producer" rule protects.
- **Continuing versus re-binding.** `KnowledgeReadCursor` names the exact snapshot, context, selector, policy,
  manifest and position it continues, so a cursor presentable against another dataset is refused rather than
  serving a page assembled from two revisions.

**Three model-level invariants a consumer may rely on**, each refused at construction: `KnowledgeReadPage`
refuses `has_more == enumeration_complete` or a `has_more` that disagrees with the presence of a continuation
(**a truncated page cannot be presentable as complete**); `KnowledgeReadCounts` refuses
`returned + remaining != total`; and `KnowledgeReadResult` refuses to be both a page and a refusal, or neither.

**The read context is the whole admission one read has,** and it enforces two rules at construction: the selected
snapshot must belong to the named repository namespace, and source resolution needs **both** `repository_root` and
`code_tree_id`. A half-specified resolution is refused rather than answered with `not_requested`, because that
would report a caller's mistake as a fact about a recorded anchor. **`task_ref=None` is a supported state and not
a degraded one** — a baseline read during planning needs no leaf, an enclosure or a fabricated task.

**The vocabulary additions are the ones only a bounded, continuable selection can reach:** the operation
`read_knowledge_scope` (one rather than two, because a seed and a continuation are two ways of asking one
question and a caller branches on the refusal code, not on which of the two it passed) and six codes —
`selector_absent`, `registration_absent` (the two **absences**, separated by which question the caller got wrong,
and neither a verdict of "no semantic impact"), `page_budget_too_small` (the selection is valid and one
indivisible item does not fit; the position is unchanged), `continuation_binding_mismatch` (**no partial page**),
`snapshot_unavailable` (which is also what a schema generation this build cannot read surfaces as, so the read
does **not** use `unsupported_schema`) and `selection_incomplete` (no total, no partial manifest). Measured
at this leaf's own candidate, the unions were **twenty-five operations and forty-four refusal codes**; the
file declares **fifty operations and forty-five refusal codes** today (re-measured 2026-09-18 at code
`c5a74a85`; see the entry at the head of this history).

**One deliberate difference from the two preceding leaves is worth recording here.**
`models/knowledge/__init__.py` does **not** re-export the portable or merge vocabularies, but it **does**
re-export the read vocabulary and lists every one of its names in `__all__` — so a consumer may reach the read
shapes from either `agents_remember.models.knowledge` or `agents_remember.models.knowledge.read`.

**The path rule is shared, and that is the reason `base.py` is in this change set.** `require_plain_git_path`
refuses Git pathspec **magic** — the leading-`:` family — while **admitting `*`, `?` and `[`**, which `ls-tree`
addresses as literal characters (measured on `git 2.54.0`). Both typed path boundaries call it, so a spelling the
write path refuses cannot be presented as a seed that is answered with an absence. The card for
`models/knowledge/base.py` carries the measured table.

- The read sub-route module: the closed seed union, the context, the page and the cursor. [175]
- **The corrected count model and the truncated page that cannot claim completeness.** [176]
- The one operation and six codes this leaf added to the shared vocabulary. [177]
- **The shared Git-pathspec rule, with `*`, `?` and `[` admitted as literal characters.** [178]
- The write path's delegation of its pathspec half to that one rule. [179]
- **The facade's ninth source, which this leaf did add to `__all__`.** [180]
- The cursor decoder the read re-exports through the facade. [181]
- The cursor encoder the read re-exports through the facade. [182]
- The nodes that hold these models to their own invariants. [183]

## 260915-KS-L8 The Comparison Vocabulary

The knowledge sub-route gained its **seventeenth module**, `models/knowledge/diff.py`, and `result.py` gained
**one** operation — `diff_knowledge_scope` — and **no refusal code at all**, so the unions measured
**twenty-six operations and forty-four codes** at this leaf's own reading; the file declares **fifty
operations and forty-five refusal codes** today (re-measured 2026-09-18 at code `c5a74a85`; see the entry
at the head of this history — the module card records that this leaf's twenty-six was a count of the
members the diff work could see rather than a count of the union). (L8 is the first knowledge leaf whose boundary needed no new
refusal vocabulary, and that is recorded as a fact rather than a silence: the comparison's whole failure
surface is R07's own six codes plus `selected_input_unavailable`, and a one-sided absence travels as a value
beside the page rather than as a seventh code). The module declares what a comparison may ask and what a
caller is told; it holds no SQL, no Git resolution and no authority decision.

**Four split lines are the contract, and each is a place a future edit could silently undo a guarantee:**

- **Two snapshots, one selector policy, and no field that could carry a second one.** `KnowledgeDiffSide`
  carries the exact snapshot and an *optional* selector that **replaces** the request's seed for that side
  only — the packet's *"an explicit revision selector may address different before/after revision IDs"* as a
  value. The request has **no field** that could express a computed relevance, a ranking or an inferred
  impact, so the forbidden second relevance rule is not representable here. The one production path this
  reaches is `SelectionQuery.seed_override`, documented on the memory route's overview and in the
  sub-route's own modules — a parameterisation of R07's single rule, **not** a second rule.
- **Provenance versus verdict.** `KnowledgeDiffSourceChange` carries the two sides' observations and four
  booleans about which object moved, and **nothing that could hold a severity, a "strengthens", a "harmless"
  or a neutrality finding**. The record's own field changes are a separate collection on the item, so a
  source-only change cannot read as a changed obligation — the packet's second non-conforming example made
  structurally impossible rather than merely avoided.
- **Absence versus selection.** `DiffCoverage` keeps `present_outside_selection` apart from
  `absent_from_snapshot`, and `SideAbsence` carries one side's own typed absence **beside** the page rather
  than replacing it, because a comparison can legitimately find that one side holds nothing for the selector
  while the other holds records.
- **A comparison's cursor is not a read's cursor.** `continue_diff_from_cursor` is a separate decoder for a
  separate document: a read cursor positions a page in one selection and a comparison cursor positions one in
  a union of two, so presenting either to the other operation is a caller's mistake and both refuse it by
  name.

**Three model-level invariants a consumer may rely on**, each refused at construction: `KnowledgeDiffPage`
refuses `has_more == enumeration_complete` or a `has_more` disagreeing with the presence of a continuation
(**a truncated comparison cannot be presentable as complete**); `KnowledgeDiffCounts` refuses its own
arithmetic contradiction **and** a display/suppression total larger than the comparison; and
`KnowledgeDiffResult` refuses to be both a page and a refusal or neither, and **refuses a declared limitation
that disagrees with its omissions in either direction** — while `no_semantic_assessment_performed` is
unconditional.

**The closed vocabularies and the one member that was removed.** `DiffItemKind` (five), `DiffCoverage`
(five), `DiffRecordTransition` (six, whose `superseding`/`superseded` pair is recognised **only** from the
authored predecessor edge — never a label, a display version or an insertion order), `DiffOmissionReason`
(three) and `DiffLimitation` (four) are literals rather than free text. `assessment_beyond_this_increment`
was declared and then **removed** in fix round 1 because nothing in the package constructed it and no
limitation advertised it: a reason with no producer is dead vocabulary in a table the validator checks in
both directions. `KNOWLEDGE_DIFF_FIELD_NAMES` is the nine compared record fields in declared order, with
`selection_reasons` deliberately absent — which route of a selection reached a record is a fact about a
traversal, not about the record.

**One deliberate non-change to the facade.** `models/knowledge/__init__.py` does **not** re-export the
comparison vocabulary, exactly as it does not re-export the portable or merge vocabularies — a consumer names
`agents_remember.models.knowledge.diff`, and the module is not in the facade change set.

- The comparison sub-route module: the two sides, the request, the item, the page and the result. [184]
- **The record half and the source half, with no field that could hold a verdict and `missing_side` as a reason rather than a third change statement.** [185]
- **The binding and the digest derived from it, which is how a candidate change invalidates a continuation by construction.** [186]
- **The counts that keep the comparison total and the display total apart, and the two closed vocabularies.** [187]
- The expansion as a value, with the carried partition and its three path lists. [188]
- **The comparison's own cursor and its two functions, deliberately not the read's decoder.** [189]
- **The one operation this leaf added, and the unchanged code union.** [190]
- **The node that measures the absent verdict over the serialized response, and the node that holds the two change statements apart.** [191]
- The nodes that hold the page and result invariants: the truncated comparison and the unestablished limitation. [192]

## 260915-KS-L10 The Route Operations, And The Envelope's Refusal

This leaf added vocabulary, not a new sub-route, and the additions are exactly the two an operable `Route`
needs. `models/knowledge/result.py`'s `KnowledgeOperation` literal gained **`author_route`** and
**`set_governing_route`** — `routes.py` had been borrowing `create_invariant_revision` as the operation its
refusals named, so a caller acting on a route refusal was told an invariant-revision operation failed. The
refusal vocabulary itself did **not** grow: inadmissible record payloads are refused with the already-shipped
**`invalid_payload`** code, because "the payload you supplied is not this kind's shape" is the same fact the
envelope seam needs and no narrower code could say it better. The route rules reuse the shipped
`invalid_reference`, `missing_expected_row` and `lineage_cycle` codes for a non-confined path, an unauthored
route or parent, and a cycle respectively, and `relationship_constraint` for a second governing route on an
already-governed row.

The deliberately absent vocabulary is as load-bearing as the additions: there is **no** `Route` model in this
sub-route and no `route_schema`-style declaration, because the three generation-2 tables
(`route`, `knowledge_record`, `record_revision`) are declared by `memory/knowledge/schema_v2.py` as pinned DDL
and the route operations take frozen request dataclasses (`RouteDraft`, `GoverningRouteDraft`) rather than
pydantic models. Nothing here became a second identity authority: no field on any model in this sub-route
carries a route's identity as a fingerprint.

- The two operations the route write layer added, so a route refusal names a route operation. [193]
- The shipped code an inadmissible record payload is refused with — reused rather than widened, and re-cited by hand against the current tree. [194]
- The two operations the route write layer added, so a route refusal names a route operation. [195]
- The shipped code an inadmissible record payload is refused with — reused rather than widened, and re-cited by hand against the current tree. [196]
- The route rules' refusal shapes and the frozen request objects they report on. [197]

## 260915-KS-L11 The Authored-Judgment Vocabulary

The knowledge sub-route gained its **eighteenth and nineteenth modules** — `models/knowledge/facet.py`
and `models/knowledge/facet_read.py` — and the widening of the operation's own vocabulary in
`models/knowledge/candidate.py` and `models/knowledge/result.py`: **eighteen command kinds** (the shipped
twelve plus six facet commands), **six new operations** and **no new refusal code**:
`facet.py` added no code of its own, and every failure the write path reports reuses a shipped one
(`invalid_payload`, `invalid_reference`, `missing_expected_row`, `stale_precondition`,
`promotion_not_supported`, `lineage_cycle`, `unsupported_schema`) — all seven **reused unchanged**, and the
four factories the leaf added were mechanisms under codes the vocabulary already declared. The six
facet acts joined `KnowledgeOperation`, so this section read the operation union at **thirty-five
members** with the refusal-code union at **forty-four** — both stale, and neither may be read as the
current size: the file declares **fifty operations and forty-five refusal codes** today (re-measured
2026-09-18 at code `c5a74a85`; the measured series and the command are in the entry at the head of this
history).

**One closed list is the whole vocabulary, and everything else is derived from it.** `FACET_KINDS` is the
eight subtypes; `FacetKind` is the same eight spellings; one frozen payload model per subtype carries that
subtype's minimum meanings; `FacetPayload` is the discriminated union whose member set is exactly the eight;
and `FACET_RECORD_SCHEMAS` derives `facet-<kind>/v1` from the kind. A ninth subtype has **no member to
resolve to**, so it cannot be stored as a generic facet — it becomes the typed `invalid_payload` refusal at
the envelope seam, which is also why `AddFacet` carries its payload as a mapping: validating it in the
command would turn that refusal into a parse error.

**Three splits are load-bearing, and each is a place a future edit could undo a guarantee:**

- **Authored content versus provenance.** No payload field can be read as, or substituted for, the record's
  authorship: a decision's `decider` is content *about who decided*, there is no field for `actor_ref`,
  `authorization_ref`, `operation_id` or `recorded_at`, and `extra="forbid"` is what refuses a payload that
  arrives carrying one.
- **Guidance versus verdict.** `DiagnosticGuidancePayload` requires an interpretation **and** the limit of
  that interpretation, and carries no field that could hold an assessment, a compatibility verdict, a
  severity or an endorsement — for any of the eight subtypes.
- **Recorded designation versus derived currency.** `ExplanationRecord.current_revision_id` is the
  designation the record *stores*; `None` is the fact "no designation recorded" rather than a fallback to
  the newest revision, and no field of the read vocabulary could be read as "latest".

**The two closed sets this module declares are deliberately separate declarations.** The four attachment
endpoint kinds and the two explanation subject kinds spell two names identically because both name the same
canonical table, but they are separate constants and separate typed unions: an attachment's endpoint set and
an explanation's subject set are two closed sets that could diverge, and sharing a literal would hide it.
The **route is deliberately absent from the endpoint set** — the route association is the envelope's own
`governing_route_id`, and a second route mechanism here would be the competing one the design forbids.

**One precision the union does not carry, stated so it is not inferred:** `AddFacet.facet_kind` is a
length-bounded `str` rather than the `FacetKind` literal, so the *command* accepts any nonempty kind name
and the closure is enforced one seam later. That is the deliberate trade above, not an oversight — but a
reader should not conclude the ninth subtype is unconstructible at the command.

**One deliberate non-change to the facade.** `models/knowledge/__init__.py` does **not** re-export this
vocabulary, exactly as it does not re-export the portable, merge or comparison vocabularies — a consumer
names `agents_remember.models.knowledge.facet` or `...facet_read`, and neither module is in the facade
change set.

- The one closed list and the declarations derived from it. [198]
- **The six authored commands and the union they join, which is the operation's widened reach.** [199]
- **The standalone request and the receipt that carries no approval, endorsement or judgement field.** [200]
- **The facet selection's own policy, the complete-or-refused bound and the page whose completeness is not a settable flag.** [201]
- The two seed kinds and the six item kinds as closed unions. [202]
- The eight subtypes' payload models and the two nonempty-tuple meanings. [203]
- **The nodes that hold the closure, the per-subtype refusals and the receipt's absent verdict fields.** [204]
- **The six operations this leaf added to the shared vocabulary, and the unchanged code union.** [205]

## 260915-KS-L14 The Detection Vocabulary, And The Two Operations It Adds

The knowledge sub-route gained its **twentieth module** — `models/knowledge/detection.py` — and the
shared served vocabulary grew by **two operations and one refusal code**: `record_detection_run` and
`read_detection_run` join `KnowledgeOperation`, and `detection_self_reference` joins
`KnowledgeRefusalCode`. The operation union therefore read **thirty-seven members** and the code
union **forty-five** at this leaf's own candidate. The code union is still forty-five; the operation
union is **not** — the file declares **fifty operations** today (re-measured 2026-09-18 at code
`c5a74a85`; the measured series is in the entry at the head of this history), so the number above is
this section's own reading and not the current size. Two members rather than one, for the reason the read pair and the diff pair are
one each: recording a run and reading one back are different acts, and the read is the one that must
answer with the recorded order rather than with whatever order rows come back in.

**No field of either record can hold a conclusion, and the absence is declared rather than inferred.**
The module's whole vocabulary is built so that a severity, an assessed priority, a conflict or
compatibility verdict, a causal explanation, a harmlessness label and an authored finding are
**unrepresentable**: `CONCLUSION_BEARING_FIELD_NAMES` is one closed list of those concepts and
`conclusion_bearing_fields` is a total, mechanical **review of a model's declared field set** — it reads
`model_fields`, not an instance, so a field is reported whether or not any payload populates it. The
shipped base's `extra="forbid"` refuses a payload that supplies one; `observed_basis_detail` refuses a
verdict written into the prose field by requiring `detail` to *equal* the rendering of the record's own
recorded basis. Both records also carry the unconditional `no_semantic_assessment_performed` limitation,
so the absence is a stated fact rather than something a reader infers from a missing field.

**The closed vocabularies are declared as a `Literal` and as a tuple, and a case asserts they agree.**
`DetectionCondition` / `DETECTION_CONDITIONS` (the five declared conditions), `DeclaredInputSet` /
`DECLARED_INPUT_SETS` (the three readings), `DetectionChangeGranularity`, `DetectionScopeStatus`,
`DetectionLimitation` / `DETECTION_LIMITATIONS` and `MANIFEST_DESTINATION_KINDS`. Three published
identities travel with them: `DETECTION_POLICY_VERSION` (the detection contract's name, in the shipped
constant idiom), `CONDITION_VOCABULARY_VERSION` (the vocabulary versioned with the policy, so a condition
the policy does not declare is refused *with the version it was refused against*), and
`DETECTION_EXTRACTOR_VERSION` — **authored rather than imported**, because the shipped anchor resolver has
no symbol extractor and returns `unsupported_locator`, so there was no existing constant to cite.

**The declared input set is checked against the member's own recorded discriminator, never by counting
sides.** `DetectionRecordedInputSet` enforces that `both_sides_declared` records both declared sides each
under its own selector and context and **no** counterpart-probe outcome, that `union_of_both_sides` records
both sides *and* the probe's recorded outcome per reported item, and that `trigger_side_only` records
exactly one side and no probe at all. Each refusal names the member and what was recorded instead, because
a two-sided condition reported from a one-sided read is the silent-widening shape the requirement exists
to prevent — and a `trigger_side_only` signal that *asserts* something about the unread side gets its own
refusal, since the absence of a counterpart is a scope limitation rather than a finding of equality.

**Two shapes carry what the record cannot say.** `DetectionScopeManifest.resolve` reports a reference as
`retained` only for a resolved durable-publication destination with a recorded identity, and otherwise
`unresolved` **with what would resolve it** — never as an empty manifest, and never as an error;
`DetectionManifestResolution`'s validator refuses either half without its required field.
`DetectionRunCurrentness` carries the recorded and current versions beside the state and **no signal at
all**: its `signals_unchanged` field is the literal `True`, which is the type saying that this operation
cannot rewrite what it read. `DetectionRunReproduction` carries both run identities, both ordered
sequences, every differing input and one verdict that must follow from those facts.

**The record's own field set is all-required.** `DetectionSignalPayload` carries every field requirement
1.1 lists — signal id, repository, governing route, condition, vocabulary version, declared input set,
observed changes, relationship paths, the two published versions, the scope manifest, the registered scope
status, the unmapped paths and the limitations — with the four collection fields required even though
three are frequently empty, so a signal that observed nothing *states* that rather than defaulting.

- **The three published identities, including the extractor version authored because no shipped constant exists to cite.** [206]
- The five declared conditions and the three declared input sets, each as the validated type beside the tuple a caller enumerates. [207]
- **The closed conclusion-name list and the declared-field-set review that makes "no conclusion is representable" checkable rather than asserted.** [208]
- The observed-change granularities, the declared scope status and every declareable limitation. [209]
- **The declared-input-set discriminator contract: two sides and no probe, both sides and the probe, or one side and no probe.** [210]
- **The manifest reference and its two-state resolution, which reports an unresolvable reference with what would resolve it rather than as an empty manifest.** [211]
- **The all-required signal field set, and the `detail`-equals-rendering rule that refuses a verdict in prose as it refuses a verdict field.** [212]
- **The run payload: the per-signal declarations not collapsed into a run default, and the declared total order over signal identity.** [213]
- **The currentness answer that carries the recorded versions beside the current ones and cannot hold a re-interpreted signal.** [214]
- The one typed outcome per detection operation, serving its signals in the run's recorded order. [215]
- **The two operations and the one refusal code this leaf added to the shared vocabulary.** [216]
- The envelope registry every typed payload pair is registered under — six family groups now — and the two-kind set derived from the detection entries. [217]
- **The requirement-revision family this route gained: its frozen payload vocabulary, the pair it declares in the envelope's kind vocabulary, and the kind set derived from it.** [218]
- The pair that family declares in the envelope's typed kind vocabulary. [219]
- The kind set derived from the registry entries that pair is built from. [220]
- **The recorded quotation-degree ruling, and the absence it turns on: no payload field is the operative obligation.** [221]
- The two operation members the requirement record group added, and the fact that no refusal code was added with them. [222]
- The envelope registry key pair each detection payload is registered under, and the two-kind set derived from it. [223]
- **The cases that hold the field-set review, the three declared input sets and the retention answer.** [224]
- The eight graph operations and the anchor-endpoint union the request vocabulary gained, each cited at its own declaration. [225]
- The envelope registry key pair each detection payload is registered under, and the two-kind set derived from it. [226]

## 260915-KS-L12 The Supporting-Record Vocabulary

`KS-R12@v1` adds the record vocabulary the route's typed layer was still missing: an **evidence claim**
(authored content about what evidence covers) and a **verification observation** (a mechanical fact about
what ran). They are two kinds and not one 'evidence' record, and the separation is the whole reason the
leaf exists — collapsing them would put a human's coverage assertion in the same row as a machine's exit
status, and the first consumer to read the row would treat the whole row as machine-produced. The
separation is also what makes the no-sufficiency rule enforceable: if a passing run lives in a different
record from the claim, there is no single row in which 'passed' could be read as 'sufficient'.

Four properties of this vocabulary are load-bearing. **Nothing judges.** Neither payload has a field for a
verdict, a confidence, a severity, an endorsement or an aggregate, and `limitations` is required on a
claim with the empty string as a value it can hold — 'this author declared no limitations' rather than
'limitations unknown'. **The subject and the coverage are structural.** A claim's subject is a
discriminated union of exactly two kinds, invariant revision and knowledge facet revision, each naming its
own join table, and its claimed coverage is the same shape with a row identity that makes one endpoint
covered once unrepresentable at construction as well as in the key. **The execution result is a closed
five-member vocabulary** — `passed`, `failed`, `error`, `skipped`, `not_run` — with `not_run` a member
reported as itself and no member that says what a result means. **The references are references.** A
`ResultArtifactReference` is a confined repository-relative path, the sha256 of the artifact's bytes and
its size; a `PublicationReference` names a durable destination, the sha256 of the published bytes and the
instant, and its presence or absence is how the record states which retention route it relies on.

The route's read vocabulary is `models/knowledge/evidence_read.py`: the declared contract of a **third**
selection with its own policy name, its own two seed kinds, its own item kinds and its own counts, plus
the four artifact-resolution states and the unassessed state a claim with no assessment reference is
served with. No model here has a status, grade, score, confidence or aggregate, and the item models are
frozen and extra-forbidden, so a page cannot be extended with one.
**A property a reader should not have to rediscover:** emptiness is discovered while blocks are
*composed* — after admission succeeded and a real manifest parsed — so the guard is reachable only
through a real composition. That is why the leaf's case drives a disposable copy of the shipped
corpus rather than a fixture, and it is what makes the seed failable.

## 260915-KS-L13 The Authored-Effect Vocabulary, And The Change Set That Composes It

`KS-R13@v1` adds the record vocabulary for **authored work**: what a change was *intended* to do, and who
said so. Four kinds arrive as **envelope records** — `invariant_effect_claim`, `preservation_claim`,
`unresolved_question` and `semantic_change_set` — so the route gains their payload shapes and no identity
mechanism, no second revision aggregate and no table for the change set itself. The first three are
members of one change set and declare their own `change_set_id`, which is what makes membership a stored
fact rather than something the change set restates; the change set's own payload carries the two snapshot
identities it was authored over, the opaque requirement-revision references it names and the exact
realization-claim identities it proposes.

**Six properties are load-bearing. The effect vocabulary is closed and spelled once** —
`ADMITTED_EFFECT_LABELS` names nine labels in one tuple and `EffectLabel` is the literal type built from
exactly that tuple, so a synonym, a compound label, a free-text label and a tenth member are all the same
refusal: the payload does not validate. **Inputs and outputs are exact revision references, never prose**,
and nothing in the vocabulary parses one, splits it on a separator or infers an identity from it. **One
cardinality rule** — `cardinality_violation` — admits no revision on both sides of a claim, requires two
or more outputs for `split` and two or more inputs for `merge`, and admits any counts for the other seven
labels; it is declared here and imported by the storage boundary, so the construction validator and the
typed refusal cannot disagree. **There is no field that is a truth verdict**: no boolean, score,
confidence, verdict or `verified` field exists on a claim, and a stored claim is a claim whose *declared
shape* was accepted rather than one endorsed. **A preservation claim is a separate record and is not an
effect**: its subject is a closed four-member union (an invariant identity or revision, an anchor, or a
change set) with deliberately **no** effect-claim member, and there is no `preserve` label and no
preservation flag. **The author is not a payload field**: authorship *is* the revision's `provenance`,
stamped from the admission, so a payload naming an actor, an authorization, an operation or a recorded
time would be a second, competing statement of one fact.

**The change set is where authored work is composed and where the forbidden set is absent.** It is
superseded by a **new record with a predecessor edge** — no in-place revision, no mutable "current
version" pointer, no separately typed successor — and there is no generated summary, generated narrative,
computed effect list, severity or display ordering computed from meaning anywhere in its shape. It is
**not a decision**: it carries no acceptance, no promotion and no merge verdict. Its read models are
`UnresolvedReference` (the holder, the field's closed four-member set, the reference verbatim as written,
and a reason — with deliberately **no** slot for a resolved value), the three member views and
`SemanticChangeSetView` with all six declared parts readable, and `AuthoredEffectScope` / `EffectReadResult`
for the whole derived read. Every view is a pure function of rows the caller already read, so a view is
disposable rather than an authority; `ChangeSetMembership` is the membership *fact* the design allows code
to compute, and an empty list means exactly that no member declares the change set. `assessment_refs` are
**named** references that may remain unresolved — the assessment record belongs to another leaf — so one
that resolves to nothing is a reported state and never a refused write, a substitute, or a claim that an
assessment happened.

## 260915-KS-L16 The Registered-Scope And Family-Review Vocabulary, And Two Operations Added Without A Refusal Code

`KS-R16@v1` composes the family-integrity pipeline over three record leaves and adds **no record kind of
its own**; what this route gains is the two vocabularies that pipeline speaks. `models/knowledge/registered_scope.py`
is the §8 registered review scope's declaration — its snapshots, its followed edges with per-side
provenance, its membership, its manifest and its own construction refusal. `models/knowledge/family_review.py`
is the pipeline's vocabulary between the detector and the authored record: grouped facts, five separated
statuses, per-input currentness, the routing report and the one gate-consequence decision. Both are
**envelope-shaped additions**: neither brings a table, an identity mechanism or a storage contract, and
neither restates a schema `KS-R14@v1`, `KS-R15@v1` or `KS-R17@v1` already owns.

**The scope's five properties are shapes rather than rules a caller remembers.** `ScopeSnapshotDeclaration`
names the two sides a scope is declared over, and `FollowedScopeEdge` carries the side each result was read
from, so a cross-snapshot union is a *recorded lookup for candidate discovery* and never a claim that two
snapshots' relationships hold at once. Widening is a declared policy or it is nothing: the resolved
`(policy_id, policy_version_id, declared_version)` triple travels with the scope it produced, and a request
that declares no policy follows no composition edge. Membership is recorded, never inferred — nothing here
derives a member from prose, a label, a folder name, a path prefix or a symbol, and a path prefix compared
against a stored anchor path is a resolution fact this module cannot represent at all;
`scope_path_is_recorded` is the one path-shaped predicate it carries, and it decides exact recorded
equality. The registered scope is **not** the R07 read frontier: no field can hold a selected revision set,
a page cursor, a count of items remaining or an advertised expansion. And construction is total or it is
`ScopeConstructionRefusal`, naming the exact declared input it could not resolve — there is deliberately no
partial scope carrying an unresolved-input list, because "what a run over the scope could not resolve" is
`KS-R14@v1`'s half of the split. `SCOPE_CONSTRUCTION_VERSION` pins the declaration's own version, and **no
identity is minted here**: the scope is addressed by its declared `scope_id` and carries no content address,
logical digest or fingerprint of its own, so a `scope_manifest_ref` elsewhere points at that id and at
nothing derived from it.

**The pipeline vocabulary keeps five owners separate and refuses to carry a conclusion.**
`FamilyIntegrityFactGroup` declares no name from the detection schema's conclusion-bearing field set —
`KS-R14@v1`'s own review function is the measurement, and the case that protects it requires the empty
tuple — while `retains()` is the review that a merge lost nothing: grouping may merge matches, but every
matched condition and its supporting paths and edges are retained, and no field could hold a dropped match.
`SeparatedStatusReport` carries exactly one entry per owner in the declared order (`PIPELINE_STATUS_OWNERS`,
with `STATUS_OWNER_DECLARATIONS` and `STATUS_VOCABULARIES` giving each owner its own closed status
vocabulary and its own statement of what it does *not* establish), and there is no field anywhere in it for
one verdict, one badge or one boolean. Missing stays missing: an absent stored record is reported as
`no-record-recorded` and never as a favourable disposition, because the vocabulary has no "compatible"
member and no default. `FindingCurrentness` carries the recorded comparison's result, the identities that
moved and a typed statement that nothing was reinterpreted for the new inputs, and `FamilyReviewRouting`
carries the shipped actionability formula's three terms **beside** the family-review row count as a separate
number, with a field whose only admissible value names the validator that actually decides closeout
readiness (`CLOSEOUT_READINESS_DECIDER`) — a zero actionable count is necessary and never sufficient.
`FamilyReviewGateDecision` and its recorded instance `RECORDED_GATE_CONSEQUENCE_DECISION` make the gate's
consequence owned rather than implied. `FACT_GROUPING_POLICY_VERSION` and `FAMILY_REVIEW_ROUTING_SURFACES`
name the two declared policies the pipeline's composition is bound to.

**Two operations were added and no refusal code was.** `models/knowledge/result.py`'s `KnowledgeOperation`
union gained exactly two members — `construct_registered_scope` and `compose_family_integrity_report` — each
with its reason written beside it in the source, and `KnowledgeRefusalCode` was deliberately **not**
extended: a scope-construction refusal reuses the shipped codes, and a reader who saw the union grow and
inferred a new refusal vocabulary would be reading the wrong fact. That absence is recorded here rather than
left to a diff, because "this leaf needed no new refusal code" and "this leaf's refusal vocabulary was never
reviewed" must not read alike.

## 260915-KS-L20 The Five Query Views, The Closed Provenance Class, And The Projection Manifest

`KS-R20@v1` adds five modules to this route and **no record kind of its own**, which is the property worth
stating first: the views render the kinds `KS-R10@v1` through `KS-R19@v1` already store, and nothing here
mints an identity, a table or a content address.

**`models/knowledge/classification.py` is the whole answer to `Doc13:243`'s prohibition, and the answer is
data rather than vigilance.** The class set is closed at two members — `authored`, a stored record a named
author wrote carrying its author and its rationale, or `mechanical`, computed by a named versioned rule from
stored facts — and there is no `unknown`, no `null`, no `mixed` and no default. A value that cannot be
classified is **not emitted with an empty class**: the view layer reports it as an
`UnresolvedLimitation`. The rule set is closed and versioned: `MECHANICAL_RULES` is the registry,
`mechanical_rule` is the only way to obtain a rule, and a candidate rule that is not registered **raises**
rather than producing a classification, so no inline comparator can acquire a class by being spelled like
one. `Provenance` refuses a value carrying both an author and a rule, one carrying neither, and an authored
value whose stated reason is a mechanical rule — requirement 2.3's "the mechanical determination never
writes an authored record, and an authored determination never cites a mechanical rule as its reason" made
unrepresentable rather than documented. What the module deliberately does **not** have is as load-bearing as
what it has: no ordering comparator, no sort key, no score, no rank, no weight, no severity, no percentage,
and no field a caller could read as an assessment. `REGISTERED_ROLE_ORDER` is read from the vocabulary's own
declaration (`get_args(RealizationRole)`) rather than hand-copied, so a role added to the vocabulary cannot
silently acquire a position.

**`models/knowledge/view.py` declares the five views and makes three dishonest shapes unconstructible.**
`VIEW_NAMES` is `Doc13:235-239`'s list in that order — source context, invariant, family, review matrix,
curation queue — with no synonym, no sixth view and no view assembled at a caller's convenience, and the
payload's own `view` field says which one the caller got. Every row that orders or qualifies a value
carries a `Provenance` as a **sibling** field of that value (requirement 2.6), so a consumer can tell an
authored finding from a mechanical observation without knowing which renderer produced the payload; there is
no field anywhere below for a score, a rank, a weight, a severity, a percentage, a summary or a conclusion,
so a view cannot acquire one by accident. `ViewPayload._require_honest_bounding` refuses a payload that
returned a first page without a continuation **and** one that declares itself complete while carrying a
token, which is the structural form of "a bounded response never presents its first page as the entire
registered scope"; `ViewCompleteness` is scoped to the four inputs `Doc13:227` names and its field is
spelled `complete_within_declared_scope` so no reader can take it for a statement about the project's
semantics. `ViewCounts` carries all nine named quantities, each `counted` or `not_applicable` **with its
reason**, so a quantity with no meaning for a view says so instead of reporting a zero. And
`KnowledgeViewReader` is a runtime-checkable `Protocol` that is the only way this vocabulary obtains a row:
a view module has no path, no connection and no candidate tree, so "a view that opens the database directly
has left the contract" is a property of the type rather than a rule to remember. Its one addition for the
path-only front door is `ViewRequest.source_path`, the optional seed a caller who knows only a file can
present, and the field's validator constructs the shipped `PathSeed` rather than restating its rule — so a
path that no stored anchor could carry selects nothing by construction rather than by a lookup that happens
to miss, and the confinement rule stays in the one place the write path already spells it.

## 260915-KS-L32 The Read Request's Path Seed, And The Seeded Reads It Feeds

`models/knowledge/view.py` carries one new optional field on the read request. `ViewRequest.source_path` is
bounded by `PATH_MAX_LENGTH` and validated by constructing the shipped `PathSeed` rather than by copying its
rule, which is what keeps one spelling of "a confined repository-relative POSIX path" governing both the
write path that records realization anchors and the read seed that looks them up. The reason the field
exists at route altitude is that the seed is what makes the renderer's selection reachable from an ordinary
code hit: the application layer resolves the path to the revisions realized there and feeds both the
invariant view's selection and the family view's members and member locations from that one frontier, so a
caller no longer has to discover an invariant revision id or a family revision id before asking what governs
a file. An absent seed means "no restriction" and an empty realization set means "realized nowhere"; the two
are different answers and the model does not collapse them.


**`models/knowledge/projection_manifest.py` is the vocabulary the managed writer is judged against.** The
manifest is the only authority on ownership, so `ManagedOutput` and `RetainedOutput` are the two ways a
path can be owned and `ProjectionManifest._require_one_entry_per_path` refuses two owners for one path.
Every produced output records its stable identity, its source snapshot, its renderer version, its digest
**algorithm** and its byte count — a projection artifact without all of them is not constructible, which is
requirement 4.3 in shape. The refusal vocabulary is a closed seven-member list (`destination_escape`,
`destination_collision`, `escaping_link`, `unresolved_projection_input`, `manifest_unreadable`,
`destination_unavailable`, `unauthorized_overwrite`), the four discrepancy kinds are distinguished because
they call for different caller action, and the retention reasons are a closed five-member list. Confinement
is a pure function here (`require_confined_relative_path`) and collision detection is one
(`detect_destination_collisions`) so the writer can refuse **before** either output is written rather than
discovering the collision mid-publish. `DIGEST_ALGORITHM` is `sha256` because `SHA256_PATTERN` already
governs every digest that crosses the knowledge boundary; the manifest's digest is projection bookkeeping
about a file on disk, it is not a knowledge identity, it confers none, and nothing in the substrate reads it
as one.

**`models/tools/knowledge_responses.py` is the wire half, and its whole point is that it is one shape
rather than five.** Requirement 6.8 says a mounted tool's response payload is the same view payload
requirements 2 and 3 define, "not a second shape", so `knowledge_read` carries the view payload's own JSON
and this module adds only the envelope around it — a tool that re-rendered a view in its own format would be
a second renderer and therefore a second place for the classification rule to be violated. Each of the five
is a strict `ToolResponse` carrying a two-state discriminator (`view`/`result` or `refused`) with refusal
fields that name the offending input, so a handler cannot translate a refusal into an empty result or a
default; `KnowledgeIntegrityCheckResponse` carries `compatible: null` beside an explicit `unresolved` list
instead of manufacturing a verdict from a passing test.

## 260915-KS-L21 The Truth-Coverage Census Vocabulary, And Three Commands Added To The Closed Union

`KS-R21@v1` contributes one module to this route — `models/knowledge/census.py` — and edits one line-shaped
fact in `models/knowledge/candidate.py`. The route still adds **no record kind of its own**: the census's three
kinds are envelope records, and this module owns only their payload shapes.

**Three record kinds, and every prohibition on the vocabulary is a property of the declared fields.** The
inventory row, the assessable claim and the migration disposition are the three shapes. There is **no field that
could hold an inference**: no classification the parser could have computed, no verdict, no mismatch class and no
status derived from import success. `claim_kind` admits `unclassified` beside the four kinds `Doc12:65-70`
closes the taxonomy at, and `disposition` admits `imported`, `unmapped`, `unsupported`, `unreadable`, `retired`,
`historical` and `non_claim` — and **none of those is a verdict about whether a claim is true**. A semantic
status such as *supported*, *contradicted* or *unresolved* is a curator's authored `ReviewAssessment`, read by
the census and never written by it. `extra="forbid"` on the shared base is what refuses a payload arriving with
one.

**Provenance is a required stored value, not a report note.** `CensusProvenance` carries the artifact, the
location within it and the frozen baseline the artifact was read at, and **all three records require it** — a
record that could omit its provenance is a record whose claim is no longer addressable to its original text.
The baseline is a `SnapshotIdentity` rather than two loose strings, because the frozen baseline *is* one: the
packet requires an exact code revision and an exact memory revision recorded by identity, and `SnapshotIdentity`
is the shipped shape that records exactly that pair. Two artifacts examined at two baselines are two
observations, which is why the baseline is part of the record rather than a parameter of the run.

**No record carries an identity of its own beyond its key.** There is no content address, no logical digest and
no fingerprint field in this vocabulary, and the generation that declares these tables declares no such column
either: the census mints no second identity authority, and the content digest stays on `record_revision` where
the record envelope puts it. A case in this leaf's own suite inspects the declared columns for exactly that
absence.

**Three commands join the closed union, and the union is still closed.** `CensusInventoryRowCommand`,
`CensusClaimCommand` and `CensusDispositionCommand` are appended to `ProposedCommand`'s discriminated union in
`candidate.py`, and the six census tables are appended to `MutableRecordTable` — an inventory row, an
assessment-free claim, a migration disposition and the three relations they resolve through are each written by
a batch command, so an expectation, a duplicate check and a receipt all address one of these rows by its own
primary key. The command models are imported late, beside the other command modules, for the one-directional
reason that block already states: an import at this position resolves one way while the other side's own
annotation resolves the other. The module's own derived sets — `CENSUS_RECORD_KINDS`, `CENSUS_COMMAND_KINDS`,
`CENSUS_WRITABLE_TABLES` — are what the seam registry and the dispatch tables name, so the census answers for
its own membership rather than a count being edited in a test.

## 260915-KS-L22 The Review-Surface Vocabulary, And The Record Kind It Does Not Define

`models/knowledge/review.py` is this route's new vocabulary module, and the property that matters
most about it is a non-property: **it defines no record kind.** Every value in it renders records
another owner already stores, or states an absence where no record exists; the one thing it owns is
the shape of a display. The three pane names are declared once (`REVIEW_PANE_NAMES` = `knowledge`,
`source`, `evidence`) and `PROPOSED_ASSESSMENT_DISPOSITIONS` publishes the three dispositions the
existing curator authority accepts — as a statement about that authority rather than as a control of
this surface's own, so a reviewer can see which judgements are expressible. None of the three is
publication approval, and the payload's constructor refuses a disposition set that is not theirs.

The prohibitions are constructor checks rather than conventions a renderer is asked to remember.
`ReviewSideContent` refuses text unless the side is `present`, so a missing operand renders as a named
state (`absent`, `binary` or `unresolved`) and never as a blank that reads like an empty document.
`ReviewAssessmentDisplay` refuses an assessment displayed without its author or without the inputs it
examined, because an anonymous verdict and an assessment that examined nothing are not renderings of
a recorded assessment at all. `ReviewRemainingCount` refuses an unexplained absent count — `value` is
`None` exactly when the quantity has no meaning here, and the reason must then be stated — and refuses
a measured count that also carries a not-applicable reason, which is how a zero that means "none"
stays distinguishable from a zero that means "not measured".

The stale rule is structural at the payload. `KnowledgeReviewPayload` refuses a stale comparison whose
submission state is not `disabled_stale`, and refuses a current comparison whose submission claims to
be disabled for staleness: "an assessment is never submitted against a comparison that has moved" is a
property of the value rather than a rule a client is asked to honour. The same class keeps the
knowledge pane's own assessment one of the assessments it displays, and the evidence pane's two states
matched to the collections they carry — an empty corpus reported as `recorded`, or a populated one
reported as `none_recorded`, is a false statement about the evidence either way, and `assessed` is
false the moment there is no assessment to show.

One outcome per result closes the set. `KnowledgeReviewResult` carries either a payload or one typed
refusal, never both and never neither, so a caller that receives a refusal has no panes and cannot
read their absence as a review of an empty candidate. The refusals themselves are a closed **six**-
member union — the codes for an unresolved candidate, a non-live one, an absent dataset, an
unresolved **subject**, a refused comparison, and an unavailable adapter — each naming its detail, its
next action and, where one exists, the offending input.

**The entry half of the surface is three more declarations in the same module, and its rule is the
interesting one.** `ReviewSubjectKind` is the closed two-member `invariant`/`family` union, declared
**here once** so the transport's admission tuple, the entry list and the panes cannot come to disagree
about which identities are reviewable. `ReviewEntry` is the reviewed subject as the shipped comparison
selected it — a recorded identity, that identity's own label and the operation's count — with **no
field for a path, a file, a display version or a ranking**, which is what keeps "the browser never
chooses the candidate" a property of the value rather than a convention of its callers.
`ReviewEntryListResult` is the entry read's typed outcome, and its validator refuses a **refused** read
that offers any entry: "a refused entry read offers no subject; an entry beside a refusal is how a
caller comes to review a subject nothing admitted". Its empty `entries` on an `entries` state is
therefore a pair that selected no reviewable subject — a fact about the datasets, stated as one — and
not a disguised failure.

- The module's own non-definition: it defines no record kind. [227]
- The three pane names, declared once. [228]
- The dispositions the existing authority accepts, published rather than owned. [229]
- The present-side-requires-text rule. [230]
- The author and examined inputs a displayed assessment must carry. [231]
- The stale/submission coupling, checked at construction. [232]
- The unassessed-is-an-absence rule for counts. [233]
- One outcome per comparison result: a payload or one refusal. [234]
- **The two reviewable subject kinds, declared here once so the transport, the entry list and the panes cannot disagree.** [235]
- **The reviewed subject as the comparison selected it: a recorded identity, its own label and the operation's count, with no field for a path, a file, a display version or a ranking.** [236]
- **The entry read's typed outcome, whose validators refuse a refused read that offers any entry, non-zero totals beside a refusal, and a total smaller than the page beside it (`ICR-R09@v1`).** [237]
- The sixth refusal code, for a subject the resolution could not name. [238]
- **The seventh refusal code, added by this leaf: the generation a listing published no longer resolves to the two code objects it bound, so there are no bytes to serve for that entry.** [239]

## 260918-TSIP-L4 — The Response Models Stop Forbidding What Their Producers Emit

This route's subject in one sentence: **a strict response model that omits a key its own producer
emits rejects the payload after the write has already happened**, so the caller loses the envelope
that would have told it the work was done. This leaf swept all 84 registered models and repaired
seven instances, four of them in this route.

- **`models/worktree.py` gained `AtomicSeriesActivationReleaseFact` (`:181-201`)** — the terminal
  release evidence for the selected series (`state` ∈ `vacant`, `already-vacant`,
  `different-selection-preserved`, `unreadable-preserved`, `release-failed`, plus the optional
  error triple). It sits beside `AtomicSeriesActivationFact`, which the route already declared on
  `WorktreeSummary` and on the flexible `WorktreeCommandResponse` base.
- **`WorktreeOperationControlResponse.nextTool` was widened to its fourth reachable successor**
  (`:514-521`, `worktree_closeout_preview`), because
  `worktrees/integration/lifecycle/lifecycle_operations.py:498,508` already emitted it.
- **`models/lifecycles/finalize.py` — the `D53` repair.** `LifecycleFinalizeTaskResponse` declares
  `atomicSeriesActivation` (`:53`) and `atomicSeriesActivationRelease` (`:54`). It was the **only
  strict consumer** of that projection anywhere and the only one that had not declared it, which is
  why the terminal operation completed its transaction and then answered with a pydantic error.
- **`models/task_doc.py` declares `steps` (`:134`)** — the `read_steps` operation's payload, which
  the tool publishes as *the* way to read a checklist and which could never return.
- **`models/terminal.py` declares `strandedRowIds` / `strandedRowCount` / `surfacedRowId`
  (`:211-213`)** — the only report of an operator-inbox row surfaced while retiring a seat.
- **`models/operator_inbox.py` gained a typed refusal half** (`OperatorInboxPostStatus` at
  `:59`, `status` at `:75`, `detail` at `:101`, and a `model_validator` at `:103-116` making the
  four queued-projection fields required exactly when `ok` is true).
- **`models/structural/agent.py` declares both delivery keys on the shared
  `StructuralTargetResponse` base (`:86-87`)**, so all six consumers inherit them — the class
  repaired rather than the three instances.

The strict/flexible route model this overview describes is unchanged: the repairs **declare**
projections that were already being emitted. After them the corrected sweep reports exactly **2**
strict models forbidding a candidate key, both dismissed with their reasons at
`notes/reports/260918-TSIP-L4-worker-report.md` §5, down from 9 at this leaf's base.

## 260915-KS-L42 The Conflict Model Carries The Retraction Precondition The Offer Reads

**This route's impact is one literal, one field, and the function that reads them instead of the code.** `RetractionPrecondition` (`arriving_insertion` / `no_arriving_insertion`, published in this module's `__all__`) and `MergeConflict.precondition` (default `arriving_insertion`, consulted only for the row-less referential code) let a conflict record say whether the one row-less decision's retraction is available — because the conflict code cannot say it: the same `delete_reference_conflict` arrives when the arriving side added the broken reference and when it removed a row the retained side still cites, and `keep-left` on that code is a *retraction* of rows the arriving delta inserted, so only the first orientation can be settled by it. `expressible_decisions` now reads the measured field rather than inferring the offer from the code, and answers `("keep-left",)` where the precondition admits it and `()` where it does not.

**The default is not a fallback, and the order of the answers is load-bearing.** `arriving_insertion` is the default because it is true of every conflict that named a row, where the question never arises; the row-level question cannot be asked first for a row-less conflict, which has no table and no record id, so the precondition test comes before it. What did **not** change: the vocabulary still refuses half a row identity, a row-less decision still cannot overwrite anything, and `AuthoredReconciliation(decision="keep-left")` with no row still validates — the offer narrowed, not the vocabulary.

## 260915-KS-L43 The Merge Request's Authored Decision Becomes A Sequence

**This route's impact is one field on `MergeRequest` in `models/knowledge/merge.py`, and the field's plurality is a
measured repair rather than a generality.** `MergeRequest.reconciliation: AuthoredReconciliation | None` became
`MergeRequest.reconciliations: tuple[AuthoredReconciliation, ...] = ()`. The vocabulary beside it did not move:
`AuthoredReconciliation` still names exactly one row (or the one row-less shape), still refuses half a row identity at
construction, and `expressible_decisions` is still the single place that answers which decisions a conflict admits.
What changed is how many of those decisions one attempt may carry, and the reason is the loop: a retained merge is
answered one conflict at a time, a decision that settles the first reveals the second, and with only the newest
decision carried the two alternate forever — the caller is re-offered a decision it has already made and that has
already had its effect. Measured: twelve applications to the cap and no settlement before, two applications and a
settled merge after (`evidence/after-independent/recovery-progress-after.json` against `recovery-progress-before.json`).

**A sequence of one-row decisions is not a policy, and the model is where that could have gone wrong.** Every member
still names its own row, every conflict no member names is still refused exactly as it was, and there is still no
field meaning "prefer my side" — the shape simply lets a caller restate the decisions it has already made instead of
the merge forgetting them between attempts.

- The merge request's authored-decision channel, now a tuple of one-row decisions. [240]
- The vocabulary and its single admission point, unchanged. [241]

## 260915-KS-L44 The Two Realization Row Models Declare The Location They Were Already Being Handed

**This route's impact is two row models in `models/knowledge/view.py`, and the fields are declarations of a fact the pipeline already carried.** `FamilyRow` (`:822-859`) and `InvariantRow` (`:782-819`) now declare `role: RealizationRole | None`, `path: str | None` (bounded by `REFERENCE_MAX_LENGTH`) and `locator: SourceLocator | None`. A realization row of either view reported the claim id, the invariant revision id and the authored rationale and **no place at all**, so a caller could see that a realization existed without seeing where it is; the recorded location was already sitting on the candidate the projection had been handed, which is why the repair is three field assignments in the renderer rather than a derivation, and why nothing in this module had to change its meaning.

**Both models are one shape behind more than one row kind, and that decides the optionality — and the fields are not added where nothing can populate them.** `InvariantRow` carries the invariant view's `fact_kind="statement"` rows as well as its `realization` rows, so the three fields are optional and appear on statement rows as explicit `null`s, the same convention this module already had for `SourceContextRow.anchor_state` (produced by `knowledge_read_payload`'s `model_dump(mode="json")` with no `exclude_none`). `ReviewMatrixRow` and `CurationQueueRow` deliberately do **not** gain the fields: no candidate feeding either view sets a `path` or a `locator`, so there is no recorded location for them to drop and an added field would be a field nothing populates. `ViewSourceRow` is the reader port's own DTO rather than a rendered row and is outside this change.

## 260915-KS-L47 The Integrity Response's No-Verdict Position Is A Declared Field The Wire Omits

`models/tools/knowledge_responses.py`'s `KnowledgeIntegrityCheckResponse` keeps `compatible` declared
and always `None`, and its docstring now says both halves: the field is declared so the response
vocabulary carries the no-verdict position `Doc13:186` requires, and the shared response choke point
(`models/tools/tool_response.py`'s `finalize_tool_response`, over `ResponseModel.to_payload`) dumps with
`exclude_none=True`, so a caller sees the key **absent** rather than present-and-null. Absence means this
build reached no verdict, never that a verdict was suppressed; a producer that computed one would have
to put the key back. The `models/tools/knowledge_responses.py` sidecar states the same rule, and
`mcp/tests/test_knowledge_views_and_projection.py`'s two assertions were reconciled to it on the
developer's ruling that the incoming choke point wins: the stale `compatible is None` assertion is gone
and the no-run branch asserts `"selectedRunId" not in unnamed` rather than `is None`. **No other model
this route owns changed**, and no field was added or removed.

## 260921-ICR-L19 The Read-Files Response Carries The Repository's Published Intent

**This route's impact is one optional field on one strict response model (ICR-R19@v1).**
`ReadArFilesResponse` now declares `published_intent: dict[str, Any] | None = None` beside the
`repository_overview` / `route_overviews` front-door dicts. The application entry point populates it on
every call — its own `state` (`recorded` / `not-recorded` / `unusable`) is the answer, so `None` is the
field's declared default rather than a state the route produces.

**The shape is carried, not declared here, and that is the route boundary.** The selection contract — which
dataset is read, which seeds are used, which absences are named — belongs to
`application/published_intent.py`, so this module carries the block as a dict rather than re-declaring a
second contract for the same read. That is the same direction the front-door dicts already follow, and it
keeps the wire model from drifting into a duplicate vocabulary. `extra="forbid"` and the strict envelope
are unchanged, and no other model this route owns changed.

- **The new field, on the strict response model that declares it.** [242]
- **The owning module that decides the shape this model declines to re-declare.** [243]
- The strict envelope base the field joined. [244]
- The registry entry for the tool whose payload carries the field; unchanged by this leaf. [245]


## 260921-ICR-L2 The Review Wire Shape Carries An Inventory And An Absent Comparison

**Route meaning changed: the review payload can now describe a review that compared nothing, and it
carries the complete source change inventory either way.** `models/knowledge/review.py` gained
`ReviewChangedFile` (path, status, content kind, mode-change flag and a reason required exactly when the
content is unknown), `ReviewUnrepresentablePath` (the exact bytes of a name this surface cannot carry as
text) and `ReviewSourceInventory` (`state` measured/unavailable, the entries, a `listed_total` checked
against the list it describes, a `detail`, the reproducing `command`, both tree ids and the
unrepresentable remainder) — and `ReviewSourcePane.inventory` is now required and first.

Three optionalities and two states carry the rest of the change. `ReviewSurfaceRequest.selector` is
optional, and its **absence is the task context** rather than an empty subject. `ComparisonIdentity`
gained `knowledge_compared` and its three knowledge-half digests became optional, held all-or-nothing by
a validator. `ReviewKnowledgePane` gained `selection_state` (`subject_selected`/`task_context`) with a
reason required in exactly the second state, and `ReviewStaleness.state` gained `not_compared`.
`KnowledgeReviewPayload.comparison` became optional behind a validator that ties its absence to
`not_compared` **and** to the knowledge pane's answer, so a payload cannot disagree with itself about
which question it answered. `KNOWLEDGE_REVIEW_SURFACE_VERSION` stays `knowledge-review-surface/1`, and
the ruling is recorded beside the constant: `/1` admits both shapes, the change is additive for a client
that already requests the subject payload, and no version validator exists in this package to enforce a
bump.

- **The inventory's own model, with the count checked against the list and the rule that an unrepresentable path makes the inventory measured and partial.** [246]
- **The pane that now requires the inventory as its first fact, and carries the measured partition beside it.** [247]
- **The request whose selector may be absent, and the absence as a meaning rather than a default.** [248]
- **The comparison identity that states whether it compared knowledge, with the selector and both snapshot digests all-or-nothing.** [249]
- **The knowledge pane's selection state and its required reason, and the payload validator that holds it in agreement with the identity and the staleness state.** [250]
- **The third staleness state, which is the task context and not a flavour of current.** [251]
- **The surface version that stays `/1`, with the reasoning recorded beside the constant.** [252]
- The cases that measure the new states: a measured empty inventory beside an untouched comparison, and the structural rule that an inventory which could not carry a name is partial by construction. [253]


## 260921-ICR-L4 The Comparison Vocabulary Gains The Attribution Partition, And The Pane Carries It

**Route meaning changed: the attribution half of a review is one accounting, not two lists.**
`models/knowledge/diff.py` (634 → 892 lines) gained the partition vocabulary for ICR-R04@v1:
`ATTRIBUTION_GRANULARITY` (`changed_path`, the one granularity every attribution count is stated
at), `AttributionBucket` (three), `AttributionLink` (four — the two `outside` members are different
facts), `AttributionSideState` (three), `AttributionSide`, `ChangedPathAttribution` and
`SourceAttribution` with the disjoint-plus-exhaustive validator. `DiffOmissionReason` gained
`attribution_not_determined` and `DiffLimitation` gained `unknown_attribution_changed_paths` — two
limits, not one: the first says no valid registered attribution was established, the second says
that conclusion could not be reached at all. `models/knowledge/review.py` (836 → 857 lines) declares
the six persistent counts once as `ReviewRemainingCountName` and carries the partition on the pane
(`ReviewSourcePane.attribution` plus `unknown_attribution_changed_paths`), so a path appears in
exactly one of the three lists. The wire change is purely additive, so existing dashboard fixtures
still validate.

- **The one granularity, the three buckets, the four link labels and the three side states.** [254]
- **The partition value with its validator and its three bucket accessors, and one side's contribution beside it.** [255]
- **The two new closed-vocabulary members, and the model's own second producer of the undetermined limit.** [256]
- **The six counts declared once, and the pane that carries the partition.** [257]
- **The nine partition cases, and the unavailable-partition honesty case beside the partial-denominator case.** [258]


## 260921-ICR-L10 The Published Page Vocabulary, And The Constructor That Refuses A Remainder Without A Cursor

`260921-ICR-L10` (`ICR-R10@v1`) adds the review surface's page vocabulary to the review models.
`ReviewCollectionPage` publishes `collection`, `state`, `total`, `returned`, `remaining`, the owner's
opaque `continuation`, the active `scope`, `continued_from`, the reset refusal and `total_basis`;
`ReviewPagedCollection` names the two bounded collections once; `MAXIMUM_REVIEW_PAGE_SIZE` and
`REVIEW_PAGE_RESET_NEXT_ACTION` carry the surface's own bound and its new-generation action; and the
closed refusal-code union gained `comparison_page_reset` and `comparison_page_unreadable`, which are
different facts and are told apart by the owner's decoder rather than by their text.

**The two properties a later reader must not relax.** First, a page with a remainder cannot be
*constructed* without its cursor: the page value's own validator refuses `(remaining > 0) != (continuation
is not None)`, so the shape that produced "remaining=100 with no way to inspect them" is unrepresentable
rather than merely avoided. Second, `total_basis` says what `total` counts — `selection` for the
comparison, whose total is the whole selection on every page with `returned` cumulative over the walk,
and `walk` for the view, which measures its remainder from where the walk stands — because one rendered
sentence carrying two meanings is how `total` came to mean two different numbers.

`ReviewSurfaceRequest` gained `page_of`, `continuation` and `page_size`, and `KnowledgeReviewPayload`
gained `page` and `page_refusal`. The refusal is a **separate field** rather than an empty page: a page
value needs the owner's own counts and a refused read has none, so a page of invented zeros would be a
measured-zero lie about a read that did not happen.

## 260921-ICR-L26 The Applicability Vocabulary, And Five Display Models That Say Why

`260921-ICR-L26` (`ICR-R26@v1`, subject and comparison isolation) declares the attribution half's wire
vocabulary in a **new sibling module**, `models/knowledge/review_applicability.py` (222 L), beside the
other payload vocabularies, and re-exports it from `models/knowledge/review.py` so the names a reader
looks for stay where they were. `models/knowledge/review.py` is 1137 → 1174 lines.

**The vocabulary is an enforcement, not a container.** `ReviewApplicabilityClass` is the five supplied
collections spelled as the record-class vocabulary **minus its one measurement channel**, with an
import-time assertion proving the equality against `ReviewRecordClassName` so the two spellings cannot
drift. `ReviewDisplayedApplicability` carries a record's own recorded subject and the exact references
the treatment was decided from — `references` is required for **every** state, because a label that
names no recorded reference would be the surface's own opinion rather than a statement about the record
— and its validator refuses a `direct` or `historical` claim that names no subject, which is the F09
shape made unrepresentable rather than merely fixed. `ReviewContextRecord` is the packet's "related
family/closure context" clause as a value: true subject, the recorded relationship that reached it,
author/role and references, and **no** judgment content. `ReviewApplicabilitySummary` counts one
collection six ways and refuses a partition that does not account for every supplied record exactly
once, because a count that silently loses a record is how filtering becomes erasure. There is
deliberately no field for a similarity, a confidence, a score or a nearest match.

**Five display models gained an optional `applicability`** — `ReviewAuthoredEffect`, `ReviewSignal`,
`ReviewAssessmentDisplay`, `ReviewEvidenceLink` and `ReviewObservation` — and both panes gained
`context` (the labelled context rows) and `applicability` (the six-way counts), so the two panes that
display the same assessments cannot disagree about which of them may be displayed. Every addition is
optional and additive: a payload published before these labels existed still validates, and an absent
label means "this body states no treatment", never "this record is unrelated".

## 260921-ICR-L12 The Review Request Names Which Record It Is Addressed To

`260921-ICR-L12` (`ICR-R12@v1`) adds **one literal and one optional field** to this route's review
vocabulary: `ReviewHistoryRef = Literal["recorded"]` and `ReviewSurfaceRequest.history`. The single
value is the whole point — the surface addresses exactly one historical record, the leaf's own
published comparison generation, so there is no way to ask for a generation that is not this leaf's —
and the field's absence is the live review every caller already asks for.

**The vocabulary still defines no record kind.** The field names *which* record a read is addressed to
and carries no content of its own: the comparison, its panes, its channels and its refusals are all
rendered from records other owners store, and a historical read renders the generation's own recorded
content under exactly the same model shapes a live read uses. `models/knowledge/review.py` is 1189
lines after the addition, still under its 1200-line rail, and no limit was widened to admit it.

**A closed client vocabulary stays closed.** An absent field is the live review, so a client written
before this change asks for exactly what it asked for before; and an unknown spelling never reaches the
model at all — the transport refuses it in its own 400 vocabulary rather than letting the model's own
bound raise, which is why the request model's literal and the route's admitted value have one owner.

## 260921-ICR-L17 The Review Request Names The Comparison A Refresh Replaces

`260921-ICR-L17` (`ICR-R17@v1`) changes one model on this route:
`ReviewSurfaceRequest.previous_binding_digest` is a new **optional, sha256-shaped** field naming the
comparison the caller was already looking at when the read replaces that display.

Three facts a reader of this route should carry:

- **it is the *previous* identity, never a substitute for the current one** — it selects no dataset,
  resolves no candidate and is never rendered as the comparison; the composition only ever compares it
  against the comparison it rendered;
- **its absence is a state, not a default to fill in** — a read that carries none replaces nothing, which
  is `current` by construction;
- **its `pattern` is the digest's own published shape**, so a value that names no generation this surface
  could have published cannot be asserted as a previous input, and the route refuses a malformed spelling
  in its own vocabulary rather than raising out of the model.


## 260921-ICR-L22 The Rebinding Record's Vocabulary, And Three Display Models For The 1200-Line Rail

`260921-ICR-L22` (`ICR-R22@v1`, managed Git recovery rebinding) adds **one** module to this route and
moves two existing display models out of `models/knowledge/review.py` — one cohesive responsibility
relocated whole, so the payload module stays under the repository's hard rail while every name it
published keeps its home.

- `models/knowledge/review_sync_rebinding.py` (**390 L**) — **the typed record that binds one comparison
  generation to the source/knowledge pair a managed sync resolved.** `ReviewSyncRebinding` (`:193`) carries
  the generation it judges (id, index, binding digest and the digest of the manifest bytes that carried
  them), the reviewed source side beside the resolved one (the captured tree *and* the work-branch head the
  sync left, because a tree id alone does not say which commit the leaf now holds), each side's
  `SyncChannelMatch` (`:88` — `matches-reviewed-input`, `differs-from-reviewed-input`, `unmeasured`), the
  knowledge observation (`SyncKnowledgeObservation`, `:164`) and the reviewed knowledge state
  (`retained` / `not-recorded` / `not-selected`), plus its own self-consistency validator (`:242`), which
  re-derives every channel's verdict from the identities the record carries and refuses a record no owner
  could have produced — a forged `current` beside a differing tree, or a dataset identity for a generation
  that retained none, is refused at construction rather than repaired at read time.
- **The verdict vocabulary, and why it is three-valued.** `ReviewSyncRebindingVerdict` (`:97`) is
  `current` / `moved` / `unmeasured`. `current` is the **only** value that claims the generation still
  describes the resolved pair, so it requires a *measured* match on every channel the generation actually
  retained: a comparison the review never made must never read as agreement, and a generation that
  retained no knowledge operand may still be `current` on the code channel alone. `moved` is a measured
  difference on either channel. `unmeasured` is neither and is not a softer `moved`: the declared
  publication location held nothing this code could read, so the pair's knowledge half is simply unknown —
  and the validator refuses that value beside a location that did hold a readable dataset.
  `review_sync_verdict` (`:142`) derives the value, while `code_channel_match` (`:107`) and
  `knowledge_channel_match` (`:120`) are the pure comparisons that derivation and the validator share. The
  record's version is a literal of this vocabulary's own (`ar-review-sync-rebinding/v1`, `:76-78`) and its
  selection rule (`latest-published-generation`, `:82`) is spelled here rather than read from the producing
  owner at run time, so two records from different layouts are distinguishable from the records themselves.
- **The 1200-line rail's extraction, and what did and did not change.** `models/knowledge/review_staleness.py`
  (**204 L**) is new and owns the surface's own state about its inputs: `ReviewStaleness` (`:51`) and
  `ReviewSubmission` (`:190`) moved out of `models/knowledge/review.py` **verbatim** — all 35 of their
  non-blank lines appear byte-for-byte in the new module, so one implementation of each rule still exists
  and no behaviour travelled with the text — beside the new `ReviewSyncMovement` (`:85`, validator `:132`)
  and its four-valued `ReviewSyncMovementState` (`:48`: `current` / `stale` / `not-measured` /
  `unavailable`, where only `current` claims agreement and the two absences carry the reason behind them).
  The reason is the rail and nothing else: `review.py` was **1198 lines** against the 1200-line hard rail,
  so the movement vocabulary could not be added there without making it a new offender.
  `models/knowledge/review.py` is therefore **1198 → 1164 lines**: it re-exports all three names
  (`:61-65`), its `__all__` gained exactly `ReviewSyncMovement` (`:121`), and its payload
  `KnowledgeReviewPayload` gained one optional field, `sync_movement: ReviewSyncMovement | None = None`
  (`:1026`) — `None` meaning "no managed sync has reported", which is deliberately a different fact from a
  reported agreement, and a stale movement is folded into `staleness` beside it so a review whose inputs a
  sync moved can never read as current.

## 260921-ICR-L31 The Family-Context Vocabulary And The Third Paged Collection

**This route gained one value module and two additions to an existing one (`ICR-R31@v1`).**
``mcp/src/agents_remember/models/knowledge/review_family_context.py`` is the vocabulary for the
comparison-bound family context: one family revision's authored guarantee with its provenance and seal;
one membership row carrying its exact member revision and the other family revisions that revision is
recorded in; the read owner's own roster page with its counts, its completeness and the cursor that
reaches the rest; one snapshot's side context; one family's entry with its selection and its candidate
guarantees; and the context itself with its measured counts and its references into the evidence and
assessment owners' own collections. Four side states are four distinct facts — ``recorded``,
``not_recorded``, ``not_resolved``, ``unreadable`` — and none of them is an empty roster;
``no_family_recorded`` is a measured zero of the family population and its validator refuses it any
entries.

``models/knowledge/review.py`` changed twice in the same direction: ``ReviewPagedCollection`` and
``REVIEW_PAGED_COLLECTIONS`` now name a third bounded collection (``family_members``), and
``KnowledgeReviewPayload`` carries the required ``family_context`` field so an absent field can never be
read as a measured zero.

**The reopen corrected one reading of the roster page, and it is a *reading* rather than a new field.**
``complete`` on ``ReviewFamilyRosterPage`` describes the read **walk and not the page**: a multi-page walk
completes on its **final** page, and that page carries only its own share of the selection. So a complete
page is *the roster, whole* exactly when it is also a single page (``state == "first_page"``), and
``ReviewFamilyRevisionContext``'s validator holds only that case to the revision-wide member count; a
completed **continued** page is a position in a walk and is accepted, while the same carried rows on a
walk's first page are still refused as the truncation that guard exists for. Nothing else in this route
moved: no value gained or lost a field, no ``Literal`` state changed, no signature changed, and
``complete``'s own meaning — the read owner's own ``enumeration_complete`` — is untouched, because this
module reads that flag and never writes it. The side context's own class docstring was corrected on these
bytes to match, because its older sentence still read as though a complete page always carried the whole
roster.

## 260921-ICR-L47 The Changed-Intent Summary Model

`models/knowledge/` gains [`review_intent_summary.py`](knowledge/review_intent_summary.py.md), the typed
vocabulary of the task entry's `Intent review +N −N` (`ICR-R24@v3`). `ReviewIntentSummaryResult` is
`counted`, `partial` or `unavailable` and carries **exactly one** of counts or the owner's refusal, so an
unread comparison cannot be serialized as a measured `+0 −0`; `ReviewIntentCounts` makes `added`/`removed`
equal to the sums of their per-kind parts (invariants, joint guarantees) and keeps `realization_only`,
`membership_only` and `unresolved` outside plus/minus. Like the sibling review models it selects and
compares nothing; the application owner computes the numbers.

- The counts and their sum check. [259]
- One outcome per state. [260]

## 260928-MIK-L21 The Text Knowledge Format: A New Model Package, `knowledge_files/`

`models/knowledge_files/` is a new sub-package that declares the text knowledge format (MIK-R21@v1,
Doc14): the files under `knowledge/` and the JSON sidecars under `onboarding/` that become the source of
truth for knowledge at MIK-R37. It is separate from `models/knowledge/` on purpose: those models describe
the SQLite store (UUID- and digest-shaped), these describe files a person can read and merge. It reuses
only the shipped limits, `GIT_OBJECT_PATTERN`, `require_plain_git_path` and the packet-version pattern.

| Module | Owns |
| --- | --- |
| [`__init__.py`](knowledge_files/__init__.py.md) | the format map, the `[n]` marker/escaping rule, the public re-exports |
| [`ids.py`](knowledge_files/ids.py.md) | kind prefixes; random 6-character minted IDs; 8-character IDs derived from legacy identity (golden-pinned) |
| [`shapes.py`](knowledge_files/shapes.py.md) | `FileModel` (frozen, extra-forbidden, explicit `null` refused); anchor `{path?, locator, blob, content}`; references with typed targets; links; admission; origin |
| [`records.py`](knowledge_files/records.py.md) | the ten `ar-<kind>/v1` records, per-kind relation vocabulary, one owner per relationship |
| [`sidecars.py`](knowledge_files/sidecars.py.md) | file and route sidecars, realization/proof entries, the layout marker |
| [`documents.py`](knowledge_files/documents.py.md) | locations and `schema` dispatch |
| [`canonical.py`](knowledge_files/canonical.py.md) | the canonical JSON formatting (formatting only; content-changing input refused) |

The sub-package has no route overview of its own, like its sibling `models/knowledge/`: this overview
governs its cards. Every model checks **shape only**; integrity (IDs resolve, markers match, one owner per
relationship across files) is the validator's (MIK-R22). Nothing in the installed runtime imports it; its
only production consumer is `cli/knowledge_format.py`.

- The package map and the shape-only boundary. [261]
- The base every file model inherits. [262]
- An invariant record carries no second-owner fields. [263]
- Schema dispatch refuses unknown schemas. [264]

## 260928-MIK-L07 Per-Leaf History Files Join `knowledge_files/`

`models/knowledge_files/` gains an eighth module, [`history.py`](knowledge_files/history.py.md)
(MIK-R07@v2): the `ar-history/v1` file at `knowledge/history/<owner-id>.json`, one per leaf, wave or
crossing, holding the curator's judgment rows. Invariant rows (`changed` | `moved` | `deleted` |
`extended` | `no_impact`) carry the covered entries with their before/after anchors, the invariant's
revision and effect; family rows (`changed` | `rerouted` | `assigned` | `retired` | `no_impact`) carry the
members examined at their revisions. A row's kind is dispatched by its subject through a registry later
packets extend. A file that is closed on any base side must stay byte-identical: the module owns that
predicate, the validator (MIK-R22) and the closeout (MIK-R09, live from MIK-R37) apply it.

The existing modules changed only to take the new file in: [`ids.py`](knowledge_files/ids.py.md) adds
the `ROW-` row kind and the entry/row ID patterns; [`documents.py`](knowledge_files/documents.py.md)
registers the schema and adds `parse_history_document`, which binds a file's name to its owner;
[`canonical.py`](knowledge_files/canonical.py.md) sorts `covers` and `examined` by `id` as it already did
`rows`; [`__init__.py`](knowledge_files/__init__.py.md) re-exports the new public names. Nothing in the
installed runtime imports the package yet, so production behavior is unchanged.

- The history file: one owner, one row per subject, a strict `closed` flag. [265]
- The row-kind registry: `invariant`, `family`, since MIK-R24 MIK-R30's `onboarding_trace`, since MIK-R11 `planned`, since MIK-R10 `unexplained`, and since MIK-R14 `reconsideration`. [266]
- The freeze predicate. [267]
- The history schema in the dispatch table. [268]
- The history row ID kind. [269]

## 260928-MIK-L23 The Knowledge Tool Responses Name A Memory Tree

**Route impact (MIK-R23@v1).** [`tools/knowledge_responses.py`](tools/knowledge_responses.py.md) gains
optional, response-side fields: `memoryTree` and `indexComplete` on `KnowledgeReadResponse` and
`KnowledgeProjectResponse`, and `memoryTrees` (`before`/`after`) plus `indexComplete` on
`KnowledgeDiffResponse`. They name the converted memory tree a read went through (root, tree key, index state,
problems) and say whether its index was complete; they default to `None` and are absent from the wire for a
database. No input model changed. `ReadArFilesResponse.published_intent` stays a dict, so the published block's
new `memoryTree` and per-page `indexState` travel in it without a new declaration here.

- The optional memory-tree fields on the three responses (the read response re-read at MIK-R05's `routeChain`). [270]
- The docstring rule: a memory tree is named, never hidden, and a partial index is never presented as complete. [271]
