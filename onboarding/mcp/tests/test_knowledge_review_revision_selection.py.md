# mcp/tests/test_knowledge_review_revision_selection.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose
Pins revision-head selection without guessed winners, including explicitly damaged fixture graphs.

## Code Commentary
A unique successor chain defaults to the before head and after head, while an intermediate revision remains explicitly selectable. Forks name competing heads and choose no pair. A known-empty after side preserves a removal with its before revision. Heads come from successor edges rather than sorted identity strings, and the review pane renders the selected pair's own statements.

Fixture construction uses test-only RowStore and revision containers, not a validating production writer. Cycle and dangling-edge cases deliberately alter their scratch dataset to exercise reader refusal; the reason for that SQL is controlled corrupt read input, not proof that a shipped admission layer prevented the graph. Cyclic or missing predecessor evidence remains unresolved and names no guessed pair.

### Logic
**`_select` runs the adapter's own function, not a copy of its rule.** It calls
`select_subject_revisions` over the comparison's union items with the identity seed and the two
snapshot files — the exact call `compose_review` makes — and asserts the recorded selection. The
order-independence case (`test_heads_come_from_successors_not_from_sorted_order`) calls
`revision_heads` directly with adversarially sorted ids, proving the successor relation beats stream
position.

**The pane case closes the loop through the served payload.** `_git_tree`/`_git` build two real Git
trees, `compose_review` renders them, and the case asserts the pane's `revision_selection` is the
compared head pair *and* both statements are `present` carrying the heads' own recorded texts — the
conforming example the packet requires, measured where a reader actually sees it.

### Conventions
The module declares `pytestmark = pytest.mark.evidence_unit` (`:66`), which is what makes the lane
classification its own rather than a budget convenience: every case runs in-process over temporary
snapshots and one temporary Git pair, with no DAG, no network and no retained service. Helpers are
private (`_authorship`, `_build_snapshot`, `_build_pair`, `_identity_seed`, `_compare`, `_select`,
`_git_tree`, `_git`) and the two fixture shapes are frozen dataclasses (`ChainPair`, `SnapshotSpec`),
because a case's Given is a value, not an accumulator. Ten collected cases, no integration case —
which is why the integration lane is untouched by this leaf.

## Evidence

### Repo-Internal References

- `test_a_unique_chain_defaults_to_the_first_before_head_versus_the_last_after_head` supplies the current fixture or assertion described above. [16]
- `test_an_intermediate_revision_stays_selectable_history` supplies the current fixture or assertion described above. [17]
- `test_a_successor_cycle_is_unresolved_and_names_no_pair` supplies the current fixture or assertion described above. [18]
- `test_a_dangling_authored_edge_is_unresolved_and_names_the_missing_revision` supplies the current fixture or assertion described above. [19]
- `test_the_review_pane_renders_the_selected_head_pairs_own_statements` supplies the current fixture or assertion described above. [20]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [21]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [22]

- The new module's scope statement: heads from authored successors, the six load-bearing properties, and the fault-injection disclosure. [23]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [24]
- The fixed recorded statements every authored revision carries, so a head's text is assertable. [25]
- The adapter's own function under test, called exactly as `compose_review` calls it. [26]
- The two chain defaults with exact selected revision ids: `r1`-vs-`r3` and the advanced `r2`-vs-`r3`. [27]
- Selectable history: the default still compares the heads while `r2` is compared on demand through the per-side explicit selector with its own recorded text. [28]
- The two fork ambiguities: both heads listed, no pair, the statement naming the choice left to the reader. [29]
- The known-empty side: a removal under the R06 contract with the before head recorded and the after side absent. [30]
- The two lineage failures: a successor cycle and a dangling authored edge, each unresolved with no pair and the reason named. [31]
- Order-independence: the successor relation beats sorted position. [32]
- The pane case: the served payload records the compared head pair and renders the heads' own recorded statements as `present`. [33]
- The lane row, inserted mid-list in the alphabetical knowledge run. [34]

### Docs References

No Domain Documentation source is configured for this slice.

### Cross-Repo References

No cross-repository behavior is implemented in this file. Every case builds its snapshots and Git
trees under `tmp_path` and asserts one repository namespace's selection.

No meaningful cross-repo references found.
