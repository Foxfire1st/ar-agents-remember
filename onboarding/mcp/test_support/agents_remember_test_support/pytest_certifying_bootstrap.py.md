# mcp/test_support/agents_remember_test_support/pytest_certifying_bootstrap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/pytest_certifying_bootstrap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Composes certifying-only pytest plugins while deferring the worktree service graph until fixture execution.

## Code Commentary

### Logic

The verification-package plugin names the shared hermetic, evidence-lane, phase, and causal
plugins. Session/function fixtures bind and reset default worktree services with fixture-local
product imports, so collection does not eagerly load the service/lifecycle graph.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- This module stays at the verification-package root to avoid executing the testing package
  initializer; importing it must not eagerly load the service/lifecycle graph.
- Verification may import product fixtures at the fixture boundary. Product code must never import
  this bootstrap or any `agents_remember_test_support` module.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `_bind_worktree_services_for_session` | mcp/test_support/agents_remember_test_support/pytest_certifying_bootstrap.py:1-42 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `_bind_worktree_services_for_session` | mcp/test_support/agents_remember_test_support/pytest_certifying_bootstrap.py:1-42 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_bind_worktree_services_for_session` | mcp/test_support/agents_remember_test_support/pytest_certifying_bootstrap.py:1-42 |

## Update History

- 2026-08-27T11:14+02:00 — Rehomed the certifying plugin root under explicit verification
  authority and documented the one-way verification-to-product fixture boundary.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
