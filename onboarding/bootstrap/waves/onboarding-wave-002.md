# PDLS Onboarding Wave 002 — File-Size Ownership Splits

| Field | Value |
| --- | --- |
| repo | agents-remember |
| generated | 2026-08-24T21:43+02:00 |
| waveType | file-onboarding and route refresh |
| mode | existing-memory-slice-maintenance |
| status | complete |

## Goal

Preserve the meaning of two behavior-preserving file splits made in response to the armed
1,200-line code-quality rail.

## Included Cards

| Priority | Card | Target | Reason |
| --- | --- | --- | --- |
| high | `bootstrap/file-cards/mcp/src/agents_remember/application/worktree_tool_requests.py.card.md` | `mcp/src/agents_remember/application/worktree_tool_requests.py` | typed application request owner |
| high | `bootstrap/file-cards/mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py.card.md` | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py` | immutable publication binding owner |

## Existing Cards Refreshed

- `mcp/src/agents_remember/application/worktree_tools.py.md`
- `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py.md`
- `mcp/src/agents_remember/mcp/registration/closeout.py.md`

## Governing Overviews Refreshed

- `mcp/src/agents_remember/application/overview.md`
- `mcp/src/agents_remember/worktrees/integration/overview.md`

## Evidence Required

No Domain Documentation or cross-repository pack applies. The committed source split, former-owner
onboarding, and consuming source paths are the direct evidence.

## Acceptance

- Each new source has exactly one sidecar and one file card.
- Moved behavior remains documented at the new owner and the former owner names that owner.
- No duplicate model, locator, fallback, or compatibility path is documented.
- `worktree_tools.py` and `lifecycle_operation_location.py` remain below 1,200 lines.
- Route indexes are regenerated after the content tree is final.

## Result

Route-index regeneration covered all 66 routes: the root, MCP, application, and integration indexes
changed; the other 62 remained byte-identical. A final dry run reported zero stale indexes.
