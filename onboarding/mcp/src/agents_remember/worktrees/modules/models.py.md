# mcp/src/agents_remember/worktrees/modules/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-12T19:06+02:00     |
| lastVerifiedCommitHash | `6f1a7e9028d5d4858cf9c645f2448d5395fafc6a` |
| lastVerifiedCommitDate | 2026-06-12T19:52:16+02:00|
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

`OnboardingRefreshPlan` carries the two-tier closeout split (issue #83):
`missing`/`unsupported` block and are scoped to working-tree paths, while
`unonboarded` collects committed-range paths without existing onboarding —
reported, never blocking, so transported history cannot force whole-repository
onboarding. `PATH_SAMPLE_LIMIT` (30) caps the payload exposure of lists that
scale with transported history; closeout exposes them as count + sample while
the plans keep full lists internally.

`WorktreeProviderSetupConfig.unlink_settings_after_setup` (default False)
marks the settings path as a controller-owned temp file whose lifetime must
extend into the background setup thread, which then owns the unlink
(GitHub #53).

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP skill tools type result envelopes and provider setup config through this facade-exported model. | [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-06-12T19:06+02:00 — Issue #83: `OnboardingRefreshPlan` gained the non-blocking `unonboarded` list (committed-range paths without onboarding) and the module gained `PATH_SAMPLE_LIMIT` (30) for count+sample payload bounding.
- 2026-06-10T07:30+02:00 — `WorktreeProviderSetupConfig` gained `unlink_settings_after_setup` (default False): marks the settings path as a controller-owned temp file whose lifetime must extend into the background setup thread, which then owns the unlink (GitHub #53).
- 2026-06-10T05:20+02:00 — Issue #56 sub-task 2: added `RouteOverviewBodyClassification` (stale / untraced / attested_no_impact / stamped_without_body_review).
- 2026-06-10T04:47+02:00 — Added `SidecarBodyClassification` (stale / untraced / attested_no_impact) for the issue #56 four-case sidecar body gate.
- 2026-05-29T18:35+02:00: Added the onboarding refresh-plan TypedDicts (`OnboardingRefreshPlan`, `RouteOverviewRefreshPlan`, `EntityFingerprintRow`, `EntityFingerprintRequiredItem`, `EntityFingerprintRefreshPlan`); behavior-preserving (commit `0549b28`).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
