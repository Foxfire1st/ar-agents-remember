# test_context_providers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_context_providers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-03T01:55+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_context_providers.py` verifies the shared provider layout, settings expansion, runtime cleanup, and patch helpers used by the provider lifecycle manager — since L12 also the timer-pop patch (idempotency + marker), the patch-script drift guard pinning patch_cgc.py's snippets to the in-package constants, and the HOME-scoped global .cgcignore materialization.

## Code Commentary

### Logic

The test module imports `agents_remember.providers.context` from the MCP
package source path. Layout expansion is driven through one value object per
provider: `cgc_runtime_layout(CgcRepo(coordination_root=…, repo_id=…,
code_repo_root=…, cgcignore_patterns=…))` and
`grepai_runtime_layout(GrepaiWorkspace(coordination_root=…, name=…, roots=…))` —
note the workspace object spells the display name `name`, not the layout's own
`workspace_name` attribute the assertions still read back. It checks that CGC
runtime layout expansion produces a
contained per-repo runner root, pinned requirements file, patch root, durable
`providers/data` FalkorDB backend root, FalkorDB process env, and isolated
HOME-like runtime directories without exposing host venv executable paths. It
verifies that `ensure_cgc_runtime_layout` writes pinned defaults, inherits
source `.gitignore` rules into the managed `.cgcignore`, and excludes
process-only CGC/FalkorDB runtime keys from persisted `.env`.

The provider-settings tests cover CGC multi-root settings expansion, root-level
`cgcignorePatterns`, rejection of configured code repository roots that do not
exist, and rejection of stale `venvRoot` settings. The cleanup test creates a
synthetic stale `my-app` runtime instance plus legacy `db`, `global`, and
`kuzu` artifacts under a configured runtime root, then verifies cleanup removes
only those generated artifacts while preserving the shared FalkorDB backend
data root. The GrepAI tests cover pin handling, workspace runtime paths,
explicit external and repo-internal memory roots indexed live in place,
provider-owned workspace config, PostgreSQL store config, explicit Ollama
endpoint/dimension defaults, central `logs/providers/grepai` operator log
layout, and `ensure_grepai_root_gitignore` (appends `.grepai/` to a root's
`.gitignore`, creates one when absent, idempotent). The remaining tests cover forbidden source
artifact detection, idempotent CGC patch application including the visualizer
repo-query and route patches, rejection of unexpected patch source text, stable
repo id normalization, and stable patch id naming.

CGC layout tests also cover that ambient host `FALKORDB_HOST` and
`FALKORDB_PORT` values do not alter default layout env or provider-settings
`hostPort=auto` expansion.

Windows-host coverage asserts that `to_container_path` strips a leading drive
letter (and is a no-op on POSIX paths), that the layout's
`container_runtime_root` / `container_code_repo_root` are driveless, and that
`env(for_container=True)` renders driveless path values and omits the host-only
Windows variables (`USERPROFILE`, `APPDATA`, `LOCALAPPDATA`) while leaving
non-path values unchanged.

### Conventions

All tests use temporary directories and do not require CodeGraphContext, GrepAI, Docker, FalkorDB, or PostgreSQL to be installed. The `my-app` directory name appears only as synthetic test data to prove stale generated runtime folders are removed; it is not intended live configuration. The GrepAI tests verify generated config text and path containment, not live indexing. The patch tests use small synthetic snippets rather than mutating a real provider package.

### Invariants And Boundaries

The tests protect the core provider invariant: managed provider artifacts belong
under `ar-coordination/providers/` and operator logs under
`ar-coordination/logs/`, not as durable source or memory data. They also
protect reinstall idempotence by proving stale generated runtime instances and
legacy embedded-backend files can be removed without touching shared backend
data or onboarding files, and that GrepAI's durable database data root is
separate from provider-owned config/state scaffolding.

The tests protect that provider backend env authority stays in settings/state,
not ambient host process variables.

The tests also protect the anti-slop boundary that `venvRoot` is no longer a
supported CGC settings field and managed CGC must not fall back to a
coordination-root host executable.

### Todos

- Add integration smoke tests once the environment can provide local CGC and GrepAI packages plus Docker backends without network setup.

