# mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Revalidates the immutable lifecycle journal against the current contract, repositories, refs, source tips, and accepted commits.

## Code Commentary

`require_plane_integration_operation` proves the operation key and durable authority before protected movement. The source and commit helpers then recheck current named refs and the exact closed candidate at the last reversible boundary, preventing repository rebind, source-alias drift, candidate substitution, or replay output widening.

## Invariants And Boundaries

- A contract path alone is not integration authority.
- Configured Git common-directory identities and canonical ref names are immutable operation facts.
- Authorized outputs must equal the journaled accepted candidate; no unrecorded replay result may land.
- Legacy or malformed journal records fail closed.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Operation admission binds the requested key to one durable authority record. | `require_plane_integration_operation` | mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py:20-50 |
| Source tips and candidate commits are revalidated immediately before movement. | `require_current_integration_sources`, `require_authorized_integration_commits` | mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py:53-71; mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py:74-98 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created durable integration-operation proof onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.