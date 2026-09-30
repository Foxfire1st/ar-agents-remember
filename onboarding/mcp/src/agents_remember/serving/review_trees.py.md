# mcp/src/agents_remember/serving/review_trees.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/review_trees.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:15:39+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `mcp/src/agents_remember/serving/overview.md` |

## Governing Overview

[serving route overview](overview.md)

## Purpose

**The reviewer's tree view route, `GET /api/review/trees` (MIK-R25).** Transport only, like the other reviewer
routes: it takes the task context (`repo`, `master`, `leaf` — never a path), optionally `comparison=<n>` to
reopen a recorded comparison or `history=recorded` for the leaf's latest record, calls the `ReviewTreesPort` the
composition root wires (`cli/dashboard.py`: `application/review_tree_knowledge.read_review_trees`), and serializes
the typed `ReviewTreesResult` once (`by_alias`, `exclude_none`).

**Since MIK-L31, `invariants=<ids>`** (comma-separated identities, as the landed review payload addresses
invariants) asks for those invariants' entries only, on both code sides with their excerpts: the focused expression
cards of one selection (ruling 2026-09-30T05:36:19 Q2). The client sends it with the payload's own
`comparison=<n>`.

## Code Commentary

### Logic

- Every typed answer is a 200: `trees`, `not-converted` (the leaf's memory is unconverted, so its review is the
  dataset review) and `refused` (the owner's refusal in the body).
- A process composed without the port answers 503 with `status: "unavailable"` (`_UNWIRED`), because then no
  answer exists at all.
- The three query parameters arrive as one `ReviewTreesSelection` (a FastAPI `Depends()` value), checked as one
  question by `problem()`: a `history` other than `recorded` or a negative `comparison`, more than
  `MAX_ENTRY_INVARIANTS` (500) named invariants, or any named key longer than `MAX_INVARIANT_KEY_LENGTH` (64
  characters; identities are 36; review F10 at 2026-09-30T06:10:21) is a 400 `invalid-request` whose `detail` names
  the problem. `named()` splits the list and drops empty keys; the query carries it as `invariants`.
- `register_review_trees_route` must be called before the greedy static mount; `serving/app.py` registers it right
  after the review summary route, with `collaborators.review_trees` (`serving/_app_common.py`).

### Conventions

- The query is a frozen `ReviewTreesQuery`; the port is a plain callable, as for the other reviewer ports.

### Invariants And Boundaries

- The route reads; the pinning it may cause is the application's (rule 1: a live candidate is pinned before the
  comparison is shown), bounded and idempotent by ruling 22:22:37 Q5 and review F6.

### Todos

- **Resolved by MIK-L31 (review F9):** the application re-keys the embedded documents, so the body is snake_case
  throughout.

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
| The route path, the query with the named invariants (MIK-R31), and the port type. | `KNOWLEDGE_REVIEW_TREES_ROUTE`; `ReviewTreesQuery`; `ReviewTreesPort` | mcp/src/agents_remember/serving/review_trees.py:34-34; mcp/src/agents_remember/serving/review_trees.py:41-51; mcp/src/agents_remember/serving/review_trees.py:54-54 |
| The unwired answer: no comparison rather than an empty one. | `_UNWIRED` | mcp/src/agents_remember/serving/review_trees.py:56-63 |
| The bounds and the one selection value: at most 500 invariants, each key at most 64 characters. | `MAX_ENTRY_INVARIANTS`; `MAX_INVARIANT_KEY_LENGTH`; `ReviewTreesSelection`; `NO_SELECTION` | mcp/src/agents_remember/serving/review_trees.py:36-36; mcp/src/agents_remember/serving/review_trees.py:38-38; mcp/src/agents_remember/serving/review_trees.py:66-93; mcp/src/agents_remember/serving/review_trees.py:96-96 |
| The route: 503 unwired, 400 with the selection's own problem, otherwise the typed result. | `register_review_trees_route` | mcp/src/agents_remember/serving/review_trees.py:99-134 |
| The registration beside the other reviewer routes. | `register_review_trees_route` | mcp/src/agents_remember/serving/app.py:306-306 |
| The route served over the port, the cards read passing its invariants, 400 for a 65-character key and for 501 keys, and refused when unwired. | `test_the_tree_view_route_serves_the_port_and_refuses_when_unwired` | mcp/tests/test_review_git_trees.py:730-776 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T12:15:39+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`): No content impact: this card's own source is unchanged. MIK-R29 grew `mcp/src/agents_remember/serving/app.py` (one import and one route registration), so the citation rows into it that moved were re-pointed by the installed fixer's normalisation or by the exact base-to-staged line shift; every re-pointed row was checked to hold its anchors in the new range, and no claim was reworded. No verification stamp was advanced.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Purpose and Logic record `invariants=` (ruling 05:36:19 Q2: the on-demand cards read, at most 500 keys), the one `ReviewTreesSelection` value and its `problem()`, and the per-key bound of 64 characters (review F10 at 06:10:21); the F9 Todo is marked resolved. **Reopened claims reworded:** the query row and the route row; this pass's two generated bullets for them were removed. One row added (the bounds and the selection); the route-test row reworded.
- 2026-09-30T07:53:49+00:00: Generated citation repair: `_UNWIRED` repointed to mcp/src/agents_remember/serving/review_trees.py:56-63. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new file MIK-R25 adds, recording ruling 22:22:37 Q5 and review F6 and F9. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
