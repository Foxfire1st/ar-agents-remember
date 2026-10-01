# tools.md

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

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The memory-repo tools example says it belongs in memory-layer `system/tools.md`, can carry branch workflow notes/checks/code-quality commands, and should point implementation reporting at a project-adjusted quality report template. [1]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.
