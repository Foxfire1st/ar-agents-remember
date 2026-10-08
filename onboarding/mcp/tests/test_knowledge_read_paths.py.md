# mcp/tests/test_knowledge_read_paths.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Git path spelling and lookup failure remain distinct from an absent source.

## Code Commentary

### Logic

Leading-colon pathspec magic is refused at the test anchor-draft and production PathSeed boundaries; literal glob characters remain addressable. Fixture rows come from the test-only builder, not a canonical writer. [1] [2] [7]

Unsupported stored spelling is unsupported_locator. Missing tree objects, a Git process that cannot start, and non-zero lookup results are recorded_object_unavailable, never path_absent. The non-zero branch now has its own case. [3] [4] [5] [9]

### Invariants And Boundaries

- A refusal describes its actual cause.
- These tests protect readers and fixture input shapes, not production database write admission.

## Evidence

### Repo-Internal References


- Magic spelling refused at both typed boundaries. [1]


- Literal glob characters are addressable. [2]


- Unsupported stored spelling is not absence. [3]


- Unavailable tree is not absence. [4]


- Spawn failure is unavailable. [5]


- Anchor draft now belongs to test support. [7]


- Non-zero Git lookup has its own current case. [9]


### Cross-Repo References

No cross-repository contract is established by this file.
