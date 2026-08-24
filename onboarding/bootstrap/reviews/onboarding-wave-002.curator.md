# PDLS Onboarding Wave 002 Curator Review

| Field | Value |
| --- | --- |
| repo | agents-remember |
| reviewed | 2026-08-24T21:43+02:00 |
| waveManifest | `bootstrap/waves/onboarding-wave-002.md` |
| status | pass |
| frozen source commit | `23d35f7799153e0c7f3d126291fe2da1662fb87b` |
| frozen source tree | `a2d8c53ce5633ef0b62fb15ff33a45d2af51bc72` |

## Summary

The two new sidecars preserve the extracted behavior and keep authority with the original
application/state-machine boundaries. The three changed existing cards and both governing
overviews explain the ownership split. No compatibility copy, fallback reader, or alternate
publication path was introduced.

## Files Reviewed

| Onboarding File | Source Route/File | Result |
| --- | --- | --- |
| `mcp/src/agents_remember/application/worktree_tool_requests.py.md` | `mcp/src/agents_remember/application/worktree_tool_requests.py` | pass |
| `mcp/src/agents_remember/application/worktree_tools.py.md` | `mcp/src/agents_remember/application/worktree_tools.py` | pass |
| `mcp/src/agents_remember/mcp/registration/closeout.py.md` | `mcp/src/agents_remember/mcp/registration/closeout.py` | pass |
| `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py.md` | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py` | pass |
| `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py.md` | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py` | pass |
| `mcp/src/agents_remember/application/overview.md` | `mcp/src/agents_remember/application` | pass |
| `mcp/src/agents_remember/worktrees/integration/overview.md` | `mcp/src/agents_remember/worktrees/integration` | pass |

## Compliance Checklist

| Check | Result | Notes |
| --- | --- | --- |
| Durable overview placement is route-local and mirrored | pass | Existing governing pillars refreshed. |
| File-level onboarding is strict 1-to-1 | pass | Two new source files, two new sidecars. |
| File onboarding backlinks to nearest governing overview | pass | Application and integration parents. |
| Overview downlinks/route recovery cover new files | pass | Body plus regenerated indexes. |
| Durable onboarding contains no task-local planning | pass | Only stable ownership and invariants retained. |
| Docs References cite direct evidence | pass | Explicitly no external source configured. |
| Repo-Internal References use same-repo evidence only | pass | Source paths and exact ranges. |
| Cross-Repo References prove real boundaries | pass | None claimed. |
| No registry or embedding hit used as proof | pass | Registry used only for routing. |
| No absolute filesystem paths | pass | All durable paths are repository-relative. |
| Update History is append-only | pass | Newest entries prepended. |
| LOW-confidence claims are not stated as facts | pass | No unresolved claims. |
| Deferred files are recorded | pass | None in this bounded split. |
| STATE.md updated | pass | Source candidate and wave disposition refreshed. |

## Reference Health

All new citation targets exist in source commit `23d35f77`. Existing closeout request-model
references were repointed from the former definition site to `worktree_tool_requests.py`.

## Required Fixes

None.

## Next-Wave Recommendation

Proceed to route-index refresh, memory commit, and the exact-candidate full Dagger rerun.
