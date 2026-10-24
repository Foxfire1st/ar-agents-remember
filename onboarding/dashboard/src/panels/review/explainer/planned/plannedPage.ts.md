# dashboard/src/panels/review/explainer/planned/plannedPage.ts

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

The planned page's payload shape and its pure decisions: which sorts exist, what one row's second line says, how a scope path is captioned, and what counts as a planned page at all.

## Code Commentary

- The reader accepts the route's wrapped answer or an already unwrapped page, and answers nothing for a body whose mode is not planned, including a refusal.
- A row without a subject or an effect is dropped; a row's title falls back to its planned effect label, and absent counts read as zero rather than being invented.
- The sort control is the product's own list, so a payload cannot add a sort and a judgment order has no path onto a planned page.
- Sorting is stable on its key alone, so equal subjects or effects keep the task document's declaration order.
- A scope path is resolved only when the code tip answered it and the path exists there; anything else is captioned as not at the code tip.
- A page's model turns and agent starts are fixed at zero, so no payload can claim activity the page never performs.

## Evidence

- Only a body whose mode is planned is read as a page, and the product's sorts replace whatever the payload names [1]
- The declared order is the payload's own, and the other two orders are stable on their key [2]
- A row's second line is the current statement, the hand-off label, or a measured absence [3]
- A scope path is shown as an address at the code tip or as plain text [4]
- Exactly three deterministic sorts exist, and a judgment order is not among them [5]
