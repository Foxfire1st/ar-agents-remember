# mcp/tests/test_knowledge_diff_attribution.py

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

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. The statements below are grounded in
repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The module's statement of what it measures, and the import of the sibling's helpers. [1]
- The unit marker and the per-case fixture. [2]
- The sibling's comparison helpers these cases reuse. [3]
- **The partition case: the measured changes divided once into attributed, confirmed unregistered and undetermined, with the buckets disjoint and exhaustive.** [4]
- **The boundary case: a change mapped only to another invariant is outside selection, never unregistered.** [5]
- **The family-subject case: a family's members' own links count as selected attribution.** [6]
- **The precedence cases: a registered mapping that did not resolve — stale or unresolvable — does not establish attribution.** [7]
- The production-composition helpers the stale-mapping case authors and reads claims through. [8]
- **The incompleteness cases: one uninspected snapshot turns every unmapped change undetermined; a legitimately empty side counts as completely inspected.** [9]
- **The honesty cases: an unavailable partition states no total and never a measured zero; a partial observation states its denominator's scope.** [10]
- The arithmetic cases' two input builders. [11]
- The unit-regression lane row, beside its sibling's. [12]
- The two support artifacts whose exact `consumers` lists declare this module (at `:1442` and `:1493`). [13]

### Cross-Repo References

No cross-repository behaviour is exercised here. The fixture's Git trees are temporary and local.

No configured cross-repository evidence is claimed.
