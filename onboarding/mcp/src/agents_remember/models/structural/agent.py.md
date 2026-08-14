# mcp/src/agents_remember/models/structural/agent.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/structural/agent.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T14:29+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structural wire models](overview.md)

## Purpose

Defines strict agent-facing DTOs for dispatch, parent/child messaging, retirement, and rename. The
wire contains stable work-domain identity and intentionally has no runtime addressing fields.

## Code Commentary

### Logic

Request dataclasses accept only task-document, role, content, label, and reason fields. Response
models share `StructuralTargetResponse`, exposing the resolved task document and role plus status.

### Conventions

Every operation has a distinct response model so the registry remains self-describing while the
structural target shape stays common.

### Invariants And Boundaries

- Public request dataclasses define only the listed structural fields; registration and wire tests
  guard the absence of plane-only address vocabulary.
- Session, lifecycle, terminal, inbox-row, and gate ids are forbidden on public schemas.
- Do not add legacy aliases for removed exact-id requests.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The request family uses structural fields only. | `DispatchAgentRequest` | mcp/src/agents_remember/models/structural/agent.py:39-69 |
| The response family returns structural targets without runtime ids. | `StructuralTargetResponse` | mcp/src/agents_remember/models/structural/agent.py:71-107 |

## Cross-Repo References


## Update History

- 2026-08-11T14:29+02:00 — Re-read `DispatchAgentRequest` and widened its citation to include
  the dataclass declaration; verification metadata remains pending for governed closeout.
- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for the public structural agent DTO family.
