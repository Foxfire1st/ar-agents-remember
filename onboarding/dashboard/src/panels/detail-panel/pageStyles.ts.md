# dashboard/src/panels/detail-panel/pageStyles.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Own task-page-local layout, ground, typography and state-colour recipes shared by all three reader forms.

## Code Commentary

The page root is an inline-size query container: narrow is default, 36rem adds the middle-panel columns and 56rem gives the full row. It uses the proposal ground inside its containing panel; it does not repaint the shared panel or token system. Code ground, prose links, dim/line colours and form/status accents remain scoped to the page.

The objective after the complete head/change-set chrome, one-line tables and hidden-column/own-view affordances use the same recipes across forms. Long individual values wrap or clip instead of dictating page width. Reduced-motion handling belongs to the graph interaction and its fade variant; layout thresholds are container widths, not browser-window breakpoints. ObjectiveLead combines the shared block margin with the lead recipe. decisionReading centers whole-log content at maxWidth 100ch; productRecords styles its muted, counted disclosure. statusWord accepts mark=false to suppress a duplicate glyph when the shared task word supplies one. Order-node styling keeps dependency readiness separate from the shared task-state word/tone: the old work/waits variants and independent done-row layout are removed. These recipes do not classify task state or establish measured viewport/tooltip acceptance.

## Boundaries

These are CSS recipes, not document semantic state or measured browser acceptance. The shared Panel and global Markdown/token owners remain separate; task-page colours do not authorize a dashboard-wide restyling.

## Evidence

- The root scopes proposal ground/code/link styling to an inline-size page container. [1]
- All three form badges share one scoped recipe with distinct state colours. [2]

- Order styling uses readiness and relation marks rather than a second task-state colour vocabulary. [3]
