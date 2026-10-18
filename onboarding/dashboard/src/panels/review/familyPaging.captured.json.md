# dashboard/src/panels/review/familyPaging.captured.json

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Retained test input for the review consumers, recording its own response identities, states and bounded populations.

## Code Commentary

This file is fixture data, not current project knowledge or a new selection authority. Its literal response states and counts belong to the recorded input. Reading it does not execute its producer, validate an installed dashboard, reproduce the capture or grade the present candidate. A provenance field is a recorded custody statement, not an independent observation made by this card.

### Current input shape

- Root keys: `["family_id", "subject_id", "before", "after"]`
- Root collection sizes (physical JSON containers, not gate verdicts): `{"before": {"kind": "list", "count": 4}, "after": {"kind": "list", "count": 5}}`
- Structured state blocks (a state beside payload, operation, comparison, cards, worklist, entries or items): 27; the bounded inventory below shows 6. This is a structural inventory, not a producer count. Other values remain available through the whole-file citation.

#### Recorded state block 1

```json
{
  "jsonPath": "$[\"before\"][0]",
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
      "record_id": "8b1a17ca-96ba-5ede-a09f-abfb11ada0a5",
      "state": "compared",
      "before_revision_id": "66a9bb32-08f4-5ff4-8d80-63a8417606cb",
      "after_revision_id": "ee4052e3-a8b7-5289-9399-d609257cc16a",
      "before_heads": [
        "66a9bb32-08f4-5ff4-8d80-63a8417606cb"
      ],
      "after_heads": [
        "ee4052e3-a8b7-5289-9399-d609257cc16a"
      ],
      "before_retained": [
        "66a9bb32-08f4-5ff4-8d80-63a8417606cb"
      ],
      "after_retained": [
        "ee4052e3-a8b7-5289-9399-d609257cc16a"
      ],
      "statement": "the invariant 8b1a17ca-96ba-5ede-a09f-abfb11ada0a5 comparison uses the before revision 66a9bb32-08f4-5ff4-8d80-63a8417606cb and the after revision ee4052e3-a8b7-5289-9399-d609257cc16a, each recorded by its own memory tree"
    }
  },
  "judgment": {
    "state": "rows",
    "detail": "The leaf's recorded judgments in attempt order.",
    "rows.count": 2,
    "proofs.count": 1
  },
  "family_context": {
    "state": "partial",
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
          "complete": false,
          "counts": {
            "invariant_revisions_total": 3,
            "family_revisions_total": 1,
            "memberships_total": 3,
            "realization_claims_total": 9,
            "advertised_expansions_total": 0,
            "primary_items_total": 16,
            "primary_items_returned": 4,
            "primary_items_remaining": 12,
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
          "complete": false,
          "counts": {
            "invariant_revisions_total": 3,
            "family_revisions_total": 1,
            "memberships_total": 3,
            "realization_claims_total": 11,
            "advertised_expansions_total": 0,
            "primary_items_total": 18,
            "primary_items_returned": 4,
            "primary_items_remaining": 14,
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
  "jsonPath": "$[\"before\"][0][\"payload\"][\"source\"][\"inventory\"]",
  "state": "measured",
  "entries.count": 179
}
```

#### Recorded state block 3

```json
{
  "jsonPath": "$[\"before\"][0][\"payload\"][\"family_context\"]",
  "state": "partial",
  "entries.count": 1
}
```

#### Recorded state block 4

```json
{
  "jsonPath": "$[\"before\"][1]",
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
      "record_id": "8b1a17ca-96ba-5ede-a09f-abfb11ada0a5",
      "state": "compared",
      "before_revision_id": "66a9bb32-08f4-5ff4-8d80-63a8417606cb",
      "after_revision_id": "ee4052e3-a8b7-5289-9399-d609257cc16a",
      "before_heads": [
        "66a9bb32-08f4-5ff4-8d80-63a8417606cb"
      ],
      "after_heads": [
        "ee4052e3-a8b7-5289-9399-d609257cc16a"
      ],
      "before_retained": [
        "66a9bb32-08f4-5ff4-8d80-63a8417606cb"
      ],
      "after_retained": [
        "ee4052e3-a8b7-5289-9399-d609257cc16a"
      ],
      "statement": "the invariant 8b1a17ca-96ba-5ede-a09f-abfb11ada0a5 comparison uses the before revision 66a9bb32-08f4-5ff4-8d80-63a8417606cb and the after revision ee4052e3-a8b7-5289-9399-d609257cc16a, each recorded by its own memory tree"
    }
  },
  "judgment": {
    "state": "rows",
    "detail": "The leaf's recorded judgments in attempt order.",
    "rows.count": 2,
    "proofs.count": 1
  },
  "family_context": {
    "state": "partial",
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
          "state": "continued",
          "complete": false,
          "counts": {
            "invariant_revisions_total": 3,
            "family_revisions_total": 1,
            "memberships_total": 3,
            "realization_claims_total": 9,
            "advertised_expansions_total": 0,
            "primary_items_total": 16,
            "primary_items_returned": 8,
            "primary_items_remaining": 8,
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
          "complete": false,
          "counts": {
            "invariant_revisions_total": 3,
            "family_revisions_total": 1,
            "memberships_total": 3,
            "realization_claims_total": 11,
            "advertised_expansions_total": 0,
            "primary_items_total": 18,
            "primary_items_returned": 4,
            "primary_items_remaining": 14,
            "distinct_source_locations_total": 11,
            "distinct_source_paths_total": 9,
            "unresolved_anchor_total": 0
          }
        }
      }
    ]
  },
  "page": {
    "collection": "family_members",
    "state": "continued",
    "returned": 8,
    "remaining": 8,
    "total": 16,
    "total_basis": "selection",
    "scope": [
      "side=before",
      "family_revision_id=69927d22-e430-55b2-8f31-f84e01534db1",
      "policy_version=recorded-family-frontier/v1",
      "page_size=4"
    ],
    "continuation.fieldPresent": true,
    "continuation.nonNull": true,
    "continued_from.fieldPresent": true,
    "continued_from.nonNull": true
  }
}
```

