# repo-overview-template.md

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

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The repo overview template defines metadata, route-based verification fields, repo purpose, hot-path summary, architecture, code structure, functional areas, cross-repo references, build/dev commands, invariants, glossary, docs references, next work, verification needs, and update history. [1]
- `c-03-repo-bootstrap` skill treats the root repo overview as the minimum successful bootstrap output. [2]
- `c-03-repo-bootstrap` skill Phase 3 synthesizes the root repo overview from state, input ledger, scout report, area briefs, and existing overview when present. [3]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
