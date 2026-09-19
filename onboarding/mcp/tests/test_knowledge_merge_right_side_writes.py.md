# mcp/tests/test_knowledge_merge_right_side_writes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_merge_right_side_writes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T19:09+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The lane that pins **what the merge does with the right side's own writes: replay them, then judge
the result.** `merge_knowledge_datasets` replays one side's whole base-to-side delta onto a copy of
the other side, so the *right* side is the one whose operations travel as a changeset and the one
whose in-place edits are the merge's own work rather than a copied file. Two properties of that
replay are protected here, and neither had a case before this leaf:

- **A right-side `UPDATE` is an operation whose key lives on its old side.** SQLite reports only the
  columns an operation changes, so an update's *new* entries carry the not-supplied marker exactly
  where the primary key is. A postcondition check that read the key from that side looked for a row
  named `repository_id=<not-supplied>/invariant_id=<not-supplied>`, did not find it, and refused
  **every** update with `changeset_postcondition_failed` — so a side that edited an existing record
  in place could not be merged at all, whatever it edited. The fix is
  `MaterializedChange.primary_key` (`mcp/src/agents_remember/memory/knowledge/merge_changeset.py:96-114`),
  documented in its own docstring as *"read from the side that carries them"*: the old side is read
  first whenever it is present, which resolves a `DELETE` (old side only), an `UPDATE` (both sides,
  and only the old holds the key) and an `INSERT` (no old side).
- **A replayed `route.parent_route_id` change is judged by the acyclicity rule, in the same
  transaction.** `route` is inside the merge's attached table set and a reparent is a real operation,
  so the merge is a production path that writes route hierarchies.
  `require_acyclic_routes` (`mcp/src/agents_remember/memory/knowledge/routes.py:94-155`) runs on the
  connection the delta was applied on, after the rows are written and before that application
  commits, so a candidate whose hierarchy reaches itself is rolled back rather than published.

## Code Commentary

### Logic

**The cases drive the public merge entry point** — `resolve_knowledge_merge_base` and
`merge_resolved_knowledge_datasets` from `application/knowledge_merge.py` — **over the shared
three-dataset case** built by `merge_case_test_support.build_case`, so what they measure is the
operation a caller invokes rather than a helper beside it. `resolved_base` (`:117-135`) asserts the
resolution is not a `KnowledgeRefusal` before returning it, and `merge` (`:138-151`) optionally
publishes the candidate through `SnapshotDestinationRequest`, so one case can read a published file
back while the next can assert that no destination was created at all.

The module authors its own route hierarchy into the case's **base** state before the sides are
derived, which is why a side has a hierarchy to reparent instead of a table whose only rows arrive
with the side being judged. The three route ids are module constants (`ROOT_ROUTE_ID`,
`MID_ROUTE_ID`, `LEAF_ROUTE_ID`, `:53-55`) and the two shapers are one statement each:
`reparent_the_leaf_under_the_root` (`:95-103`) moves the leaf onto the root, and
`reparent_the_root_under_the_leaf` (`:106-114`) closes a three-node cycle. Both go through `_run`
(`:60-68`), which opens its own `apsw` connection with `PRAGMA foreign_keys=ON` and closes it in a
`finally`, so a failed case cannot leave a connection behind.

The three cases:

- **`test_a_right_side_update_is_replayed_and_the_published_candidate_carries_it`** (`:183-215`) —
  the smallest right-side `UPDATE` a merge can be asked to replay: one stored invariant's label
  changes and nothing else. The case **publishes the candidate and reads the label back out of the
  published file** through `labels_of`, so the evidence is the merged dataset rather than the outcome
  the merge reported about it; `dataset_identity(destination).logical_digest` is then compared with
  `outcome.merged_identity.logical_digest`. Reading the key from the update's new side reddens it;
  checking the changed column without the key would not, which is why the label is read back rather
  than inferred from the state.
- **`test_a_replayed_reparent_moves_the_row_it_names_and_no_other`** (`:218-241`) — three assertions
  on the published candidate (`parent_of(destination, LEAF_ROUTE_ID) == ROOT_ROUTE_ID`,
  `MID_ROUTE_ID`'s parent unchanged, the root's parent `None`) plus `route_count(destination) ==
  route_count(case.state_path("left"))`. The two sibling assertions separate *"the right row moved"*
  from *"something moved"*.
- **`test_a_replayed_route_reparent_that_closes_a_cycle_refuses_the_whole_merge`** (`:244-285`) — the
  acyclicity rule over the rows the delta just wrote, inside that application. It asserts
  `outcome.state == "refused"`, `merged_identity is None`, `not destination.exists()`, and a refusal
  carrying `code == "lineage_cycle"`, `operation == MERGE_OPERATION`, `table == "route"` and both
  route ids in `observed`; then that the three inputs keep their exact `dataset_identity` digests.
  Removing the walk from the merge reddens it, and running the walk on the *inputs* instead of the
  result reddens it too — neither input is cyclic, and only the replayed rows make the candidate so.

### Conventions

`pytestmark = pytest.mark.evidence_unit` (`:49`) declares the module's retained delivery-evidence
category, and its single lane row was **appended** to the end of `unit-regression` in
`mcp/tests/test-evidence-lanes.toml:193`. The module imports the shared case support as itself —
`MergeCase`, `build_case`, `labels_of`, `set_label` from `merge_case_test_support` — because
`merge_case_test_support.py` declares `consumer_scope = "exact"` in
`mcp/tests/evidence-lifecycle.toml`, so this module is a registered consumer of it; that registration
is a precondition, and an unregistered exact-scope consumer is a hard collection error. Read-only
inspection of a dataset always goes through `open_read_only_database` and a `finally` close, so no
case can leave a writer open on a fixture another case will read.

