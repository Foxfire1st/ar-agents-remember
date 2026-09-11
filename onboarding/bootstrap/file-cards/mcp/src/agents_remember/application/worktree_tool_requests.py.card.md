# File Card — mcp/src/agents_remember/application/worktree_tool_requests.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/src/agents_remember/application/worktree_tool_requests.py` |
| targetOnboardingFile | `mcp/src/agents_remember/application/worktree_tool_requests.py.md` |
| generated | 2026-08-24T21:43+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | application request boundary |
| Risk | typed authority/input split |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-002 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/src/agents_remember/application/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |
| localArea | worktree application composition |

## Why This File Matters

[HIGH] The file becomes the only definition owner for seven request/default concepts extracted from
the oversized worktree application facade. Closeout approval/message separation and canonical
lifecycle-control vocabulary must survive the move.

## What The Worker Must Explain

- immutable task-start, lifecycle-control, closeout, and finalize concepts
- canonical public-model reconstruction
- approval/message separation
- absence of Git/journal/task mutation
- shared defaults and single-definition ownership

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/src/agents_remember/application/worktree_tool_requests.py` | yes | concrete behavior |
| Governing overview | `mcp/src/agents_remember/application/overview.md` | yes | application ownership |
| Former owner card | `mcp/src/agents_remember/application/worktree_tools.py.md` | yes | preserve moved knowledge |

## Files The Worker May Read

- `mcp/src/agents_remember/application/worktree_tool_requests.py`
- `mcp/src/agents_remember/application/worktree_tools.py`
- `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py`
- the three onboarding paths listed above

## Files The Worker Must Not Read Without Escalation

- unrelated application routes
- adjacent repositories
- broad historical task archives

## Required Onboarding Sections

- metadata and governing overview
- Purpose
- Code Commentary
- Invariants And Boundaries
- Docs References
- Repo-Internal References
- Cross-Repo References
- Update History

## Reference Expectations

| Section | Expected? | Evidence Source |
| --- | --- | --- |
| Docs References | no | no Domain Documentation configured |
| Repo-Internal References | yes | extracted owner and consuming facade |
| Cross-Repo References | no | no boundary owned |

## Known Traps

- Do not claim a second model or compatibility surface; definitions moved once.
- Do not collapse closeout approval into commit-message input.

## Questions To Resolve

None.

## Done When

- The exact sidecar exists and explains the single typed owner.
- The former owner's card and application overview describe the split.
- Route indexes include the new sidecar.
