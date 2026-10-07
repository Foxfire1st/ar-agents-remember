# dashboard/src/panels/changeset/ChangeSetViewer.test.tsx

## Governing Overview

[changeset/ overview](overview.md)

## Purpose

`ChangeSetViewer.test.tsx` proves the cockpit change-set takeover wiring at its boundary: its only
cockpit case mounts the shell on an injected Operations view with a projection already applied and
asserts the takeover is absent initially with the Operations rails present. Direct `ChangeSetViewer`
and `DetailPanel` cases elsewhere cover the viewer and its open callback; no cockpit case asserts a
rendered positive takeover.

## Code Commentary

### Logic

The takeover-wiring case applies a projection before mounting `CockpitShell` on an injected
`initialView="operations"` and asserts the viewer is **absent** with the Operations rails present; it
does not assert the viewer becoming present. Direct `ChangeSetViewer`/`DetailPanel` cases elsewhere
cover the positive rendering and its open callback.

### Conventions

Vitest + Testing Library; the dashboard store is seeded through the fixture gallery.

### Invariants And Boundaries

The test binds the takeover visibility contract on the Operations view and does not assert the
Knowledge reader or the product tab list.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The requirement packet
`MIK-R79@v1` (rule 16) fixes the opening view; it lives outside the code and memory repositories, so
it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The case mounts the shell explicitly on Operations. [7]
- The viewer the case asserts absent while the shell is mounted on an injected Operations view; direct viewer and DetailPanel cases elsewhere cover its positive rendering and open callback. [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
