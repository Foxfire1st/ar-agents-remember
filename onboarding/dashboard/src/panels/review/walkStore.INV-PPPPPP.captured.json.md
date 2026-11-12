# dashboard/src/panels/review/walkStore.INV-PPPPPP.captured.json

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Retained test input for the review consumers, recording its own response identities, states and bounded populations.

## Code Commentary

This file is fixture data, not current project knowledge or a new selection authority. Its literal response states and counts belong to the recorded input. Reading it does not execute its producer, validate an installed dashboard, reproduce the capture or grade the present candidate. A provenance field is a recorded custody statement, not an independent observation made by this card.

### Current input shape

- Root keys: `["state", "operation", "repository_id", "payload"]`
- Root collection sizes (physical JSON containers, not gate verdicts): `{"payload": {"kind": "dict", "count": 12}}`
- Structured state blocks (a state beside payload, operation, comparison, cards, worklist, entries or items): 3; the bounded inventory below shows 3. This is a structural inventory, not a producer count. Other values remain available through the whole-file citation.

#### Recorded state block 1

```json
{
  "jsonPath": "$",
  "state": "review",
  "operation": "read_knowledge_review",
  "candidate": {
    "repository_id": "agents-remember",
    "master": "260101_tree_review",
    "leaf_id": "260101-TRV-L1",
    "task_ref": "260101_tree_review"
  },
  "knowledge": {
    "selection_state": "subject_selected",
    "revision_selection": {
      "record_kind": "invariant",
      "record_id": "a6312ea8-654b-5f11-8f5b-5881ea910b60",
      "state": "compared",
      "before_revision_id": "5c89d1f9-5485-531c-980d-d0abcd2f89a9",
      "after_revision_id": "5c89d1f9-5485-531c-980d-d0abcd2f89a9",
      "before_heads": [
        "5c89d1f9-5485-531c-980d-d0abcd2f89a9"
      ],
      "after_heads": [
        "5c89d1f9-5485-531c-980d-d0abcd2f89a9"
      ],
      "before_retained": [
        "5c89d1f9-5485-531c-980d-d0abcd2f89a9"
      ],
      "after_retained": [
        "5c89d1f9-5485-531c-980d-d0abcd2f89a9"
      ],
      "statement": "the invariant a6312ea8-654b-5f11-8f5b-5881ea910b60 comparison uses the before revision 5c89d1f9-5485-531c-980d-d0abcd2f89a9 and the after revision 5c89d1f9-5485-531c-980d-d0abcd2f89a9, each recorded by its own memory tree"
    }
  },
  "judgment": {
    "state": "none",
    "detail": "This leaf recorded no judgment about this record",
    "rows.count": 0,
    "proofs.count": 0
  },
  "family_context": {
    "state": "recorded",
    "families_total": 1,
    "families_returned": 1,
    "families_remaining": 0,
    "membership_rows_total": 5,
    "unique_member_revision_total": 3,
    "entries.count": 1,
    "sides": [
      {
        "family_id": "6dbf7a49-9dd7-5bc7-8464-845ac0768d44",
        "side": "before",
        "state": "recorded",
        "members_total": 2,
        "members.count": 2,
        "page": {
          "state": "first_page",
          "complete": true,
          "counts": {
            "invariant_revisions_total": 2,
            "family_revisions_total": 1,
            "memberships_total": 2,
            "realization_claims_total": 1,
            "advertised_expansions_total": 1,
            "primary_items_total": 7,
            "primary_items_returned": 7,
            "primary_items_remaining": 0,
            "distinct_source_locations_total": 1,
            "distinct_source_paths_total": 1,
            "unresolved_anchor_total": 0
          }
        }
      },
      {
        "family_id": "6dbf7a49-9dd7-5bc7-8464-845ac0768d44",
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
            "realization_claims_total": 2,
            "advertised_expansions_total": 2,
            "primary_items_total": 11,
            "primary_items_returned": 11,
            "primary_items_remaining": 0,
            "distinct_source_locations_total": 1,
            "distinct_source_paths_total": 1,
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
  "entries.count": 3
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

> # dashboard/src/panels/review/walkStore.INV-PPPPPP.captured.json
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> The review of the invariant INV-PPPPPP (`GET /api/review/intent`) for leaf `260101-TRV-L1`, as served.
>
> ## Code Commentary
>
> ### What the body holds
>
> - `state` is `review`; the subject is invariant `a6312ea8-654b-5f11-8f5b-5881ea910b60`. The family context is `recorded` with 1 family.
> - Family "FAM-F00002" (state `recorded`): 2 of 2 members on the before side and 3 of 3 on the after side. Its guarantee's change kind is `intent`, and the change kinds of the 3 member occurrences it describes are 1 `intent`, 1 `membership`, 1 `unchanged`. Both roster pages are complete and publish no cursor.
> - The limitations name `review:trees:1`, so the review is a tree comparison.
>
> ### Use
>
> `ReviewSurface.walkStore.test.tsx` serves it for the member of the second family only (`MEMBER_P`).
>
> ### Boundaries
>
> - The body is one captured answer of the route. Its receipt is `walkStore.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (58,785 bytes).
> - The body is a served answer over the store-authored world of `mcp/tests/test_review_change_kinds.py` (`build_world`: the live leaf `260101-TRV-L1` of master `260101_tree_review` over four Git trees; the receipt's `comparison` field). It is not current project knowledge; its identifiers and blobs are that world's.
>
> ## Evidence
>
> - The served answer, whole. (historical reference 3)
> - Its receipt row: route, parameters, status, hash and size. (historical reference 4)

## Evidence

### Repo-Internal References

- The current retained JSON input supplies the literal identities, response states and populations summarized above; these are fixture facts, not live project knowledge or fresh execution evidence. [5]
