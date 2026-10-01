# mcp/src/agents_remember/models/knowledge/review_intent_summary.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The typed vocabulary of the changed-intent summary (`ICR-R24@v3`, leaf `260921-ICR-L47`): what the
task entry's `+N −N` count, what they cannot be, and the three states an answer can take. The
application owner ([`review_intent_summary`](../../application/review_intent_summary.py.md)) computes
the counts; this module fixes the shape and the arithmetic they must satisfy, so no caller can be handed
a total its parts do not make or a zero for a comparison nobody read.

## Code Commentary

### Logic

- `ReviewIntentSummaryState` is `counted` | `partial` | `unavailable`.
- `IntentHeadChanges` is one statement kind's `after_only` / `before_only` head count.
- `ReviewIntentCounts` carries `added` (`+`) and `removed` (`−`) with their two parts (`invariants`,
  `guarantees`), plus the typed counts kept outside plus/minus: `realization_only`, `membership_only`
  and `unresolved`. Its validator requires `added` and `removed` to equal the sums of their parts.
- `ReviewIntentSummaryResult` (`operation="read_review_intent_summary"`) carries the task context and
  exactly one outcome: `counts` for `counted`/`partial`, `refusal` for `unavailable`. Its validator
  refuses an `unavailable` result with counts, a counted one with a refusal, and a `partial` state that
  does not match `unresolved > 0`.
- **`attribution` (MIK-L32, MIK-R32 rule 9).** A tree comparison's result also carries a
  [`ReviewLaneSummary`](review_lane.py.md): the unexplained-changes lane's file-level count, read in the same request
  as the intent counts and never more eagerly. It is optional, outside the one-outcome validator (it may sit beside
  counts or beside a refusal, ruling 2026-09-30T12:19:20 Q6), and a dataset comparison carries none; the route
  serializes with `exclude_none`, so a dataset body is unchanged.

The module docstring states the count semantics after the F3 ruling: every successor revision counts
once on each side (new text, changed origin state or acceptance reference, or a version-only
successor); only a same-content successor whose relationships moved, or an unchanged head whose
realizations moved, is kept in the typed counts.

### Conventions

Pydantic `KnowledgeModel` subclasses with non-negative integer fields and `model_validator(mode="after")`
checks, like the sibling review models.

### Invariants And Boundaries

- **A missing dataset is never a measured `+0 −0`**: `unavailable` carries a refusal and no counts, by
  construction.
- `+`/`−` are exactly the invariant and guarantee head counts; relationship-only changes cannot be
  folded in without breaking the sum check.
- This module selects and compares nothing.
- **The lane's count is never folded into `+N −N`:** it is a separate field with its own states, where `partial` and
  `unavailable` carry no count.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this module.

No relevant domain documentation was found.

### Repo-Internal References

- The three answer states. [1]
- One kind's after-only/before-only head counts. [2]
- The counts, the typed counts outside plus/minus, and the sum check. [3]
- Exactly one outcome per state; unavailable carries no counts. [4]
- The lane's entry count, for a tree comparison only (MIK-R32 rule 9). [5]
- The dashboard's mirror of this shape. [6]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.
