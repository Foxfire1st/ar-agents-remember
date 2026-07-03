# dashboard/src/panels/file-viewer/codemirrorTheme.ts

| Field | Value |
| ---------------------- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/file-viewer/codemirrorTheme.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-29T17:00+02:00 |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

Maps the podracer OKLCH palette (the `styles/tokens.css` `:root` vars) onto CodeMirror 6 so the
read-only code pane matches the rest of the cockpit. Exports a single `codeTheme` extension that the
code pane mounts.

## Code Commentary

### Logic

Two pieces composed into one bundle. `chrome = EditorView.theme({...}, { dark: true })` owns the editor
chrome: bg/ink/height/font-size from `--bg-panel`/`--ink`, the scroller font from `--font-mono`, gutters
from `--bg`/`--grid`, a transparent active line, an amber-tinted selection (`color-mix` over `--amber`),
and a removed focus outline. `highlight = HighlightStyle.define([...])` maps Lezer tags to token vars —
keywords/types/tags → `--amber`, strings → `--mint`, numbers/bools/functions → `--cyan`, properties →
`--ink`, and **comments (italic) + operators/punctuation/brackets → a readable mid-lightness ink/bg blend**
(`color-mix(in oklab, var(--ink) 60%/75%, var(--bg))`) rather than `--grid` (the 0.30-L gutter tone,
near-invisible on the 0.16-L bg; gutter line numbers still use `--grid`). The exported
`codeTheme: Extension = [chrome, syntaxHighlighting(highlight)]` is the chrome + syntax-token pair.

### Invariants And Boundaries

No CSS animation here — motion is GSAP/Motion only (master invariant), as the header states. Colors are
read from CSS custom properties rather than hardcoded, so the theme tracks the live token set;
`tokens.css` owns the actual OKLCH values. Purely presentational and shared by every CodeMirror surface
(the plain pane and L4's diff) so syntax tokens stay identical across them.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `FilePane` builds its `EditorView` with this theme bundle. | L10, L37 | [FilePane.tsx](FilePane.tsx) |
| The OKLCH token vars this theme reads. | L5-L19 | [../../styles/tokens.css](../../styles/tokens.css) |

## Update History

- 2026-06-29T17:00+02:00 — L4 follow-up (readability): comments and operators/punctuation/brackets now use
  a mid-lightness ink/bg blend (`color-mix(in oklab, var(--ink) 60%/75%, var(--bg))`) instead of `--grid`
  (the gutter/border tone, near-invisible on the dark bg); gutter line numbers keep `--grid`. Shared by the
  File Viewer + L4 diff. Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): the read-only CodeMirror
  theme bundle (`EditorView.theme` chrome + a `HighlightStyle`) mapping the podracer `tokens.css` OKLCH
  vars onto the code pane. Verification metadata pinned to the task base until closeout stamps the L2
  code commit.
