# mcp/src/agents_remember/mcp/command_capture.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/command_capture.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:09+02:00                     |
| lastVerifiedCommitHash | `d445e83e7d28e3c34b15d8299d279d65ab9183b9` |
| lastVerifiedCommitDate | 2026-05-23T05:45:38+02:00                 |
| governingOverview      | `../../../overview.md`                     |

## Purpose

`command_capture.py` adapts package-local command-style modules into structured
MCP response payloads.

## Code Commentary

### Logic

`run_package_main()` redirects stdout and stderr while calling an importable
`main(argv)` function. It returns `ok`, `operation`, `returncode`, `argv`,
captured streams, and parsed JSON payload when stdout is JSON.

### Invariants And Boundaries

- This helper invokes importable package functions, not arbitrary shell command
  strings.
- It exists only for old behavior that still has command-shaped internals during
  the parity bridge.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Phase 04 facades use this helper for provider, worktree, memory, and benchmark command-shaped flows. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-05-23T13:09+02:00: Created for package-local command capture.
