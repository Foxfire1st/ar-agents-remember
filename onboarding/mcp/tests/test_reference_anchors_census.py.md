# mcp/tests/test_reference_anchors_census.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_reference_anchors_census.py` pins the reference census under MIK-R198 rules 1 and 2: the one reproducible measurement the leaf reports and the curator's work order. Its classification and its repair promise are fixed exactly — a stale blob whose bytes hold, a uniquely moved range, and the judgment shapes the mechanical fixer must refuse — and every case resolves through the product's own anchor resolver.

## Code Commentary

Sidecars are authored from the test support's `tree`/`encode` helpers with an anchor built from `git_blob_id` and the product's `content_identity`, so no anchor is hand-spelled. Classification is read from `observations` one target at a time and from `census` as a whole. Class (a) is a stale blob whose recorded content still holds; class (b) is a range the shipped rule re-records, including a recorded range past the shortened file. Judgment covers a same-blob anchor with the wrong locator (the fixer refreshes nothing when the blob already matches), an ambiguous repeated range, changed bytes with no identical same-length range, a changed whole-file identity, and distinct unresolved-symbol versus absent-path names. The parity case is bidirectional against `refreshed_anchor`, so the census can neither promise a repair the fixer cannot make nor send a repairable anchor to judgment. Input-completeness cases keep a readable-but-misplaced sidecar and an accepted sidecar that declares the rejected file's path from restoring `ok: true` over a denominator of zero. Row cases require each target's recorded content identity and the source-route totals to reconcile to the denominator.

## Evidence

- A current anchor is the only zero-debt state [1]
- A stale blob whose recorded bytes hold is class (a) [2]
- A uniquely moved line range is class (b) and names where it is re-recorded [3]
- A same-blob anchor with a wrong locator is judgment because the shipped fixer refuses it [4]
- Mechanical repair is claimed exactly where the shipped fixer repairs, in both directions [5]
- A readable sidecar the tree parser refused is named and the census is not reported complete [6]
- An accepted sidecar cannot alias a rejected one out of the accounting [7]
