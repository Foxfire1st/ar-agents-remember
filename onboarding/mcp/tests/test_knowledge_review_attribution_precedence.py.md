# mcp/tests/test_knowledge_review_attribution_precedence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_attribution_precedence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T23:41:23+02:00 |
| lastVerifiedCommitHash | `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4`|
| lastVerifiedCommitDate | 2026-09-29T00:17:28+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

**Attribution precedence across knowledge availability (`ICR-R04@v1`), measured over one real review
enclosure.** Six production-composition cases. `260921-ICR-L4` added them to
[`test_knowledge_review_source_endpoints.py`](test_knowledge_review_source_endpoints.py.md).
`260921-ICR-L57` moved them here verbatim when that module crossed the 1200-line rail; no case was
added, dropped or changed.

Every case builds the same real enclosure, linked Git worktree and capture through the sibling's
`build_endpoint_fixture`, and opens the review through the production resolution and composition. Only
the state of the knowledge halves changes around the one bound code-tree pair. The source inventory is
measured from that pair in every case, so the only thing that moves is which attribution conclusions
the review may state. Nothing injects a partition, a mapping or a payload.

The properties:

- **one unreadable half** (the baseline removed after the pair resolves) leaves a path the readable
  candidate registers attributed, and every other path *undetermined*, never confirmed unregistered;
- **an identified empty first generation** (`ICR-R05`'s empty dataset with its origin record) counts as
  completely inspected, so a path no valid mapping resolves is confirmed unregistered;
- **the same pair read completely** is the control: identical enclosure and capture, both halves
  readable, and the same path is confirmed unregistered;
- **a damaged half** (valid bytes, origin record disagreeing with them) cannot support a negative
  conclusion: the partition treats it as uninspected, and the subject route keeps its refusal;
- **an unreadable candidate receipt** is stated on the task-context route and refused on the subject
  route, on the same bytes, with no storage error escaping either;
- **a receipt that breaks after the preflight** is carried into the pane and the declared limitations,
  not only the partition's side entry. The race is produced by breaking the record at the composition's
  own second question.

## Code Commentary

### Logic

**The enclosure comes from the sibling module.** The module imports `LEAF_ID`, `EndpointFixture` and
`build_endpoint_fixture` from `test_knowledge_review_source_endpoints`, and `SUCCESSOR_PATH` /
`UNMAPPED_PATH` from `diff_scope_test_support`, so it adds no fixture and no catalog artifact.

**The knowledge states are built by their owners.** `_damaged_origin` writes an origin record whose
logical digest is not the dataset's, through `ICR-R05`'s own writer. That is the state a repeated
successful ingest can leave behind. `_identified_empty_first_generation` materializes the identified
empty before half with the shipped candidate-creation owner and origin writer, using the identity read
back from the created bytes. This keeps the case independent of the ingest CLI.

### Conventions

Marked `pytest.mark.evidence_unit`. Every case is function-scoped over `tmp_path` and states the
property it protects in its docstring.

### Invariants And Boundaries

- **Production composition only.** Each case drives `read_knowledge_review` and the real resolution;
  the one monkeypatch (the receipt race) wraps the shipped `review_task_context.candidate_receipt_refusal`.
  The first call answers normally; after that, the wrapper really rewrites the receipt on disk and then
  delegates to the genuine check, so the real guard fires.
- **Behaviour-preserving split.** The cases and their two helpers are byte-identical to the section they
  came from. The collected node names match the pre-split population; only the module name in the node
  id changed.
- **Catalog footprint.** The module reaches `diff_scope_test_support.py` and `read_scope_test_support.py`
  through its imports. It is declared on both artifacts' exact `consumers` rows beside its sibling, and
  registers no artifact of its own.

### Todos

None.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement (one enclosure, only the knowledge halves vary, nothing injected), and the import of the sibling's enclosure fixture. | "Attribution precedence across knowledge availability, over one real review enclosure."; "from test_knowledge_review_source_endpoints import LEAF_ID, EndpointFixture, build_endpoint_fixture" | mcp/tests/test_knowledge_review_attribution_precedence.py:1-41 |
| The sibling's enclosure fixture these cases build on. | `EndpointFixture`; `build_endpoint_fixture`; `LEAF_ID` | mcp/tests/test_knowledge_review_source_endpoints.py:113-197; mcp/tests/test_knowledge_review_source_endpoints.py:207-239; mcp/tests/test_knowledge_review_source_endpoints.py:93-93 |
| **The precedence cases: one unreadable half leaves the readable side attributed and the rest unknown; the same pair read completely confirms absence where the lost half could not; a damaged half cannot support a negative conclusion.** | `test_one_unreadable_knowledge_half_leaves_the_readable_side_attributed_and_the_rest_unknown`; `test_the_same_pair_read_completely_confirms_absence_where_the_lost_half_could_not`; `test_a_damaged_knowledge_half_cannot_support_a_negative_attribution_conclusion` | mcp/tests/test_knowledge_review_attribution_precedence.py:53-123; mcp/tests/test_knowledge_review_attribution_precedence.py:163-196; mcp/tests/test_knowledge_review_attribution_precedence.py:199-247 |
| **The empty-generation case: an identified empty first generation counts as completely inspected for absence.** | `test_an_identified_empty_first_generation_counts_as_completely_inspected_for_absence` | mcp/tests/test_knowledge_review_attribution_precedence.py:126-160 |
| **The receipt cases: an unreadable candidate receipt is stated on the task route and refused on the subject route; a receipt that breaks after the preflight is stated in the pane and the limits.** | `test_an_unreadable_candidate_receipt_is_stated_on_the_task_route_and_refused_on_the_subject_route`; `test_a_receipt_that_breaks_after_the_preflight_is_stated_in_the_pane_and_the_limits` | mcp/tests/test_knowledge_review_attribution_precedence.py:250-326; mcp/tests/test_knowledge_review_attribution_precedence.py:329-377 |
| The two knowledge states built by their owners' own writers. | `_damaged_origin`; `_identified_empty_first_generation` | mcp/tests/test_knowledge_review_attribution_precedence.py:380-402; mcp/tests/test_knowledge_review_attribution_precedence.py:405-450 |
| The unit-regression lane row, beside its sibling's. | "mcp/tests/test_knowledge_review_attribution_precedence.py" | mcp/tests/test-evidence-lanes.toml:127-127 |
| The two support artifacts whose exact `consumers` lists declare this module (at `:1449` and `:1505`). | "path = \"mcp/tests/diff_scope_test_support.py\""; "path = \"mcp/tests/read_scope_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:1425-1470; mcp/tests/evidence-lifecycle.toml:1473-1529 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every case runs in-process against a
temporary coordination root, its own repositories and its own datasets.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): created this one-to-one card for the six attribution-precedence and receipt cases. The worker moved them verbatim out of `test_knowledge_review_source_endpoints.py` (1515 → 1093 lines there; 450 lines and 6 cases here). The three case rows moved from `test_knowledge_review_source_endpoints.py.md`, where they were removed. Their ranges were re-derived to each case's own extent: the precedence and receipt rows had collapsed to single `def` lines, and the receipt row had one range for two cases. The case descriptions reuse the `260921-ICR-L4` curator's account and the cases' own docstrings. Verification metadata remains empty until closeout stamps the code commit.
