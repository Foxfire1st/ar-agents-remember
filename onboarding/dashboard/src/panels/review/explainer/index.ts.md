# dashboard/src/panels/review/explainer/index.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The module's public surface: the top line's switch, the explanation page and its parts, the planned page with its readers, and the one read the review page mounts.

## Code Commentary

- The review page mounts these exports and keeps owning the top line, the tree and the chat, so this module owns the explainer's page without reaching into that file.
- Components are exported with their prop types, so a caller can type what it mounts.
- The planned page is exported together with its payload readers and pure orders, keeping planned mode inside one surface.
- The pure model helpers and the host's answer types are re-exported too, so the page and its tests import the vocabulary from one place.
- Nothing here is a route, a reader or a side effect: the surface is declarations only.

## Evidence

- The switch is exported with its prop type and its view type
- The planned page is exported with the payload readers and pure orders it needs [2]
- The one read and the limit refusal are exported for the page's owner [3]

- Retired at the fifth freeze d59c3493: dashboard/src/panels/review/explainer/index.ts:23-23 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