#### Recorded state block 5

```json
{
  "jsonPath": "$[\"before\"][1][\"payload\"][\"source\"][\"inventory\"]",
  "state": "measured",
  "entries.count": 179
}
```

#### Recorded state block 6

```json
{
  "jsonPath": "$[\"before\"][1][\"payload\"][\"family_context\"]",
  "state": "partial",
  "entries.count": 1
}
```

### Reading boundary

Missing fields are not converted into zero counts. Present state, measured population, carried page and continuation-field presence remain separate observations; an opaque cursor is not decoded or called admitted here. Synthetic overlays in consuming tests require their own disclosure and do not turn this recorded body into fresh native or browser acceptance. Regeneration belongs to the source/capture owner; old fixture descriptions below are not instructions to fabricate successful response bytes.

## Previous Input Account — Historical Only

The following account describes the preceding fixture bytes, receipts and consuming-test scope. Its present-tense clauses, measurements and numeric reference labels are historical, not current guarantees or live citations. The actual current input shape is recorded above; general design context is retained here rather than discarded.

> # dashboard/src/panels/review/familyPaging.captured.json
>
> ## Governing Overview
>
> [panels route overview](../overview.md)
>
> ## Purpose
>
> Retain complete real HTTP review responses for a bounded two-sided family walk, so mounted client regressions consume the production wire shape.
>
> ## Code Commentary
>
> ### Logic
>
> The document identifies one selected subject and family, then stores three before-walk and three after-walk bodies. They were captured through the public-authored family scenario and real HTTP continuation helper at page size four. **MIK-L31 re-captured them from the current route** (MIK-R31 rule 6, the L44-R1-F5 remainder; L44's producer, first build accepted, one attempt; the receipt's `mik_l31_recapture` row, requests `paging1-paging-before-0` to `paging1-paging-after-2`), so the member sources now carry `locator`, `resolved_ranges` and `locator_state`. On this draw the before walk reads 11 items in three bodies (the last with nothing remaining) and the after walk 9. Family order follows the stored identities each build draws afresh, so the late-source case of `ReviewReadCycle.family.test.tsx` opens the subject inside this document's own `family_id` explicitly. Content, memberships and claims can appear on different pages; another side's response can repeat its first page. Those are the cases the read-cycle test must preserve.
>
> ### Conventions
>
> Regenerate through the existing scenario and HTTP walk helper when the wire contract changes. Do not hand-edit successful response bodies to manufacture an expected display. Deliberate negative mutations belong in the consuming test and are explicitly asserted as failures.
>
> ### Invariants And Boundaries
>
> These are regression fixture records, not the project's published knowledge database, a new selection authority or installed-browser evidence. The complete response keeps comparison, subject, family, source and evidence dimensions available to the real client.
>
> ### Todos
>
> None recorded.
>
> ## Evidence
>
> ### Docs References
>
> No Domain Documentation source is configured; the capture's producer and consumer are repository source.
>
> No configured domain source could be checked.
>
> ### Repo-Internal References
>
> The document's identifiers and walks are paired with the existing real-route producer and mounted consumer.
>
> - The fixture names its exact selected family, subject and before walk. (historical reference 1)
> - The second collection holds the after-side walk. (historical reference 2)
> - The receipt row for this document in the MIK-L31 re-capture. (historical reference 3)
> - The producer follows published HTTP cursors under one fixed bound. (historical reference 4)
> - The consumer reads the complete captured bodies before mounting the actual read cycle. (historical reference 5)
>
> ### Cross-Repo References
>
> No external repository boundary is introduced.
>
> No cross-repository reference is required.

## Evidence

### Repo-Internal References

- The current retained JSON input supplies the literal identities, response states and populations summarized above; these are fixture facts, not live project knowledge or fresh execution evidence. [6]
