# subjectReview.invariant.captured.json

## Governing Overview

[overview.md](../overview.md)

## Purpose

Retain a captured invariant-selected response with an authored concern for central subject-review regressions.

## Code Commentary

### Logic

The response carries the selected invariant revision-selection state, retained revisions and its own assessment. Cases preserve ambiguous heads without a first/latest guess and contrast this subject read with family-selected evidence. Fixture identities remain test inputs and are never promoted as normal project knowledge. The body is a real review-route response re-captured over HTTP (route bytes omit null fields); its receipt row in `subjectReview.capture-provenance.json` names the command, source tree, scenario and requests. Each of its 18 member sources carries the structured `locator`, `resolved_ranges` and `locator_state` fields; every locator here is a `file` locator, so the sources are `whole_file` on the exact recorded blob or `unresolved` otherwise, and none carries a range.

### Conventions

Keep captured provenance and exact input identities intact. Only the test harness selects these fixtures.

### Invariants And Boundaries

This source supplies scoped regression evidence, not semantic approval, execution certification or a replacement for the real mounted workflow.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No Domain Documentation source is configured; the fixture and regression source establish this local test contract.

No configured domain source could be checked.

### Repo-Internal References

The named case or selected revision field is the direct source of this test input.

- The case or fixture preserves its own selected input. [1]
- The member sources carry their structured locator state as the route emits it. [2]
- The receipt row naming this body's re-capture command, source tree and requests. [3]

### Cross-Repo References

No independent cross-repository authority is introduced.

No additional cross-repository evidence is required.
