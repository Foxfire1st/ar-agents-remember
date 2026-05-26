# Task: GrepAI MCP Search Tool Shape

**Status:** planning
**Repo:** agents-remember-md
**Type:** Code
**Created:** 2026-05-26T14:39

---

## Objective

Fix the Agents Remember MCP GrepAI tools so agents can query the managed memory workspace directly through MCP instead of falling back to Docker CLI. The search tool should support workspace-wide memory search by default and explicit multi-repo filtering for cross-repo relationship discovery.

---

## Requirements

- `grepai_search` must run against the configured GrepAI workspace, not the current shell/project directory.
- Calling `grepai_search(query=..., dry_run=false)` with no repo filter must search all indexed memory projects in the configured workspace.
- Calling `grepai_search(..., repo_ids=[...])` must restrict search to the matching GrepAI projects and pass one `--project` flag per repo/project.
- The tool should expose a small result-shaping surface needed by agents, at least `limit` and an output mode such as JSON or TOON.
- Unknown repo/project ids should fail clearly before invoking GrepAI; this validation is necessary because otherwise the tool can silently query the wrong scope or return misleading empty results.
- `grepai_trace` must be reshaped from a free-form `query` wrapper into the CLI's actual trace contract, with an explicit trace action such as `callers`, `callees`, or `graph`.
- Tests must cover dry-run command construction and at least one non-dry-run-capable command path with workspace and project flags.
- Runtime skill/docs snippets that teach agents to call GrepAI MCP must be updated to show workspace-wide and multi-repo search.

---

## Implementation Steps

### S1 - Confirm Current Tool And Provider Contracts

- [ ] Map the current MCP GrepAI call path and CLI contract.
  - [ ] Inspect `mcp/src/agents_remember/mcp/server.py`, `mcp/src/agents_remember/mcp/tools.py`, `mcp/src/agents_remember/controllers/skill_tools.py`, and GrepAI lifecycle run helpers.
  - [ ] Confirm how configured GrepAI roots map configured repo ids to stable GrepAI project ids.
  - [ ] Record any conflict with the already-running provider compose/dockerization work before editing shared lifecycle files.
  - [ ] Verification: dry-run the current failing MCP command shape and the known-good CLI shape as comparison evidence.

### S2 - Add Workspace And Project Selection To `grepai_search`

- [ ] Update the MCP search tool schema and payload path.
  - [ ] Add `repo_ids: list[str] | None`, `all_repos: bool`, `limit: int`, and `output_format: str` arguments through `server.py`, `tools.py`, and `skill_tools.py`.
  - [ ] Resolve the GrepAI workspace name and valid project ids from generated provider lifecycle settings.
  - [ ] Build `grepai search <query> --workspace <workspace> --limit <limit> --json|--toon` plus repeated `--project <project>` flags when `repo_ids` is supplied.
  - [ ] Keep the default no-filter behavior workspace-wide so cross-repo memory discovery works without the caller guessing every project id.
  - [ ] Verification: focused tests prove default workspace-wide command construction and explicit multi-repo command construction.

### S3 - Reshape `grepai_trace`

- [ ] Replace the free-form trace wrapper with an explicit trace API.
  - [ ] Add a `trace_action` argument constrained to GrepAI's trace subcommands, plus `symbol`, optional `repo_ids`, `all_repos`, `depth`, and `output_format` only where the CLI supports them.
  - [ ] Build commands such as `grepai trace callers <symbol> --workspace <workspace> --project <project>`.
  - [ ] Do not add compatibility aliases for the old `query` shape unless the developer explicitly asks for migration support; the current project is pre-1.0 and the wrong shape is newly discovered slop.
  - [ ] Verification: focused tests cover at least one valid trace action and one invalid trace action.

### S4 - Update Tests And Runtime Guidance

- [ ] Update the test suite and package guidance.
  - [ ] Add/adjust unit tests in `mcp/tests/test_tools.py` or the nearest provider-tool test file for the new MCP payload shape.
  - [ ] Update runtime examples under `mcp/src/agents_remember/package_data/runtime/...` that currently show `grepai_search(query="<query>", dry_run=false)` without scope/result arguments.
  - [ ] Run focused checks from the source repo root: `python -m pytest mcp/tests/test_tools.py -q` and `python -m ruff check` on touched Python files.
  - [ ] Verification: document the exact MCP calls that should replace the Docker CLI workaround.

### S5 - Refresh Onboarding For Changed Behavior

- [ ] Update memory through the approved onboarding path after code changes.
  - [ ] Use `C-05-create-or-update-onboarding-files` for changed source and runtime guidance files.
  - [ ] Capture the durable finding that GrepAI workspace-only search spans all indexed memory projects while `--project` filters selected repos.
  - [ ] Verification: rerun `context_packet(repo_id="agents-remember-md", include_providers=true)` and real `grepai_search` MCP calls for all-repo and multi-repo cases.

