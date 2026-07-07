# docs/reference/skills.md

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| repository             | agents-remember                         |
| path                   | `docs/reference/skills.md`              |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-07-07T22:50+02:00                  |
| lastVerifiedCommitHash |                                         |
| lastVerifiedCommitDate |                                         |
| governingOverview      | `../../overview.md`                     |

## Governing Overview

[root repo overview](../../overview.md) — the `docs/reference` route has no route-local overview
of its own (pre-existing registered gap; see the root overview's L16 history entry).

## Purpose

Public skills reference: where installed and canonical skill copies live, the
`scripts/sync-skills.py` sync step, the lifecycle/workflow and core skill tables, and the manual
`skills_install()` maintenance path.

## Code Commentary

The page documents the two skill locations (installed `ar-coordination/skills/`, canonical
`agents-remember/skills/`) and the sync command that refreshes the MCP package-data copy and every
harness starter package (pre-push runs `scripts/sync-skills.py --check`). The Lifecycle And
Workflow Skills table describes `l-01-agent-lifecycles` with the current HFX-L6 role census and
routing: three router conditions (spawn-role env → fresh role brief → otherwise architect), eight
per-role lifecycles — architect · backend orchestrator · designer · strategist · manager · worker ·
curator · adversarial reviewer — with the architect lifecycle (request → trust-checkpoint →
reframe-research → decide → build → close) owning the developer-facing research-only exit and
build decision, and backend orchestrators running as spawned seats. `w-02-light-task-workflow` is
the durable one-page plan that escalates to a master + light sub-task series. The Core Skills table
lists `c-00` through `c-13` one line each. The install section routes first-run setup to the
harness starter packages and manual maintenance installs through `skills_install()` (target
inferred from the MCP settings location; packaged skills are flat, one folder per skill).

## Invariants And Boundaries

- Public documentation, not runtime code; the canonical role/router doctrine lives in
  `skills/l-01-agent-lifecycles/SKILL.md` — this page must stay consistent with it.
- `docs/**` is excluded from file-level onboarding by the active path rules; this sidecar exists
  by explicit HFX-L6 manager instruction to cover the L6R5 role-list delta.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Canonical role registry and three-condition router this page summarizes. | [skills/l-01-agent-lifecycles/SKILL.md](../../../skills/l-01-agent-lifecycles/SKILL.md) |
| Sync script the page instructs running after skill edits. | [scripts/sync-skills.py](../../../scripts/sync-skills.py) |

## Update History

- 2026-07-07T22:50+02:00 — Created by the 260707-HFX-L6 curator memory pass: the source page's
  l-01 row (updated in builder round L6R5) now lists all eight roles including **curator** and the
  architect/backend-orchestrator routing; sidecar records that census. Verification metadata
  pinned until closeout stamps the HFX-L6 commit.
