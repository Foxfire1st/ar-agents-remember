# dashboard/src/cockpit/paseoPluginClient.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The helper suite protects web page lifetime, exact framing trust, checked navigation and appearance/write provenance.

## Code Commentary

Cases bound reloads, retain first-visit deep links and exercise the one opening migration for an old stored-closed host sidebar: with the state open, closed and absent the plugin does not click the toggle on an ordinary load and writes nothing to the host's stored panel state, while a stored closed list is opened once and marked. Fresh trust waits for exact pair confirmation; window/origin lookalikes fail. Same-page verified trust is rechecked for explicit revocation, and stopped async completion does nothing. Shared-storage cases distinguish running-look writers.

## Invariants And Boundaries

The old initial-open sidebar claim is superseded. Plain-page/SDK fixtures do not establish live native framing or actor operations.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- A page is replaced once and the resulting page consumes its reload flag without replacing itself again. [1]
- Parent detection, exact origin pairing and the actual parent window are asserted separately from top-level or lookalike pages. [2]
- The client-part cases distinguish standalone, listed and unlisted frames, waiting for the embed list before opening the trusted channel. [3]
- Saves standalone look/sidebar values before storing the AR appearance, and keeps earlier saved values when the last recorded writer was a frame. [4]
- Waits for an exact embed-list match before trusting a new parent and drops a previously trusted bridge when the refreshed list excludes it. [5]
