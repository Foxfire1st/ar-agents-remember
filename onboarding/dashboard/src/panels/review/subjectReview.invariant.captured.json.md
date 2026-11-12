# dashboard/src/panels/review/subjectReview.invariant.captured.json

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Retained test input for the review consumers, recording its own response identities, states and bounded populations.

## Code Commentary

This file is fixture data, not current project knowledge or a new selection authority. Its literal response states and counts belong to the recorded input. Reading it does not execute its producer, validate an installed dashboard, reproduce the capture or grade the present candidate. A provenance field is a recorded custody statement, not an independent observation made by this card.

### Current input shape

- Root keys: `["state", "operation", "repository_id", "payload"]`
- Root collection sizes (physical JSON containers, not gate verdicts): `{"payload": {"kind": "dict", "count": 11}}`
- Structured state blocks (a state beside payload, operation, comparison, cards, worklist, entries or items): 3; the bounded inventory below shows 3. This is a structural inventory, not a producer count. Other values remain available through the whole-file citation.

#### Recorded state block 1

```json
{
  "jsonPath": "$",
  "state": "review",
  "operation": "read_knowledge_review",
  "candidate": {
    "repository_id": "agents-remember",
    "master": "260928_maintained-invariant-knowledge",
    "leaf_id": "260928-MIK-L37",
    "task_ref": "260928_maintained-invariant-knowledge"
  },
  "knowledge": {
    "selection_state": "subject_selected",
    "revision_selection": {
      "record_kind": "invariant",
      "record_id": "104c2f90-c046-578f-950a-2a66c9ac93d0",
      "state": "compared",
      "before_revision_id": "d8cc11c2-1643-59e4-91de-2c9c849f14cc",
      "after_revision_id": "4089659e-cba1-5ed3-98ed-c902a9ebe1e0",
      "before_heads": [
        "d8cc11c2-1643-59e4-91de-2c9c849f14cc"
      ],
      "after_heads": [
        "4089659e-cba1-5ed3-98ed-c902a9ebe1e0"
      ],
      "before_retained": [
        "d8cc11c2-1643-59e4-91de-2c9c849f14cc"
      ],
      "after_retained": [
        "4089659e-cba1-5ed3-98ed-c902a9ebe1e0"
      ],
      "statement": "the invariant 104c2f90-c046-578f-950a-2a66c9ac93d0 comparison uses the before revision d8cc11c2-1643-59e4-91de-2c9c849f14cc and the after revision 4089659e-cba1-5ed3-98ed-c902a9ebe1e0, each recorded by its own memory tree"
    }
  },
  "judgment": {
    "state": "rows",
    "detail": "The leaf's recorded judgments in attempt order.",
    "rows.count": 2,
    "proofs.count": 0
  },
  "family_context": {
    "state": "partial",
    "families_total": 1,
    "families_returned": 1,
    "families_remaining": 0,
    "membership_rows_total": 22,
    "unique_member_revision_total": 13,
    "entries.count": 1,
    "sides": [
      {
        "family_id": "b6bbe31f-6ff4-50cc-aa80-c1dc91809539",
        "side": "before",
        "state": "recorded",
        "members_total": 11,
        "members.count": 11,
        "page": {
          "state": "first_page",
          "complete": false,
          "counts": {
            "invariant_revisions_total": 11,
            "family_revisions_total": 1,
            "memberships_total": 11,
            "realization_claims_total": 28,
            "advertised_expansions_total": 0,
            "primary_items_total": 51,
            "primary_items_returned": 30,
            "primary_items_remaining": 21,
            "distinct_source_locations_total": 27,
            "distinct_source_paths_total": 17,
            "unresolved_anchor_total": 10
          }
        }
      },
      {
        "family_id": "b6bbe31f-6ff4-50cc-aa80-c1dc91809539",
        "side": "after",
        "state": "recorded",
        "members_total": 11,
        "members.count": 11,
        "page": {
          "state": "first_page",
          "complete": false,
          "counts": {
            "invariant_revisions_total": 11,
            "family_revisions_total": 1,
            "memberships_total": 11,
            "realization_claims_total": 29,
            "advertised_expansions_total": 0,
            "primary_items_total": 52,
            "primary_items_returned": 29,
            "primary_items_remaining": 23,
            "distinct_source_locations_total": 28,
            "distinct_source_paths_total": 17,
            "unresolved_anchor_total": 0
          }
        }
      }
    ]
  }
}
```

#### Recorded state block 2

```json
{
  "jsonPath": "$[\"payload\"][\"source\"][\"inventory\"]",
  "state": "measured",
  "entries.count": 179
}
```

#### Recorded state block 3

```json
{
  "jsonPath": "$[\"payload\"][\"family_context\"]",
  "state": "partial",
  "entries.count": 1
}
```

### Reading boundary

Missing fields are not converted into zero counts. Present state, measured population, carried page and continuation-field presence remain separate observations; an opaque cursor is not decoded or called admitted here. Synthetic overlays in consuming tests require their own disclosure and do not turn this recorded body into fresh native or browser acceptance. Regeneration belongs to the source/capture owner; old fixture descriptions below are not instructions to fabricate successful response bytes.

## Previous Input Account — Historical Only

The following account describes the preceding fixture bytes, receipts and consuming-test scope. Its present-tense clauses, measurements and numeric reference labels are historical, not current guarantees or live citations. The actual current input shape is recorded above; general design context is retained here rather than discarded.

> # subjectReview.invariant.captured.json
>
> ## Governing Overview
>
> [overview.md](../overview.md)
>
> ## Purpose
>
> Retain a captured invariant-selected response with an authored concern for central subject-review regressions.
>
> ## Code Commentary
>
> ### Logic
>
> The response carries the selected invariant revision-selection state, retained revisions and its own assessment. Cases preserve ambiguous heads without a first/latest guess and contrast this subject read with family-selected evidence. Fixture identities remain test inputs and are never promoted as normal project knowledge. The body is a real review-route response re-captured over HTTP (route bytes omit null fields); its receipt row in `subjectReview.capture-provenance.json` names the command, source tree, scenario and requests. Each of its 18 member sources carries the structured `locator`, `resolved_ranges` and `locator_state` fields; every locator here is a `file` locator, so the sources are `whole_file` on the exact recorded blob or `unresolved` otherwise, and none carries a range.
>
> ### Conventions
>
> Keep captured provenance and exact input identities intact. Only the test harness selects these fixtures.
>
> ### Invariants And Boundaries
>
> This source supplies scoped regression evidence, not semantic approval, execution certification or a replacement for the real mounted workflow.
>
> ### Todos
>
> No additional work is asserted by this card.
>
> ## Evidence
>
> ### Docs References
>
> No Domain Documentation source is configured; the fixture and regression source establish this local test contract.
>
> No configured domain source could be checked.
>
> ### Repo-Internal References
>
> The named case or selected revision field is the direct source of this test input.
>
> - The case or fixture preserves its own selected input. (historical reference 1)
> - The member sources carry their structured locator state as the route emits it. (historical reference 2)
> - The receipt row naming this body's re-capture command, source tree and requests. (historical reference 3)
>
> ### Cross-Repo References
>
> No independent cross-repository authority is introduced.
>
> No additional cross-repository evidence is required.

## Evidence

### Repo-Internal References

- The current retained JSON input supplies the literal identities, response states and populations summarized above; these are fixture facts, not live project knowledge or fresh execution evidence. [4]
