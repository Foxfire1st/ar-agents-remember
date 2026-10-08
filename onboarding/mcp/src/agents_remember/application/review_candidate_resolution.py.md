# mcp/src/agents_remember/application/review_candidate_resolution.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Resolves a canonical review selection into its exact before and candidate source/memory trees, with typed refusals when that selection cannot be resolved.

## Code Commentary

`resolve_review_candidate` admits only the declared selectors and enclosure identity. For a live leaf, `_live_resolution` obtains the source tree through the existing capture owner and resolves converted memory through `tree_resolution`. Its baseline_database and candidate_database fields name derived indexes of the selected trees. An unconverted half is explicitly legacy-unavailable, not an empty or substituted dataset. Recorded/closed leaf selection delegates to the retained generation owner. `require_current_candidate_identity` detects a candidate that moved after admission. The old REVIEW_BASELINE_DIRECTORY and REVIEW_CANDIDATE_DIRECTORY layout and dataset receipts are retired.

## Evidence

### Repo-Internal References

- `resolve_review_candidate` owns the current boundary described above. [23]
- `_live_resolution` owns the current boundary described above. [24]
- `require_current_candidate_identity` owns the current boundary described above. [25]
