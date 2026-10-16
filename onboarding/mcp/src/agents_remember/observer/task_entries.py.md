# mcp/src/agents_remember/observer/task_entries.py

[governing overview](overview.md)

## Purpose

Produce the single server-side join of authored task stage, worktree binding, host activity, membership and counts.

## Commentary

Authored planning/inProgress/abandoned/Completed map to planned/started/aborted/completed; only started joins activity. Unknown host means unknown; in-turn/permission means works; otherwise known host means paused. Qualified documents override declared row fallback. Worktrees bind by repo/exact taskRoot/leaf ID; others stay unbound. Declared order and unique commanded-master matches form one deterministic parent-per-child acyclic forest, respecting declared parent. Server counts produced entries; clients do not rebuild status/membership. This join retains the selected contributing eventAt but does not calculate or serve task-event ageSeconds; TaskStatusWord derives its display age from that event time in the browser.

## Evidence

- Produce the single server-side join of authored task stage, worktree binding, host activity, membership and counts. [1]

- Task event time is served; display age is computed by the browser. [2]
