# dashboard/src/panels/review/explainer/ExplanationView.test-utils.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The stubbed explainer and recorded calls the explanation view's tests run against.

## Code Commentary

What must stay true here is what the stub answers and records: state and revision reads that match the real server's shapes, and a record of what was sent. `ExplanationView.test.tsx`, `ExplanationBuild.test.tsx` and `RevisionFrameProtocol.test.tsx` are the readers; the assertions are theirs.

## Boundaries

The obligation above is about what this file builds and returns; the assertions belong to the suites that read it.

## Evidence

- The explanation view is testable without a live explainer seat, because the stubbed server answers the same reads the real one does. [1]
