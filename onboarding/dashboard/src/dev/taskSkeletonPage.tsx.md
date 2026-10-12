# dashboard/src/dev/taskSkeletonPage.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Mount the real DetailPanel as an isolated deterministic developer evidence surface for each reader form.

## Code Commentary

The form query selects a seeded sprint, master or task. long=1 deliberately augments the seeded representatives with synthetic long content; rich=1 replaces them with the fully invented taskSkeletonDocs set and installs only its supported response mocks. A requested width gives the panel its own container width, rather than pretending the window width is the cockpit middle column.

The demo applies its selected projection before mounting the DetailPanel. Rich-mode requests not covered by the fixture still use the original fetch, and the override is restored on unmount. The fixture choice/augmentation must stay disclosed when interpreting a screenshot or interaction.

## Boundaries

This developer page is not a production route, older-server proof, real native task or generated evidence verdict. Using the real reader demonstrates its mounting seam, not every acceptance condition.

## Evidence

- The selected DEV fixture and limited fetch override are scoped and restored. [1]
