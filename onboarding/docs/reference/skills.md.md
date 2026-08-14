# docs/reference/skills.md

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| repository             | agents-remember                         |
| path                   | `docs/reference/skills.md`              |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-07-08T01:00+02:00                  |
| lastVerifiedCommitHash |                                         `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |                                         2026-08-14T14:36:50+02:00|
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
Workflow Skills table describes `l-01-agent-lifecycles` with the current **HFX-L7** role census and
routing: three router conditions (spawn-role env → fresh role brief → otherwise architect), **nine**
per-role lifecycles — architect · backend orchestrator · designer · strategist · manager · worker ·
curator · **system-specialist** · adversarial reviewer — with the architect lifecycle (request →
trust-checkpoint → reframe-research → decide → build → close) owning the developer-facing
research-only exit and build decision, backend orchestrators running as spawned seats, and the
new **system-specialist** seat (260707-HFX-L7) as the investigate-first provider-degradation
responder: it reports first and fixes only on explicit orchestrator order, is never developer-facing,
and escalates directly to the orchestrator (one rung, matching `_ROLE_ESCALATION` in
`orchestration_artifacts.py`). `w-02-light-task-workflow` is
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical role registry and three-condition router this page summarizes. | `# l-01-agent-lifecycles — The Agent Lifecycles` | skills/l-01-agent-lifecycles/SKILL.md:6-416 |
| Sync script the page instructs running after skill edits. | "class SkillTarget" | scripts/sync-skills.py:27-27 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-08T01:00+02:00 — 260707-HFX-L7 curator memory pass: the source page's l-01 row now
  lists all nine roles including **system-specialist**, the provider-degradation investigate-first
  seat that reports first and fixes only on explicit orchestrator order; sidecar census updated
  from HFX-L6 (eight roles) to HFX-L7 (nine roles). Verification metadata pinned until closeout
  stamps the HFX-L7 commit.
- 2026-07-07T22:50+02:00 — Created by the 260707-HFX-L6 curator memory pass: the source page's
  l-01 row (updated in builder round L6R5) now lists all eight roles including **curator** and the
  architect/backend-orchestrator routing; sidecar records that census. Verification metadata
  pinned until closeout stamps the HFX-L6 commit.
