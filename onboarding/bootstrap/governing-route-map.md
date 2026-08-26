# IAS Source-Pair Coordination Governing Route Map

| Source route | Governing onboarding | Action |
| --- | --- | --- |
| `mcp/src/agents_remember/worktrees` | `onboarding/mcp/src/agents_remember/worktrees/overview.md` | create parent pillar for activation/sync authority |
| `mcp/src/agents_remember/worktrees/activation` | `onboarding/mcp/src/agents_remember/worktrees/activation/overview.md` | create focused selector/admission/vacancy pillar after the structural-limit move |
| `mcp/src/agents_remember/worktrees/modules` | existing `onboarding/mcp/src/agents_remember/worktrees/modules/overview.md` | refresh public lifecycle composition |
| `mcp/src/agents_remember/worktrees/queue` | existing `onboarding/mcp/src/agents_remember/worktrees/queue/overview.md` | refresh disposable activation-aware projection |
| `mcp/src/agents_remember/worktrees/integration` | existing `onboarding/mcp/src/agents_remember/worktrees/integration/overview.md` | refresh source-pair serialization |
| `mcp/src/agents_remember/application` | existing `onboarding/mcp/src/agents_remember/application/overview.md` | refresh public application composition |
| `mcp/src/agents_remember/application/structural` | existing `onboarding/mcp/src/agents_remember/application/structural/overview.md` | refresh task-unlocked structural route |
| `mcp/src/agents_remember/application/task_docs` | existing `onboarding/mcp/src/agents_remember/application/task_docs/overview.md` | preserve wholly upstream task authoring |
| `mcp/src/agents_remember/models` | existing `onboarding/mcp/src/agents_remember/models/overview.md` | refresh strict activation/sync vocabulary |
| `mcp/src/agents_remember/models/structural` | existing `onboarding/mcp/src/agents_remember/models/structural/overview.md` | add the relocated selector identity/archive model |
| `mcp/src/agents_remember/mcp/registration` | existing `onboarding/mcp/src/agents_remember/mcp/registration/overview.md` | refresh public schema registration |
| `mcp/src/agents_remember/mcp/tools` | existing `onboarding/mcp/src/agents_remember/mcp/tools/overview.md` | refresh tool translation |
| `mcp/tests` | existing `onboarding/mcp/tests/overview.md` | refresh focused activation/sync/projection evidence |
| `docs/reference` | existing `onboarding/docs/reference/overview.md` | refresh graph-less activation operator guidance |
| `skills/c-09-git-worktree-manager` | new `onboarding/skills/c-09-git-worktree-manager/overview.md` | create canonical skill pillar and strict SKILL sidecar |
| `skills/l-01-agent-lifecycles` | existing route-local skill overviews | refresh changed doctrine files if retained |
| `mcp/src/agents_remember/package_data/runtime/skills` | broad `onboarding/mcp/overview.md` fallback used by existing cards | refresh changed installed-copy sidecars without duplicating canonical ownership |

## Placement Decision

The direct `worktrees` route now coordinates two load-bearing workflows: focused source-pair
activation under `worktrees/activation/` and root-level resumable synchronization. Its previous
fallback to the broad MCP overview is no longer sufficient, so it earns one parent route pillar.
The structural-limit consolidation gives activation its own child pillar; existing child overviews
remain the nearest governors for `modules`, `queue`, and `integration`, while the flat sync files
remain governed by the new parent pillar.

## Moved Or Deleted Routes

The activation model moved from `models/atomic_series_activation.py` to
`models/structural/atomic_series_activation.py`; the four activation owners moved from the flat
`worktrees/` route into `worktrees/activation/`, which also gained a package marker. Their sidecars
moved with their semantic histories. No old-path compatibility card or source forwarder remains.
