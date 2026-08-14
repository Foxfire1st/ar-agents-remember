# mcp/src/agents_remember/serving/conversation/library/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

Marks the package that owns dormant native conversation list/read/resume serving.

## Code Commentary

### Logic

Contains only a package docstring; sibling `api.py` owns the route entrypoint.

### Conventions

Keep the marker behavior-free and separate from active exact-session projection.

### Invariants And Boundaries

- Library reads use native history authority, project scope, authorization, and library cursors.
- This marker does not enable a capability or load a vendor dependency.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The sibling router reserves the harness-native conversation-library prefix. | "/api/harnesses/{harness_id}/conversations" | mcp/src/agents_remember/serving/conversation/library/api.py:66-66 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 2 citation finding(s); scoped recheck clean.

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: re-pointed the governing overview link to
  the new library route-local overview created for the implemented slice. The source marker is
  unchanged, so no other content change was needed. Verification metadata remains pinned.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the package-marker sidecar.
  Verification is blank until closeout commits and stamps the new source.
