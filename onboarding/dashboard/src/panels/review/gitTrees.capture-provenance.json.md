# dashboard/src/panels/review/gitTrees.capture-provenance.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/gitTrees.capture-provenance.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:46:54+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The receipt of the four MIK-R25 captured bodies.** It names the capture time, the producer
(`notes/reports/260928-MIK-L25-evidence/capture_ui_fixtures.py`, task-local evidence outside the repository), the
route (`create_app(config, collaborators=serving_collaborators(config))` over a FastAPI `TestClient`), the scratch
(`/tmp/mik-l25-real`, `--shared` clones, the memory converted with the leaf's own `knowledge-convert` at
`a4eba7b7`), and one row per fixture with its route, status, sha256 and bytes.

## Code Commentary

### Logic

- Four rows: `gitTrees.entries.captured.json` (`GET /api/review/intent/entries`), `gitTrees.family.captured.json`
  and `gitTrees.invariant.captured.json` (`GET /api/review/intent`), and `data/reviewTrees.captured.json`
  (`GET /api/review/trees`).
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
| When and by what the bodies were captured, and over which scratch. | "captured_at"; "scratch" | dashboard/src/panels/review/gitTrees.capture-provenance.json:2-5 |
| One receipt row per captured body. | "fixtures" | dashboard/src/panels/review/gitTrees.capture-provenance.json:6-35 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new capture receipt. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
