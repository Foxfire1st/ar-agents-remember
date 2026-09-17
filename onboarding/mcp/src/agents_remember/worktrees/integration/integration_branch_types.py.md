# mcp/src/agents_remember/worktrees/integration/integration_branch_types.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_branch_types.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `997305a9ced4caea67edb826224bf0351264fd56` |
| lastVerifiedCommitDate | 2026-09-17T19:54:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

Defines the immutable data contracts exchanged by task-derived integration branch authority without owning repository queries or lifecycle policy.

## Code Commentary

The module holds the public protected-surface, integration-target, proposed-work-branch, and repository-checkout request records together with the resolver's internal repository-side, task scope, and master-authority projections. Keeping these dependency-light records outside the policy resolver preserves its public imports while the resolver, Git fact owner, and lifecycle callers retain one implementation each.

## Invariants And Boundaries

- Records are frozen values; they do not perform Git, task-document, or contract I/O.
- Surface side and kind vocabularies remain closed literals shared by all authority callers.
- Repository and branch policy remains in `integration_branch_authority.py`; exact Git facts remain in `integration_branch_repository.py`.
- The move is structural and supplies no compatibility fallback or alternate authority route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Surface and target records carry exact side, kind, repository, branch, and owner identity. | `IntegrationSurface`, `IntegrationTarget` | mcp/src/agents_remember/worktrees/integration/integration_branch_types.py:17-23; mcp/src/agents_remember/worktrees/integration/integration_branch_types.py:26-32 |
| Workbench and checkout requests carry the task and repository facts required by the resolver. | `ProposedWorkBranches`, `RepositoryCheckoutRequest` | mcp/src/agents_remember/worktrees/integration/integration_branch_types.py:61-69; mcp/src/agents_remember/worktrees/integration/integration_branch_types.py:72-80 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **dead governing-overview body link repaired, and the field brought into agreement with it.** The field named `overview.md` — which resolves, but only under the onboarding root rather than against this card's own route — while the body link named `../../../overview.md` and resolved card-relative to nothing, so a reader clicking it landed nowhere and the two declarations disagreed. Both now name `overview.md`, the route-local overview of this card's own directory, so the field and the link agree by construction. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_branch_types.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-16T07:02+02:00 — 260815-DAG-L4: moved the integration authority data contracts into a bounded dependency-light owner to satisfy the enforced source-file size contract without duplicating policy.
