# mcp/src/agents_remember/worktrees/modules/onboarding.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/onboarding.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T07:36+02:00                     |
| lastVerifiedCommitHash | `b3dc26b0d809e6d386fd13adc77c8530f174b826` |
| lastVerifiedCommitDate | 2026-05-29T07:42:25+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Plans and applies closeout-time onboarding metadata, route overview metadata,
route index, and entity fingerprint refreshes for changed code paths.

## Code Commentary

The module finds changed source sidecars, validates required verification
metadata, updates `lastVerifiedCommitHash` and `lastVerifiedCommitDate`, parses
route overview metadata, updates affected route overviews, runs generated route
index refreshes, parses repo entity fingerprint tables, computes
`git-blob-set-v1` fingerprints, and updates affected entity rows after the code
commit exists.

It also enforces the closeout content gate via `require_updated_sidecar_content`:
when a changed source file's existing sidecar body was not modified in the task
(checked against the memory worktree's changed paths),
`validate_onboarding_refresh_plan_for_context` raises instead of advancing
verification metadata over stale content. The check accepts an explicit
`memory_tree` (the worktree wrapper passes the memory worktree) and safely skips
sidecars that do not resolve under that tree rather than reporting false stale
findings.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Drift checking verifies the same sidecar and entity fingerprint metadata maintained here. | [drift.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py) |
| Route index refresh is delegated to the generated route index builder. | [route_index.py](agents-remember-md/mcp/src/agents_remember/kernel/route_index.py) |
| Worktree tests cover missing sidecar blocking, metadata refresh, long paths, and entity fingerprint refresh. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-05-29T07:36+02:00: Added `require_updated_sidecar_content` and wired it into `validate_onboarding_refresh_plan_for_context` (direct and worktree) so a changed source file with an unmodified sidecar body fails closeout instead of receiving a metadata-only verification refresh.
- 2026-05-28T15:24+02:00: Updated after closeout began refreshing route overview metadata and generated route indexes before memory quality and memory commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
