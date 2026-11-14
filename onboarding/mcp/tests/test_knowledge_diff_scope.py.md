# mcp/tests/test_knowledge_diff_scope.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**The comparison's unit population: thirteen cases over the shared two-snapshot fixture, running
in-process with no repository working tree, no network and no integration marker**
(`pytestmark = pytest.mark.evidence_unit`). The module is registered in the **unit-regression** lane at
`mcp/tests/test-evidence-lanes.toml:228`.

**The attribution partition's original nine-case cohort lives next door; that sibling now has ten source test definitions.** `260921-ICR-L4` appended nine `ICR-R04@v1`
cases here (22 cases, 1384 lines). `260921-ICR-L57` moved them verbatim into
[`test_knowledge_diff_attribution.py`](test_knowledge_diff_attribution.py.md) to bring this module back
under the 1200-line rail, which leaves these thirteen cases in 714 lines. That module imports `diff_seed`
and `run_diff` from here, so both drive the comparison the same way.

Every case is named for the property it protects rather than for the fixture state it happens to use,
and the population is deliberately one case per packet obligation: statement-only, source-only,
removed link, unchanged sibling, divergent revisions, explicit per-side selectors, the
present-outside-selection distinction, the display filter, the filter's binding, the limitation
validator, truncation, and the no-trees expansion.

**Current source identity: 714 physical lines and thirteen top-level test definitions**
at code tree `96bf7343`, measured by complete AST inspection. The earlier card's
779-line review freeze, 741-line pre-round file, 790-line reference account and
`M25`/`M26` citation dispute belong to earlier source epochs; those coordinates
are not current navigation. The live function names and extents below describe
this code tree. Earlier ledger/debt and mutation accounts remain historical
provenance, with no new execution or verdict inferred.

## Code Commentary

### Logic

`run_diff(fixture, seed, …)` drives the **public application seam**
(`application.knowledge_diff.diff_knowledge_scope`) over the fixture's two database paths and the two
resolved sides, so the cases exercise the contract a caller uses rather than the comparison's private
helpers. `item_for(result, item_id)` and `items_of(result, kind)` read the union by stable identity, so
a case names the record it is about rather than a position in the stream.

**The two cases the review made load-bearing:**


| Node | What it owns |
| --- | --- |
| `test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union` | The packet's **first non-conforming example**: the removed claim stays in the union with its before-side anchor at `exact_recorded_blob` and its path still in `attributed_changed_paths`. It is also the node mutation rows `M1` and `M2` kill — `M1` on `assert 'unchanged' == 'removed'` |
| `test_a_revised_statement_arrives_as_a_successor_alongside_the_revision_it_replaced` | The revised statement reads as a removal beside an unrelated addition — never a succession — with each side present outside the other's selection, because the candidate selected another exact revision of the same identity |

**The corrected coverage-rule reason, which is the leaf's most-corrected contract.** Two ways of
establishing that the other snapshot holds a record — the other side *selected* another exact
revision of the same identity, and the other side's *tables* hold the record by its own key —
and they are not two independent deciders: removing the first turns a missing selection into a real
absence, while forcing the second present turns a genuine deletion into a missing selection.
**Collapsing the rules is wrong because it turns a missing selection into a real absence** — the reverse of what the leaf first claimed.

**The nodes that hold the response's honesty properties:**

- `test_a_comparison_that_declares_a_limit_it_did_not_establish_fails_construction`
  (`:529-610`) checks limitation/omission agreement in both directions; the
  model-owned refusal assertion is at `:604-607`.
- `test_a_truncated_comparison_cannot_be_presented_as_a_complete_one`
  (`:613-674`) checks honest complete/truncated pages and contradictory states;
  the model-owned refusal assertion is at `:672-674`.
- `test_the_filter_is_bound_into_the_comparison_identity_so_another_filter_cannot_reuse_it`
  (`:502-523`) keeps continuation identity bound to the filter.
- `test_the_expansion_of_a_comparison_that_observed_no_trees_claims_no_change_set`
  (`:677-714`) reports the missing source observation without claiming an empty change set.

The former `M26`/`M25` names are historical mutant attribution, not results of
executing those mutants on this tree.

### Conventions

