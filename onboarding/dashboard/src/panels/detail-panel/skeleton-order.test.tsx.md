# dashboard/src/panels/detail-panel/skeleton-order.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin fixed descendant block order and empty-block omission on all three forms, plus actual reader-chrome/objective order, shared block classes and fixed structured-prose expansion.

## Code Commentary

Full task, master and sprint fixtures require fixed ordered blocks with one objective immediately after the complete head, before Steps or Now. Each form has a mounted DOM-order assertion for that boundary; bare fixtures omit an absent objective and contain only the head. Intro-only index prose keeps the meaningful index block. Master Now uses actual step/review facts and sprint progress resolves commanded-master documents. The added TaskContent cases render an actual `open-changeset` series/committed line before the objective on sprint/master/task; unavailable-body notice precedes it, and the task direct-grant line also precedes it. Objective remains before Now/Steps. No-series cases assert the shared titled-block classes. Master/task `nonGoals` follows objective and `acceptance` follows design, both render Markdown without replacing historical Further-notes. Twelve-paragraph fields expose `Paragraph 11.` only after the two in-place toggles. These are DOM/class/content observations, not screenshot or pixel proof.

## Boundaries

This card describes the executable assertions and fixture seams of this module. It does not turn a mocked or seeded unit observation into system-wide acceptance. Keep fixture provenance, controlled time and actual producer opportunities explicit when extending the cases.

## Evidence

- Original full/bare form order and head-only boundary checks remain; new actual series chrome, block classes, fixed nonGoals/acceptance and in-place expansion have separate DOM assertions. [1]
