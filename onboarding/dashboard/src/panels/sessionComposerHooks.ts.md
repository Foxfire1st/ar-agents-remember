# dashboard/src/panels/sessionComposerHooks.ts

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The hook layer of the shared `SessionComposer`, extracted from `SessionComposer.tsx`
by the 260731-EFA-L8 split. Owns the interaction/store/submit/keymap/editor/recovery/
view/status hooks behind the composer surface.

## Code Commentary

### Logic

`useComposerEditor` creates the CodeMirror editor once and reads initial values
through refs so `exhaustive-deps` passes without recreating the editor per
keystroke; `useComposerSubmit` owns reliable submit; `useComposerRecovery` drives
authoritative withdrawal pop-back; `useComposerView`/`useComposerStatusHandlers`
shape the view data the parts render.

### Conventions

One hook per concern; no JSX here.

### Invariants And Boundaries

The editor-creation effect must keep the compartment-architecture contract (initial
values through refs) so keystroke re-renders never rebuild the editor.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The composer hook layer. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
