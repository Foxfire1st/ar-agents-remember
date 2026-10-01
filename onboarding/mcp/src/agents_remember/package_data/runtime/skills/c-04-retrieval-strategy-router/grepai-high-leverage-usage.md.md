# c-04-retrieval-strategy-router/grepai-high-leverage-usage.md

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

## Evidence

### Docs References

No external documentation is cited here. The document records the local
Agents Remember MCP GrepAI invocation contract and presents only synthetic
example outputs.

No relevant external documentation found.

### Repo-Internal References

- The GrepAI catalog requires synthetic examples only and positions GrepAI as the fuzzy discovery tool for memory/onboarding, with CGC reserved for structural code relationships. [1]
- The managed invocation section routes through `grepai_search` MCP tool and `grepai_trace`, defaults examples to JSON, and says `repo_ids` must be MCP-configured repositories. [2]
- The command chooser maps semantic routing, JSON anchors, configured repo scoping, route-focused follow-up reads, trace, and health checks to MCP tool calls. [3]
- Broad semantic routing, scoped project search, and route-focused snippet search sections show placeholder MCP calls and synthetic JSON output shapes. [4]
- Trace, coverage, and practical rules explain when GrepAI trace is acceptable, how to check status, how to keep result budgets small, and that MCP GrepAI does not expose path scoping. [5]
- The `c-04-retrieval-strategy-router` skill links agents to this catalog from the Semantics section. [6]

### Cross-Repo References

The example outputs are synthetic response-shape illustrations. They do not
contain private sibling repository names, symbols, paths, snippets, or results.

No source-code contract is imported from a sibling repository.
