# dashboard/src/panels/review/walkReal.FAM-R6R095RW-continued.captured.json

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Retained test input for the review consumers, recording its own response identities, states and bounded populations.

## Code Commentary

This file is fixture data, not current project knowledge or a new selection authority. Its literal response states and counts belong to the recorded input. Reading it does not execute its producer, validate an installed dashboard, reproduce the capture or grade the present candidate. A provenance field is a recorded custody statement, not an independent observation made by this card.

### Current input shape

- Root keys: `["state", "operation", "repository_id", "payload"]`
- Root collection sizes (physical JSON containers, not gate verdicts): `{"payload": {"kind": "dict", "count": 13}}`
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
    "leaf_id": "260928-MIK-L33",
    "task_ref": "260928_maintained-invariant-knowledge"
  },
  "knowledge": {
    "selection_state": "subject_selected",
    "revision_selection": {
      "record_kind": "family",
      "record_id": "b9f95278-5712-5867-aa87-6e225aed4d45",
      "state": "unresolved",
      "before_heads": [],
      "after_heads": [],
      "before_retained": [],
      "after_retained": [],
      "statement": "no revision of the family b9f95278-5712-5867-aa87-6e225aed4d45 was selected on either side, so no pair was established and no statements render as operands"
    }
  },
  "judgment": {
    "state": "none",
    "detail": "This leaf recorded no judgment about this record",
    "rows.count": 0,
    "proofs.count": 0
  },
  "family_context": {
    "state": "partial",
    "families_total": 1,
    "families_returned": 1,
    "families_remaining": 0,
    "membership_rows_total": 47,
    "unique_member_revision_total": 4,
    "entries.count": 1,
    "sides": [
      {
        "family_id": "b9f95278-5712-5867-aa87-6e225aed4d45",
        "side": "before",
        "state": "recorded",
        "members_total": 23,
        "members.count": 2,
        "page": {
          "state": "continued",
          "complete": false,
          "counts": {
            "invariant_revisions_total": 23,
            "family_revisions_total": 1,
            "memberships_total": 23,
            "realization_claims_total": 45,
            "advertised_expansions_total": 0,
            "primary_items_total": 92,
            "primary_items_returned": 4,
            "primary_items_remaining": 88,
            "distinct_source_locations_total": 40,
            "distinct_source_paths_total": 21,
            "unresolved_anchor_total": 0
          }
        }
      },
      {
        "family_id": "b9f95278-5712-5867-aa87-6e225aed4d45",
        "side": "after",
        "state": "recorded",
        "members_total": 24,
        "members.count": 2,
        "page": {
          "state": "first_page",
          "complete": false,
          "counts": {
            "invariant_revisions_total": 24,
            "family_revisions_total": 1,
            "memberships_total": 24,
            "realization_claims_total": 46,
            "advertised_expansions_total": 1,
            "primary_items_total": 96,
            "primary_items_returned": 2,
            "primary_items_remaining": 94,
            "distinct_source_locations_total": 41,
            "distinct_source_paths_total": 22,
            "unresolved_anchor_total": 0
          }
        }
      }
    ]
  },
  "page": {
    "collection": "family_members",
    "state": "continued",
    "returned": 4,
    "remaining": 88,
    "total": 92,
    "total_basis": "selection",
    "scope": [
      "side=before",
      "family_revision_id=0085407b-fd42-584e-adf3-4eaefcb5df98",
      "policy_version=recorded-family-frontier/v1",
      "page_size=2"
    ],
    "continuation.fieldPresent": true,
    "continuation.nonNull": true,
    "continued_from.fieldPresent": true,
    "continued_from.nonNull": true
  }
}
```

#### Recorded state block 2

```json
{
  "jsonPath": "$[\"payload\"][\"source\"][\"inventory\"]",
  "state": "measured",
  "entries.count": 4
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

> # dashboard/src/panels/review/walkReal.FAM-R6R095RW-continued.captured.json
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> The review of the family "Coherent intent and source review" (`GET /api/review/intent`) for leaf `260928-MIK-L33`, as served, continued: the request names `pageOf=family_members`, the server's own `pageSize=2` and the cursor that `walkReal.INV-2TQGXFAX-page2.captured.json` published for this family's before side.
>
> ## Code Commentary
>
> ### What the body holds
>
> - `state` is `review`; the subject is family `b9f95278-5712-5867-aa87-6e225aed4d45`. The family context is `partial` with 1 family.
> - Family "Coherent intent and source review" (state `partial`): 2 of 23 members on the before side and 2 of 24 on the after side. Its guarantee's change kind is `unchanged`, and the change kinds of the 4 member occurrences it describes are 1 `membership`, 3 `unchanged`. The roster pages are not complete (`continued` on the before side, `first_page` on the after side) and each publishes a continuation cursor.
> - The answer is a page of `family_members` in state `continued`.
> - The limitations name `review:trees:1`, so the review is a tree comparison.
>
> ### Use
>
> `ReviewSurface.walkPartial.test.tsx` serves it for every review request that carries a `continuation` parameter (`CONTINUED`).
>
> ### Boundaries
>
> - The body is one captured answer of the route. Its receipt is `walkReal.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (45,881 bytes).
> - The body is a served answer over a scratch copy: shared clones of the code repository at `e40d1f21` and of the converted memory repository at `40ae8395`, with the scratch leaf 260928-MIK-L33 that carries four scratch code edits and five scratch-authored curator edits (the receipt's `scratch` field). It is not current project knowledge; its identifiers, blobs and paths are the scratch copy's.
>
> ## Evidence
>
> - The served answer, whole. (historical reference 1)
> - Its receipt row: route, parameters, status, hash and size. (historical reference 2)

## Evidence

### Repo-Internal References

- The current retained JSON input supplies the literal identities, response states and populations summarized above; these are fixture facts, not live project knowledge or fresh execution evidence. [3]
