# mcp/tests/test_mcp_stdio_transport.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_mcp_stdio_transport.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00                     |
| lastVerifiedCommitHash | `642cca15f206cf8cf43ff7ffd6dadc5c27af2879`|
| lastVerifiedCommitDate | 2026-06-10T01:44:33+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

End-to-end stdio transport tests for hang-prone MCP tools: spawns the real
server over real pipes (the same topology as a harness) and asserts tool calls
complete within a bound. Born from GitHub #49, where `memory_carryover_plan`
hung 6–8 minutes via MCP while the identical function ran in 2.6s directly.

## Code Commentary

### Logic

`call_tool_over_stdio` launches `python -m agents_remember.mcp --config <tmp
settings>` through `mcp.client.stdio`, initializes a `ClientSession`, and calls
the tool under `asyncio.wait_for` bounds. `build_carryover_fixture` reuses the
worktree-support git helpers to build a code repo with a landed branch, an
official memory repo, and an in-coordination source memory tree, so the plan
has a real auto-carry candidate. A `ping` test proves the harness itself.

### Invariants And Boundaries

- This harness is the regression proof for #49: pre-fix it reproduced the hang
  (120s timeout, server stuck after `CallToolRequest`); post-fix it passes in
  ~3.4s. Keep it wired to real subprocess pipes — an in-process client would
  not exercise the inherited-descriptor failure mode.
- `source_memory` must live inside the coordination root
  (`require_within_coordination`).

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The fixed subprocess call site. | [carryover.py](agents-remember/mcp/src/agents_remember/memory/carryover.py) |
| The package-wide stdin guard that prevents reintroduction. | [test_subprocess_hygiene.py](agents-remember/mcp/tests/test_subprocess_hygiene.py) |

## Update History

- 2026-06-10T05:30+02:00: Created as the reproducing harness and permanent regression for GitHub #49 (2.5.1).
