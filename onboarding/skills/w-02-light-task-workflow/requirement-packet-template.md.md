# skills/w-02-light-task-workflow/requirement-packet-template.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/w-02-light-task-workflow/requirement-packet-template.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `onboarding/overview.md` |

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

## Docs References

No external Domain Documentation source governs this requirement packet.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The template contains the full self-contained requirement contract. | `# Canonical Requirement Packet Template` | skills/w-02-light-task-workflow/requirement-packet-template.md:1-125 |
| Approval immutability, versioning, diagrams, and predeclared evidence are normative rules. | `## Rules` | skills/w-02-light-task-workflow/requirement-packet-template.md:126-139 |

## Cross-Repo References

Intent sources and evidence may point to another repository, but each such dependency must be
named explicitly in the packet rather than inferred from this generic template.

## Update History

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T14:52+02:00 — Created onboarding for immutable revision packets, cold-read approval,
  evidence classes, and affected-acceptance invalidation.
