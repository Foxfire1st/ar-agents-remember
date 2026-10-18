# mcp/tests/review_curator_fixture_support.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Builds a real curator-coherence assessment fixture for lifecycle/history tests independently of retired dashboard evidence channels.

## Code Commentary

`build_recorded_fixture` creates a converted Git-tree world, loads its exact contract, authors fixture topology and passing route-review input, then prepares and publishes an assessment through `curator_coherence_action`. The returned frozen fixture keeps world, contract and sprint identity. `_publish_assessment` writes the fixture evidence text under the task root, uses the prepared candidate set and publication input helper, supplies a judgment per candidate and a separate assessment collection, and asserts published or already-current. `_assessment_revision` binds its concern to the fixture invariant’s exact projected revision pair and task-relative evidence.

This support writes only when a test invokes it on its supplied fixture directory. It does not seed a live reviewer evidence pane or stand in for publication with a fabricated response.

## Invariants And Boundaries

A passing-route fixture is test setup, not an independent acceptance result. This analysis inspected the code and did not invoke its publisher. Historical assessments remain valid lifecycle data even though the dashboard channel is retired.

## Evidence

- The fixture uses a real world/contract and calls its publication helper. [1]
- Fixture evidence and real prepare/publish calls remain separate from review display channels. [2]
- The authored assessment names the fixture revision pair and evidence namespace. [3]
