# tools.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/tools.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|

## Purpose

This example is the tools starter for a memory layer.

## Code Commentary

### Logic

The file tells users to copy the example to memory-layer `system/tools.md` and
use it for CLI commands, MCPs, code quality tools, branch workflow notes, and
checks that agents should reference for the target code repository. The
code-quality subsection explicitly asks for repo-specific lint, format,
typecheck, test, build, and smoke-check commands.

### Conventions

Repo-specific validation, code quality, and branch workflow guidance belongs
here, not in coordinator tools.

### Invariants And Boundaries

Coordinator tools may set global defaults, but memory-layer tools are the authority for repository-specific commands.

### Todos

None.

### Docs References

No external documentation is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The memory-repo tools example says it belongs in memory-layer `system/tools.md` and can carry branch workflow notes, checks, and code quality commands. | L1-L17 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/tools.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/tools.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-23T21:25+02:00: Added explicit code-quality command guidance to the memory-repo tools example.
- 2026-05-13T13:38: Created onboarding for the memory-repo tools example.
