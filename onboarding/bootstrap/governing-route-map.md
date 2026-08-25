# PDLS Governing Route Map

| Source route | Governing onboarding | Action |
| --- | --- | --- |
| `mcp/src/agents_remember/application/lifecycle` | `onboarding/mcp/src/agents_remember/application/lifecycle/overview.md` | created |
| `mcp/src/agents_remember/code_quality` | `onboarding/mcp/src/agents_remember/code_quality/overview.md` | created |
| `mcp/src/agents_remember/models/closeout` | `onboarding/mcp/src/agents_remember/models/closeout/overview.md` | created |
| `mcp/src/agents_remember/testing` | `onboarding/mcp/src/agents_remember/testing/overview.md` | created |
| `mcp/src/agents_remember/worktrees/integration/closeout` | `onboarding/mcp/src/agents_remember/worktrees/integration/closeout/overview.md` | created |
| `mcp/src/agents_remember/worktrees/integration/legacy` | `onboarding/mcp/src/agents_remember/worktrees/integration/legacy/overview.md` | created |
| `mcp/src/agents_remember/worktrees/integration/lifecycle` | `onboarding/mcp/src/agents_remember/worktrees/integration/lifecycle/overview.md` | created |
| `mcp/src/agents_remember/worktrees/integration` | existing parent overview | refreshed with child routing |
| `mcp/tests` | existing `onboarding/mcp/tests/overview.md` | refresh for bootstrap/fan-out proof |
| `dashboard/src/test` | existing `onboarding/dashboard/src/overview.md` | refresh contract guard sidecar and its dependent snapshot sidecar |

## Placement Decision

The seven new pillars each govern a shared workflow or contract with multiple load-bearing files.
No overview was created for single-file helper folders. File sidecars link to the nearest pillar,
falling back to the existing parent overview where a child route does not earn its own owner.

## Moved Or Deleted Routes

The certifying pytest plugin moved from `agents_remember.testing` to the `agents_remember` package
root. There was no prior file sidecar to move. The new root sidecar records the certifying service
composition; the testing overview records the leaf-import/no-facade rule. The deleted old source
gets no retained compatibility document.
