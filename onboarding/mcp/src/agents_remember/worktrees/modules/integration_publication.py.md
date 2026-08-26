# mcp/src/agents_remember/worktrees/modules/integration_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/integration_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

Carries typed preflight state from integration planning into the irreversible publication step.

## Code Commentary

### Logic

`IntegratePreview` holds the evaluated seam guard, optional handover warning, and the planned altitude-routed quality gate. `IntegrationPublication` bundles every preflight fact the protected publication must re-verify: the contract, worktree args, locked args, integration sources, integrated commits, the preflight organizational-completion presence, the quality gate, and the handover warning.

### Invariants And Boundaries

- These are dependency-light value types; each has exactly one implementation owner and is imported directly by `integrate.py` and `organizational_completion_integration.py`.
- No compatibility shim or implicit fallback exists.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Evaluated seam guard and planned quality gate for preview. | `IntegratePreview` | mcp/src/agents_remember/worktrees/modules/integration_publication.py:30-35 |
| Every preflight fact the irreversible publication re-verifies. | `IntegrationPublication` | mcp/src/agents_remember/worktrees/modules/integration_publication.py:39-49 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Contract

The current source seams include `IntegratePreview`, `IntegrationPublication`, `protected_integration_decision`. Integration transfers authority from the waiting-door projection into the journal, revalidates configured contract and protected refs at the mutation boundary, and records publication evidence. Source-ref movement must reconcile or complete the same generation.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `IntegratePreview`, `IntegrationPublication`, `protected_integration_decision` at this ownership boundary. | `IntegratePreview`; `IntegrationPublication`; `protected_integration_decision` | mcp/src/agents_remember/worktrees/modules/integration_publication.py:29-35; mcp/src/agents_remember/worktrees/modules/integration_publication.py:38-49; mcp/src/agents_remember/worktrees/modules/integration_publication.py:52-60 |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the integration publication typed state.
