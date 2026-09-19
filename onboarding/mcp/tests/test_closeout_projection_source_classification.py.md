# mcp/tests/test_closeout_projection_source_classification.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| lastUpdated | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c` |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| path | `mcp/tests/test_closeout_projection_source_classification.py` |
| doc_type | `file-level-onboarding` |
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
| The fixture this module composes instead of rebuilding the world. | `QueueFixture`; `REPO`; `SPRINT` | mcp/tests/test_closeout_queue.py:54-55; mcp/tests/test_closeout_queue.py:184-694 |
| The two artifact rows that declare this module as an exact consumer, both through `test_closeout_queue`. | "path = \"mcp/tests/closeout_input_test_support.py\""; "path = \"mcp/tests/curator_coherence_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:338-338; mcp/tests/evidence-lifecycle.toml:385-385; mcp/tests/evidence-lifecycle.toml:410-410 |
| The integration lane row the fail-closed manifest requires. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:224-224 |

## Cross-Repo References

Each case's `QueueFixture` builds the repositories it needs — a code repository and, where the fixture
declares one, an external memory repository — as real temporary Git repositories, which is what lets
the graph admission and projection path run at all. No production cross-repository authority is claimed
by this focused module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture's repositories are real temporary Git repositories created per case, not mocks. | `QueueFixture` | mcp/tests/test_closeout_queue.py:184-195 |
| The fixture's repositories are real temporary Git repositories created per case, not mocks. | `QueueFixture` | mcp/tests/test_closeout_queue.py:184-694 |

## Update History
- 2026-09-18T19:53:17+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document** (one table row, two anchors). The artifact row cited `337-337` (the `[[artifact]]` header) for `"path = \"mcp/tests/closeout_input_test_support.py\""` and `384-384` (the next header) for `"path = \"mcp/tests/curator_coherence_test_support.py\""`; each `path = …` line sits one line below its header, so both ranges were widened by one line (`337-338`, `384-385`). The claim, the anchors and the consumer-list ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:219-219. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:219-219. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:214-214. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:214-214. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:173-173. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:212-212. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:212-212. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:188-188. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:186-186. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 8 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_closeout_projection_source_classification.py`, `QueueFixture`, `REPO`, `SPRINT`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 5 generated projection bullet(s) by hand** — `mcp/tests/test_closeout_projection_source_classification.py`, `QueueFixture`, `REPO`, `SPRINT`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_closeout_projection_source_classification.py"` → `mcp/tests/test-evidence-lanes.toml:179-179`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.
- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/test-evidence-lanes.toml:177-177` -> `mcp/tests/test-evidence-lanes.toml:178-178`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `QueueFixture` repointed to mcp/tests/test_closeout_queue.py:184-694. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:172-172. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/tests/test_closeout_queue.py:184-195 in the row 112 of this card; the repetition added no pooled evidence
- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `REPO` in the row 112 of this card from mcp/tests/test_closeout_queue.py:184-195 to mcp/tests/test_closeout_queue.py:54-58, the extent of the construct the claim is about (the checker named line(s) [54, 55, 56] as its live location); added mcp/tests/test_closeout_queue.py:55 to the row 112 of this card as the citation for `SPRINT`: no cited file carried the construct, and the checker named line(s) [55, 284, 442] in this file as its live location
- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 3 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (drift re-verification): this row cites the
  curator-coherence artifact path at `mcp/tests/evidence-lifecycle.toml:363`, which is its position
  in the current working tree, where the in-flight `checkpoint_landing_test_support.py` artifact
  block sits above it. The committed HEAD still carries that path at `:343`; the two forms differ
  only by that uncommitted insertion, so the citation is correct for the tree this leaf is being
  curated against and must be re-measured if the insertion does not land. Flagged rather than
  silently chosen; verification metadata remains closeout-owned.
- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (flag resolved): the code worktree is frozen, so
  the earlier flag is now measured rather than conditional. `mcp/tests/evidence-lifecycle.toml`
  carries the inserted `checkpoint_landing_test_support.py` artifact block at `:342-361`, which
  leaves `path = "mcp/tests/curator_coherence_test_support.py"` at `:363` — the position this row
  already cites — and `path = "mcp/tests/closeout_input_test_support.py"` at `:283`. The pair
  `283-283` / `363-363` is confirmed against the frozen tree, and the flag above stands as the
  record of the interim state it described. Verification metadata remains closeout-owned.
- 2026-09-14T12:20:00+00:00 — 260913-LCA-L7 curator (uncommitted change set on `ar/260913-lca-l7`):
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
