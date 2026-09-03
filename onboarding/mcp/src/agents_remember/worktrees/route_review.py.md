# mcp/src/agents_remember/worktrees/route_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/route_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00 |
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

Own the control-plane binding between independent route-review evidence and the exact current leaf
candidate tree. Curator admission and closeout consume this proof so a review cannot silently apply
to a later code change. Under CCR-R03@v1 the binding is content-addressed: every evidence file is
hashed, the record carries a typed dependency declaration, and a self-digest proves the record
bytes.

## Code Commentary

### Logic

`build_route_review` accepts only reviewer-authored verdict, evidence, and route rows; the plane
derives candidate tree and review time and verifies every evidence path stays inside the task root.
Since 260815-DAG-L16 it takes a `branch_addressed` flag: a leaf contract stamps the worktree
candidate tree as before, while `branch_addressed=true` (policy-gated direct execution) accepts a
series contract and stamps the branch HEAD tree instead (L16-R6) — same evidence semantics, no
worktree.
`require_current_route_review` first excludes series/master altitude because route-review records
are leaf-owned, then skips unchanged leaves. A changed leaf resolves its canonical task document,
requires a passing record for the exact current tree, and rechecks its evidence files.

Under R03 `build_route_review` now stamps per-evidence-file SHA-256 digests
(`_stamp_evidence_digests`), builds the `route-review/v1` dependency declaration (code tree,
task intent, every evidence-bytes edge, validator), and computes `recordDigest` over the record's
canonical JSON cit:([`build_route_review`, `_stamp_evidence_digests`], mcp/src/agents_remember/worktrees/route_review.py:56-116, 274-296).
`_require_evidence_files` was replaced by digest-based currentness: `_evidence_file_sha256` names
`route-review-evidence-outside-task` / `route-review-evidence-missing` / `route-review-evidence-stale`
when evidence bytes change after publication
cit:([`_evidence_file_sha256`], mcp/src/agents_remember/worktrees/route_review.py:309-331).
`require_current_route_review_task_intent` and `_require_current_dependencies` refuse
`route-review-task-intent-missing`, `evidence-dependencies-missing`, or
`route-review-dependencies-stale` when the declared inputs no longer match the current record
cit:([`require_current_route_review_task_intent`, `_require_current_dependencies`], mcp/src/agents_remember/worktrees/route_review.py:187-196, 229-271).

### Conventions

Public failures use a typed status on `RouteReviewError`; private candidate identity is derived from
the contract with an isolated temporary Git index. Evidence digests are SHA-256 of the exact task-
relative files, never mtimes or filenames; the digest declaration participates in the shared
evidence-dependency encoding.

### Invariants And Boundaries

- Agents never author `candidateTree`, `reviewedAt`, evidence digests, or the record digest.
- Route review belongs only to leaf altitude and is required for code-changing leaves; series
  closeout must not attempt candidate-tree or terminal-leaf resolution. The sole exception is the
  policy-gated `branch_addressed=true` direct-execution binding, which accepts a series contract
  explicitly (L16-R6); no silent cross-mode exists.
- Blocking, missing, stale, outside-task, and missing-file evidence all fail closed.
- Evidence references are task-relative and may not escape the task root.
- This module validates evidence; it does not perform review or mutate source.
- Content addressing is all-or-nothing: a record with partial digest fields cannot validate, and a
  changed evidence file always stales its review and dependent door.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The plane stamps reviewer payloads with the exact candidate and validates task-local evidence. | `build_route_review`; `_require_evidence_files` | mcp/src/agents_remember/worktrees/route_review.py:42-71; mcp/src/agents_remember/worktrees/route_review.py:114-134 |
| Series altitude is excluded before leaf resolution; changed leaves require a passing record for the current candidate tree. | `require_current_route_review` | mcp/src/agents_remember/worktrees/route_review.py:74-113 |
| The R03 evidence-digest stamping and dependency currentness seam. | `_stamp_evidence_digests`; `_require_current_dependencies`; `_evidence_file_sha256` | mcp/src/agents_remember/worktrees/route_review.py:229-331 |
| The route-review record's content-addressed fields and self-digest validator. | `RouteReviewRecord` | mcp/src/agents_remember/tasks/document.py:151-198 |

## Cross-Repo References

No cross-repository implementation source governs route review.

## R39 Route-Review Altitude

Current-route-review returns not-required-master-altitude before probing candidate or leaf
task-document state for non-leaf contracts. Candidate-bound independent review remains a leaf
closeout requirement; series/master closeout does not impersonate a terminal leaf.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260831-CCR-R03 Evidence-Bound Route Review

Route review now stamps and re-verifies the exact SHA-256 of every evidence file, declares its
direct dependencies (code tree, task intent, evidence bytes, validator), and self-addresses the
record; the closeout door fingerprints review provenance as `recordDigest` instead of a
recomputed evidence tuple (worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the evidence SHA-256 stamping, `route-review/v1` dependency declaration, record self-digest, and digest-based evidence currentness refusals; prior altitude, branch-addressed, and evidence-path prose preserved.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: `build_route_review` takes `branch_addressed`
  (policy-gated series-contract stamp from branch HEAD for sanctioned direct execution, L16-R6);
  leaf-worktree stamping is unchanged and no silent cross-mode exists. Verified at code commit
  a9d50e08.


- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-14T11:25+02:00 — R39 curator: documented the explicit non-leaf route-review bypass.
  Verification remains closeout-owned.

- 2026-08-14T09:08+02:00 — Reopened L23 repair: excluded series/master closeout before
  candidate-tree and terminal-leaf resolution. Independent route-review authority remains
  leaf-only; verification metadata remains closeout-owned.
- 2026-08-14T05:26Z — Created for L23's mandatory candidate-bound independent route-review gate.
  Verification remains closeout-owned until the source commit exists.