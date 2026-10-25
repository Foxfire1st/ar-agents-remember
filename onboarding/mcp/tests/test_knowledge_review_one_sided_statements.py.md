# mcp/tests/test_knowledge_review_one_sided_statements.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The one-sided statement contract drives real compose_review over two independently built read-side snapshots. Their entries are assembled by knowledge_rows_test_support, the test-only builder; no production canonical database writer is involved. The after half holds an addition and the before half a removal, each selected by its own identity. [15]

The renderer cases in `dashboard/src/panels/review/KnowledgeStatements.test.tsx` use their own
synthetic statement values and before/after states. They neither share these Python constants nor
assert the backend acceptance_ref field-row contract. The Python and renderer assertions are distinct.

## Code Commentary

### Logic

**The fixture is two independently built snapshots, and that is the preservation boundary made
mechanical.** The module-scoped `pair` fixture uses `INDEX_REPOSITORY_ID` as its namespace and builds two
`build_read_scope_fixture` trees — the "before" half and the "after" half **under the
same namespace** — then adds one whole extra invariant apiece via `ExtraInvariantSeed`:
the added seed into *after* only, the removed seed into *before* only, and one shared identity proposed in
*before* and accepted in *after*. So the addition and the removal are a real difference between two
real snapshots, not an edit of one tree, and no stored identity is altered to produce a case.
Module scope is documented in the fixture's own docstring: both trees are read-only once built, no
case writes after the fixture is built, and a per-case rebuild would pay for two fixture trees to
measure the same bytes.

The extra-invariant seeds are written through the test-only rows builder; text records carry no
authored acceptance event, so the accepting side's acceptance reference is derived by the projection
as `text-knowledge:<record path>`. Only accepted origin data receives that reference. This constructs read-side data and proves no
production write refusal. [15]

**`review` is the one composition call, and it fails loudly on a refusal.** It hands `compose_review`
a hand-assembled `ReviewCandidateResolution` (the two databases, the two `git_root`s and the two
`git_tree_id`s the fixtures carry), a `ReviewSurfaceRequest` naming the master, the leaf and the
selector; when the result carries no payload it raises with the
composition's own refusal rather than asserting on `None`. The one case that must render *no*
subject — `test_a_review_that_compared_no_subject_serves_no_operand_at_all` — calls `compose_review`
directly with `selector=None` instead, because that path is the point of the case.

**The six cases, and the property each one owns.**

- **An addition**: the after side is `present` and carries `ADDED_STATEMENT` verbatim,
  the before side is `absent` with `text is None` and its own no-record detail, and the comparison's
  own `side_absence:before:selector_absent` travels beside it in the payload's limitations. The
  reviewed subject is selected by its own recorded `InvariantIdentitySeed`.
- **A removal**: the mirror image, with `side_absence:after:selector_absent`.
- **A one-sided field row**: the shared revision identity is proposed in *before* and
  accepted in *after*, so the comparison reports the transition and each side's own value; the roster
  is asserted **by exact key set** (`acceptance_ref`, `lifecycle`, `payload_digest`),
  `acceptance_ref` keeps `before_value is None` beside a non-`None` after value starting with `text-knowledge:`, and
  `lifecycle` is `("proposed", "accepted")`. Dropping the row, or printing the side that did record a
  value as blank, is what a one-sided statement must not become.
- **A structured value**: the retained function pins key-order canonicality:
  `structured_value_text({"b": 1, "a": 2}) == structured_value_text({"a": 2, "b": 1})`.
  Its former fixture-driven envelope round trip is explicitly retired: the shared text's provenance
  is equal on both sides, so the comparison reports no changed `provenance` row.
- **A one-sided record keeps an empty roster**: an addition reports
  `field_changes == ()` and `before_conditions == ()` while `after_conditions == CONDITIONS`, because
  the comparison reports such a record through its coverage and nine field rows would state nine
  differences where there is one absence.
