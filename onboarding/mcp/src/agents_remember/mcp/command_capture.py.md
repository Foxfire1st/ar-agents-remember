# mcp/src/agents_remember/mcp/command_capture.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/command_capture.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `ddf6fcd5981664813c915e94e1c5229b542a28a4` |
| lastVerifiedCommitDate | 2026-05-24T00:25:39+02:00                 |
| governingOverview      | `../../../overview.md`                     |

## Purpose

`command_capture.py` adapts package-local command-style modules into structured
response payloads for the remaining script-facade bridge code.

## Code Commentary

### Logic

`run_package_main()` redirects stdout and stderr while calling an importable
`main(argv)` function. It returns `ok`, `operation`, `returncode`, `argv`,
captured streams, and parsed JSON payload when stdout is JSON. Current MCP
skill controllers call service functions directly; this helper remains only
where lower-level provider setup still bridges through `lifecycle.main`.

### Invariants And Boundaries

- This helper invokes importable package functions, not arbitrary shell command
  strings.
- It exists only for old behavior that still has command-shaped internals during
  the parity bridge; do not use it as the default controller pattern.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider setup still uses this helper while bridging to the provider lifecycle CLI facade. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |
| Skill controllers now call service-backed functions instead of returning command-capture payloads. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-05-25T19:16+02:00: Updated after lower-level provider setup command capture switched wording to the direct `providers.lifecycle` facade.
- 2026-05-24T00:37+02:00: Updated after worktree, memory, and benchmark MCP controllers stopped using command capture and moved to direct service results.
- 2026-05-23T13:09+02:00: Created for package-local command capture.
