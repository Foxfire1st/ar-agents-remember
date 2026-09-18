# mcp/tests/test_knowledge_family_composition_boundaries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_family_composition_boundaries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:33+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

The composition leaf's **boundary suite**: eight cases that measure the leaf's own claims against the
thing the leaf must not move. Every case protects a clause of `KS-R17@v1` §7 and §8, and the
load-bearing ones are boundary cases rather than traversals:

- **The retrieval read is untouched.** The composition table is not consulted for selection, and the
  cases measure that **twice** — by value (the same dataset and seed produce the same selected items,
  counts, revision groups, advertised frontier and manifest digest with composition edges present and
  absent), and by the call-site derivation the packet's own Open Truth Gap asks for.
- **The traversal is a different operation.** Following declared edges under a policy version builds a
  scope and reports the version it executed under; it never changes what `read_knowledge_scope`
  selects, and it refuses rather than truncating.
- **The projection reports stored facts.** A missing link, route or context is reported absent, and
  nothing is reconstructed from a label, a path, a member or the joint guarantee.
- **The escalation is recorded and not activated.** The R07 proposal exists as a named artifact with
  its subject and effect scope, so the edge cannot be forgotten and cannot be read as a retirement.

The preservation comparisons are **by value and by digest, never by inspection**: the shipped read's
own output model and the sealed family-revision `payload_digest` are the things compared.

## Code Commentary

### Logic

- `test_a_composition_graph_leaves_the_shipped_selection_exactly_as_it_was` — copies the real fixture
  dataset, adds two composition edges, and compares every preserved field by value across two seeds,
  with table counts confirming the edges are the only difference.
- `test_no_shipped_read_path_consults_the_composition_table` — the derivation half: `READ_PATH_SOURCES`
  names the read-path modules, and the case asserts the selection statements carry no composition
  table reference and that `family_view.py` never imports the traversal. The set is stated in one
  place so a later leaf that adds a read path has one place to extend.
- The **traversal cases** assert that a traversal reports the policy identity and version it executed
  under and widens nothing else; that an unknown, a malformed and a not-permitted policy are each
  refused **by name**; and that a traversal which would exceed its declared bound is **refused, not
  truncated**.
- `test_every_pre_existing_family_revision_keeps_its_payload_digest` — the seal is unchanged: the
  payload version constant and every pre-existing revision's `payload_digest` are asserted after the
  new tables exist.
- `test_the_r07_escalation_proposal_is_recorded_with_its_subject_and_effect_scope` — the escalation
  artifact must exist and state its subject, so an accidentally deleted escalation fails the suite.
- `test_the_application_seam_is_read_only_carries_the_operation_and_moves_no_selection` — the one
  case that drives the read-only seam end to end: the projection reports the recorded link with its
  policy version, the traversal carries `follow_family_composition` as its own operation, a refused
  traversal leaves the file **byte-identical**, and a family revision this namespace does not hold is
  a typed refusal rather than an empty report. The projection's absent-state assertions are driven
  here too, inside this case, rather than by separate cases of their own.

### Conventions

- Hermetic where it can be, integration where it must be: the selection-preservation case uses the
  registered read-scope fixture, and the boundary cases compare **digests and bytes** rather than
  describing behaviour.
- **Always run with `-o "filterwarnings=ignore"` on this host** — a pre-existing host condition, not
  this leaf's.
- The suite is a **consumer** of `knowledge-read-scope-cases`, `knowledge-facet-cases` and
  `knowledge-generation-cases`; it registers **no** new contract and **no** new artifact, so the
  catalogue's counts stay at **13 contracts / 54 artifacts**.

### Invariants And Boundaries

- **The escalation is recorded, not activated.** The case asserts the artifact's existence and its
  required content; it does not assert that the shipped read changed, because it must not.
- **Nothing here is a retirement.** No case deletes, skips, deselects or weakens a shipped assertion.
- **Boundary.** The write shape and the generation are the sibling module's; this one owns the
  boundary between the composed graph and the retrieval selection.

### Todos

