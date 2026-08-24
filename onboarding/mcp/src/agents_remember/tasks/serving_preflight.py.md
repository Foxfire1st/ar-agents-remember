# mcp/src/agents_remember/tasks/serving_preflight.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/serving_preflight.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
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

`TOPOLOGY_SCHEMA_VERSION = "ar-execution-topology/v1"` names the schema the graph operations emit;
`TOPOLOGY_SERVING_VERSION_FLOOR = "3.0.0rc8"` is the first served distribution known to carry the
topology fields (rc7 predates them; every later release compares above the floor).
`require_serving_topology_schema()` has two legs:

1. **Model self-probe** — the process that will serve is the MCP server running the tool for
   in-process invocations, so it checks `TaskDocument.model_fields` for
   `executionNature`/`executionGraph`; a missing field raises `TopologyServingBuildError`
   (`task-execution-topology-serving-build-unsupported`) naming the missing fields and pointing at
   `docs/reference/execution-topology-migration.md`.
2. **Installed-distribution check** — when the installed `agents-remember-mcp` distribution is a
   non-editable wheel below the floor, refuse even when the checkout code on `sys.path` is current
   (that mixed build is exactly what wrote rc7-unreadable rows). Editable installs pass by
   construction (the checkout code is the serving code); a source-tree run with no installed
   distribution passes and relies on the operator contract (run authoring through the deployed
   serving server).

`_is_editable_install` proves the resolved distribution is served from this checkout with three
signals: the metadata directory (`*.egg-info` when `mcp/src` is on the import path, or the dist-info
of an editable install) sits inside the running package's source tree (`_PACKAGE_SOURCE_ROOT`,
derived from `agents_remember.__file__`); `direct_url.json` declares an editable install; or an
`__editable__*.pth` sits beside the dist-info. A real installed wheel fails all three and the
version floor decides. `_below_floor` refuses only **proven** pre-floor releases: dev/post/local
builds and unparseable versions pass (they are not provably the stale rc7 build), so CI editable
installs and dev builds are unaffected (L15-R4).

For DAGQC L2 every observable metadata boundary is explicit: distribution discovery, metadata-path
iteration, path stat, `direct_url.json` read, and version metadata read each translate expected
environment failures into a chained `TopologyServingBuildError`. The distribution version is read
once and that snapshot is used for the policy decision. Programmer errors outside the declared
read/stat/metadata failure families still escape.

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
- Editable/dev/post/local installs and source-tree runs pass; only proven pre-floor non-editable
  wheels refuse.
- This module is pure policy plus importlib.metadata inspection — it never writes, never mutates,
  and never touches the coordination root.
- Expected read/stat/iteration/version failures are total at the public preflight boundary and keep
  their original cause through exception chaining; broad catch-all translation is forbidden.
- One preflight uses one distribution-version snapshot.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| The operator contract for served-build preflight (section 4): run authoring through the deployed serving server; refresh the rc7 venv. | "## 4. Served-build preflight (blocks the rc7 failure class)" | docs/reference/execution-topology-migration.md:66-92 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The preflight gate and its two legs. | `require_serving_topology_schema`; `_installed_distribution`; `_is_editable_install`; `_below_floor` | mcp/src/agents_remember/tasks/serving_preflight.py:55-89; mcp/src/agents_remember/tasks/serving_preflight.py:91-95; mcp/src/agents_remember/tasks/serving_preflight.py:98-132; mcp/src/agents_remember/tasks/serving_preflight.py:143-154 |
| Wired before any write in graph authoring. | `author_execution_graph` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:193-261 |
| Wired into ordinary topology-emitting edits. | `enforce_execution_topology_edit`; `_edit_emits_topology_schema` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:762-813; mcp/src/agents_remember/application/task_docs/task_execution_topology.py:828-842 |
| Wired into sprint attach/detach through the linkage wrapper. | `_require_serving_topology_schema` | mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:85-91 |
| The forcing suite covers the model-field refusal, the below-floor refusal, the editable/source pass, and every `_is_editable_install` branch. | `ServingFloorTests`; `EditableInstallDetectionTests` | mcp/tests/test_serving_preflight.py:26-238 |

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

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: centralized explicit distribution read/stat/iteration/version translations and single-snapshot version policy under the typed serving-build error. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-20T21:30+02:00 — Created for 260815-DAG-L15-R4: the served-build preflight module
  (model self-probe + non-editable wheel version floor 3.0.0rc8, fail-closed), wired before every
  topology-schema write. Verified at code commit de3a0fd9.
