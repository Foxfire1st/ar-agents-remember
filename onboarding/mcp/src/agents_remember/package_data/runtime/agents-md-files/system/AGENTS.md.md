# AGENTS.md

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

## Evidence

### Docs References

No external domain documentation is needed for this repository-local runtime
template.

No relevant external documentation found.

### Repo-Internal References

This onboarding is backed by the source template itself.

- The start-of-task trust gate requires `c-08-ar-coordination-context-resolver` skill context resolution, a configured-provider check, `c-02-memory-quality-control` skill memory quality control, clean-source versus dirty-source drift classification, developer review of drift, approved `c-05-create-or-update-onboarding-files` skill refresh, a second `c-02-memory-quality-control` skill check, and drift report deletion. [1]
- Gate 2 runs provider readiness through `context_packet` MCP tool only when the MCP server is configured and provider settings are enabled. [2]
- Cross-repository drift handling runs the first three gates for every allowed repo before asking about onboarding refresh. [3]
- Post-gate planning and research routes context-backed source reading to `c-04-retrieval-strategy-router`, which owns Semantics, Relationship, and Intent routing across providers, route indexes, onboarding, and bounded source confirmation. [4]
- Post-gate implementation updates or creates onboarding through `c-05-create-or-update-onboarding-files` skill when changed source files alter current-state knowledge. [5]
- The final code-quality section points agents at resolved memory-layer `system/tools.md` and optional `system/coding-guidelines.md` for repository-specific checks and coding rules. [6]

### Cross-Repo References

No sibling repository evidence is needed for this runtime template.

No meaningful cross-repo references found.
