# mcp/src/agents_remember/application/worktree_tool_requests.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/worktree_tool_requests.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Application layer](overview.md)

## Purpose

Owns the immutable request concepts and shared defaults used by the worktree application entry
points. The extraction keeps argument meaning in one typed module while `worktree_tools.py` remains
the operation-composition facade.

## Code Commentary

### Logic

`CloseoutCommitMessages` and `OperationControlRequest` expose only code and memory subjects.
`LandedCommits` records the landed code SHA and optional memory-content SHA; it carries no ledger
output. Approval, candidate admission, generation checks, and corrective dispositions retain their
separate typed meanings.

`TaskIdentity`, `TaskBases`, and `StartExecution` describe task creation. `OperationControlRequest`
describes one public lifecycle-control request and normalizes public JSON-shaped caller, grade, and
admission values into their canonical models. `CloseoutCommitMessages` remains separate from
`CloseoutApproval`, so a preview cannot look approved merely because it carries commit text.
`FinalizeTaskDocs` names only the task-document addresses reconciled by finalization.

The defaults are real typed instances: ordinary callers share the repository-default task bases,
normal start execution, preview-only closeout approval, and no-task-doc finalization values.
`LifecycleControlAction` is imported from the integration control owner rather than re-declared at
the application boundary.

### Conventions

Keep request concepts immutable and approval separate from commit text; normalize only the canonical typed public values.

### Invariants And Boundaries

- This module owns request data and input normalization; it performs no Git, filesystem, journal,
  queue, or task-document mutation.
- `CloseoutApproval` and `CloseoutCommitMessages` must remain distinct types.
- Public JSON reconstruction is bounded to the three canonical models in
  `OperationControlRequest.__post_init__`; unknown compatibility shapes are not inferred.
- Callers use these exact types and defaults; they must not re-derive equivalent dictionaries.

### Todos

No additional file-local TODO is established by this candidate review.

## Docs References

No external Domain Documentation source is configured. These are repository-owned application
contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation source applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Raw closeout/control messages and landed commits contain only code/memory values. | `CloseoutCommitMessages` | mcp/src/agents_remember/application/worktree_tool_requests.py:110-115 |
| Task-start concepts and shared defaults have one definition. | `TaskIdentity`; `TaskBases`; `StartExecution` | mcp/src/agents_remember/application/worktree_tool_requests.py:17-30; mcp/src/agents_remember/application/worktree_tool_requests.py:34-48; mcp/src/agents_remember/application/worktree_tool_requests.py:52-57 |
| Lifecycle control reconstructs only canonical typed public values. | `OperationControlRequest`; `__post_init__` | mcp/src/agents_remember/application/worktree_tool_requests.py:68-107 |
| Closeout approval, messages, and finalization documents remain separate concepts. | `CloseoutCommitMessages`; `CloseoutApproval`; `FinalizeTaskDocs` | mcp/src/agents_remember/application/worktree_tool_requests.py:110-115; mcp/src/agents_remember/application/worktree_tool_requests.py:131-136; mcp/src/agents_remember/application/worktree_tool_requests.py:143-149 |
| The start tool consumes the request types this module extracts. | `worktree_start_tool` | mcp/src/agents_remember/application/worktree_tools.py:103-109 |
| Operation control consumes its extracted request type. | `_operation_control_request_refusal` | mcp/src/agents_remember/application/worktree_tools.py:557-585 |
| Closeout apply consumes its extracted request type. | `worktree_closeout_apply_tool` | mcp/src/agents_remember/application/worktree_tools.py:353-368 |

## Cross-Repo References

No cross-repository boundary is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separate external implementation source applies to this file. | N/A | N/A |
## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Removed ledger subjects and landed-ledger identities from the documented request concepts. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.

- 2026-09-13T17:20:55+00:00: Generated citation repair: `worktree_operation_control_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:539-559. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:06:15+00:00: Generated citation repair: `worktree_operation_control_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:503-523. No content impact: mechanical anchor-range projection bound to citation source snapshot 1740540b8733028dd833a3538d739271e8925ea5f51911a0f8dcd8c49e7e1c13; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `worktree_start_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:103-200. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `worktree_operation_control_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:464-484. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `worktree_closeout_apply_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:353-368. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `worktree_start_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:111-208. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `worktree_operation_control_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:545-565. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `worktree_closeout_apply_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:361-379. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `CloseoutCommitMessages`; `CloseoutApproval`; `FinalizeTaskDocs` repointed to mcp/src/agents_remember/application/worktree_tool_requests.py:111-117; mcp/src/agents_remember/application/worktree_tool_requests.py:120-125; mcp/src/agents_remember/application/worktree_tool_requests.py:132-138. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T10:44:52+02:00 — No request behavior change: closeout-source models moved into their package and `LifecycleControlAction` now comes from the canonical operation-kind model owner.

- 2026-08-24T21:43+02:00 — Created for the hard-limit repair that extracted typed worktree request
  concepts from `worktree_tools.py` without changing their public behavior.