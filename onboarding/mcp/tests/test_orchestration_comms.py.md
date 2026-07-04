# mcp/tests/test_orchestration_comms.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_orchestration_comms.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T12:31+02:00                     |
| lastVerifiedCommitHash |                                            `6b940141fc319f1d2d18b2c94fd9e9a213d43141`|
| lastVerifiedCommitDate |                                            2026-07-04T12:52:03+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Focused backend tests for the L3 orchestration communication helpers: artifact
paths, escalation routing, nudge rate limiting, observer events, and manager inbox
enqueueing.

## Code Commentary

### Logic

The suite pins the pure artifact helpers (`turn_report_artifact`,
`escalation_packet`), the missing-artifact check, `OrchestrationNudgeStore`
rate-limit behavior, and the `orchestration_nudge_manager_payload(...)` path that
records an event and queues a manager-addressed inbox message.

### Conventions

Tests use temporary observer roots and the existing conformance-test config
helpers so they exercise the real payload builder without touching a live
workspace.

### Invariants And Boundaries

- Missing turn reports are absent or zero-byte files.
- Rate-limited nudges are logged as such and do not create a second manager inbox
  entry.
- Payload tests assert the durable event and inbox rows, not frontend rendering.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Artifact and escalation helpers under test. | [orchestration_artifacts.py](agents-remember/mcp/src/agents_remember/controlplane/orchestration_artifacts.py) |
| Nudge store and message policy under test. | [orchestration_nudges.py](agents-remember/mcp/src/agents_remember/controlplane/orchestration_nudges.py) |
| Public nudge payload under test. | [orchestration.py](agents-remember/mcp/src/agents_remember/mcp/tools/orchestration.py) |

## Update History

- 2026-07-04T12:31+02:00 - L3: created orchestration communication helper coverage. Verification metadata pinned until closeout stamps the L3 commit.
