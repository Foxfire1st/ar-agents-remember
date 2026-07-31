# mcp/src/agents_remember/controlplane/orchestration_nudges.py

| Field                  | Value                                                             |
| ---------------------- | ----------------------------------------------------------------- |
| repository             | agents-remember                                                   |
| path                   | `mcp/src/agents_remember/controlplane/orchestration_nudges.py`    |
| doc_type               | `file-level-onboarding`                                           |
| lastUpdated            | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash |                                                                   `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |                                                                   2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

Persists rate-limited orchestration nudge attempts for inactivity and missing
turn-report artifacts.

## Code Commentary

### 260707-HFX2-L12 CS-6 Update

`OrchestrationNudgeStore.read()` is now a dashboard-tolerant reader: one torn or legacy nudge row is skipped instead of raising through the supervisor/projection path, while valid rows remain available to the rate-limit lookup.

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

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/controlplane/orchestration_nudges.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 2 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-04T12:31+02:00 - L3: created the orchestration nudge store card for rate-limited manager nudges. Verification metadata pinned until closeout stamps the L3 commit.
