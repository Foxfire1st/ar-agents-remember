# mcp/tests/test_knowledge_read_boundaries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_read_boundaries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `1ff1893f44d875073d58af863238501a6be35288`|
| lastVerifiedCommitDate | 2026-09-16T23:58:57+02:00|
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
| The premise node: the fixture tree really holds the blobs its anchors record. | "test_the_fixture_tree_really_holds_the_blobs_its_anchors_record" | mcp/tests/test_knowledge_read_boundaries.py:157-185 |
| **The four blob-observation nodes (`exact`, `mismatch`, `path_absent`, `not_requested`).** | "test_an_anchor_whose_recorded_blob_is_the_requested_trees_blob_is_observed_as_exact"; "test_a_changed_path_reports_a_blob_mismatch_and_never_promotes_the_old_claim"; "test_a_path_absent_from_the_requested_tree_keeps_the_claim_and_reports_the_absence"; "test_no_requested_tree_reports_not_requested_and_still_returns_the_recorded_identities" | mcp/tests/test_knowledge_read_boundaries.py:186-206; mcp/tests/test_knowledge_read_boundaries.py:207-229; mcp/tests/test_knowledge_read_boundaries.py:230-252; mcp/tests/test_knowledge_read_boundaries.py:253-284 |
| **The unavailable-tree and unsupported-locator nodes, and the non-blob entry node.** | "test_an_unavailable_tree_reports_the_unavailable_object_and_substitutes_nothing"; "test_an_unsupported_locator_stays_visible_while_its_blob_is_still_observed"; "test_a_non_blob_tree_entry_is_reported_as_an_entry_and_never_read_as_source_bytes" | mcp/tests/test_knowledge_read_boundaries.py:285-315; mcp/tests/test_knowledge_read_boundaries.py:316-374; mcp/tests/test_knowledge_read_boundaries.py:375-464 |
| **The task-free baseline read node.** | "test_a_baseline_read_serves_a_task_free_context_and_reaches_the_whole_selected_scope" | mcp/tests/test_knowledge_read_boundaries.py:465-497 |
| **The namespace, digest and absent-database refusal nodes.** | "test_a_context_naming_another_namespace_refuses_and_names_both_identities"; "test_a_context_whose_logical_digest_is_not_the_files_is_refused"; "test_an_absent_database_refuses_as_an_unavailable_input_rather_than_as_empty_knowledge" | mcp/tests/test_knowledge_read_boundaries.py:498-527; mcp/tests/test_knowledge_read_boundaries.py:528-553; mcp/tests/test_knowledge_read_boundaries.py:554-575 |
| **The schema-generation node, which also asserts the digest-only variant.** | "test_a_context_declaring_another_schema_generation_is_refused_before_a_page_is_built" | mcp/tests/test_knowledge_read_boundaries.py:763-826 |
| **The continuation-binding nodes, each with its own control, and the manifest node that verifies every page's own cursor.** | "test_a_continuation_presented_with_another_selector_refuses_and_returns_no_partial_page"; "test_a_continuation_presented_under_another_context_or_policy_refuses"; "test_a_continuation_that_binds_another_manifest_is_refused_and_its_own_is_verified"; "test_a_continuation_naming_a_position_past_the_selection_refuses_rather_than_escaping"; "test_a_continuation_whose_declared_snapshot_was_altered_refuses_rather_than_mixing_revisions"; "test_a_continuation_against_its_own_snapshot_continues_the_same_manifest" | mcp/tests/test_knowledge_read_boundaries.py:576-604; mcp/tests/test_knowledge_read_boundaries.py:605-663; mcp/tests/test_knowledge_read_boundaries.py:664-724; mcp/tests/test_knowledge_read_boundaries.py:725-762; mcp/tests/test_knowledge_read_boundaries.py:827-858; mcp/tests/test_knowledge_read_boundaries.py:859-892 |
| **The read-only property, measured on a real database file.** | "test_a_refused_read_of_a_real_database_leaves_the_file_byte_identical" | mcp/tests/test_knowledge_read_boundaries.py:893-941 |
| **The disclosed unasserted defensive branch this module does not count as coverage.** | `_tree_entry`; `_TreeLookupFailed` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:250-281; mcp/src/agents_remember/memory/knowledge/read_anchors.py:298-305 |
| The lane row this module occupies. | "mcp/tests/test_knowledge_read_boundaries.py" | mcp/tests/test-evidence-lanes.toml:157 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the read's integration-lane population. It records the seven anchor observations measured against real committed bytes, the snapshot/namespace/schema refusals (with the schema node asserting the digest-only variant that shows why the digest cannot stand in for the schema comparison), the continuation-binding family with its positive controls, the read-only property measured on a real file, and the task-free baseline read. **The card also carries the honest limit explicitly: `_tree_entry`'s non-zero-exit branch is disclosed as an unasserted defensive branch (L9 ledger `A6`) and must not be read as coverage — the published claim that a mutation made it reachable was withdrawn by the leaf's evidence erratum**, because the kill that appeared to prove it also appears with the production line untouched; the `OSError` half is driven by a case in the paths module. It records that the path cases moved out of this module in fix round 2 rather than the 1 200-line limit being waived. Verification metadata remains empty until closeout stamps the code commit.
