# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/agents-md-files/skills/AGENTS.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `31846c1136f0fe75503a63fb557303a79fa022e8` |
| lastVerifiedCommitDate | 2026-05-24T23:07:31+02:00|

## Purpose

This file is the package-owned template for the installed
`ar-coordination/skills/AGENTS.md`. It is a compact routing guide for the core
Agents Remember support skills.

## Code Commentary

### Logic

The file is a numbered question-to-skill map. It routes context resolution to
C-08, missing repo memory scaffolds to C-00, stale onboarding to C-02, durable
finding placement to C-01, bootstrap onboarding to C-03, retrieval strategy
selection across semantic search, relationship graph queries, and
onboarding/source proof to C-04, onboarding artifact maintenance to C-05,
lifecycle and ledger operations to C-09, baseline adoption to C-10, and branch
memory carryover to C-11.

### Conventions

Each route is written as a developer-facing question followed by the canonical
skill identifier. The template intentionally stays compact so it can be read
quickly when an agent is already inside the installed skills tree.

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
| Core-skill routing maps common memory, retrieval strategy, lifecycle, baseline, and carryover needs to C-* IDs. | L1-L33    | [mcp/src/agents_remember/package_data/runtime/agents-md-files/skills/AGENTS.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/agents-md-files/skills/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this routing guide.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-21T03:05+02:00: Updated C-04 routing language to point at retrieval strategy selection across GrepAI semantics, CGC relationships, and Intent proof.
- 2026-05-18T21:44+02:00: Refreshed after pulling the committed C-04 onboarding read-mode rename from `origin/main`.
- 2026-05-18T21:38+02:00: Refreshed against the current committed skills routing template, restoring C-04 as unfamiliar-surface discovery and updating verification metadata.
- 2026-05-18T16:42+02:00: Updated C-04 routing language from unfamiliar-surface discovery to onboarding read mode for source reasoning.
- 2026-05-15T00:38+02:00: Moved onboarding semantics from the deleted core-skills local `AGENTS.md` to the new installable skills template path. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T11:36: Created onboarding for the core-skills routing guide while preparing direct closeout.
