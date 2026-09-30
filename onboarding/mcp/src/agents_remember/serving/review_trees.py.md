# mcp/src/agents_remember/serving/review_trees.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/review_trees.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:46:54+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `mcp/src/agents_remember/serving/overview.md` |

## Governing Overview

[serving route overview](overview.md)

## Purpose

**The reviewer's tree view route, `GET /api/review/trees` (MIK-R25).** Transport only, like the other reviewer
routes: it takes the task context (`repo`, `master`, `leaf` — never a path), optionally `comparison=<n>` to
reopen a recorded comparison or `history=recorded` for the leaf's latest record, calls the `ReviewTreesPort` the
composition root wires (`cli/dashboard.py`: `application/review_tree_knowledge.read_review_trees`), and serializes
the typed `ReviewTreesResult` once (`by_alias`, `exclude_none`).

## Code Commentary

### Logic

- Every typed answer is a 200: `trees`, `not-converted` (the leaf's memory is unconverted, so its review is the
  dataset review) and `refused` (the owner's refusal in the body).
- A process composed without the port answers 503 with `status: "unavailable"` (`_UNWIRED`), because then no
  answer exists at all.
- A `history` other than `recorded`, or a negative `comparison`, is a 400 `invalid-request`.
- `register_review_trees_route` must be called before the greedy static mount; `serving/app.py` registers it right
  after the review summary route, with `collaborators.review_trees` (`serving/_app_common.py`).

### Conventions

- The query is a frozen `ReviewTreesQuery`; the port is a plain callable, as for the other reviewer ports.

### Invariants And Boundaries

- The route reads; the pinning it may cause is the application's (rule 1: a live candidate is pinned before the
  comparison is shown), bounded and idempotent by ruling 22:22:37 Q5 and review F6.

### Todos

- **L31 (review F9):** the body mixes snake_case model fields with camelCase embedded documents.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R25@v1` with its rulings in `25_reviewer-on-git-trees.json`; they live outside the code and memory
repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The route path, the query and the port type. | `KNOWLEDGE_REVIEW_TREES_ROUTE`; `ReviewTreesQuery`; `ReviewTreesPort` | mcp/src/agents_remember/serving/review_trees.py:31-45 |
| The unwired answer: no comparison rather than an empty one. | `_UNWIRED` | mcp/src/agents_remember/serving/review_trees.py:47-54 |
| The route: 503 unwired, 400 invalid, otherwise the typed result. | `register_review_trees_route` | mcp/src/agents_remember/serving/review_trees.py:57-88 |
| The registration beside the other reviewer routes. | `register_review_trees_route` | mcp/src/agents_remember/serving/app.py:305-305 |
| The route served over the port, and refused when unwired. | `test_the_tree_view_route_serves_the_port_and_refuses_when_unwired` | mcp/tests/test_review_git_trees.py:718-744 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new file MIK-R25 adds, recording ruling 22:22:37 Q5 and review F6 and F9. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
