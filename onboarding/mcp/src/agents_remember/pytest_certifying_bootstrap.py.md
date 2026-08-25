# mcp/src/agents_remember/pytest_certifying_bootstrap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/pytest_certifying_bootstrap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Composes certifying-only pytest plugins while deferring the worktree service graph until fixture execution.

## Code Commentary

### Logic

The root-level plugin names shared hermetic/evidence/causal plugins and uses session/function fixtures to bind and reset default worktree services with fixture-local imports.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- This module stays outside the testing package to avoid executing its initializer; importing it must not eagerly load the service/lifecycle graph.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `_bind_worktree_services_for_session` | mcp/src/agents_remember/pytest_certifying_bootstrap.py:1-42 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `_bind_worktree_services_for_session` | mcp/src/agents_remember/pytest_certifying_bootstrap.py:1-42 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_bind_worktree_services_for_session` | mcp/src/agents_remember/pytest_certifying_bootstrap.py:1-42 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
