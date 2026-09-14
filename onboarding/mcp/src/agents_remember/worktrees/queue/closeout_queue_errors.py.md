# mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T14:20+02:00 |
| lastVerifiedCommitHash | `c1bb3543c6711f7f51991ec0afbd1a1defe181e2` |
| lastVerifiedCommitDate | 2026-09-14T14:09:55+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Defines the shared typed fail-closed error crossing the queue application, evidence, store-facing,
and lifecycle services, plus the shared request-reference validator.

## Code Commentary

### Logic

`CloseoutQueueError` retains both machine-readable `status` and exact `detail` attributes while the
base exception carries them together, preserving task-domain refusal facts through queue adapters
and detached worker diagnostics.
`queue_task_ref` (extracted from `closeout_queue.py` in 260815-DAG-L13) validates one
request-carried task-document reference, failing closed with `closeout-queue-reference-required` /
`closeout-queue-reference-invalid`.

Since 260913-LCA-L7 this module is also the one declaration of the capacity-refusal family. Capacity
refusals are the one family whose source was read perfectly and is invalid — the graph, or the
problem list built from it, is larger than its bound admits — so the module publishes the codes
`MASTER_CAPACITY_EXCEEDED` (`closeout-queue-master-capacity-exceeded`), `EDGE_CAPACITY_EXCEEDED`
(`closeout-queue-edge-capacity-exceeded`) and `SOURCE_PROBLEM_CAP_EXCEEDED`
(`source-problem-cap-exceeded`), and the set `CAPACITY_REFUSAL_CODES` that names all three. The
classification the closeout projection applies lives beside the codes on purpose: deriving it from a
code's spelling is how the projection came to test the substring `cap-exceeded` and miss every code
that spells the bound `capacity-exceeded`, reporting a sprint past its graph bound as a source that
could not be read. A rename here moves the raiser in `closeout_queue_graph.py` and the classifier in
`closeout_projection.py` together, which a substring test never did. No refusal code was renamed.

### Conventions

Queue refusal sites use stable status strings rather than exposing internal exception classes.

### Invariants And Boundaries

- Every refusal has both a status and a detail.
- Each capacity code is declared once with the classification the closeout projection applies, so a
  raiser and the classifier cannot drift apart.
- This module contains no recovery or policy logic beyond reference validation.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared queue error stores exact public status and detail as direct typed attributes. | `CloseoutQueueError` | mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py:17-23 |
| Request-carried task references validate fail-closed in one place. | `queue_task_ref` | mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py:64-85 |
| The capacity-refusal family is declared once, codes beside the classification the projection applies. | `CAPACITY_REFUSAL_CODES`; `MASTER_CAPACITY_EXCEEDED`; `EDGE_CAPACITY_EXCEEDED`; `SOURCE_PROBLEM_CAP_EXCEEDED` | mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py:26-40 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Shared Queue Failure Evidence API

`bounded_queue_failure_detail` is the one queue-facing adapter from lower-level exceptions to
stable public evidence. It delegates redaction to `public_failure_evidence`, serializes the bounded
record deterministically, and prevents backend text or offending input from leaking through each
queue consumer's local exception formatting.

| Finding | Anchor | Source |
| --- | --- | --- |
| Queue consumers share one bounded, stable failure-detail constructor. | `bounded_queue_failure_detail` | mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py:43-61 |
| Task-reference validation also uses that constructor instead of echoing the supplied value. | `queue_task_ref` | mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py:64-85 |

## Update History

- 2026-09-14T14:20+02:00 — 260913-LCA-L7 (uncommitted change set on `ar/260913-lca-l7`): the module
  now declares the capacity-refusal family — `MASTER_CAPACITY_EXCEEDED`, `EDGE_CAPACITY_EXCEEDED`,
  `SOURCE_PROBLEM_CAP_EXCEEDED` and the `CAPACITY_REFUSAL_CODES` set — beside the reason a code and
  its classification are one declaration, so `closeout_queue_graph.py` raises through the constants
  and `closeout_projection._problem` classifies by membership instead of by the substring
  `cap-exceeded`. Re-derived the module's own ranges against the current 85-line source:
  `bounded_queue_failure_detail` 25-43 → 43-61 and `queue_task_ref` 46-67 → 64-85; added the
  declaration's evidence row. Verification metadata remains closeout-owned; no stamp advanced.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: made exact refusal `detail` a direct typed
  attribute so semantic-topology adapters preserve status and detail without reparsing exception
  text. Verification remains closeout-owned.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: documented the shared bounded queue failure-evidence API. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: added `queue_task_ref`, the shared request-reference
  validator extracted from `closeout_queue.py` so the queue service and the extracted blocker
  module validate refs identically. Verification remains closeout-owned.

- 2026-08-15T11:07+02:00 — L3 Dagger repair: included the stable status in exception text while
  retaining the typed `status` field, so lifecycle failure records do not erase the refusal class.
- 2026-08-15T09:10+02:00 — Created for L3's typed queue refusal boundary; verification remains closeout-owned.
