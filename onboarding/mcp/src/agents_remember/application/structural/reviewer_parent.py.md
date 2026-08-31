# mcp/src/agents_remember/application/structural/reviewer_parent.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/structural/reviewer_parent.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T07:35+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[structural application overview](overview.md)

## Purpose

Centralizes structural-parent derivation and dispatch provenance for identity-free reviewer seats.

## Code Commentary

### Logic

`ambient_reviewer_parent` maps a leaf reviewer to its owning master manager and a master reviewer to
that master's manager. Sprint reviewer dispatch refuses because architect and orchestrator are both
valid owners. `resolve_dispatch_provenance` stamps the resolved parent into both spawn provenance and
the expected reviewer generation.

### Conventions

An existing bound caller supplies explicit parent authority. Ambient derivation is allowed only when
topology has one unambiguous owner.

### Invariants And Boundaries

- Parent identity is generation-bound and includes both task document and role.
- Sprint ambiguity refuses before host effects.
- Non-reviewer roles do not acquire reviewer-parent metadata.
- The helper never guesses between architect and orchestrator.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Ambient parent derivation is topology- and altitude-specific. | `ambient_reviewer_parent` | mcp/src/agents_remember/application/structural/reviewer_parent.py:32-55 |
| Dispatch provenance carries the exact reviewer parent. | `resolve_dispatch_provenance` | mcp/src/agents_remember/application/structural/reviewer_parent.py:58-78 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-31T07:35+02:00 — Created for 260821-ARSPAWN-L5 independent-review repair. Verification remains closeout-owned.
