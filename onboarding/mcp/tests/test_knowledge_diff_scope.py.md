# mcp/tests/test_knowledge_diff_scope.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**The comparison's unit population: thirteen cases over the shared two-snapshot fixture, running
in-process over temporary fixture repositories, with no network and no integration marker**
(`pytestmark = pytest.mark.evidence_unit`). The module is registered in the **unit-regression** lane at
`mcp/tests/test-evidence-lanes.toml:237`.

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

**Current source identity: 714 physical lines and thirteen top-level test definitions**,
measured by complete static AST/source inspection. The earlier 779-line review freeze,
741-line pre-round file and790-line reference account belong to earlier source epochs.
The parked account records the former `M25`/`M26` pairs `scope:640`/`:678` and
`scope:565`/`:620` as documentary debt carried to `KS-R09`/`L9` (ledger A9, finding `L8-W1`).
Those retained historical coordinates and mutant attributions are not current navigation
or a fresh authority, execution or verdict; current functions and assertion extents follow below.

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
| `test_a_revised_statement_arrives_as_a_successor_alongside_the_revision_it_replaced` | The two exact revisions of the same identity appear as separate removal and addition items. Each revision is present outside the other side’s selection. |

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
  (`:502-523`) requires different display policies for different filters while keeping the
  comparison binding and selector digests equal; it presents no continuation cursor.
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


- The unit marker, per-test fixture builder, identity seed and application comparison driver. [1]


- The two readers that let a case name a record rather than a position. [2]



- The comparison shows the two exact revisions of one identity as separate removal and addition items. The identity seed retains one selected revision in each side's group. [3]



- Both claims at the rewritten path retain their recorded source identities. The comparison reports a source-observation change and no record-field change for each. [4]



- The new revision remains an added record with a candidate-side exact-recorded-blob attribution. The case asserts no source-observation change. [5]


- The removed realization retains its baseline anchor at exact_recorded_blob in the comparison union, and its path remains attributed. [7]



- The explicit before and after selectors name different revisions of the same invariant. The union reports the old revision on the before side and the new revision on the after side. [8]



- The test distinguishes an unselected revision from a removed realization. The coverage implementation checks for another selected revision of the same identity before probing whether the other side stores the item. [9]


- The limitation/omission model guard, with honest construction and both mismatch directions checked in the named current function. Historical mutant attribution: `M26`. [11]
- Complete/truncated page agreement and the model-owned contradiction refusal in the named current function. Historical mutant attribution: `M25`. [12]

- The comparison still returns a page without named code trees. The source expansion carries neither a measured unattributed path nor an unattributed-path limitation. [13]


- The fixture these cases run on. [14]

> Retained earlier citation wording: - **The unit-lane row this module occupies, and the governed support artifact it consumes.**

### Cross-Repo References

No cross-repository behaviour is exercised here. The fixture's Git trees are temporary and local, and
the comparison's source resolution is driven through the fixture's own committed trees.

No configured cross-repository evidence is claimed.
> Retained earlier citation wording: - **The unit-lane row this module occupies, and the governed support artifact it consumes.**

### Repo-Internal References (continued)





- The filter narrows the display without changing comparison totals; its policy differs while comparison binding and selector digests remain equal. [10]

### Repo-Internal References (renewed)

- The two sibling claims are returned on both sides with unchanged record fields; both have changed source observations, with no still-source item in this fixture. Anchor: "test_an_unchanged_sibling_is_returned_identically_on_both_sides_rather_than_omitted" [6]




- The lifecycle catalog binds the diff-scope support artifact to the exact baseline-union proof node. [16]






- **The unit-lane row this module occupies, and the governed support artifact it consumes.** Anchor: "evidence_node = \"mcp/tests/test_knowledge_diff_scope.py::test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union\"" Anchor: "evidence_node = \"mcp/tests/test_knowledge_diff_scope.py::test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union\"" [15]
