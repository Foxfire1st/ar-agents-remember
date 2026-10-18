# dashboard/src/panels/review/familyReview.oneSided.captured.json

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
      "record_id": "2d1f7c95-81e0-5eda-8fa0-e3cf24cacfab",
      "state": "added",
      "after_revision_id": "510079af-10c5-5ade-beac-d8202cb88198",
      "before_heads": [],
      "after_heads": [
        "510079af-10c5-5ade-beac-d8202cb88198"
      ],
      "before_retained": [],
      "after_retained": [
        "510079af-10c5-5ade-beac-d8202cb88198"
      ],
      "statement": "the before snapshot retains no revision of the family 2d1f7c95-81e0-5eda-8fa0-e3cf24cacfab, so the after revision 510079af-10c5-5ade-beac-d8202cb88198 is shown as an addition under the one-sided contract"
    }
  },
  "judgment": {
    "state": "rows",
    "detail": "The leaf's recorded judgments in attempt order.",
    "rows.count": 1,
    "proofs.count": 18
  },
  "family_context": {
    "state": "partial",
    "families_total": 1,
    "families_returned": 1,
    "families_remaining": 0,
    "membership_rows_total": 6,
    "unique_member_revision_total": 6,
    "entries.count": 1,
    "sides": [
      {
        "family_id": "2d1f7c95-81e0-5eda-8fa0-e3cf24cacfab",
        "side": "before",
        "state": "not_recorded",
        "members_total": 0,
        "members.count": 0
      },
      {
        "family_id": "2d1f7c95-81e0-5eda-8fa0-e3cf24cacfab",
        "side": "after",
        "state": "recorded",
        "members_total": 6,
        "members.count": 6,
        "page": {
          "state": "first_page",
          "complete": false,
          "counts": {
            "invariant_revisions_total": 6,
            "family_revisions_total": 1,
            "memberships_total": 6,
            "realization_claims_total": 38,
            "advertised_expansions_total": 0,
            "primary_items_total": 51,
            "primary_items_returned": 27,
            "primary_items_remaining": 24,
            "distinct_source_locations_total": 37,
            "distinct_source_paths_total": 19,
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

> # dashboard/src/panels/review/familyReview.oneSided.captured.json
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> One **captured route answer body**: the bytes the intent-review route published for one real enclosure,
> **re-captured by MIK-L31 from the current route** (MIK-R31 rule 6, the L44-R1-F5 remainder) with L44's producer,
> first build accepted, and installed as the fixture the family workspace case stubs `fetch` with. **45,874 bytes;
> sha256 `16e24767eb5556bd238ff195b8a6714b8ff82e3b05a9f1a5dde2f0783d3ad134`**, as its row in
> `familyReview.capture-provenance.json` (`mik_l31_recapture`) records. It is the `one-sided1-one-sided` request: the
> `retry-and-anchor-family` before-side cursor of a page-size-1 read, continued at page size 4.
>
> It is data with a provenance chain, not an assembled fixture: the case stubs **only `fetch`** and lets the real
> client, the shared decode and the real component tree read these bytes. It is **not browser evidence**.
>
> The envelope is the review read (`state: "review"`, `operation: "read_knowledge_review"`,
> `surface_version: "knowledge-review-surface/1"`) over the fixture enclosure (`leaf_id: "260921-icr-l1"`,
> master/task_ref `review-source-endpoints-fixture`) with the per-run fixture repository uuid normalized
> to `<repository_id>`.
>
> **What this body pins: the one membership row that a single snapshot records, whose revision content this page did
> not carry.** Exactly one row in the whole body carries the page-scoped uncarried state, and the other snapshot does
> not list that revision at all, which is why the case can address the row in the singular and why the sentence it
> must produce is a fact about the **page** — never the one-sided comparison wrapper, and never "the snapshot records
> no row".
>
> ## Code Commentary
>
> ### Logic
>
> **The body is a continued page of the before side's walk.** `payload.page` is `collection: "family_members"`,
> `state: "continued"`, `returned` 5, `remaining` 6, `total` 11 on `total_basis: "selection"`, with `continued_from`
> (position 1) and `continuation` cursors and a scope naming `side=before`, family revision `f20547ca…` and
> `page_size=4`. The family context is `partial` with two families, `membership_rows_total` 8 and
> `unique_member_revision_total` 4; every side carried both of its 2 recorded rows.
>
> **The uncarried row is the whole reason this file exists.** `retry-and-anchor-family`'s before side lists member
> `9b397d0d-93ab-4c8b-949a-546685c06e31` (`anchor-identity-preservation`, revision
> `dccb2d50-628c-4f00-aa46-e3ba98c46874`) with state `content_not_on_page`. The after side of that family (revision
> `a98b9149…`) lists two recorded rows and does **not** list `dccb2d50…` at all. So for that member no side this page
> reached carried content: the comparison is `not_on_page`, and the only truthful sentence is the page-scoped one.
>
> **The same body carries the other one-snapshot fact, outside the family context.** `source.unresolved` holds exactly
> **two** rows (references `0133d688-6f67-467a-a24a-68b587b602c3` and `2c2e8b4a-d6c9-4d69-8a0f-c397336befca`), each
> with the owner's sentence "this record is held by one snapshot and was not reached by the other side's declared
> selection; it is displayed as present outside the selection and never as a deletion". That is a different owner's
> fact from the member row above and must not be merged with it.
>
> **What a reader must NOT look for in this body.** Every family side is `state: "recorded"` and carries a
> guarantee, so the guarantee-level `one_sided` and `unrecorded` shapes are not composed here. This body's
> one-sidedness is the member row and the two unresolved attribution rows.
>
> **One case drives these bytes, and it asserts the boundary in four directions.** It takes the single row carrying
> `review-family-member-state`, clicks that row's opener, and asserts the centre shows the not-on-page statement
> containing "did not carry the revision content" while the one-sided, unchanged and changed member blocks are all
> **absent**. The sibling `walkFinal` body carries eleven uncarried rows and could not be driven this way, and the
> sibling `continued` body's uncarried row is listed by **both** sides.
>
> ### Conventions
>
> - Captured bytes, never hand-edited: the provenance is the receipt's `mik_l31_recapture` row.
> - One JSON document, minified to a **single line** with sorted keys. Every reference row below cites the
>   whole file (`:1-1`) and names the exact key path and value in the finding.
> - The body is opaque data to this client: the case types it `unknown` and narrows it at runtime.
> - Numbers on this card are the file's; the identities are one draw of the scenario builder.
>
> ### Invariants And Boundaries
>
> - **A row whose content no reached side carried is a statement about the page.** It is not a deletion,
>   not an absence from a snapshot, and not a one-sided comparison.
> - **`content_not_on_page` is the state the whole distinction rests on.** The membership row **is**
>   recorded; only its revision content fell outside the page.
> - **One snapshot holding a record is its own published fact** on `source.unresolved`, and it is not evidence that
>   the other snapshot deleted anything.
> - **No conclusion is carried anywhere in the body**, and **not browser evidence**.
>
> ### Todos
>
> None recorded.
>
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured for this repository (`system/sources.md` carries no
> `Domain Documentation` entries). The statements below are grounded in repository source only.
>
> No configured domain documentation could be checked.
>
> ### Repo-Internal References
>
> Every row was re-derived against the MIK-L31 re-capture, and every anchor in a row occurs on the line the row
> cites. Because each captured body is one minified line, the cited range is the whole file and the finding names the
> exact key path and value a reader can re-check.
>
> - **The envelope: the one review read the surface makes, its surface version, and its state.** (historical reference 1)
> - **The enclosure the bytes were recorded over, the one normalization, and the scratch directory the capture ran in.** (historical reference 2)
> - **The page block: a continued page of the before side's walk, with its returned/remaining/total arithmetic and its scope.** (historical reference 3)
> - **The family context and its counts.** (historical reference 4)
> - **The one uncarried row of the whole body: its revision and member identities, and the state that says the row is recorded while its content is not on the page.** (historical reference 5)
> - **The other one-snapshot fact: two unresolved attribution rows, each a record held by one snapshot displayed as present outside the selection.** (historical reference 6)
> - **The receipt row for this file in the MIK-L31 re-capture.** (historical reference 7)
> - The one constant that binds this body to its case, and the runtime narrowing. (historical reference 8)
> - **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** (historical reference 9)
> - **The case this body exists for: it addresses the single uncarried row, reads the page-scoped statement, and refuses all three comparison wrappers.** (historical reference 10)
> - **The derivation that decides this row: a member comparison falls to the one-sided helper, and nothing carried means `not_on_page` while exactly one carried means `one_sided`.** (historical reference 11)
> - **The row's own page-scoped line in the tree, and the member statement block the centre mounts for it.** (historical reference 12)
> - Roster context does not select a primary statement pair; the subject owner supplies that pair, while an unaddressable member remains context. (historical reference 13)
>
> ### Cross-Repo References
>
> No cross-repository behavior is exercised in this file: it is one recorded response body from this
> repository's own route over this repository's own fixture enclosure.
>
> No meaningful cross-repo references found.

## Evidence

### Repo-Internal References

- The current retained JSON input supplies the literal identities, response states and populations summarized above; these are fixture facts, not live project knowledge or fresh execution evidence. [14]
