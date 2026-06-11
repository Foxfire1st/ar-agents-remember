# c-04-retrieval-strategy-router/grepai-high-leverage-usage.md

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                     |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/grepai-high-leverage-usage.md` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-26T23:11+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`             |
| lastVerifiedCommitDate | 2026-06-02T16:24:22+02:00|
| governingOverview      | `../../../../../../../overview.md`                              |

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

This sibling reference teaches agents how to use GrepAI after `c-04-retrieval-strategy-router` skill selects the
`Semantics` substrate. It documents high-leverage search and trace patterns
with synthetic MCP call shapes and JSON-oriented example outputs so agents can
use the memory substrate through MCP without relying on private examples,
global GrepAI state, or raw Docker CLI workarounds.

## Code Commentary

### Logic

The document starts with the MCP managed invocation contract: request GrepAI
through `grepai_search`, `grepai_trace`, and `provider_status` so the server
selects the Docker runner container and provider-owned environment. It then
maps common semantic retrieval questions to workspace-wide JSON search,
configured `repo_ids` scoping, route-focused follow-up reads, explicit trace
actions, and provider health checks.

The examples focus on broad semantic routing, scoped project search,
route-focused snippet follow-up, GrepAI trace as a fallback relationship tool,
and coverage/status checks. Every output example is synthetic and uses
placeholder project ids, paths, symbols, snippets, and scores.

### Conventions

Run GrepAI examples through MCP provider tools:

```text
grepai_search(query="<query>", all_repos=true, limit=5, output_format="json")
grepai_search(query="<query>", repo_ids=["<repoId>"], limit=5, output_format="json")
grepai_trace(trace_action="callers", symbol="<symbol>", output_format="json")
provider_status()
```

Use `all_repos=true` for broad routing when the memory project is unknown, keep
`output_format="json"` for machine-readable anchors, and add `repo_ids` only
after the relevant configured memory root is known. The MCP GrepAI tools do not
currently expose path scoping; after route discovery, open the selected
onboarding or source paths directly.

### Invariants And Boundaries

GrepAI output is semantic discovery, not proof. Use it to choose memory routes,
overviews, sidecars, or candidate source areas, then confirm with onboarding
and bounded source reads before answering or editing. Prefer CGC for code
relationships when it is configured; GrepAI trace is a fallback or
single-provider relationship aid.

Reusable docs must not contain private repository names, symbols, paths,
snippets, or search results. Use placeholder examples only.

### Todos

None.

## Docs References

No external documentation is cited here. The document records the local
Agents Remember MCP GrepAI invocation contract and presents only synthetic
example outputs.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The GrepAI catalog requires synthetic examples only and positions GrepAI as the fuzzy discovery tool for memory/onboarding, with CGC reserved for structural code relationships. | L1-L12 | [grepai-high-leverage-usage.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/grepai-high-leverage-usage.md) |
| The managed invocation section routes through `grepai_search` MCP tool and `grepai_trace`, defaults examples to JSON, and says `repo_ids` must be MCP-configured repositories. | L14-L28 | [grepai-high-leverage-usage.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/grepai-high-leverage-usage.md) |
| The command chooser maps semantic routing, JSON anchors, configured repo scoping, route-focused follow-up reads, trace, and health checks to MCP tool calls. | L30-L39 | [grepai-high-leverage-usage.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/grepai-high-leverage-usage.md) |
| Broad semantic routing, scoped project search, and route-focused snippet search sections show placeholder MCP calls and synthetic JSON output shapes. | L41-L138 | [grepai-high-leverage-usage.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/grepai-high-leverage-usage.md) |
| Trace, coverage, and practical rules explain when GrepAI trace is acceptable, how to check status, how to keep result budgets small, and that MCP GrepAI does not expose path scoping. | L140-L207 | [grepai-high-leverage-usage.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/grepai-high-leverage-usage.md) |
| The `c-04-retrieval-strategy-router` skill links agents to this catalog from the Semantics section. | L75-L78 | [`c-04-retrieval-strategy-router` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md) |

## Cross-Repo References

The example outputs are synthetic response-shape illustrations. They do not
contain private sibling repository names, symbols, paths, snippets, or results.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No source-code contract is imported from a sibling repository. | n/a | n/a |

## Update History

- 2026-05-29T20:25+02:00: Dropped the now-redundant `dry_run=false` from the GrepAI examples (queries return results by default after the act-by-default flip) and noted `dry_run=true` is a command-preview/debug-only affordance.
- 2026-05-26T23:11+02:00: Refreshed verification metadata after source commit `5ab704a` landed the updated GrepAI MCP usage catalog.
- 2026-05-26T22:54+02:00: Updated after the catalog switched to the typed GrepAI MCP shape with JSON defaults, configured `repo_ids`, explicit trace actions, and route-follow-up reads instead of raw path scoping.
- 2026-05-25T18:07+02:00: Updated managed invocation commentary after GrepAI became Docker-runner-owned rather than runtime-binary-owned.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T00:37+02:00: Refreshed verification and citations after the catalog moved fully to MCP provider-tool invocation examples.
- 2026-05-23T13:46+02:00: Updated examples to use MCP provider tools instead of direct runtime binary or deleted source lifecycle script calls.
- 2026-05-23T05:32+02:00: Updated GrepAI managed invocation paths after provider instances moved under `providers/runners/grepai`.
- 2026-05-21T16:14+02:00: Created onboarding for the GrepAI high-leverage usage catalog.
