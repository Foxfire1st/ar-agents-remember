# dashboard/src/panels/review/walkReal.capture-provenance.json

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Retained capture-custody metadata for the neighbouring test responses.

## Code Commentary

This file is fixture data, not current project knowledge or a new selection authority. Its literal response states and counts belong to the recorded input. Reading it does not execute its producer, validate an installed dashboard, reproduce the capture or grade the present candidate. A provenance field is a recorded custody statement, not an independent observation made by this card.

### Current input shape

- Root keys: `["schema", "captured_at", "producer", "source_tree", "normalization", "scenario", "manifest", "manifest_sha256", "source_hashes_verified", "source_files", "prior_capture_provenance", "fixtures", "limitations", "source_manifest_canonical_sha256", "source_files_scope"]`
- Root collection sizes (physical JSON containers, not gate verdicts): `{"source_files": {"kind": "dict", "count": 6}, "fixtures": {"kind": "list", "count": 17}}`

Declared capture metadata, not a new observation of the run:

```json
{
  "scenario": "Retained lane-D2/R33/setup_leaf.py unchanged; real bases e40d1f21 / 40ae8395; setup four code edits, five curator edits; curate 12 entries, zero unresolved.",
  "captured_at": "2026-10-15T22:42:18.527037+00:00"
}
```
- Structured state blocks (a state beside payload, operation, comparison, cards, worklist, entries or items): 0; the bounded inventory below shows 0. This is a structural inventory, not a producer count. Other values remain available through the whole-file citation.
- This is a receipt/metadata file. Every declared run or overlay, when present, keeps its own metadata; the card neither merges grades nor invents recapture.

### Reading boundary

Missing fields are not converted into zero counts. Present state, measured population, carried page and continuation-field presence remain separate observations; an opaque cursor is not decoded or called admitted here. Synthetic overlays in consuming tests require their own disclosure and do not turn this recorded body into fresh native or browser acceptance. Regeneration belongs to the source/capture owner; old fixture descriptions below are not instructions to fabricate successful response bytes.

## Previous Input Account — Historical Only

The following account describes the preceding fixture bytes, receipts and consuming-test scope. Its present-tense clauses, measurements and numeric reference labels are historical, not current guarantees or live citations. The actual current input shape is recorded above; general design context is retained here rather than discarded.

> # dashboard/src/panels/review/walkReal.capture-provenance.json
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> The receipt of the 16 real served bodies `walkReal.*.captured.json` that the walked-tree tests (requirement MIK-R39) serve to the mounted reviewer. It records when and how the bodies were captured, over which scratch copy, and one row per body with the route, the parameters, the status, the time taken, the `sha256` and the size.
>
> ## Code Commentary
>
> ### The capture
>
> - `captured_at` is 2026-10-04T15:58:35+00:00. The producer is the leaf's worker with `capture_real_bodies.py`; the command starts `serve_scratch.py` with the leaf's `mcp/src` on the Python path and then runs the capture script.
> - `route`: the application's routes registered by `serve_scratch.py` with `serving_collaborators(config)`, over HTTP on `127.0.0.1:18852`.
> - `source_tree`: the `260928-mik-l39` worktree on base `e40d1f21660386f9b091ae5e6fee595a467d4cef`, in which no file under `mcp/` changed.
> - `scratch`: `--shared` clones of the real code repository at `e40d1f21` and of the real memory repository at `40ae8395` (converted), with the leaf 260928-MIK-L33 from lane D2's `setup_leaf.py`: four scratch code edits and five scratch-authored curator edits in the leaf's own worktrees, then its curate step (12 entries re-recorded at the candidate blob).
> - `attempts`: one capture per body; each body is the first answer.
>
> ### The rows
>
> - 14 rows of the first round: the subject catalogue (`entries`); the reviews of the families FAM-R6R095RW and FAM-2HBJREC2; the task-context review (`task`); the unexplained-changes lane (`lane`), the classification of `familyWalkMerge.ts` (`file`) and its source content (`source`); and the reviews of the seven changed members of FAM-R6R095RW: INV-2E8MG43K, INV-ZS9ZS878, INV-555EHWM8, INV-BR5MTSTY, INV-H8EM1VJR, INV-VPX81HXV and INV-2TQGXFAX.
> - 2 rows of the partial round, described by the `partial_round` note (2026-10-04T19:56:00+00:00): the same scratch leaf and route asked with the server's own `pageSize=2`, so a real family is partial. `INV-2TQGXFAX-page2` is the shared member's first page, and `FAM-R6R095RW-continued` continues the cursor that page published for FAM-R6R095RW's before side.
> - Every row's `sha256` and `bytes` match the file it names.
>
> ### Boundaries
>
> These are captures over a scratch copy, not current project knowledge.
>
> ## Evidence
>
> - When, by what command, at which source tree and over which scratch leaf the bodies were captured. (historical reference 1)
> - One receipt row per body. (historical reference 2)
> - The note of the partial round. (historical reference 3)
> - The kit that serves these bodies. (historical reference 4)

## Evidence

### Repo-Internal References

- The current receipt preserves its explicit section names and declared capture custody; reading the metadata does not independently execute or validate any recorded run. [5]
