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
| `mcp/src/agents_remember/worktrees/integration` | `onboarding/mcp/src/agents_remember/worktrees/integration/overview.md` |
| `mcp/src/agents_remember/worktrees/modules` | `onboarding/mcp/src/agents_remember/worktrees/modules/overview.md` |
| `mcp/tests` | `onboarding/mcp/tests/overview.md` |

The testing route remains the sole new governing pillar. Code-quality owners stay under the MCP
overview because this master consolidates cross-owner semantics without creating another package
route. Exact one-to-one cards carry the high-risk implementation detail.
