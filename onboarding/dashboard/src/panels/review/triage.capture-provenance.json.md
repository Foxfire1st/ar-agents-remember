# dashboard/src/panels/review/triage.capture-provenance.json

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Retained capture-custody metadata for the neighbouring test responses.

## Code Commentary

This file is fixture data, not current project knowledge or a new selection authority. Its literal response states and counts belong to the recorded input. Reading it does not execute its producer, validate an installed dashboard, reproduce the capture or grade the present candidate. A provenance field is a recorded custody statement, not an independent observation made by this card.

### Current input shape

- Root keys: `["schema", "captured_at", "producer", "source_tree", "normalization", "scenario", "manifest", "manifest_sha256", "source_hashes_verified", "source_files", "prior_capture_provenance", "fixtures", "limitations", "source_manifest_canonical_sha256", "source_files_scope", "continuation_correction_receipt"]`
- Root collection sizes (physical JSON containers, not gate verdicts): `{"source_files": {"kind": "dict", "count": 6}, "fixtures": {"kind": "list", "count": 7}}`

Declared capture metadata, not a new observation of the run:

```json
{
  "scenario": "Canonical STORE-AUTHORED synthetic test fixture, not real user data; unmodified mcp/tests/test_review_change_kinds.py::build_world over four Git trees",
  "captured_at": "2026-10-15T22:42:18.580612+00:00"
}
```
- Structured state blocks (a state beside payload, operation, comparison, cards, worklist, entries or items): 0; the bounded inventory below shows 0. This is a structural inventory, not a producer count. Other values remain available through the whole-file citation.
- This is a receipt/metadata file. Every declared run or overlay, when present, keeps its own metadata; the card neither merges grades nor invents recapture.

### Reading boundary

Missing fields are not converted into zero counts. Present state, measured population, carried page and continuation-field presence remain separate observations; an opaque cursor is not decoded or called admitted here. Synthetic overlays in consuming tests require their own disclosure and do not turn this recorded body into fresh native or browser acceptance. Regeneration belongs to the source/capture owner; old fixture descriptions below are not instructions to fabricate successful response bytes.

## Previous Input Account — Historical Only

The following account describes the preceding fixture bytes, receipts and consuming-test scope. Its present-tense clauses, measurements and numeric reference labels are historical, not current guarantees or live citations. The actual current input shape is recorded above; general design context is retained here rather than discarded.

> # dashboard/src/panels/review/triage.capture-provenance.json
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> **The receipt of the seven store-authored bodies MIK-L33 captured for its triage tests.** It names the capture time
> (2026-09-30T19:15:19Z, the merge round), the producer (`notes/reports/260928-MIK-L33-evidence/capture_fixture_bodies.py`,
> task-local evidence outside the repository) and its command, the route (`create_app(config,
> collaborators=serving_collaborators(config))` over a FastAPI `TestClient`), the source tree (the L33 worktree on base
> `d3a22213`, MIK-L34 landed, with this leaf's changes), the comparison (the STORE-AUTHORED world of
> `mcp/tests/test_review_change_kinds.py`), the attempts (one capture per body, each the first answer), one row per body
> with route, parameters, status, seconds, sha256 and bytes, and a `merge_round` note: re-captured over the merged tree
> because each body's facts now carry `membership_reasons` apart from `unknown_reasons`.
>
> ## Code Commentary
>
> ### Logic
>
> - Seven rows: the subject catalogue (`GET /api/review/intent/entries`), FAM-F00001's family review (whole, and with
>   `pageSize=2` plus its `family_members` continuation), the shared member INV-FFFFFF's review (`triage.shared`), and
>   the member reviews of INV-AAAAAA (`memberA`) and INV-HHHHHH (`memberH`).
> - The store-authored bodies were re-captured in fresh Git repositories in each round; their change facts and member
>   rows were identical between captures (the worker's `recapture-compare*.txt`), while scratch-dependent ids such as
>   `before_code_tree_id`, digests and continuation cursors differ.
>
> ### Conventions
>
> Keep the captured bytes and their receipt intact; a recapture rewrites both.
>
> ### Invariants And Boundaries
>
> These are captures of a SYNTHETIC test-fixture world, not current project knowledge. All seven sha256 values and byte counts match the bodies (checked by this curation).
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
> - When, by what command, at which source tree and over which comparison the bodies were captured. (historical reference 1)
> - One receipt row per body, and the merge-round note. (historical reference 2)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.

## Evidence

### Repo-Internal References

- The current receipt preserves its explicit section names and declared capture custody; reading the metadata does not independently execute or validate any recorded run. [3]
