# mcp/src/agents_remember/controllers/provider_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/provider_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-30T21:33+02:00                     |
| lastVerifiedCommitHash | `825a172bdf0d4ee3489ae25dbcc19c4e9c7b9493` |
| lastVerifiedCommitDate | 2026-05-30T17:31:45+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`provider_tools.py` is the controller surface for provider status,
diagnostics, watcher lifecycle, GrepAI search/trace, and CodeGraphContext MCP
tools.

## Code Commentary

Status and diagnostics delegate to `providers.status`. Watcher actions route
through provider lifecycle services and write current provider state when a
real status/refresh result is produced. GrepAI helpers validate configured repo
scope, workspace/project selection, output format, trace action, and numeric
limits before calling `lifecycle_service.run_grepai_lifecycle()`. CGC helpers
construct fixed native argument vectors for typed code-relationship operations
before calling `lifecycle_service.run_cgc_lifecycle()`.

## Invariants And Boundaries

- Provider callers may name configured repo IDs and typed options, not
  arbitrary provider roots or generic native command strings.
- `provider_diagnostics` is the detail tool for raw provider state; normal
  context-facing provider status stays compact.
- Provider runner integrity failures should return structured recovery actions
  instead of proceeding into lifecycle execution.
- `provider_watchers_tool` and the `cgc_*`/`grepai_*` query controllers default
  `dry_run=False` (act-by-default): a plain query returns results and
  `dry_run=true` returns the planned provider command without executing it.
  `provider_watchers` still forces a live path for `action="status"`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider summary and diagnostics projection live in the provider status module. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Provider response models distinguish compact summaries from diagnostics/native payloads. | [providers.py](agents-remember-md/mcp/src/agents_remember/models/providers.py) |
| MCP payload builders validate this controller output through the model registry. | [tools/providers.py](agents-remember-md/mcp/src/agents_remember/mcp/tools/providers.py) |

## Update History

- 2026-05-30T21:33+02:00: Re-verified against `825a172` after the provider dockerization / never-cap-indexing run; the controller surface (status, diagnostics, watchers, GrepAI search/trace, typed CGC tools) and its act-by-default `dry_run` behavior still match. Repaired the builder reference — provider payload builders now live in `tools/providers.py` after the `01f503d` `mcp/tools.py` split.
- 2026-05-28T19:52+02:00: Created when provider MCP behavior moved out of the former `skill_tools.py` mega-facade.
