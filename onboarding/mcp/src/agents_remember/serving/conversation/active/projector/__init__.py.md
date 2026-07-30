# mcp/src/agents_remember/serving/conversation/active/projector/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Preserves the former `active.projector` import surface after the implementation moved into a
package.

## Code Commentary

### Logic

Re-exports `ActiveSessionProjector`, `PageResult`, the close sentinel, and the two ordering
exceptions used by callers and tests. It contains no runtime state or forwarding behavior beyond
Python package exports.

### Conventions

Only intentionally public names belong in `__all__`.

### Invariants And Boundaries

- Existing imports from `agents_remember.serving.conversation.active.projector` keep working.
- Implementation ownership stays in the named component modules.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public implementation facade. | [facade.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector/facade.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the compatibility-export
  sidecar for the new projector package. Verification metadata remains blank until commit.
