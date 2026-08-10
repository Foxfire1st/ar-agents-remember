# test_identity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_identity.py`               |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-04T23:15+02:00|
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../overview.md`                              |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The provider identity helpers under test. | `provider_instance_id`; `scoped_name` | mcp/src/agents_remember/kernel/primitives/identity.py:31-57; mcp/src/agents_remember/kernel/primitives/identity.py:109-120 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 1 citation row to the provider identity helpers; scoped citation fixing regenerated the source ranges.

- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-04T23:15+02:00: Added coverage for dotted release worktree names, asserting provider instance IDs replace dots with hyphens before being used in Docker Compose project names. Verification metadata pinned until closeout.
- 2026-06-01T13:30+02:00: Created with the `scoped_name` DNS-label bound (mcp 1.0.1). Verification metadata pinned to the last committed source until closeout.
