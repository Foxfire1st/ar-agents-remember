# mcp/src/agents_remember/controlplane/orchestration_nudges.py

| Field                  | Value                                                             |
| ---------------------- | ----------------------------------------------------------------- |
| repository             | agents-remember                                                   |
| path                   | `mcp/src/agents_remember/controlplane/orchestration_nudges.py`    |
| doc_type               | `file-level-onboarding`                                           |
| lastUpdated            | 2026-07-04T12:31+02:00                                            |
| lastVerifiedCommitHash |                                                                   `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`|
| lastVerifiedCommitDate |                                                                   2026-07-07T05:26:14+02:00|
| governingOverview      | `overview.md`                                                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

Persists rate-limited orchestration nudge attempts for inactivity and missing
turn-report artifacts.

## Code Commentary

### Logic

`OrchestrationNudgeRecord` is the strict JSONL row (`ar-orchestration-nudge/v1`).
`OrchestrationNudgeStore` writes `workspace/orchestration-nudges.jsonl`, reads the
append-only log, finds the last sent row for the same target/subject/reason tuple,
and records a new attempt as `rate-limited` when it falls inside the caller's rate
window. `nudge_message(...)` formats the manager-facing stdin text, and
`missing_artifact(...)` is the small file-existence/empty check for turn reports.

### Conventions

The store follows the existing control-plane JSONL pattern: strict Pydantic row,
workspace-scoped log under the observer root, append for every attempt, and pure
helpers for message/artifact policy.

### Invariants And Boundaries

- Rate limiting keys on target agent/lifecycle, subject agent/lifecycle, and reason.
- Rate-limited attempts are still appended for auditability.
- This file records the nudge decision; push delivery is handled by the MCP tool
  through the operator inbox.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public nudge tool records these rows and emits the manager inbox message. | [orchestration.py](agents-remember/mcp/src/agents_remember/mcp/tools/orchestration.py) |
| Nudge events are written into the observer workspace event log. | [store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |

## Update History

- 2026-07-04T12:31+02:00 - L3: created the orchestration nudge store card for rate-limited manager nudges. Verification metadata pinned until closeout stamps the L3 commit.
