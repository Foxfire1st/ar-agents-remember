# mcp/tests/test_knowledge_review_revision_selection.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The explicit revision comparison's case module: **heads from authored successors, never from order
or presence.** Ten cases drive the **real** two-snapshot comparison over **real** snapshot pairs
built through the public store operations, then run the exact head-selection function the review
adapter calls. Nothing here re-implements a read, a comparison or a predecessor lookup, fakes a
snapshot, or asserts a rendering it did not read back — except the two fault-injection cases, which
say so in their own docstrings: a corrupt snapshot cannot be authored through the validating write
path, so the corruption is inserted as SQL into a scratch copy and the case asserts the read path
refuses to select from it.

The module docstring names the load-bearing properties, **one case each**:

- a unique multi-step chain defaults to the first before head versus the last after head (before
  `r1` and after `r1 → r2 → r3` is `r1` versus `r3`; an advanced before head `r2` moves the default
  to `r2` versus `r3`), with the exact selected revision ids recorded;
- an intermediate revision stays selectable history through the comparison's own per-side explicit
  revision selector;
- a fork on either side is an explicit ambiguity naming every head — never an arbitrary winner;
- a known-empty side stays a one-sided addition or removal with the nonempty side's head recorded,
  which is `ICR-R06@v1`'s contract reused rather than restated;
- a successor cycle and a dangling authored edge are unresolved selections with no pair recorded —
  no timestamp, no similarity and no collection order fabricates a newest version;
- the review pane renders the selected head pair's own recorded statements.

The fixture builds each pair through the shipped candidate write path (`_build_pair` over
`_build_snapshot`): real Git trees for the source half, real snapshot databases for the knowledge
half, opened through `open_diff_side` under one namespace — so a chain, a fork, a cycle and a
dangling edge are real differences between two real snapshots rather than edits of one dataset. The
final case drives the whole surface (`compose_review` over two real Git trees) and asserts the pane
renders the head pair's own recorded texts.

## Code Commentary

### Logic

**The pair builder is the whole Given, and it authors through the validating write path.**
`_build_snapshot` writes `before_count`/`after_count` revisions of one invariant with fixed recorded
statements (`STATEMENTS`), chaining each revision's predecessor to the previous one — or, with
`fork=True`, branching every later revision off the first — and `_build_pair` places a before
snapshot and an after snapshot sharing the same revision-id lineage under one repository id. The
cycle and dangling cases cannot be authored that way (the write path validates), so they fault-inject
as SQL into a scratch copy and assert the refusal — each docstring says so, so no reader mistakes an
injected corruption for an authored history.

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

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own scope statement,
its lane declaration, the fixture that authors real snapshot pairs, the ten cases, and the lane row
that selects them.

- The new module's scope statement: heads from authored successors, the six load-bearing properties, and the fault-injection disclosure. [1]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [2]
- The fixed recorded statements every authored revision carries, so a head's text is assertable. [3]
- The fixture that makes a chain, a fork and a history real: two independently built snapshots under one namespace through the public write path. [4]
- The adapter's own function under test, called exactly as `compose_review` calls it. [5]
- The two chain defaults with exact selected revision ids: `r1`-vs-`r3` and the advanced `r2`-vs-`r3`. [6]
- Selectable history: the default still compares the heads while `r2` is compared on demand through the per-side explicit selector with its own recorded text. [7]
- The two fork ambiguities: both heads listed, no pair, the statement naming the choice left to the reader. [8]
- The known-empty side: a removal under the R06 contract with the before head recorded and the after side absent. [9]
- The two lineage failures: a successor cycle and a dangling authored edge, each unresolved with no pair and the reason named. [10]
- Order-independence: the successor relation beats sorted position. [11]
- The pane case: the served payload records the compared head pair and renders the heads' own recorded statements as `present`. [12]
- The lane row, inserted mid-list in the alphabetical knowledge run. [13]
- The policy the cases measure. [14]
- The value the cases assert. [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file. Every case builds its snapshots and Git
trees under `tmp_path` and asserts one repository namespace's selection.

No meaningful cross-repo references found.
