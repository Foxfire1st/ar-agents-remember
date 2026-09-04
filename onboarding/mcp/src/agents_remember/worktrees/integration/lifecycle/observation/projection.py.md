# mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00|
| lastVerifiedCommitHash | `f93ac631ca161e5880db3a937728cb256686b13b` |
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[worktree integration overview](../../overview.md)

## Purpose

Owns read-only lifecycle-journal observation across closeout, integration, and direct landing. It
turns exact retained records and contract/location failures into total public projections without
acquiring mutation, queue, or lifecycle-evidence authority.

## Code Commentary

### Logic

`observe_operation`, `latest_operation_projection`, and `current_operation_projections` locate and
read the stable enclosure-root journals, project every actionable sibling, and surface typed read
or location decisions. `unreadable_contract_operation_projections` retains exact-path journal
visibility when the task contract is unreadable while deliberately exposing no unsafe controls.
The final read pass reconciles observable worker exit and proven closeout mutations into a derived
projection; it does not rewrite the journal.

### Conventions

Aggregate readers remain total across damaged pre-locator state. Task-addressed tools retain the
precise repair refusal, while broad status projection returns no unsafe guess. Imports that would
create a projection cycle stay local to the read helper.

### Invariants And Boundaries

- Observation never writes journals, task documents, doors, queues, Git refs, or contracts.
- Mutable task status cannot hide an actionable journal sibling.
- An unreadable contract preserves exact retained evidence but yields zero legal controls unless
  authority can be re-established.
- Queue rows are schedulability projection only and never become lifecycle evidence here.
- Mutation and recovery facts are derived from exact journal/Git evidence, not inferred from prose.

### Todos

None recorded.

## Docs References

No configured external Domain Documentation source governs this repository-internal projection.

## Repo-Internal References

The source defines the total observation and degraded-projection contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| Single/latest/all readers project retained journals and keep task status from hiding siblings. | `observe_operation`; `latest_operation_projection`; `current_operation_projections` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:47-137 |
| Location contradictions and unreadable contracts become bounded developer-decision projections with no controls. | `_operation_location_decision`; `unreadable_contract_operation_projections` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:138-223 |
| Worker exit and closeout mutation recovery are reconciled into read-only derived records. | `_project_observed_record`; `_project_worker_observed_record` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:224-261 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## CCR-R18@v1 Location And Unreadable Decisions Through The Binder

260831-CCR-L18 replaced the observation layer's `model_copy` projection rewrites with `bind_projection_decision` (from `lifecycle_operation_projection`): `_operation_location_decision` and `unreadable_contract_operation_projections` now compose their bounded developer-decision result through the envelope validator, which clears residual legal controls and cancellability and rebinds every component digest. The unreadable-contract path also passes `doorIdentity=operation_projection_identity(record)` in its `OperationProjectionContext` so a door-observed operation binds the same journal revision the location observation came from.

## Update History

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the observation layer moving location/unreadable developer decisions to `bind_projection_decision` and binding the door identity on unreadable-contract observations. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: created for the extracted read-only projection owner and verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this provenance does not certify the red Dagger gate.
