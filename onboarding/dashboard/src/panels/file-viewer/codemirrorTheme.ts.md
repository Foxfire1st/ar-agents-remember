# dashboard/src/panels/file-viewer/codemirrorTheme.ts

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

Maps the podracer OKLCH palette (the `styles/tokens.css` `:root` vars) onto CodeMirror 6 so the
read-only code pane matches the rest of the cockpit. Exports a single `codeTheme` extension that the
code pane mounts.

## Code Commentary

### Logic

Two pieces are now unified in one `chrome = EditorView.theme({...}, { dark: true })` extension: editor
chrome (bg/ink/height/font-size from `--bg-panel`/`--ink`, scroller font from `--font-mono`, gutters
from `--bg`/`--grid`, transparent active line, amber-tinted selection via `color-mix` over `--amber`,
and removed focus outline) plus the eleven foreground-only server-computed tree-sitter token classes
(`.cm-ar-tok-*`): keywords/types/tags/bold headings → `--amber`, strings → `--mint`, numbers/functions →
`--cyan`, attributes → `--ink`, and **comments (italic) + operators/punctuation → a readable
mid-lightness ink/bg blend** (`color-mix(in oklab, var(--ink) 60%/75%, var(--bg))`) rather than `--grid`
(the 0.30-L gutter tone, near-invisible on the 0.16-L bg; gutter line numbers still use `--grid`). The
exported `codeTheme: Extension = chrome` carries no `@codemirror/language` or `@lezer/highlight`
dependency so foreground-only decorations preserve citation and merge-diff background tints.

### Invariants And Boundaries

No CSS animation here — motion is GSAP/Motion only (master invariant), as the header states. Colors are
read from CSS custom properties rather than hardcoded, so the theme tracks the live token set;
`tokens.css` owns the actual OKLCH values. Purely presentational and shared by every CodeMirror surface
(the plain pane and L4's diff) so syntax tokens stay identical across them.

## Evidence

### Repo-Internal References


- `FilePane` builds its `EditorView` with this theme bundle. [1]
- The CodeMirror chrome bundle reads the panel, ink, grid, amber selection, and monospace font tokens. [2]
- The foreground-only `.cm-ar-tok-*` token classes map server highlight kinds onto amber, mint, cyan, ink, and mid-lightness comment/operator blends. [3]
