# PDLS Governing Route Map

| Source route | Governing onboarding |
| --- | --- |
| repository-wide guidance | `onboarding/overview.md`, `system/tools.md` |
| `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, design docs | `onboarding/overview.md` |
| `mcp` | `onboarding/mcp/overview.md` |
| `mcp/src/agents_remember/testing` | `onboarding/mcp/src/agents_remember/testing/overview.md` |
| `mcp/src/agents_remember/code_quality` | `onboarding/mcp/overview.md` plus exact sidecars |
| `mcp/src/agents_remember/models/conversations` | `onboarding/mcp/src/agents_remember/models/conversations/overview.md` |
| `mcp/src/agents_remember/application` | `onboarding/mcp/src/agents_remember/application/overview.md` |
| `mcp/src/agents_remember/application/memory_quality` | application overview; focused packaging does not create a second authority |
| `mcp/src/agents_remember/models/closeout` | `onboarding/mcp/src/agents_remember/models/overview.md` |
| `mcp/src/agents_remember/worktrees/integration` | `onboarding/mcp/src/agents_remember/worktrees/integration/overview.md` |
| `mcp/src/agents_remember/worktrees/integration/closeout` | integration overview plus exact moved sidecars |
| `mcp/src/agents_remember/worktrees/integration/lifecycle/{control,observation,worker}` | integration overview plus exact owner sidecars |
| `mcp/src/agents_remember/worktrees/modules` | `onboarding/mcp/src/agents_remember/worktrees/modules/overview.md` |
| `mcp/src/agents_remember/worktrees/modules/quality` | modules overview plus exact moved sidecars |
| `mcp/tests` | `onboarding/mcp/tests/overview.md` |

The testing route remains the sole new governing pillar. The final package splits preserve
existing parent-route governance because they separate file ownership and size without creating a
new API or lifecycle authority. Exact one-to-one sidecars carry the moved behavior; file cards are
reserved for the newly extracted high-risk owners.
