# mcp/src/agents_remember/tasks/leaf_doc.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/tasks/leaf_doc.py` |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-08-02T01:05+02:00                      |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`  |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The reopen reset that clears the doc's stamp before the next start restamps it. | `_reset_leaf_doc` | mcp/src/agents_remember/worktrees/reopen.py:162-195 |
| The post-contract-write restamp call site in worktree start. | "restamp_leaf_doc_lifecycle(" | mcp/src/agents_remember/worktrees/modules/start.py:584-584 |
| The observer joins this lookup mirrors (doc id → enclosures[] refs → stem). | `read_task_documents` | mcp/src/agents_remember/observer/snapshots.py:1154-1182 |

## Update History
- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 3 repository-reference citations (3/3 anchored and sourced; scoped citation check clean).

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-03T00:30+02:00 — Created for L11: exact case-insensitive leaf-doc lookup plus the explicit
  lifecycleId restamp worktree_start applies after (re)creating a leaf whose doc already exists.
  Verification metadata pinned until closeout stamps the code commit.
