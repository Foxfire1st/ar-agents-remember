# mcp/tests/merge_case_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/merge_case_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80` |
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

**The case harness for guarded common-base merge cases**, registered as the `shared-support` owned artifact of `contract:common-base-merge-cases`. Every merge case needs the same three things, and this module owns them so no case re-derives them:

- **Authored datasets.** Each state is written through the real store operation — schema created by the store, rows inserted by the store's own create operations with real provenance envelopes — and then closed through a SQLite backup, so a case measures datasets the package itself produced rather than hand-built files.
- **A real Git branching scenario.** The base dataset is committed, and each side is a *child commit of that same commit* holding its own dataset, so the common base is a fact of the commit graph rather than of the fixture's own bookkeeping. The three files a case merges are checked back out of those commits through Git, which is what makes the ancestry evidence and the datasets agree.
- **The measurements a claim needs.** Logical identities, per-table row sets, file digests and journal peers are read through separate read-only connections, so "both sides' edits survived" and "the inputs did not move" are measured rather than asserted.

It is test support, not production code: it decides nothing, holds no policy, and the only writes it performs are the ones a case explicitly asks for.

## Code Commentary

### Logic

`new_case` creates one case's world (a repository namespace and private paths); `build_case(base_shape=…, shape=…)` builds the complete case. **Both shape callbacks run before the Git scenario is built**, so a case that needs an unusual state gets it inside the commits instead of having to rewrite the repository afterwards — that ordering is what keeps the ancestry evidence and the datasets true statements about each other. `base_shape` runs on the base state and `shape` runs after the two sides are derived; the two sides always diverge by their own successor revisions and their own identities, and anything more specific (a same-field label conflict, a tampered sealed revision, a removed anchor) arrives through `shape` so the commit graph is built from the states the case means to merge.

