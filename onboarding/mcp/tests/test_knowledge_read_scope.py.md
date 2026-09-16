# mcp/tests/test_knowledge_read_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_read_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `1ff1893f44d875073d58af863238501a6be35288`|
| lastVerifiedCommitDate | 2026-09-16T23:58:57+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l07` uncommitted source; base `4eb2b1992f6183fba06e9f31aa664d9a93094c26` |
| governingOverview | `mcp/tests/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The node the requirement's non-conformance example points at: a one-item page still advertises the second location, with the corrected counts.** | "test_a_page_budget_of_one_item_still_advertises_the_second_location" | mcp/tests/test_knowledge_read_scope.py:547-657 |
| **The completeness node that compares the walk against the mandatory set derived from recorded rows rather than against the implementation's own page manifest.** | "test_every_page_declares_the_same_snapshot_and_manifest_and_the_union_equals_the_selection" | mcp/tests/test_knowledge_read_scope.py:658-721 |
| **The ordering node the review sealed as HIGH, and the fixture repair that made it deterministic.** | "test_the_item_stream_is_ordered_by_stored_identity_and_never_by_an_authored_label" | mcp/tests/test_knowledge_read_scope.py:722-837 |
| The packet's stopping-rule nodes, including the explicit `G` expansion that reaches K1. | "test_a_path_seed_returns_the_sibling_realizations_and_advertises_the_unreached_family"; "test_an_exact_invariant_revision_seed_selects_that_revision_and_its_directly_containing_families"; "test_an_exact_family_revision_seed_stops_after_its_own_members"; "test_selecting_the_advertised_family_explicitly_is_what_reaches_the_further_realizations" | mcp/tests/test_knowledge_read_scope.py:139-169; mcp/tests/test_knowledge_read_scope.py:170-205; mcp/tests/test_knowledge_read_scope.py:206-245; mcp/tests/test_knowledge_read_scope.py:246-274 |
| The two equivalence nodes (invariant versus family seed; path versus exact revision seed). | "test_the_invariant_seed_and_the_family_seed_enumerate_the_same_claims_and_locations"; "test_a_path_seed_and_the_exact_invariant_revision_seed_close_over_the_same_records" | mcp/tests/test_knowledge_read_scope.py:275-334; mcp/tests/test_knowledge_read_scope.py:335-393 |
| The revision-grouping nodes. | "test_an_identity_seed_returns_every_retained_revision_as_its_own_group"; "test_an_exact_revision_seed_does_not_select_the_identitys_other_retained_revisions" | mcp/tests/test_knowledge_read_scope.py:394-443; mcp/tests/test_knowledge_read_scope.py:444-474 |
| The count-separation and multi-family-membership nodes. | "test_claim_identities_and_distinct_source_locations_are_counted_separately"; "test_a_revision_reached_through_two_families_appears_once_with_both_membership_rows" | mcp/tests/test_knowledge_read_scope.py:475-509; mcp/tests/test_knowledge_read_scope.py:510-546 |
| The truncation, too-small-budget, execution-bound and absence nodes. | "test_a_truncated_page_states_that_items_remain_rather_than_claiming_completeness"; "test_a_page_budget_that_cannot_hold_one_item_refuses_and_keeps_the_position"; "test_a_selection_that_reaches_its_declared_bound_refuses_rather_than_reporting_a_total"; "test_the_declared_bound_admits_a_selection_that_fits_and_refuses_one_that_does_not"; "test_an_unregistered_path_reports_registration_absence_rather_than_an_empty_scope"; "test_a_selector_naming_no_recorded_identity_is_told_that_the_selector_is_absent" | mcp/tests/test_knowledge_read_scope.py:838-871; mcp/tests/test_knowledge_read_scope.py:872-901; mcp/tests/test_knowledge_read_scope.py:902-929; mcp/tests/test_knowledge_read_scope.py:930-961; mcp/tests/test_knowledge_read_scope.py:962-981; mcp/tests/test_knowledge_read_scope.py:982-1000 |
| **The persisted-nothing and namespace-confinement nodes.** | "test_a_refused_read_leaves_every_table_and_the_logical_digest_unchanged"; "test_the_selection_reads_only_the_requested_namespace" | mcp/tests/test_knowledge_read_scope.py:1001-1058; mcp/tests/test_knowledge_read_scope.py:1059-1163 |
| The fixture every node builds through the public store operations. | `build_read_scope_fixture` | mcp/tests/read_scope_test_support.py:266-284 |
| The lane row this module occupies. | "mcp/tests/test_knowledge_read_scope.py" | mcp/tests/test-evidence-lanes.toml:75 |
| The support artifact and contract this module is a declared consumer of. | "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1198-1221 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the unit-lane population. It records five groups by protected property and, in the form a successor needs, the two nodes the review made load-bearing: the **one-item page that still advertises the second location** (the requirement's own non-conformance example, with the corrected count semantics) and the **completeness node that derives the mandatory claim-id set from the recorded rows** instead of comparing the walk with the implementation's own full-budget page manifest — the circularity the round-1 review sealed. It records the **HIGH finding** on the ordering node and the fixture repair that made it deterministic, together with the rule to cite the pure label-major replacement (20/20) rather than the draw-dependent original. It also carries the forward constraints: **37 lines of headroom before the 1 200-line limit, so L8 must split this module before adding cases**, and the `_manifest_digest` composition is a reachable covered gap this module does not close (L9 ledger **A4**). Verification metadata remains empty until closeout stamps the code commit.
