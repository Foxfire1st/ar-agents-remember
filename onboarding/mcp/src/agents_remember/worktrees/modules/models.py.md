# mcp/src/agents_remember/worktrees/modules/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

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

**`VerifiedChange` (frozen, 260731-EFA-L2)** is the landed code change that onboarding metadata is
stamped against: `commit`, `commit_date`, `changed_paths`, and `working_paths` (the working-tree
subset that gates closeout; `None` when the caller has no separate working set). Every refresher
needs the same four facts together, and splitting them let a caller stamp one commit's hash beside
another's path list. `closeout._external_closeout_commits` builds it once and
`onboarding.refresh_onboarding_metadata` / `refresh_onboarding_metadata_for_context` /
`refresh_route_overview_metadata_for_context` all take it. `refresh_entity_fingerprints_for_context`
deliberately still takes `change.changed_paths` alone — it stamps no commit.

`WorktreeProviderSetupConfig.unlink_settings_after_setup` (default False)
marks the settings path as an application-owned temp file whose lifetime must
extend into the background setup thread, which then owns the unlink
(GitHub #53).

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| MCP skill tools type result envelopes and provider setup config through this facade-exported model. | "def skills_install_tool" | mcp/src/agents_remember/application/skill_tools.py:11-11 |

## Update History

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 1 citation item; scoped citation check now passes.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `VerifiedChange(commit, commit_date, changed_paths, working_paths=None)` — the
  landed code change every onboarding refresher stamps against. Additive to this module; the
  signature changes land in `closeout.py` and `onboarding.py`. Verification metadata pinned until
  closeout stamps the L2 commit.
- 2026-06-12T19:06+02:00 — Issue #83: `OnboardingRefreshPlan` gained the non-blocking `unonboarded` list (committed-range paths without onboarding) and the module gained `PATH_SAMPLE_LIMIT` (30) for count+sample payload bounding.
- 2026-06-10T07:30+02:00 — `WorktreeProviderSetupConfig` gained `unlink_settings_after_setup` (default False): marks the settings path as a controller-owned temp file whose lifetime must extend into the background setup thread, which then owns the unlink (GitHub #53).
- 2026-06-10T05:20+02:00 — Issue #56 sub-task 2: added `RouteOverviewBodyClassification` (stale / untraced / attested_no_impact / stamped_without_body_review).
- 2026-06-10T04:47+02:00 — Added `SidecarBodyClassification` (stale / untraced / attested_no_impact) for the issue #56 four-case sidecar body gate.
- 2026-05-29T18:35+02:00: Added the onboarding refresh-plan TypedDicts (`OnboardingRefreshPlan`, `RouteOverviewRefreshPlan`, `EntityFingerprintRow`, `EntityFingerprintRequiredItem`, `EntityFingerprintRefreshPlan`); behavior-preserving (commit `0549b28`).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
