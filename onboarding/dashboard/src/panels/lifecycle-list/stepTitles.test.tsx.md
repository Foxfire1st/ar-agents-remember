# dashboard/src/panels/lifecycle-list/stepTitles.test.tsx

## Governing Overview

[overview.md](overview.md)

## Purpose

The sidebar step-tooltip contract: no native title on any ancestor of a step mark, the row's hover text still on its own cells, and the tooltip's id and status word kept whole.

## Code Commentary

The cases pin MIK-R175's two visible promises: walking from a step dot to the row line finds no `title` the browser would show over the dot, while the title and status cells keep the row's hover text; and the tooltip's head and substep rows declare the parts that do not shrink or wrap, leaving only the title to wrap.

## Evidence

- No ancestor of a step mark carries a native title, and the row text keeps its hover. [1]
- The tooltip's id and status parts stay whole; only the title shrinks and wraps. [2]
