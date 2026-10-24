# mcp/tests/test_canvas_prospective.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The prospective load before publication: a failed or unavailable load refuses publication and keeps the last ready revision, a loaded revision publishes exactly the assets the loader saw, and the static check never stands in for a load.

## Code Commentary

- A load that cannot run is an unavailable load, not a pass.
- The published revision carries exactly the bytes that were loaded.


The rendered reference-inventory case keeps `claimIds` separate from `evidenceReferences`: real packet claim IDs pass in `claimIds`, a claim ID used as a basis reference fails, and a basis reference used as a claim ID fails. It also pins the default loader's separate DOM selectors for the two marks; no browser run is claimed by reading these assertions.

## Evidence

- The case `test_a_failed_load_refuses_publication_and_keeps_the_last_ready_revision` protects this behaviour. [1]
- The case `test_the_static_check_never_stands_in_for_a_load` protects this behaviour. [2]

- The rendered reference-inventory case keeps `claimIds` separate from `evidenceReferences`: real packet claim IDs pass in `claimIds`, a claim ID used as a basis reference fails, and a basis reference used as a claim ID fails. It also pins the default loader's separate DOM selectors for the two marks; no browser run is claimed by reading these assertions. [3]
