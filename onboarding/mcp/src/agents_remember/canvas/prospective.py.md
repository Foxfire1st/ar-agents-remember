# mcp/src/agents_remember/canvas/prospective.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The model-free load of a prospective revision before its ready pointer moves. It stages the exact bytes, loads them once in the selected browser through the package-owned runner, and reports what was observed.

## Code Commentary

- `BrowserProspectiveLoad.load` refuses a path that leaves the staging directory, runs the ordinary load, and treats an unreadable answer as an unavailable load. An optional separate diagnostic process records interaction coverage.
- Before it stages a run folder, `load` calls `_browser_unready`: a load that runs on the product's own Node asks `canvas.explainer_browser` to make the module and Chromium ready, and a refusal becomes an `unavailable` load named `browser` with nothing published and no run folder left behind. A caller that names its own `node` is an instrumented load: it brings its own browser and nothing is fetched for it. The browser the load used travels in `ProspectiveResult.browser` and in the render answer.
- A `loaded` answer that names its own faults — including browser-observed `media_faults` checked in `_observed_faults` — is downgraded to `failed` by `_consistent`, so a pass cannot contradict its own observations; `ProspectiveResult.diagnostics()` reports `media_faults` under `media-controls:`.
- `StaticProspectiveLoad` stands in a load's place and says so, which keeps the difference between a static check and a real load visible.

The Python reader accepts the browser’s full basis-reference and claim-ID string inventories from the bounded observation window. `_validate_rendered_citations` resolves both against the bound packet and checks the static part map: an unknown claim, unresolved claim basis or invalid part map makes the load fail, even when the browser otherwise reports loaded. `_read_result` also evaluates browser-observed `mediaElements` and `mediaFaults` through `_media_faults` into `ProspectiveResult.media_faults` so non-conforming script-inserted audio or video elements cannot pass unnoticed.

## Evidence

- The prospective revision is loaded once in the selected browser through the package-owned runner. 
- A success that contradicts its own observations is downgraded. 


- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/prospective.py::BrowserProspectiveLoad - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/canvas/prospective.py::_consistent - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.


- The load makes the product's browser ready before it stages a run folder, and a load that names its own Node fetches nothing. [4]
- The browser the load used travels in the load's result. [5]

- The Python reader validates separate basis and claim inventories and marked parts against the static part map and bound packet, keeps loaded assets and DOM inventory separate, and populates `media_faults` via `_media_faults`. [3]
- `_media_faults` re-derives autoplay, loop, and missing-controls faults from observed `mediaElements` merged with reported `mediaFaults`, and `ProspectiveResult.diagnostics()` reports them under `media-controls:`. [6]
- `_observed_faults` and `_consistent` include `result.media_faults` so a nominally `loaded` payload carrying media faults is downgraded to `failed`. [7]
