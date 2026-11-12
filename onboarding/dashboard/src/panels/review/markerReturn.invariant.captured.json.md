# dashboard/src/panels/review/markerReturn.invariant.captured.json

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
    "master": "260928_maintained-invariant-knowledge",
    "leaf_id": "260928-MIK-L34",
    "task_ref": "260928_maintained-invariant-knowledge"
  },
  "knowledge": {
    "selection_state": "subject_selected",
    "revision_selection": {
      "record_kind": "invariant",
      "record_id": "c7c5be49-164f-56e0-923d-fb5f5259d80c",
      "state": "compared",
      "before_revision_id": "a1c28709-da32-5ca3-91c4-5e43f5c498da",
      "after_revision_id": "a1c28709-da32-5ca3-91c4-5e43f5c498da",
      "before_heads": [
        "a1c28709-da32-5ca3-91c4-5e43f5c498da"
      ],
      "after_heads": [
        "a1c28709-da32-5ca3-91c4-5e43f5c498da"
      ],
      "before_retained": [
        "a1c28709-da32-5ca3-91c4-5e43f5c498da"
      ],
      "after_retained": [
        "a1c28709-da32-5ca3-91c4-5e43f5c498da"
      ],
      "statement": "the invariant c7c5be49-164f-56e0-923d-fb5f5259d80c comparison uses the before revision a1c28709-da32-5ca3-91c4-5e43f5c498da and the after revision a1c28709-da32-5ca3-91c4-5e43f5c498da, each recorded by its own memory tree"
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
    "membership_rows_total": 9,
    "unique_member_revision_total": 5,
    "entries.count": 1,
    "sides": [
      {
        "family_id": "8519c70b-92ae-5ad6-9c6c-2fcf83d498ea",
        "side": "before",
        "state": "recorded",
        "members_total": 5,
        "members.count": 5,
        "page": {
          "state": "first_page",
          "complete": true,
          "counts": {
            "invariant_revisions_total": 5,
            "family_revisions_total": 1,
            "memberships_total": 5,
            "realization_claims_total": 7,
            "advertised_expansions_total": 0,
            "primary_items_total": 18,
            "primary_items_returned": 18,
            "primary_items_remaining": 0,
            "distinct_source_locations_total": 6,
            "distinct_source_paths_total": 1,
            "unresolved_anchor_total": 0
          }
        }
      },
      {
        "family_id": "8519c70b-92ae-5ad6-9c6c-2fcf83d498ea",
        "side": "after",
        "state": "recorded",
        "members_total": 4,
        "members.count": 4,
        "page": {
          "state": "first_page",
          "complete": true,
          "counts": {
            "invariant_revisions_total": 4,
            "family_revisions_total": 1,
            "memberships_total": 4,
            "realization_claims_total": 6,
            "advertised_expansions_total": 0,
            "primary_items_total": 15,
            "primary_items_returned": 15,
            "primary_items_remaining": 0,
            "distinct_source_locations_total": 6,
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
  "entries.count": 4
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

> # dashboard/src/panels/review/markerReturn.invariant.captured.json
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> **A real `GET /api/review/intent` review of INV-Z66EMHMH (selector `c7c5be49…`) on comparison 2 of the MIK-L34 scratch
> leaf** (139,987 bytes; test evidence for `ReviewSurface.markers.test.tsx`: the target a followed marker reads).
>
> ## Code Commentary
>
> ### Logic
>
> - Family context `recorded`: one family, FAM-4V4GSQCS ("Bounded notes listing with unchanged meaning", family id
>   `8519c70b…`), with its before and after revisions and member rosters, so the member row of INV-Z66EMHMH's revision
>   becomes current when the marker is followed.
> - The limitations name `review:trees:2` and both indexes complete.
> - **`change_kinds` (MIK-L33):** guarantee `unchanged`, `members_total` 5; INV-ZJS1XY4R `implementation` `+membership`
>   (reassigned out of the family on the after side; the L210 deletion meets its entry), INV-Z66EMHMH and INV-EJW15DXA
>   `implementation` (the two hunks), INV-QR24S1VH and INV-DA7D417G `unchanged`.
>
> - **Re-captured in MIK-L33's merge round** over the merged tree (MIK-L34 landed; the review route now carries `change_kinds`). Against MIK-L34's capture it differs only by scratch paths, the converted memory commit, timestamps and comparison digests, and it now carries FAM-4V4GSQCS's `change_kinds` (the reviewer's structural diff, review R3 point 5).
>
> ### Conventions
>
> Keep the captured bytes and their receipt intact; a recapture rewrites both.
>
> ### Invariants And Boundaries
>
> The body describes the scratch copies under `/tmp/mik-l33-merge`: MIK-L34's scenario, rebuilt by MIK-L33's merge round with MIK-L34's own scripts (code `59daf505` with the scratch leaf's edits and the same curated blobs `9019bea5` and `b6d07091`; memory `76f5e91e1` converted and committed as scratch `main` `31ab7016`), not current project knowledge; its line numbers, blobs and keys are the scratch tree's.
>
> ### Todos
>
> No additional work is asserted by this card.
>
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
> - The recorded family context with its one family and rosters. (historical reference 1)
> - The comparison token. (historical reference 2)
> - The receipt row for this body. (historical reference 3)
> - The family's change facts (MIK-L33). (historical reference 4)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.

## Evidence

### Repo-Internal References

- The current retained JSON input supplies the literal identities, response states and populations summarized above; these are fixture facts, not live project knowledge or fresh execution evidence. [5]
