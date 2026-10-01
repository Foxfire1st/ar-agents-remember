# mcp/src/agents_remember/models/knowledge/projection.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The projection rule, and the whole of it is one property: **a projection may display an assessment,
and when it does the assessment's provenance and status travel with it** — its author, its exact
examined inputs and its recorded disposition.

## Code Commentary

### Logic

`AssessmentDisplay` carries the recorded `disposition` verbatim, the recorded `author`, the exactly
recorded `examined_inputs`, and a `status` drawn from `ASSESSMENT_STATUSES` — `current` or `stale`,
exhaustive on purpose. Its validator refuses a blank author and refuses a display with no examined
inputs, so a conclusion cannot be rendered without its basis. `status` is *measured from the examined
inputs* rather than stored beside them, which is why a stale assessment stays stale: nothing here
re-judges and no path upgrades a status.

`ProjectionRow.assessment` is `None` for an unassessed claim rather than an instance with empty
fields, because an instance with empty fields is a *present* assessment that happens to say nothing.
`assessment_display` is the one constructor and it derives the status from the row's recorded inputs.

### Invariants And Boundaries

- **Missing stays missing.** An unassessed claim renders as unassessed; there is no favourable
  default and no manufactured approval.
- **A disagreement is displayed, not resolved.** Picking a winner between two assessments would be a
  new interpretation rather than a rendering.
- **No field can hold a conclusion, a severity or a recommendation**, so a projection cannot acquire
  one by accident.
- **Nothing here persists, publishes or deletes.** The module imports no store, holds no handle and
  writes no file: a projection is derived and regenerable, never a second authority. Regenerating it
  is the only way it changes.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The two statuses a displayed assessment can carry, exhaustive because the assessment either examined the inputs the row now rests on or it did not.** [1]
- **The display that refuses a conclusion without its basis: a recorded disposition, a named author and the exact examined inputs.** [2]
- **The row whose missing assessment is `None` rather than an empty instance, and the one constructor that measures the status from the recorded inputs.** [3]
- The models vocabulary this rule is built on. [4]
- **The cases that measure the three consequences: a conclusion without its basis is refused, a missing assessment renders missing, and a stale assessment is never upgraded.** [5]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