## Docs References

No external documentation is needed for these unit tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The layout tests assert that CGC uses `providers/runners/codegraphcontext/<repo-id>`, a shared `providers/data/codegraphcontext/falkordb` backend root, `providers/requirements/codegraphcontext.txt`, patch root, and per-repo FalkorDB process env without host venv executable fields. | `test_cgc_layout_uses_managed_runtime_root` | mcp/tests/test_context_providers.py:91-133 |
| The default-layout test asserts the pinned requirement, config, managed `.cgcignore`, persisted `.env` exclusions, logs, run, HOME, APPDATA, and LOCALAPPDATA directories. | `test_ensure_cgc_runtime_layout_writes_pinned_defaults` | mcp/tests/test_context_providers.py:211-260 |
| The cleanup test removes a synthetic stale `my-app` instance and legacy `db`, `global`, and `kuzu` artifacts while preserving the shared FalkorDB backend data root. | `test_cleanup_cgc_runtime_artifacts_removes_stale_runtime_only` | mcp/tests/test_context_providers.py:262-302 |
| Provider-settings tests cover root expansion, per-root `cgcignorePatterns`, rejection of configured code repository paths that do not exist, and rejection of removed `venvRoot` settings. | `test_cgc_layout_expands_provider_settings_roots`; `test_cgc_layout_rejects_missing_provider_settings_root`; `test_cgc_layout_rejects_removed_venv_root_settings` | mcp/tests/test_context_providers.py:304-345; mcp/tests/test_context_providers.py:383-399; mcp/tests/test_context_providers.py:401-414 |
| GrepAI tests cover pin handling, workspace runtime and PostgreSQL data roots, central log roots, settings expansion across external and internal memory roots indexed live in place, provider-owned workspace config, PostgreSQL store config, explicit Ollama endpoint/dimension defaults, and `ensure_grepai_root_gitignore` (append/create/idempotent `.grepai/` ignore). | `test_grepai_requirements_pin_is_created_and_readable`; `test_grepai_layout_uses_workspace_runtime_and_postgres_data_root`; `test_grepai_layout_expands_provider_settings_roots`; `test_grepai_workspace_config_is_provider_owned_and_names_projects`; `test_grepai_root_gitignore_ignores_working_dir`; `test_grepai_root_gitignore_is_idempotent` | mcp/tests/test_context_providers.py:416-420; mcp/tests/test_context_providers.py:422-452; mcp/tests/test_context_providers.py:454-500; mcp/tests/test_context_providers.py:502-525; mcp/tests/test_context_providers.py:527-538; mcp/tests/test_context_providers.py:540-576 |
| Source artifact, patch idempotence, patch rejection, repo id, and patch id tests cover the remaining provider containment and patch helper edge cases, including the visualizer repo-query and route patches. | `test_detects_forbidden_source_provider_artifacts`; `test_cgc_cgcignore_patch_is_idempotent`; `test_cgc_timer_pop_patch_is_idempotent`; `test_cgc_delete_patch_is_idempotent`; `test_cgc_graph_builder_extensions_patch_is_idempotent`; `test_cgc_discovery_extensions_patch_is_idempotent`; `test_cgc_viz_repo_query_patch_is_idempotent`; `test_cgc_viz_server_route_patch_is_idempotent`; `test_cgc_viz_cli_route_patch_is_idempotent`; `test_patch_rejects_unexpected_source`; `test_stable_provider_id_never_returns_empty`; `test_patch_id_is_stable` | mcp/tests/test_context_providers.py:578-590; mcp/tests/test_context_providers.py:592-603; mcp/tests/test_context_providers.py:605-618; mcp/tests/test_context_providers.py:627-650; mcp/tests/test_context_providers.py:652-680; mcp/tests/test_context_providers.py:682-692; mcp/tests/test_context_providers.py:694-707; mcp/tests/test_context_providers.py:709-731; mcp/tests/test_context_providers.py:733-751; mcp/tests/test_context_providers.py:753-759; mcp/tests/test_context_providers.py:761-763; mcp/tests/test_context_providers.py:765-780 |
| The Windows-host container-path tests (`to_container_path`, driveless container roots, `env(for_container=True)`) sit between the first layout test and the pinned-defaults test. | `test_to_container_path_strips_windows_drive`; `test_cgc_container_paths_are_driveless_posix`; `test_cgc_container_env_is_posix_and_omits_windows_vars` | mcp/tests/test_context_providers.py:135-142; mcp/tests/test_context_providers.py:144-162; mcp/tests/test_context_providers.py:164-188 |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T18:15+02:00 — 260731-EFA-L6 curator W1-B06: anchored 7 Repo-Internal reference rows; scoped result 0 findings.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: both layout builders now take one value object
  — `cgc_runtime_layout(CgcRepo(...))` and `grepai_runtime_layout(GrepaiWorkspace(...))`, the
  latter renaming the caller-side `workspace_name` keyword to `name` while the layout attribute
  the tests read back keeps its old spelling — so the Logic section names both objects and that
  asymmetry. The rewrapped call sites shifted every test in the file, and all six own-file
  reference rows were re-verified against the current line numbers and re-anchored (for example
  the GrepAI row from L243-L420 to L416-L577 and the patch-helper row from L423-L726 to
  L578-L784); a row was added for the Windows-host container-path tests the table never covered.
  No test case or assertion changed.

