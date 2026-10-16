# dashboard/src/cockpit/Cockpit.memo.test.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`Cockpit.memo.test.tsx` proves the persistent-layer memoization contract from 260721: a tab switch
reconciles only layers whose props changed, and the hidden-not-unmounted identity of the persistent
layers survives switches.

## Code Commentary

### Logic

- Operations is injected explicitly. EngineRoom stays unbuilt; DetailPanel renders 2/2/3 across Chats/File Viewer/Operations because hide/show stops its clock. LifecycleList renders three times; the nested bell once, with no selection-callback prop. File Viewer and sidebar chat retain DOM identity through switches; sidebar ARIA remains outside this suite.

### Conventions

Vitest + Testing Library; render counts come from module-level spies on the layer components.

### Invariants And Boundaries

The suite binds the memo/keep-alive behavior for the current product views; it does not assert the
retained pages' internal rendering.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The requirement packet
`MIK-R79@v1` (rule 16) removes the Engine Room from the bar; it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The keep-alive case observes the File Viewer layer identity instead of the Engine Room. [13]


- The hidden-not-unmounted wrapper whose identity survives a switch. [14]


- The mounted layers the render counts observe. [15]



- The River-hidden sidebar case keeps the same document-chat node across the EventRiver toggle. [16]


### Cross-Repo References

No cross-repo boundary is crossed by this file.
