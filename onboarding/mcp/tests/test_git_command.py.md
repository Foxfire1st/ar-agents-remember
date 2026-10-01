# mcp/tests/test_git_command.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Safe Git execution and exact private-commit preparation contracts.

## Code Commentary

### Logic

A decoy selected through Git environment variables never receives the real commit. Timeout and concurrent candidate-index cases remain bounded and isolated. Private preparation preserves logical HEAD/index, normal hook execution, exact tree/parent and raw CRLF/signature commit bytes. Forged/cancelled authority, hidden index flags, physical drift and stale bindings refuse; a failed hook returns its original failure once.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Repository selectors are deliberately reset inside the test so fixture cleanup cannot mask the runner guard. Private commit creation does not itself publish protected refs or confer lifecycle authority.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- A commit lands in the real repository not the decoy. [1]
- An explicit timeout still bounds a stalled command. [2]
- Candidate tree isolates concurrent observers with one scratch namespace. [3]
- Exact private commit preserves logical state and normal hook policy. [4]
- Raw commit readback preserves crlf and opaque signature header. [5]
- Cancelled owner and forged capability start no commit. [6]
- Hidden index flags and changed physical bytes refuse commit. [7]
- Stale logical tip and rebound private metadata refuse before mutation. [8]
- Failed hook returns original failure and does not retry. [9]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
