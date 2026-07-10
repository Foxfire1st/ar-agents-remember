# mcp/tests/test_orchestration_comms.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_orchestration_comms.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-08T01:00+02:00 |
| lastVerifiedCommitHash |                                            `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`|
| lastVerifiedCommitDate |                                            2026-07-10T22:30:19+02:00|
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
records an event and queues a manager-addressed inbox message. As of 260703-L12
it also pins the strategist rung: `test_strategist_escalates_to_orchestrator`
asserts an `escalation_packet(from_role="strategist", ...)` routes to the
orchestrator (the new `OrchestrationRole` literal's ladder entry). HFX-L6 adds
`test_orchestrator_escalates_to_architect` and `test_architect_escalates_to_developer`
to pin the new architect rung. L6R4 adds `test_curator_escalates_to_manager` so the
dedicated onboarding-writer seat is typed by the artifact helper and returns blockers to the
owning manager. 260707-HFX-L7's R2 fix round adds `test_system_specialist_escalates_to_orchestrator`
(closes reviewer F5): asserts `escalation_packet(from_role="system-specialist", ...).toRole ==
"orchestrator"`, pinning the provider-degradation investigator's escalation rung.

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

As of the 260703-L9 lifecycle convergence, the artifact-helper test pins the turn-report template path under `runtime/skills/l-01-agent-lifecycles/templates/` (the unified skill folder that replaced the l-02 tree).

## Update History

- 2026-07-08T01:00+02:00 — 260707-HFX-L7 R2 fix round (closes reviewer F5): added
  `test_system_specialist_escalates_to_orchestrator` pinning the new
  `system-specialist -> orchestrator` escalation rung in `escalation_packet`. Verification
  metadata pinned until closeout stamps the HFX-L7 commit.
- 2026-07-07T22:21+02:00 — 260707-HFX-L6R4 curator spawnability fix: added
  `test_curator_escalates_to_manager` for the artifact helper's curator role/escalation coverage.
  Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: added
  escalation tests for orchestrator -> architect and architect -> developer, matching the
  updated backend-to-owner ladder. Verification metadata pinned until closeout stamps the
  HFX-L6 commit.

- 2026-07-06T15:35+02:00 — 260703-L12 (three-party loops): added `test_strategist_escalates_to_orchestrator` pinning the new strategist ladder rung in `escalation_packet`. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: the pinned turn-report template path expectation moved to runtime skills/l-01-agent-lifecycles/templates/. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T12:31+02:00 - L3: created orchestration communication helper coverage. Verification metadata pinned until closeout stamps the L3 commit.
