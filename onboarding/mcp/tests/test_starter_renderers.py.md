# test_starter_renderers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_starter_renderers.py`      |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-30T22:33:39+02:00                     |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `../../overview.md`                        |

## Purpose

`test_starter_renderers.py` verifies that each copied harness starter package
can render its local placeholders, repository settings, and executable hook
commands for a concrete workspace.

## Code Commentary

### Logic

The test defines a shared set of repository ids and placeholder tokens, then
enumerates harness cases for Codex, Claude Code, Cursor, VS Code/Copilot,
Antigravity, OpenClaw, Hermes, and Pi. Each case records the source starter
folder, copied target folder, rendered settings file, rendered files that must
be placeholder-free, and an optional hook script to smoke-test.

`render_case()` creates a temporary workspace, creates two repository
directories, copies the relevant starter package, copies any paired config
folder required by the harness, and runs that harness's local
`render-starter.py` with a single `--repo` list. The duplicate repository value
in that list proves the renderer's output de-duplicates repository ids while
preserving the intended order. Shared assertions then verify MCP settings roots,
absence of unresolved placeholders, command rendering, and hook smoke output.
For Codex, the rendered MCP registration must also retain exact forwarding of
`AR_HOSTED_SESSION_ID` and `AR_SPAWN_ROLE`.
The missing-repository test runs the Codex renderer against an absent repo id
and requires a non-zero exit plus an explicit `repository root does not exist`
error.

### Invariants And Boundaries

- The tests exercise copied starter packages in temporary workspaces, not the
  developer's live harness folders.
- Rendered MCP settings must include deterministic `coordinationRoot`,
  `workspaceRoot`, `transcriptRoot`, and repository id ordering.
- Generated executable hook commands must use the current Python interpreter
  selected at render time.
- Rendered Codex MCP settings must forward exactly the hosted-seat and spawn-role lifecycle
  variables needed to preserve ambient versus hosted routing.
- Hook smoke tests only execute Python hook scripts; they do not launch Codex,
  Claude Code, Cursor, VS Code, or any other harness.
- Missing repository paths must fail before writing a silently-invalid starter
  package.

### Todos

After closeout commits this new source file, refresh verification metadata to
the committed source revision.

## Docs References

No external documentation is needed for this repository-local renderer test.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Harness cases cover copied starter folders, rendered settings files, rendered placeholder-free files, and optional hook smoke scripts. | `test_starter_renderers_fill_placeholders_and_settings` | mcp/tests/test_starter_renderers.py:238-247 |
| `render_case()` creates temporary repository roots, copies starter folders, invokes the harness-local renderer, and passes a duplicate repo argument to prove output de-duplication. | `render_case` | mcp/tests/test_starter_renderers.py:137-156 |
| Shared assertions verify MCP root settings, absence of placeholders, hook smoke output, and rendered Python command shapes for Codex, Claude Code, Cursor, and VS Code/Copilot. | `assert_no_placeholders` | mcp/tests/test_starter_renderers.py:169-173 |
| The missing-repository test requires the renderer to fail explicitly when a requested repository root is absent. | `test_starter_renderer_rejects_missing_repository` | mcp/tests/test_starter_renderers.py:250-269 |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-30T22:33:39+02:00 — 260821-ARSPAWN-L5 recorded exact Codex lifecycle-variable
  forwarding in copied starter output. Verification remains closeout-owned.

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 8 citation findings; scoped check passed.

- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/tests/test_starter_renderers.py` and moved the lines this card cites, so the Citations
  column no longer pointed at the code its rows name. Corrected the ranges (L161-L239 → L161-L249;
  L242-L263 → L250-L269). The behaviour described is unchanged — the file's AST is identical to
  the base revision — this is a citation repair only. The second row's recorded end (L263) already
  ran past the end of the base revision (259 lines), so it was re-derived from the test's real
  bounds rather than shifted. Verification metadata pinned until closeout stamps the L2 commit.

- 2026-06-06T18:19+02:00: Updated after renderer tests switched from a separate workspace-root argument plus repeated repo flags to one inferred-workspace `--repo` list. Verification metadata remains pending until closeout creates the source commit.
- 2026-06-06T17:27+02:00: Created onboarding for the new harness starter renderer regression tests. Verification metadata remains pending until closeout creates the source commit.
