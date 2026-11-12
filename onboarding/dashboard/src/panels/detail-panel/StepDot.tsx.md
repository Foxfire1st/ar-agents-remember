# dashboard/src/panels/detail-panel/StepDot.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Show a cached major-step state mark and pointer-rest details without fetching data or adding a focus stop.

## Code Commentary

After 300ms of non-touch pointer rest, a supplied step opens a body portal showing its ID, Markdown title, display state and ordered nested states. The optional-payload fallback still draws the state mark but cannot open details. Layout measures the portal and clamps its initial placement near the anchor within the viewport.

Pointer leave/down cancels the timer and closes details; unmount cancels a pending timer. This is pointer interaction, not keyboard tooltip or continuous scroll-tracking ownership. Details use already supplied step data, not a body request or lifecycle authority.

MIK-R175 rule 3: in the tooltip's head and in every substep row the id and the status word carry `tipPart` — full width, never shrunk or wrapped — while the title alone takes `tipTitle` and wraps. The style objects are exported beside their `css()` results so that contract is pinned without layout.

## Evidence

- The tooltip's id and status word keep their full width while only the title wraps. [2]


- Optional cached step details use a cancelable non-touch pointer-rest timer and a body portal, with no fetch or tab stop. [1]
