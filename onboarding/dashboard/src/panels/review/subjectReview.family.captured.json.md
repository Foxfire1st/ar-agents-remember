# dashboard/src/panels/review/subjectReview.family.captured.json

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
      "record_kind": "family",
      "record_id": "fa2aac3a-f406-595a-a1e6-b50c656704ca",
      "state": "compared",
      "before_revision_id": "69927d22-e430-55b2-8f31-f84e01534db1",
      "after_revision_id": "c90b49d3-c3bd-5399-9478-25eecd7a6468",
      "before_heads": [
        "69927d22-e430-55b2-8f31-f84e01534db1"
      ],
      "after_heads": [
        "c90b49d3-c3bd-5399-9478-25eecd7a6468"
      ],
      "before_retained": [
        "69927d22-e430-55b2-8f31-f84e01534db1"
      ],
      "after_retained": [
        "c90b49d3-c3bd-5399-9478-25eecd7a6468"
      ],
      "statement": "the family fa2aac3a-f406-595a-a1e6-b50c656704ca comparison uses the before revision 69927d22-e430-55b2-8f31-f84e01534db1 and the after revision c90b49d3-c3bd-5399-9478-25eecd7a6468, each recorded by its own memory tree"
    }
  },
  "judgment": {
    "state": "rows",
    "detail": "The leaf's recorded judgments in attempt order.",
    "rows.count": 2,
    "proofs.count": 1
  },
  "family_context": {
    "state": "recorded",
    "families_total": 1,
    "families_returned": 1,
    "families_remaining": 0,
    "membership_rows_total": 6,
    "unique_member_revision_total": 5,
    "entries.count": 1,
    "sides": [
      {
        "family_id": "fa2aac3a-f406-595a-a1e6-b50c656704ca",
        "side": "before",
        "state": "recorded",
        "members_total": 3,
        "members.count": 3,
        "page": {
          "state": "first_page",
          "complete": true,
          "counts": {
            "invariant_revisions_total": 3,
            "family_revisions_total": 1,
            "memberships_total": 3,
            "realization_claims_total": 9,
            "advertised_expansions_total": 0,
            "primary_items_total": 16,
            "primary_items_returned": 16,
            "primary_items_remaining": 0,
            "distinct_source_locations_total": 9,
            "distinct_source_paths_total": 8,
            "unresolved_anchor_total": 5
          }
        }
      },
      {
        "family_id": "fa2aac3a-f406-595a-a1e6-b50c656704ca",
        "side": "after",
        "state": "recorded",
        "members_total": 3,
        "members.count": 3,
        "page": {
          "state": "first_page",
          "complete": true,
          "counts": {
            "invariant_revisions_total": 3,
            "family_revisions_total": 1,
            "memberships_total": 3,
            "realization_claims_total": 11,
            "advertised_expansions_total": 0,
            "primary_items_total": 18,
            "primary_items_returned": 18,
            "primary_items_remaining": 0,
            "distinct_source_locations_total": 11,
            "distinct_source_paths_total": 9,
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
  "state": "recorded",
  "entries.count": 1
}
```

### Reading boundary

Missing fields are not converted into zero counts. Present state, measured population, carried page and continuation-field presence remain separate observations; an opaque cursor is not decoded or called admitted here. Synthetic overlays in consuming tests require their own disclosure and do not turn this recorded body into fresh native or browser acceptance. Regeneration belongs to the source/capture owner; old fixture descriptions below are not instructions to fabricate successful response bytes.

## Previous Input Account — Historical Only

The following account describes the preceding fixture bytes, receipts and consuming-test scope. Its present-tense clauses, measurements and numeric reference labels are historical, not current guarantees or live citations. The actual current input shape is recorded above; general design context is retained here rather than discarded.

> # subjectReview.family.captured.json
>
> ## Governing Overview
>
> [overview.md](../overview.md)
>
> ## Purpose
>
> Retain a captured family-selected response for subject-navigation regressions.
>
> ## Code Commentary
>
> ### Logic
>
> The family response records its own selected family context and record-channel availability. It is paired with the invariant-selected response to prove a family read cannot establish a member assessment absence. The fixture is test evidence, not a current production dataset or invented authored judgment. The body is a real review-route response re-captured over HTTP (route bytes omit null fields); its receipt row in `subjectReview.capture-provenance.json` names the command, source tree, scenario and requests. Each of its 10 member sources carries the structured `locator`, `resolved_ranges` and `locator_state` fields; every locator here is a `file` locator, so the sources are `whole_file` on the exact recorded blob or `unresolved` otherwise, and none carries a range.
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