### Invariants And Boundaries

- **A key is read from the side that carries it**, never from the side the operation wrote: the
  `primary_key` docstring is the rule's own statement, and the case that reads the published label
  back is what makes a regression visible.
- **The cycle walk runs on the merged result, inside the same transaction.** A walk over the inputs
  cannot see the cycle the replay created, and a walk after commit would publish the candidate first.
- **A refusal publishes nothing.** `not destination.exists()` and the three unchanged input digests
  are asserted together, so "refused" cannot be true while a partial candidate survives.
- **The shared case's fixture chain owns the three datasets.** No case builds a parser, a schema or a
  snapshot of its own; `merge_case_test_support` is the one producer.
- **Boundary.** This is a test module. It owns no production contract and adds no support module.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the two replayed-write properties it protects. | "What the merge does with the right side's own writes: replay them, then judge the result." | mcp/tests/test_knowledge_merge_right_side_writes.py:1-22 |
| The lane marker, which declares this module's retained evidence category. | "pytestmark = pytest.mark.evidence_unit" | mcp/tests/test_knowledge_merge_right_side_writes.py:49-49 |
| **The key rule: read from the side that carries it, old side first, which is what makes a right-side `UPDATE` mergeable.** | `MaterializedChange`; `primary_key` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:75-122; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:96-114 |
| **The acyclicity rule the replayed reparent is judged by, inside the merge's own transaction.** | `require_acyclic_routes` | mcp/src/agents_remember/memory/knowledge/routes.py:94-155 |
| The public merge entry points the cases actually invoke. | `resolve_knowledge_merge_base`; `merge_resolved_knowledge_datasets` | mcp/src/agents_remember/application/knowledge_merge.py:36-52; mcp/src/agents_remember/application/knowledge_merge.py:55-64 |
| The shared three-dataset case and the helpers that shape and read it. | `MergeCase`; `build_case`; `labels_of`; `set_label` | mcp/tests/merge_case_test_support.py:82-132; mcp/tests/merge_case_test_support.py:511-571; mcp/tests/merge_case_test_support.py:635-644; mcp/tests/merge_case_test_support.py:309-314 |
| The route ids and the one-statement shapers that author and reparent the hierarchy. | `author_routes`; `reparent_the_leaf_under_the_root`; `reparent_the_root_under_the_leaf` | mcp/tests/test_knowledge_merge_right_side_writes.py:71-92; mcp/tests/test_knowledge_merge_right_side_writes.py:95-103; mcp/tests/test_knowledge_merge_right_side_writes.py:106-114 |
| The base resolution and the optional publication every case goes through. | `resolved_base`; `merge` | mcp/tests/test_knowledge_merge_right_side_writes.py:117-135; mcp/tests/test_knowledge_merge_right_side_writes.py:138-151 |
| **The published-candidate case: the right side's own label is read back out of the merged file.** | `test_a_right_side_update_is_replayed_and_the_published_candidate_carries_it` | mcp/tests/test_knowledge_merge_right_side_writes.py:183-215 |
| **The reparent case, with the two sibling assertions that separate "the right row moved" from "something moved".** | `test_a_replayed_reparent_moves_the_row_it_names_and_no_other` | mcp/tests/test_knowledge_merge_right_side_writes.py:218-241 |
| **The cycle case: `lineage_cycle` attributed to the merge, nothing published, the three inputs byte-identical.** | `test_a_replayed_route_reparent_that_closes_a_cycle_refuses_the_whole_merge` | mcp/tests/test_knowledge_merge_right_side_writes.py:244-285 |
| The lane row this module was appended to. | "mcp/tests/test_knowledge_merge_right_side_writes.py" | mcp/tests/test-evidence-lanes.toml:193-193 |
| The exact-scope consumer registration this module obliged, inside `merge_case_test_support.py`'s own `consumers` list. | "mcp/tests/test_knowledge_merge_right_side_writes.py" | mcp/tests/evidence-lifecycle.toml:1269-1288 |

## Cross-Repo References

No cross-repository behavior is implemented or measured in this file. Every case builds its three
datasets under `tmp_path` and asserts one repository's own merge.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T20:45:09+02:00 — 260915-KS-L23 post-closeout clearance (change set on `ar/260915-ks-l23`, memory base `ce3028e9`, code `5e4eb651`): **cleared the 1 enforced `citation_anchor_absent_from_range` row in this document.** The closeout's own code commit appended one `consumers` registration above every construct these cards cite, so each cited range ended exactly one line above the line that now carries the anchor row. Widened to the carrying line: `mcp/tests/evidence-lifecycle.toml:1269-1287` → `mcp/tests/evidence-lifecycle.toml:1269-1288` (row 141). Every line the author cited stays inside its range; no claim, Anchor cell or other range was dropped or re-worded, and each named anchor now resolves inside the widened range.
- 2026-09-18T19:09+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): created this one-to-one card for the right-side-writes lane. It records the two properties the module protects, the mechanism each one turns on (`UPDATE` keys living on the old side; the acyclicity walk running on the replayed rows inside the application that wrote them), the fact that every case drives the **public** merge entry point over the shared three-dataset case rather than a helper beside it, and the reason the sibling assertions exist (separating "the right row moved" from "something moved"). It also records the module's `evidence_unit` mark and its exact-scope consumer registration in `evidence-lifecycle.toml`, which is a precondition rather than metadata. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate. The `reviewedWorkingCandidate` row states what was read, and closeout owns the stamp.
