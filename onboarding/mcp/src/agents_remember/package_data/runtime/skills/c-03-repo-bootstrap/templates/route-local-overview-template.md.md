# route-local-overview-template.md

## Purpose

This template defines durable route-local overview files that live in the mirrored onboarding hierarchy and act as construction pillars for nearby file-level onboarding.

## Code Commentary

### Logic

The template records route metadata, route-based verification fields, parent overview, area explanation, hot-path summary, scope boundaries, structures, operating model, flows, load-bearing files, local invariants, canonical reference sections, file-level onboarding map, child overviews, usage guidance, verification needs, and update history.

### Conventions

Route-local overviews use canonical `Repo-Internal References`, `Cross-Repo References`, and `Docs References` buckets. Their `## Hot Path Summary` stays short because it is copied into generated route indexes for `c-04-retrieval-strategy-router` skill discovery. Links from nested route-local overviews to root `bootstrap/` evidence packs must be calculated relative to the overview's depth. Their `sourceRoute`, `lastVerifiedCommitHash`, and `lastVerifiedCommitDate` fields give `c-02-memory-quality-control` skill the deterministic route scope to compare later.

### Invariants And Boundaries

Route-local overviews are durable memory, but they are not replacements for file-level onboarding. They provide local area context and must keep file-specific facts in file-level onboarding.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The route-local overview template defines route metadata, route verification fields, hot-path summary, scope, structures, flows, load-bearing files, local invariants, and traps. [1]
- The template uses canonical repo-internal, cross-repo, and docs reference sections, with depth-aware evidence-pack link placeholders. [2]
- The template maps file-level onboarding, child overviews, usage order, needs verification, and update history. [3]
- `c-03-repo-bootstrap` skill Phase 4D writes route-local overviews in mirrored source folders using this template. [4]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