None recorded. The R07 escalation awaits a developer ruling; nothing about the shipped read changes
until then.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The case that compares the shipped selection by value with composition edges present and absent, over two seeds.** | "test_a_composition_graph_leaves_the_shipped_selection_exactly_as_it_was" | mcp/tests/test_knowledge_family_composition_boundaries.py:219-219 |
| **The call-site derivation, stated as one extendable set so a later leaf that adds a read path has one place to extend.** | `READ_PATH_SOURCES` | mcp/tests/test_knowledge_family_composition_boundaries.py:84-84 |
| **The case that proves no shipped read path consults the composition table.** | "test_no_shipped_read_path_consults_the_composition_table" | mcp/tests/test_knowledge_family_composition_boundaries.py:252-252 |
| **The case that proves a traversal reports its declared version and widens nothing else.** | "test_a_traversal_under_a_declared_policy_reports_its_version_and_widens_nothing_else" | mcp/tests/test_knowledge_family_composition_boundaries.py:288-288 |
| **The case that proves an unknown, a malformed and a not-permitted policy are each refused by name.** | "test_an_unknown_a_malformed_and_a_not_permitted_policy_are_each_refused_by_name" | mcp/tests/test_knowledge_family_composition_boundaries.py:335-335 |
| **The case that proves a traversal past its declared bound is refused rather than truncated.** | "test_a_traversal_that_would_exceed_its_declared_bound_is_refused_not_truncated" | mcp/tests/test_knowledge_family_composition_boundaries.py:429-429 |
| **The case that asserts every pre-existing family revision keeps its sealed `payload_digest`.** | "test_every_pre_existing_family_revision_keeps_its_payload_digest" | mcp/tests/test_knowledge_family_composition_boundaries.py:496-496 |
| **The case that asserts the escalation artifact exists and states its subject and effect scope.** | "test_the_r07_escalation_proposal_is_recorded_with_its_subject_and_effect_scope" | mcp/tests/test_knowledge_family_composition_boundaries.py:589-589 |
| **The end-to-end seam case: the recorded link is reported, the refusal leaves the file byte-identical, and a missing revision is refused rather than reported empty.** | "test_the_application_seam_is_read_only_carries_the_operation_and_moves_no_selection" | mcp/tests/test_knowledge_family_composition_boundaries.py:615-615 |
| The contract whose consumer list this module joined for its read-scope fixture. | "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1412-1412 |
| The lane row this module is registered under. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1412-1412. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1408-1408. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1407-1407. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1403-1403. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_an_unknown_a_malformed_and_a_not_permitted_policy_are_each_refused_by_name" repointed to mcp/tests/test_knowledge_family_composition_boundaries.py:335-335. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_a_traversal_that_would_exceed_its_declared_bound_is_refused_not_truncated" repointed to mcp/tests/test_knowledge_family_composition_boundaries.py:429-429. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_every_pre_existing_family_revision_keeps_its_payload_digest" repointed to mcp/tests/test_knowledge_family_composition_boundaries.py:496-496. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_r07_escalation_proposal_is_recorded_with_its_subject_and_effect_scope" repointed to mcp/tests/test_knowledge_family_composition_boundaries.py:589-589. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_application_seam_is_read_only_carries_the_operation_and_moves_no_selection" repointed to mcp/tests/test_knowledge_family_composition_boundaries.py:615-615. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1402-1402. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1310-1310. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:06:32+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1307-1307. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:33+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): created this one-to-one card for the composition leaf's boundary module. It records the four boundary claims and, in particular, the two halves of the axis separation (compared **by value** and derived **by call site**), that an exceeded bound is refused rather than truncated, that a missing family revision is refused rather than reported empty, and that the escalation is recorded but **not activated**. This seat re-read the module against the candidate and recorded that the projection's own absent-state assertions are driven inside the end-to-end seam case rather than by separate cases of their own. The card records the three evidence-contract consumer entries with **no** new fixture, contract or artifact, so counts stay 13 / 54. Verification metadata is the leaf's base commit `e963a01c`: the code commit does not exist yet and closeout owns that stamp.
