# mcp/src/agents_remember/controlplane/stamps.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/stamps.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Aging an ISO-8601 stamp against a clock -- the primitive the record stores share.

## Code Commentary

### Logic

Module-level surface:

- `age_seconds` (function, lines 22-35) — Seconds between an ISO-8601 ``stamp`` and ``now``; ``None`` when unparseable.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the function `age_seconds` (lines 22-35) — Seconds between an ISO-8601 ``stamp`` and ``now``; ``None`` when unparseable.. | `age_seconds` | mcp/src/agents_remember/controlplane/stamps.py:22-35 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
