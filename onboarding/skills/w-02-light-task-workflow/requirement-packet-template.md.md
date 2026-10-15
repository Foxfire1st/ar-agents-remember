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

## Inherited Source-Epoch Commentary

The following account preserves the former distribution-copy card and its useful explanations, history and warnings. It is inherited scope, not a second current contract or a fresh certification of its dated/currentness, tool, provider, registry, execution or permission claims. The canonical account above retains its existing attribution and qualifications; the authored source below is the authority for the file. Historical reference labels in this quotation are provenance labels, not reference identities of this card.

> # `w-02-light-task-workflow` requirement-packet-template.md
>
> ## Purpose
>
> This installed template is the canonical shape for one independently falsifiable requirement
> revision before task decomposition.
>
> ## Logic
>
> The packet records stable identity/version, normative behavior, problem/rationale, scope and
> exclusions, preservation and failure/recovery boundaries, examples and forbidden overreach,
> material diagrams, deliverable/verification evidence classes, authority/provenance, dependencies,
> truth gaps, a transcript-free cold-read record, and revision/invalidation history.
>
> ## Invariants And Boundaries
>
> - The packet is canonical and immutable after approval; task documents link its
>   `<stable-id>-<version>-<slug>.md` address and never rewrite its contract.
> - Approval binds one exact ID + version.
> - Every approved packet records the durable corpus ruling. Semantic change increments version,
>   creates a new version-addressed file, and invalidates only affected acceptance.
> - Expected evidence is specified before implementation but does not pre-approve later artifacts.
> - This runtime copy is generated from root `skills/` by `scripts/sync-skills.py`.

## Canonical Source Ownership

The authored file is the canonical contract; its measured byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. The following whole-file reference locates that authored contract; it does not convert inherited statements into executed or whole-card acceptance.

- The authored source owns this contract; the distribution copy is not a separate authority. [3]
