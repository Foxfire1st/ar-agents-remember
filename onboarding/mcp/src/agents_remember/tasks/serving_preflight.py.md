# mcp/src/agents_remember/tasks/serving_preflight.py

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Served-build preflight for execution-topology schema writes (260815-DAG-L15-R4). The 3.0.0rc7
failure class (ar-coordination l9-issues.md:9-19) wrote `executionNature`/`executionGraph` into the
persistent task tree while the served build's `TaskDocument` model predated the fields and used
`extra="forbid"`, forcing a snapshot restore. Graph authoring/migration operations therefore verify
the serving runtime understands the topology schema **before** writing, refusing with upgrade
guidance otherwise. Fail-closed: an unverifiable serving build refuses rather than risking the rc7
restore class.

## Code Commentary

### Logic

`TOPOLOGY_SCHEMA_VERSION = "ar-execution-topology/v1"` names the schema the graph operations emit.
`require_serving_topology_schema()` now has **one** leg:

1. **Model self-probe** — the process that will serve is the MCP server running the tool for
   in-process invocations, so it checks `TaskDocument.model_fields` for
   `executionNature`/`executionGraph`; a missing field raises `TopologyServingBuildError`
   (`task-execution-topology-serving-build-unsupported`) naming the missing fields and pointing at
   `docs/reference/execution-topology-migration.md`.

The installed-distribution leg is gone. `TOPOLOGY_SERVING_VERSION_FLOOR`, `_installed_distribution`,
`_is_editable_install` and `_below_floor` no longer exist in the tree: a task-plane edit does not
consult the installed distribution version at all, so an authoring run against a stale installed
wheel is no longer refused here. What survives is the self-probe above plus the operator contract to
run authoring through the deployed serving server.

`require_serving_retirement_schema()` is a second, separate self-probe for master retirement: it checks that
`SubTaskRef.model_fields` holds `retirement` and otherwise raises `TopologyServingBuildError` with the status
`task-master-retirement-serving-build-unsupported` and the text "restart required: this build predates master
retirement and cannot parse a sprint that holds a retired row". The document model is strict, so a process
started before a build that has the `retirement` key cannot read a sprint that holds a retired row; a retirement
write therefore refuses in a process whose model lacks the key, rather than leaving a sprint that the old build
cannot parse. The topology probe above is unchanged.

### Conventions

- The refusal is a typed `AgentsRememberError` subclass (`TopologyServingBuildError`) with the
  `task-execution-topology-serving-build-unsupported` status; the application seams wrap it in their
  own error families (`ExecutionTopologyError` in topology authoring, `SprintLinkageError` in sprint
  linkage).
- Fail-closed by design: the check never guesses that an unverifiable build is safe.

### Invariants And Boundaries

- The preflight runs **before** any topology-schema write (validate-then-mutate), including ordinary
  `create`/`replace`/`set_field` edits that emit topology schema bytes (`_edit_emits_topology_schema`
  in `application/task_execution_topology.py`).
- Editable/dev/post/local installs and source-tree runs pass, and so does every other install now:
  the distribution-version leg was deleted, so installation shape no longer reaches this decision.
- This module is pure policy plus a model self-probe — it never writes, never mutates, and never
  touches the coordination root.
- The remaining failure surface is the self-probe alone; instantiating the preflight raises no
  bare exception of its own beyond `TopologyServingBuildError`.

## Evidence

### Docs References

- The operator contract for served-build preflight (section 4): run authoring through the deployed serving server; refresh the rc7 venv. [1]

### Repo-Internal References

- The preflight gate is now the model self-probe alone: `require_serving_topology_schema` refuses when the running build's `TaskDocument.model_fields` lack the topology fields. The installed-distribution leg and its helpers `_installed_distribution`, `_is_editable_install`, `_below_floor`, and `TOPOLOGY_SERVING_VERSION_FLOOR` no longer exist in the tree — a task-plane edit never consults the installed distribution version. [2]
- Wired before any write in graph authoring. [3]

- Wired into ordinary topology-emitting edits. [4]

- Wired into sprint attach/detach through the linkage wrapper. [5]

### Cross-Repo References

The preflight guards the persistent task tree in the configured coordination root, but it has no
sibling-repository code dependency; the operator guidance points at the same-repository migration
document.

No meaningful cross-repo references found.

- The retirement probe refuses when the running model has no `retirement` row field. [6]

## 260821-DAGQC-L2 Explicit Serving-Build Failure Boundary

The preflight no longer depends on callers remembering every lower-level metadata failure class.
Each observable operation has one explicit translation seam, while semantic policy—model probe,
editable/source-tree handling, release floor, and dev/post/local treatment—remains unchanged. This
makes the public check total for expected environment failures without hiding programmer defects.
