# mcp/tests/test_canvas_authoring_retired.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The retired authoring POSTs refuse by name while a page already saved keeps opening, and a frame the request named is never answered with another frame's bytes.

## Code Commentary

- Every retired authoring path answers the same typed refusal, and the refusal is registered ahead of the canvas routes so it is what matches.
- Refusing authoring costs nothing already saved: the frame state, the page itself and a single asset segment all still answer.
- On the real app a refusal leaves the frame state byte-identical, while sessions, both revisions, nested assets and bridge messages keep working.
- A frame folder that does not exist is refused by name rather than swapped for a sibling's bytes.

## Evidence

- The case `test_every_retired_authoring_post_refuses_by_name` protects the typed refusal every retired authoring path answers. [1]
- The case `test_the_saved_page_and_its_reads_still_serve` protects the saved page, its asset and its frame state surviving the refusal. [2]
- The case `test_a_saved_pages_assets_keep_their_path_conversion` protects an asset conversion reaching the route behind the refusal. [3]
- The case `test_real_create_app_serves_saved_frame_revisions_nested_assets_and_bridge_messages` protects zero effects from a refusal on the real app while sessions and messages still work. [4]
- The case `test_a_missing_frame_is_refused_by_name_and_never_swapped` protects a missing frame being refused by name instead of answered with another frame's bytes. [5]
