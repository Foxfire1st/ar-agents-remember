# dashboard/src/panels/review/SubjectJudgment.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Selected-subject judgment and proofs.

## Code Commentary

Require payload.judgment and a revision_selection matching requested kind/id; missing current fields or a different subject produce alerts, not no-judgment claims. Render Judgment and proofs openly: owner state/detail, delivered row order with attempt/disposition/effect/open-or-closed, reason, because references and covered-entry/examined-member counts. Only identifiers/history paths are in identifiers disclosures. A changed family row without effect reads effect not recorded. Proofs show path/symbol, owner state/facet/detail and grouped proof/invariant identifiers; no proofs returned is explicit even when history is unavailable. The renderer does not fetch, sort history independently, compute currentness or author a row.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- Selected-subject judgment and proofs: `SubjectJudgment` owns the described branch. [1]
- Selected-subject judgment and proofs: `JudgmentRow` owns the described branch. [2]
- Selected-subject judgment and proofs: `Proof` owns the described branch. [3]
- Selected-subject judgment and proofs: `effectLabel` owns the described branch. [4]

