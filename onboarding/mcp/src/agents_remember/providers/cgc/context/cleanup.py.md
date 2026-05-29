# mcp/src/agents_remember/providers/cgc/context/cleanup.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember-md                                           |
| path                   | `mcp/src/agents_remember/providers/cgc/context/cleanup.py`   |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2`                                                    |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
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

| Finding | Source Path |
| --- | --- |
| `CgcRuntimeLayout` definition. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/context/core.py) |
| `remove_runtime_path` and `ContextProviderError`. | [common.py](agents-remember-md/mcp/src/agents_remember/providers/context/common.py) |

## Update History

- 2026-05-29T18:35+02:00: Created when the runtime-artifact cleanup functions were extracted from `core.py` (commit `01f503d`).
