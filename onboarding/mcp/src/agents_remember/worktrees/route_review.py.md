# mcp/src/agents_remember/worktrees/route_review.py

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

Own the control-plane binding between independent route-review evidence and the exact current leaf
candidate tree. Curator admission and closeout consume this proof so a review cannot silently apply
to a later code change. Under CCR-R03@v1 the binding is content-addressed: every evidence file is
hashed, the record carries a typed dependency declaration, and a self-digest proves the record
bytes.

## Code Commentary

### Current Contract

Inspection guidance and mutation guidance are separate. inspect_task_document for a task_doc plan names taskDocumentPath and file-reading prose, with no nextTool/nextArgs invoking a removed read. record_route_review alone carries the mutating task_doc address and required review value. Currentness and developer-decision mappings remain governed by their existing owners; file reading does not record an intent verdict.

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
canonical JSON (source owners: `build_route_review`, `_stamp_evidence_digests`; native references below).
`_require_evidence_files` rechecks the stamped verdict and route evidence through digest-based currentness: `_evidence_file_sha256` names
`route-review-evidence-outside-task` / `route-review-evidence-missing` / `route-review-evidence-stale`
when evidence bytes change after publication
(source owners: `_evidence_file_sha256`; native references below).
`require_current_route_review_task_intent` and `_require_current_dependencies` refuse
`route-review-task-intent-missing`, `evidence-dependencies-missing`, or
`route-review-dependencies-stale` when the declared inputs no longer match the current record
(source owners: `require_current_route_review_task_intent`, `_require_current_dependencies`; native references below).

> **Retained historical source account — superseded by the current contract:**
> CCR-R25 adds `route_review_refusal_projection`, a pure explanation layer for an already-observed
> `RouteReviewError`. It classifies currentness and task-intent statuses as a
> `record_route_review` correction, maps a blocked or otherwise invalid status to developer
> decision, and maps a missing task document to a task-document inspection. With an exact contract it
> adds only the contract-bound `task_doc` address; the caller must provide the `review` value named in
> `nextRequiredArgs`. It never writes a task document, creates a review record, changes route-review
> altitude, or weakens the currentness gate. `route_review_refusal_fields` is the typed adapter used
> by application start/admission and direct closeout.

### Conventions

Public failures use a typed status on `RouteReviewError`; private candidate identity is derived from
the contract with an isolated temporary Git index. The index path is scratch namespace only
(rule 6): it names the system temp directory, never the enclosure's `reports/` directory, which a
read would otherwise create and leave behind empty. Evidence digests are SHA-256 of the exact task-
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
- Refusal projection reports the gate's observed status and exact recovery address; it never
  fabricates evidence or turns a developer decision into an executable retry.

### Todos

None recorded.

## Exact clean-sync comparison

The closeout door first allows the recorded candidate tree itself. For a different tree, it calls clean_sync_keeps_route_review: the plane-stamped baseCommit must be an ancestor of the current base; the reviewed and incoming changed-path sets must be disjoint; and the current-base-to-candidate after-image map must equal the recorded-base-to-reviewed map exactly. Map identity includes each raw pathname byte sequence, blob and mode. An absent stamp supplies no exception. The door preserves the existing review record digest as its fingerprint and still checks task intent, evidence bytes and dependencies. This exception belongs to the door; require_current_route_review keeps its own exact-current-tree contract.

A NUL-delimited Git pathname is an exact byte identity. Ordinary run_git still uses text transport, whose universal-newline handling can collapse CR and LF pathnames. run_git_bytes selects raw output through the same _git_run environment, identity guard, working directory, timeout and session options. _tree_change_after_images splits b"\0", keeps pathname keys as bytes, and decodes only the ASCII mode/blob fields. It raises on failed or malformed raw diff output; it does not normalize, rename-pair or infer path equivalence.

## Evidence

- The helper admits only ancestral, path-disjoint sync with an identical reviewed after-image map. [7]
- Raw diff records preserve byte pathname keys, modes and object IDs; malformed observations raise. [8]
- The plane stamps candidate and base, while the evidence-byte owner confines and hashes task files. [1]
- R03 evidence digests and declared dependency currentness keep their distinct source owners. [3]


### Docs References

No configured Domain Documentation source applies.

### Repo-Internal References


- Series altitude is excluded before leaf resolution; changed leaves require a passing record for the current candidate tree. [2]

- CCR-R25 maps observed route-review refusals into bounded structured recovery guidance. [4]
- The route-review record's content-addressed fields and self-digest validator. [5]

### Cross-Repo References

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

- Inspection guidance and mutation guidance are separate. inspect_task_document for a task_doc plan names taskDocumentPath and file-reading prose, with no nextTool/nextArgs invoking a removed read. record_route_review alone carries the mutating task_doc address and required review value. Currentness and developer-decision mappings remain governed by their existing owners; file reading does not record an intent verdict. [6]
