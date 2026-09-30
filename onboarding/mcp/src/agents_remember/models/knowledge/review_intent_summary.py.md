# mcp/src/agents_remember/models/knowledge/review_intent_summary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_intent_summary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:18:54+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4` |
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
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

## Docs References

No Domain Documentation source is configured for this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three answer states. | `ReviewIntentSummaryState` | mcp/src/agents_remember/models/knowledge/review_intent_summary.py:51-51 |
| One kind's after-only/before-only head counts. | `IntentHeadChanges` | mcp/src/agents_remember/models/knowledge/review_intent_summary.py:54-58 |
| The counts, the typed counts outside plus/minus, and the sum check. | `ReviewIntentCounts`; `_require_the_totals_to_be_their_parts` | mcp/src/agents_remember/models/knowledge/review_intent_summary.py:61-90 |
| Exactly one outcome per state; unavailable carries no counts. | `ReviewIntentSummaryResult`; `_require_one_outcome` | mcp/src/agents_remember/models/knowledge/review_intent_summary.py:93-123 |
| The lane's entry count, for a tree comparison only (MIK-R32 rule 9). | "A tree comparison (MIK-R25) also carries"; "attribution: ReviewLaneSummary" | mcp/src/agents_remember/models/knowledge/review_intent_summary.py:28-31; mcp/src/agents_remember/models/knowledge/review_intent_summary.py:107-108 |
| The dashboard's mirror of this shape. | `ReviewIntentSummaryResult`; `ReviewIntentCounts` | dashboard/src/data/reviewIntentSummary.ts:39-47; dashboard/src/data/reviewIntentSummary.ts:49-58 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): **body update for MIK-R32.** Logic records the optional `attribution` field (the lane's `ReviewLaneSummary`, outside the one-outcome validator, ruling 2026-09-30T12:19:20 Q6), and an Invariants bullet keeps it apart from `+N −N`. One row added. The moved rows were re-pointed by the installed fixer (its bullets kept, since no claim was reworded). No verification stamp was advanced.
- 2026-09-30T12:07:49+00:00: Generated citation repair: `ReviewIntentSummaryState` repointed to mcp/src/agents_remember/models/knowledge/review_intent_summary.py:51-51. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T12:07:49+00:00: Generated citation repair: `IntentHeadChanges` repointed to mcp/src/agents_remember/models/knowledge/review_intent_summary.py:54-58. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-28T16:55:21+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the changed-intent summary model (`ICR-R24@v3`). The verification pair names the code base; closeout owns the real stamp.
