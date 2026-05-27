# mcp/tests/test_provider_workflow_integration.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_provider_workflow_integration.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-27T18:10:12+02:00                  |
| lastVerifiedCommitHash | `f20f75e3e3c6da0c56a6ccfdedfa9d859d7329b7`                         |
| lastVerifiedCommitDate | 2026-05-27T18:11:35+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_provider_workflow_integration.py` is the Docker-backed end-to-end provider workflow test for source, worktree-local, and benchmark-local provider instances.

## Code Commentary

### Logic

The test is skipped unless `AGENTS_REMEMBER_PROVIDER_INTEGRATION=1` is set. When enabled, it creates temporary code and external-memory repositories, writes MCP settings with a unique provider instance id, prepares the source providers, starts a worktree through the MCP tool path, verifies worktree-local provider settings and watcher status, prepares benchmark-local providers using the benchmark registration path, verifies watcher status again, and finally removes the generated provider containers and networks.

### Invariants And Boundaries

- The test is intentionally Docker-gated because it starts real GrepAI, Postgres, Ollama, CGC watcher, and FalkorDB resources.
- It uses unique instance ids and cleans resources derived from generated provider settings so it does not touch the developer's normal provider containers.
- The test proves workflow-level behavior through public setup/tool entry points, not private helper-only assertions.
- Keep this test focused on provider workflow compatibility; unit tests should continue to cover pure parsing and render details.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider setup is the public service path used to prepare source providers. | [../src/agents_remember/providers/provider_setup.py](../src/agents_remember/providers/provider_setup.py.md) |
| Worktree start is exercised through `worktree_start_tool`, which writes isolated provider state. | [../src/agents_remember/worktrees/modules/start.py](../src/agents_remember/worktrees/modules/start.py.md) |
| Benchmark provider setup is exercised through the benchmark runner registration/setup path. | [../src/agents_remember/benchmarks/runner_modules/mcp_registration.py](../src/agents_remember/benchmarks/runner_modules/mcp_registration.py.md) |
| Focused provider setup tests cover the same settings and seed behavior without Docker. | [test_provider_setup.py](test_provider_setup.py.md) |

## Update History

- 2026-05-27T18:10:12+02:00: Created for Docker-backed worktree and benchmark provider workflow validation.
