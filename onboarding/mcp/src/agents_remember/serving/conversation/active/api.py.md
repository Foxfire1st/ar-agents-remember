# mcp/src/agents_remember/serving/conversation/active/api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Structured conversation contract overview](../overview.md)

## Purpose

Reserves ownership of the exact-session active structured-conversation HTTP route for the later
active projector implementation.

## Code Commentary

### Logic

Creates a behavior-empty `APIRouter` at
`/api/terminal/{ar_session_id}/conversation` with the structured-active tag.

### Conventions

This leaf establishes URL and ownership only. Endpoint functions arrive in this module rather than
through another global application edit.

### Invariants And Boundaries

- The router must remain empty until its production projector leaf implements and verifies it.
- Exact-session active reads must use the active port and active cursors, not dormant library keys.
- Do not project terminal text as structured native history.

### Todos

Implement page/status/capability/event endpoints only in the owning active-projector leaf.

## Docs References

No Domain Documentation source is configured for this internal route shell.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The active read port defines identify, page, subscribe, status, and capability operations. | L27-L56 | [ports.py](agents-remember/mcp/src/agents_remember/serving/conversation/ports.py) |
| The foundation regression asserts this prefix and the current behavior-empty state. | L31-L47 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local route shell.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the active route-shell sidecar.
  Verification is blank until closeout commits and stamps the new source.
