# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff` |
| lastVerifiedCommitDate | 2026-06-02T16:24:22+02:00|
| governingOverview      | `../../../../../../overview.md`                              |

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

This file is the package-owned template for installed
`ar-coordination/system/AGENTS.md`. It defines the hard onboarding maintenance
gate and the read/update discipline agents must follow around memory-backed
onboarding.

## Code Commentary

### Logic

The template requires `c-08-ar-coordination-context-resolver` skill context resolution, a configured-provider check, and
`c-02-memory-quality-control` skill memory quality control before agents rely on repository onboarding for any task,
including read-only analysis. It defines the developer decision point when drift
exists, requires agents to separate clean-source update candidates from
dirty-source active work-in-progress, keeps `c-05-create-or-update-onboarding-files` skill as the maintenance route for
approved refreshes, and requires a second `c-02-memory-quality-control` skill check after maintenance. It then
separates post-gate planning from implementation.
The configured-provider check now invokes the Agents Remember MCP
`context_packet` tool with provider inspection enabled. Provider authority is
stated directly as the MCP settings file.
For context-backed source reading, use `c-04-retrieval-strategy-router`. `c-04-retrieval-strategy-router` skill
owns Semantics, Relationship, and Intent routing across optional providers,
route indexes, onboarding, and bounded source confirmation.
Implementation updates or creates onboarding when code changes current-state
knowledge. The final code-quality section routes repository-specific validation
and coding-rule lookup to the resolved memory layer's `system/tools.md` and
optional `system/coding-guidelines.md`.

### Conventions

The system template is strict because it protects trust in durable memory. It
uses numbered gates for the startup workflow and clearer headings for
single-repo, cross-repo, planning, and implementation phases. The template now
keeps the trust, configured-provider, and maintenance gates here while routing
read behavior to `c-04-retrieval-strategy-router` skill, so the read-mode contract has one owning document.

### Invariants And Boundaries

`c-08-ar-coordination-context-resolver` skill and `c-02-memory-quality-control` skill memory quality control are mandatory before trusting onboarding. The provider check runs
only when the MCP server is configured and the MCP settings report enabled
providers. `c-02-memory-quality-control` skill detects
drift but does not update onboarding; `c-05-create-or-update-onboarding-files` skill owns approved onboarding maintenance.
The drift report is temporary coordination state and should be deleted after the
gate is complete. `c-04-retrieval-strategy-router` skill owns post-gate context retrieval strategy and
source/onboarding confirmation. Repository-specific test, lint, typecheck,
build, smoke-check, branch, and local command guidance belongs in the resolved
memory layer's `system/tools.md`; repo-specific coding rules belong in optional
`system/coding-guidelines.md`.

### Todos

None.

## Docs References

No external domain documentation is needed for this repository-local runtime
template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

This onboarding is backed by the source template itself.

| Finding                                                                                                                     | Citations | Source Path |
| --------------------------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| The start-of-task trust gate requires `c-08-ar-coordination-context-resolver` skill context resolution, a configured-provider check, `c-02-memory-quality-control` skill memory quality control, clean-source versus dirty-source drift classification, developer review of drift, approved `c-05-create-or-update-onboarding-files` skill refresh, a second `c-02-memory-quality-control` skill check, and drift report deletion. | L1-L37 | [mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md) |
| Gate 2 runs provider readiness through `context_packet` MCP tool only when the MCP server is configured and provider settings are enabled. | L17-L26 | [mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md) |
| Cross-repository drift handling runs the first three gates for every allowed repo before asking about onboarding refresh. | L40-L46 | [mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md) |
| Post-gate planning and research routes context-backed source reading to `c-04-retrieval-strategy-router`, which owns Semantics, Relationship, and Intent routing across providers, route indexes, onboarding, and bounded source confirmation. | L50-L54 | [mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md) |
| Post-gate implementation updates or creates onboarding through `c-05-create-or-update-onboarding-files` skill when changed source files alter current-state knowledge. | L58-L73 | [mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md) |
| The final code-quality section points agents at resolved memory-layer `system/tools.md` and optional `system/coding-guidelines.md` for repository-specific checks and coding rules. | L77-L81 | [mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this runtime template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` added clean-source versus dirty-source drift classification to the installed system gate.
- 2026-05-24T04:34+02:00: Updated after system template routed Gates 3 and 6 through `c-02-memory-quality-control` skill memory quality control.
- 2026-05-23T21:25+02:00: Simplified provider-authority wording and added installed system code-quality routing to resolved memory-layer tools and coding guidelines.
- 2026-05-23T04:43+02:00: Updated Gate 2 onboarding for `context_packet` MCP tool authority instead of coordinator settings.
- 2026-05-21T15:42+02:00: Updated the provider readiness gate after the lifecycle script began defaulting the coordinator root from its installed location.
- 2026-05-21T04:09+02:00: Added configured-provider readiness as Gate 2 and renumbered the onboarding drift gates.
- 2026-05-21T03:05+02:00: Updated the post-gate read route from onboarding read mode to the `c-04-retrieval-strategy-router` skill retrieval strategy router.
- 2026-05-18T21:44+02:00: Refreshed after pulling the committed `c-04-retrieval-strategy-router` skill onboarding read-mode rename from `origin/main`.
- 2026-05-18T21:38+02:00: Refreshed against the current committed system template, removing unlanded `c-04-retrieval-strategy-router` skill read-mode wording and updating verification metadata.
- 2026-05-18T17:03+02:00: Reduced the system onboarding description to the trust and maintenance gates plus `c-04-retrieval-strategy-router` skill routing for post-gate read behavior, matching the updated runtime template.
- 2026-05-18T15:32+02:00: Tightened onboarding-led discovery into an ordering rule: candidate pairs must precede source discovery search, onboarding tree enumeration is fallback-only, and source search must stay route-local before broad fallback.
- 2026-05-18T14:48+02:00: Renamed the system gate headings and added the onboarding-led source discovery path so warm-memory agents use overview and route maps to choose candidate files before broad source search.
- 2026-05-15T00:38+02:00: Created onboarding after the former root `system/AGENTS.md` guidance moved to the installable system template path. Verification metadata remains pinned to the last committed source until closeout.