---

## Proposed Code Examples

### E1 - Search Tool Schema And Command Construction

Distinct change covered: MCP schema expansion plus workspace/project-aware command construction.

Why this example is included: this is the core behavior change that removes the Docker CLI workaround and makes workspace-wide search the default power move.

```python
def grepai_search_tool(
    config: McpRuntimeConfig,
    *,
    query: str,
    repo_ids: list[str] | None = None,
    all_repos: bool = True,
    limit: int = 10,
    output_format: str = "json",
    dry_run: bool = True,
    timeout: int | None = None,
) -> dict[str, Any]:
    selection = grepai_project_selection(config, repo_ids=repo_ids, all_repos=all_repos)
    native_args = ["search", query, "--workspace", selection.workspace, "--limit", str(limit)]
    native_args.append("--toon" if output_format == "toon" else "--json")
    for project_id in selection.project_ids:
        native_args.extend(["--project", project_id])
    return _provider_operation_result(
        config,
        operation="grepai_search",
        dry_run=dry_run,
        timeout=timeout,
        run=lambda service_config: lifecycle_service.run_grepai_lifecycle(
            service_config,
            action="run",
            native_args=native_args,
        ),
    )
```

### E2 - Trace Tool Shape

Distinct change covered: `grepai_trace` becomes an explicit trace-subcommand wrapper instead of passing an invalid free-form query.

Why this example is included: the current wrapper can return help text successfully while not performing the requested trace, so the shape must make invalid calls hard to express.

```python
def grepai_trace_tool(
    config: McpRuntimeConfig,
    *,
    trace_action: str,
    symbol: str,
    repo_ids: list[str] | None = None,
    all_repos: bool = True,
    dry_run: bool = True,
    timeout: int | None = None,
) -> dict[str, Any]:
    if trace_action not in {"callers", "callees", "graph"}:
        raise ValueError("grepai_trace trace_action must be callers, callees, or graph")
    selection = grepai_project_selection(config, repo_ids=repo_ids, all_repos=all_repos)
    native_args = ["trace", trace_action, symbol, "--workspace", selection.workspace]
    for project_id in selection.project_ids:
        native_args.extend(["--project", project_id])
    return _provider_operation_result(
        config,
        operation="grepai_trace",
        dry_run=dry_run,
        timeout=timeout,
        run=lambda service_config: lifecycle_service.run_grepai_lifecycle(
            service_config,
            action="run",
            native_args=native_args,
        ),
    )
```

### E3 - User-Facing MCP Calls

Distinct change covered: expected agent-facing usage examples.

Why this example is included: the runtime skill/docs examples are part of the tool contract agents will copy.

```text
grepai_search(
  query="battery test PSU",
  all_repos=true,
  limit=5,
  output_format="json",
  dry_run=false,
)

grepai_search(
  query="battery test PSU",
  repo_ids=["device-management", "dema-platform-backend", "TAS-Expand"],
  limit=5,
  output_format="json",
  dry_run=false,
)
```

---

## Decision Log

| Date-Time          | Decision | Rationale |
| ------------------ | -------- | --------- |
| 2026-05-26T14:39 | Create a focused light task for GrepAI MCP tool shape. | The provider is healthy and queryable through CLI, but the MCP wrapper omits workspace/project arguments and therefore fails real search. |
| 2026-05-26T14:39 | Default `grepai_search` to workspace-wide search when no repo filter is supplied. | The managed GrepAI ingestion already indexes memory repos as projects inside one workspace; workspace-wide search is the useful default for cross-repo relationship discovery. |
| 2026-05-26T14:39 | Keep explicit multi-repo filtering via `repo_ids`. | Scoped search remains important for precision and for comparing related repositories without scanning the whole memory workspace. |
| 2026-05-26T14:39 | Do not silently preserve the old `grepai_trace(query=...)` shape. | The old shape maps poorly to GrepAI's trace subcommands and can produce help output instead of a useful query; the project should avoid pre-1.0 compatibility slop. |

---

## Open Questions

- Should `repo_ids` accept only configured Agents Remember repo ids, only GrepAI project ids, or both with normalization to stable project ids?
- Should `output_format` default to JSON for machine parsing or TOON for token economy?
- Should the first implementation include real MCP integration smoke tests, or keep verification at unit tests plus manual MCP calls because the provider containers are environment-dependent?

---

## References

- `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/mcp/server.py`
- `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/mcp/tools.py`
- `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py`
- `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/actions.py`
- `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/grepai/context/layout.py`
- `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/grepai-high-leverage-usage.md`
- Current observed failure: `grepai_search(query=..., dry_run=false)` invokes `grepai search <query>` and fails with `no grepai project found`.
- Current observed success: `grepai search <query> --workspace agents-remember-memory` searches all indexed memory projects; repeated `--project` flags restrict search to selected projects.
