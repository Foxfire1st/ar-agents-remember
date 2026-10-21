# dashboard/src/panels/review/ReviewSurface.memberCards.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Check that mounted member and family selections read their own subject while the opening keeps sole ownership of the cards read.

## Code Commentary

The fetch fixture serves captured family/member answers and a comparison-bound cards answer with no entries. Subject answers can be held independently; the initial family settles after one subject request and one cards request.

Selecting an uncached member sends its own subject review. While pending, exactly one subject slot is labelled with that member, the old family reading is absent, and cards requests remain at one. Answering the member keeps that count at one.

Selecting the shared member exposes the other family’s canonical row. Opening that family reads its own pending/answered subject without a second cards request, including when the family’s invariant set differs. The former changed-set card-prefetch expectation is gone.

### Evidence Boundary

These are source-inspected mounted checks with the inputs and replacements named here. This analysis did not execute them, recapture backend output, measure a real browser, or reopen the passed code candidate or D417 closures. Declaration counts and DOM assertions are not execution receipts. The synthetic cards body contains no entries. These request-order and pending-slot tests do not prove merged card contents, exact source bytes, a new backend run or browser acceptance.

## Evidence

- Mounted member/other-family pending and answered reads retain exactly the opening cards request. [2]
