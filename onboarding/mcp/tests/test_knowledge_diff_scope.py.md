# mcp/tests/test_knowledge_diff_scope.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**The comparison's unit population: thirteen cases over the shared two-snapshot fixture, running
in-process with no repository working tree, no network and no integration marker**
(`pytestmark = pytest.mark.evidence_unit`). The module is registered in the **unit-regression** lane at
`mcp/tests/test-evidence-lanes.toml:138`.

**The attribution partition's nine cases live next door.** `260921-ICR-L4` appended nine `ICR-R04@v1`
cases here (22 cases, 1384 lines). `260921-ICR-L57` moved them verbatim into
[`test_knowledge_diff_attribution.py`](test_knowledge_diff_attribution.py.md) to bring this module back
under the 1200-line rail, which leaves these thirteen cases in 714 lines. That module imports `diff_seed`
and `run_diff` from here, so both drive the comparison the same way.

Every case is named for the property it protects rather than for the fixture state it happens to use,
and the population is deliberately one case per packet obligation: statement-only, source-only,
removed link, unchanged sibling, divergent revisions, explicit per-side selectors, the
present-outside-selection distinction, the display filter, the filter's binding, the limitation
validator, truncation, and the no-trees expansion.

**Frozen identity at review: 779 lines.** The bare `:NNN` line numbers in the prose below were measured
against that file; the reference table cites the current 790-line module. The leaf's own evidence artifacts republish a **`M25`/`M26` citation pair that does
not exist on these bytes** — `scope:640` / `:678` and `scope:565` / `:620`, which are the **pre-round
741-line file's** numbers — and are carried to
`KS-R09`/`L9` as documentation debt (ledger entry **A9**, finding **`L8-W1`**). **This card's numbers are
the measured ones and the ledger is authoritative for the contested pair.**

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

- `test_a_comparison_that_declares_a_limit_it_did_not_establish_fails_construction` (`:603`, failing
  assertion `:658`) — the limitation/omission check runs **in both directions**.
- `test_a_truncated_comparison_cannot_be_presented_as_a_complete_one` (`:678`, failing assertion `:716`)
  — a truncated comparison is never presentable as complete. **These two nodes are `M26` and `M25`
  respectively**, and these are the measured line numbers (a verification report's `:570` is inside the
  first node's docstring; the number pytest reports for its row is `:658`).
- `test_the_filter_is_bound_into_the_comparison_identity_so_another_filter_cannot_reuse_it` (`:576`) —
  a continuation cannot silently change the filter it was a position in.
- `test_the_expansion_of_a_comparison_that_observed_no_trees_claims_no_change_set` (`:742`) — the
  comparison whose sides named no code tree claims no change set.

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
- **No weakened evidence.** No `skip`, `xfail`, `deselect`, per-file ignore, widened limit or deleted
  node; thirteen cases before and after fix round 2's test-side edit.
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

None recorded. `M25`/`M26`'s citations are correct **here** and must not be copied from the leaf's
artifacts, whose pair is stale; if a successor needs the exact nodes, use the two entries in the
"honesty properties" list above.

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

- **`M26`'s node: the limitation validator, whose failing assertion on the frozen file is at `:658`.** [11]
- **`M25`'s node: the truncated comparison, whose failing assertion on the frozen file is at `:716`.** [12]
- The no-trees expansion that claims no change set. [13]

- The fixture these cases run on. [14]

> Retained earlier citation wording: - **The unit-lane row this module occupies, and the governed support artifact it consumes.** [15]

### Cross-Repo References

No cross-repository behaviour is exercised here. The fixture's Git trees are temporary and local, and
the comparison's source resolution is driven through the fixture's own committed trees.

No configured cross-repository evidence is claimed.
> Retained earlier citation wording: - **The unit-lane row this module occupies, and the governed support artifact it consumes.** [16]

- **The unit-lane row this module occupies, and the governed support artifact it consumes.** [15]


- **The unit-lane row this module occupies, and the governed support artifact it consumes.** [16]
