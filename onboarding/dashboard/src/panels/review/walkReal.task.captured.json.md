# dashboard/src/panels/review/walkReal.task.captured.json

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
    "leaf_id": "260928-MIK-L33",
    "task_ref": "260928_maintained-invariant-knowledge"
  },
  "knowledge": {
    "selection_state": "task_context"
  },
  "judgment": {
    "state": "unavailable",
    "detail": "No knowledge subject was selected for this review",
    "rows.count": 0,
    "proofs.count": 0
  },
  "family_context": {
    "state": "no_subject_selected",
    "families_total": 0,
    "families_returned": 0,
    "families_remaining": 0,
    "membership_rows_total": 0,
    "unique_member_revision_total": 0,
    "entries.count": 0,
    "sides": []
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
  "state": "no_subject_selected",
  "entries.count": 0
}
```

### Reading boundary

Missing fields are not converted into zero counts. Present state, measured population, carried page and continuation-field presence remain separate observations; an opaque cursor is not decoded or called admitted here. Synthetic overlays in consuming tests require their own disclosure and do not turn this recorded body into fresh native or browser acceptance. Regeneration belongs to the source/capture owner; old fixture descriptions below are not instructions to fabricate successful response bytes.

## Previous Input Account — Historical Only

The following account describes the preceding fixture bytes, receipts and consuming-test scope. Its present-tense clauses, measurements and numeric reference labels are historical, not current guarantees or live citations. The actual current input shape is recorded above; general design context is retained here rather than discarded.

> # dashboard/src/panels/review/walkReal.task.captured.json
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> The task-context review (`GET /api/review/intent` with no subject) of leaf `260928-MIK-L33`, as served.
>
> ## Code Commentary
>
> ### What the body holds
>
> - `state` is `review` with `selection_state` `task_context`. The family context is `no_subject_selected` with no family.
> - The source inventory lists 4 changed files.
> - The limitations name `review:trees:1`, so the review is a tree comparison.
>
> ### Use
>
> `walk.test-utils.tsx` serves it for every review request that names no subject.
>
> ### Boundaries
>
> - The body is one captured answer of the route. Its receipt is `walkReal.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (15,110 bytes).
> - The body is a served answer over a scratch copy: shared clones of the code repository at `e40d1f21` and of the converted memory repository at `40ae8395`, with the scratch leaf 260928-MIK-L33 that carries four scratch code edits and five scratch-authored curator edits (the receipt's `scratch` field). It is not current project knowledge; its identifiers, blobs and paths are the scratch copy's.
>
> ## Evidence
>
> - The served answer, whole. (historical reference 1)
> - Its receipt row: route, parameters, status, hash and size. (historical reference 2)

## Evidence

### Repo-Internal References

- The current retained JSON input supplies the literal identities, response states and populations summarized above; these are fixture facts, not live project knowledge or fresh execution evidence. [3]
