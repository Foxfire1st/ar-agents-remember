# dashboard/src/panels/review/gitTrees.capture-provenance.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/gitTrees.capture-provenance.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The receipt of the five captured tree-review bodies, re-captured by MIK-L31.** It names the capture time
(2026-09-30T04:18:40Z), the producer (`notes/reports/260928-MIK-L31-evidence/capture_ui_fixtures.py`, task-local
evidence outside the repository) and its command, the route (`create_app(config,
collaborators=serving_collaborators(config))` over a FastAPI `TestClient`), the source tree (the L31 worktree on base
`31d761a2` with the leaf's changes), the scratch (`/tmp/mik-l31-real`: `--shared` clones, memory `b1311393`
converted with the worktree's `knowledge-convert` and committed as scratch `main` with `Code-Commit: 8a2d4b47`; leaf
`260928-MIK-L31` edits `_not_listed`, re-anchors RLZ-CXH58B4W, adds a scratch-authored proof PRF-7Q3M5K and a
history row, and declares two expected effects), the attempts (one capture per body, each the first answer), and
one row per fixture with its route, request parameters, status, seconds, sha256 and bytes. A `tree_note` says the
capture ran at the L10-synced tree and that the later L05 sync touches no review-route module (review R2-4).

## Code Commentary

### Logic

- Five rows: `gitTrees.entries.captured.json` (`GET /api/review/intent/entries`), `gitTrees.family.captured.json`
  and `gitTrees.invariant.captured.json` (`GET /api/review/intent`), `data/reviewTrees.captured.json` (the leaf-wide
  `GET /api/review/trees`), and the new `gitTrees.cards.captured.json` (`GET /api/review/trees` with `comparison=1`
  and the seven member identities of `FAM-2HBJREC2` as `invariants`, 0.12 s, 38,264 bytes). File paths are now
  relative to the dashboard.
- Review F7: the git-trees bodies re-captured after the fix round were byte-identical; only this receipt changed.
- The producer is task-local evidence with an expiry: re-running it later means re-creating an equivalent
  producer.

### Conventions

Keep hashes and byte counts in step with the fixtures; a recapture rewrites both.

### Invariants And Boundaries

These are scratch-copy captures, not current project knowledge or mounted-product acceptance.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` and its rulings
(`25_reviewer-on-git-trees.json`) live outside the code and memory repositories, so they are named here and not
cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| When, by what command and at which source tree the bodies were captured, and over which scratch leaf. | "captured_at"; "scratch"; "source_tree" | dashboard/src/panels/review/gitTrees.capture-provenance.json:2-7 |
| One receipt row per captured body, the cards read's with its seven invariants. | "fixtures"; "gitTrees.cards.captured.json" | dashboard/src/panels/review/gitTrees.capture-provenance.json:9-81 |
| The tree the capture ran at, and why the later sync keeps it representative. | "tree_note" | dashboard/src/panels/review/gitTrees.capture-provenance.json:82-82 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update for the MIK-L31 re-capture: five rows (the new cards read), the producer, command, source tree, scratch leaf, attempts and the `tree_note` (review R2-4 at 06:47:03); F7 recorded. **Claims reworded:** both rows (this pass's generated bullet removed); one row added.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new capture receipt. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
