# AGENTS.md

## Purpose

This file is the package-owned template for the installed
`ar-coordination/skills/AGENTS.md`. It is a compact routing guide for the core
Agents Remember support skills.

## Code Commentary

### Logic

The file is a numbered question-to-skill map. It routes context resolution to
`c-08-ar-coordination-context-resolver` skill, missing repo memory scaffolds to `c-00-initialize-memory-repo` skill, stale onboarding to `c-02-memory-quality-control` skill, durable
finding placement to `c-01-findings-capture` skill, bootstrap onboarding to `c-03-repo-bootstrap` skill, retrieval strategy
selection across semantic search, relationship graph queries, and
onboarding/source proof to `c-04-retrieval-strategy-router` skill, onboarding artifact maintenance to `c-05-create-or-update-onboarding-files` skill,
lifecycle and ledger operations to `c-09-git-worktree-manager` skill, baseline adoption to `c-10-adopt-memory-baseline` skill, and branch
memory carryover to `c-11-memory-carryover-from-branch` skill.

### Conventions

Each route is written as a developer-facing question followed by the canonical
skill identifier. The template intentionally stays compact so it can be read
quickly when an agent is already inside the installed skills tree. A closing
Reference Style section requires full lowercase skill ids with the word "skill"
(its lifecycle example cites *the `l-01-agent-lifecycles` skill*) and snake_case
MCP tool names qualified with "MCP tool", so skills and tools stay
distinguishable in prose.

### Invariants And Boundaries

This file is routing context only. It should point to the owning skill rather
than duplicating that skill's full workflow contract, approval gates, or command
syntax.

### Todos

None.

### Docs References

No external domain documentation is needed for this repository-local routing
guide.

No relevant external documentation found.

## Evidence

### Repo-Internal References

The route list itself is the primary implementation evidence.

- Core-skill routing maps common memory, retrieval strategy, lifecycle, baseline, and carryover needs to C-* IDs. [1]

### Cross-Repo References

No sibling repository evidence is needed for this routing guide.

No meaningful cross-repo references found.
