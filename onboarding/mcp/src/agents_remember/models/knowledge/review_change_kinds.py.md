# mcp/src/agents_remember/models/knowledge/review_change_kinds.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The wire vocabulary of MIK-R33's change-kind facts and the validators that keep every delivered badge derived from
its facts.** `ReviewFamilyChanges` rides on each `ReviewFamilyContextEntry` of a tree comparison as `change_kinds`
(declared in `review_family_context.py`); it holds the family's guarantee fact and detail, `members_total` and one
`ReviewMemberChange` per returned member occurrence. The dashboard mirrors it in `data/reviewFamily.ts`.

## Code Commentary

### Logic

- **Literals.** `ChangeKind` (`intent`, `implementation`, `membership`, `unknown`, `unchanged`), `ChangeFact`
  (`established`, `not_established`, `unknown`), `ChangeMark` (the three facts, `text_differs`, `test`, `unknown`),
  `GuaranteeChange` (`intent`, `unchanged`, `unknown`). `CHANGE_PRECEDENCE` is ICR-R32 rule 2's order.
- **`primary_change`.** The highest established fact in precedence, else `unknown` when a fact is unknown, else
  `unchanged` only when all three are established as not changed.
- **`change_marks`.** The other established facts, then `text_differs`, `test` for a proof, and `unknown` for an
  unknown fact or, unconditionally, for `range_unresolved` (review R1 F4), never beside an `unknown` primary.
- **`ReviewMemberChange.of`.** Derives `primary` and `marks`, keeps `proof` only on an established implementation and
  `text_differs` only on an established intent, and clips every evidence and reason line
  (`EVIDENCE_LIMIT` 8, `UNKNOWN_REASON_LIMIT` 6, `MEMBERSHIP_REASON_LIMIT` 2, `EVIDENCE_TEXT_LIMIT` 600 characters).
- **Validators.** `_derived_from_the_facts` refuses a primary or marks that disagree with the facts, a proof or a
  `text_differs` without its fact, and a `range_unresolved` beside a `not_established` implementation.
  `_unknowns_say_why` requires `unknown_reasons` exactly when the change kind is not fully known and
  `membership_reasons` exactly when the membership is unknown (the merge round split them), and bounds every line.
  `ReviewFamilyChanges._one_occurrence_per_member` lists each occurrence once.

### Conventions

`KnowledgeModel` subclasses and `NamedTuple` carriers, as the other review wire models in `models/knowledge/`. The module
docstring states the three facts and the marks once; `application/review_change_kinds.py` computes them.

### Invariants And Boundaries

- An unknown fact always names why, and a known one names no reason (`_unknowns_say_why`): no unknown badge is
  unexplained, and "change kind unknown" never reads as "membership unknown" (part of the candidate invariant recorded
  on `application/review_change_kinds.py.md`).
- `primary` and `marks` cannot be set apart from the facts: the validator re-derives them.
- Nothing here is a verdict, a risk score or an assessment.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's statement of the three facts, the primary kind and the marks. [1]
- The literals, the precedence and the bounds. [2]
- The facts and evidence carriers. [3]
- The primary kind and the marks, including the unconditional unknown (review R1 F4). [4]
- One member occurrence, built from its facts, with both validators. [5]
- One family occurrence: guarantee, total and one occurrence per returned member. [6]
- Where it rides: the family context entry, validated against exactly the returned members. [7]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
