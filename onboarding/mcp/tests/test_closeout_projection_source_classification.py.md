# mcp/tests/test_closeout_projection_source_classification.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_projection_source_classification.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash | `e963a01c6804570d597e451eaa069eaba66bd3ec`|
| lastVerifiedCommitDate | 2026-09-18T04:45:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Proves that a closeout capacity refusal reaches the operator as an **invalid** source rather than
an unreadable one, and that the unreadable state survives in the other direction.

The measured defect: `closeout_queue_graph` refuses a sprint whose authored graph is past its
bound with `closeout-queue-master-capacity-exceeded`, and `closeout_projection._problem` decided
the reported state by testing the substring `cap-exceeded`. Both surviving capacity codes spell
the bound `capacity-exceeded`, so the classifier missed every one of them and a sprint that had
been read perfectly — and was simply too large for its bound — was reported to the operator as a
source that could not be read. The fix declares each capacity code once, beside the classification
it carries, in `closeout_queue_errors.py`; this module pins that the raiser's own declared code
reaches `invalid` and that the two states never collapse into each other.

## Code Commentary

### Logic

`_oversized_graph` (`:45-56`) builds one node past the master bound: `MAX_CLOSEOUT_MASTERS + 1`
well-formed `SprintExecutionNode` refs over `REPO`, `bulk-<index>/task.json`, and no edges. The
bound is a property of the sprint's own authored graph, which is the graph the projection hands to
the raiser.

- `test_a_graph_past_its_bound_refuses_by_its_own_declared_code` (`:59-86`) is the end-to-end half. It
  builds a real `QueueFixture`, rewrites the sprint document's `executionGraph` to the oversized graph
  through `read_task_doc`/`write_task_doc`, and drives the production `graph_context` with that
  `authored_graph`, `strict_registers=False` and no overrides. Admission is asserted to refuse rather
  than pass, and the refusal is then asserted on its own terms: `refused.status` equals
  `MASTER_CAPACITY_EXCEEDED`, and `_problem("task", SPRINT.key, refused.status, ...)` reports `invalid`.
  The second assertion is the point — the code the raiser published is the input to the classifier.
- `test_an_unreadable_source_and_the_ordinary_case_are_unchanged` (`:89-100`) is the both-directions
  case. `capture_projection_source` on the untouched fixture must be readable, carry no problems and
  classify `active`; and `contract-unreadable` / `atomic-series-contract-unreadable` must still report
  `unreadable`. A classifier that widened `invalid` until it swallowed the unreadable state fails here
  rather than passing quietly.
- `test_every_declared_capacity_code_classifies_as_invalid` (`:103-108`) closes the declaration loop: it
  asserts `MASTER_CAPACITY_EXCEEDED` is a member of `CAPACITY_REFUSAL_CODES` and that every code in the
  sorted set classifies `invalid`. A code added to the set without a classification, or a classification
  removed from the set, fails here.

### Conventions

The module imports `QueueFixture`, `REPO` and `SPRINT` from the sibling `test_closeout_queue`
fixture rather than rebuilding the world, so it exercises the same real task topology and
coordination root the other closeout boundary suites use. It drives production owners
(`graph_context`, `capture_projection_source`) and reads the classifier through its module-private
`_problem`, because the classification decision is the subject rather than a public surface.

The module is registered in the **integration** lane of `mcp/tests/test-evidence-lanes.toml`
(entry row `:137`) by the same change set that created it: it composes the real `QueueFixture`
over temporary Git repositories and drives the production graph admission and projection path, so
that is its behaviour-preserving lane. It is a declared exact consumer of
`mcp/tests/closeout_input_test_support.py` (consumer row `:307`) and
`mcp/tests/curator_coherence_test_support.py` (consumer row `:366`) in
`mcp/tests/evidence-lifecycle.toml`, both reached transitively through `test_closeout_queue`,
which imports `curator_coherence_test_support` and `test_worktree_support`, and the latter imports
`closeout_input_test_support`. Consumer declarations are ownership accounting only; they are not
execution or acceptance evidence.

### Invariants And Boundaries

- The refusal is asserted against the constant the raiser uses, not against a retyped literal, so a
  renamed code cannot leave this module green while the raiser and classifier disagree.
- Both directions are asserted in the same pass: a capacity refusal is `invalid` and a genuinely
  unreadable source is still `unreadable`, so the fix cannot be satisfied by collapsing the states.
- The ordinary readable case is asserted with no problems at all, so the module cannot pass on a
  fixture that already refuses for an unrelated reason.
- These are focused development cases over a disposable coordination root. They are behavior evidence
  for one classification, not full-suite certification or independent review, and this card records
  source inspection, not a test run.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this repository; the proving evidence is this
