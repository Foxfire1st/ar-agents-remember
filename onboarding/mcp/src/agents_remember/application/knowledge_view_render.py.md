# mcp/src/agents_remember/application/knowledge_view_render.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_view_render.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T15:30+02:00 |
| lastVerifiedCommitHash | `b7bfebb550f036a7e51de1f390be1123cd2d2172` |
| lastVerifiedCommitDate | 2026-09-20T05:54:26+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l41-ar`, uncommitted; base `756c47b37fa16324a836a44336655413d10fffaa` |
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

**Both views that can answer "what governs this file?" read their selections through one shared seed
frontier, and the membership that selects a family is read from where membership is stored.** Four
private helpers state the seed once per reader and answer three questions from it. `_seed_revisions`
resolves `request.source_path` to the revisions realized there and keeps the two honest answers apart:
`None` means "no seed was named" and an empty set means "a path was named and it selects nothing", so an
unrecorded path returns no rows instead of falling back to everything. `_seed_memo` attaches that answer
to the **reader object** under `_SEED_MEMO_ATTRIBUTE`, so it lives exactly as long as the reader the seam
already opened and closed; `_seeded_realizations` is the memoised front door, and `_seed_selects` is the
single predicate both views ask -- deliberately written so that `None` selects everything and a set
selects only its members. `_seeded_family_revisions` is the one hop that is not a lookup: **a family is
not a file**, so the seed selects a family through the `family_member` rows that name a revision the path
realizes, which is why `_family_candidates` filters on a frontier of *family* revisions while
`_family_members` filters on the revision frontier itself, and `_member_locations` then emits only the
locations of the members this read selected. `_selected_invariant_revisions` returns the same frontier as
a set rather than a per-row boolean so the `source_context` view can apply it to both the registered
realizations and the authored decisions attached to those revisions, which is what makes the path seed
reach that view at all. Read one function at a time the seed looks like three different filters; read
together they are one frontier computed once, and the distinction between "no seed" and "a seed that
selects nothing" is the only thing that keeps an absent path honest.

**Membership is read through its own port method, because it is its own recorded entity.**
`_family_members` calls `reader.family_member_rows()` -- a method the `KnowledgeViewReader` protocol
declares and `StoreViewReader` answers from the dedicated `family_member` table -- rather than
`reader.rows("family_member")`. The distinction is the whole finding this behaviour exists to close: the
generic envelope reader answers for `knowledge_record`/`record_revision` kinds, and a membership row is
not duplicated into that envelope, so asking for the kind by name returned **no members on a dataset that
holds them** -- and the family view then reported a joint guarantee, no members, no locations and
`completeWithinDeclaredScope: true`. The two row shapes that membership produces also carry the family
view's own vocabulary rather than the source-context view's: a member row and a member's realization row
both use `fact_kind="member"` (`FamilyRow` declares that closed set, and `"family_member"` /
`"registered_realization"` are not members of it), so the traversal from a path to the governing family,
to its other member and to that member's implementation location is measurable through
`subject.revision_id` plus `fact_kind` and not through an item id.

**The public context is completed as one pair rather than half-supplied, and the pair is resolved from
the repository the caller actually named.** `_source_resolution(request, workspace_root)` returns
`(repository_root, code_tree_id)` and it never returns one without the other. A caller who named both
gets both back untouched; a caller who named a root gets that root's own current tree from
`_current_code_tree`; a caller who named **neither** gets the mount's workspace default -- but only when
a tree can actually be resolved from it, because naming a root without a tree is exactly the
`KnowledgeReadContext` refusal the mount's own default used to hand a minimal caller. `_current_code_tree`
shells `git -C <root> rev-parse HEAD^{tree}` under `_GIT_TIMEOUT_SECONDS` and validates the answer against
`_TREE_ID_PATTERN`, returning `None` -- never a guess -- when the root is not a repository, Git is absent,
Git does not answer in time, or the answer is not a tree id; the context is then built with neither half,
which the shipped resolver reports as "no source resolution was requested" rather than as a resolution
that silently failed. So anchor resolution stays `not_requested` for a caller who names no repository,
unless the mount's own workspace is itself the Git repository a tree can be read from.

**The remaining three renderers, and the shared body every one of the five ends in.**
`render_source_context` also collects the authored decisions of one invariant revision when the request
names one, distinguishing `authored_responsibility` from `diagnostic_evidence` by `is_no_consequence`.
`render_review_matrix` defaults to the six requirement/effect/preservation/
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
leaving the other module-level functions private: 41 module-level functions and five classes in total,
with no class of its own beyond those five (`AuthoredDecision`, `Candidate`, `OrderedSet`,
`UnadmittedOrderingInput` and `Page`). Seven of those private functions are the one seed frontier the
Path Seed section describes: `_seed_revisions` resolves the request's optional source path to the
revisions realized there (`None` meaning "no restriction", an empty set meaning "realized nowhere", which
is an answer and not a fallback to everything), `_seed_memo` / `_seeded_realizations` / `_seed_selects`
memoise that answer on the reader and turn it into the one predicate every caller uses,
`_seeded_family_revisions` and `_selected_invariant_revisions` are the two derived frontiers the family
and source-context views filter on, and `_family_members` and `_member_locations` apply the revision
frontier to the family view's membership rows and to the locations those members name. The seed's memo
attribute and its two cache keys are module constants (`_SEED_MEMO_ATTRIBUTE`, `_SEED_KEY`,
`_SEED_FAMILY_KEY`) rather than literals, because two functions must agree on them exactly.

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
as a trigger-derived row names `DETECTION_RULE`. Those two row shapes state their kind in the family
view's own vocabulary and nowhere else: `fact_kind="member"` is written at both construction sites, and
neither `"family_member"` (the envelope kind the membership is *not* read as) nor
`"registered_realization"` (the source-context view's kind for the same recorded rows) is a member of
`FamilyRow`'s closed set, so stating the wrong one is a validation failure rather than a silently
mis-typed row. The three seed-cache names are constants for the same reason the rule identities are: two
functions must agree on the exact key, and a literal in each would be a second declaration of one fact.
The curation queue's `DISPOSITION_VOCABULARY_VERSION` names the vocabulary it states on every machine item.
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
- **Every view that can be seeded applies the same frontier, and the two "nothing" answers stay
  distinct.** `_seed_selects` is the only predicate: `None` selects every row and a set selects only its
  members, so `source_context`, `invariant` and `family` cannot disagree about what a path selected. The
  seed is computed once per reader through `_seed_memo` and never recomputed per view, which is what
  makes "the same read asked three questions" one answer rather than three chances to differ.
- **A family is selected through its recorded membership, not by matching a path against the family.**
  A family revision has no path, so `_seeded_family_revisions` selects the families whose `family_member`
  rows name a revision the seed realizes; `_family_candidates` then filters on that set of *family*
  revisions while `_family_members` filters on the revision set itself. A family none of whose members is
  realized at the named file is another subject's answer to "what governs this file" and is absent from
  the read rather than softened into a weaker match.
- **Membership is read from the table membership is stored in.** `_family_members` reads
  `reader.family_member_rows()` — the port method `StoreViewReader` answers from the dedicated
  `family_member` table — and never `reader.rows("family_member")`. The envelope reader answers only for
  `knowledge_record`/`record_revision` kinds, and a membership row is not duplicated into that envelope,
  so the named-kind read returned no members on a dataset that holds them and the family view reported a
  guarantee, no members, no locations and a complete answer. The port method's absence is a type error
  rather than a silently empty read, which is why the protocol declares it.
- **A member row and a member's location speak the family view's vocabulary.** Both carry
  `fact_kind="member"`, the closed set `FamilyRow` declares; the traversal a caller measures is therefore
  `subject.revision_id` plus `fact_kind`, not an item id, and a location reported as one of a family's
  members is a member fact about that family rather than the source-context view's
  `registered_realization`.
- **The source-resolution pair is named as a pair or not at all.** `_source_resolution` never returns a
  root without a tree or a tree without a root: a caller-named root is completed with that root's own
  current tree, the mount's workspace default is named only when a tree can be resolved from it, and a
  root Git cannot answer for is named as neither half. `_current_code_tree` returns `None` — never a
  guess — for a root that is not a repository, an absent Git, a timeout, or an answer that is not a tree
  id, so a minimal read reaches the context as "no source resolution was requested" instead of as a raw
  `KnowledgeReadContext` validation error.
- **The module holds no I/O and no durable state.** Its imports are `collections.abc`, `dataclasses`,
  `typing.cast` and two model modules; it opens no connection, reads no path, holds no module-level
  mutable value, and therefore cannot disagree with itself between two calls at one snapshot. The seed
  cache it *does* keep is attached to the reader object under `_SEED_MEMO_ATTRIBUTE` rather than to this
  module, so it is bounded by the reader the seam already opened and closed and a reader that forbids
  attributes falls back to computing the seed rather than failing the read.
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
| The three generated-content rules the module classifies under: a recorded trigger identity, a payload byte-equality consequence, and the registered rule a membership-derived row names. | `DETECTION_RULE`; `CONSEQUENCE_RULE`; `REGISTERED_ROLE_RULE` | mcp/src/agents_remember/application/knowledge_view_render.py:105-107; mcp/src/agents_remember/application/knowledge_view_render.py:105-105; mcp/src/agents_remember/application/knowledge_view_render.py:106-106; mcp/src/agents_remember/application/knowledge_view_render.py:107-107 |
| One authored determination read from a stored facet — the canonical-spelling rule that decides whether it is a priority at all, and the reader that turns one facet row into it with the envelope actor used only when the payload is silent. | `AuthoredDecision`; `priority_position`; `is_no_consequence`; `no_consequence_detail`; `authored_decision` | mcp/src/agents_remember/application/knowledge_view_render.py:117-152; mcp/src/agents_remember/application/knowledge_view_render.py:156-166; mcp/src/agents_remember/application/knowledge_view_render.py:154-154; mcp/src/agents_remember/application/knowledge_view_render.py:155-178 |
| The pre-classification working type and the ordering pass's outcome, both frozen dataclasses rather than models. | `Candidate`; `OrderedSet` | mcp/src/agents_remember/application/knowledge_view_render.py:183-208; mcp/src/agents_remember/application/knowledge_view_render.py:212-217 |
| The declared key each admitted input produces (including the sentinel that orders an unprioritised row after every prioritised one and the rule that the priority is read from the candidate's own subject), and the exception that replaces a default order with its raise site and the two-member class closure the caller turns into a recorded limitation. | `_ordering_keys`; `_declared_priority`; `return (1,), mechanical_provenance("ordering.declared-tiebreak", 1)`; `UnadmittedOrderingInput`; `order_candidates`; `_classified` | mcp/src/agents_remember/application/knowledge_view_render.py:231-264; mcp/src/agents_remember/application/knowledge_view_render.py:220-228; mcp/src/agents_remember/application/knowledge_view_render.py:274-275; mcp/src/agents_remember/application/knowledge_view_render.py:278-313; mcp/src/agents_remember/application/knowledge_view_render.py:342-361 |
| The total sort key ending in record identity and the registered rule ids an ordering touched. | `_sort_key`; `_rules_used` | mcp/src/agents_remember/application/knowledge_view_render.py:316-325; mcp/src/agents_remember/application/knowledge_view_render.py:328-339 |
| The position that carries the class of the input, and the no-consequence statement built from either branch with its paging helper. | `_position`; `_consequence`; `_page` | mcp/src/agents_remember/application/knowledge_view_render.py:364-367; mcp/src/agents_remember/application/knowledge_view_render.py:370-386; mcp/src/agents_remember/application/knowledge_view_render.py:389-395 |
| The attachment read that fetches a subject's own decisions, and the rule that only one declared position may order. | `_decisions_for`; `_priority_of` | mcp/src/agents_remember/application/knowledge_view_render.py:420-440; mcp/src/agents_remember/application/knowledge_view_render.py:443-450 |
| The per-view selection functions and the five renderers they feed, each returning rows with the limitations, the rule ids and the selection's own size. | `_invariant_candidates`; `_family_candidates`; `_review_candidates`; `_curation_candidates`; `render_source_context`; `render_invariant`; `render_family` | mcp/src/agents_remember/application/knowledge_view_render.py:547-613; mcp/src/agents_remember/application/knowledge_view_render.py:678-725; mcp/src/agents_remember/application/knowledge_view_render.py:823-838; mcp/src/agents_remember/application/knowledge_view_render.py:864-887; mcp/src/agents_remember/application/knowledge_view_render.py:949-984; mcp/src/agents_remember/application/knowledge_view_render.py:987-1022; mcp/src/agents_remember/application/knowledge_view_render.py:1028-1061 |
| The renderer's own ordering-and-paging step with the token-tail offset recovery, and the two views that carry the classification fields and the queue shapes. | `_render`; `render_review_matrix`; `render_curation_queue` | mcp/src/agents_remember/application/knowledge_view_render.py:936-946; mcp/src/agents_remember/application/knowledge_view_render.py:1064-1120; mcp/src/agents_remember/application/knowledge_view_render.py:1129-1158; mcp/src/agents_remember/application/knowledge_view_render.py:1083-1083; mcp/src/agents_remember/application/knowledge_views.py:38-38; mcp/src/agents_remember/application/knowledge_views.py:273-273; mcp/src/agents_remember/application/knowledge_view_render.py:1150-1150 |
| The queue row that separates a machine work item from an attributed curator disposition, with the disposition vocabulary version it states. | `_queue_row`; `DISPOSITION_VOCABULARY_VERSION` | mcp/src/agents_remember/application/knowledge_view_render.py:1161-1194; mcp/src/agents_remember/application/knowledge_view_render.py:1025-1025; mcp/src/agents_remember/application/knowledge_view_render.py:1172-1172; mcp/src/agents_remember/serving/conversation/control/queue_projection.py:85-85; mcp/tests/test_conversation_control_queue.py:243-243; mcp/src/agents_remember/application/knowledge_view_render.py:907-907 |
| The four admitted ordering inputs and the closed two-member class set the module imports instead of re-declaring, the registry holding one ordering rule per admitted input, and the declared stable tiebreak every position must name. | `OrderingInput`; `ORDERING_INPUTS`; `AUTHORED_CLASS`; `MECHANICAL_CLASS`; `MECHANICAL_RULES`; `ORDERING_PROVENANCE_RULE`; `ordering_position` | mcp/src/agents_remember/models/knowledge/classification.py:80-86; mcp/src/agents_remember/models/knowledge/classification.py:73-76; mcp/src/agents_remember/models/knowledge/classification.py:168-265; mcp/src/agents_remember/models/knowledge/view.py:162-162; mcp/src/agents_remember/models/knowledge/view.py:650-665; mcp/src/agents_remember/models/knowledge/view.py:70-70; mcp/src/agents_remember/models/knowledge/view.py:633-647 |
| The limitation record a withheld value becomes, the position shape, and the refusal of one subject at two positions. | `UnresolvedLimitation`; `OrderedPosition`; `require_distinct_row_subjects` | mcp/src/agents_remember/models/knowledge/view.py:587-599; mcp/src/agents_remember/models/knowledge/view.py:615-647; mcp/src/agents_remember/models/knowledge/view.py:722-746; mcp/src/agents_remember/application/knowledge_view_render.py:67-67; mcp/src/agents_remember/application/knowledge_view_render.py:363-363; mcp/src/agents_remember/application/knowledge_view_render.py:1019-1019; mcp/src/agents_remember/models/knowledge/view.py:785-809; mcp/src/agents_remember/models/knowledge/view.py:597-602; mcp/src/agents_remember/models/knowledge/view.py:607-612 |
| The reader port the module reads through and the store-side reader that answers it, including the per-kind row cache. | `KnowledgeViewReader`; `StoreViewReader`; `open_view_reader` | mcp/src/agents_remember/models/knowledge/view.py:1041-1086; mcp/src/agents_remember/memory/knowledge/view_source.py:154-197; mcp/src/agents_remember/memory/knowledge/view_source.py:405-428; mcp/src/agents_remember/memory/knowledge/view_source.py:431-455 |
| The seam that calls the renderers, screens the ordering input before any read, and accounts withheld rows as unresolved references. | `_admit`; `_render`; `_counts` | mcp/src/agents_remember/application/knowledge_views.py:115-148; mcp/src/agents_remember/application/knowledge_views.py:161-210; mcp/src/agents_remember/application/knowledge_views.py:227-254 |
| The admission cases: one rule per admitted input, an unadmitted input refused rather than defaulted, and every position naming the declared tiebreak. | "def test_the_registry_admits_one_rule_per_ordering_input("; "def test_an_unadmitted_ordering_input_is_refused_rather_than_defaulted("; "def test_every_admitted_position_names_the_declared_tiebreak_rule(" | mcp/tests/test_knowledge_views_and_projection.py:222-228; mcp/tests/test_knowledge_views_and_projection.py:245-252; mcp/tests/test_knowledge_views_and_projection.py:255-263 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A view renders over one reader port bound to one
repository namespace, every subject it emits is a store-local record identity or revision identity, and
no construct here reads a path prefix, a file extension or a repository location.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T05:44+02:00 — 260915-KS-L41 curator (uncommitted change set on `ar/260915-ks-l41-ar`, code base `756c47b3` at this leaf's cut and `f79f4db745ad00b908d6ce4871d0b4ab2320207c` after the L39 sync, memory base `da33325c` at the cut and `37d0787571bfbf92890049ee0614fa159012be39` after it): **body update for the one seed frontier this leaf completes, and the two row classes the report named on this card.** (a) The path seed is now computed once per reader and applied by every view that can be seeded. `_seed_memo` (`application/knowledge_view_render.py:472-486`) attaches the answer to the reader object under `_SEED_MEMO_ATTRIBUTE`; `_seeded_realizations` (`:489-495`) is the memoised front door; `_seed_selects` (`:498-501`) is the one predicate, written so that `None` selects everything and a set selects only its members; `_seeded_family_revisions` (`:504-525`) is the hop that is not a lookup, because **a family is not a file** and is selected through the `family_member` rows naming a revision the path realizes; `_selected_invariant_revisions` (`:528-544`) returns the same frontier as a set so `source_context` can apply it to both its registered realizations and the authored decisions attached to those revisions; and `_source_context_candidates` (`:616-654`) now calls `_seed_selects` at all, which is what stops the path seed from being ignored by that view. (b) `_family_members` (`:728-766`) reads `reader.family_member_rows()` — the port method answered from the dedicated `family_member` table — instead of the generic envelope read, and both membership-derived row shapes now carry `fact_kind="member"`, the closed set `FamilyRow` declares, rather than `"family_member"` / `"registered_realization"`. The Logic section gained three paragraphs (the shared frontier, the membership read and why it cannot be a kind lookup, and the source-resolution pair the read completes), the private-helper count was corrected from 34 functions and four classes to **41 functions and five classes**, the Conventions section now names the three seed-cache constants and the family view's own `fact_kind` vocabulary, and the Invariants list gained five entries. Twelve `citation_anchor_absent_from_range` cells and one reopened claim were re-read against the candidate rather than shifted: the three admission-case cells now cite the test declarations they name (`222-228`, `245-252`, `255-263`), and the per-view selection, renderer, queue-row, decisions and reader-port cells were repointed to the constructs each row actually names. No claim was re-worded to fit a stale pointer and no anchor or range was dropped. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained as recorded — the candidate is uncommitted and the governed closeout owns the real stamp — the superseded `ar/260915-ks-l32-ar` candidate row is replaced by the `reviewedWorkingCandidate` row above, and no stamp was advanced or invented.
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
