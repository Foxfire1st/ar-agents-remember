# mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py

## Governing Overview

[MCP overview](overview.md)

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

## Evidence

### Docs References

No configured Domain Documentation source applies.

### Repo-Internal References

- The shared queue error stores exact public status and detail as direct typed attributes. [1]
- Request-carried task references validate fail-closed in one place. [2]
- The capacity-refusal family is declared once, codes beside the classification the projection applies. [3]

### Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Shared Queue Failure Evidence API

`bounded_queue_failure_detail` is the one queue-facing adapter from lower-level exceptions to
stable public evidence. It delegates redaction to `public_failure_evidence`, serializes the bounded
record deterministically, and prevents backend text or offending input from leaking through each
queue consumer's local exception formatting.

- Queue consumers share one bounded, stable failure-detail constructor. [4]
- Task-reference validation also uses that constructor instead of echoing the supplied value. [5]