- **No subject compared**: `selection_state == "task_context"`, `comparison is None`,
  both sides `unresolved` with `text is None` and **the same** detail ("no knowledge operand was
  compared"), and an empty roster — the case a one-sided rendering must not swallow.

**The fixture helpers are typed and named.** `ExtraInvariantSeed` carries the identities, the
words and the origin state for one whole extra invariant; `OneSidedPair` carries the
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
- **Backend assertions and renderer assertions have separate fixtures and scope.** This module
  asserts its own statement constants, absent/unresolved details and `acceptance_ref` field row.
  The renderer suite uses synthetic statements; it supplies no shared-value or acceptance-field binding.
- **The acceptance row preserves a one-sided value.** Its before value is `None`, while its after
  value is present and starts with `text-knowledge:`. The structured-value case checks canonicality only.
- **Read-only after the fixture is built.** No case writes to either dataset, and the fixture is
  module-scoped precisely because that holds.
- **Boundary.** This is measurement, not a second implementation: the module imports
  `structured_value_text` to check the projection's key-order canonicality, and it re-derives no
  composition rule of its own.

### Todos

No current page-order/retained-revision limitation is established by this module. Current
composition calls `select_subject_revisions` for each tree's selected subject; an invariant text
record has one numeric revision and one statement.

**Historical selector account, not a current limitation:** the earlier R07 account described a
one-sided subject with several retained revisions, `_identity_item` returning `candidates`, and
page-order-dependent wording. That describes the former model, not the present selector or text
record shape. The old account is retained here only as history.

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



- **The fixture: two independently built snapshots under one namespace, and the four authored revisions that make an addition, a removal and a real transition.** [6]


- The one composition call, with the hand-assembled resolution and the loud failure on a refusal. [7]

- **The addition and the removal: the complete present-side statement, the named absent side with `text is None`, and the comparison's own side-absence code.** [8]
- The one-sided record reported by coverage with an empty roster, against the conditions the after side really recorded. [11]

- **The task-context case: no comparison, both sides unresolved with the same reason and no text, and no roster.** [12]



- Read fixture and test-only row builder supply both datasets. [15]





> Retained earlier citation wording: - **The lane row that selects this module, and the artifact consumer row that registers it against the fixture it consumes.** [16]





> Retained earlier citation wording: - The `consumer_scope = "exact"` artifact whose list this module joined. [17]




- The renderer displays before/after statements and its component tests use synthetic statement values; they neither import the Python statement constants nor assert acceptance_ref field rows. [18]


- Current revision selection takes the subject's own before/after item for each tree, rather than the historical _identity_item/page-order account. [19]

- An invariant text record stores one numeric revision and one statement, distinct from the former retained-revision model. [20]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture boundaries.

Fixture repositories and protocol doubles do not establish a live external integration.

- Retain the authored statement constants; remove the nonexistent SHARED_ACCEPTANCE_REF target. Acceptance is asserted by its text-knowledge prefix. [3]
- OneSidedPair remains the local frozen dataclass. Extra seeds are constructed by _extra; the former AuthoredInvariant target does not survive. [4]
- _extra constructs ExtraInvariantSeed values, and pair supplies them to the test fixture builder. The former author_invariant target is absent. [5]
- The exact roster is acceptance_ref, lifecycle and payload_digest; accepted provenance uses a text-knowledge acceptance prefix. [9]
- The retained function asserts key-order canonicality only and explicitly discloses withdrawal of its fixture-driven round trip. [10]
- The projection owner defines canonical structured-value text and its wrapper markers. The retained local test asserts key-order canonicality; marker round-trip test coverage is not claimed. [13]

- The current compose_review entry point takes resolution and request; the local review helper invokes it without the removed ReviewRecordInputs bag. [14]

- **The lane row that selects this module, and the artifact consumer row that registers it against the fixture it consumes.** [16]


- The `consumer_scope = "exact"` artifact whose list this module joined. [17]
