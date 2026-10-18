# dashboard/src/panels/review/triage.shared.captured.json

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
      "record_id": "e701c262-50a6-553b-bab6-691caed0fb04",
      "state": "compared",
      "before_revision_id": "848ff4da-c662-5358-be3b-9c284578a825",
      "after_revision_id": "848ff4da-c662-5358-be3b-9c284578a825",
      "before_heads": [
        "848ff4da-c662-5358-be3b-9c284578a825"
      ],
      "after_heads": [
        "848ff4da-c662-5358-be3b-9c284578a825"
      ],
      "before_retained": [
        "848ff4da-c662-5358-be3b-9c284578a825"
      ],
      "after_retained": [
        "848ff4da-c662-5358-be3b-9c284578a825"
      ],
      "statement": "the invariant e701c262-50a6-553b-bab6-691caed0fb04 comparison uses the before revision 848ff4da-c662-5358-be3b-9c284578a825 and the after revision 848ff4da-c662-5358-be3b-9c284578a825, each recorded by its own memory tree"
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
    "families_total": 2,
    "families_returned": 2,
    "families_remaining": 0,
    "membership_rows_total": 22,
    "unique_member_revision_total": 11,
    "entries.count": 2,
    "sides": [
      {
        "family_id": "338785bb-9701-50e9-a383-ff33746d5bc0",
        "side": "before",
        "state": "recorded",
        "members_total": 8,
        "members.count": 8,
        "page": {
          "state": "first_page",
          "complete": true,
          "counts": {
            "invariant_revisions_total": 8,
            "family_revisions_total": 1,
            "memberships_total": 8,
            "realization_claims_total": 7,
            "advertised_expansions_total": 1,
            "primary_items_total": 25,
            "primary_items_returned": 25,
            "primary_items_remaining": 0,
            "distinct_source_locations_total": 5,
            "distinct_source_paths_total": 2,
            "unresolved_anchor_total": 1
          }
        }
      },
      {
        "family_id": "338785bb-9701-50e9-a383-ff33746d5bc0",
        "side": "after",
        "state": "recorded",
        "members_total": 9,
        "members.count": 9,
        "page": {
          "state": "first_page",
          "complete": true,
          "counts": {
            "invariant_revisions_total": 9,
            "family_revisions_total": 1,
            "memberships_total": 9,
            "realization_claims_total": 7,
            "advertised_expansions_total": 2,
            "primary_items_total": 28,
            "primary_items_returned": 28,
            "primary_items_remaining": 0,
            "distinct_source_locations_total": 4,
            "distinct_source_paths_total": 2,
            "unresolved_anchor_total": 2
          }
        }
      },
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
  "entries.count": 2
}
```

### Reading boundary

Missing fields are not converted into zero counts. Present state, measured population, carried page and continuation-field presence remain separate observations; an opaque cursor is not decoded or called admitted here. Synthetic overlays in consuming tests require their own disclosure and do not turn this recorded body into fresh native or browser acceptance. Regeneration belongs to the source/capture owner; old fixture descriptions below are not instructions to fabricate successful response bytes.

## Previous Input Account — Historical Only

The following account describes the preceding fixture bytes, receipts and consuming-test scope. Its present-tense clauses, measurements and numeric reference labels are historical, not current guarantees or live citations. The actual current input shape is recorded above; general design context is retained here rather than discarded.

> # dashboard/src/panels/review/triage.shared.captured.json
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> **The shared member INV-FFFFFF's review** (`selectorKind=invariant`, 167,361 bytes; test evidence for
> `changeTriage.test.ts` and `FamilyTree.triage.test.tsx`: one member in two families).
>
> ## Code Commentary
>
> ### Logic
>
> - Two families: FAM-F00001 (guarantee `unchanged`, INV-FFFFFF `unchanged`) and FAM-F00002 (guarantee `intent`: its
>   guarantee text changed; INV-FFFFFF `membership` where it joined, INV-PPPPPP `intent` with `text_differs`, INV-EEEEEE
>   `unchanged`).
>
> ### Conventions
>
> Keep the captured bytes and their receipt intact; a recapture rewrites both.
>
> ### Invariants And Boundaries
>
> The body is served over the SYNTHETIC store-authored world of `mcp/tests/test_review_change_kinds.py` (`build_world`: a live leaf `260101-TRV-L1` of master `260101_tree_review` over four real Git trees), not current project knowledge; its identities, blobs and scratch paths are that world's.
>
> ### Todos
>
> No additional work is asserted by this card.
>
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
> - Both families' facts: unchanged in one, membership where it joined, the revised guarantee. (historical reference 1)
> - The receipt row for this body. (historical reference 2)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.

## Evidence

### Repo-Internal References

- The current retained JSON input supplies the literal identities, response states and populations summarized above; these are fixture facts, not live project knowledge or fresh execution evidence. [3]
