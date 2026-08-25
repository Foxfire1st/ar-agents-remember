# File Card — mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py` |
| targetOnboardingFile | `mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py.md` |
| generated | 2026-08-25T08:27+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | lifecycle cancellation mutation owner |
| Risk | worker authority escape or claimed-door corruption during recovery |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-004 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `mcp/src/agents_remember/worktrees/integration/overview.md` |
| ancestorOverviews | `overview.md`, `mcp/overview.md`, `mcp/src/agents_remember/worktrees/integration/overview.md` |
| localArea | lifecycle mutation control |

## Why This File Matters

[HIGH] It performs the cancellation transaction that makes a failed operation recoverable without
losing exact journal, worker, Git, or closeout-door authority.

## What The Worker Must Explain

- worker-exit proof before release
- exact claimed-door successor publication
- terminal idempotence and completed refusal
- organizational repair and dry-run boundaries

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py` | yes | exact mutation ordering and refusal behavior |
| Governing overview | `mcp/src/agents_remember/worktrees/integration/overview.md` | yes | lifecycle ownership boundary |
| Target sidecar | `mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py.md` | yes | durable one-to-one onboarding |

## Files The Worker May Read

- `mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py`
- `mcp/src/agents_remember/worktrees/integration/overview.md`
- `mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py.md`
- directly imported journal, worker, and closeout-door owners needed to prove ordering

## Files The Worker Must Not Read Without Escalation

- unrelated worktree lifecycle operations
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
| Docs References | no | transaction is repository-internal |
| Repo-Internal References | yes | cancellation owner plus journal, worker, and closeout-door consumers |
| Cross-Repo References | no | no adjacent-repository boundary is owned |

## Known Traps

- Do not treat cancellation as deleting a journal generation.
- Do not let queue or task-document state replace exact lifecycle evidence.

## Questions To Resolve

None.

## Done When

- Exact sidecar explains the mutation ordering and non-owners.
- Governing integration overview names the extracted control owner.
- Generated route indexes include the sidecar.
