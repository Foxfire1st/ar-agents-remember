# dashboard/src/panels/review/markerUnknown.cards.captured.json

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Retain a test-only input/capture receipt for the reviewer.

## Code Commentary

The facts below are read from the retained source bytes, not from a fresh producer invocation.

### Retained Input Facts

- `state`: "trees"
- `repository_id`: "agents-remember"
- `comparison.number`: 3
- `comparison.keys`: ["schema", "task_id", "leaf_id", "number", "code_base", "code_candidate", "memory_base", "memory_candidate", "recorded_at"]
- `entries.count`: 2
- `entries.kind_counts`: {"realization": 2}

These are fixture facts, not current project knowledge. A receipt states its recorded capture custody; reading it here does not recreate its command or validate an installed dashboard.

## Evidence

- The retained source supplies the facts and declared boundaries described above. [1]
