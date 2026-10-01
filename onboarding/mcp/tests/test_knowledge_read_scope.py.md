# mcp/tests/test_knowledge_read_scope.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The selective recorded-scope read's unit-lane population: the selection policy, revision grouping, the
corrected count semantics, paging, budget, the execution bound and typed absence.** Twenty-one nodes in
`unit-regression` (row `mcp/tests/test-evidence-lanes.toml:75`), all hermetic — temporary directories under
`tmp_path`, in-process APSW databases, no repository working tree, no network, no integration marker.

**It is at 1 163 of the repository's 1 200-line hard limit: 37 lines of headroom. L8 must split it before
adding cases**, which is exactly what fix round 2 did for the integration side rather than waiving the
limit.

## Code Commentary

### Logic

The nodes group by the property each protects, and the grouping is the useful reading:

**The packet's stopping rule** (`:139`–`:390`) — the five nodes that measure the `P/I1/F/J1/G/K1` graph and
its two subtleties: a path seed returns the sibling's realizations and **advertises** the unreached family;
an exact family revision seed stops after its own members; selecting the advertised family **explicitly** is
what reaches the further realizations; the invariant seed and the family seed enumerate the same claims and
locations; and a path seed and the exact invariant revision seed close over the same records. One node
(`:510`) measures that a revision reached through two families appears **once** with both membership rows.

**Revision grouping and the absent current-revision pointer** (`:391`–`:471`) — an identity seed returns
every retained revision as its own group, and an exact revision seed does **not** select the identity's
other retained revisions. Nothing in either node can be read as a version or an insertion ordering.

**Counts** (`:472`–`:543`) — claim identities and distinct source locations are counted **separately**
(a node that would pass under a single collapsed counter fails here).

**Paging: completeness by continuation** (`:544`–`:958`) — the coverage the phase-1 candidate got wrong and
the review sealed:

- **`test_a_page_budget_of_one_item_still_advertises_the_second_location`** (`:547`) is the node the
  requirement's own non-conforming example points at: a one-item page must not imply the invariant has one
  implementation. It asserts the corrected arithmetic — page 2's `primary_items_total` is the **declared**
  total, `primary_items_returned` is the walk's cumulative progress, and a later page's refusal still
  leaves every table and the logical digest unchanged.
- **`test_every_page_declares_the_same_snapshot_and_manifest_and_the_union_equals_the_selection`** (`:658`)
  derives the mandatory claim-id set from the **recorded rows** and compares the walk's union with it,
  rather than comparing the walk with the implementation's own full-budget page manifest. That
  circularity was the round-1 finding, and the derived comparison is the repair.
- The truncation (`:838`), too-small-budget (`:872`), execution-bound (`:902`, `:930`) and
  declared-order (`:722`) nodes.

**Absence and the persisted-nothing property** (`:959`–`:1163`) — `registration_absent` for an
unregistered path, `selector_absent` for an identity that names nothing, a refused read leaving every table
and the logical digest unchanged, and one node measuring that the selection reads only the requested
namespace.

### The ordering node, and why the fixture had to change

`test_the_item_stream_is_ordered_by_stored_identity_and_never_by_an_authored_label` (`:722`) is the node
the baseline review sealed as **HIGH**: as published it was true for only about two of three fixture draws,
because two successors share the `v2` label and a stable label sort can coincide with the stored-id order,
so the leaf's own unit module was intermittently red. The repair is in the **fixture** (the three retry
revision ids are now allocated with deterministic prefixes and the predecessor carries a distinct label)
plus an assertion that the emitted page order **differs** from the label-major order, so the property is
measured on every draw rather than on the draws that happen to disagree.

**The deterministic replacement for that property is the pure label-major key `(kind, label, item_id)`,
measured at 20/20 across three samples.** The original draw-dependent `X1b` shape is **not** the row a
successor should cite; the erratum's `4/6, 4/6, 6/6, 6/6` figures and the discarded 27-run total belong to
the evidence apparatus, not to this module's contract.

### Conventions

- `pytestmark = pytest.mark.evidence_unit`; the lane is declared in `mcp/tests/test-evidence-lanes.toml`
  and the module's support artifact in `mcp/tests/evidence-lifecycle.toml`. **An unregistered module makes
  `load_lane_manifest` refuse the repository**, so a row is a precondition rather than bookkeeping.
- Every case builds its own fixture through the public store operations; none inserts rows directly.
- Assertions name the property, not the implementation's internal shape.

### Invariants And Boundaries

- **Nothing here asserts a semantic verdict.** No node expects a "current", "accepted", "severity" or
  "ranked" field, because the response model has no field that could hold one.
- **A survivor is not coverage.** Any claim that a mutated line is protected must come from a node that
  fails on an assertion against the mutated production line; an exception death is not a kill.
- **Boundary.** This is a test module. It declares one lane, asserts behaviour and owns no production
  contract.

### Todos

None recorded. Two carried items belong to the owning seat: the **`_manifest_digest` composition** is a
reachable covered gap this module does not close (L9 ledger **A4**), and the module's remaining headroom is
37 lines before the 1 200-line limit.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The node the requirement's non-conformance example points at: a one-item page still advertises the second location, with the corrected counts.** [1]
- **The completeness node that compares the walk against the mandatory set derived from recorded rows rather than against the implementation's own page manifest.** [2]
- **The ordering node the review sealed as HIGH, and the fixture repair that made it deterministic.** [3]
- The packet's stopping-rule nodes, including the explicit `G` expansion that reaches K1. [4]
- The two equivalence nodes (invariant versus family seed; path versus exact revision seed). [5]
- The revision-grouping nodes. [6]
- The count-separation and multi-family-membership nodes. [7]
- The truncation, too-small-budget, execution-bound and absence nodes. [8]
- **The persisted-nothing and namespace-confinement nodes.** [9]
- The fixture every node builds through the public store operations. [10]
- The lane row this module occupies. [11]
- The support artifact and contract this module is a declared consumer of. [12]
- The support artifact and contract this module is a declared consumer of. [13]
- The lane row this module occupies. [14]
- The support artifact and contract this module is a declared consumer of. [15]
- The support artifact and contract this module is a declared consumer of. [16]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
- The support artifact and contract this module is a declared consumer of. [17]
- The support artifact and contract this module is a declared consumer of. [18]
