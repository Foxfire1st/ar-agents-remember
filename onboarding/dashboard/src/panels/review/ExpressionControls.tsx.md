# dashboard/src/panels/review/ExpressionControls.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Expression-card presentation controls.

## Code Commentary

Draw the Code & test expressions heading, caller-selected split/inline Layout, and full-file toggle. The select normalizes its event value to inline or split; the button flips fullFile and changes Expand full file / Show changed regions text and aria-pressed. The caller owns both states. There is no request, source selection or attribution logic. Extracting these controls does not preserve the deleted ReviewExpressions accordion.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- Expression-card presentation controls: `ExpressionControls` owns the described branch. [1]

