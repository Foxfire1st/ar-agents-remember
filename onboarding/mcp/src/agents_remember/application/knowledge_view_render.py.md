# mcp/src/agents_remember/application/knowledge_view_render.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_view_render.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T15:30+02:00 |
| lastVerifiedCommitHash | `5d64af264dc89b51d5c5e6454216573abde3c12e` |
| lastVerifiedCommitDate | 2026-09-20T02:50:22+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l32-ar`, uncommitted; base `7dcec036094768c5f50e571fb45e59a27ae78efc` |
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

The five views rendered deterministically over the reader port, with their provenance classes: the
module the whole leaf exists for, whose docstring states that "Everything before it settles vocabulary
and everything after it transports bytes; here a view decides what it selects, how it orders it, and --
the clause the packet calls the one this leaf exists to close -- **which of the two provenance classes
every ordered value carries**." It does **not** open a database, hold a connection, or keep any state
between calls: its only non-stdlib imports are two sibling model modules
(`models/knowledge/classification.py` and `models/knowledge/view.py`) plus `collections.abc` and
`dataclasses`, and it *deliberately does not have* a third provenance class, a default order, a
fallback comparator, an actionable count, a clock read, or any way to emit a value whose classification
it could not determine. It also has no validation of the stored determinations it reads: a decision
facet's outcome is taken exactly as recorded, and an outcome that is not canonically spelled is not
guessed at — the row is withheld and reported as an unresolved limitation instead.

## Code Commentary

### Logic

**Four properties are enforced together, because the docstring's own premise is that a renderer
satisfying three of them will lose the fourth.** Ordering comes from one of the four admitted inputs and
it is named: `order_candidates` is described as "the only ordering path", dispatching on the request's
admitted input through `MECHANICAL_RULES`' four registered ordering rules and reporting per position
which input produced it and whether that input is authored or mechanical. A value that cannot be
classified is withheld, not emitted: `_classified` returns `None`, and the caller turns that `None` into
an `UnresolvedLimitation` rather than a row. The declared tiebreak is the only lexical order: when every
declared key ties, positions are assigned by record identity ascending under
`ordering.declared-tiebreak`, reported `mechanical`, and "Nothing here reads a symbol name's spelling, a
path prefix, a directory depth, a file extension or a repository location, and nothing here reads
another view's result." Two runs at one snapshot are byte-identical, because every input is a recorded
value or a registered constant and "nothing is read from the clock, the environment, the filesystem or a
live count that a page boundary could move."

**`order_candidates` is the only ordering path, and an unadmitted input raises instead of degrading.**
It first calls `require_admitted_ordering_input`, and when that returns a refusal it raises
`UnadmittedOrderingInput` — a `ValueError` subclass, documented as "An ordering request named none of
the four admitted inputs, so no rows are returned" — so "a refusal here means the caller receives no
rows at all rather than a default order. There is no fallback comparator in this function and no
database order that survives it." Two checks guard the same property at different layers:
`knowledge_views._admit` screens `request.ordering_input` against the imported `ORDERING_INPUTS` before
any row exists, and `knowledge_views._render` catches the exception the renderer raises and converts it
back into a typed `ViewRefusal`. `order_candidates` is exported in `__all__` and has exactly one caller
in the shipped candidate, `_render` inside this same module.

**The withholding branch is one `None`, and two callers turn it into two different recorded things.**
`_classified` has "the two branches are the whole closure": a candidate whose own content is a stored
record with a named author yields `Provenance(provenance_class=AUTHORED_CLASS, ...)`; a candidate a
registered rule produced yields `mechanical_provenance(*candidate.mechanical_rule_id)`; anything else
returns `None` and "is not returned." Inside `order_candidates` that `None` becomes an
`UnresolvedLimitation` with `code="unclassified_value"` and the subject spelled
`f"{record_kind}:{record_id}"`; the five renderers then pass `ordered.limitations` into the seam, whose
`_counts` counts those withheld rows in `unresolved_references` "rather than dropped, because a withheld
row is an unresolved input and not an absent fact." Requirement 2.1's forbidden third class, null and
default are therefore unrepresentable rather than merely absent, and `_classified` is a closure over two
members, not a lookup that could grow a third.

**The total order is the declared key tuple and then record identity, and the tiebreak's identity is
stated as a constant.** `_sort_key` returns `(keys, candidate.subject.record_id,
candidate.subject.revision_id or "")`, so the final terms are never a recomputed score, and
`_ordering_keys` builds the declared member per admitted input: a recorded
`declared_priority:` position prefixed with a `0` sentinel, a `1` sentinel with the tiebreak's own
mechanical provenance for a subject recording no priority, `REGISTERED_ROLE_ORDER.index(role)` with
`len(REGISTERED_ROLE_ORDER)` for an unknown role, and `sum(trigger.encode("utf-8"))` for the recorded
trigger identity. `_rules_used` names "Every registered rule id this ordering touched, tiebreak
included" — the tiebreak plus at most one of `ordering.declared-priority`, `ordering.registered-role`
and `ordering.trigger-rule`, sorted and deduplicated — and `_position` wraps `index + 1` through
`ordering_position`, which validates against `ORDERING_PROVENANCE_RULE`'s declared
`("ordering.declared-tiebreak", 1)` so a position cannot name an unregistered rule. The class a position
carries is the class of the *input*, and for `declared_priority` that is
`authored_provenance(decider, reason)` read from the facet that recorded the position.

**Two runs at one snapshot are byte-identical because nothing in the module reads live state.**
`_page` slices an already-ordered sequence and returns the next offset, so a page boundary cannot move an
ordering decision; the reader port beneath it caches the rows of a record kind for the reader's lifetime,
"so two views built over one reader cannot disagree about the rows of a kind merely because a write
landed between them." Combined with the total order of the previous paragraph — a total order over
identities, which the docstring says means "two runs at one snapshot cannot disagree" — the selection,
the ordering and the row content are all functions of recorded values and registered constants. The
shipped conformance check is the differential that renders every view twice at one snapshot and compares
`payload.model_dump_json()`; nothing in this module records a run id, a duration or a timestamp.

**The authored side is an intake decision: an authored claim is a stored `decision` facet of an
already-registered kind.** `DECISION_FACET_KIND` is `"decision"` — the facet kind of `KS-R11@v1`'s
`DecisionPayload`, whose `decider`, `reason` and `outcome` are the fields `authored_decision` reads — and
the docstring records the reason: an authored no-consequence claim must be a *stored* record while the
packet's Exclusions forbid a new canonical record kind, so it is carried inside this existing one. The
two canonical outcome prefixes are `PRIORITY_OUTCOME_PREFIX = "declared_priority: "` and
`NO_CONSEQUENCE_OUTCOME_PREFIX = "no_consequence: "`, and the module's comment states why they are read
at all: "Both are recorded scalars on a registered payload field, so a priority is never scraped out of
prose." An outcome that is not canonically spelled is deliberately not read as a priority —
`AuthoredDecision.priority_position` requires `spelling.isdigit()` and `spelling == str(int(spelling))`
and a positive value, otherwise returning `None` — and `_priority_of` returns a position only when
exactly one distinct one is declared among a subject's decisions, so two competing declarations order
nothing rather than picking a winner. `_declared_priority` reads the candidate's own recorded priority
field, and its docstring says why no lookup happens: "A priority facet attached to another record does
not order this one."

**Each view has its own renderer, and the only differences between them are the selection and the row
shape.** `render_source_context` collects realization claims, plus the authored decisions of one
invariant revision when the request names one, distinguishing `authored_responsibility` from
`diagnostic_evidence` by `is_no_consequence`. `render_invariant` filters `reader.invariant_rows()` by
`request.invariant_revision_id` and pairs each with its attachment rows through `_decisions_for`, then
adds realization claims — and it adds only the realization rows whose revision the same filter selected,
because a realization answers "where is this realized" and one realizing an unselected revision is a
different subject's answer rather than a second view of this one. `render_family` keeps "member-record and attributed-source changes apart" by
setting `change_locus="member_record"` for a family revision and for each of its members, and
`change_locus="attributed_source"` for those members' own realization loci and for the recorded detection
signals. The joint guarantee is no longer the whole answer here: a caller asking which obligations a
family admits -- and where they are implemented -- is shown the member rows this read selected and the
locations those members name, and nothing outside that frontier. `render_review_matrix` defaults to the six requirement/effect/preservation/
question/evidence/observation kinds, preserves recorded references as `assessment_ids`, and attaches
`_consequence(candidate)`. `render_curation_queue` emits machine work items and separately attributed
curator dispositions in two shapes and, per its own docstring, "computes no actionable count" because a
count of "actionable" work "would be the semantic conclusion this leaf is forbidden to generate." All
five share one body: order, assert that every paged candidate has a class, build the row, and return
`(rows, ordered.limitations, ordered.rule_ids, len(ordered.ordered))` — the fourth element being the
selection's own size, so a page cannot report a scope smaller than the walk it is a page of.

**The small helpers each name one fact, and the module is otherwise pure.** `_rules_used` returns the
rule ids one ordering touched with the tiebreak always included; `_position` is "One ordered position
carrying the class of the *input*, not of the row's content"; `_consequence` returns a
`NoConsequenceStatement` built from an authored claim's own recorded text or from a mechanical rule,
never a mixture; `_page` returns one page and the offset the next page starts at. The two internal
working types are frozen dataclasses rather than models — `Candidate` is "One row a view may emit,
before ordering and before classification" and `OrderedSet` is "The outcome of one ordering pass: the
ordered candidates and what could not be classified" — while every row that leaves the module is a
shipped model (`SourceContextRow`, `InvariantRow`, `FamilyRow`, `ReviewMatrixRow`, `CurationQueueRow`)
and the port it reads through is the shipped `KnowledgeViewReader`. `__all__` names thirteen public
names — the facet-kind constant, the two outcome prefixes, `Candidate`, `OrderedSet`,
`UnadmittedOrderingInput`, `authored_decision`, `order_candidates` and the five `render_*` functions —
leaving the other module-level functions private: 34 module-level functions and four classes in total,
with no class of its own beyond those four. Three of those private functions are the front door's own
seam: `_seed_revisions` resolves the request's optional source path to the revisions realized there
(`None` meaning "no restriction", an empty set meaning "realized nowhere", which is an answer and not a
fallback to everything), and `_family_members` and `_member_locations` apply it to the family view's
membership rows and to the locations those members name.

### Conventions

Every emitted shape derives from `KnowledgeModel` in the models layer, so `extra="forbid"` and
`frozen=True` are what make an undeclared field impossible rather than merely discouraged; this module
declares no model base of its own and constructs the shipped row and payload types instead. The two
provenance classes are imported rather than spelled locally — `AUTHORED_CLASS`, `MECHANICAL_CLASS` and
`CLASSIFICATION_CLASSES` come from `models/knowledge/classification.py`, where the class set is derived
from its literal, and the module builds provenance through the shared constructors `authored_provenance`
and `mechanical_provenance` rather than instantiating `Provenance` itself. The four admitted ordering
inputs, the ordering vocabulary and the mechanical registry belong to that same module and are imported
(`OrderingInput`, `ORDERING_INPUTS`, `REGISTERED_ROLE_ORDER`, `MECHANICAL_RULES`); the module re-declares
none of them, and its `_ordering_keys` dispatches on the same four literal names the registry carries.
Bounded lengths are not restated either: identities, statements, paths and conditions travel in models
whose own fields already declare the bound. Three rule identities used to classify generated content are
module constants — `DETECTION_RULE = ("ordering.trigger-rule", 1)`, `CONSEQUENCE_RULE =
("consequence.record-payload-byte-equal", 1)` and `REGISTERED_ROLE_RULE = ("ordering.registered-role", 1)`
— so a rule version is not re-typed at each use. The third is the rule the two membership-derived row
shapes are classified under: a `family_member` row and a member's realization row are recorded rather
than authored (the membership edge carries both revision ids and its own provenance), so they are
mechanically determined and name the registered rule that determined them rather than an author, exactly
as a trigger-derived row names `DETECTION_RULE`. The curation queue's `DISPOSITION_VOCABULARY_VERSION` names the vocabulary it states on every machine item.
`UnadmittedOrderingInput` is deliberately a `ValueError` and not a refusal model, because the caller has a
programming defect rather than a data condition. `__all__` is the module's public surface: the thirteen
names listed above, with the constants that could be mistaken for local spellings included so a reader
finds the canonical owner.

### Invariants And Boundaries

- **An unadmitted ordering input produces no rows.** `order_candidates` raises
  `UnadmittedOrderingInput` before any candidate is touched, `_admit` screens the same input against
  `ORDERING_INPUTS` before anything is opened, and `_render` converts the raised error into a
  `ViewRefusal` with `code="unadmitted_ordering_input"`; no fallback order exists on either path.
- **A value with no class is withheld, and its withholding is reported.** `_classified` returns `None`
  for a candidate with neither an authored record nor a registered rule, and each renderer returns the
  resulting `UnresolvedLimitation` tuple in its second position, so a withheld row can never appear as an
  empty class, a null, or a default.
- **Ordering is total and it is reproducible.** `_sort_key` ends in record identity and revision
  identity, `_rules_used` includes `ordering.declared-tiebreak` on every ordering, and `_position`
  routes through `ordering_position`, which validates against `ORDERING_PROVENANCE_RULE` — the declared
  `("ordering.declared-tiebreak", 1)`.
- **A realization row is emitted only for a revision the same read selected.** Both selection paths
  apply one frontier: the invariant view appends a `reader.realization_rows()` row only when its
  `revision_id` is in the set the invariant loop selected, and the family view appends one only when its
  `revision_id` is a member that loop just emitted. A location belonging to another invariant — or to
  another family's member — is a different subject's answer, and reporting it would attribute a location
  to a statement this view did not select. With no seed and no revision named the frontier is every
  revision, which is the broader view this operation already offered.
- **The path seed restricts by realization, and its absence is not an error.** `_seed_revisions` returns
  `None` when the request names no source path (every existing caller's behaviour is unchanged), the set
  of revisions realized at that path when it does, and an empty set when the path is recorded as realized
  nowhere — which selects no rows and is reported as a selection of nothing rather than being widened
  back to everything. The seed is not a second selection vocabulary: it is validated by the shipped
  `PathSeed` on the request model, so a spelling the write path refuses cannot become a read seed.
- **The module holds no I/O and no durable state.** Its imports are `collections.abc`, `dataclasses` and
  two model modules; it opens no connection, reads no path, holds no module-level mutable value, and
  therefore cannot disagree with itself between two calls at one snapshot.
- **A row is emitted only after classification.** Every renderer asserts the class of each paged
  candidate before building its row, so a row that reaches a payload always carries exactly one of the
  two provenance classes.
- **The seam re-derives the page offset from the continuation token, and the renderer's own next offset
  is discarded.** `_render` computes `next_offset` and each renderer binds it to `_next` without using
  it, while `knowledge_views._render` parses the token's last `:`-segment to recover the position — a
  real coupling across the two modules that a reader of either alone would miss.
- **The curation queue computes no actionable count and fills no per-row limitations.** No function here
  writes `CurationQueueRow.limitations`; unresolved rows are reported through the payload's
  `limitations` instead, and `design/retrieval-review-design.md:348` is cited in the renderer's docstring
  as the rule that keeps the review section report-only. That design file is not present in this code
  worktree, so the claim is anchored to the renderer's own docstring rather than to the design document.
- **The module adds no verification authority.** It reads recorded determinations as recorded, refuses to
  parse a non-canonical outcome into a priority, and never converts its own read into a statement about
  what the knowledge means.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Everything this card asserts is checkable inside the shipped candidate: the module's own docstring and
constants, the two model modules it imports its vocabulary and provenance classes from, the reader port
it consumes, the seam that calls it, and the cases that protect its properties — the determinism
differential in one test file and the ordering-and-admission cases in the other. The design document the
renderer's docstring cites by path lives outside this code worktree, so it is quoted as the module's own
statement rather than cited as a file.

| Finding | Anchor | Source |
| --- | --- | --- |
| The docstring that states the four properties together and the CR20-6 intake decision behind the authored side. | `order_candidates`; `_classified` | mcp/src/agents_remember/application/knowledge_view_render.py:1-38 |
| The differential that renders every view twice at one snapshot and compares the payload bytes. | "def test_every_view_renders_two_byte_identical_runs_at_one_snapshot(" | mcp/tests/test_knowledge_projection_vault_safety.py:281-281 |
| The registered facet kind the authored claim is carried in, with the two canonical outcome prefixes and the three payload fields `authored_decision` reads. | `DECISION_FACET_KIND`; `PRIORITY_OUTCOME_PREFIX`; `NO_CONSEQUENCE_OUTCOME_PREFIX`; `DecisionPayload`; `outcome`; `decider` | mcp/src/agents_remember/application/knowledge_view_render.py:80-101; mcp/src/agents_remember/application/knowledge_view_render.py:99-101; mcp/src/agents_remember/models/knowledge/facet.py:91-103; mcp/src/agents_remember/application/knowledge_view_render.py:96-98; mcp/src/agents_remember/models/knowledge/facet.py:101-103 |
| The three generated-content rules the module classifies under: a recorded trigger identity, a payload byte-equality consequence, and the registered rule a membership-derived row names. | `DETECTION_RULE`; `CONSEQUENCE_RULE`; `REGISTERED_ROLE_RULE` | mcp/src/agents_remember/application/knowledge_view_render.py:104-106; mcp/src/agents_remember/application/knowledge_view_render.py:104-104; mcp/src/agents_remember/application/knowledge_view_render.py:105-105; mcp/src/agents_remember/application/knowledge_view_render.py:106-106 |
| One authored determination read from a stored facet — the canonical-spelling rule that decides whether it is a priority at all, and the reader that turns one facet row into it with the envelope actor used only when the payload is silent. | `AuthoredDecision`; `priority_position`; `is_no_consequence`; `no_consequence_detail`; `authored_decision` | mcp/src/agents_remember/application/knowledge_view_render.py:101-136; mcp/src/agents_remember/application/knowledge_view_render.py:139-163; mcp/src/agents_remember/application/knowledge_view_render.py:137-137; mcp/src/agents_remember/application/knowledge_view_render.py:138-141 |
| The pre-classification working type and the ordering pass's outcome, both frozen dataclasses rather than models. | `Candidate`; `OrderedSet` | mcp/src/agents_remember/application/knowledge_view_render.py:176-212 |
| The declared key each admitted input produces (including the sentinel that orders an unprioritised row after every prioritised one and the rule that the priority is read from the candidate's own subject), and the exception that replaces a default order with its raise site and the two-member class closure the caller turns into a recorded limitation. | `_ordering_keys`; `_declared_priority`; `return (1,), mechanical_provenance("ordering.declared-tiebreak", 1)`; `UnadmittedOrderingInput`; `order_candidates`; `_classified` | mcp/src/agents_remember/application/knowledge_view_render.py:203-211; mcp/src/agents_remember/application/knowledge_view_render.py:214-247; mcp/src/agents_remember/application/knowledge_view_render.py:257-296; mcp/src/agents_remember/application/knowledge_view_render.py:325-344 |
| The total sort key ending in record identity and the registered rule ids an ordering touched. | `_sort_key`; `_rules_used` | mcp/src/agents_remember/application/knowledge_view_render.py:299-322 |
| The position that carries the class of the input, and the no-consequence statement built from either branch with its paging helper. | `_position`; `_consequence`; `_page` | mcp/src/agents_remember/application/knowledge_view_render.py:357-361; mcp/src/agents_remember/application/knowledge_view_render.py:363-380; mcp/src/agents_remember/application/knowledge_view_render.py:382-390 |
| The attachment read that fetches a subject's own decisions, and the rule that only one declared position may order. | `_decisions_for`; `_priority_of` | mcp/src/agents_remember/application/knowledge_view_render.py:386-416; mcp/src/agents_remember/application/knowledge_view_render.py:431-431; mcp/src/agents_remember/application/knowledge_view_render.py:431-438 |
| The per-view selection functions and the five renderers they feed, each returning rows with the limitations, the rule ids and the selection's own size. | `_invariant_candidates`; `_family_candidates`; `_review_candidates`; `_curation_candidates`; `render_source_context`; `render_invariant`; `render_family` | mcp/src/agents_remember/application/knowledge_view_render.py:465-531; mcp/src/agents_remember/application/knowledge_view_render.py:580-621; mcp/src/agents_remember/application/knowledge_view_render.py:709-738; mcp/src/agents_remember/application/knowledge_view_render.py:750-770; mcp/src/agents_remember/application/knowledge_view_render.py:835-870; mcp/src/agents_remember/application/knowledge_view_render.py:873-908; mcp/src/agents_remember/application/knowledge_view_render.py:914-947 |
| The renderer's own ordering-and-paging step with the token-tail offset recovery, and the two views that carry the classification fields and the queue shapes. | `_render`; `render_review_matrix`; `render_curation_queue` | mcp/src/agents_remember/application/knowledge_view_render.py:822-833; mcp/src/agents_remember/application/knowledge_view_render.py:950-1006; mcp/src/agents_remember/application/knowledge_view_render.py:1015-1045; mcp/src/agents_remember/application/knowledge_view_render.py:966-966; mcp/src/agents_remember/application/knowledge_views.py:35-35; mcp/src/agents_remember/application/knowledge_views.py:274-274; mcp/src/agents_remember/application/knowledge_view_render.py:1031-1031 |
| The queue row that separates a machine work item from an attributed curator disposition, with the disposition vocabulary version it states. | `_queue_row`; `DISPOSITION_VOCABULARY_VERSION` | mcp/src/agents_remember/application/knowledge_view_render.py:825-858; mcp/src/agents_remember/application/knowledge_view_render.py:725-725; mcp/src/agents_remember/application/knowledge_view_render.py:908-908; mcp/src/agents_remember/serving/conversation/control/queue_projection.py:85-85; mcp/tests/test_conversation_control_queue.py:243-243; mcp/src/agents_remember/application/knowledge_view_render.py:772-772; mcp/src/agents_remember/application/knowledge_view_render.py:908-941 |
| The four admitted ordering inputs and the closed two-member class set the module imports instead of re-declaring, the registry holding one ordering rule per admitted input, and the declared stable tiebreak every position must name. | `OrderingInput`; `ORDERING_INPUTS`; `AUTHORED_CLASS`; `MECHANICAL_CLASS`; `MECHANICAL_RULES`; `ORDERING_PROVENANCE_RULE`; `ordering_position` | mcp/src/agents_remember/models/knowledge/classification.py:80-86; mcp/src/agents_remember/models/knowledge/classification.py:73-76; mcp/src/agents_remember/models/knowledge/classification.py:168-265; mcp/src/agents_remember/models/knowledge/view.py:162-162; mcp/src/agents_remember/models/knowledge/view.py:650-665; mcp/src/agents_remember/models/knowledge/view.py:70-70; mcp/src/agents_remember/models/knowledge/view.py:633-647 |
| The limitation record a withheld value becomes, the position shape, and the refusal of one subject at two positions. | `UnresolvedLimitation`; `OrderedPosition`; `require_distinct_row_subjects` | mcp/src/agents_remember/models/knowledge/view.py:417-429; mcp/src/agents_remember/models/knowledge/view.py:445-477; mcp/src/agents_remember/models/knowledge/view.py:552-576; mcp/src/agents_remember/application/knowledge_view_render.py:67-67; mcp/src/agents_remember/application/knowledge_view_render.py:352-352; mcp/src/agents_remember/application/knowledge_view_render.py:909-909; mcp/src/agents_remember/models/knowledge/view.py:712-736; mcp/src/agents_remember/models/knowledge/view.py:577-589; mcp/src/agents_remember/models/knowledge/view.py:605-637 |
| The reader port the module reads through and the store-side reader that answers it, including the per-kind row cache. | `KnowledgeViewReader`; `StoreViewReader`; `open_view_reader` | mcp/src/agents_remember/models/knowledge/view.py:863-881; mcp/src/agents_remember/memory/knowledge/view_source.py:154-197; mcp/src/agents_remember/memory/knowledge/view_source.py:383-407 |
| The seam that calls the renderers, screens the ordering input before any read, and accounts withheld rows as unresolved references. | `_admit`; `_render`; `_counts` | mcp/src/agents_remember/application/knowledge_views.py:107-140; mcp/src/agents_remember/application/knowledge_views.py:153-201; mcp/src/agents_remember/application/knowledge_views.py:204-224 |
| The admission cases: one rule per admitted input, an unadmitted input refused rather than defaulted, and every position naming the declared tiebreak. | "def test_the_registry_admits_one_rule_per_ordering_input("; "def test_an_unadmitted_ordering_input_is_refused_rather_than_defaulted("; "def test_every_admitted_position_names_the_declared_tiebreak_rule(" | mcp/tests/test_knowledge_views_and_projection.py:183-183; mcp/tests/test_knowledge_views_and_projection.py:206-206; mcp/tests/test_knowledge_views_and_projection.py:216-216 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A view renders over one reader port bound to one
repository namespace, every subject it emits is a store-local record identity or revision identity, and
no construct here reads a path prefix, a file extension or a repository location.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T02:24+02:00 — 260915-KS-L32 curator, post-sync citation pass (uncommitted change set on `ar/260915-ks-l32-ar`, code base `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`, memory base `4ffb8d8d3ff372847784fe8f7d2a13e57d9509a5`): re-measured this card after the master-line sync and the settled resolution pass, and it carries **no enforced finding**: the report's repairable set holds no row of this card, and the two stale-cell rows the previous pass cleared stay cleared against the merged tree (`_invariant_candidates` `465-531`, `_family_candidates` `580-621`, `render_source_context` `835-870`, `render_invariant` `873-908`, `render_family` `914-947`, `render_review_matrix` `950-1006`, `render_curation_queue` `1015-1045`, and `ORDERING_PROVENANCE_RULE` at `view.py:162`, `OrderedPosition` at `view.py:615-647`, `ordering_position` at `view.py:650-665`). The one change made here is bookkeeping: the `reviewedWorkingCandidate` row named the superseded `ar/260915-ks-l20` candidate at base `9f88a6de`, a base the merged candidate no longer stands on, and now names this leaf's candidate `ar/260915-ks-l32-ar` at base `7dcec036` — the same candidate every other row of this block was read against. The card's `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained unchanged (the closeout's memory leg requires it present), no claim was re-worded, no anchor, row or citation was added, removed or dropped, and no stamp was advanced or invented.
- 2026-09-20T02:12+02:00 — 260915-KS-L32 memory-side conflict resolution (uncommitted; this worktree, code base `7dcec036`, merged tree = L30's landed `7ca3ac48` plus this leaf's four modified paths): **resolved two reference-table hunks and the Update History block.** Every cell of both conflicted hunks cites `application/knowledge_view_render.py`, one of this leaf's four modified paths, so this leaf's ranges were kept; upstream's side was measured before this leaf's own additions and is stale by a different amount per construct (`_invariant_candidates`; `_family_candidates`; `render_source_context`; `render_invariant`; `render_family`; `render_review_matrix`; `ORDERING_PROVENANCE_RULE` and `Candidate`/`OrderedSet` were all cited at ranges that hold them only on this leaf's side). One cell was cited fresh: `knowledge_view_render.py:98-98` (a bare comment line holding nothing the row names, on both sides) → `96-98`, the comment block the three facet constants are read from. The rules row keeps this leaf's `REGISTERED_ROLE_RULE` anchor, its Finding and its `104-106` range, because that constant is this leaf's own addition. The admission-case row cites `mcp/tests/test_knowledge_views_and_projection.py`, modified by neither leaf, so upstream's `183-183; 206-206; 216-216` was kept after reading the three `def` lines in the code worktree. Update History is the union of both sides, newest first; no claim was re-worded, no anchor, row or citation dropped, and no verification stamp advanced.
- 2026-09-20T01:39:03+02:00 — 260915-KS-L32 curator (uncommitted change set on `ar/260915-ks-l32-ar`, code base `7dcec036`, memory base `66b2ae8a`): **cleared the two enforced `citation_anchor_absent_from_range` rows this card carried, by repointing each stale cell onto the declaration that actually holds the construct the row names.** No Finding text, Anchor cell, row or citation was dropped, and no cell that already held its anchor was touched. (a) The renderer row (`_render`; `render_review_matrix`; `render_curation_queue`) cited five `knowledge_view_render.py` spans that this module's own growth had left behind: they now read `822-833` (`_render`, declared at `822`), `950-1006` (`render_review_matrix`, declared at `950`) and `1015-1045` (`render_curation_queue`, declared at `1015`), with `966-966` and `1031-1031` carrying the two `_render` calls those two renderers make; the two `knowledge_views.py` cells are left as written because `35-35` and `274-274` do hold `render_curation_queue`, in the import block and in the registry. (b) The ordering row (`OrderingInput`; `ORDERING_INPUTS`; `AUTHORED_CLASS`; `MECHANICAL_CLASS`; `MECHANICAL_RULES`; `ORDERING_PROVENANCE_RULE`; `ordering_position`) had four `models/knowledge/view.py` cells left over from a layout this module no longer has: `149-149` now reads `162-162`, the line that declares `ORDERING_PROVENANCE_RULE = ("ordering.declared-tiebreak", 1)`; `480-495` now reads `650-665`, the declaration extent of `ordering_position`, which reads that rule at `658`; `152-152` now reads `70-70`, the name's own export in `__all__`; and `640-655` now reads `633-647`, the `_require_the_declared_tiebreak` validator the row's own words describe as the declared stable tiebreak every position must name. The three `models/knowledge/classification.py` cells were verified against their constructs and are unchanged: `80-86` holds `OrderingInput` and `ORDERING_INPUTS`, `73-76` holds `AUTHORED_CLASS` and `MECHANICAL_CLASS`, and `168-265` holds `MECHANICAL_RULES`. Every substituted range was read in the code worktree before it was written and none was inferred by arithmetic. No claim was re-worded to fit a stale pointer, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-20T01:23+02:00 — 260915-KS-L30 curator, final citation pass (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared the 8 enforced `citation_anchor_absent_from_range` rows this card carried by RANGE REPAIR.** Every flagged range was hand-read against this candidate and repointed to the declaration extent of the anchor it was written for: `DECISION_FACET_KIND` `:96-96` → `:99-99`, `NO_CONSEQUENCE_OUTCOME_PREFIX` `:97-97` → `:100-100` and `PRIORITY_OUTCOME_PREFIX` `:98-98` → `:101-101` (the three registered literals, each range still the one written for that constant); `CONSEQUENCE_RULE` `:102-102` → `:105-105` and `DETECTION_RULE` `:101-101` → `:104-104` (the two generated-content rules, each range still the one written for that rule); `_curation_candidates` `:603-626` → `:631-654` (now the whole selection function, `def` through `return tuple(candidates)`); `render_review_matrix` `:805-822` → `:831-887` (now the whole renderer, `def` through its closing `)`); and `def test_an_unadmitted_ordering_input_is_refused_rather_than_defaulted(` `mcp/tests/test_knowledge_views_and_projection.py:192-200` → `:206-206`, the declaration line its two sibling cases already cite. The pairing of each range to its anchor was fixed by the construct the range held at the revision its numbers were true at, so no citation changed which anchor it belongs to and none was dropped; the `facet.py:91-103` payload citation and every range not named above were left as they stand. Each named claim was re-read at the repointed construct and its wording retained: the two prefixes are still the canonical spellings read off the facet payload's `outcome`, the two rules are still the trigger-identity and payload-byte-equality classifications, `_curation_candidates` still returns the machine and curator row sets, and `render_review_matrix` is still the renderer the admission cases govern. No claim wording, anchor or other citation was added, removed or re-worded. **Stamp position:** unchanged — this pass advances no verification stamp and writes no commit hash; the source is uncommitted and closeout owns the stamp.
- 2026-09-20T00:46:52+02:00 — 260915-KS-L32 curator (uncommitted change set on `ar/260915-ks-l32-ar`, code base `7dcec036`, memory base `66b2ae8a`): **body update for this leaf's four closed behaviours, and the citations this file's own edits moved.** The front door now has a path seed: `_seed_revisions` resolves `request.source_path` to the revisions realized there and `_family_members` / `_member_locations` carry the family view's members and those members' realization loci, classified under the new `REGISTERED_ROLE_RULE`; and both the invariant and the family view now apply **one frontier** to realizations, so an exact revision read no longer returns a location belonging to another invariant or another family's member. The commentary, the Conventions rule list (two constants became three), the private-helper count (31 to 34) and the Invariants list (two new entries: the shared realization frontier, and the seed's `None`/empty-set distinction) state that. Citation repair in the same pass: the facet-kind row moved from `91-93; 97-97; 96-96` to `80-101; 99-101` (the three constants are now 99, 100 and 101) with its `DecisionPayload` cell repointed to `facet.py:91-103` and its `outcome`/`decider` cell to `facet.py:101-103`, and the rules row widened from `96-97; 102-102; 101-101` to `104-106` to carry `DETECTION_RULE` (104), `CONSEQUENCE_RULE` (105) and the new `REGISTERED_ROLE_RULE` (106). The selection row's anchors were repointed from the pre-leaf ranges to `465-531`, `580-621`, `709-738`, `750-770`, `835-870`, `873-908` and `914-947`, and the admission-case row from `169-182; 192-200; 202-215` to `169-183; 192-205; 206-216` so each range carries the definition it names at `183`, `205` (the test body immediately preceding `206`) and `216`. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 2 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `def test_every_admitted_position_names_the_declared_tiebreak_rule(`; `def test_the_registry_admits_one_rule_per_ordering_input(`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `Candidate`; `OrderedSet` repointed to mcp/src/agents_remember/application/knowledge_view_render.py:174-200; mcp/src/agents_remember/application/knowledge_view_render.py:203-209. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `_position`; `_consequence`; `_page` repointed to mcp/src/agents_remember/application/knowledge_view_render.py:356-359; mcp/src/agents_remember/application/knowledge_view_render.py:362-378; mcp/src/agents_remember/application/knowledge_view_render.py:381-387. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:55:32+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document** (one table row, two anchors). The admission-case row cited `169-176` for `def test_the_registry_admits_one_rule_per_ordering_input(`, defined at `182`, and `202-211` for `def test_every_admitted_position_names_the_declared_tiebreak_rule(`, defined at `215`. Both ranges were widened to the definition they name (`169-182`, `202-215`); the middle range and the claim are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "def test_every_view_renders_two_byte_identical_runs_at_one_snapshot(" repointed to mcp/tests/test_knowledge_projection_vault_safety.py:281-281. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): created this one-to-one card for the five-view renderer and its provenance classes. It records the four properties the module enforces together (an admitted and named ordering input, a withheld rather than emitted unclassifiable value, the declared tiebreak as the only lexical order, and byte-identical runs at one snapshot), the `order_candidates` path with the `UnadmittedOrderingInput` it raises, the two-branch closure behind `_classified` and the `UnresolvedLimitation` its `None` becomes, and the CR20-6 intake decision that carries an authored claim as a stored `decision` facet with its two canonical outcome prefixes. It also records the deliberate absences: no third provenance class, no default order, no actionable count, no clock or environment read, and no I/O beyond the reader port. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
