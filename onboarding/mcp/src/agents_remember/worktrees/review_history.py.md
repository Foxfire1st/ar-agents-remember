# mcp/src/agents_remember/worktrees/review_history.py

## Governing Overview

[worktrees overview](../../../overview.md)

## Purpose

Owns task-document transitions for the fixed-list review protocol: begin a pending round,
publish one result, require the pending bit before reviewer work, and enforce the ordinary
three-round limit with a directly recorded developer permission for cumulative extra rounds.

## Code Commentary

### Logic

`begin_task_review` treats missing or explicit zero `reviewState` as round zero and starts round
one with `pending=True`. Replaying a pending begin is idempotent and does not consume an allowance.
A completed sealed state with no remaining findings refuses a new round. The transition imports
the existing ordinary three-round limit; at exhaustion it requires a nonblank `developerApproval`
and positive `additionalRounds`, records that answer, and accumulates the allowance without
resetting the round or sealed issue list. Before exhaustion, or on a first/zero-state begin, that
permission payload is rejected. The recorded answer is a direct workflow input; this module adds
no authentication or provenance claim.

`record_task_review` requires a pending state and permits only verdict, findings,
`remainingFindingIds`, and `verdictRef`. The first result validates and seals the baseline
findings; a non-empty baseline must remain blocking and remaining IDs are derived from those findings.
Successor rounds may not add findings and may only shrink the prior remaining set and the sealed
baseline. A passing successor must leave no finding unresolved.

`require_pending_review` is the reviewer-work admission guard. It refuses when state is missing or
not pending and otherwise returns the task-owned state unchanged.

### Invariants And Boundaries

- Missing state means zero; no external history store or identity/authentication claim is introduced.
- The transition is monotonic over the sealed finding list: later rounds can only remove remaining IDs.
- The ordinary cap is fixed at the existing settings constant; explicit developer permission adds
  only a positive cumulative allowance and never resets the count or baseline.
- This module owns state transitions, not candidate-tree, evidence, integration authority, or
  reviewer authentication.
- The worker report records implementation checks only; this card does not claim review or acceptance.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source governs these task-owned transitions.

No configured external source applies.

### Repo-Internal References

- Error/status boundary, cap-aware begin semantics, and pending admission. [1]
- Publication field validation, developer-permission parsing, and sealed baseline creation. [2]
- Successor monotonicity and duplicate/blank-ID refusals. [3]

## Source File Binding

The current L41 source bytes are SHA-256
`a9ef793019ed3e2a66c258d977a493d9f431194b91d2f6c4897acd5821a895b6`
(`9166` bytes, `235` lines). The source is an uncommitted preparation candidate, so
verification metadata remains blank until a genuine commit-owned refresh.
