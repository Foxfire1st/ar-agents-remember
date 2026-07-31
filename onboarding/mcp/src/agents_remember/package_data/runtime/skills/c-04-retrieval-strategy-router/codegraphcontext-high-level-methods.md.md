# c-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                     |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`             |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `../../../../../../../overview.md`                              |

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

## Docs References

No external documentation is cited here. The document records verified local CGC
command shapes from the managed provider wrapper, then presents only synthetic
example outputs.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The CGC catalog states the typed MCP tool contract and says generic `cgc_query` is removed. | L1-L42 | [codegraphcontext-high-level-methods.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md) |
| Symbol search, callees, callers, dependencies, and complexity sections show placeholder tool calls and synthetic output shapes. | L44-L175 | [codegraphcontext-high-level-methods.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md) |
| Practical rules explain when to use each typed CGC tool and require source confirmation before edits. | L174-L184 | [codegraphcontext-high-level-methods.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md) |
| The `c-04-retrieval-strategy-router` skill links agents to this catalog from the Relationship section. | L107-L111 | [`c-04-retrieval-strategy-router` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md) |

## Cross-Repo References

The example outputs are synthetic response-shape illustrations. They do not
contain private sibling repository names, symbols, paths, or code.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No source-code contract is imported from a sibling repository. | n/a | n/a |

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 line citation. The catalog is 184 lines,
  so the Practical Rules row's L177-L185 ran past the end; the `## Practical Rules` section now reads
  L174-L184 (five bullets, ending on the "Treat CGC output as discovery, not proof" source-confirmation
  rule). Verified by reading the file tail.
- 2026-07-02T15:40+02:00 — Updated the CGC dependency-method catalog to document
  the current native command shape as `analyze deps <module>`.
- 2026-05-29T20:25+02:00: Reviewed for the act-by-default `dry_run` flip — the CGC query examples dropped the now-redundant `dry_run=false` (queries return results by default; `dry_run=true` returns the planned command without executing it).
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-23T21:25+02:00: Simplified provider-authority wording in the CGC tool guidance.
- 2026-05-23T20:42+02:00: Replaced generic `cgc_query` guidance with typed CGC tool guidance.
- 2026-05-23T13:46+02:00: Updated examples to use MCP `cgc_query` instead of the deleted source provider lifecycle script.
- 2026-05-21T15:20+02:00: Replaced private-project examples with synthetic response-shape examples.
- 2026-05-21T14:10+02:00: Created onboarding for the CGC high-level methods catalog.
