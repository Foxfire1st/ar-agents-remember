# dashboard/src/data/keymap/zones.ts

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

Pure keyboard routing for chrome and review zones. Unknown and removed zone markers fall back to chrome; editable targets suppress printable bindings.

## Code Commentary

zoneForTarget follows the nearest data-kbzone marker and recognizes only review/chrome. isEditableTarget recognizes editable content, text areas, selects and writable inputs; isPrintable checks a single unmodified character. routeKey applies the same editable/printable rule to both zones. No PTY reserved dispatch or slashOpensPalette remains; this module owns neither editor configuration nor hosted terminal interception.

## Evidence

### Repo-Internal References

- Current zone resolution and editable/printable routing own chrome/review only. [1]

- The current source suite asserts chrome/review fallback and printable suppression, not PTY passthrough or slash rules. [4]

- Review is explicitly recognized and unknown/removed markers fall back to chrome. [5]
