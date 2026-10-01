# mcp/src/agents_remember/controlplane/orchestration_artifacts.py

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
routes one role up the worker -> manager -> orchestrator -> architect -> developer ladder, and
`render_master_handover_packet(...)` emits Markdown in the bundled master-handover
template shape. As of 260703-L12 the `OrchestrationRole` literal carries
`strategist` (between `designer` and `orchestrator`) and `_ROLE_ESCALATION`
maps `strategist -> orchestrator` — the spawn-first sprint planner escalates
one rung to its spawner, like the designer and reviewer rungs.
As of HFX-L6 the literal also carries `architect`; `_ROLE_ESCALATION` maps
`orchestrator -> architect`, `architect -> developer`, and `designer -> architect`.
As of L6R4 the literal also carries `curator`; `_ROLE_ESCALATION` maps
`curator -> manager`, so onboarding-writer blockers return to the owning manager instead of
skipping a rung or falling outside the typed role set.
As of 260707-HFX-L7 (R2 fix round, closes reviewer F5) the literal also carries
`system-specialist`; `_ROLE_ESCALATION` maps `system-specialist -> orchestrator` — the
provider-degradation investigator escalates to its dispatcher, matching the SKILL.md escalation
ladder (`system-specialist → orchestrator`) that R1 had landed in doctrine without the matching
code-side enum/ladder entry.

### Conventions

The helpers are pure path/string builders. They do not create files, mutate task
documents, or decide orchestration state; callers write the returned artifacts in
their own workflow.

### Invariants And Boundaries

- Role escalation advances exactly one rung according to the L2 ladder.
- Leaf ids are sanitized only for the report filename; the artifact still carries
  the original `leafId`.
- The runtime template directory remains the source of the packet shapes.

## Evidence

### Repo-Internal References

- The bundled turn-report template is the worker artifact shape. [1]
- The bundled master-handover template is rendered by the helper. [2]
