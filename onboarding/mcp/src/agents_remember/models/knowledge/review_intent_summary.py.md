# mcp/src/agents_remember/models/knowledge/review_intent_summary.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The typed vocabulary of the changed-intent summary (`ICR-R24@v3`, leaf `260921-ICR-L47`): what the
task entry's `+N −N` count, what they cannot be, and the three states an answer can take. The
application owner ([`review_intent_summary`](../../application/review_intent_summary.py.md)) computes
the counts; this module fixes the declared shape and the arithmetic they must satisfy. An unavailable
result cannot carry counts, and the declared totals must equal their parts. These are constructor
consistency checks, not independent evidence that a producer actually read the comparison.

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

`unexplained_open` is a newly added optional non-negative integer, defaulting to `None`. It is
separate from authored-intent plus/minus and from file-attribution buckets; the one-outcome validator
does not couple it to the intent state. The tree-comparison producer asks `stored_unexplained_open`
for it alongside attribution. That owner requires a complete stored worklist bound to the exact
comparison, filters unexplained hunk/file items, delegates to gate verdicts, and withholds the count
if any relevant verdict is undecided. Missing, unreadable, incomplete or differently bound stored
work returns `None`, not an invented zero. The dashboard adapter preserves a supplied value as
`unexplainedOpen`; no additional rendering or freshness guarantee follows from the DTO field alone.

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
- The intended `+`/`−` inputs are invariant and guarantee head counts. The validator checks only
  their arithmetic against declared parts; it cannot authenticate those inputs against a tree.
  Relationship-only and stored-open counts remain separate fields, not additional plus/minus terms.
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
- The result declares the optional non-negative stored-open field while the outcome validator constrains counts/refusal and partial/unresolved, not that auxiliary count. [4]
- The lane's entry count, for a tree comparison only (MIK-R32 rule 9). [5]
- The dashboard mirrors the component counts and optional stored-open result, then preserves a supplied value as unexplainedOpen without adding it to authored-intent counts. [6]

- The tree-comparison summary attaches attribution and the separately computed stored-open count. [7]
- Matching complete stored work and decidable gate verdicts are required for an open count; absent or unusable work is not zero. [8]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.
