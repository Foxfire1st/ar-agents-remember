# mcp/tests/test_knowledge_consolidation_proposal.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Tests the `knowledge_read(view="consolidation_proposal")` tool payload across all three proposal modes (after a master, for a named family or folder, and oldest-unconsolidated default) plus selector refusals.

## Code Commentary

Builds a two-commit Git memory fixture (`_memory`) holding three families (`FAM-F00001`..`FAM-F00003`), seven invariants realized across files via onboarding sidecars, a finished master history (`261112-FIX-L1` modifying `INV-A00001` and `INV-N00001`, writing `INV-C00001`, and only reading `INV-B00001`), and a prior reviewed consolidator pass on `FAM-F00002`. Calling `knowledge_read_payload` verifies: (1) `master_id` proposes touched families (`FAM-F00001`, `FAM-F00003`) with same-file loose rules attached (`INV-N00001`, `INV-N00002`), excludes different-file loose rules in the same folder (`INV-N00003`), ignores read-only `INV-B00001`, and lists touched loose rules in `proposal.rulesInNoFamily`; (2) `record_id` and `source_path` scope the proposal to one family or folder with same-file loose rules attached; (3) an unqualified read orders families oldest-unconsolidated first (`FAM-F00003`, `FAM-F00001`, then previously consolidated `FAM-F00002` carrying `lastConsolidated`), reports exact `counts`, and writes a matching JSON report; and (4) supplying two selectors refuses with `bad_selector` while an unknown `master_id` refuses with `selector_absent`.

## Relationships

Exercises the full `mcp.tools.knowledge.knowledge_read_payload` -> `knowledge_views.record_views._proposal_view` -> `application.knowledge_consolidation_proposal.proposal_view` path. Uses `knowledge_index_test_support` and `knowledge_review_fact_test_support` fixtures.

## Evidence

- `_memory` constructs a two-commit converted Git memory tree so family creation order, realization sidecars, master writes, and prior consolidator history are all exercised over real commits. [1]
- Verifies master-scoped, family/folder-scoped, and oldest-first consolidation proposals, same-file-only loose-rule attachment, `rulesInNoFamily`, `lastConsolidated`, counts, and report output. [2]
- Verifies supplying conflicting selectors refuses with `bad_selector` and an unknown `master_id` refuses with `selector_absent`. [3]
