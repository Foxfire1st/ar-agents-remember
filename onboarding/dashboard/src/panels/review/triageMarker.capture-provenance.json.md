# dashboard/src/panels/review/triageMarker.capture-provenance.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The receipt of the one body MIK-L33's merge round captured for its marker test.** It names the capture time
(2026-09-30T19:18:28Z), the producer (`notes/reports/260928-MIK-L33-evidence/merge-round/capture_merge_fixtures.py`)
and its command, the route, the source tree (the L33 worktree on base `d3a22213`, MIK-L34 landed, with this leaf's
changes), the scratch (`/tmp/mik-l33-merge`: MIK-L34's scenario rebuilt with MIK-L34's own scripts, after
`break-family`), comparison `3`, the attempts, and one row: the expression cards of FAM-4V4GSQCS's five invariants
(`GET /api/review/trees`, 0.05 s).

## Code Commentary

### Logic

The one body exists so the card of INV-Z66EMHMH on comparison 3 can be opened and its marker followed in `ReviewSurface.triageMarkers.test.tsx`; the comparison's other bodies are MIK-L34's re-captured `markerUnknown.*`.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

A scratch-copy capture, not current project knowledge. Its sha256 and byte count match the body (checked by this curation).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- When, by what command, at which source tree and over which scratch and comparison the body was captured. [1]
- The one receipt row. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
