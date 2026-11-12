# mcp/tests/reviewer_leaf_view_support.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Provides direct/child leaf-view parity adapters and instrumentation that distinguishes reuse of classifications from merely cached blob reads.

## Code Commentary

`direct_leaf_view` returns the unpersisted worklist with `_review` facts computed for the supplied trees. `observe_child` wraps the real child reply parser and records validated replies with transport byte count and request payload. `classified_leaf_view` runs a script through the real child-script seam, instruments entry/path classifications, code opens, hunk intersections and knowledge-side construction, and writes observations to the caller-supplied path.

The assertions require each entry and gate path to classify once, no new classification counters during leaf facts or gate-answer reconstruction, exactly one K_B and K_C construction, actual reuse of the same classifier/path objects, and cleared classifier/candidate/path/pairing state after the run. The result remains the production `ReviewTreesResult` rather than a synthetic replacement.

## Invariants And Boundaries

These are source-defined test assertions and instrumentation, not fresh executions or a latency/acceptance claim. The helper intentionally uses private test seams, not production publication authority.

## Evidence

- The direct adapter keeps the worklist’s own bytes and adds review facts without persistence. [1]
- The observer records validated child replies and actual transport metadata. [2]
- The child-script instrumentation separately asserts actual classification reuse and released run-local state. [3]


