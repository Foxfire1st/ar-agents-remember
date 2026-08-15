# mcp/tests/test_task_execution_topology.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_execution_topology.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T03:20:17+02:00 |
| lastVerifiedCommitHash | `28a66feae742bf02fe4b647388b220f921cc7007` |
| lastVerifiedCommitDate | 2026-08-15T03:44:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the persisted execution-nature and sprint activity-on-node graph contract through schema,
cross-document topology, task-doc migration, deterministic rendering, observer projection, and
atomic rollback behavior.

## Code Commentary

### Logic

The schema cases reject duplicate nodes and edges, unknown endpoints, self edges, blank reasons,
cycles, and invalid master/sprint field placement. The topology cases build minimal synthetic task
roots, prove legacy state remains migration-required, reject unknown, duplicate, and drifted command
membership, exercise preview and apply, and inject a mid-batch write failure to prove rollback. The
suite also forces multi-parent DAG release, malformed migration envelopes, missing and wrong-kind
migration targets, unresolved masters, non-sprint use, and override identity confinement. A
poisoned second-read regression proves wave derivation validates and returns one pinned sprint
snapshot, and the out-of-root case asserts the actual `task.json` and `task.md` publication targets.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; unpublished candidate code never writes the
  deployed coordinator.
- The suite asserts behavior through public task-document and projection boundaries instead of
  duplicating the topology algorithm.
- Migration must update the sprint and all commanded masters together or leave every file unchanged.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Graph schema cases force the closed structural contract. | `ExecutionGraphSchemaTests` | mcp/tests/test_task_execution_topology.py:53-104 |
| Migration and cross-document cases force exact membership, projection, and rollback. | `ExecutionTopologyTests` | mcp/tests/test_task_execution_topology.py:107-317 |
| The production policy under test lives in the application topology module. | `migrate_execution_topology` | mcp/src/agents_remember/application/task_execution_topology.py:67-129 |

## Update History

- 2026-08-15T03:20:17+02:00 — 260815-DAG-L1 independent-review repair: corrected the
  out-of-repository no-write assertion to the real task-doc filenames and added a poisoned
  second-read regression that distinguishes snapshot-safe wave derivation from the former
  validate-one/read-another sequence.
- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: added production-bound
  refusal cells for every branch reported uncovered by the first targeted artifact and a diamond
  graph that releases its successor only after both predecessors complete. These tests preserve
  the closed contract rather than adding coverage exclusions.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: expanded forcing proof through
  production task-doc create/replace/set-field paths, alias drift/collision refusals, structured
  preview classifications, same-path master/sprint kind-downgrade refusals, exact
  render/projection cells, and normalized out-of-root refusal.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: created as the forcing suite for the new persisted
  topology and finite migration boundary. Verification remains closeout-owned.
