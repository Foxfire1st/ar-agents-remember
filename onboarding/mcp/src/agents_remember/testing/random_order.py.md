# mcp/src/agents_remember/testing/random_order.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/random_order.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Provides deterministic pytest collection-order randomization shared by both testing routes. It
moved from the test tree so production plugins do not depend on test helpers.

## Code Commentary

`shuffle_items` uses a local `random.Random(seed)` instance and changes only the supplied item
list, preserving reproducibility without mutating the process-global RNG.

## Invariants And Boundaries

- The reported seed reproduces the exact order.
- No process-global random state is changed.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Collection order uses a local seeded RNG. | `shuffle_items` | mcp/src/agents_remember/testing/random_order.py:9-10 |

## Update History

- 2026-08-24T21:23+02:00 — Moved from `mcp/tests/_random_order.py` into shared production testing.
