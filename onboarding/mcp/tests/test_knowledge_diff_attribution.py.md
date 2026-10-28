# mcp/tests/test_knowledge_diff_attribution.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**The comparison's source attribution partition (`ICR-R04@v1`): nine unit cases, each asserting that
every measured changed path lands in exactly one bucket.** `260921-ICR-L4` added these cases to
[`test_knowledge_diff_scope.py`](test_knowledge_diff_scope.py.md). `260921-ICR-L57` moved them here
verbatim when that module crossed the 1200-line rail; no case was added, dropped or changed. The module
runs the same real comparison, over the fixture-built candidate snapshots and real Git trees that
`diff_scope_test_support` builds. It is marked `pytest.mark.evidence_unit` and registered in the
**unit-regression** lane beside its sibling.

The properties, one case each:

- the measured change set is partitioned once into attributed, confirmed-unregistered and undetermined
  buckets, which are disjoint and exhaustive;
- a path realized only by another subject is attributed *outside the selection*, never read as
  unregistered;
- a family subject counts its own members' links as selected attribution;
- a registered mapping that never resolved establishes no attribution. The arithmetic case covers this,
  and so does the fixture-composition case, which authors the claims into the candidate snapshot with
  the fixture constructors and asserts the shipped reader's own resolutions for a stale or unresolvable
  mapping;
- one uninspected snapshot makes every unmapped change undetermined;
- a legitimately empty side counts as completely inspected; and
- an unavailable partition states no total and never a measured zero, and a partial observation states
  the scope of its own denominator.

## Code Commentary


The comparison partitions the measured changed-path population into disjoint attributed, confirmed-unregistered and unknown-attribution buckets. Unchanged mapped paths contribute no changed count, repeated claims contribute one path, and selected-subject links are distinguished from completely established outside-selection links. Family scope comes from exact membership revisions.

Unresolved or stale locators do not establish attribution. An unread snapshot prevents a negative conclusion and qualifies outside-selection membership; a known-empty inspected side can support absence. An unavailable observation carries null totals, while a partial denominator names omitted uncarriable paths.

The two-tree fixture and extra realization rows use test-only knowledge_rows_test_support constructors. `_author_candidate_claim` is a fixture helper despite its historical write-plane docstring. Surviving production anchor readers, source measurement and partition/comparison code supply the asserted output; this suite does not prove canonical write admission.

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
into the candidate snapshot through `create_realization_claim`, built on the fixture constructors
(`anchor_fixture_models` drafts, `DiffFixture`), not the production write plane. `_candidate_claim_resolutions` then reads the shipped reader's own resolutions for that path. So the
precedence is measured through production composition, not injected.

### Conventions

- Cases assert against `DiffFixture`'s named identity fields and path constants, never against a stream
  position.
- One case per property; the case name states the property.

### Invariants And Boundaries

- **Unit lane by behaviour.** Everything is built under `tmp_path`; the
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

## Evidence


### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_the_measured_changes_are_partitioned_once_and_the_buckets_are_disjoint_and_exhaustive` supplies the current fixture or assertion described above. [14]
- `test_a_registered_mapping_that_did_not_resolve_does_not_establish_attribution` supplies the current fixture or assertion described above. [15]
- `test_one_uninspected_snapshot_turns_every_unmapped_change_into_undetermined_attribution` supplies the current fixture or assertion described above. [16]
- `test_an_unavailable_partition_states_no_total_and_never_a_measured_zero` supplies the current fixture or assertion described above. [17]

- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [18]


- RowStore writes text-tree fixture rows without the retired production admission plane. [19]


### Docs References

No Domain Documentation entries are configured in this memory root. The statements below are grounded in
repository source only.

No configured domain documentation could be checked.


- The unit marker and the per-case fixture. [20]

- The sibling's comparison helpers these cases reuse. [21]
- **The partition case: the measured changes divided once into attributed, confirmed unregistered and undetermined, with the buckets disjoint and exhaustive.** [22]

- The boundary case: a change mapped only to another invariant is outside selection, never unregistered. [23]


- **The family-subject case: a family's members' own links count as selected attribution.** [24]



- The precedence cases: a registered mapping that did not resolve — stale or unresolvable — does not establish attribution. [25]



- The production-composition helpers the stale-mapping case authors and reads claims through. [26]


- The incompleteness cases: one uninspected snapshot turns every unmapped change undetermined; a legitimately empty side counts as completely inspected. [27]

- The honesty cases: an unavailable partition states no total and never a measured zero; a partial observation states its denominator's scope. [28]


- The arithmetic cases' two input builders. [29]






> Retained earlier citation wording: - The unit-regression lane registers test_knowledge_diff_attribution.py. Seven lifecycle artifact lists declare it as a consumer: _user_settings_guard.py, anchor_fixture_models.py, diff_scope_test_support.py, the Node package-lock fixture, knowledge_row_codec_test_support.py, knowledge_rows_test_support.py and read_scope_test_support.py. Declaration is not execution.



### Cross-Repo References

No cross-repository behaviour is exercised here. The fixture's Git trees are temporary and local.

No configured cross-repository evidence is claimed.









- The unit-regression lane row, beside its sibling's.  Anchor: `test_knowledge_diff_attribution` [30]


- The unit-regression lane registers test_knowledge_diff_attribution.py. Seven lifecycle artifact lists declare it as a consumer: _user_settings_guard.py, anchor_fixture_models.py, diff_scope_test_support.py, the Node package-lock fixture, knowledge_row_codec_test_support.py, knowledge_rows_test_support.py and read_scope_test_support.py. Declaration is not execution.

- The unit-regression lane registers test_knowledge_diff_attribution.py. Seven lifecycle artifact lists declare it as a consumer: _user_settings_guard.py, anchor_fixture_models.py, diff_scope_test_support.py, the Node package-lock fixture, knowledge_row_codec_test_support.py, knowledge_rows_test_support.py and read_scope_test_support.py. Declaration is not execution. [31]

## Retirements

- Retired at the fifth freeze d59c3493: mcp/tests/evidence-lifecycle.toml:352-352 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:800-800 - the bytes it recorded now occur 4 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:1202-1202 - the bytes it recorded now occur 5 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2029-2029 - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2740-2740 - the bytes it recorded now occur 50 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2783-2783 - the bytes it recorded now occur 7 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:3299-3299 - the bytes it recorded now occur 5 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
