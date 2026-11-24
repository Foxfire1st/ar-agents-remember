# mcp/tests/test_canvas_prospective.py

## Governing Overview

[governing route overview](overview.md)

The fixture covers visible-content eligibility, advisory interactions and the distinct DOM and loaded-asset inventories. Its bound document has the normal revision binding without an effects field or dataset bridge.

## Purpose

The prospective load before publication: a failed or unavailable load refuses publication and keeps the last ready revision, a loaded revision publishes exactly the assets the loader saw, and the static check never stands in for a load.

## Code Commentary

- A load that cannot run is an unavailable load, not a pass.
- The published revision carries exactly the bytes that were loaded.


The rendered reference-inventory case keeps `claimIds` separate from `evidenceReferences`: real packet claim IDs pass in `claimIds`, a claim ID used as a basis reference fails, and a basis reference used as a claim ID fails. It also pins the default loader's separate DOM selectors for the two marks; no browser run is claimed by reading these assertions.

- The browser cases hold the load's own preconditions: a load that names its own Node is an instrumented load and fetches nothing, a load whose browser cannot be made ready is `unavailable` with nothing loaded, a render answer carries the browser it ran with, and the presenter's first render on a browserless installation announces and fetches nothing.

The runner-source test pins the WebM and MP4 MIME mappings.

## Evidence




- A load whose browser cannot be made ready is unavailable and stages no run. [5]
- A render answer carries the browser the page was loaded with. [6]
- A first render with a missing browser announces and fetches nothing. [7]

- A failed prospective load keeps the previous ready revision. [1]
- Static readiness does not stand in for a prospective load. [2]
- The prospective checks distinguish actual claim IDs from basis references. [3]
- The runner source maps WebM to video/webm and MP4 to video/mp4. [8]
- An instrumented load names its Node. The default load uses the product's Node and browser. [4]
