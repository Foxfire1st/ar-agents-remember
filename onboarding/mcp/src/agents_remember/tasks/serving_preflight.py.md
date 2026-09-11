# mcp/src/agents_remember/tasks/serving_preflight.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/serving_preflight.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `overview.md` |

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

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| The operator contract for served-build preflight (section 4): run authoring through the deployed serving server; refresh the rc7 venv. | "## 4. Served-build preflight (blocks the rc7 failure class)" | docs/reference/execution-topology-migration.md:66-92 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The preflight gate is now the model self-probe alone: `require_serving_topology_schema` refuses when the running build's `TaskDocument.model_fields` lack the topology fields. The installed-distribution leg and its helpers `_installed_distribution`, `_is_editable_install`, `_below_floor`, and `TOPOLOGY_SERVING_VERSION_FLOOR` no longer exist in the tree — a task-plane edit never consults the installed distribution version. | `require_serving_topology_schema` | mcp/src/agents_remember/tasks/serving_preflight.py:32-42 |
| Wired before any write in graph authoring. | `author_execution_graph` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:202-285 |
| Wired into ordinary topology-emitting edits. | `enforce_execution_topology_edit`; `_edit_emits_topology_schema` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:780-802; mcp/src/agents_remember/application/task_docs/task_execution_topology.py:877-891; mcp/src/agents_remember/application/task_docs/task_execution_topology.py:828-842 |
| Wired into sprint attach/detach through the linkage wrapper. | `_require_serving_topology_schema` | mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:84-90 |

## Cross-Repo References

The preflight guards the persistent task tree in the configured coordination root, but it has no
sibling-repository code dependency; the operator guidance points at the same-repository migration
document.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260821-DAGQC-L2 Explicit Serving-Build Failure Boundary

The preflight no longer depends on callers remembering every lower-level metadata failure class.
Each observable operation has one explicit translation seam, while semantic policy—model probe,
editable/source-tree handling, release floor, and dev/post/local treatment—remains unchanged. This
makes the public check total for expected environment failures without hiding programmer defects.

## Update History
- 2026-09-11T23:25:00+00:00: Completed the narrative pass the row repair left owed. The Logic section no longer documents a two-leg preflight: it records the single model self-probe and states that `TOPOLOGY_SERVING_VERSION_FLOOR`, `_installed_distribution`, `_is_editable_install` and `_below_floor` no longer exist and that installation shape no longer reaches this decision. The three invariants that described the distribution-version snapshot, its total failure translation and the pre-floor-wheel refusal were replaced with the surviving behavior. Content change, not a range repoint.
- 2026-09-11T23:05:00+00:00: The row claiming a two-leg preflight anchored `_installed_distribution`, `_is_editable_install`, and `_below_floor`, which no longer exist anywhere in the tree, and cited ranges past the end of a now 42-line module. The installed-distribution leg was deleted — a task-plane edit never consults the installed distribution version — so the row records that removal and anchors the surviving model self-probe `require_serving_topology_schema` at its current definition. The surrounding narrative still describes the removed leg and needs a curator pass.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_require_serving_topology_schema` repointed to mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:84-90. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: centralized explicit distribution read/stat/iteration/version translations and single-snapshot version policy under the typed serving-build error. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-20T21:30+02:00 — Created for 260815-DAG-L15-R4: the served-build preflight module
  (model self-probe + non-editable wheel version floor 3.0.0rc8, fail-closed), wired before every
  topology-schema write. Verified at code commit de3a0fd9.
