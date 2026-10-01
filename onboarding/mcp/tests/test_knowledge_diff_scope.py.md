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
under the 1200-line rail, which leaves these thirteen cases in 790 lines. That module imports `diff_seed`
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

| Node | Line | What it owns |
| --- | ---: | --- |
| `test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union` | `:309` | The packet's **first non-conforming example**: the removed claim stays in the union with its before-side anchor at `exact_recorded_blob` and its path still in `attributed_changed_paths`. It is also the node mutation rows `M1` and `M2` kill — `M1` on `assert 'unchanged' == 'removed'` |
| `test_a_record_the_other_snapshot_holds_but_the_selection_missed_is_not_an_absence` | `:424` | Present-but-outside-the-selection is **not** deletion, and the two states are asserted **side by side** so the distinction cannot collapse. Its second half is the rule-2 subsumption measurement through the **published read surface** |

**The rule-2 subsumption half, as measured on these bytes.** For every authored edge each side declares,
that side's own tables hold **both** revisions it names — asserted per table, each predecessor table
asked with its own probe (`invariant_revision_is_recorded` at `:500`, `family_revision_is_recorded` at
`:509`), with the union identity asserted back against `fetch_predecessor_edges` at `:530`. The split is
the fix round 2 repair: `fetch_predecessor_edges` unions both tables, so asking the invariant probe about
a *family* endpoint was a false alarm on a legal snapshot — measured, one schema-valid family edge made
the pre-fix form fail at `:474`, while a dangling family edge now fails at `:509` and a dangling
invariant edge at `:500`. **The family half is nevertheless unexercised**: the fixture authors 0
`family_predecessor` rows (measured 2 invariant / 0 family before, 4 / 0 after), and the case's docstring
says so.

**The corrected coverage-rule reason, which is the leaf's most-corrected contract.** The ablation forms
(the fix rounds' own runs, reproduced independently by the final verification round on these bytes):

| Variant | Edit | Result on the owning nodes |
| --- | --- | --- |
| `A` | rule 1 removed | **2 assertion kills** — `assert 'absent_from_snapshot' == 'present_outside_selection'` |
| `B` | rule 2 removed | 7 passed — no state changes, because `_supersedes` is called 0 times on this population |
| `C` | rule 3's answer forced **absent** | **7 passed, and all 28 nodes of the two modules survive** |
| `C'` | rule 3's answer forced **present** | **2 assertion kills** — `assert 'present_outside_selection' == 'absent_from_snapshot'` |
| `D` | rules 1 + 2 removed | 2 kills, the same two nodes as `A` |
| `E` | collapsed to one rule | 2 kills — the collapse is measurably wrong |
| `G` | rule 1 removed **and** rule 3 forced absent | 2 kills — rule 2 does not cover them |

So **rule 1 is load-bearing alone**, **rule 3 is load-bearing in the forced-present direction**, and
**rule 2 cannot decide a state its neighbours do not** (it is kept as a short-circuit over
already-loaded lineage). The `2 failed` that an earlier artifact published for variant `C` belongs to
variant **`G`**; `C`'s own log records all survivors. **Collapsing the rules is wrong because it turns a
missing selection into a real absence** — the reverse of what the leaf first claimed.

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
- `superseding_revisions` is the one shared assertion helper; it exists because three cases read the same
  supersession pair.
- A case that needs a *different* snapshot state builds it through the public store operations
  (`add_unrelated_revision` in the boundary module, a real write in the continuation case) rather than by
  hand-editing a file.

### Invariants And Boundaries

- **Unit lane by behaviour, not by preference.** The module builds its two snapshots under `tmp_path`
  through the public store operations and drives the seam in-process; the only subprocesses are the
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
- **The revised statement as a successor pair, and the divergent revision groups an identity seed retains per side.** [3]
- **The source-only change: `record_field_changed=False` with `source_observation_changed=True`, on identical recorded anchors.** [4]
- The statement-only change that still returns the attributed code. [5]
- **The unchanged sibling returned on both sides rather than omitted, with one item each way across the record/source split.** [6]
- **The packet's first non-conforming example, and the node `M1`/`M2` kill.** [7]
- **The explicit per-side selectors addressing two different exact revisions of one identity.** [8]
- **The present-outside-versus-absent distinction side by side, and the per-table rule-2 subsumption assertion with its dangling-edge failure lines.** [9]
- **The filter narrowing the display and never the comparison, and the filter bound into the comparison identity.** [10]
- **`M26`'s node: the limitation validator, whose failing assertion on the frozen file is at `:658`.** [11]
- **`M25`'s node: the truncated comparison, whose failing assertion on the frozen file is at `:716`.** [12]
- The no-trees expansion that claims no change set. [13]
- The fixture these cases run on. [14]
- **The unit-lane row this module occupies, and the governed support artifact it consumes.** [15]

### Cross-Repo References

No cross-repository behaviour is exercised here. The fixture's Git trees are temporary and local, and
the comparison's source resolution is driven through the fixture's own committed trees.

No configured cross-repository evidence is claimed.
- **The unit-lane row this module occupies, and the governed support artifact it consumes.** [16]
