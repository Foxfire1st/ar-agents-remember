# dashboard/src/panels/sessionComposerStyles.ts

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The Panda CSS recipes of the shared `SessionComposer`, extracted from
`SessionComposer.tsx` by the 260731-EFA-L8 split. Owns the dock, editor frame,
footer, send/stop buttons, status/error/recovery text, secondary button, and the
CodeMirror theme.

## Code Commentary

### Logic

Static atoms plus the `composerTheme` EditorView theme extension; stop-button
enabled/disabled states are distinct recipes.

### Conventions

Tokens; the editor theme stays with the composer styles.

### Invariants And Boundaries

The dock must keep the editor surface stable across submit cycles.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The composer recipes. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
