# mcp/src/agents_remember/worktrees/modules/onboarding.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/onboarding.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T15:24+02:00                     |
| lastVerifiedCommitHash | `fee469fd8435b9b74e13264591a8c7c6c2773012` |
| lastVerifiedCommitDate | 2026-05-28T15:30:29+02:00|
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

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Drift checking verifies the same sidecar and entity fingerprint metadata maintained here. | [drift.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py) |
| Route index refresh is delegated to the generated route index builder. | [route_index.py](agents-remember-md/mcp/src/agents_remember/kernel/route_index.py) |
| Worktree tests cover missing sidecar blocking, metadata refresh, long paths, and entity fingerprint refresh. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-05-28T15:24+02:00: Updated after closeout began refreshing route overview metadata and generated route indexes before memory quality and memory commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
