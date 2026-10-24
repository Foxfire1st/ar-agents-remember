# dashboard/src/panels/review/explainer/ReviewExplainerIntegration.test.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Measures the switch, the explanation page and the planned page inside the mounted review page, so their placement and their reads are proven against that page's own tree, chat and stream.

## Code Commentary

- The review page is mounted whole over a stubbed transport that serves its own reads plus the explainer's state and revision routes.
- One case requires the switch in the top line, the explanation page in the reading column with the tree and the chat still outside it, and a claim link returning to the Review view with that exact block selected.
- A planning-mode leaf mounts the planned page instead, with no change set and no frame.
- The moved stream event is required to show the notice and Update at once when work exists, and to renew the deterministic reads instead when none does.
- The judgment cases mount explainer categories and grades into the tree's ordering, ungraded grouping, stale marks and hover reasons without the page reading a model.

## Evidence

- The switch sits in the top line, the explanation page keeps the tree and chat outside it, and a claim link selects its exact block on return [1]
- A planning-mode leaf mounts the planned page [2]
- A moved event shows the notice at once where work exists, and renews the deterministic reads where none does [3]
