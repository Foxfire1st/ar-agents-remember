# C-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-23T13:46+02:00                                 |
| lastVerifiedCommitHash | `5ff4ed4ef94b5576a45059de8ac7c03e8c4c04a1`             |
| lastVerifiedCommitDate | 2026-05-21T18:12:00+02:00|
| governingOverview      | `../../overview.md`                                    |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

This sibling reference teaches agents what CodeGraphContext can do after C-04
selects the `Relationship` substrate. It documents high-level `cgc analyze`
methods with synthetic MCP `cgc_query` shapes and example outputs so agents do
not treat CGC as only a file-line locator.

## Code Commentary

### Logic

The document starts with the MCP provider tool contract and makes the central
distinction: `find name` locates candidate symbols, while high-level `analyze`
methods expose relationships. The method chooser maps common
relationship questions to commands: calls, callers, chain, deps, tree,
complexity, dead-code, overrides, variable, and kotlin-call-audit.

Each method section gives a placeholder MCP request and a synthetic output shape.
The examples cover downstream calls, reverse callers, multi-hop call chains,
module import neighborhoods, inheritance plus attached methods, complexity
rankings, unused-code candidates, implementations of a shared method name,
variable occurrences, and Kotlin call ambiguity coverage without exposing
private repository names, symbols, paths, or code.

### Conventions

Run all examples through the MCP provider tool:

```text
cgc_query(repo_id="<repoId>", query_type="<cgc command>", arguments=[...])
```

Provider authority comes from MCP settings. Add `--file` in the native argument
list when a symbol name is common, overloaded, or implemented in many places.
For `deps`, use the module import string recorded in code, not necessarily the
source file path.

### Invariants And Boundaries

CGC output is discovery, not proof. Use it to choose source anchors and narrow
relationship neighborhoods, then confirm contracts and edit direction with
bounded source reads. `dead-code` is especially provisional because framework
entry points, event callbacks, and dynamic calls can look unused.

`kotlin-call-audit` is useful only when the indexed repository actually contains
Kotlin graph nodes. In a non-Kotlin repo it is a coverage check rather than a
relationship retrieval method.

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
| The CGC catalog states the managed wrapper command, explains that high-level methods expose relationships beyond `find name`, and requires synthetic examples only. | L1-L23 | [codegraphcontext-high-level-methods.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md) |
| The method chooser maps relationship questions to `calls`, `callers`, `chain`, `deps`, `tree`, `complexity`, `dead-code`, `overrides`, `variable`, and `kotlin-call-audit`. | L25-L38 | [codegraphcontext-high-level-methods.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md) |
| Calls, callers, chain, and deps sections show placeholder command forms and synthetic relationship output shapes for impact tracing and import-neighborhood discovery. | L40-L150 | [codegraphcontext-high-level-methods.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md) |
| Tree, complexity, and dead-code sections show synthetic class hierarchy, risk ranking, and unused-candidate output shapes. | L152-L238 | [codegraphcontext-high-level-methods.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md) |
| Overrides, variable, kotlin-call-audit, and practical rules explain method implementation search, local variable occurrence search, Kotlin coverage limits, and confirmation rules. | L240-L332 | [codegraphcontext-high-level-methods.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md) |
| The C-04 skill links agents to this catalog from the Relationship section. | L107-L111 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |

## Cross-Repo References

The example outputs are synthetic response-shape illustrations. They do not
contain private sibling repository names, symbols, paths, or code.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No source-code contract is imported from a sibling repository. | n/a | n/a |

## Update History

- 2026-05-23T13:46+02:00: Updated examples to use MCP `cgc_query` instead of the deleted source provider lifecycle script.
- 2026-05-21T15:20+02:00: Replaced private-project examples with synthetic response-shape examples.
- 2026-05-21T14:10+02:00: Created onboarding for the CGC high-level methods catalog.
