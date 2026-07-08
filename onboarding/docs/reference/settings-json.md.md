# docs/reference/settings-json.md

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| repository             | agents-remember                         |
| path                   | `docs/reference/settings-json.md`       |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-07-08T23:59+02:00                  |
| lastVerifiedCommitHash |                                         |
| lastVerifiedCommitDate |                                         |
| governingOverview      | `../../overview.md`                     |

## Governing Overview

[root repo overview](../../overview.md) — the `docs/reference` route has no route-local overview
of its own (pre-existing registered gap; see the skills reference sidecar).

## Purpose

Public settings reference for Agents Remember. It separates the four settings homes (MCP
authority, memory topology, agentic orchestration, provider lifecycle), documents their read
cadence, and gives examples for internal/external memory and MCP authority files.

## Code Commentary

The page is documentation, not parser code. Runtime parsing lives in `kernel/agentic_settings.py`
for `orchestration.*` and the MCP authority/config loaders for boot infrastructure. HFX2-L8 adds the
`orchestration.supervisor` table documenting safe defaults for the deterministic supervisor sweep:
`enabled`, `intervalSeconds`, `staleCutoffSeconds`, `redeliverRateLimitSeconds`, and
`redeliverBudget` (default 250) so an empty supervisor block remains bounded during large inbox
backlogs.

## Invariants And Boundaries

- Settings families have exactly one home; do not present coordinator `system/settings.json` as an
  MCP authority file.
- Unknown keys under `orchestration.*` fail loud in the parser; docs must track parser field names.
- The supervisor redelivery budget is a conservative default, not a required operator knob.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Agentic settings parser that implements the documented `orchestration.*` families. | [../../mcp/src/agents_remember/kernel/agentic_settings.py](../../mcp/src/agents_remember/kernel/agentic_settings.py.md) |
| Serving app that reads supervisor settings per sweep. | [../../mcp/src/agents_remember/serving/app.py](../../mcp/src/agents_remember/serving/app.py.md) |
| Supervisor implementation consuming the redelivery budget. | [../../mcp/src/agents_remember/serving/supervisor.py](../../mcp/src/agents_remember/serving/supervisor.py.md) |

## Update History

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (settings docs): created sidecar after the settings
  reference gained the `orchestration.supervisor` section including `redeliverBudget` default 250
  and the safe-empty-block posture. Verification metadata pinned until closeout stamps the
  260707-HFX2-L8 commit.
