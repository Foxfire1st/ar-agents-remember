# dashboard/src/panels/review/walkStore.capture-provenance.json

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Retained capture-custody metadata for the neighbouring test responses.

## Code Commentary

This file is fixture data, not current project knowledge or a new selection authority. Its literal response states and counts belong to the recorded input. Reading it does not execute its producer, validate an installed dashboard, reproduce the capture or grade the present candidate. A provenance field is a recorded custody statement, not an independent observation made by this card.

### Current input shape

- Root keys: `["producer", "comparison", "route", "raw_policy", "argv", "python", "python_version", "import_origin", "source_manifest", "source_manifest_sha256", "scope", "fixtures", "continuation_correction_receipt"]`
- Root collection sizes (physical JSON containers, not gate verdicts): `{"argv": {"kind": "list", "count": 1}, "fixtures": {"kind": "list", "count": 7}}`

Declared capture metadata, not a new observation of the run:

```json
{
  "route": "FastAPI register_review_routes wired by serving_collaborators(world.config), TestClient.get",
  "scope": "Canonical STORE-AUTHORED four-Git-tree fixture through the current public producer; synthetic fixture records, not real user data; raw response bytes unchanged."
}
```
- Structured state blocks (a state beside payload, operation, comparison, cards, worklist, entries or items): 0; the bounded inventory below shows 0. This is a structural inventory, not a producer count. Other values remain available through the whole-file citation.
- This is a receipt/metadata file. Every declared run or overlay, when present, keeps its own metadata; the card neither merges grades nor invents recapture.

### Reading boundary

Missing fields are not converted into zero counts. Present state, measured population, carried page and continuation-field presence remain separate observations; an opaque cursor is not decoded or called admitted here. Synthetic overlays in consuming tests require their own disclosure and do not turn this recorded body into fresh native or browser acceptance. Regeneration belongs to the source/capture owner; old fixture descriptions below are not instructions to fabricate successful response bytes.

## Previous Input Account — Historical Only

The following account describes the preceding fixture bytes, receipts and consuming-test scope. Its present-tense clauses, measurements and numeric reference labels are historical, not current guarantees or live citations. The actual current input shape is recorded above; general design context is retained here rather than discarded.

> # dashboard/src/panels/review/walkStore.capture-provenance.json
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> The receipt of the 7 served bodies `walkStore.*.captured.json` of the store-authored comparison that the walked-tree tests (requirement MIK-R39) use. It records when and how the bodies were captured, over which world, and one row per body with the route, the parameters, the status, the time taken, the `sha256` and the size.
>
> ## Code Commentary
>
> ### The capture
>
> - `captured_at` is 2026-10-04T15:56:14+00:00. The producer is the leaf's worker with `capture_store_bodies.py`, run with `mcp/tests` and `mcp/src` on the Python path.
> - `route`: `create_app(config, collaborators=serving_collaborators(config))` over a FastAPI `TestClient`.
> - `source_tree`: the `260928-mik-l39` worktree on base `e40d1f21660386f9b091ae5e6fee595a467d4cef`, in which no file under `mcp/` changed.
> - `comparison`: a store-authored fixture, `build_world` of `mcp/tests/test_review_change_kinds.py`: a live leaf over four Git trees, every memory side read through its derived index.
> - `attempts`: one capture per body; each body is the first answer.
> - `not_kept`: the same run also captured `walkStore.INV-AAAAAA.captured.json` and `walkStore.INV-HHHHHH.captured.json`. No test loads them, so the two files are not in the tree and the receipt lists no row for them.
>
> ### The rows
>
> All seven rows are of leaf `260101-TRV-L1` of master `260101_tree_review`:
>
> - the subject catalogue (`entries`);
> - the shared member's review (`shared`) and the same review asked with `pageSize=2` (`sharedPage`);
> - the reviews of the families FAM-F00001 and FAM-F00002;
> - the review of the invariant INV-PPPPPP;
> - `FAM-F00001Continued`: the review of FAM-F00001 asked with `pageSize=2`, `pageOf=family_members` and the cursor that `sharedPage` published for that family's before side.
>
> Every row's `sha256` and `bytes` match the file it names.
>
> ### Boundaries
>
> These are captures over a synthetic store-authored world, not current project knowledge.
>
> ## Evidence
>
> - When, by what command, at which source tree and over which world the bodies were captured, and which two captures are not kept. (historical reference 4)
> - One receipt row per body. (historical reference 5)
> - The test file that serves these bodies. (historical reference 6)

## Evidence

### Repo-Internal References

- The current receipt preserves its explicit section names and declared capture custody; reading the metadata does not independently execute or validate any recorded run. [7]