- Cases assert against `DiffFixture`'s **named identity fields**, never against a stream position.
- `superseding_revisions` is the one shared assertion helper: the revisions the candidate holds that
  the baseline's selection does not reach — named for the coverage state, not for a succession.
- A case that needs a *different* snapshot state builds it through the public rows builder
  (`rebuild_after_tree` carries a whole candidate-side delta) rather than by hand-editing a file.

### Invariants And Boundaries

- **Unit lane by behaviour, not by preference.** The module builds its two snapshots under `tmp_path`
  through the rows builder and drives the seam in-process; the only subprocesses are the
  fixture's own `git` calls.
- **Historical fix-round boundary.** The earlier card recorded no `skip`, `xfail`, `deselect`, per-file ignore, widened limit or deleted node and thirteen cases before and after that fix round 2. That account is not fresh execution evidence for this tree.
- **The evidence debt this module's numbers carry.** The mutation taxonomy over `M1`…`M27` is **19
  assertion kills, 1 exception death, 3 equivalent mutants, 3 covered gaps and 1 non-experiment = 27**;
  the four non-kill classes are disclosed as such and are recorded in
  `memory/knowledge/diff.py`'s card with the input that would close each. The leaf's **contested evidence
  items** — the stale `M25`/`M26` citations published as "regenerated from the frozen file", a cited
  artifact that does not exist, three counts and one set-statement that do not reproduce, and row tables
  attributed to the frozen bytes but measured before the round's own edit — are carried to `KS-R09`/`L9`
  (ledger **A9**/**A10**); **none of them changes a verdict**, and this card cites only the measured
  numbers.
- **Boundary.** This module measures the comparison through its public seam. It does not re-implement
  selection, and it asserts nothing about a refusal code the seam does not return.

### Todos

None recorded. Use the current named functions and extents in the "honesty properties" list above. The earlier `M25`/`M26` citation dispute and its ledger account do not establish current source coordinates.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. The statements below are grounded in
repository source and package-local evidence only.

No configured domain documentation could be checked.

### Repo-Internal References

- The unit marker, the fixture, the seed and the public-seam driver every case uses. [1]

- The two readers that let a case name a record rather than a position. [2]


- **The revised statement as removal beside unrelated addition, and the divergent revision groups an identity seed retains per side.** [3]


- **The source-only change: `record_field_changed=False` with `source_observation_changed=True`, on identical recorded anchors.** [4]

- The statement-only change that still returns the attributed code. [5]
- **The unchanged sibling returned on both sides rather than omitted, with one item each way across the record/source split.** [6]
- **The packet's first non-conforming example, and the node `M1`/`M2` kill.** [7]

- **The explicit per-side selectors addressing two different exact revisions of one identity.** [8]


- The present-outside-versus-absent distinction asserted side by side, and the coverage decision's two selection- and probe-based rules -- another exact revision selected, or the record held by the other side's tables -- with no authored edge participating. [9]


- **The filter narrowing the display and never the comparison, and the filter bound into the comparison identity.** [10]

- The limitation/omission model guard, with honest construction and both mismatch directions checked in the named current function. Historical mutant attribution: `M26`. [11]
- Complete/truncated page agreement and the model-owned contradiction refusal in the named current function. Historical mutant attribution: `M25`. [12]
- The no-trees expansion that claims no change set. [13]

- The fixture these cases run on. [14]

> Retained earlier citation wording: - **The unit-lane row this module occupies, and the governed support artifact it consumes.**

### Cross-Repo References

No cross-repository behaviour is exercised here. The fixture's Git trees are temporary and local, and
the comparison's source resolution is driven through the fixture's own committed trees.

No configured cross-repository evidence is claimed.
> Retained earlier citation wording: - **The unit-lane row this module occupies, and the governed support artifact it consumes.**




- **The unit-lane row this module occupies, and the governed support artifact it consumes.** Anchor: "evidence_node = \"mcp/tests/test_knowledge_diff_scope.py::test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union\"" Anchor: "evidence_node = \"mcp/tests/test_knowledge_diff_scope.py::test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union\"" [15]




- **The unit-lane row this module occupies, and the governed support artifact it consumes.** Anchor: "evidence_node = \"mcp/tests/test_knowledge_diff_scope.py::test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union\"" Anchor: "evidence_node = \"mcp/tests/test_knowledge_diff_scope.py::test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union\"" [16]
