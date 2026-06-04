# test_identity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_identity.py`               |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-04T23:15+02:00|
| lastVerifiedCommitHash | `83b147e9ccc481749f7a3b40a27acf23cfe4296b` |
| lastVerifiedCommitDate | 2026-06-04T23:30:06+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_identity.py` verifies that provider identity helpers produce Docker-safe
provider instance and scoped names. It covers both the 63-char DNS label limit
and dotted worktree names that would otherwise leak into invalid Docker Compose
project names.

## Code Commentary

### Logic

The tests assert that a short scoped name is returned unchanged, that a long
worktree-scoped name (the FalkorDB host case that produced FalkorDB
`label too long`) is capped to `MAX_SCOPED_NAME` (63), that the cap is
deterministic for identical inputs, and that two distinct long inputs still
produce distinct (and still bounded) names so worktree instances cannot collide.
They also assert that a dotted release worktree runtime path derives
`projects-release-mcp-2-3-3-ar`, and that the resulting GrepAI Compose project
matches Docker Compose's lowercase alphanumeric / hyphen / underscore grammar.

### Invariants And Boundaries

These tests protect the provider naming invariants: generated instance IDs and
scoped names must be valid for Docker-backed lifecycle operations, names used as
container/network hostnames must stay ≤ 63 chars, and bounding must be
deterministic and collision-safe rather than a lossy truncation.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The provider identity helpers under test. | [identity.py](agents-remember-md/mcp/src/agents_remember/providers/identity.py) |

## Update History

- 2026-06-04T23:15+02:00: Added coverage for dotted release worktree names, asserting provider instance IDs replace dots with hyphens before being used in Docker Compose project names. Verification metadata pinned until closeout.
- 2026-06-01T13:30+02:00: Created with the `scoped_name` DNS-label bound (mcp 1.0.1). Verification metadata pinned to the last committed source until closeout.
