# mcp/src/agents_remember/worktrees/modules/integration_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/integration_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-17T12:09+02:00 |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b` |
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
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
| Evaluated seam guard and planned quality gate for preview. | `IntegratePreview` | mcp/src/agents_remember/worktrees/modules/integration_publication.py:16-22 |
| Every preflight fact the irreversible publication re-verifies. | `IntegrationPublication` | mcp/src/agents_remember/worktrees/modules/integration_publication.py:25-36 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the integration publication typed state.
