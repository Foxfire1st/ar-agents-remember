# mcp/tests/test_knowledge_diff_attribution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_diff_attribution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T23:41:23+02:00 |
| lastVerifiedCommitHash | `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4`|
| lastVerifiedCommitDate | 2026-09-29T00:17:28+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**The comparison's source attribution partition (`ICR-R04@v1`): nine unit cases, each asserting that
every measured changed path lands in exactly one bucket.** `260921-ICR-L4` added these cases to
[`test_knowledge_diff_scope.py`](test_knowledge_diff_scope.py.md). `260921-ICR-L57` moved them here
verbatim when that module crossed the 1200-line rail; no case was added, dropped or changed. The module
runs the same real comparison, over the two real databases and Git trees that
`diff_scope_test_support` builds. It is marked `pytest.mark.evidence_unit` and registered in the
**unit-regression** lane beside its sibling.

The properties, one case each:

- the measured change set is partitioned once into attributed, confirmed-unregistered and undetermined
  buckets, which are disjoint and exhaustive;
- a path realized only by another subject is attributed *outside the selection*, never read as
  unregistered;
- a family subject counts its own members' links as selected attribution;
- a registered mapping that never resolved establishes no attribution. The arithmetic case covers this,
  and so does the production-composition case, which authors the claims into the candidate snapshot and
  asserts the shipped reader's own resolutions for a stale or unresolvable mapping;
- one uninspected snapshot makes every unmapped change undetermined;
- a legitimately empty side counts as completely inspected; and
- an unavailable partition states no total and never a measured zero, and a partial observation states
  the scope of its own denominator.

## Code Commentary

### Logic

**The sibling's comparison helpers are shared, not restated.** The module imports `diff_seed` and
`run_diff` from `test_knowledge_diff_scope`, so both modules drive the public application seam the same
way. It defines its own three-line `fixture` over `build_diff_fixture`, as the sibling does; importing
the fixture would shadow a parameter and hide fixture discovery.

**Two kinds of case.** The fixture-driven cases read the partition the comparison's expansion publishes.
Where a knowledge-availability state cannot be reached with a fixture snapshot (an uninspected side, an
unavailable or partial observation), the case calls the partition owner directly
(`partition_attribution` / `unavailable_attribution`). It builds the inputs with `_observed`
(one complete observation of named paths) and `_inspected_sides` (two completely inspected snapshots).
`entry_link` reads the link label one measured path carries.

**The stale-mapping case authors real claims.** `_author_candidate_claim` writes one realization claim
into the candidate snapshot through `create_realization_claim`, exactly as the write plane does.
`_candidate_claim_resolutions` then reads the shipped reader's own resolutions for that path. So the
precedence is measured through production composition, not injected.

### Conventions

- Cases assert against `DiffFixture`'s named identity fields and path constants, never against a stream
  position.
- One case per property; the case name states the property.

### Invariants And Boundaries

- **Unit lane by behaviour.** Everything is built under `tmp_path` through public store operations; the
  only subprocesses are the fixture's own `git` calls.
- **Behaviour-preserving split.** The nine cases and their helpers are byte-identical to the section they
  came from. The collected node names match the pre-split population; only the module name in the node
  id changed.
- **Catalog footprint.** The module imports `diff_scope_test_support.py`, and reaches
  `read_scope_test_support.py` through it. The source-derived ownership census therefore names it on both
  artifacts' exact `consumers` rows, where it is declared beside its sibling. It registers no artifact of
  its own.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in this memory root. The statements below are grounded in
repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's statement of what it measures, and the import of the sibling's helpers. | "The comparison's source attribution partition: every measured changed path in exactly one bucket."; "from test_knowledge_diff_scope import diff_seed, run_diff" | mcp/tests/test_knowledge_diff_attribution.py:1-49 |
| The unit marker and the per-case fixture. | `pytestmark`; `fixture` | mcp/tests/test_knowledge_diff_attribution.py:51-58 |
| The sibling's comparison helpers these cases reuse. | `diff_seed`; `run_diff` | mcp/tests/test_knowledge_diff_scope.py:68-75; mcp/tests/test_knowledge_diff_scope.py:78-113 |
| **The partition case: the measured changes divided once into attributed, confirmed unregistered and undetermined, with the buckets disjoint and exhaustive.** | "test_the_measured_changes_are_partitioned_once_and_the_buckets_are_disjoint_and_exhaustive" | mcp/tests/test_knowledge_diff_attribution.py:64-135 |
| **The boundary case: a change mapped only to another invariant is outside selection, never unregistered.** | "test_a_change_mapped_only_to_another_invariant_is_outside_selection_not_unregistered"; `entry_link` | mcp/tests/test_knowledge_diff_attribution.py:144-183; mcp/tests/test_knowledge_diff_attribution.py:138-141 |
| **The family-subject case: a family's members' own links count as selected attribution.** | "test_a_family_subject_counts_its_members_own_links_as_selected_attribution" | mcp/tests/test_knowledge_diff_attribution.py:186-218 |
| **The precedence cases: a registered mapping that did not resolve — stale or unresolvable — does not establish attribution.** | "test_a_registered_mapping_that_did_not_resolve_does_not_establish_attribution"; "test_a_stale_or_unresolvable_mapping_does_not_establish_attribution" | mcp/tests/test_knowledge_diff_attribution.py:221-299; mcp/tests/test_knowledge_diff_attribution.py:302-364 |
| The production-composition helpers the stale-mapping case authors and reads claims through. | `_author_candidate_claim`; `_candidate_claim_resolutions` | mcp/tests/test_knowledge_diff_attribution.py:367-403; mcp/tests/test_knowledge_diff_attribution.py:406-423 |
| **The incompleteness cases: one uninspected snapshot turns every unmapped change undetermined; a legitimately empty side counts as completely inspected.** | "test_one_uninspected_snapshot_turns_every_unmapped_change_into_undetermined_attribution"; "test_a_legitimately_empty_side_counts_as_completely_inspected_for_absence" | mcp/tests/test_knowledge_diff_attribution.py:426-488; mcp/tests/test_knowledge_diff_attribution.py:491-526 |
| **The honesty cases: an unavailable partition states no total and never a measured zero; a partial observation states its denominator's scope.** | "test_an_unavailable_partition_states_no_total_and_never_a_measured_zero"; "test_a_partial_observation_states_the_scope_of_its_own_denominator" | mcp/tests/test_knowledge_diff_attribution.py:529-555; mcp/tests/test_knowledge_diff_attribution.py:558-601 |
| The arithmetic cases' two input builders. | `_observed`; `_inspected_sides` | mcp/tests/test_knowledge_diff_attribution.py:604-607; mcp/tests/test_knowledge_diff_attribution.py:610-626 |
| The unit-regression lane row, beside its sibling's. | "mcp/tests/test_knowledge_diff_attribution.py" | mcp/tests/test-evidence-lanes.toml:139-139 |
| The two support artifacts whose exact `consumers` lists declare this module (at `:1442` and `:1493`). | "path = \"mcp/tests/diff_scope_test_support.py\""; "path = \"mcp/tests/read_scope_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:1425-1470; mcp/tests/evidence-lifecycle.toml:1473-1529 |

## Cross-Repo References

No cross-repository behaviour is exercised here. The fixture's Git trees are temporary and local.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured cross-repository evidence is claimed. | — | — |

## Update History

- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): created this one-to-one card for the attribution-partition cases, which the worker moved verbatim out of `test_knowledge_diff_scope.py` (1384 → 790 lines there; 626 lines and 9 cases here). The six case rows moved from `test_knowledge_diff_scope.py.md`, where they were removed, and their ranges were re-derived to each case's own extent. The case list reuses the `260921-ICR-L4` curator's account of the nine cases. New rows cite the helpers, the lane row and the two consumer declarations. Verification metadata remains empty until closeout stamps the code commit.
