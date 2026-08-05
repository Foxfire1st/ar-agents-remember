# mcp/src/agents_remember/serving/conversation/active/projector/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |  2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Public implementation facade. | `ActiveSessionProjector` | mcp/src/agents_remember/serving/conversation/active/projector/facade.py:59-221 |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18 hygiene curator: removed the redundant
  `facade.py:1-1` fixer-input entry (the `ActiveSessionProjector` anchor is covered by the
  `59-221` range); exact check remains zero-finding.

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: bound the facade row to facade.py 1-1
  plus the `ActiveSessionProjector` class extent (59-221) with a plain source. Zero findings
  remain.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the compatibility-export
  sidecar for the new projector package. Verification metadata remains blank until commit.
