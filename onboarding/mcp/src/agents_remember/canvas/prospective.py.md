# mcp/src/agents_remember/canvas/prospective.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The model-free load of a prospective revision before its ready pointer moves. It stages the exact bytes, loads them once in the selected browser through the package-owned runner, and reports what was observed.

## Code Commentary

- `BrowserProspectiveLoad.load` refuses a path that leaves the staging directory, runs the child once, and treats an unreadable answer as an unavailable load rather than a pass.
- Before it stages a run folder, `load` calls `_browser_unready`: a load that runs on the product's own Node asks `canvas.explainer_browser` to make the module and Chromium ready, and a refusal becomes an `unavailable` load named `browser` with nothing published and no run folder left behind. A caller that names its own `node` is an instrumented load: it brings its own browser and nothing is fetched for it. The browser the load used travels in `ProspectiveResult.browser` and in the render answer.
- A `loaded` answer that names its own faults is downgraded, so a pass cannot contradict its own observations.
- `StaticProspectiveLoad` stands in a load's place and says so, which keeps the difference between a static check and a real load visible.

The browser’s legacy evidence references and `data-evidence-claim` ids are read as separate bounded inventories. `_validate_rendered_citations` resolves both against the bound packet and checks the static part map: an unknown claim, unresolved claim basis or invalid part map makes the load fail, even when the browser otherwise reports loaded.

## Evidence

- The prospective revision is loaded once in the selected browser through the package-owned runner. 
- A success that contradicts its own observations is downgraded. 


- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/prospective.py::BrowserProspectiveLoad - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/canvas/prospective.py::_consistent - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.


- The load makes the product's browser ready before it stages a run folder, and a load that names its own Node fetches nothing. [4]
- The browser the load used travels in the load's result. [5]


- The current implementation separates claim IDs from basis references and validates rendered citations/parts before accepting the browser result. [3]
