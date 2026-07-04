# mcp/src/agents_remember/controlplane/orchestration_artifacts.py

| Field                  | Value                                                               |
| ---------------------- | ------------------------------------------------------------------- |
| repository             | agents-remember                                                     |
| path                   | `mcp/src/agents_remember/controlplane/orchestration_artifacts.py`   |
| doc_type               | `file-level-onboarding`                                             |
| lastUpdated            | 2026-07-05T01:32+02:00 |
| lastVerifiedCommitHash |                                                                     `277f27a33b35aed8235cbb3c1ae2b5633cc88b22`|
| lastVerifiedCommitDate |                                                                     2026-07-05T01:30:08+02:00|
| governingOverview      | `overview.md`                                                       |

## Governing Overview

[overview.md](overview.md)

## Purpose

Defines typed orchestration hand-off artifacts for the L2 orchestration frame:
worker turn reports, manager master-handover packets, and structured escalation
packets.

## Code Commentary

### Logic

`TurnReportArtifact`, `MasterHandoverPacket`, and `EscalationPacket` are strict
Pydantic contracts. `template_path(...)` resolves the runtime
`l-01-agent-lifecycles/templates/` file, `turn_report_artifact(...)` derives
the standard `notes/reports/<leaf>-worker-report.md` path, `escalation_packet(...)`
routes one role up the worker -> manager -> orchestrator -> developer ladder, and
`render_master_handover_packet(...)` emits Markdown in the bundled master-handover
template shape.

### Conventions

The helpers are pure path/string builders. They do not create files, mutate task
documents, or decide orchestration state; callers write the returned artifacts in
their own workflow.

### Invariants And Boundaries

- Role escalation advances exactly one rung according to the L2 ladder.
- Leaf ids are sanitized only for the report filename; the artifact still carries
  the original `leafId`.
- The runtime template directory remains the source of the packet shapes.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The L2 worker job requires a durable turn report at hand-off. | [worker.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/jobs/worker.md) |
| The bundled turn-report template is the worker artifact shape. | [turn-report.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/turn-report.md) |
| The bundled master-handover template is rendered by the helper. | [master-handover-packet.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/master-handover-packet.md) |

## Update History

- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: template_path now resolves under runtime skills/l-01-agent-lifecycles/templates/ (the unified skill folder replaced l-02-agent-orchestration). Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T12:31+02:00 - L3: created the typed orchestration artifact and escalation packet helper card. Verification metadata pinned until closeout stamps the L3 commit.
