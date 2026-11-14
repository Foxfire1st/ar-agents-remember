# dashboard/src/panels/review/explainer/ExplanationEmptyBrowser.test.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Display assertions for supplied browser announcements and last-render failures: the failure appears inside the empty block without a page, while the top-level browser notice can appear both without a page and above a retained page.

## Code Commentary

- The cases fix the state the server sends (`browserNotice`, `lastRender`) and read only what the panel draws, so they hold the display contract rather than the render path's own answers; the server side of the same record is covered in `mcp/tests/test_explainer_server.py`.
- The empty-failure case checks that the block contains the Playwright version and fetch command, retains its Explain button and has no `explanation-empty-browser-fetch` control.
- The failure-over-page case checks the failed-publication wording, fetch command and “earlier” text, while the saved frame remains present. The final case supplies `NOTHING_YET` with `lastRender: null`; it checks Explain and absence of the empty-block browser failure, without supplying a published page.

## Relationships

It draws `ExplanationView`'s `statusLine` and `failureLine` through the shared view fixtures, and depends on `explainerApi`'s `browserNotice` and `lastRender` parsers. The records those fields come from are written by `canvas.presenter_tools` and read by `serving.explainer`.

## Evidence

- With no page, the empty block names the missing browser and the command, and adds no control. [1]

- Without a page, the supplied announcement appears in the top-level browser notice. [2]
- With a saved page, the announcement appears and the frame remains drawn. [3]
- With a saved page, the failure notice contains the fetch command and “earlier”, and the frame remains drawn. [4]
- An empty state with no last-render failure retains Explain and omits the empty-block browser failure. [5]
