# C-04-retrieval-strategy-router/grepai-high-leverage-usage.md

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/grepai-high-leverage-usage.md` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-23T13:46+02:00                                 |
| lastVerifiedCommitHash | `5ff4ed4ef94b5576a45059de8ac7c03e8c4c04a1`             |
| lastVerifiedCommitDate | 2026-05-21T18:12:00+02:00|
| governingOverview      | `../../overview.md`                                    |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

This sibling reference teaches agents how to use GrepAI after C-04 selects the
`Semantics` substrate. It documents high-leverage search and trace patterns
with synthetic command shapes and example outputs so agents can use the memory
substrate through MCP without relying on private examples or global GrepAI
state.

## Code Commentary

### Logic

The document starts with the MCP managed invocation contract: request GrepAI
through `grepai_search`, `grepai_trace`, and `provider_status` so the server
selects the runtime-owned binary and provider-owned environment. It then maps
common semantic retrieval questions to broad workspace search, compact JSON
anchors, snippet search, project scoping, path scoping, trace commands, status,
and stats.

The examples focus on broad semantic routing, scoped project search,
route-scoped snippet search, GrepAI trace as a fallback relationship tool, and
coverage/status checks. Every output example is synthetic and uses placeholder
project ids, paths, symbols, snippets, and scores.

### Conventions

Run GrepAI examples through MCP provider tools:

```text
grepai_search(query="<query>", dry_run=false)
grepai_trace(query="<query>", dry_run=false)
provider_status()
```

Use `--toon --compact` for the cheapest broad routing pass, `--json --compact`
for API callers that need anchors, and full `--json` only when snippets are
needed to choose between close candidates. Add `--project` after the relevant
memory root is known and `--path` only after route discovery has already
narrowed the search.

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

No external documentation is cited here. The document records local GrepAI
v0.35.0 command surfaces from help output, then presents only synthetic example
outputs.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The GrepAI catalog requires synthetic examples only and positions GrepAI as the fuzzy discovery tool for memory/onboarding, with CGC reserved for structural code relationships. | L1-L12 | [grepai-high-leverage-usage.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/grepai-high-leverage-usage.md) |
| The managed invocation section sets provider-owned `HOME`, `XDG_STATE_HOME`, and `XDG_CACHE_HOME` and points at the runtime-owned binary so agents do not use global GrepAI state. | L14-L33 | [grepai-high-leverage-usage.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/grepai-high-leverage-usage.md) |
| The command chooser maps semantic routing, compact API anchors, snippet search, project/path scoping, trace, status, and stats to GrepAI command patterns. | L35-L46 | [grepai-high-leverage-usage.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/grepai-high-leverage-usage.md) |
| Broad semantic routing, scoped project search, and route-scoped snippet search sections show placeholder command forms and synthetic TOON/JSON output shapes. | L48-L153 | [grepai-high-leverage-usage.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/grepai-high-leverage-usage.md) |
| Trace, coverage, and practical rules explain when GrepAI trace is acceptable, how to check status, and how to keep result budgets small. | L155-L236 | [grepai-high-leverage-usage.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/grepai-high-leverage-usage.md) |
| The C-04 skill links agents to this catalog from the Semantics section. | L100-L103 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |

## Cross-Repo References

The example outputs are synthetic response-shape illustrations. They do not
contain private sibling repository names, symbols, paths, snippets, or results.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No source-code contract is imported from a sibling repository. | n/a | n/a |

## Update History

- 2026-05-23T13:46+02:00: Updated examples to use MCP provider tools instead of direct runtime binary or deleted source lifecycle script calls.
- 2026-05-23T05:32+02:00: Updated GrepAI managed invocation paths after provider instances moved under `providers/runners/grepai`.
- 2026-05-21T16:14+02:00: Created onboarding for the GrepAI high-leverage usage catalog.
