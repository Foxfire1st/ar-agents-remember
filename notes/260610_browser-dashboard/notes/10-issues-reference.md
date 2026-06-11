# 10 — GitHub Issues Reference (dashboard-relevant threads)

| Field | Value |
| --- | --- |
| Topic | Status and key content of every issue thread feeding this feature |
| Status | Swept 2026-06-10 (`gh` over Foxfire1st/agents-remember-md, all states); re-check states before task creation — #54's fix landed via the other chat (MCP now 2.8.0, new `worktree_sync` tool) |

## The Map

| # | Title | State (at sweep) | Role for the dashboard |
| --- | --- | --- | --- |
| 2 | Browser Dashboard | OPEN, 0 comments | The wishlist. Its embedded mockup image is from the **older local mockup lineage** (developer call 2026-06-10: "wrong" mockup; copy removed from raw/) — the canonical advanced mockups are the `origin/browser-dashboard` files preserved at `raw/mockups/` |
| 43 | Design A2A control plane for observable AR lifecycle | OPEN, 0 comments | Lifecycle sessions as root tasks; gates as `input-required`; durable `sessions/<id>/events.jsonl` ("durable store is the truth, streams are projections"); dashboard approve/reject. Feeds notes 01/02/04 |
| 46 | Add MCP source/onboarding read packet tool | OPEN, 0 comments | Paired reads → observable, lifecycle-attributable (note 05). **Correction recorded: #46 has nothing to do with worktree_start** |
| 53 | worktree_start: ~6 min silence indistinguishable from hang | CLOSED | Developer direction in comments: **async shape** — return fast with `providerSetup: running`, poll `provider_status`/`worktree_status`; surface `seedFallback: full-reindex` with refusal reason. Origin of the boot-progress data the dashboard animates |
| 54 | worktree_start branches from stale local bases | OPEN at sweep; **fix task completed in parallel chat 2026-06-10** | The actual "remaining worktree_start issue" (active branch `issue-54-stale-bases`). Comment ties #53+#54: stale base defeats CGC seed (HEAD mismatch → 240.86s full reindex) making silence read as hang |
| 49 | memory_carryover tools hang (work completes, response never returns) | CLOSED | Context: stdio-pipe deadlock class; another "server did the work, client saw nothing" story reinforcing the observability theme |

## Issue #2 Mockup Image (context)

The image embedded in #2 is a light-theme three-pane "Workspace / Agent
Operations" console (operation tree | task detail with gate banner | provider
health + attention queue + event log; full description preserved in
`raw/recon-workflow-output.json` → `issues.mockupDescription`). Per developer
(2026-06-10) it belongs to the **older local mockup lineage** — treat it as an
ancestor of, not independent confirmation of, the `origin/browser-dashboard`
designs in `raw/mockups/`. The three-pane IA itself carries forward into those
canonical mockups (see note 07's screenshot map).

## Corrections / Clarifications Recorded

- The "remaining worktree_start issue" is **#54**, not #46 (developer
  misattribution corrected during recon; #54 matches the `issue-54-stale-bases`
  worktree that was active at the time).
- #53 is closed but its comments contain standing design direction (async
  setup + phase progress surfacing) that the dashboard work inherits.
- 2026-06-09 incident (recorded in onboarding update history, `status.py.md`):
  `context_packet` reported green over a 0-node CGC graph for 3 days → 2.5.0
  content-gated readiness (`indexed/indexing/empty/backend-unreachable`). That
  incident is the canonical "invisible fire" the alarm grammar exists to show.
