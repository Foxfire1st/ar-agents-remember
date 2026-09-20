# mcp/tests/test_knowledge_read_boundaries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_read_boundaries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`|
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l07` uncommitted source; base `4eb2b1992f6183fba06e9f31aa664d9a93094c26` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The read's real boundaries: a real Git tree, a real snapshot identity, a real publication.** Twenty
nodes in `integration` (row `mcp/tests/test-evidence-lanes.toml:157`) — the properties the ordinary unit
path cannot fail from outside, because they need real committed bytes, a real database file and a real
publication to exist at all.

941 lines. It held the path cases until fix round 2 pushed it past the 1 200-line limit, at which point the
path cases moved to `mcp/tests/test_knowledge_read_paths.py` rather than the limit being waived.

## Code Commentary

### Logic

**The seven anchor observations, against real committed bytes** (`:157`–`:464`):

- the fixture's tree really holds the blobs its anchors record (the premise, measured as a fact rather than
  asserted from prose);
- `exact_recorded_blob` when the requested tree holds the recorded blob;
- `recorded_blob_mismatch` when the path changed, **with the old claim never promoted**;
- `path_absent` for a path the requested tree does not carry, **with the recorded claim and its blob
  identity preserved**;
- `not_requested` when no tree was named, **still carrying every recorded identity**;
- `recorded_object_unavailable` for an unavailable tree, substituting nothing;
- `unsupported_locator` remaining visible while the blob is still observed, and a non-blob tree entry
  reported **as an entry** and never read as source bytes.

**The snapshot, namespace and schema refusals** (`:498`–`:575`, `:763`–`:826`): a context naming another
namespace refuses and names both identities; a context whose logical digest is not the file's refuses; an
**absent database refuses as an unavailable input rather than as empty knowledge**; and a context
declaring another schema generation refuses before a page is built — the node that also asserts the
digest-only variant, which is what shows why the digest comparison cannot stand in for the schema
comparison.

**The continuation-binding family, each with its own positive control** (`:576`–`:892`): another selector,
another context or policy, **another manifest** (with the walk asserting at every step that the
continuation a page hands back carries the manifest that page declared), a position past the end of the
selection, an altered declared snapshot, and the control that a continuation against its own snapshot
continues the same manifest. **No one of these returns a partial page.**

**The read-only property, measured on a real file** (`:893`): a refused read of a real database leaves the
file byte-identical.

**The task-free baseline read** (`:465`): a context with `task_ref=None` serves a page and reaches the whole
selected scope — planning can read recorded knowledge with no leaf and no enclosure.

### Conventions

- `pytestmark = pytest.mark.integration`. The module's registration is a precondition: an unregistered
  `test_*.py` module makes `load_lane_manifest` refuse the repository, which the collection hook turns into
  a collection error.
- The real Git tree is built in `tmp_path`; no case touches the checkout or the network.
- A refusal node asserts the **code** and, where the code alone would be ambiguous, the detail's named
  comparison.

### Invariants And Boundaries

- **The one honestly unasserted branch is disclosed, not counted.** `read_anchors._tree_entry`'s
  **non-zero-exit** branch is reachable by no input on this host and is an explicitly disclosed unasserted
  defensive branch (L9 ledger **A6**). A published claim that a mutation made it reachable was **withdrawn**
  by the leaf's evidence erratum, because the kill that appeared to prove it also appears with the
  production line untouched. **Do not read that branch as coverage.** The `OSError` half is driven by a
  case in `mcp/tests/test_knowledge_read_paths.py:539`.
- **A guard that is reachable and verdict-changing but has no killing node is reported, not claimed.** This
  module reports the one such line it knows of through the ledger rather than presenting it as protection.
- **Boundary.** This is a test module. It declares one lane, asserts behaviour and owns no production
  contract.

### Todos

None recorded. The disclosed non-zero-exit branch above is L9's, not this module's to close by assertion.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The premise node: the fixture tree really holds the blobs its anchors record. | "test_the_fixture_tree_really_holds_the_blobs_its_anchors_record" | mcp/tests/test_knowledge_read_boundaries.py:193-193 |
| **The four blob-observation nodes (`exact`, `mismatch`, `path_absent`, `not_requested`).** | "test_an_anchor_whose_recorded_blob_is_the_requested_trees_blob_is_observed_as_exact"; "test_a_changed_path_reports_a_blob_mismatch_and_never_promotes_the_old_claim"; "test_a_path_absent_from_the_requested_tree_keeps_the_claim_and_reports_the_absence"; "test_no_requested_tree_reports_not_requested_and_still_returns_the_recorded_identities" | mcp/tests/test_knowledge_read_boundaries.py:222-240; mcp/tests/test_knowledge_read_boundaries.py:243-263; mcp/tests/test_knowledge_read_boundaries.py:266-286; mcp/tests/test_knowledge_read_boundaries.py:289-318 |
| **The unavailable-tree and unsupported-locator nodes, and the non-blob entry node.** | "test_an_unavailable_tree_reports_the_unavailable_object_and_substitutes_nothing"; "test_an_unsupported_locator_stays_visible_while_its_blob_is_still_observed"; "test_a_non_blob_tree_entry_is_reported_as_an_entry_and_never_read_as_source_bytes" | mcp/tests/test_knowledge_read_boundaries.py:285-315; mcp/tests/test_knowledge_read_boundaries.py:316-374; mcp/tests/test_knowledge_read_boundaries.py:375-464 |
| **The task-free baseline read node.** | "test_a_baseline_read_serves_a_task_free_context_and_reaches_the_whole_selected_scope" | mcp/tests/test_knowledge_read_boundaries.py:502-502 |
| **The namespace, digest and absent-database refusal nodes.** | "test_a_context_naming_another_namespace_refuses_and_names_both_identities"; "test_a_context_whose_logical_digest_is_not_the_files_is_refused"; "test_an_absent_database_refuses_as_an_unavailable_input_rather_than_as_empty_knowledge" | mcp/tests/test_knowledge_read_boundaries.py:535-562; mcp/tests/test_knowledge_read_boundaries.py:565-588; mcp/tests/test_knowledge_read_boundaries.py:591-610 |
| **The schema-generation node, which also asserts the digest-only variant.** | "test_a_context_declaring_another_schema_generation_is_refused_before_a_page_is_built" | mcp/tests/test_knowledge_read_boundaries.py:763-826 |
| **The continuation-binding nodes, each with its own control, and the manifest node that verifies every page's own cursor.** | "test_a_continuation_presented_with_another_binding_refuses_and_returns_no_partial_page"; "test_a_continuation_that_binds_another_manifest_is_refused_and_its_own_is_verified"; "test_a_continuation_naming_a_position_past_the_selection_refuses_rather_than_escaping"; "test_a_continuation_whose_declared_snapshot_was_altered_refuses_rather_than_mixing_revisions"; "test_a_continuation_against_its_own_snapshot_continues_the_same_manifest" | mcp/tests/test_knowledge_read_boundaries.py:613-708; mcp/tests/test_knowledge_read_boundaries.py:711-769; mcp/tests/test_knowledge_read_boundaries.py:772-807; mcp/tests/test_knowledge_read_boundaries.py:891-920; mcp/tests/test_knowledge_read_boundaries.py:923-954 |
| **The read-only property, measured on a real database file.** | "test_a_refused_read_of_a_real_database_leaves_the_file_byte_identical" | mcp/tests/test_knowledge_read_boundaries.py:957-957 |
| **The disclosed unasserted defensive branch this module does not count as coverage.** | `_tree_entry`; `_TreeLookupFailed` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:368-399; mcp/src/agents_remember/memory/knowledge/read_anchors.py:416-423 |
| The lane row this module occupies. | "mcp/tests/test_knowledge_read_boundaries.py" | mcp/tests/test-evidence-lanes.toml:206-206 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T01:23+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared the last 2 enforced citation rows this card carried (`citation_anchor_absent_from_range`), by renaming the dead anchors to the surviving construct and citing its own extent.** `test_a_continuation_presented_with_another_selector_refuses_and_returns_no_partial_page` and `test_a_continuation_presented_under_another_context_or_policy_refuses` exist nowhere in the tree; reading `mcp/tests/test_knowledge_read_boundaries.py` shows they were consolidated into `test_a_continuation_presented_with_another_binding_refuses_and_returns_no_partial_page` at `:613`, whose own docstring says so in the source's words — *"The selector half and the context/policy half are one rule … so they are one case … This was three cases until they were merged, and every assertion of all three survives here."* Its body calls `_selector_binding_refuses` (`:627-651`) and `_context_and_policy_bindings_refuse` (`:654-708`), so the merged case's own extent is `:613-708`, and the row's first range was repointed there from `:613-653` (which reached the selector half only). The two dead anchor cells were replaced by that one surviving name; the Finding text, the claim's other four anchors and the other four ranges are unchanged, and no citation was dropped. Reviewed against the working candidate `ar/260915-ks-l30-ar`; no commit exists for these bytes and the commit stamp is not advanced.
- 2026-09-20T00:54+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): finished by hand-reading the rows the earlier mechanical projection left open, verifying each anchor with `grep -n`/AST against the candidate before writing. Against the checklist rows this card carried, three are cleared (`citation_anchor_absent_from_range` — the four blob-observation nodes, the namespace/digest/absent-database nodes, and the continuation-binding nodes): every range that did not hold its anchor was replaced with the exact construct extent the claim names (`222-240`, `243-263`, `266-286`, `289-318`, `535-562`, `565-588`, `591-610`, `613-653`, `711-769`, `772-807`, `891-920`, `923-954`), because the registration rows above them shifted every construct down. One row is LEFT and reported: `test_a_continuation_presented_with_another_selector_refuses_and_returns_no_partial_page` and `test_a_continuation_presented_under_another_context_or_policy_refuses` exist nowhere in the tree — both were merged into `test_a_continuation_presented_with_another_binding_refuses_and_returns_no_partial_page`, so the claim's six-node list is now four nodes and only a curator re-reading the claim can fix it. Claims, anchors and every other range are unchanged, and no verification stamp was advanced. No commits.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 6 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `_TreeLookupFailed`; `_tree_entry`; `test_a_continuation_against_its_own_snapshot_continues_the_same_manifest`; `test_a_continuation_naming_a_position_past_the_selection_refuses_rather_than_escaping`; `test_an_absent_database_refuses_as_an_unavailable_input_rather_than_as_empty_knowledge`; `test_no_requested_tree_reports_not_requested_and_still_returns_the_recorded_identities`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "test_the_fixture_tree_really_holds_the_blobs_its_anchors_record" repointed to mcp/tests/test_knowledge_read_boundaries.py:193-193. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "test_a_baseline_read_serves_a_task_free_context_and_reaches_the_whole_selected_scope" repointed to mcp/tests/test_knowledge_read_boundaries.py:502-502. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "test_a_refused_read_of_a_real_database_leaves_the_file_byte_identical" repointed to mcp/tests/test_knowledge_read_boundaries.py:957-957. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:54:18+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the three enforced `citation_anchor_absent_from_range` rows in this document** (three table rows, one node each). Each row's node list stopped one node short of its last entry: the fourth blob-observation node's definition is at `287` and the row ended at `284`; the absent-database node's definition is at `588` and the row ended at `575`; the manifest node's definition is at `910` and the row ended at `892`. Each row's last range was widened to the definition line it names (`253-287`, `554-588`, `859-910`), so the ranges now reach the defs the anchors name, exactly as the leaf's own renumbering shifted them. No claim was re-worded; every other range and anchor in each row is unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_the_fixture_tree_really_holds_the_blobs_its_anchors_record" repointed to mcp/tests/test_knowledge_read_boundaries.py:191-191. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_baseline_read_serves_a_task_free_context_and_reaches_the_whole_selected_scope" repointed to mcp/tests/test_knowledge_read_boundaries.py:499-499. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_refused_read_of_a_real_database_leaves_the_file_byte_identical" repointed to mcp/tests/test_knowledge_read_boundaries.py:944-944. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:206-206. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:200-200. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:199-199. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:197-197. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:195-195. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:175-175. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:173-173. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 6 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_knowledge_read_boundaries.py`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 3 generated projection bullet(s) by hand** — `mcp/tests/test_knowledge_read_boundaries.py`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_knowledge_read_boundaries.py"` → `mcp/tests/test-evidence-lanes.toml:166-166`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/test-evidence-lanes.toml:164-164` -> `mcp/tests/test-evidence-lanes.toml:165-165`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-17T19:11:00+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): No content impact: this leaf changed the *cited* sources, not this file's own source, and the card's claim bytes were re-read against the current anchored construct and retained; only citation ranges were re-derived where a cited file grew. No row, citation or claim was deleted, and the verification metadata is not advanced because the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T19:11:00+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): No content impact: this leaf changed the *cited* sources, not this file's own source, and the card's claim bytes were re-read against the current anchored construct and retained; only citation ranges were re-derived where a cited file grew. No row, citation or claim was deleted, and the verification metadata is not advanced because the code commit does not exist yet and closeout owns the stamp.

- 2026-09-16T21:50:00+00:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the read's integration-lane population. It records the seven anchor observations measured against real committed bytes, the snapshot/namespace/schema refusals (with the schema node asserting the digest-only variant that shows why the digest cannot stand in for the schema comparison), the continuation-binding family with its positive controls, the read-only property measured on a real file, and the task-free baseline read. **The card also carries the honest limit explicitly: `_tree_entry`'s non-zero-exit branch is disclosed as an unasserted defensive branch (L9 ledger `A6`) and must not be read as coverage — the published claim that a mutation made it reachable was withdrawn by the leaf's evidence erratum**, because the kill that appeared to prove it also appears with the production line untouched; the `OSError` half is driven by a case in the paths module. It records that the path cases moved out of this module in fix round 2 rather than the 1 200-line limit being waived. Verification metadata remains empty until closeout stamps the code commit.
