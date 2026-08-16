# mcp/src/agents_remember/tasks/document_refs.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/document_refs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T05:27+02:00 |
| lastVerifiedCommitHash |  `8bf6edad7e7e65e27cf735be0822f604531d0c8a`|
| lastVerifiedCommitDate |  2026-08-16T10:54:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Resolves canonical sprint/master/leaf document references and their containment from the actual task
files. This is the topology authority behind structural seat qualification and replaces leaf-key
parsing as an identity model.

## Code Commentary

### Logic

`TaskDocumentTopology` indexes real task documents, normalizes repository-qualified references,
checks level and containment, and walks leaf→master→sprint without synthesizing anchors. Typed
`TaskDocumentRefError` failures distinguish malformed, missing, mismatched, and ambiguous topology.

For execution topology, `validate_execution_topology` resolves every sprint `orchestrates` alias to
exactly one commanded master, requires graph membership to equal that resolved set, and refuses a
missing graph or nature as migration-required. Candidate overrides let task-doc authoring validate
before publication. `execution_sprints_affected_by_master` inventories old and new folder/id/title
aliases so identity edits and same-path kind replacement cannot silently detach or collide a
commanded master; `execution_waves` exposes only the graph-derived order after validating the exact
sprint snapshot it will dereference, so a concurrent migration cannot split validation from the
returned graph. Override resolution retains independent root-confinement and repository-identity
guards for pre-publication candidates.
`resolve_candidate` exposes that same canonical override resolver to other task-authority owners;
callers do not duplicate the root and repository checks when inspecting a document that has not
yet been written.

### Conventions

Canonical paths are coordination-root-relative and remain tied to the actual task document.

### Invariants And Boundaries

- Task files, not session ancestry, define containment.
- Every resolved reference names one real document at one verified level.
- Ambiguity and scope loss fail closed.
- This module does not inspect terminal liveness or choose occupants.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Task document topology is centralized in one typed resolver. | `TaskDocumentTopology` | mcp/src/agents_remember/tasks/document_refs.py:26-252 |
| Structural seats consume this topology to qualify parent and child relations. | `StructuralSeatResolver` | mcp/src/agents_remember/serving/structural_seats.py:22-160 |

## Cross-Repo References

The task documents live in the configured coordination root, but the resolver contract is implemented
inside agents-remember and has no sibling-repository code dependency.


## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History

- 2026-08-16T05:27+02:00 — L4 exact-review repair: exposed the existing canonical override
  resolver through `resolve_candidate`, preserving its root-confinement and repository-identity
  checks for live-leaf publication authority without adding a second validation route.
- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-15T03:20:17+02:00 — 260815-DAG-L1 independent-review repair: `execution_waves` now pins
  the first resolved sprint into topology validation before deriving its waves, closing the
  double-read race in which validation and return could observe different graph generations.
- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: forcing coverage now reaches
  non-sprint topology use plus override root-confinement and repository-identity refusals.
  `execution_waves` relies on the immediately preceding durable topology validation instead of
  carrying a second impossible missing-graph branch.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: added the affected-sprint census
  used to revalidate old and new folder/id/title aliases, preventing commanded-master identity
  drift or a new alias collision from bypassing exact execution-graph membership.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: canonical task topology now validates exact
  `orchestrates`/graph membership, rejects aliases and unresolved masters, requires every commanded
  nature explicitly, and exposes graph-derived waves without inference.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created as the real-document topology authority; absorbs canonical validation formerly described by `serving/leaf_ref_validation.py`.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: predecessor leaf-reference card was verified against the then-current worktree; stale moved-path references were repaired.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 curator: predecessor card rebound two onboarding citations to code authorities.
- 2026-08-02T16:55+02:00 — 260731-EFA-L6 curator: predecessor card repaired three repo-internal citation rows.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: predecessor leaf validation added bounded legacy role-suffix detection and canonical leaf-plus-role refusal guidance.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: predecessor card was created for terminal leaf-key normalization at serving and MCP write boundaries.
