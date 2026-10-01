# mcp/tests/test_knowledge_review_one_sided_statements.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **production-composition half** of ICR-R06@v1, in six cases. They drive the real
`compose_review` over **two real datasets**, each built through the public store operations by
`read_scope_test_support.build_read_scope_fixture` and then extended with one authored invariant
apiece. Nothing here substitutes a payload, edits a stored row or deletes a record to manufacture a
case: the after snapshot simply holds an invariant the before snapshot does not, and the before
snapshot holds one the after snapshot does not. Those two snapshots are what an addition and a
removal **are**, and the reviewed subject is selected from each side in turn.

The renderer half of the same requirement is `dashboard/src/panels/review/KnowledgeStatements.test.tsx`,
which uses these same values. A change to either half's contract fails in one of the two.

## Code Commentary

### Logic

**The fixture is two independently built snapshots, and that is the preservation boundary made
mechanical.** The module-scoped `pair` fixture mints one random namespace, builds a
`build_read_scope_fixture` tree for the "before" half and another for the "after" half **under the
same namespace**, then authors four invariant revisions through `author_invariant`:
`ADDED_*` into *after* only, `REMOVED_*` into *before* only, and one shared identity proposed in
*before* and accepted in *after*. So the addition and the removal are a real difference between two
real snapshots, not an edit of one dataset, and no stored identity is altered to produce a case.
Module scope is documented in the fixture's own docstring: both datasets are read-only once built, no
case writes after the fixture is built, and a per-case rebuild would pay for two fixture trees to
measure the same bytes.

**`author_invariant` writes through the store's own operations and refuses quietly never.** It opens
the fixture's database with `open_knowledge_store`, calls `create_invariant` and then
`create_revision`, and raises an `AssertionError` carrying the store's own refusal when either
answers anything but `"created"`. The acceptance reference is **not** a free argument:
`SHARED_ACCEPTANCE_REF` is attached only when the authored origin state is `accepted`, because the
vocabulary refuses a *proposed* revision that claims an acceptance — a proposal claiming an event
that did not happen. That single rule is what makes the shared subject's `acceptance_ref` transition
real rather than fabricated.

**`review` is the one composition call, and it fails loudly on a refusal.** It hands `compose_review`
a hand-assembled `ReviewCandidateResolution` (the two databases, the two `git_root`s and the two
`git_tree_id`s the fixtures carry), a `ReviewSurfaceRequest` naming the master, the leaf and the
selector, and an empty `ReviewRecordInputs`; when the result carries no payload it raises with the
composition's own refusal rather than asserting on `None`. The one case that must render *no*
subject — `test_a_review_that_compared_no_subject_serves_no_operand_at_all` — calls `compose_review`
directly with `selector=None` instead, because that path is the point of the case.

**The six cases, and the property each one owns.**

- **An addition** (`:249-269`): the after side is `present` and carries `ADDED_STATEMENT` verbatim,
  the before side is `absent` with `text is None` and its own no-record detail, and the comparison's
  own `side_absence:before:selector_absent` travels beside it in the payload's limitations. The
  reviewed subject is selected by its own recorded `InvariantIdentitySeed`.
- **A removal** (`:272-285`): the mirror image, with `side_absence:after:selector_absent`.
- **A one-sided field row** (`:288-317`): the shared revision identity is proposed in *before* and
  accepted in *after*, so the comparison reports the transition and each side's own value; the roster
  is asserted **by exact key set** (`acceptance_ref`, `lifecycle`, `payload_digest`, `provenance`),
  `acceptance_ref` keeps `before_value is None` beside `after_value == SHARED_ACCEPTANCE_REF`, and
  `lifecycle` is `("proposed", "accepted")`. Dropping the row, or printing the side that did record a
  value as blank, is what a one-sided statement must not become.
- **A structured value** (`:320-350`): the `provenance` row the comparison reports as *changed*
  carries a value on **both** sides, the two differ, and each is parsed back out of its marker and
  checked against the fixture's own stored authorship envelope (`actor_ref`, `operation_id`,
  `authorization_ref`) — so the projection invents nothing. The case also pins the projection's
  canonicality: `structured_value_text({"b": 1, "a": 2}) == structured_value_text({"a": 2, "b": 1})`.
- **A one-sided record keeps an empty roster** (`:353-369`): an addition reports
  `field_changes == ()` and `before_conditions == ()` while `after_conditions == CONDITIONS`, because
  the comparison reports such a record through its coverage and nine field rows would state nine
  differences where there is one absence.
