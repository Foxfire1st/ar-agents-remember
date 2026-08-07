# dashboard/src/panels/sessionComposerHooks.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/sessionComposerHooks.ts`              |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The composer hook layer. | `useComposerEditor`; `useComposerSubmit`; `useComposerRecovery` | dashboard/src/panels/sessionComposerHooks.ts:295-365; dashboard/src/panels/sessionComposerHooks.ts:99-155; dashboard/src/panels/sessionComposerHooks.ts:429-464 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the hook
  layer extracted from `SessionComposer.tsx`. Verification pinned to the leaf base
  until closeout stamps the code commit.
