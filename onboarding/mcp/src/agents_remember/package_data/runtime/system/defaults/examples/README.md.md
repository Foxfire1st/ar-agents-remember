# README.md

## Purpose

`mcp/src/agents_remember/package_data/runtime/system/defaults/examples/README.md` explains why system examples are split into target-shaped folders instead of encoded through file names.

## Code Commentary

### Logic

The file defines two example targets: `examples/coordinator/` for workspace-wide
coordinator files and `examples/memory-repo/` for repository-specific
memory-layer files. It states that coordinator files can define global defaults
but should not encode one-repository rules, while memory-layer rules win for
their own repository. It also notes that the memory-repo examples include a
`git-workflow.md` landing-flow starter (for repos that land through a gated
branch) and a code quality report template for implementation validation summaries.

### Conventions

Examples are arranged by destination folder shape so users can copy a whole directory and preserve normal target file names such as `AGENTS.md`, `settings.md`, and `tools.md`.

### Invariants And Boundaries

Coordinator guidance is global by default; memory-repo guidance is more
specific and overrides it for the target code repository. The packaged report
template is example scaffolding and should be adapted to the target
repository's actual quality tools.

### Todos

None.

### Docs References

No external documentation is needed for this example index.

No relevant external documentation found.

## Evidence

### Repo-Internal References

The source file itself is the active example index.

- The README states that examples are split by target folder rather than by inferred ownership from file names. [1]
- The README defines coordinator examples as workspace-wide/global, memory-repo examples as repository-specific, and names the memory-repo `git-workflow.md` landing-flow starter and quality-report template. [2]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.
