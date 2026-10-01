# mcp/src/agents_remember/worktrees/modules/models.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Defines shared dataclasses used by the worktree lifecycle modules.

## Code Commentary

`WorktreeCommandResult` is the result envelope consumed by MCP application entry points and
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

`RouteOverviewRefreshPlan` is the combined route transaction plan: `required`
contains source-matched overviews and task-edited overviews discovered relative
to the verified memory baseline, while `missing_metadata` retains the exact
fail-closed verification-metadata worklist. The type carries plan membership;
the onboarding module separately proves substantive body/history evidence.

**`VerifiedChange` (frozen, 260731-EFA-L2)** is the landed code change that onboarding metadata is
stamped against: `commit`, `commit_date`, `changed_paths`, and `working_paths` (the working-tree
subset that gates closeout; `None` when the caller has no separate working set). Every refresher
needs the same four facts together, and splitting them let a caller stamp one commit's hash beside
another's path list. The closeout coordinator builds it once, then
`closeout_external.external_closeout_commits` and
`onboarding.refresh_onboarding_metadata` / `refresh_onboarding_metadata_for_context` /
`refresh_route_overview_metadata_for_context` all take it. `refresh_entity_fingerprints_for_context`
deliberately still takes `change.changed_paths` alone — it stamps no commit.

`WorktreeProviderSetupConfig.unlink_settings_after_setup` (default False)
marks the settings path as an application-owned temp file whose lifetime must
extend into the background setup thread, which then owns the unlink
(GitHub #53).

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- MCP skill tools type result envelopes and provider setup config through this facade-exported model. [1]
