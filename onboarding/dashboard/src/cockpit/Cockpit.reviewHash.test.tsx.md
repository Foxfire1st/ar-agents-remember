# dashboard/src/cockpit/Cockpit.reviewHash.test.tsx

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Declare startup, refusal and browser-history checks for the cockpit’s addressed review page.

## Code Commentary

The recorded startup case gives the shell an unknown complete task address, checks recorded-history request identity and the dedicated review refusal, then leaves through Back to Operations with the hash cleared.

The history case uses captured l86 task/catalogue/subject/tree/change-set inputs and a controlled fetch router. It deliberately refuses cards outside this hash/back journey instead of answering them with an unrelated family capture. An extra selectorId query key preserves the mounted surface and adds no intent read. The tree’s All changes action opens the nested change-set page, and browser Back removes both surfaces and restores the prior Knowledge address/view.

The file resets the store, global stubs, DOM and history after each case. Its two declared it blocks are not a collected parametrized-case total.

## Invariants And Boundaries

These are controlled jsdom and captured-fixture assertions. The source does not establish fresh Vitest execution, native browser geometry, plugin behavior or acceptance of the captured families’ unrelated card requests.

## Evidence

- Recorded startup addresses the correct review refusal and leaves through Back. [2]
- The fetch router explicitly refuses out-of-scope card requests rather than substituting captures. [3]
- An extra selector key retains the surface; tree All changes and browser Back restore the prior Knowledge view. [4]
