# dashboard/src/cockpit/Cockpit.memo.test.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`Cockpit.memo.test.tsx` proves the persistent-layer memoization contract from 260721: a tab switch
reconciles only layers whose props changed, and the hidden-not-unmounted identity of the persistent
layers survives switches.

## Code Commentary

### Logic

- The layer-count fixture mounts `CockpitShell`; MIK-R79 moved the opening view to Chats, so the
  cases mount `CockpitShell initialView="operations"` when they need the railed shell.
- Because Engine Room left the product bar and is not built at load, `counts.engineRoom` is now `0`
  throughout; the sweep clicks the remaining product entries (Chats, File Viewer, Operations) and
  the keep-alive assertions use the File Viewer layer in place of the Engine Room layer.
- The visibility sweep gives the LifecycleList controller three renders but the nested attention bell only its original mount. The hidden rendered-collection gate and then the bell's stable-callback memo gate isolate it from the rail edges.
- Since MIK-R122 the suite also pins the right-rail chat keep-alive: the River-hidden
  sidebar case keeps the same document-chat node across the EventRiver presence/absence
  toggle, and the memoized rail toggle still updates. Sidebar ARIA on the right rail is
  source, not asserted by this suite; the separate top-level visibility cases cover
  other panes.

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
