# mcp/src/agents_remember/controlplane/orchestration_artifacts.py

| Field                  | Value                                                               |
| ---------------------- | ------------------------------------------------------------------- |
| repository             | agents-remember                                                     |
| path                   | `mcp/src/agents_remember/controlplane/orchestration_artifacts.py`   |
| doc_type               | `file-level-onboarding`                                             |
| lastUpdated            | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash |                                                                     `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |                                                                     2026-08-12T00:45:15+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The bundled turn-report template is the worker artifact shape. | `# Turn-Report Template` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/turn-report.md:1-57 |
| The bundled master-handover template is rendered by the helper. | `# Master-Handover-Packet Template` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/master-handover-packet.md:1-49 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: replaced the `n/a` table rows with
  exact template heading anchors (deleting the unresolvable `jobs/worker.md` row); exact
  non-fixing check returns zero findings.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/controlplane/orchestration_artifacts.py` since the L2 base commit is
  the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 4 line(s) and normalised string
  quoting to double quotes. Checked by parsing both revisions and comparing the abstract syntax
  trees (identical) and the comment tokens (identical), so no symbol, signature, default,
  decorator, control-flow branch, docstring, or assertion this card describes has moved, and every
  claim this card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 R2 fix round (closes reviewer F5, role-enum sibling
  gap): added `system-specialist` to `OrchestrationRole` and routed
  `system-specialist -> orchestrator` in `_ROLE_ESCALATION`, matching the SKILL.md escalation
  ladder the R1 builder pass had already landed in doctrine. Pinned by
  `test_system_specialist_escalates_to_orchestrator` in `test_orchestration_comms.py`.
  Verification metadata pinned until closeout stamps the HFX-L7 commit.
- 2026-07-07T22:21+02:00 — 260707-HFX-L6R4 curator spawnability fix: added
  `curator` to `OrchestrationRole` and routed curator escalations/blockers to `manager` in
  `_ROLE_ESCALATION`. Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: added
  `architect` to `OrchestrationRole` and changed the escalation ladder to route backend
  orchestrator and designer escalations through architect before developer. Verification
  metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-06T15:35+02:00 — 260703-L12 (three-party loops): `OrchestrationRole` gains the `strategist` literal and `_ROLE_ESCALATION` gains `strategist -> orchestrator`; covered by the new strategist-escalation test in `test_orchestration_comms.py`. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: template_path now resolves under runtime skills/l-01-agent-lifecycles/templates/ (the unified skill folder replaced l-02-agent-orchestration). Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T12:31+02:00 - L3: created the typed orchestration artifact and escalation packet helper card. Verification metadata pinned until closeout stamps the L3 commit.
