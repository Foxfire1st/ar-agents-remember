# test_identity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_identity.py`               |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T13:30+02:00|
| lastVerifiedCommitHash | `6bca8938635734072b08955f9dc47ebdaba763fd` |
| lastVerifiedCommitDate | 2026-06-01T14:01:01+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_identity.py` verifies that `scoped_name` keeps provider container/host/network
names within the 63-char DNS label limit, the constraint that the worktree
`label too long` crash exposed.

## Code Commentary

### Logic

The tests assert that a short scoped name is returned unchanged, that a long
worktree-scoped name (the FalkorDB host case that produced FalkorDB
`label too long`) is capped to `MAX_SCOPED_NAME` (63), that the cap is
deterministic for identical inputs, and that two distinct long inputs still
produce distinct (and still bounded) names so worktree instances cannot collide.

### Invariants And Boundaries

These tests protect the DNS-label invariant for scoped provider names: any name
used as a container/network hostname must stay ≤ 63 chars, and the bounding must
be deterministic and collision-safe rather than a lossy truncation.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The bounded helper under test. | [identity.py](agents-remember-md/mcp/src/agents_remember/providers/identity.py) |

## Update History

- 2026-06-01T13:30+02:00: Created with the `scoped_name` DNS-label bound (mcp 1.0.1). Verification metadata pinned to the last committed source until closeout.
