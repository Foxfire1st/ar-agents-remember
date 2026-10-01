# cross-repo-boundary-pack-template.md

## Purpose

This template defines the evidence pack for allowed cross-repo or external-system boundaries discovered during bootstrap.

## Code Commentary

### Logic

The boundary pack records adjacent repos, branch status, boundary summary, confirmed interfaces, shared contracts, branch/topology notes, same-repo facts that must stay out of cross-repo buckets, risks, and low-confidence ties.

### Conventions

Boundary packs use adjacent repos as read-only evidence when allowed by topology and branch safeguards. Same-repo implementation facts are explicitly routed to `Repo-Internal References`.

### Invariants And Boundaries

The template must not let naming-only or low-confidence ties become durable cross-repo facts. It documents evidence for boundary claims; it does not authorize updating adjacent repo memory.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The boundary pack records allowed adjacent repos, boundary summaries, confirmed interfaces, and shared contracts. [1]
- The template records branch/topology notes, same-repo facts that must not be classified as cross-repo, boundary risks, and developer-confirmation needs. [2]
- `c-03-repo-bootstrap` skill Phase 4F writes boundary packs for priority routes with inbound or outbound cross-repo signals. [3]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
