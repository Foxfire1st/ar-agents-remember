# mcp/src/agents_remember/application/knowledge_view_render.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Candidate selection and ordering for the five knowledge views. Final row projections live in `knowledge_view_rows.py`; both halves share this module's candidates, ordering and classification.

## Code Commentary

### Logic

Only declared ordering inputs are admitted. Candidates lacking an authored determination or registered mechanical rule are withheld with an unresolved limitation. Recorded identity supplies the stable tiebreak, never a guessed path, symbol or route ranking.

`authored_decision` reads the text decision's own `decider`, `reason` and canonical `outcome`. A silent decider may use the record's author reference; a non-canonical decimal outcome never becomes a priority. The retired typed `DecisionPayload` model is not a production dependency.

A single realization frontier supplies path-seeded source-context, invariant and family selections. No seed selects unrestricted content; a held path realized nowhere selects nothing rather than widening to all. Families and member locations follow recorded membership and retain the recorded role, path and locator.

### Invariants And Boundaries

Emitted candidates are classified authored or mechanical, never default-classed. The application seam admits the offset once and passes it to the row renderer; no second token parse or position-zero fallback exists. Retaining text decisions restores no canonical facet model or writer.

### Todos

None recorded.

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
back into a typed `ViewRefusal`. `order_candidates` is exported in `__all__`

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
the ordering and the row content are all functions of recorded values and registered constants.

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

**The small helpers each name one fact, and the module is otherwise pure.** `_rules_used` returns the
rule ids one ordering touched with the tiebreak always included; `_position` is "One ordered position
carrying the class of the *input*, not of the row's content"; `_consequence` returns a
`NoConsequenceStatement` built from an authored claim's own recorded text or from a mechanical rule,
never a mixture; `_page` returns one page and the offset the next page starts at. The two internal
working types are frozen dataclasses rather than models — `Candidate` is "One row a view may emit,
before ordering and before classification" and `OrderedSet` is "The outcome of one ordering pass: the
ordered candidates and what could not be classified" — while every row that leaves the module is a
shipped model (`SourceContextRow`, `InvariantRow`, `FamilyRow`, `ReviewMatrixRow`, `CurationQueueRow`)
and the port it reads through is the shipped `KnowledgeViewReader`.  Seven of those private functions are the one seed frontier the
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

`UnadmittedOrderingInput` is deliberately a `ValueError` and not a refusal model, because the caller has a
programming defect rather than a data condition.

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
- **The module holds no I/O and no durable state.** Its imports are `collections.abc`, `dataclasses`,
  `typing.cast` and two model modules; it opens no connection, reads no path, holds no module-level
  mutable value, and therefore cannot disagree with itself between two calls at one snapshot. The seed
  cache it *does* keep is attached to the reader object under `_SEED_MEMO_ATTRIBUTE` rather than to this
  module, so it is bounded by the reader the seam already opened and closed and a reader that forbids
  attributes falls back to computing the seed rather than failing the read.
- **A row is emitted only after classification.** Every renderer asserts the class of each paged
  candidate before building its row, so a row that reaches a payload always carries exactly one of the
  two provenance classes.
- **The curation queue computes no actionable count and fills no per-row limitations.** No function here
  writes `CurationQueueRow.limitations`; unresolved rows are reported through the payload's
  `limitations` instead, and `design/retrieval-review-design.md:348` is cited in the renderer's docstring
  as the rule that keeps the review section report-only. That design file is not present in this code
  worktree, so the claim is anchored to the renderer's own docstring rather than to the design document.
- **The module adds no verification authority.** It reads recorded determinations as recorded, refuses to
  parse a non-canonical outcome into a priority, and never converts its own read into a statement about
  what the knowledge means.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Everything this card asserts is checkable inside the shipped candidate: the module's own docstring and
constants, the two model modules it imports its vocabulary and provenance classes from, the reader port
it consumes, the seam that calls it, and the cases that protect its properties — the determinism
differential in one test file and the ordering-and-admission cases in the other. The design document the
renderer's docstring cites by path lives outside this code worktree, so it is quoted as the module's own
statement rather than cited as a file.

- The docstring that states the four properties together and the CR20-6 intake decision behind the authored side. [1]

- The text-decision reader consumes recorded fields and canonical outcome prefixes; the canonical facet payload type is retired. [3]

- The two generated-content rules the module classifies under: a recorded trigger identity and a payload byte-equality consequence. [4]
- The three generated-content rules the module classifies under: a recorded trigger identity, a payload byte-equality consequence, and the registered rule a membership-derived row names. [5]
- One authored determination read from a stored facet — the canonical-spelling rule that decides whether it is a priority at all, and the reader that turns one facet row into it with the envelope actor used only when the payload is silent. [6]
- The pre-classification working type and the ordering pass's outcome, both frozen dataclasses rather than models. [7]
- The declared key each admitted input produces (including the sentinel that orders an unprioritised row after every prioritised one and the rule that the priority is read from the candidate's own subject), and the exception that replaces a default order with its raise site and the two-member class closure the caller turns into a recorded limitation. [8]
- The total sort key ending in record identity and the registered rule ids an ordering touched. [9]
- The position that carries the class of the input, and the no-consequence statement built from either branch with its paging helper. [10]
- The attachment read that fetches a subject's own decisions, and the rule that only one declared position may order. [11]
- The per-view selection functions and the five renderers they feed, each returning rows with the limitations, the rule ids and the selection's own size. [12]
- The two projections that carry a row's recorded location into the response, the candidate builder each copies from rather than re-deriving, and the single decoder both share with the source-context view. [13]
- The renderer's own ordering-and-paging step with the token-tail offset recovery, and the two views that carry the classification fields and the queue shapes. [14]
- The queue row that separates a machine work item from an attributed curator disposition, with the disposition vocabulary version it states. [15]
- The four admitted ordering inputs and the closed two-member class set the module imports instead of re-declaring, the registry holding one ordering rule per admitted input, and the declared stable tiebreak every position must name. [16]
- The limitation record a withheld value becomes, the position shape, and the refusal of one subject at two positions. [17]
- The reader port the module reads through and the store-side reader that answers it, including the per-kind row cache. [18]
- The seam that calls the renderers, screens the ordering input before any read, and accounts withheld rows as unresolved references. [19]

### Cross-Repo References

No cross-repository behavior is implemented in this file. A view renders over one reader port bound to one
repository namespace, every subject it emits is a store-local record identity or revision identity, and
no construct here reads a path prefix, a file extension or a repository location.

No meaningful cross-repo references found.

### Repo-Internal References

- The registered facet kind the authored claim is carried in, with the two canonical outcome prefixes and the three payload fields `authored_decision` reads. [20]