repository's own source and its own declared refusal codes.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required for this repository-owned classification proof. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One node past the master bound, every node a well-formed master reference. | `_oversized_graph` | mcp/tests/test_closeout_projection_source_classification.py:45-56 |
| The real raiser refuses the sprint's own authored graph, and its declared code classifies `invalid`. | `test_a_graph_past_its_bound_refuses_by_its_own_declared_code` | mcp/tests/test_closeout_projection_source_classification.py:59-86 |
| The ordinary source stays readable with no problems, and unreadable sources still report `unreadable`. | `test_an_unreadable_source_and_the_ordinary_case_are_unchanged` | mcp/tests/test_closeout_projection_source_classification.py:89-100 |
| Every declared capacity code classifies `invalid`. | `test_every_declared_capacity_code_classifies_as_invalid` | mcp/tests/test_closeout_projection_source_classification.py:103-108 |
| The classification the module pins: membership of the declared set, with the other vocabularies' markers untouched. | `_problem`; "error_type in CAPACITY_REFUSAL_CODES" | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:835-863 |
| The single declaration that owns the capacity codes and their classification. | `CAPACITY_REFUSAL_CODES`; `MASTER_CAPACITY_EXCEEDED` | mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py:34-34; mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py:38-40 |
| The raiser that publishes the code the first case reads back. | `MASTER_CAPACITY_EXCEEDED`; `EDGE_CAPACITY_EXCEEDED` | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:165-174 |
| The fixture this module composes instead of rebuilding the world. | `QueueFixture`; `REPO`; `SPRINT` | mcp/tests/test_closeout_queue.py:54-55; mcp/tests/test_closeout_queue.py:184-696 |
| The two artifact rows that declare this module as an exact consumer, both through `test_closeout_queue`. | "path = \"mcp/tests/closeout_input_test_support.py\""; "path = \"mcp/tests/curator_coherence_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:283-283; mcp/tests/evidence-lifecycle.toml:363-363; mcp/tests/evidence-lifecycle.toml:330-330 |
| The integration lane row the fail-closed manifest requires. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:177-177 |

## Cross-Repo References

Each case's `QueueFixture` builds the repositories it needs — a code repository and, where the fixture
declares one, an external memory repository — as real temporary Git repositories, which is what lets
the graph admission and projection path run at all. No production cross-repository authority is claimed
by this focused module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture's repositories are real temporary Git repositories created per case, not mocks. | `QueueFixture` | mcp/tests/test_closeout_queue.py:184-195 |

## Update History
- 2026-09-18T02:37:44+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:177-177. No content impact: mechanical anchor-range projection bound to citation source snapshot d211cfd02f11c0600198b11c621aa5574ac8743db6e0ca1d2c92936e561c5146; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:175-175. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T07:33:51+00:00: Generated citation repair: `QueueFixture`; `REPO`; `SPRINT` repointed to mcp/tests/test_closeout_queue.py:184-696; mcp/tests/test_closeout_queue.py:54-54; mcp/tests/test_closeout_queue.py:55-55. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:171-171. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `QueueFixture` repointed to mcp/tests/test_closeout_queue.py:184-696. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `REPO` in the row 112 of this card from mcp/tests/test_closeout_queue.py:184-195 to mcp/tests/test_closeout_queue.py:54-58, the extent of the construct the claim is about (the checker named line(s) [54, 55, 56] as its live location); added mcp/tests/test_closeout_queue.py:55 to the row 112 of this card as the citation for `SPRINT`: no cited file carried the construct, and the checker named line(s) [55, 284, 442] in this file as its live location
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/tests/test_closeout_queue.py:184-195 in the row 112 of this card; the repetition added no pooled evidence
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (flag resolved): the code worktree is frozen, so
  the earlier flag is now measured rather than conditional. `mcp/tests/evidence-lifecycle.toml`
  carries the inserted `checkpoint_landing_test_support.py` artifact block at `:342-361`, which
  leaves `path = "mcp/tests/curator_coherence_test_support.py"` at `:363` — the position this row
  already cites — and `path = "mcp/tests/closeout_input_test_support.py"` at `:283`. The pair
  `283-283` / `363-363` is confirmed against the frozen tree, and the flag above stands as the
  record of the interim state it described. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): this row cites the
  curator-coherence artifact path at `mcp/tests/evidence-lifecycle.toml:363`, which is its position
  in the current working tree, where the in-flight `checkpoint_landing_test_support.py` artifact
  block sits above it. The committed HEAD still carries that path at `:343`; the two forms differ
  only by that uncommitted insertion, so the citation is correct for the tree this leaf is being
  curated against and must be re-measured if the insertion does not land. Flagged rather than
  silently chosen; verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 3 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T14:20+02:00 — 260913-LCA-L7 curator (uncommitted change set on `ar/260913-lca-l7`):
  created this one-to-one sidecar for the leaf's new integration module. Recorded the measured defect
  it pins (a capacity code spelling `capacity-exceeded` never matched the `cap-exceeded` substring the
  classifier tested, so a sprint past its graph bound was reported unreadable), the case-by-case proof
  shape — one node past the master bound refused by its own declared code and classified `invalid`, the
  ordinary source readable with no problems while unreadable codes still report `unreadable`, and every
  declared capacity code classified `invalid` — and the two ownership facts the registration carries:
  the **integration** lane row at `mcp/tests/test-evidence-lanes.toml:137`, and the exact-consumer
  entries in `mcp/tests/evidence-lifecycle.toml` at `:307` and `:366`, both reached transitively
  through `test_closeout_queue`. Verification metadata is intentionally blank: the candidate is
  uncommitted, no commit contains this file yet, and closeout owns the stamp; no execution or
  acceptance claim.
