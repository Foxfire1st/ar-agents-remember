# L4 Onboarding Maintenance Input Ledger

| Field | Value |
| --- | --- |
| repository | agents-remember |
| mode | automated existing-memory-slice-maintenance |
| task | 260815-DAG-L4 integration branch authority |
| capturedAt | 2026-08-15T23:38+02:00 |
| source registry | system/sources.md |
| domain documentation | none configured |
| cross-repository sources | none allowed |
| operator decision | proceed; autonomous atomic-master completion was explicitly authorized |

## Authoritative Inputs

The frozen L4 code candidate, the L4 task document, and the two independent route-review reports are
the authoritative inputs. Existing onboarding supplies route structure and historical context; it
is not allowed to override current source behavior.

## New Source Units

- mcp/src/agents_remember/controlplane/integration_authority_lock.py
- mcp/src/agents_remember/worktrees/atomic_series_seal.py
- mcp/src/agents_remember/worktrees/closeout_preview.py
- mcp/src/agents_remember/worktrees/integration_branch_authority.py
- mcp/src/agents_remember/worktrees/integration_operation_authority.py
- mcp/src/agents_remember/worktrees/integration_quality_checkout.py
- mcp/src/agents_remember/worktrees/integration_ref_transaction.py
- mcp/src/agents_remember/worktrees/lifecycle_operation_lease.py
- mcp/src/agents_remember/worktrees/named_ref_memory.py
- mcp/src/agents_remember/worktrees/series_closeout.py
- mcp/tests/integration_branch_authority_test_support.py
- mcp/tests/test_atomic_series_seal.py
- mcp/tests/test_closeout_queue_task_doc_status.py
- mcp/tests/test_integration_authority_lowest_writers.py
- mcp/tests/test_integration_branch_authority.py
- mcp/tests/test_integration_branch_authority_edges.py
- mcp/tests/test_integration_ref_transaction.py
- mcp/tests/test_topology_publication_authority.py
- mcp/tests/test_worktree_organizational_start.py

## Existing Units Reconciled

Seventy-eight changed-source file cards were body-reviewed and updated: two dashboard projection
units, forty application/control-plane/model/memory/task/worktree/skill units, and thirty-six test
units. Thirteen governing route overviews plus the entity catalog were reconciled. The generated
projection schema card was updated surgically because it contains a pre-existing duplicated history
section that this task did not use as an authority source.

## Coverage Boundary

Path rules include the changed MCP, dashboard, runtime-skill, and test sources. Build/cache/vendor
outputs remain excluded. No documentation or cross-repository source was inferred beyond the empty
configured registry.

