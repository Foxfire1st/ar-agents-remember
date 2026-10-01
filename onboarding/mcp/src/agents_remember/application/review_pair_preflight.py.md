# mcp/src/agents_remember/application/review_pair_preflight.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this module.

No relevant domain documentation was found.

### Repo-Internal References

- The four refusals in their fixed order. [1]
- The live pair's absent-half refusal, naming the half and the file. [2]
- The catalogue caller: one call, refused before any subject is listed. [3]
- The summary caller: the same call before either side is read. [4]
- The absent-half probe it builds on. [5]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.
