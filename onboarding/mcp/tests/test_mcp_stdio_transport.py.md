# mcp/tests/test_mcp_stdio_transport.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_mcp_stdio_transport.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixed subprocess boundary used by carryover. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:85-151 |
| The package-wide stdin guard that prevents reintroduction. | `test_every_subprocess_call_site_handles_stdin` | mcp/tests/test_subprocess_hygiene.py:44-66 |

## Update History

- 2026-08-02T21:29+02:00 — W2-B08 curator: anchored 4 citation findings to the shared `run_git` subprocess boundary and the package-wide stdin hygiene test. Verification metadata stays pinned until closeout.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/tests/test_mcp_stdio_transport.py` since the L2 base commit is the whole-tree `ruff format`
  pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever. Checked by
  parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-06-10T05:30+02:00: Created as the reproducing harness and permanent regression for GitHub #49 (2.5.1).
