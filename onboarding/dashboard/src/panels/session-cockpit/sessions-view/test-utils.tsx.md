# dashboard/src/panels/session-cockpit/sessions-view/test-utils.tsx

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

Shared fixture builders for the split SessionsView test files, extracted from
`SessionsView.test.tsx` by the 260731-EFA-L8 split. Exports the lazy-loaded
terminal mount/unmount ledgers and the session seeding helpers the split suites use.

## Code Commentary

### Logic

`mockTerminalMounts` / `mockTerminalUnmounts` record Terminal lifecycle calls;
`seedReadyComposerSession` / `seedLegacyRawSession` / `seedLiveProjection` seed the
cockpit store; `stubHangingFetch` installs the hanging-fetch stub. The `vi.mock`
factory imports these lazily to avoid hoisting TDZ.

### Conventions

Test-only; never imported by production code.

### Invariants And Boundaries

The ledgers must be imported by any split file that asserts Terminal mount/unmount
behavior.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The shared seeds and terminal ledgers. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
