# AGENTS.md

## Governing Overview

[overview.md](../../../../../../overview.md)

## Current source contract evidence



## Purpose

This file is the package-owned template for installed
`ar-coordination/system/AGENTS.md`. It defines the hard onboarding maintenance
gate and the read/update discipline agents must follow around memory-backed
onboarding.

## Code Commentary

### Logic

The template requires `c-08-ar-coordination-context-resolver` skill context resolution, a configured-provider check, and
`c-05-create-or-update-onboarding-files` skill memory quality control before agents rely on repository onboarding for any task,
including read-only analysis. It defines the developer decision point when drift
exists, requires agents to separate clean-source update candidates from
dirty-source active work-in-progress, keeps `c-05-create-or-update-onboarding-files` skill as the maintenance route for
approved refreshes, and requires a second `c-05-create-or-update-onboarding-files` skill check after maintenance. It then
separates post-gate planning from implementation.
The configured-provider gate requests `context_packet` for the target repository without a provider argument. Provider authority remains the MCP settings file; provider state comes from settings/provider operations, never packet provider blocks.
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

`c-08-ar-coordination-context-resolver` skill and `c-05-create-or-update-onboarding-files` skill memory quality control are mandatory before trusting onboarding. The provider check runs
only when the MCP server is configured and the MCP settings report enabled
providers. The consolidated `c-05-create-or-update-onboarding-files` skill owns the first/second drift checks and approved onboarding maintenance; those stages retain their separate classification, developer-decision and report-cleanup duties.
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

- The template routes first/second drift checks and approved maintenance through c-05 while retaining clean/dirty-source classification, developer review and report deletion. [1]

- Cross-repository drift handling runs the first three gates for every allowed repo before asking about onboarding refresh. [3]
- Post-gate planning and research routes context-backed source reading to `c-04-retrieval-strategy-router`, which owns Semantics, Relationship, and Intent routing across providers, route indexes, onboarding, and bounded source confirmation. [4]
- Post-gate implementation updates or creates onboarding through `c-05-create-or-update-onboarding-files` skill when changed source files alter current-state knowledge. [5]
- The final code-quality section points agents at resolved memory-layer `system/tools.md` and optional `system/coding-guidelines.md` for repository-specific checks and coding rules. [6]

### Cross-Repo References

No sibling repository evidence is needed for this runtime template.

No meaningful cross-repo references found.

- Gate2 calls context_packet for the configured MCP repository; provider authority comes from MCP settings and provider operations, never a packet provider argument. [2]
- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance. [7]
