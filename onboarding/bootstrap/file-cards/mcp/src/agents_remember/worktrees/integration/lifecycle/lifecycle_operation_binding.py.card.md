# File Card — mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py` |
| targetOnboardingFile | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py.md` |
| generated | 2026-08-24T21:43+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | durability identity boundary |
| Risk | immutable publication evidence |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-002 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/src/agents_remember/worktrees/integration/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md` |
| localArea | lifecycle enclosure publication |

## Why This File Matters

[HIGH] The file owns the canonical identity/digest bytes used to prove enclosure locator and
manifest agreement. It must stay pure and must not become a second location or recovery authority.

## What The Worker Must Explain

- closed binding identity and predecessor handling
- canonical JSON and SHA-256 construction
- immutable versus mutable locator fields
- bounded conflict disclosure
- strict separation from state-machine I/O

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py` | yes | concrete behavior |
| Governing overview | `mcp/src/agents_remember/worktrees/integration/overview.md` | yes | lifecycle ownership |
| Former owner card | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py.md` | yes | preserve moved knowledge |

## Files The Worker May Read

- `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py`
- `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py`
- `mcp/src/agents_remember/models/lifecycles/enclosure.py`
- the three onboarding paths listed above

## Files The Worker Must Not Read Without Escalation

- unrelated lifecycle workers
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
| Repo-Internal References | yes | binding owner and consuming state machine |
| Cross-Repo References | no | no boundary owned |

## Known Traps

- Do not move path confinement, locking, reads, writes, or state transitions into the pure helper.
- Do not document the helper as a locator fallback or compatibility reader.

## Questions To Resolve

None.

## Done When

- The exact sidecar exists and explains the pure contract.
- The former owner's card and integration overview describe the split.
- Route indexes include the new sidecar.
