# mcp/tests/tool_answer_l109_cases.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The L109 largest-case producers and the fixtures they pin: each producer rebuilds one largest answer from a hermetic fixture under the L109 answer directory, so the production tests can compare an operation-produced answer with a stored one.

## Code Commentary

The module fixes the git environment (`_L109_FIXED_GIT_ENV`) so a rebuilt repository produces stable hashes, and uses `_l109_git` with `_l109_commit_all` to build one. `_write_l109_largest_pair` writes a governed file with its card, sidecar and invariant, which is what makes the largest case large. Three producers rebuild the largest answers for reading AR files, reading knowledge and diffing knowledge. The mounted leaf file-read producer checks all twenty compact rows against the bound. Each row names a relative brief path marked missing. The memory files, tree and Git status agree before and after the call, and the briefs directory is absent in both observations. `_sanitize_l109_answer` normalizes scratch paths and volatile log fields while retaining stable Git identities.

## Invariants And Boundaries

The fixtures under `mcp/tests/fixtures/l109_tool_answers` and these producers are two halves of one comparison: the producers must not read the stored case to build it. The comparison normalizes scratch paths and volatile log fields. The fixture retains the committed Git identities.

## Evidence

### Repo-Internal References




- The producer checks the delivered bound and the twenty relative pointers with missing freshness. It compares the files, memory tree and Git status before and after the read. [1]






- The fixture normalizes scratch paths and volatile log fields while retaining stable Git identities. [2]
