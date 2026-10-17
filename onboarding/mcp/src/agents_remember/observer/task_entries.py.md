# mcp/src/agents_remember/observer/task_entries.py

[governing overview](overview.md)

## Purpose

Produce the single server-side join of authored task stage, worktree binding, host activity, membership and counts.

## Commentary

Authored planning/inProgress/abandoned/Completed map to planned/started/aborted/completed; only started joins activity. Unknown host means unknown; in-turn/permission means works; otherwise known host means paused. Qualified documents override declared row fallback. Worktrees bind by repo/exact taskRoot/leaf ID; others stay unbound. Declared list order and unique commanded-master matches form one deterministic parent-per-child acyclic forest. A documented subTask's own qualified master governs its parent admission. For those subTasks only, a genuinely absent master falls back to the listing master; a present contrary or unresolvable master is preserved, reported and not adopted. Other listed document kinds are not rejected by this path and use the list subject to the existing identity/cycle guards; their own master field does not control placement. Conflicts remain single-placement and cycle-safe; unlisted records remain reachable as roots. Server counts produced entries; clients do not rebuild status/membership. This join retains the selected contributing eventAt but does not calculate or serve task-event ageSeconds; TaskStatusWord derives its display age from that event time in the browser.

The declaring master receives structured `disagreements` for a documented subTask whose own master disagrees, for its present master literal that resolves to no document, and for a subTask that names a master but is missing from that master's list. The producer suppresses repeats by `(declaring master key, disagreement.model_dump_json())`, so differences in any served disagreement field remain distinct, independently of forest placement. `TaskDocumentSource.master_literal` preserves the distinction lost by `declared_parent=None`; `serving/projections/snapshots_impl/_task_documents.project_task_sources` supplies that original text. Serving these facts neither edits a task document nor lets the client repair membership.

## Evidence

- The source distinguishes an absent master from a present unresolvable master and carries the original literal into list/record reconciliation. [3]
- Documented-subTask admission respects its own master, reports its contrary/unresolvable input and deduplicates complete reports; other listed kinds use list placement under identity/cycle guards. [4]

- Produce the single server-side join of authored task stage, worktree binding, host activity, membership and counts. [1]

- Task event time is served; display age is computed by the browser. [2]