State authoring goes through the store: `author_base_state` (through the real operations, then closed through SQLite's own backup), `derive_state` (copy one closed dataset to a path a case will change through the store), and the per-edit helpers `add_revision` (a successor is a new revision naming its predecessor — nothing here edits a sealed row, which is the only legitimate side shape for revision content), `add_invariant`, `set_label` (the one mutable authored edit), `delete_anchor`, `add_anchor`, `add_realization_claim`, `add_family_member`, `add_family`, `add_family_revision`. `_execute` runs one explicit statement with foreign keys enforced.

The Git half: `build_git_world` commits the three datasets into one temporary repository, `_commit_state` commits one dataset as the working tree's only file, and `materialize_commit` exports one commit's dataset file through Git and writes it to a case path. `_git` runs every scenario Git command through the package's **single** runner and refuses a failure.

The measurement half: `table_rows`, `row_counts`, `file_digest`, `journal_peer_names`, `statements_of`, `labels_of` and `revision_id_for`, each read through a separate read-only connection.

### Conventions

- `GitBranchWorld` / `MergeCase` hold one case's world; `state_path(role)`, `identity(role)`, `merge_inputs()` and `databases_by_role()` are the readers the cases use, so no case addresses a raw path.
- `copy_closed` normalises the copy's journal mode, because a case must merge closed files and a backup destination inherits the source's journal mode.
- **`_read_committed_blob` is the one binary read in the harness, and it deliberately does not go through the package's text-decoding runner**: a dataset is bytes, and a runner that decodes to text with `surrogateescape` would hand back something that is not the blob Git stored. The read is read-only and scoped to a repository this fixture created.

### Invariants And Boundaries

- **The base commit is a real commit and each side is a child of it**, so a history with exactly one common base is a property of the repository rather than of the fixture's bookkeeping. Nothing outside `work` is touched: the repository is created here, its objects are its own, and no ref outside it exists.
- **Rows are authored through the store, not by direct INSERT**, so a case measures datasets this package could have produced. `_insert_revision` in the unit module is the documented exception, and it belongs to that case's subject (two independent authors colliding) rather than to this harness.
- **It decides nothing.** No policy, no expectation and no refusal lives here; a case states its own assertions.
- **Boundary.** This is test support and it is not importable by production code. Its registered consumers are exactly the two merge test modules.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
|  The harness's three responsibilities and the statement that it holds no policy. | "It is test support, not production code: it decides nothing, holds no policy" | mcp/tests/merge_case_test_support.py:1-20 |
| The one case world and the readers a case uses instead of raw paths. | `GitBranchWorld`; `MergeCase`; `state_path`; `databases_by_role` | mcp/tests/merge_case_test_support.py:72-78; mcp/tests/merge_case_test_support.py:82-132; mcp/tests/merge_case_test_support.py:91-94; mcp/tests/merge_case_test_support.py:125-132 |
| The base state authored through the real store operations and closed through SQLite's own backup. | `author_base_state`; `copy_closed` | mcp/tests/merge_case_test_support.py:153-194; mcp/tests/merge_case_test_support.py:219-239 |
| The successor rule: a new revision naming its predecessor, never an edit of a sealed row. | `add_revision`; `set_label` | mcp/tests/merge_case_test_support.py:248-285; mcp/tests/merge_case_test_support.py:309-314 |
| The three-commit world whose base is the sides' parent, and the per-commit dataset export. | `build_git_world`; `materialize_commit` | mcp/tests/merge_case_test_support.py:427-449; mcp/tests/merge_case_test_support.py:474-484 |
| The one binary read, and why it does not go through the text-decoding runner. | `_read_committed_blob` | mcp/tests/merge_case_test_support.py:487-508 |
| The build order that puts an unusual state inside the commits. | `build_case` | mcp/tests/merge_case_test_support.py:511-571 |
| The measurement helpers that make input preservation and survival measured rather than asserted. | `table_rows`; `row_counts`; `file_digest`; `journal_peer_names`; `statements_of`; `labels_of` | mcp/tests/merge_case_test_support.py:583-591; mcp/tests/merge_case_test_support.py:594-605; mcp/tests/merge_case_test_support.py:607-611; mcp/tests/merge_case_test_support.py:613-621; mcp/tests/merge_case_test_support.py:623-633; mcp/tests/merge_case_test_support.py:635-645 |
|The registered artifact that makes this harness an owned contract rather than a private helper.|"contract:common-base-merge-cases"| mcp/tests/evidence-lifecycle.toml:1284-1284 |
| The unit-side consuming module, which drives the disjoint-edit survival case. | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:307-310 |
| The integration-side consuming module, whose docstring states which integrity checks a case can reach. | "Boundary cases for the guarded merge: the conflict row identity and the final-integrity checks." | mcp/tests/test_knowledge_guarded_merge_boundaries.py:1-22 |
| The store operations the authored states go through. | `create_invariant`; `create_revision` | mcp/src/agents_remember/memory/knowledge/store.py:236-253; mcp/src/agents_remember/memory/knowledge/store.py:255-289 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |
|  The registered artifact that makes this harness an owned contract rather than a private helper. | "contract:common-base-merge-cases" | mcp/tests/evidence-lifecycle.toml:1284-1284  |
| **The consuming module that drives the harness's own deletion case, cited at the definition the claim is about.** | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/test_knowledge_guarded_merge.py:307-309 |
| **The boundary module that supplies the conflict-row and final-integrity cases, cited at its own module docstring.** | "Boundary cases for the guarded merge: the conflict row identity and the final-integrity checks." | mcp/tests/test_knowledge_guarded_merge_boundaries.py:1-2 |

## Update History
- 2026-09-19T22:28:52+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1284-1284. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1284-1284. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T20:45:09+02:00 — 260915-KS-L23 post-closeout clearance (change set on `ar/260915-ks-l23`, memory base `ce3028e9`, code `5e4eb651`): **cleared the 2 enforced `citation_anchor_absent_from_range` rows in this document.** The closeout's own code commit appended one `consumers` registration above every construct these cards cite, so each cited range ended exactly one line above the line that now carries the anchor row. Widened to the carrying line: `mcp/tests/evidence-lifecycle.toml:1280-1280` → `mcp/tests/evidence-lifecycle.toml:1280-1281` (rows 76, 88). Every line the author cited stays inside its range; no claim, Anchor cell or other range was dropped or re-worded, and each named anchor now resolves inside the widened range.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1280-1280. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1280-1280. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1277-1277. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1277-1277. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1273-1273. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1273-1273. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1161-1161. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1161-1161. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1159-1159. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1159-1159. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T04:55:18+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1155-1155. No content impact: mechanical anchor-range projection bound to citation source snapshot 116840615150c9097436b691cc4243186059d79f882e7a6c73cd85d688950e12; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/evidence-lifecycle.toml:1132-1152` -> `mcp/tests/evidence-lifecycle.toml:1153-1153`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new shared case harness and its `shared-support` contract (`contract:common-base-merge-cases`, exact two-module consumer scope). It records the three responsibilities, the ordering rule that makes a case's unusual state part of the commit graph rather than a post-hoc rewrite of it, the successor-only rule for legitimate side states, and the one deliberate binary read that bypasses the package's text-decoding runner because a dataset is bytes. Verification metadata remains empty until closeout stamps the code commit.
