# File Card — mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py` |
| targetOnboardingFile | `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py.md` |
| generated | 2026-08-25T08:27+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | total read-only lifecycle projection owner |
| Risk | damaged contract or task status hiding retained actionable operations |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-004 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/src/agents_remember/worktrees/integration/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md`, `mcp/src/agents_remember/worktrees/integration/overview.md` |
| localArea | lifecycle read projection |

## Why This File Matters

[HIGH] It preserves observable lifecycle state when mutable task or contract surfaces are damaged,
without granting unsafe controls or becoming a mutation owner.

## What The Worker Must Explain

- single/latest/all projection surfaces
- unreadable-contract retained evidence
- zero-control degraded projection
- derived worker/mutation recovery without writes

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py` | yes | total projection and degraded-read behavior |
| Governing overview | `mcp/src/agents_remember/worktrees/integration/overview.md` | yes | lifecycle observation boundary |
| Target sidecar | `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py`
- `mcp/src/agents_remember/worktrees/integration/overview.md`
- `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py.md`
- directly imported journal and lifecycle model owners needed to prove projection inputs

## Files The Worker Must Not Read Without Escalation

- unrelated lifecycle mutation routes
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
| Docs References | no | projection contract is repository-internal |
| Repo-Internal References | yes | projection owner and canonical journal/model inputs |
| Cross-Repo References | no | no adjacent-repository boundary is owned |

## Known Traps

- Do not document observation as journal authority.
- Do not infer lifecycle truth from queue rows or mutable task status.

## Questions To Resolve

None.

## Done When

- Exact sidecar explains total read behavior and its fail-closed boundary.
- Governing integration overview names the extracted observation owner.
- Generated route indexes include the sidecar.
