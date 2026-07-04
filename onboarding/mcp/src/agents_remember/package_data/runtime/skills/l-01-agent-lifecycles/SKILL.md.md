# l-01-agent-lifecycles/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T01:30+02:00 |
| lastVerifiedCommitHash | `277f27a33b35aed8235cbb3c1ae2b5633cc88b22` |
| lastVerifiedCommitDate | 2026-07-05T01:30:08+02:00|

## Purpose

The spine of the unified `l-01-agent-lifecycles` skill: lifecycle and job are ONE entity (one lifecycle per agent type). This file is the router + the minimal frame + the shared invariants; the per-role lifecycles live in `roles/`, the lenses in `lenses.md`, the report templates in `templates/`. It supersedes and replaces BOTH `l-01-session-job-lifecycle` and `l-02-agent-orchestration` (converged 2026-07-05, series 260703-L9).

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-01-agent-lifecycles/SKILL.md`. The router has exactly three conditions, in order: (1) `AR_SPAWN_ROLE` env set -> run `roles/<value>.md`; (2) first user message is a role brief -> run that role; (3) otherwise the session is developer-facing -> run `roles/orchestrator.md` (solo work is the degenerate portfolio). The minimal frame is the only shared machinery: the six `lifecycle_*` signals, fleeting->persistent promotion at `worktree_start`, `awaiting-developer` auto-resume on the next AR call, server-side identity; a spawned role that never touches mutating AR tools never instantiates a lifecycle (designed shape), and a spawned role never adopts its spawner's lifecycle - the session<->leaf association is the catalog binding via the QUALIFIED leaf key `<repository>/<master>/<docId>`. Shared invariants: continuity in task_doc + durable artifacts (never transcripts); the escalation ladder worker -> manager -> orchestrator -> developer with no rung skipped; decision-needing questions land in task-doc `openQuestions`. Also carries the knob-block/per-harness variant resolution (role base < `roles/<R>.<H>.md` < settings.json orchestration block), the as-built settings documentation (`orchestration.gateDelegation` parsed + enforced by `controlplane/gate_policy.py`; `roles`/`concurrency` documented schema with parsing tracked as backlog), a 6-line super-branch orientation diagram (the full topology's single home is `roles/orchestrator.md`), and the credits lineage (260619 spec -> Archon / agent-control-plane).

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: SKILL.md is now the unified-skill spine (router + minimal frame + shared invariants); body rewritten accordingly; supersedes the two retired skill spines. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T13:16+02:00 — 260703-L6 documented the adversarial seam procedures end to end: manager
  spawn at master-exit, orchestrator spawn at super-exit, `notes/reports/` verdict placement,
  `reviewer-verdict` gate evidence refs, policy-required verdict evidence, and block-to-fix-leaf routing
  back to the owning manager/orchestrator. Verification metadata pinned until closeout stamps the L6
  commit.
- 2026-07-04T13:03+02:00 — 260703-L5 expanded the frame's super integration branch topology from a
  summary into doctrine: super branches from main, masters branch from super, leaves branch from their
  master, C-11 is universal at every edge, dependent managers dispatch only after dependencies
  integrate into super, independent masters reconcile a moved super base, master-to-super integration
  runs in an orchestrator worktree, conflict resolution is either up-front foundation-master extraction
  or post-hoc super-worktree dedup with memory single-siding, leaf moves carry decision-log entries,
  and the final super-to-main PR includes main-memory carry-over plus push. Also recorded the
  260630-derived master finalize/archive and parallel-master reconcile items as sequenced follow-ups,
  not implemented behavior. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-04T11:00+02:00 — Created file-level onboarding for the new `l-02-agent-orchestration` skill
  (leaf 260703-L1), the developer-invoked, never-self-spawning frame that houses the five
  orchestration-family jobs via the four thin contact points (context → job selection → housed job
  execution → wrap-up). Captured the frame doctrine, the job registry, the coordination-leaf
  convention, the escalation ladder + orchestrator-only spirit test, the two adversarial seams, the
  gate-delegation doctrine (enforcement deferred to L4), the knob block + per-harness variant
  resolution, the settings.json orchestration schema block (schema doc only; parsing deferred to L4),
  the super integration branch topology summary (full topology owned by L5), the comms protocol
  (substrate implemented in L3), and the credits; noted `spawn_agent_session` is the L2 tool (not yet
  implemented). Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-02-agent-orchestration/SKILL.md`. Verification metadata pinned until closeout stamps the L1
  commit.
