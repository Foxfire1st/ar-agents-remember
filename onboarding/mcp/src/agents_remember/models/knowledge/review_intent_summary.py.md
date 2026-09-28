# mcp/src/agents_remember/models/knowledge/review_intent_summary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_intent_summary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:55:21+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28` |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

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

### Todos

None.

## Docs References

No Domain Documentation source is configured for this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three answer states. | `ReviewIntentSummaryState` | mcp/src/agents_remember/models/knowledge/review_intent_summary.py:45-45 |
| One kind's after-only/before-only head counts. | `IntentHeadChanges` | mcp/src/agents_remember/models/knowledge/review_intent_summary.py:48-52 |
| The counts, the typed counts outside plus/minus, and the sum check. | `ReviewIntentCounts`; `_require_the_totals_to_be_their_parts` | mcp/src/agents_remember/models/knowledge/review_intent_summary.py:55-84 |
| Exactly one outcome per state; unavailable carries no counts. | `ReviewIntentSummaryResult`; `_require_one_outcome` | mcp/src/agents_remember/models/knowledge/review_intent_summary.py:87-115 |
| The dashboard's mirror of this shape. | `ReviewIntentSummaryResult`; `ReviewIntentCounts` | dashboard/src/data/reviewIntentSummary.ts:34-52 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T16:55:21+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the changed-intent summary model (`ICR-R24@v3`). The verification pair names the code base; closeout owns the real stamp.
