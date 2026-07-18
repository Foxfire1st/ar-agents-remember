# mcp/src/agents_remember/serving/conversation/library/api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Structured conversation contract overview](../overview.md)

## Purpose

Reserves the per-harness dormant native conversation-library route for later list/read/exact-resume
implementation.

## Code Commentary

### Logic

Creates a behavior-empty `APIRouter` at `/api/harnesses/{harness_id}/conversations` with the
structured-library tag.

### Conventions

Endpoint behavior is added here by the native-library owner without another global registration
edit.

### Invariants And Boundaries

- The router prefix is harness-scoped; authorization and canonical project scope remain mandatory
  in the eventual service.
- Fixture or helper presence does not make list/read/resume supported.
- Keep active exact-session events and control actions out of this module.

### Todos

Implement list/read/resume only after the installed-runtime interoperability gates pass.

## Docs References

No Domain Documentation source is configured for this internal route shell.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The library port defines scoped list, historical read, and server-private resume-target resolution. | L59-L84 | [ports.py](agents-remember/mcp/src/agents_remember/serving/conversation/ports.py) |
| Runtime fixtures explicitly keep list/read/resume unexercised and non-enabling. | L102-L123 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local route shell.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the native-library route-shell
  sidecar. Verification is blank until closeout commits and stamps the new source.
