# dashboard/src/panels/review/family-member-statement/FamilyMemberStatement.tsx

## Governing Overview

[dashboard/src/panels route overview](../../overview.md)

## Purpose

One changed statement passage in a family roster.

## Code Commentary

memberStatementPairs indexes each roster side once by invariant identity; any repeated identity becomes ambiguous. A pair requires both unique rows recorded, both statements supplied and unequal. FamilyMemberStatement places the one IntentTextPassage on the before revision row and omits duplicate text on the after revision row, leaving revision buttons to the parent. Unpaired recorded rows keep own statement; unreadable rows state content not carried. No ambiguous/incomplete pair is guessed and no subject review is fetched.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- One changed statement passage in a family roster: `memberStatementPairs` owns the described branch. [1]
- One changed statement passage in a family roster: `FamilyMemberStatement` owns the described branch. [2]

