# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/agents-md-files/skills/AGENTS.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063` |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|

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

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

The route list itself is the primary implementation evidence.

| Finding                                                                                                             | Citations | Source Path |
| ------------------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| Core-skill routing maps common memory, retrieval strategy, lifecycle, baseline, and carryover needs to C-* IDs. | L1-L33    | [mcp/src/agents_remember/package_data/runtime/agents-md-files/skills/AGENTS.md](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/skills/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this routing guide.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-07-06T12:05+02:00 — 260703-L10 (one-vocabulary sweep, synced from root `agents-md-files/` via `sync-runtime.py`): the Reference Style section's lifecycle example now cites the `l-01-agent-lifecycles` skill instead of the retired `l-01-session-job-lifecycle`; the routing map itself is unchanged. Documented the Reference Style section in Conventions. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-21T03:05+02:00: Updated `c-04-retrieval-strategy-router` skill routing language to point at retrieval strategy selection across GrepAI semantics, CGC relationships, and Intent proof.
- 2026-05-18T21:44+02:00: Refreshed after pulling the committed `c-04-retrieval-strategy-router` skill onboarding read-mode rename from `origin/main`.
- 2026-05-18T21:38+02:00: Refreshed against the current committed skills routing template, restoring `c-04-retrieval-strategy-router` skill as unfamiliar-surface discovery and updating verification metadata.
- 2026-05-18T16:42+02:00: Updated `c-04-retrieval-strategy-router` skill routing language from unfamiliar-surface discovery to onboarding read mode for source reasoning.
- 2026-05-15T00:38+02:00: Moved onboarding semantics from the deleted core-skills local `AGENTS.md` to the new installable skills template path. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T11:36: Created onboarding for the core-skills routing guide while preparing direct closeout.
