# mcp/tests/test_execution_graph_view.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_execution_graph_view.py`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
| governingOverview      | `overview.md`                                    |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the render-ready sprint graph projection builder (260815-DAG-L12 R4). The builder
under test is primitives-only (the observer package must not import tasks); the tests
build a real persisted graph and walk it the same way the serving layer does — derived
waves, resolved edge endpoints, facts, and titles — then feed the builder plain data.

## Code Commentary

### Logic

`ExecutionGraphViewBuilderTests` forces `build_execution_graph_view` with the serving-layer
walk (`_walk` mirrors `_task_documents._execution_graph_view`): a zero-edge graph projects
one wave of independent lump nodes with mechanical frontier states (`in-flight` for an
in-progress master, `landed` for a completed one); a segmented master projects
wave-ordered segment nodes (`seg1`/`seg2` node identities) with joined titles and
predecessor reasons plus judgment ids; a missing master falls back to the ref key and a
conservative `ready` state (never landed, never in-flight — reviewer finding F6); and
`node_identity` stays stable for lumps and segments (the segment ordinal is
declaration-ordered so appended segments keep earlier identities).

### Invariants And Boundaries

- Tests exercise the public builder through the same walk the serving layer performs, not
  through an internal re-derivation.
- Frontier state is asserted as mechanical (statuses + edges only).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The builder forcing suite. | `ExecutionGraphViewBuilderTests` | mcp/tests/test_execution_graph_view.py:129-265 |
| The primitives-only builder under test. | `build_execution_graph_view` | mcp/src/agents_remember/observer/projection_graph.py:228-260 |
| The serving-layer walk the tests mirror. | `_execution_graph_view` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:327-367 |
| The joined-titles input type. | `SprintGraphTitles` | mcp/src/agents_remember/tasks/execution_graph_titles.py:22-33 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R4): the graph-view builder forcing

suite — zero-edge, segmented-master, missing-master fallback, and stable node identity.

Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R4): the graph-view builder forcing
  suite — zero-edge, segmented-master, missing-master fallback, and stable node identity.
  Verified at code commit b7f2c8e2.
