# mcp/src/agents_remember/worktrees/modules/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `ebe9ef2aa882b5ed6df6dcb2491452efc0cf5c30` |
| lastVerifiedCommitDate | 2026-06-10T07:59:14+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Defines shared dataclasses used by the worktree lifecycle modules.

## Code Commentary

`WorktreeCommandResult` is the result envelope consumed by MCP controllers and
CLI adapters. `WorktreeProviderSetupConfig` carries MCP-derived provider setup
roots into worktree start preparation without rebuilding CLI arguments.
`SidecarBodyClassification` types the closeout body gate's
stale/untraced/attested-no-impact result consumed by closeout payloads;
`RouteOverviewBodyClassification` adds `stamped_without_body_review` for
route overviews matched only as ancestors of changed paths.

`WorktreeProviderSetupConfig.unlink_settings_after_setup` (default False)
marks the settings path as a controller-owned temp file whose lifetime must
extend into the background setup thread, which then owns the unlink
(GitHub #53).

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP skill tools type result envelopes and provider setup config through this facade-exported model. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-06-10T07:30+02:00 — `WorktreeProviderSetupConfig` gained `unlink_settings_after_setup` (default False): marks the settings path as a controller-owned temp file whose lifetime must extend into the background setup thread, which then owns the unlink (GitHub #53).
- 2026-06-10T05:20+02:00 — Issue #56 sub-task 2: added `RouteOverviewBodyClassification` (stale / untraced / attested_no_impact / stamped_without_body_review).
- 2026-06-10T04:47+02:00 — Added `SidecarBodyClassification` (stale / untraced / attested_no_impact) for the issue #56 four-case sidecar body gate.
- 2026-05-29T18:35+02:00: Added the onboarding refresh-plan TypedDicts (`OnboardingRefreshPlan`, `RouteOverviewRefreshPlan`, `EntityFingerprintRow`, `EntityFingerprintRequiredItem`, `EntityFingerprintRefreshPlan`); behavior-preserving (commit `0549b28`).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
