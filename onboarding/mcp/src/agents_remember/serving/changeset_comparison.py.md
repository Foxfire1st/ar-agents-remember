# mcp/src/agents_remember/serving/changeset_comparison.py

## Governing Overview

[serving overview](overview.md)

## Purpose

`serving/changeset_comparison.py` runs the existing change-set viewer on a recorded review's exact trees: the code range and the memory range (limited to the two knowledge roots) of one numbered comparison, with per-file diffs read from immutable Git objects rather than the live filesystem.

## Code Commentary

`recorded_comparison` loads comparison N from the leaf's comparison directory, refusing unknown numbers by name. `_range` maps the record to `(repository, base, tip)` per half, using the converted base as the memory before-tree; `_files` runs one raw+numstat diff per half (no renames, memory scoped to `knowledge/` and `onboarding/`, non-text paths left to the inventory) with status and counts; `_paired_sidecars` marks code files whose onboarding sidecar exists on either memory tree; `_counts` sums the counters. `comparison_changeset` answers the `ComparisonChangeSet` body with scope, mode, number, echoed trees, lists and counters from exactly two diffs and no blob reads. `comparison_file_diff` resolves each side with `git show` on the recorded trees (missing path vs lost tree distinguished by `cat-file`), confines memory paths to the two roots, and never follows today's filesystem aliases.

## Evidence

- Comparison N loads from the leaf's comparison record [1]
- One diff per half supplies status and counts, renames off [2]
- The list echoes trees with code, memory and counters [3]
- File diffs read immutable trees and confine memory paths [4]
