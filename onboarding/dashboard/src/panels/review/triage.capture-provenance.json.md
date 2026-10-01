# dashboard/src/panels/review/triage.capture-provenance.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The receipt of the seven store-authored bodies MIK-L33 captured for its triage tests.** It names the capture time
(2026-09-30T19:15:19Z, the merge round), the producer (`notes/reports/260928-MIK-L33-evidence/capture_fixture_bodies.py`,
task-local evidence outside the repository) and its command, the route (`create_app(config,
collaborators=serving_collaborators(config))` over a FastAPI `TestClient`), the source tree (the L33 worktree on base
`d3a22213`, MIK-L34 landed, with this leaf's changes), the comparison (the STORE-AUTHORED world of
`mcp/tests/test_review_change_kinds.py`), the attempts (one capture per body, each the first answer), one row per body
with route, parameters, status, seconds, sha256 and bytes, and a `merge_round` note: re-captured over the merged tree
because each body's facts now carry `membership_reasons` apart from `unknown_reasons`.

## Code Commentary

### Logic

- Seven rows: the subject catalogue (`GET /api/review/intent/entries`), FAM-F00001's family review (whole, and with
  `pageSize=2` plus its `family_members` continuation), the shared member INV-FFFFFF's review (`triage.shared`), and
  the member reviews of INV-AAAAAA (`memberA`) and INV-HHHHHH (`memberH`).
- The store-authored bodies were re-captured in fresh Git repositories in each round; their change facts and member
  rows were identical between captures (the worker's `recapture-compare*.txt`), while scratch-dependent ids such as
  `before_code_tree_id`, digests and continuation cursors differ.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

These are captures of a SYNTHETIC test-fixture world, not current project knowledge. All seven sha256 values and byte counts match the bodies (checked by this curation).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- When, by what command, at which source tree and over which comparison the bodies were captured. [1]
- One receipt row per body, and the merge-round note. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
