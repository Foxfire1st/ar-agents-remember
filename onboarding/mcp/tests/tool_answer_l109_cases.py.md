# mcp/tests/tool_answer_l109_cases.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The L109 largest-case producers and the fixtures they pin: each producer rebuilds one largest answer from a hermetic fixture under the L109 answer directory, so the production tests can compare an operation-produced answer with a stored one.

## Code Commentary

The module fixes the git environment (`_L109_FIXED_GIT_ENV`) so a rebuilt repository produces stable hashes, and uses `_l109_git` with `_l109_commit_all` to build one. `_write_l109_largest_pair` writes a governed file with its card, sidecar and invariant, which is what makes the largest case large. Three producers rebuild the largest answers for reading AR files, reading knowledge and diffing knowledge, and `_sanitize_l109_answer` normalizes scratch paths and identities before comparison.

## Invariants And Boundaries

The fixtures under `mcp/tests/fixtures/l109_tool_answers` and these producers are two halves of one comparison: the producers must not read the stored case to build it. Every path and identity a scratch run invents is sanitized, so a difference reported is a shape or content difference.

## Evidence

### Repo-Internal References

- Each producer rebuilds one largest answer from a hermetic fixture with a fixed git environment. [1]

- The built answer is sanitized of scratch paths and identities before it is compared with the stored case. [2]
