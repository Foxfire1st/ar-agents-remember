# mcp/tests/test_provider_workflow_integration.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_workflow_integration.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `4728fa846d20cffd3f25c34e072e41920b49461e`                         |
| lastVerifiedCommitDate | 2026-06-19T14:22:14+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_provider_workflow_integration.py` is the Docker-backed end-to-end provider workflow test for source, worktree-local, and benchmark-local provider instances.

## Code Commentary

### Logic

The test is skipped unless `AGENTS_REMEMBER_PROVIDER_INTEGRATION=1` is set. When enabled, it creates temporary code and external-memory repositories, writes MCP settings with a unique provider instance id, prepares the source providers, starts a worktree through the MCP tool path, verifies worktree-local provider settings and watcher status, prepares benchmark-local providers using the (now hermetic, no-seed) benchmark registration path, verifies watcher status again, and finally removes the generated provider containers and networks.

The helper parsing now uses small typed dictionary/list adapters so Pyright can
check nested provider settings traversal without relying on broad untyped-dict
coercion. `worktree_start_tool` is imported from the split
`controllers.worktree_tools` module rather than the former `skill_tools`
facade.

The worktree start assertions follow the async contract (GitHub #53): the
tool returns providers `starting` plus a progressFile, the test polls
`read_setup_progress` to a terminal state within the provider timeout, and
reads the provider-state file from the finish summary's `providerStateFile`.

### Invariants And Boundaries

- The test is intentionally Docker-gated because it starts real GrepAI, Postgres, Ollama, CGC watcher, and FalkorDB resources.
- It uses unique instance ids and cleans resources derived from generated provider settings so it does not touch the developer's normal provider containers.
- The test proves workflow-level behavior through public setup/tool entry points, not private helper-only assertions.
- Keep this test focused on provider workflow compatibility; unit tests should continue to cover pure parsing and render details.
- Keep helper casts narrow and local to raw JSON/settings adapter boundaries.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider setup is the public service path used to prepare source providers. | [../src/agents_remember/providers/provider_setup.py](../src/agents_remember/providers/provider_setup.py.md) |
| Worktree start is exercised through the split `worktree_start_tool`, which writes isolated provider state. | [../src/agents_remember/controllers/worktree_tools.py](../src/agents_remember/controllers/worktree_tools.py.md) |
| Benchmark provider setup is exercised through the benchmark runner registration/setup path. | [../src/agents_remember/benchmarks/runner_modules/mcp_registration.py](../src/agents_remember/benchmarks/runner_modules/mcp_registration.py.md) |
| Focused provider setup tests cover the same settings and seed behavior without Docker. | [test_provider_setup.py](test_provider_setup.py.md) |

## Update History

- 2026-06-19T13:42: The benchmark `prepare_configured_providers` call dropped its seed kwargs to match the hermetic-cold benchmark API; the Docker-gated workflow now exercises a cold benchmark provider build (task 260619).
- 2026-06-10T07:30+02:00 — Worktree start assertions updated for async provider setup (GitHub #53): the tool returns providers `starting` + progressFile; the test now polls `read_setup_progress` to a terminal state and reads the provider-state file from the finish summary.
- 2026-05-30T21:51+02:00: Re-verified against `825a172`; the only change was the MCP settings fixture adopting the renamed `timeoutCaps.providerSetupSeconds` key. Test behavior unchanged.
- 2026-05-28T19:52+02:00: Updated after Pyright-oriented helper adapters and split worktree controller imports replaced the old `skill_tools` import.
- 2026-05-27T18:10:12+02:00: Created for Docker-backed worktree and benchmark provider workflow validation.
