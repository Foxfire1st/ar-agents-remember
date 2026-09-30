# mcp/src/agents_remember/application/review_pair_preflight.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_pair_preflight.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076` |
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The one rule by which a resolved review pair is refused as a whole, before any subject is read from
it.** Two reads ask the whole pair a question before a reviewer opens it: the subject catalogue
(`knowledge_review.list_knowledge_review_entries`) and the changed-intent summary
([`review_intent_summary`](review_intent_summary.py.md)). They must refuse by the same rule and in the
same order, or the task entry could offer a count for a pair its catalogue refuses. Leaf
`260921-ICR-L47` extracted the rule out of `list_knowledge_review_entries` so both callers share it.

## Code Commentary

### Logic

`pair_preflight_refusal(resolved)` returns the **first** refusal, in this fixed order, or `None`:

1. `closed_leaf_dataset_refusal` — a closed leaf's record answers in its own words; a half the leaf
   never recorded is a fact about history, not lost content (`ICR-R12`);
2. `absent_pair_refusal` — a live pair with an absent half names the half and the file
   (`candidate_dataset_absent`), because authoring a candidate and placing the baseline it forks from
   are different actions;
3. `unreadable_half_refusal` — a half that is present but is not a readable dataset;
4. `candidate_receipt_refusal` — an unreadable candidate receipt.

`absent_pair_refusal` is the former private `knowledge_review._absent_pair_refusal`, moved unchanged
(same code, detail, next action and offending input).

### Conventions

It reads each half only as far as those checks need; what the pair *holds* is the caller's question.
Every refusal is a typed `ReviewRefusal` from the existing owners — this module mints no new code.

### Invariants And Boundaries

- One order for both callers. Reordering here changes both answers together, which is the point.
- A closed leaf's declared absence and a live leaf's missing file stay two different refusals.
- No dataset is substituted and nothing is read out of the live coordination tree.

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
| The four refusals in their fixed order. | `pair_preflight_refusal`; `closed_leaf_dataset_refusal`; `unreadable_half_refusal`; `candidate_receipt_refusal` | mcp/src/agents_remember/application/review_pair_preflight.py:34-42 |
| The live pair's absent-half refusal, naming the half and the file. | `absent_pair_refusal`; "candidate_dataset_absent" | mcp/src/agents_remember/application/review_pair_preflight.py:45-71 |
| The catalogue caller: one call, refused before any subject is listed. | `list_knowledge_review_entries`; `pair_preflight_refusal` | mcp/src/agents_remember/application/knowledge_review.py:257-318 |
| The summary caller: the same call before either side is read. | `intent_summary_of`; `pair_preflight_refusal` | mcp/src/agents_remember/application/review_intent_summary.py:145-175 |
| The absent-half probe it builds on. | `missing_dataset_half` | mcp/src/agents_remember/application/review_candidate_resolution.py:370-388 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`knowledge_review.py`) moved with the leaf's inserted lines: 1 passing row(s) normalised by the fixer. No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T14:22:59+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): No content impact: this card's own source is unchanged. MIK-R32 moved lines in `mcp/src/agents_remember/application/review_intent_summary.py`, so the citation rows into them that moved were re-pointed by the installed fixer (run once; its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; every re-pointed row was byte-identical to memory HEAD beforehand and was checked to hold its anchors in the new range. The fixer's normalisation also re-measured passing rows into files this leaf did not change (`mcp/src/agents_remember/application/review_candidate_resolution.py`); no claim changed. No verification stamp was advanced.
- 2026-09-30T12:21:42+00:00: Generated citation repair: `missing_dataset_half` repointed to mcp/src/agents_remember/application/review_candidate_resolution.py:370-388. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-28T16:55:21+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the pair preflight extracted from `knowledge_review.list_knowledge_review_entries` (`ICR-R24@v3`). The catalogue's refusal order is preserved exactly; the changed-intent summary now shares it. The verification pair names the code base; closeout owns the real stamp.
