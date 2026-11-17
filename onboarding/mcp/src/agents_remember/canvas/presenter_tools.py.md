# mcp/src/agents_remember/canvas/presenter_tools.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The shared implementation of the explainer’s draft render: digest-checked input reads, guarded assets, and one report and set of pictures per run. The bound task server calls it; this module starts no standalone server.

## Code Commentary

- `AuthoringTools` receives explicit working, host, grants and optional renders paths. It checks that the grant names the working folder; `read` accepts only granted inputs and checks their digests.

- `render` asks `canvas.explainer_browser` for the missing browser before it prepares anything. With a browser missing and no announcement yet in this workspace, it fetches nothing: it answers `state: announce` with the missing part, the one sentence and a request to call again, and keeps that announcement in `state/browser-announced.json` so the next call renders instead of announcing again. The next call fetches, loads and publishes. Nothing is downloaded before the seat could say the sentence.
- `_remember` keeps the last render's failure in `state/last-render.json` while it ended `unavailable` for a missing browser, so the review page's own empty block and its line over an earlier page can say what is missing and the command; a published page clears both that record and the announcement. `keep_report` answers `None` for an answer that began no run, so the announce has no run folder to write into.

## Evidence








- The first render on a browserless installation fetches nothing and answers announce with the missing part and the sentence. [4]
- The announcement is kept in the workspace state folder so the next call renders instead of announcing again. [5]
- The last render that ended unavailable for a missing browser is kept for the page and cleared by a published page. [6]
- A run-less answer is filed nowhere and answered as it stands. [7]


- The shared authoring implementation admits the prepared folder and its exact input grants. [1]
- AuthoringTools admits the prepared input grants and output folder; the standalone presenter server constructor and CLI entry are removed. [3]
