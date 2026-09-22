# mcp/tests/test_knowledge_review_revision_selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_revision_selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T10:40:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l7`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5` |
| lastVerifiedCommitHash | `f33f58eab87bd4db0eb944999d01808821ef9c3a` |
| lastVerifiedCommitDate | 2026-09-22T11:27:22+02:00|
| governingOverview | `mcp/tests/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own scope statement,
its lane declaration, the fixture that authors real snapshot pairs, the ten cases, and the lane row
that selects them.

| Finding | Anchor | Source |
| --- | --- | --- |
| The new module's scope statement: heads from authored successors, the six load-bearing properties, and the fault-injection disclosure. | `select_subject_revisions`; `revision_heads` | mcp/tests/test_knowledge_review_revision_selection.py:1-29; mcp/tests/test_knowledge_review_revision_selection.py:42-45 |
| The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. | `pytestmark` | mcp/tests/test_knowledge_review_revision_selection.py:66-66 |
| The fixed recorded statements every authored revision carries, so a head's text is assertable. | `STATEMENTS` | mcp/tests/test_knowledge_review_revision_selection.py:68-73 |
| The fixture that makes a chain, a fork and a history real: two independently built snapshots under one namespace through the public write path. | `_build_snapshot`; `_build_pair`; `ChainPair`; `SnapshotSpec` | mcp/tests/test_knowledge_review_revision_selection.py:109-157; mcp/tests/test_knowledge_review_revision_selection.py:158-218; mcp/tests/test_knowledge_review_revision_selection.py:89-99; mcp/tests/test_knowledge_review_revision_selection.py:101-107 |
| The adapter's own function under test, called exactly as `compose_review` calls it. | `_select`; `_compare`; `_identity_seed` | mcp/tests/test_knowledge_review_revision_selection.py:244-256; mcp/tests/test_knowledge_review_revision_selection.py:223-241; mcp/tests/test_knowledge_review_revision_selection.py:219-221 |
| The two chain defaults with exact selected revision ids: `r1`-vs-`r3` and the advanced `r2`-vs-`r3`. | `test_a_unique_chain_defaults_to_the_first_before_head_versus_the_last_after_head`; `test_an_advanced_before_head_moves_the_default_pair` | mcp/tests/test_knowledge_review_revision_selection.py:259-280; mcp/tests/test_knowledge_review_revision_selection.py:282-290 |
| Selectable history: the default still compares the heads while `r2` is compared on demand through the per-side explicit selector with its own recorded text. | `test_an_intermediate_revision_stays_selectable_history` | mcp/tests/test_knowledge_review_revision_selection.py:293-330 |
| The two fork ambiguities: both heads listed, no pair, the statement naming the choice left to the reader. | `test_a_fork_on_the_after_side_is_an_explicit_ambiguity`; `test_a_fork_on_the_before_side_is_an_explicit_ambiguity` | mcp/tests/test_knowledge_review_revision_selection.py:333-345; mcp/tests/test_knowledge_review_revision_selection.py:348-359 |
| The known-empty side: a removal under the R06 contract with the before head recorded and the after side absent. | `test_a_known_empty_after_side_stays_a_removal_with_the_before_head_recorded` | mcp/tests/test_knowledge_review_revision_selection.py:361-414 |
| The two lineage failures: a successor cycle and a dangling authored edge, each unresolved with no pair and the reason named. | `test_a_successor_cycle_is_unresolved_and_names_no_pair`; `test_a_dangling_authored_edge_is_unresolved_and_names_the_missing_revision` | mcp/tests/test_knowledge_review_revision_selection.py:416-467; mcp/tests/test_knowledge_review_revision_selection.py:469-522 |
| Order-independence: the successor relation beats sorted position. | `test_heads_come_from_successors_not_from_sorted_order` | mcp/tests/test_knowledge_review_revision_selection.py:524-536 |
| The pane case: the served payload records the compared head pair and renders the heads' own recorded statements as `present`. | `test_the_review_pane_renders_the_selected_head_pairs_own_statements` | mcp/tests/test_knowledge_review_revision_selection.py:571-615 |
| The lane row, inserted mid-list in the alphabetical knowledge run. | "mcp/tests/test_knowledge_review_revision_selection.py" | mcp/tests/test-evidence-lanes.toml:111-111 |
| The policy the cases measure. | `select_subject_revisions` | mcp/src/agents_remember/application/review_revision_comparison.py:144-187 |
| The value the cases assert. | `ReviewRevisionSelection` | mcp/src/agents_remember/models/knowledge/revision_selection.py:54-74 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every case builds its snapshots and Git
trees under `tmp_path` and asserts one repository namespace's selection.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-22T10:40:00+02:00 — 260921-ICR-L7 curator (uncommitted change set on `ar/260921-icr-l7`, base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **created.** The module is new in this leaf (615 lines, 10 cases) and this is its one-to-one card. It records the six load-bearing properties the module docstring names, the real-snapshot fixture (plus the two disclosed SQL fault-injection cases), the adapter's-own-function convention (`_select` calls what `compose_review` calls), and the pane case that closes the loop through the served payload. Every range was measured against the candidate module. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the leaf's base — the last real commit the reading was taken against — because every construct this card cites exists only in this leaf's uncommitted candidate and no commit contains the bytes a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read; closeout owns the stamp once the code commit exists.
