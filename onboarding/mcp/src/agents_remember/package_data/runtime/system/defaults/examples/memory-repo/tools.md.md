# tools.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/tools.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T12:32+02:00                     |
| lastVerifiedCommitHash | `3f09b75461760479b443f1b04b180772724e7a24` |
| lastVerifiedCommitDate | 2026-05-28T15:10:01+02:00|

## Purpose

This example is the tools starter for a memory layer.

## Code Commentary

### Logic

The file tells users to copy the example to memory-layer `system/tools.md` and
use it for CLI commands, MCPs, code quality tools, branch workflow notes, and
checks that agents should reference for the target code repository. The
code-quality subsection explicitly asks for repo-specific lint, format,
typecheck, test, build, and smoke-check commands. It now also points
implementation reporting at a project-adjusted copy of
`system/code-quality-report-template.md` and tells agents to include actual tool
findings instead of just saying checks ran.

### Conventions

Repo-specific validation, code quality, and branch workflow guidance belongs
here, not in coordinator tools.

### Invariants And Boundaries

Coordinator tools may set global defaults, but memory-layer tools are the
authority for repository-specific commands. The packaged quality-report wording
is an example; each memory layer should adapt it to the repository's real
validation stack.

### Todos

None.

### Docs References

No external documentation is needed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The memory-repo tools example says it belongs in memory-layer `system/tools.md`, can carry branch workflow notes/checks/code-quality commands, and should point implementation reporting at a project-adjusted quality report template. | `# Tools Example` | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/tools.md:1-24 |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-28T12:32+02:00: Updated after the tools example began instructing agents to report implementation quality findings through an adapted report template.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-23T21:25+02:00: Added explicit code-quality command guidance to the memory-repo tools example.
- 2026-05-13T13:38: Created onboarding for the memory-repo tools example.
