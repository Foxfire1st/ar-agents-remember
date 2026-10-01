# dashboard/src/panels/review/hunkMarkers.capture-provenance.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The receipt of the one body set MIK-L34 captured for its marker-model and renderer tests.** It names the capture time
(2026-09-30T13:41:23Z), the producer (`notes/reports/260928-MIK-L34-evidence/capture_classifier_fixtures.py`,
task-local evidence outside the repository) and its command, the route (`GET /api/review/trees?comparison=1&file=<path>`
through `register_review_trees_route` over `review_tree_knowledge._file_view`, that is MIK-L32's
`classify_changed_path`, on a FastAPI `TestClient`), the source tree (the L34 worktree on base `59daf505`; the
classifier is L32's, unchanged by this leaf), the world (MIK-L32's lane fixture in `mcp/tests/test_review_unexplained_lane.py`:
code base and candidate, converted memory, families before `{FAM-F00001:[A], FAM-F00002:[A], FAM-F00003:[A]}` and after
`{FAM-F00001:[A], FAM-F00002:[B]}`), the two scratch-authored realizations of the `curated` and `before_unread`
scenarios (RLZ-A00010 and RLZ-C00010), the six scenarios and their files, and the one body file with its sha256 and
bytes.

## Code Commentary

### Logic

- Six scenarios, eleven file bodies: `precuration` (`pkg/lines.txt`, `pkg/a.py`, `tests/test_a.py`, `pkg/new.py`,
  `pkg/stale.py`), `curated` (`lines.txt`, `a.py`), `before_unread` (`a.py`, `lines.txt`), `after_unread` (`a.py`),
  `both_unread` (`a.py`) and `partial` (`lines.txt`).
- Each body's `texts` field is fixture-only, not a route field: the exact side blob texts, read with `git cat-file` at
  the blobs the classification names, so the renderer tests draw exactly the classified text.
- One capture per body, each the first answer; 1.26 s in all.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

These are scratch captures of a test fixture world, not current project knowledge. The sha256 and byte count match
the body file (checked by this curation).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- When, by what command, at which source tree and over which world the bodies were captured. [1]
- The six scenarios and their files, and the body file's digest. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
