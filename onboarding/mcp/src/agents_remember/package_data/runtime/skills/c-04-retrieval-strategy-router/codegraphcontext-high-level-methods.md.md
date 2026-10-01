# c-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

This sibling reference teaches agents what CodeGraphContext can do after `c-04-retrieval-strategy-router` skill
selects the `Relationship` substrate. It documents typed MCP CGC tools and
synthetic output shapes so agents do not treat CGC as only a file-line locator
and do not request the removed generic `cgc_query` facade.

## Code Commentary

### Logic

The document starts with the typed MCP provider contract and maps common
relationship questions to `cgc_symbol_search`, `cgc_callees`, `cgc_callers`,
`cgc_dependencies`, `cgc_complexity`, and `cgc_visualize`.
Its native-operation table records `cgc_dependencies` as the current
CodeGraphContext `analyze deps <module>` command shape.

Each method section gives a placeholder MCP request and a synthetic output
shape. The examples cover symbol location, downstream calls, reverse callers,
module import neighborhoods, and complexity signals without exposing private
repository names, symbols, paths, or code.

### Conventions

Run examples through typed MCP provider tools:

```text
cgc_callers(repo_id="<repoId>", function="<function>", file="<optional path>")
```

Provider authority comes from MCP settings. Pass `file` to `cgc_callers` when a
symbol name is common, overloaded, or implemented in many places. For
`cgc_dependencies`, use the module import string recorded in code, not
necessarily the source file path.

### Invariants And Boundaries

CGC output is discovery, not proof. Use it to choose source anchors and narrow
relationship neighborhoods, then confirm contracts and edit direction with
bounded source reads. Native CGC operations not listed in this document are not
public MCP tools yet; add a typed MCP tool before teaching skills to request
one of those operations.

### Todos

None.

## Evidence

### Docs References

No external documentation is cited here. The document records verified local CGC
command shapes from the managed provider wrapper, then presents only synthetic
example outputs.

No relevant external documentation found.

### Repo-Internal References

- The CGC catalog states the typed MCP tool contract and says generic `cgc_query` is removed. [1]
- Symbol search, callees, callers, dependencies, and complexity sections show placeholder tool calls and synthetic output shapes. [2]
- Practical rules explain when to use each typed CGC tool and require source confirmation before edits. [3]
- The `c-04-retrieval-strategy-router` skill links agents to this catalog from the Relationship section. [4]

### Cross-Repo References

The example outputs are synthetic response-shape illustrations. They do not
contain private sibling repository names, symbols, paths, or code.

No source-code contract is imported from a sibling repository.
