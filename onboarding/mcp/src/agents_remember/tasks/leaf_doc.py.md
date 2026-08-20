# mcp/src/agents_remember/tasks/leaf_doc.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/tasks/leaf_doc.py` |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated | 2026-08-20T09:35+02:00 |
| lastVerifiedCommitHash | `a9d50e08b830c4a34c14e495706c19fe697f47ab` |
| lastVerifiedCommitDate | 2026-08-20T09:26:15+02:00 |
| governingOverview      | `overview.md`                               |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Leaf task-document lookup and lifecycle stamping (L11). A leaf's JSON-primary task
document is the lifecycle-keyed work content of its enclosure; this module makes that
binding survive restarts by explicit restamp — never by read-time heuristics.

## Code Commentary

### Logic

`find_leaf_doc(task_root, leaf_id)` scans the task root's `*.json` documents (skipping
masters and unparseable files) and returns the first whose authored `id`, any
`enclosures[]` ref `leafId`, or file stem equals the leaf id case-insensitively — the
same exact joins the observer projection uses, in the same order. The
case-insensitivity matters because doc ids are authored labels (`260628-L11`) while
enclosure leaf ids are lowercase directory names (`260628-l11`).
`restamp_leaf_doc_lifecycle(task_root, leaf_id, lifecycle_id)` points the found doc at
the given lifecycle, OVERWRITING any previous stamp (the enclosure's newest lifecycle
IS the doc's binding), re-rendering the markdown via `write_task_docs`; it returns a
small `{docPath, lifecycleId, changed}` report, or `None` when the leaf has no doc yet
(a first start authors the doc afterwards, already stamped by `task_doc`).

### Invariants And Boundaries

- Pure task-domain module: it imports only `tasks.document` and `tasks.store`, so
  `worktree_start` can import it along the existing worktrees→tasks dependency
  direction without cycles.
- Restamp is idempotent (`changed: false` when the stamp already matches) and total
  (overwrites a stale finalized-lifecycle stamp — a reopened leaf's doc must follow
  the fresh lifecycle, not the old one).
- Since 260815-DAG-L16 `resolve_terminal_leaf_doc` names the missing binding and the recovery
  (L16-R9): a blank leaf id refuses with "the leaf has no stamped contract binding — re-stamp the
  series contract (series-contract.md) or use branch-addressed mode for direct execution" instead
  of the opaque "terminal leaf resolution requires a nonblank leaf id".
## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The atomic reopen plan clears the doc's stamp before the next start restamps it. | `_plan_leaf_doc_reset` | mcp/src/agents_remember/worktrees/reopen.py:393-436 |
| The post-contract-write restamp call site in worktree start. | "restamp_leaf_doc_lifecycle(" | mcp/src/agents_remember/worktrees/modules/start.py:590-590 |
| The observer joins this lookup mirrors (doc id → enclosures[] refs → stem). | "def read_task_documents(" | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:63-63 |

## 260815-DAG-L3 Governed Lifecycle Restamp

`restamp_leaf_doc_lifecycle` now plans the same exact leaf-doc change but delegates publication to
an injected writer. Worktree start supplies the queue-governed task-fact publisher, so lifecycle
restamping cannot bypass an active sprint lane or atomic blocker; standalone tests can inject the
ordinary task-doc writer without duplicating policy.

## Update History


- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: `resolve_terminal_leaf_doc` blank-id refusal now names
  the missing binding and the recovery (L16-R9: re-stamp the series contract / use
  branch-addressed mode). Verified at code commit a9d50e08.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: documented publisher injection for queue-governed
  leaf lifecycle restamping; verification remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: updated the reopen reference to the current atomic
  `_plan_leaf_doc_reset` owner; leaf lookup and restart stamping remain unchanged. Verification
  remains closeout-owned.
- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 3 repository-reference citations (3/3 anchored and sourced; scoped citation check clean).

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-03T00:30+02:00 — Created for L11: exact case-insensitive leaf-doc lookup plus the explicit
  lifecycleId restamp worktree_start applies after (re)creating a leaf whose doc already exists.
  Verification metadata pinned until closeout stamps the code commit.
