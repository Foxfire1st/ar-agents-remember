# repo-overview-template.md

| Field                  | Value                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------- |
| repository             | agents-remember                                                                    |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/repo-overview-template.md` |
| doc_type               | `file-level-onboarding`                                                               |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`                                                                                    |
| lastVerifiedCommitDate |                                                                                       2026-08-05T12:41:24+02:00|

## Purpose

This template defines the root repo overview created or refreshed by `c-03-repo-bootstrap` skill bootstrap.

## Code Commentary

### Logic

The template records repo metadata, route-based verification fields, purpose, hot-path summary, architecture, code structure with local-overview status, functional areas, cross-repo references, build/dev commands, invariants, glossary terms, docs references, next exploration targets, needs verification, and update history.

### Conventions

The root overview is the minimum successful bootstrap output and should stay high-signal. Its `## Hot Path Summary` gives `c-04-retrieval-strategy-router` skill and the route-index generator a compact discovery summary. Detailed local routing moves into route-local overviews once they exist. Its `sourceRoute` is `<repo-root>`, and `lastVerifiedCommitHash` plus `lastVerifiedCommitDate` describe the source commit `c-02-memory-quality-control` skill should compare against for repo-wide overview drift.

### Invariants And Boundaries

The root overview gives repo-wide context. It should not become a catch-all area deep dive or replace route-local/file-level onboarding.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The repo overview template defines metadata, route-based verification fields, repo purpose, hot-path summary, architecture, code structure, functional areas, cross-repo references, build/dev commands, invariants, glossary, docs references, next work, verification needs, and update history. | `# <repo> — Onboarding Overview` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/repo-overview-template.md:1-83 |
| `c-03-repo-bootstrap` skill treats the root repo overview as the minimum successful bootstrap output. | `# Repo Bootstrap` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:6-1265 |
| `c-03-repo-bootstrap` skill Phase 3 synthesizes the root repo overview from state, input ledger, scout report, area briefs, and existing overview when present. | "# Scout Report — <repo>" | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:610-610 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  heading anchors; exact non-fixing check returns zero findings.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-19T02:45+02:00: Added `## Hot Path Summary` to the root overview template so generated route indexes can expose compact discovery context.
- 2026-05-15T11:46+02:00: Updated after the template added `lastVerifiedCommitDate` for deterministic route-based overview drift checks. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-14T18:00+02:00: Created onboarding for the repo overview template and route-local overview-aware code-structure model. Verification metadata remains blank until the source file is committed.
