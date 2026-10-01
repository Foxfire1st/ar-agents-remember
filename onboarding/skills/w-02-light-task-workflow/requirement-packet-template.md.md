# skills/w-02-light-task-workflow/requirement-packet-template.md

## Governing Overview

[repository onboarding overview](../../overview.md)

## Purpose

This is the canonical shape for one independently falsifiable requirement revision compiled before
task decomposition. Each approved revision has an immutable, version-addressed file.

## Code Commentary

### Logic

The packet records stable identity and version, normative behavior, the motivating problem,
rationale, scope and exclusions, preserved behavior, failure/recovery states, examples, forbidden
overreach, material diagrams, predeclared deliverable and verification evidence classes,
authority/provenance, dependencies, truth gaps, transcript-free cold-read results, and revision
invalidation history.

### Conventions

- Store packets under `requirements/` as `<stable-id>-<version>-<slug>.md`.
- Keep the ID/version index in `requirements/README.md`.
- Add diagrams only where they materially clarify interactions.
- Record the durable developer ruling inside every approved packet.

### Invariants And Boundaries

- Approved packet revisions are immutable; a semantic change creates a new versioned file.
- A packet covers exactly one independently falsifiable obligation.
- Approval binds one exact ID and version.
- Expected evidence classes guide later proof but do not pre-approve artifacts.
- Cold-read failure returns the packet for rewriting before topology exists.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source governs this requirement packet.

### Repo-Internal References

- The template contains the full self-contained requirement contract. [1]
- Approval immutability, versioning, diagrams, and predeclared evidence are normative rules. [2]

### Cross-Repo References

Intent sources and evidence may point to another repository, but each such dependency must be
named explicitly in the packet rather than inferred from this generic template.
