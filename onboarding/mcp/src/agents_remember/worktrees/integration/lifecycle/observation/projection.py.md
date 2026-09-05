# mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
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
| Single/latest/all readers project retained journals and keep task status from hiding siblings. | `observe_operation`; `latest_operation_projection`; `current_operation_projections` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:45-133 |
| Location contradictions and unreadable contracts become bounded developer-decision projections with no controls. | `_operation_location_decision`; `unreadable_contract_operation_projections` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:136-231 |
| Worker exit and closeout mutation recovery are reconciled into read-only derived records. | `_project_observed_record`; `_project_worker_observed_record` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:224-245; mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:248-257 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.


## 260831-CCR-L15 Observed Operation Projection

`observed_operation_projection` projects one exact durable journal read through the
shared status pipeline: `_project_observed_record` performs only read-only
reconciliation, then `operation_projection` renders the envelope. CCR-R18/R15: a
status-change wait snapshot must be the same coherent envelope a task status read returns for the
exact record whose durable meaningful revision the waiter compared, so the returned cursor and
envelope never splice facts from different journal revisions.

| Finding | Anchor | Source |
| --- | --- | --- |
| The read-only wait snapshot projection entry point. | `observed_operation_projection` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:260-278 |
| The wait controller consuming it for the changed snapshot. | `worktree_status_wait_tool` | mcp/src/agents_remember/application/lifecycle/lifecycle_status_wait.py:81-111 |

## Update History

- 2026-09-05T07:19:22+00:00 — L31-MR-02 history recovery: restored the original dated L18 entry verbatim from memory commit fd41221f11dfe5ac2993520c0d7176ada59ce2ba (its recorded code provenance: f93ac631ca161e5880db3a937728cb256686b13b). This preserves sibling curation history; current body and verification metadata are unchanged.

- 2026-09-05T06:24:16+00:00: Generated citation repair: `_project_observed_record`; `_project_worker_observed_record` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:224-245; mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:248-257. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `observed_operation_projection` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py:260-278. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded `observed_operation_projection` and its R18/R15 same-envelope guarantee for wait snapshots.
- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the observation layer moving location/unreadable developer decisions to `bind_projection_decision` and binding the door identity on unreadable-contract observations. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: created for the extracted read-only projection owner and verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this provenance does not certify the red Dagger gate.
