# mcp/src/agents_remember/application/tool_response.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/tool_response.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Complete one tool result at the application boundary.

## Code Commentary

### Logic

Module-level surface:

- `_agent_notifier_banner` (function, lines 22-31) — Return the stale-supervisor banner without blocking a tool response.
- `_attach_lifecycle_tail` (function, lines 34-44)
- `complete_tool_response` (function, lines 47-61) — Validate, enrich, count, and observe one application result.

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
| Defines the function `_agent_notifier_banner` (lines 22-31) — Return the stale-supervisor banner without blocking a tool response.. | `_agent_notifier_banner` | mcp/src/agents_remember/application/tool_response.py:22-31 |
| Defines the function `_attach_lifecycle_tail` (lines 34-44). | `_attach_lifecycle_tail` | mcp/src/agents_remember/application/tool_response.py:34-44 |
| Defines the function `complete_tool_response` (lines 47-61) — Validate, enrich, count, and observe one application result.. | `complete_tool_response` | mcp/src/agents_remember/application/tool_response.py:47-61 |

## L23 Final Candidate Disposition

The response completion boundary continues to normalize bounded task-addressed payloads only. L23's
operation phase and report evidence can pass through the existing response contract, while private
operation keys, worker PIDs, leases, and resume tokens remain absent.

## Update History

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the source only repoints `finalize_tool_response` to its moved `models.tools` package. Verified at code commit `1d446724`.
- 2026-08-14T06:30+02:00 — No contract expansion: L23 keeps tool-response completion bounded while
  carrying the existing task-addressed lifecycle-operation projection; private recovery identity
  remains excluded. Verification stays closeout-owned.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
