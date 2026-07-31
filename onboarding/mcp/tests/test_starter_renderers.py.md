# test_starter_renderers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_starter_renderers.py`      |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-06T18:19+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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
- Hook smoke tests only execute Python hook scripts; they do not launch Codex,
  Claude Code, Cursor, VS Code, or any other harness.
- Missing repository paths must fail before writing a silently-invalid starter
  package.

### Todos

After closeout commits this new source file, refresh verification metadata to
the committed source revision.

## Docs References

No external documentation is needed for this repository-local renderer test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Harness cases cover copied starter folders, rendered settings files, rendered placeholder-free files, and optional hook smoke scripts. | L15-L126 | [test_starter_renderers.py](agents-remember/mcp/tests/test_starter_renderers.py) |
| `render_case()` creates temporary repository roots, copies starter folders, invokes the harness-local renderer, and passes a duplicate repo argument to prove output de-duplication. | L129-L158 | [test_starter_renderers.py](agents-remember/mcp/tests/test_starter_renderers.py) |
| Shared assertions verify MCP root settings, absence of placeholders, hook smoke output, and rendered Python command shapes for Codex, Claude Code, Cursor, and VS Code/Copilot. | L161-L249 | [test_starter_renderers.py](agents-remember/mcp/tests/test_starter_renderers.py) |
| The missing-repository test requires the renderer to fail explicitly when a requested repository root is absent. | L250-L269 | [test_starter_renderers.py](agents-remember/mcp/tests/test_starter_renderers.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/tests/test_starter_renderers.py` and moved the lines this card cites, so the Citations
  column no longer pointed at the code its rows name. Corrected the ranges (L161-L239 → L161-L249;
  L242-L263 → L250-L269). The behaviour described is unchanged — the file's AST is identical to
  the base revision — this is a citation repair only. The second row's recorded end (L263) already
  ran past the end of the base revision (259 lines), so it was re-derived from the test's real
  bounds rather than shifted. Verification metadata pinned until closeout stamps the L2 commit.

- 2026-06-06T18:19+02:00: Updated after renderer tests switched from a separate workspace-root argument plus repeated repo flags to one inferred-workspace `--repo` list. Verification metadata remains pending until closeout creates the source commit.
- 2026-06-06T17:27+02:00: Created onboarding for the new harness starter renderer regression tests. Verification metadata remains pending until closeout creates the source commit.
