# mcp/src/agents_remember/providers/cgc/context/cleanup.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/providers/cgc/context/cleanup.py`   |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0`                                                    |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `overview.md`                                                |

## Purpose

Detect and remove stale or out-of-layout CGC runtime artifacts, and assert that
source repositories contain no provider-created artifacts.

## Code Commentary

### Logic

`source_provider_artifacts` / `assert_no_source_provider_artifacts` guard source
repos against `SOURCE_ARTIFACT_NAMES`. `cleanup_cgc_runtime_artifacts(layouts)`
computes the provider root and configured roots, then removes (a) unconfigured
runtime instances under the provider root
(`_unconfigured_cgc_runtime_removals` / `_should_remove_cgc_runtime_child`) and
(b) legacy embedded db/global/kuzu files inside each instance
(`_obsolete_cgc_runtime_removals`). Both removal paths assert the target stays
under the expected root before calling `remove_runtime_path`.

### Invariants And Boundaries

- Refuses to remove any path that resolves outside the provider root / instance
  root (raises `ContextProviderError`).
- Operates on resolved `CgcRuntimeLayout` instances (imported from `core`).
- Was extracted from `core.py` (commit `01f503d`); matches the module's
  "layouts and runtime cleanup" split.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `CgcRuntimeLayout` definition. | `CgcRuntimeLayout` | mcp/src/agents_remember/providers/cgc/context/core.py:36-126 |
| `remove_runtime_path` and `ContextProviderError`. | `ContextProviderError`, `remove_runtime_path` | mcp/src/agents_remember/providers/context_common.py:18-19; mcp/src/agents_remember/providers/context_common.py:122-128 |

## Update History

- 2026-08-03T03:59:59+02:00 — Curated 2 citation findings (1 table row, 1 source-form repair): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-06-10T07:30+02:00 — No content impact: import path updated to `providers/context_common.py` (shared helpers moved out of the facade package, GitHub #58); documented behavior unchanged.
- 2026-05-29T18:35+02:00: Created when the runtime-artifact cleanup functions were extracted from `core.py` (commit `01f503d`).
