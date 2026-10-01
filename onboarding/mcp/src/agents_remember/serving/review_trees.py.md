# mcp/src/agents_remember/serving/review_trees.py

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

**Since MIK-L32, `lane=files` and `file=<path>`** ask the unexplained-changes lane (MIK-R32): `lane=files` its two
destinations, `file=<path>` the per-file classification of one changed path. Each names one focused question, so at
most one of `invariants`, `lane` and `file` is given; the client sends each with the payload's own `comparison=<n>`.

## Code Commentary

### Logic

- Every typed answer is a 200: `trees`, `not-converted` (the leaf's memory is unconverted, so its review is the
  dataset review) and `refused` (the owner's refusal in the body).
- A process composed without the port answers 503 with `status: "unavailable"` (`_UNWIRED`), because then no
  answer exists at all.
- The query parameters arrive as one `ReviewTreesSelection` (a FastAPI `Depends()` value), checked as one
  question by `problem()`: a `history` other than `recorded` or a negative `comparison`, more than
  `MAX_ENTRY_INVARIANTS` (500) named invariants, or any named key longer than `MAX_INVARIANT_KEY_LENGTH` (64
  characters; identities are 36; review F10 at 2026-09-30T06:10:21) is a 400 `invalid-request` whose `detail` names
  the problem. `named()` splits the list and drops empty keys; the query carries it as `invariants`.
- **The lane's bounds (MIK-L32, `_focus_problem`).** `lane` other than `LANE_FILES` (`files`), an empty `file` or one
  longer than `MAX_FILE_PATH_LENGTH` (4,096 characters), or more than one of `invariants`, `lane` and `file` is a 400
  whose `nextAction` names the three questions. The query carries `lane` (a flag) and `file`; `ReviewTreesQuery.focused`
  is true for any of the three, and the application reopens the comparison for every focused read.
- **Every admitted path answers typed (review R1 F2, ruling 2026-09-30T13:07:38).** A `file=` value up to 4,096
  characters that is not a changed path reaches the application, which answers the 200 `refused` with the refusal's
  `offending_input` clipped to its 1,024-character field; the route itself never answers 500 for it.
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

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R25@v1` with its rulings in `25_reviewer-on-git-trees.json`; they live outside the code and memory
repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The route path, the query with the named invariants (MIK-R31) and the lane or file question with `focused` (MIK-R32), and the port type. [1]
- The unwired answer: no comparison rather than an empty one. [2]
- The bounds and the one selection value: at most 500 invariants, each key at most 64 characters; `lane=files` only, a path of at most 4,096 characters, one question at a time. [3]
- The route: 503 unwired, 400 with the selection's own problem, otherwise the typed result; `lane` and `file` passed to the query. [4]
- One focused question at a time at the route; long paths answered with the typed 200 refusal (review F2). [5]
- The registration beside the other reviewer routes. [6]
- The route served over the port, the cards read passing its invariants, 400 for a 65-character key and for 501 keys, and refused when unwired. [7]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
