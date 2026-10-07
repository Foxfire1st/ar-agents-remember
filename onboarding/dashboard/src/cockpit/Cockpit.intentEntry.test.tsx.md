# dashboard/src/cockpit/Cockpit.intentEntry.test.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`Cockpit.intentEntry.test.tsx` proves the Operations intent-entry re-validation contract (260921-ICR-L47):
the entry's summary re-reads once per showing, opening a task from another view reads its entry exactly
once, and leaving and returning to the reviewer re-reads it while otherwise reads stay standing.

## Code Commentary

### Logic

- The cases mount `CockpitShell`; MIK-R79 made Chats the opening view, so they mount
  `CockpitShell initialView="operations"` and use **File Viewer** as the other full-bleed view to
  leave and return to Operations (replacing the Memory tab, which has no bar entry).
- The read-count assertions and the stale-entry setup are unchanged.

### Conventions

Vitest + Testing Library; the routes stub counts summary and catalogue reads per case.

### Invariants And Boundaries

The suite binds the re-validation generation wiring (`IntentEntryRevalidation`) to the Operations
view only; it does not assert the retired pages.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The requirement packet
`MIK-R79@v1` (rule 16) fixes the opening view and the product bar; it lives outside the code and
memory repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The re-validation boundary the cases exercise. [10]
- The shell the cases mount on an injected view. [11]
- The mode-bar entry used to leave and return to Operations. [12]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
