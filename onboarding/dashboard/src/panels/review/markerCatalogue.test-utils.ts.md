# dashboard/src/panels/review/markerCatalogue.test-utils.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Adapt immutable pre-R86 marker captures to the R86 tree: carry their recorded change facts into a synthetic outline without interpreting a missing roster as removal, and reach a family's existing card from a captured invariant answer.

## Code Commentary

- `syntheticMarkerCatalogue` starts from `syntheticCatalogue`, then overlays the delivered facts: an unknown family guarantee marks the outline family `unknown`, and delivered `implementation` or `unknown` member facts adjust the invariant rows (implementation alone never reads as a meaning change).
- `syntheticMarkerFamilyReview` clones the captured invariant answer with the family's own revision selection taken from its first context entry, so the family's existing card is reachable while the marker's target answer stays an untouched capture.

## Evidence

- Recorded facts carried into the synthetic outline [1]
- Family review reached from the captured selection [2]