- 2026-07-03T01:55+02:00 — L12: timer-pop patch idempotency test, patch-script drift guard, and the materialize test asserts the global/.cgcignore copy is byte-identical to the runtime-root copy.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-02T01:15+02:00: Replaced the mirror-sync and `.grepai/` artifact detection/removal tests with `ensure_grepai_root_gitignore` coverage (append/create/idempotent) and switched layout expansion expectations to live in-place roots (watch-live).
- 2026-05-29T07:19+02:00: Added coverage for `to_container_path`, driveless `container_runtime_root` / `container_code_repo_root` properties, and `env(for_container=True)` (driveless path values, omitted host-only Windows env) for Windows-host provider support.
- 2026-05-28T13:40+02:00: Updated after CGC layout tests removed host venv executable expectations, added stale `venvRoot` rejection coverage, and removed venv module lookup tests.
- 2026-05-28T12:32+02:00: Updated after GrepAI context layout tests moved operator logs under `logs/providers/grepai`.
- 2026-05-25T19:16+02:00: Updated after tests imported the direct `providers.context` facade and provider context implementation moved into `context_modules/`.
- 2026-05-24T19:25+02:00: Added coverage that CGC FalkorDB host/port defaults ignore ambient host `FALKORDB_*` environment variables.
- 2026-05-23T17:50+02:00: Moved onboarding to `mcp/tests` after the tests moved out of `runtime/skills/tests` and updated imports to the MCP package provider module.
- 2026-05-23T05:32+02:00: Updated provider layout expectations to `providers/runners` plus `providers/data`.
- 2026-05-21T23:18+02:00: Updated after adding GrepAI disposable root artifact removal coverage.
- 2026-05-21T13:22+02:00: Updated CGC patch tests for visualizer server route handling, CLI default-route propagation, CLI helper lookup, and the two new patch ids.
- 2026-05-21T12:40+02:00: Updated CGC patch tests for the visualizer repo-query patch, `viz/server.py` module lookup, and patch id stability.
- 2026-05-21T12:35+02:00: Updated GrepAI tests for provider-owned mirror-root expansion and mirror sync that excludes source `.grepai/` artifacts.
- 2026-05-21T12:20+02:00: Updated GrepAI workspace config test notes for explicit local Ollama endpoint and dimensions.
- 2026-05-21T11:50+02:00: Updated for GrepAI workspace-mode tests covering multi-root memory indexing, PostgreSQL data roots, provider-owned config, and `.grepai/` containment.
- 2026-05-21T02:10+02:00: Updated expected CGC backend data layout from provider-owned `_backends` to durable `provider-data/`.
- 2026-05-21T01:47+02:00: Updated for FalkorDB-only CGC layout, managed `.cgcignore` inheritance, missing-root rejection, stale runtime cleanup, GrepAI pin coverage, and the second CGC patch.
- 2026-05-20T19:11+02:00: Created onboarding for the provider layout and patch helper unit tests. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
