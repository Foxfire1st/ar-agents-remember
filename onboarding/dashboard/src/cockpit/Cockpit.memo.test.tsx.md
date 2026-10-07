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
- The rail-visibility counts shrink accordingly (Chats hides the rails, Operations shows them again);
  the memo gate itself is unchanged.

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

### Cross-Repo References

No cross-repo boundary is crossed by this file.