- **No subject compared** (`:370-408`): `selection_state == "task_context"`, `comparison is None`,
  both sides `unresolved` with `text is None` and **the same** detail ("no knowledge operand was
  compared"), and an empty roster — the case a one-sided rendering must not swallow.

**The fixture helpers are typed and named.** `AuthoredInvariant` is a frozen dataclass carrying the
identities, the words and the origin state; `OneSidedPair` is a frozen dataclass carrying the
namespace, the two `ReadScopeFixture`s and the six identities the cases select subjects by. Every id
is drawn once (`uuid4()`), so a case asserts against the exact identity the review was asked for
rather than against a shape that could be anything.

### Conventions

`pytestmark = pytest.mark.evidence_unit` is the module's whole lane declaration; its membership is the
`unit-regression` row at `mcp/tests/test-evidence-lanes.toml:105`, and its consumption of
`read_scope_test_support` is the consumer row at `mcp/tests/evidence-lifecycle.toml:1436` on that
artifact's `consumer_scope = "exact"` list. The import block is alphabetical within its groups, and
the case functions are full sentences naming the rendering obligation they measure. Constants are
module-level and upper-case, and each case's docstring states the property rather than the mechanics.

### Invariants And Boundaries

- **Two real snapshots, no manufactured edit.** The difference between the halves is authored
  content, not a mutation of one dataset; no stored identity is altered and no record is deleted to
  produce a removal example.
- **The composition is real, and it is the adapter's own entry point.** `compose_review` is called
  with the shipped request type; no payload is substituted and no private helper is reached into.
- **The values the dashboard renders are the values asserted here.** The statements, the
  absent/unresolved details and the `acceptance_ref`/`provenance` rows are the binding between this
  module and the renderer suite.
- **A `None` on a field row is an absence and nothing else.** The structured-value case exists to
  make that falsifiable from both directions: `before_value is not None` and the two projections
  differ.
- **Read-only after the fixture is built.** No case writes to either dataset, and the fixture is
  module-scoped precisely because that holds.
- **Boundary.** This is measurement, not a second implementation: the module imports
  `structured_value_text` to check the projection's markers and canonicality, and it re-derives no
  composition rule of its own.

### Todos

None recorded. One measured limit is deliberately out of this module's scope and is recorded by the
leaf for R07: when the reviewed subject exists only on one side **and that side holds several retained
revisions**, `_identity_item` still returns `candidates[0]`, so which revision's statement is shown is
decided by page order. These cases avoid it by authoring subjects with a single revision and no
claims.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and case
bodies, the fixture module it builds on, the store operations it authors through, the composition it
drives, the owner of the projection it asserts against, and the catalogue and lane rows that register
it.

- **The module's own scope statement: six cases over the real adapter and two real datasets, and the load-bearing properties each one owns.** [1]
- The module's whole lane declaration. [2]
- The authored identities and words every case asserts against, drawn once in the builder. [3]
- **The two frozen fixture values: one invariant to author (with the origin state that alone decides its acceptance reference) and the pair of snapshots plus the identities cases select by.** [4]
- **The authoring helper: the store's own `create_invariant`/`create_revision`, the refusal carried into an `AssertionError`, and the rule that only an accepted origin state carries the acceptance reference.** [5]
- **The fixture: two independently built snapshots under one namespace, and the four authored revisions that make an addition, a removal and a real transition.** [6]
- The one composition call, with the hand-assembled resolution and the loud failure on a refusal. [7]
- **The addition and the removal: the complete present-side statement, the named absent side with `text is None`, and the comparison's own side-absence code.** [8]
- **The field row: the roster asserted by exact key set, the one-sided value kept, and the lifecycle transition beside it.** [9]
- **The structured value: both sides present and different, each projection round-tripped back to the stored envelope, and the projection's canonicality pinned.** [10]
- The one-sided record reported by coverage with an empty roster, against the conditions the after side really recorded. [11]
- **The task-context case: no comparison, both sides unresolved with the same reason and no text, and no roster.** [12]
- **The projection owner whose markers and canonicality this module asserts.** [13]
- The adapter entry point the cases drive, and the one-sided contract its pane values carry. [14]
- **The fixture this module builds on, and the public store operations it authors through.** [15]
- **The lane row that selects this module, and the artifact consumer row that registers it against the fixture it consumes.** [16]
- The `consumer_scope = "exact"` artifact whose list this module joined. [17]
- **The renderer half that uses these same values, which is what makes a change to either half fail in one of the two.** [18]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture boundaries.

Fixture repositories and protocol doubles do not establish a live external integration.
