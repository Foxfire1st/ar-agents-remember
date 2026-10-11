# mcp/src/agents_remember/worktrees/review_history.py

## Governing Overview

[worktrees overview](../../../overview.md)

## Purpose

Owns task-document transitions for the fixed-list review protocol: settings-owned pending-round admission, sealed-list result publication, cumulative recorded architect/developer allowances, and a same-round record-only result guarded by the independently resolved candidate identity.

## Code Commentary

### Logic

`begin_task_review` treats missing or explicit zero state as round zero and starts a pending first round with the supplied settings number, or its fallback. A pending replay stays on the same round and does not add allowance. Each new begin recomputes `limit` as the current settings number plus approved extras. At exhaustion an approval naming architect or developer and positive `additionalRounds` opens the next round, records normalized approval words and adds the allowance without resetting count or sealed findings. Earlier developerApproval input is normalized to developer approval. Premature or malformed approval is refused. A clean sealed review may begin a later round within the budget; it does not reopen the finding list. This module validates the recorded shape, not approval authenticity.

`record_task_review` accepts verdict, findings, remainingFindingIds, verdictRef and optional checked candidateTree. An absent state permits the initial baseline record; a pending first result seals findings, and pending successors shrink only the preceding remaining set. A nonpending result passes only if the recorded authority-resolved candidateIdentity and the current resolved identity are present and equal; a recorded candidateTree also requires the same checked-tree claim. Missing, unproven or changed identity refuses with begin_review as the next step. The result stays on the recorded round, still cannot add/reintroduce findings, and a passing result leaves none unresolved. The caller supplies the independent binding, which is persisted when available. A first or legacy zero-limit record is backfilled from the supplied settings number plus extras; a positive stored limit is not rewritten by record.

`require_pending_review` returns the existing task-owned state unchanged, or a first-round pending default when the field is absent. Despite its name, it does not reject an existing nonpending state; actual begin/record admission is owned by the transition functions.

### Invariants And Boundaries

- Missing state means zero; no external history store or identity/authentication claim is introduced.
- The transition is monotonic over the sealed finding list: later rounds can only remove remaining IDs.
- The budget is the supplied current settings number plus positive cumulative approved extras; approval never resets count or baseline.
- This module owns state transitions and comparison/persistence of the supplied candidate binding, not candidate resolution, route-evidence construction, integration authority or reviewer authentication.
- The worker report records implementation checks only; this card does not claim review or acceptance.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source governs these task-owned transitions.

No configured external source applies.

### Repo-Internal References

- Error/status boundary, cap-aware begin semantics, and pending admission. [1]
- Publication field validation, architect/developer approval parsing, and sealed baseline creation. [2]
- Successor monotonicity and duplicate/blank-ID refusals. [3]

## Historical L41 Source File Binding

At the historical L41 preparation, the source bytes were SHA-256
`a9ef793019ed3e2a66c258d977a493d9f431194b91d2f6c4897acd5821a895b6`
(`9166` bytes, `235` lines). The source is an uncommitted preparation candidate, so
verification metadata remains blank until a genuine commit-owned refresh.
