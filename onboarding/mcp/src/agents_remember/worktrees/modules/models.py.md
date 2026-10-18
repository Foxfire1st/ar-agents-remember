# mcp/src/agents_remember/worktrees/modules/models.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Shared lifecycle types also own CommitPublicationRefusal, parent of exact-tree and hook refusals.

## Code Commentary

`WorktreeCommandResult` supplies the MCP/CLI result envelope. `WorktreeProviderSetupConfig` carries application-derived setup roots and owns the optional delayed temporary-settings unlink flag. Legacy `SidecarBodyClassification` and `RouteOverviewBodyClassification` DTOs and their operational consumers were removed.

`OnboardingRefreshPlan` carries the two-tier closeout split (issue #83):
`missing`/`unsupported` block and are scoped to working-tree paths, while
`unonboarded` collects committed-range paths without existing onboarding —
reported, never blocking, so transported history cannot force whole-repository
onboarding. `PATH_SAMPLE_LIMIT` (30) caps the payload exposure of lists that
scale with transported history; closeout exposes them as count + sample while
the plans keep full lists internally.

`RouteOverviewRefreshPlan` retains required and missing-metadata list fields as a transport shape; current `_memory_refresh_preview` supplies both as empty. The type does not prove substantive body/history validation or verification stamping.

`VerifiedChange` is the frozen commit/date/changed-path/optional-working-path bundle built once by closeout and passed to `external_closeout_commits`. Current external refresh uses `changed_paths` for entity fingerprints and refreshes generated route indexes. The metadata-stamping consumers were removed; the retained DTO docstring alone does not imply an operational stamp.

`WorktreeProviderSetupConfig.unlink_settings_after_setup` (default False)
marks the settings path as an application-owned temp file whose lifetime must
extend into the background setup thread, which then owns the unlink
(GitHub #53).

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- MCP skill tools type result envelopes and provider setup config through this facade-exported model. [1]

- Retained frozen DTOs and plan list shapes do not imply the removed legacy classifiers or verification stamping. [2]
