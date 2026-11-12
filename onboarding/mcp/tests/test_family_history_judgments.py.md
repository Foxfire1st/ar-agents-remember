# mcp/tests/test_family_history_judgments.py

## Governing Overview

[mcp/tests/overview.md](./overview.md)

## Purpose

Pins MIK-R48: recorded family meaning judgments keep their curator-authored effect
and their writer-recorded own revision, and the publication population judges only
the rows the route publishes.

## Code Commentary

The test source drives real Git fixture repositories under `tmp_path`: four effect labels
stored/read back, no-write refusals, own-revision currentness, master landing (a), open-file
refusal (b), leaf publication (d), frozen preservation and later attempts. For (c), baseless
validation still leaves closed historical rows unjudged, but now refuses solely for new
`R27.4-legacy-unassessed` debt. The based master landing still passes. These are source
assertions, not a fresh end-to-end run; hand-closed and disposition-specific drift facets remain.

## Evidence

- Each authored label is stored with the family revision and read back whole. [1]
- Bad inputs refuse with files, refs and index unchanged. [2]
- Open unpublished rows are refused naming file, row and rule. [4]
- The leaf's own unlabelled changed row is refused, open or hand-closed. [5]
- Drift refuses until the current row is authored again. [6]

- The based master landing passes over closed historical rows absent from its base; baseless validation does not judge those rows but refuses new `R27.4-legacy-unassessed` debt alone. [3]
- Current source delta inspected statically: Correct baseless whole-validation success without erasing the distinct historical-row exemption or based master-landing success. [7]
