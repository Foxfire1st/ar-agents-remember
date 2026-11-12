# dashboard/src/panels/review/outline.test-utils.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Adapt immutable pre-R86 captures to the R86 outline tree without changing their bytes: build an explicit synthetic catalogue outline over captured family contexts so older bodies stay mountable as tests.

## Code Commentary

- `syntheticCatalogue` unions the family contexts of the given results into outline families (ordered by delivered `authored_position`) with a per-member change derived by `memberChange`: absent on one side reads `added`/`removed`, a delivered intent fact reads `changed`, else equal revision sets read `unchanged`.
- Family change compares the before and after joint guarantees; members carry `joined`/`left`/`both` membership; catalogue entries list every family then every invariant with its summary.
- The outline is labelled synthetic in its own detail, so no test mistakes it for a served outline.

## Evidence

- Synthetic catalogue and outline over captures [1]
- Per-member change from presence, facts and revisions [2]
- Guarantee comparison for family change [3]
- Explicit synthetic labelling in the outline detail [4]
